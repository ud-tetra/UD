"""Locate C2 angular join crossings at the fingerprint-matched held probes."""
from pathlib import Path
import json,sys
import numpy as np
from scipy.spatial import cKDTree
from scipy.optimize import brentq
R=Path(__file__).resolve().parent
case=sys.argv[1];a=np.load(R/f'{case}_candidate.npz');x=a['positions_A'];typ=a['atom_types'];B=a['B_extended'];probe=34 if case=='21_dir_0' else 30;d=B[:,:,probe]
pat,name=case.split('_',1);lines=(R/'graphite-target-replay/selected'/pat/name/'struct.inp.data').read_text().splitlines()
lx=float(next(z for z in lines if 'xlo xhi' in z).split()[1]);ly=float(next(z for z in lines if 'ylo yhi' in z).split()[1]);xy=float(next(z for z in lines if 'xy xz yz' in z).split()[0]);v1=np.array([lx,0,0]);v2=np.array([xy,ly,0]);n=len(x)
nei=np.empty((n,3),int);sh=np.empty((n,3,3));dist=np.empty((n,3))
for t in (1,2):
 ids=np.flatnonzero(typ==t);pts=np.concatenate([x[ids]+i*v1+j*v2 for i in (-1,0,1) for j in (-1,0,1)]);idx=np.tile(ids,9);offs=np.concatenate([np.repeat([i*v1+j*v2],len(ids),axis=0) for i in (-1,0,1) for j in (-1,0,1)]);dd,ii=cKDTree(pts).query(x[ids],k=5)
 for row,ii0 in enumerate(ids):
  keep=[k for k in range(5) if not (idx[ii[row,k]]==ii0 and dd[row,k]<1e-6)][:3]
  assert len(keep)==3
  nei[ii0]=idx[ii[row,keep]];sh[ii0]=offs[ii[row,keep]];dist[ii0]=dd[row,keep]
assert np.max(dist)<1.7
b=x[nei]+sh-x[:,None,:];db=d[nei]-d[:,None,:]
def theta(t):
 bb=b+t*db;u=bb/np.linalg.norm(bb,axis=2)[:,:,None]
 return np.stack([np.sum(u[:,i]*u[:,j],axis=1) for i,j in ((0,1),(0,2),(1,2))],axis=1)
q0=theta(0);qplus=theta(8e-5);qminus=theta(-8e-5);lo=np.minimum(qplus,qminus);hi=np.maximum(qplus,qminus)
mask=(lo<-.5)&(hi>-.5);ii=np.argwhere(mask);roots=[]
for j,k in ii:
 f=lambda t:theta(t)[j,k]+.5
 roots.append(brentq(f,-8e-5,8e-5,xtol=1e-15))
roots=np.array(roots)
bins,counts=np.unique(np.round(roots,9),return_counts=True)
result={'case':case,'n_atoms':n,'max_bond_A':float(np.max(dist)),'baseline_near_1e12':int(np.sum(abs(q0+.5)<1e-12)),'crossing_counts':{str(h):int(np.sum((theta(h)>=-.5)!=(theta(-h)>=-.5))) for h in (8e-5,4e-5,2e-5,1e-5,5e-6,2.5e-6,1.25e-6)},'roots_count':len(roots),'roots_positive':int(np.sum(roots>0)),'roots_negative':int(np.sum(roots<0)),'root_abs_A_quantiles':np.quantile(abs(roots),[0,.1,.25,.5,.75,.9,1]).tolist(),'root_A_clusters':[{'root_A_rounded_1e9':float(v),'count':int(c)} for v,c in zip(bins,counts)]}
print(json.dumps(result,indent=2));(R/f'{case}_angular_trace.json').write_text(json.dumps(result,indent=2)+'\n')
