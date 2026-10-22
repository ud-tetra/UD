from pathlib import Path
import numpy as np,json,ctypes,sys,hashlib,time
from lammps import lammps
from common import ROOT,load,vector,positions
p=Path(__file__).resolve().parent;f=json.loads((p/'FREEZE.json').read_text());case=sys.argv[1];a,B,nei,b=load(case);x=a['positions_A'];N=len(x);m=B.shape[2];flat=B.reshape(3*N,m);out=p/case;out.mkdir(exist_ok=True)
for fn,sha in f['inputs'].items():assert hashlib.sha256((ROOT/fn).read_bytes()).hexdigest()==sha
for fn,sha in json.loads((p/'CODE_FREEZE.json').read_text())['files'].items():assert hashlib.sha256((p/fn).read_bytes()).hexdigest()==sha
pat,name=case.split('_',1);params=ROOT/'lammps-runtime/lammps/share/lammps/potentials';plugin=ROOT/'graphite-width/plugin/kcz_width2.so';data=ROOT/'graphite-target-replay/selected'/pat/name/'struct.inp.data';l=lammps(cmdargs=['-screen','none','-log',str(out/'lammps.log')]);start=time.time()
try:
 for cmd in [f'plugin load {plugin}','units metal','boundary p p p','atom_style full','box tilt large',f'read_data {data}','pair_style hybrid/overlay rebo rebo kolmogorov/crespi/z/smooth 24',f'pair_coeff * * rebo 1 {params}/CH.rebo C NULL',f'pair_coeff * * rebo 2 {params}/CH.rebo NULL C',f'pair_coeff 1 2 kolmogorov/crespi/z/smooth {params}/CC.KC C C','neighbor 3.0 nsq','neigh_modify one 4096']:l.command(cmd)
 def force(xx):
  xx=np.ascontiguousarray(xx);l.scatter_atoms('x',1,3,xx.ctypes.data_as(ctypes.POINTER(ctypes.c_double)));l.command('run 0 pre yes post no');F=np.ctypeslib.as_array(l.gather_atoms('f',1,3),shape=(3*N,)).copy();return flat.T@F
 for cfg in f['probes']:
  if cfg['case']!=case:continue
  dest=p/cfg['id'];dest.mkdir();w=vector(m,cfg['kind'],cfg['index_0based']);disp=np.einsum('nam,m->na',B,w);baseline=[force(x)];raw=[];derivs=[];actual=[];guards=[];errors=[];perp=[];tangent=[];knots=np.array(f['branch_knots'])
  def angles(xx):
   bb=b+(xx-x)[nei]-(xx-x)[:,None,:];norm=np.linalg.norm(bb,axis=2);assert np.max(norm)<1.7;u=bb/norm[:,:,None];return np.stack([np.sum(u[:,i]*u[:,j],axis=1) for i,j in [(0,1),(0,2),(1,2)]],axis=1)
  branch0=np.searchsorted(knots,angles(x));minmargin=[]
  for h in cfg['steps_A']:
   xp=positions(x,disp,h);xm=positions(x,disp,-h);actual.append([xp,xm]);eff=np.asarray((xp.astype(np.longdouble)-xm.astype(np.longdouble))/(2*np.longdouble(h)),dtype=np.float64).ravel();qe=flat.T@eff;errors.append(float(np.linalg.norm(eff-disp.ravel())));tangent.append(float(np.linalg.norm(qe-w)));perp.append(float(np.linalg.norm(eff-flat@qe)));safe=True;margin=np.inf
   for t in np.linspace(-1,1,9):
    ca=angles(positions(x,disp,t*h));safe=bool(safe and np.array_equal(np.searchsorted(knots,ca),branch0));margin=min(margin,float(np.min(abs(ca[:,:,None]-knots))))
   guards.append(safe);minmargin.append(margin)
  # Record all selected numerical input controls before force sampling for this probe.
  (dest/'INPUT_GUARD.json').write_text(json.dumps({'probe':cfg['id'],'all_stencils_branch_safe':guards,'minimum_sampled_knot_distance':minmargin,'actual_direction_norm_errors':errors,'tangent_direction_norm_errors':tangent,'orthogonal_direction_norms':perp},indent=2)+'\n')
  for h,(xp,xm) in zip(cfg['steps_A'],actual):
   gp=force(xp);gm=force(xm);raw.append([gp,gm]);derivs.append(-(gp-gm)/(2*h))
  baseline.append(force(x));xm=actual[1][1];xp=actual[1][0];gm_repeat=force(xm);gp_repeat=force(xp);baseline.append(force(x))
  np.savez_compressed(dest/'RAW.npz',positive_negative_forces=raw,derivatives=derivs,actual_positions_A=actual,baseline_forces=baseline,repeat_middle_positive_negative_forces=[gp_repeat,gm_repeat],vector=w,steps_A=cfg['steps_A'])
  print('COMPLETE '+cfg['id'],flush=True)
 (out/'TIMING.json').write_text(json.dumps({'seconds':time.time()-start})+'\n')
finally:l.close()
