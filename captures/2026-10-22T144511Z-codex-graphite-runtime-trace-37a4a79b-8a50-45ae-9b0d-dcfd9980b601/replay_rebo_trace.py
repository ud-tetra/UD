"""Replay unmodified REBO forces through an instrumented, version-pinned plugin."""
from pathlib import Path
import sys,ctypes,hashlib,json
import numpy as np
from lammps import lammps
R=Path(__file__).resolve().parent
CASE=sys.argv[1];assert CASE in ('21_dir_0','21_dir_10024')
probe,comp=(34,8) if CASE=='21_dir_0' else (30,4)
a=np.load(R/f'{CASE}_candidate.npz');x=a['positions_A'];B=a['B_extended'];flat=B.reshape(-1,81);direction=B[:,:,probe]
old=np.load(R/'ud-sync/graphite-analysis'/f'{CASE}_ladder_raw.npz')
arch=np.load(R/'ud-sync/graphite-analysis'/f'{CASE}_projected.npz')
ref_rebo1=arch['projected_forces'][list(arch['modes']).index('rebo1')]
assert np.array_equal(old['steps_A'],[8e-5,4e-5,2e-5,1e-5,5e-6,2.5e-6,1.25e-6])
plugin=R/'graphite-trace/rebo_udtrace.so';lib=ctypes.CDLL(str(plugin));lib.ud_trace_count.restype=ctypes.c_size_t;lib.ud_trace_copy.argtypes=[ctypes.POINTER(ctypes.c_double),ctypes.c_size_t];lib.ud_trace_copy.restype=ctypes.c_size_t
pat,name=CASE.split('_',1);data=R/'graphite-target-replay/selected'/pat/name/'struct.inp.data';params=R/'lammps-runtime/lammps/share/lammps/potentials/CH.rebo'
assert hashlib.sha256(params.read_bytes()).hexdigest()=='70b77656397c0468631af41883d3b781f30432189f749eb0c3d724141055cbd4'
l=lammps(cmdargs=['-screen','none','-log',str(R/f'{CASE}_rebo_udtrace.log')]);lref=lammps(cmdargs=['-screen','none','-log',str(R/f'{CASE}_rebo_reference.log')]);records_middle={}
try:
 for c in (f'plugin load {plugin}','units metal','boundary p p p','atom_style full','box tilt large',f'read_data {data}','pair_style hybrid/overlay rebo/udtrace',f'pair_coeff * * rebo/udtrace {params} C NULL','pair_coeff 1 2 none','pair_coeff 2 2 none','neighbor 3.0 nsq','neigh_modify one 4096'):l.command(c)
 for c in ('units metal','boundary p p p','atom_style full','box tilt large',f'read_data {data}','pair_style hybrid/overlay rebo',f'pair_coeff * * rebo {params} C NULL','pair_coeff 1 2 none','pair_coeff 2 2 none','neighbor 3.0 nsq','neigh_modify one 4096'):lref.command(c)
 def sample(t,save=False):
  xx=np.ascontiguousarray(np.asarray(x.astype(np.longdouble)+np.longdouble(t)*direction.astype(np.longdouble),dtype=np.float64))
  l.scatter_atoms('x',1,3,xx.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))
  l.command('run 0 pre yes post no')
  F=np.ctypeslib.as_array(l.gather_atoms('f',1,3),shape=(3*len(x),)).copy();proj=flat.T@F
  count=lib.ud_trace_count();out=np.empty((count,17),dtype=np.float64)
  got=lib.ud_trace_copy(out.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),count);assert got==count
  ids=out[:,:3].astype(np.int64)-1;assert np.all((ids>=0)&(ids<len(x)))
  sf=np.sum(out[:,8:11]*B[ids[:,0],:,comp]+out[:,11:14]*B[ids[:,1],:,comp]+out[:,14:17]*B[ids[:,2],:,comp],axis=1)
  order=np.lexsort((ids[:,2],ids[:,1],ids[:,0]));ids=ids[order];out=out[order];sf=sf[order]
  lref.scatter_atoms('x',1,3,xx.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))
  lref.command('run 0 pre yes post no')
  Fref=np.ctypeslib.as_array(lref.gather_atoms('f',1,3),shape=(3*len(x),)).copy()
  return proj,ids,out,sf,float(np.max(abs(F-Fref)))
 f0,id0,t0,a0,e0=sample(0,True)
 assert len(t0)==3024,len(t0) # 504 active first-layer C atoms, 756 bonds.
 rows=[]
 for z,h in enumerate(old['steps_A']):
  fp,idp,tp,ap,ep=sample(h);f2p,id2p,t2p,a2p,e2p=sample(2*h);fm,idm,tm,am,em=sample(-h);f2m,id2m,t2m,a2m,e2m=sample(-2*h)
  assert np.array_equal(id0,idp) and np.array_equal(id0,id2p) and np.array_equal(id0,idm) and np.array_equal(id0,id2m)
  S=-((-3*f0+4*fp-f2p)-(3*f0-4*fm+f2m))/(2*h)
  T=-((-3*a0+4*ap-a2p)-(3*a0-4*am+a2m))/(2*h)
  changed=np.any(np.stack((tp[:,5],t2p[:,5],tm[:,5],t2m[:,5]),axis=1)!=t0[:,5,None],axis=1)
  values={f'+{h:.12g}':fp,f'+{2*h:.12g}':f2p,f'-{h:.12g}':fm,f'-{2*h:.12g}':f2m}
  archive_errors=[float(np.max(abs(val-ref_rebo1[list(arch['point_keys']).index(key)]))) for key,val in values.items() if key in arch['point_keys']]
  entry={'h_A':float(h),'runtime_full_S_eV_per_A2':float(S[comp]),'runtime_direct_angle_S_eV_per_A2':float(np.sum(T)),'full_minus_direct_eV_per_A2':float(S[comp]-np.sum(T)),'plugin_vs_builtin_raw_force_max_abs_eV_per_A':max(ep,e2p,em,e2m),'plugin_vs_archived_first_layer_max_abs_eV_per_A':max(archive_errors) if archive_errors else None,'archived_points_compared':len(archive_errors),'changed_segment_calls':int(np.sum(changed)),'changed_segment_S_eV_per_A2':float(np.sum(T[changed])),'unchanged_segment_S_eV_per_A2':float(np.sum(T[~changed])),'direct_angle_calls':int(len(tp)),'coordination_range':list(map(float,[np.min(tp[:,4]),np.max(tp[:,4])]))}
  rows.append(entry)
  if h==2e-5:
   records_middle={'ids_1based':id0+1,'cos_A':np.stack((t0[:,3],tp[:,3],t2p[:,3],tm[:,3],t2m[:,3]),axis=1),'Nij':np.stack((t0[:,4],tp[:,4],t2p[:,4],tm[:,4],t2m[:,4]),axis=1),'segment':np.stack((t0[:,5],tp[:,5],t2p[:,5],tm[:,5],t2m[:,5]),axis=1),'g':np.stack((t0[:,6],tp[:,6],t2p[:,6],tm[:,6],t2m[:,6]),axis=1),'dgdc':np.stack((t0[:,7],tp[:,7],t2p[:,7],tm[:,7],t2m[:,7]),axis=1),'projected_force_eV_per_A':np.stack((a0,ap,a2p,am,a2m),axis=1),'side_S_eV_per_A2':T}
 result={'case':CASE,'plugin_sha256':hashlib.sha256(plugin.read_bytes()).hexdigest(),'source_potential_sha256':hashlib.sha256(params.read_bytes()).hexdigest(),'baseline_plugin_vs_builtin_raw_force_max_abs_eV_per_A':e0,'baseline_plugin_vs_archived_first_layer_max_abs_eV_per_A':float(np.max(abs(f0-ref_rebo1[0]))),'baseline_direct_angular_fixed_eV_per_A':float(np.sum(a0)),'rows':rows,'status':'PATCHED_RUNTIME_DIRECT_ANGULAR_LOG_WITH_UNMODIFIED_FORCE_MATCH'}
 print(json.dumps(result,indent=2),flush=True)
 (R/f'{CASE}_runtime_trace.json').write_text(json.dumps(result,indent=2)+'\n')
 np.savez_compressed(R/f'{CASE}_runtime_middle_records.npz',**records_middle)
finally:l.close();lref.close()
