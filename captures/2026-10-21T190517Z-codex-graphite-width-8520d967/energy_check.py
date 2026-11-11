from pathlib import Path
import numpy as np,ctypes,json,sys,hashlib
from lammps import lammps
root=Path(__file__).resolve().parent;prior=root;source=root.parent/'graphite-target-replay'/'selected';params=root.parent/'lammps-runtime'/'lammps'/'share'/'lammps'/'potentials'
cases=[('21','dir_0'),('21','dir_10024'),('31','dir_10084'),('31','dir_10134')]
pat,name=cases[int(sys.argv[1])];cutoff=float(sys.argv[2]);width=int(sys.argv[3]);a=np.load(prior/('width_'+str(width))/(pat+'_'+name)/('cutoff_'+sys.argv[2])/'MATRICES.npz');n=len(a['atom_types']);group=a['group_index'];d=a['K_fine'].shape[0];counts=np.bincount(group);P=np.zeros((n,d));P[np.arange(n),group]=1/np.sqrt(counts[group]);top=a['atom_types']==2;x0=a['equilibrium_positions_A'];K=a['K_fine'];g=a['g_fine'];f0=a['vertical_forces']
Q=np.zeros((d,d-1))
for j in range(d-1):
 scale=np.sqrt((j+1)*(j+2));Q[:j+1,j]=1/scale;Q[j+1,j]=-(j+1)/scale
w=np.where(np.arange(d)<d//2,-1.,1.);w/=np.linalg.norm(w)
directions=[('first_Helmert',Q[:,0]),('last_Helmert',Q[:,-1]),('breathing',w)]
out=root/('width_'+str(width))/(pat+'_'+name)/('cutoff_'+sys.argv[2]);out.mkdir(parents=True,exist_ok=True);l=lammps(cmdargs=['-screen','none','-log',str(out/'energy.log')])
try:
 for c in [f'plugin load {root}/plugin/kcz_width{width}.so','units metal','boundary p p p','atom_style full','box tilt large',f'read_data {source/pat/name}/struct.inp.data',f'pair_style hybrid/overlay rebo rebo kolmogorov/crespi/z/smooth {cutoff}',f'pair_coeff * * rebo 1 {params}/CH.rebo C NULL',f'pair_coeff * * rebo 2 {params}/CH.rebo NULL C',f'pair_coeff 1 2 kolmogorov/crespi/z/smooth {params}/CC.KC C C','neighbor 3.0 nsq','neigh_modify one 4096','fix 2 all lineforce 0.0 0.0 1.0']:l.command(c)
 def E(x):
  x=np.ascontiguousarray(x);l.scatter_atoms('x',1,3,x.ctypes.data_as(ctypes.POINTER(ctypes.c_double)));l.command('run 0 pre yes post no');return float(l.get_thermo('pe'))
 E0=E(x0);rows=[]
 for label,v in directions:
  D=P@v;kref=float(v@K@v);gref=v@g;force_ref=float(-(D@f0))
  for h in [.002,.001,.0005]:
   xp=x0.copy();xm=x0.copy();xp[:,2]+=h*D;xm[:,2]-=h*D;ep=E(xp);em=E(xm);ke=(ep-2*E0+em)/(h*h);first=(ep-em)/(2*h)
   grows=[]
   for axis in range(2):
    energies=[]
    for sz,sx in [(1,1),(1,-1),(-1,1),(-1,-1)]:
     x=x0.copy();x[:,2]+=sz*h*D;x[top,axis]+=sx*h;energies.append(E(x))
    ge=(energies[0]-energies[1]-energies[2]+energies[3])/(4*h*h)
    grows.append({'axis':axis,'energy_mixed':ge,'force_mixed':float(gref[axis]),'absolute_error':abs(ge-gref[axis]),'passes':bool(abs(ge-gref[axis])<=2e-5+1e-3*abs(gref[axis])),'raw_energies_eV':energies})
   rows.append({'direction':label,'h_A':h,'K_energy':ke,'K_force':kref,'K_absolute_error':abs(ke-kref),'K_passes':bool(abs(ke-kref)<=1e-5+1e-4*abs(kref)),'first_energy':first,'first_force':force_ref,'first_passes':bool(abs(first-force_ref)<=2e-7),'mixed':grows,'raw_energies_eV':[ep,E0,em]})
 result={'case':pat+'_'+name,'cutoff_A':cutoff,'model_id':'KCz-C2-width-sensitivity-v0.2','width_A':width,'checks':rows,'all_fine_checks_pass':all(r['K_passes'] and r['first_passes'] and all(g['passes'] for g in r['mixed']) for r in rows if r['h_A']<=.001),'scope':'directional energy-force checks only; not every entry','physical_promotion':0}
finally:l.close()
result['log_sha256']=hashlib.sha256((out/'energy.log').read_bytes()).hexdigest();(out/'ENERGY_CHECK.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'case':result['case'],'all_fine_checks_pass':result['all_fine_checks_pass']}),flush=True)
