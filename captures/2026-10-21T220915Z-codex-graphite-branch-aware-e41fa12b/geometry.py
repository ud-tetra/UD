import numpy as np
from pathlib import Path

def setup(root,case,a):
 g=np.load(root/'graphite-map/MAPS.npz');edges=g[case+'_edges_0based'];shift=g[case+'_edge_shifts_xy_A'].copy();pat,di=case.split('_',1);lines=(root/'graphite-target-replay/selected'/pat/di/'struct.inp.data').read_text().splitlines();lx=float(next(z for z in lines if 'xlo xhi' in z).split()[1]);ly=float(next(z for z in lines if 'ylo yhi' in z).split()[1]);xy=float(next(z for z in lines if 'xy xz yz' in z).split()[0]);L=np.array([[lx,xy],[0,ly]]);delta=a['initial_positions_A'][:,:2]-g[case+'_source_positions_A'][:,:2];offset=(L@np.rint(np.linalg.solve(L,delta.T))).T;assert np.max(abs(delta-offset))<1e-10;shift-=offset[edges[:,1]]-offset[edges[:,0]];adj=[[] for _ in a['positions_A']]
 for (i,j),sh in zip(edges,shift):adj[i].append((j,np.r_[sh,0]));adj[j].append((i,np.r_[-sh,0]))
 assert all(len(z)==3 for z in adj)
 nei=np.array([[v[0] for v in z] for z in adj]);sh=np.array([[v[1] for v in z] for z in adj]);b=a['positions_A'][nei]-a['positions_A'][:,None,:]+sh;assert np.max(np.linalg.norm(b,axis=2))<1.7
 return nei,b

def clearance(nei,b,disp,knots,hmax=1.25e-5):
 # Squaring cos=k yields a quartic in scaled displacement t=s/hmax.
 db=(disp[nei]-disp[:,None,:])*hmax;nearest=np.inf;checked=0;max_res=0.
 for i,j in [(0,1),(0,2),(1,2)]:
  u,v=b[:,i],b[:,j];du,dv=db[:,i],db[:,j];un=np.linalg.norm(u,axis=1);vn=np.linalg.norm(v,axis=1);dn=np.linalg.norm(du,axis=1);en=np.linalg.norm(dv,axis=1);cos=np.sum(u*v,axis=1)/(un*vn);bound=2*dn/(un-dn)+2*en/(vn-en)
  for k in knots:
   for z in np.flatnonzero(abs(cos-k)<=bound):
    dot=np.array([u[z]@v[z],u[z]@dv[z]+du[z]@v[z],du[z]@dv[z]]);uu=np.array([u[z]@u[z],2*u[z]@du[z],du[z]@du[z]]);vv=np.array([v[z]@v[z],2*v[z]@dv[z],dv[z]@dv[z]]);poly=np.polynomial.polynomial.polymul(dot,dot)-k*k*np.polynomial.polynomial.polymul(uu,vv);checked+=1
    for rt in np.polynomial.polynomial.polyroots(poly):
     if abs(rt.imag)>1e-6 or abs(rt.real)>1.000001:continue
     t=float(rt.real);ut=u[z]+t*du[z];vt=v[z]+t*dv[z];res=abs(ut@vt/(np.linalg.norm(ut)*np.linalg.norm(vt))-k)
     if res<1e-9:nearest=min(nearest,abs(t*hmax));max_res=max(max_res,res)
 return nearest,checked,max_res
