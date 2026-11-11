"""Source-equation reconstruction of the direct gSpline angular force in REBO.

This computes only the VA*.5*tmp*wik*dgdc angle-gradient lines of bondorder().
Compare its projected stencil with the archived unmodified first-layer REBO.
"""
from pathlib import Path
import json,sys,hashlib
import numpy as np
from scipy.spatial import cKDTree
R=Path(__file__).resolve().parent;case=sys.argv[1]
assert case in ('21_dir_0','21_dir_10024')
a=np.load(R/f'{case}_candidate.npz');x0=a['positions_A'];B=a['B_extended'];typ=a['atom_types'];probe,comp=(34,8) if case=='21_dir_0' else (30,4);D=B[:,:,probe];N=len(x0)
original=R/'lammps-runtime/lammps/share/lammps/potentials/CH.rebo';L=original.read_text().splitlines()
def param(label):return float(next(s.split()[0] for s in L if s.strip().endswith(' '+label)))
bij=np.array([param('BIJc_CC'+str(i)) for i in (1,2,3)]);beta=np.array([param('Beta_CC'+str(i)) for i in (1,2,3)])
start=next(i for i,s in enumerate(L) if '# gC1 and gC2' in s)
numbers=[]
for s in L[start+1:]:
 if '# gH' in s:break
 if s.strip() and not s.lstrip().startswith('#'):numbers.append(float(s.strip()))
assert len(numbers)==54
knots=np.array(numbers[1:6]);gC1=np.array(numbers[6:30]).reshape(4,6);gC2=np.array(numbers[30:54]).reshape(4,6)
assert np.array_equal(gC1[:3],gC2[:3])
pat,name=case.split('_',1);data=R/'graphite-target-replay/selected'/pat/name/'struct.inp.data';lines=data.read_text().splitlines();lx=float(next(z for z in lines if 'xlo xhi' in z).split()[1]);ly=float(next(z for z in lines if 'ylo yhi' in z).split()[1]);xy=float(next(z for z in lines if 'xy xz yz' in z).split()[0]);v1=np.array([lx,0,0]);v2=np.array([xy,ly,0]);nei=np.empty((N,3),int);sh=np.empty((N,3,3));dist=np.empty((N,3))
for t in (1,2):
 ids=np.flatnonzero(typ==t);pts=np.concatenate([x0[ids]+i*v1+j*v2 for i in (-1,0,1) for j in (-1,0,1)]);idx=np.tile(ids,9);offs=np.concatenate([np.repeat([i*v1+j*v2],len(ids),axis=0) for i in (-1,0,1) for j in (-1,0,1)]);dd,ii=cKDTree(pts).query(x0[ids],k=5)
 for row,ii0 in enumerate(ids):
  keep=[k for k in range(5) if not (idx[ii[row,k]]==ii0 and dd[row,k]<1e-6)][:3]
  assert len(keep)==3
  nei[ii0]=idx[ii[row,keep]];sh[ii0]=offs[ii[row,keep]];dist[ii0]=dd[row,keep]
assert np.max(dist)<1.7 and np.min(dist)>1.3
edges=[]
for i in range(N):
 for slot,j in enumerate(nei[i]):
  if i<j:edges.append((i,int(j),slot))
assert len(edges)==3*N//2,len(edges)
ii,jj,slot=np.array(edges).T;other=np.array([[z for z in range(3) if z!=s] for s in slot]);reverse=np.empty(len(edges),int)
for e,(i,j) in enumerate(zip(ii,jj)):
 hit=np.flatnonzero(nei[j]==i);assert len(hit)==1;reverse[e]=hit[0]

def g_eval(c):
 segment=np.searchsorted(knots[1:],c,side='right').clip(0,3)
 coeffs=gC1[segment]
 # Use LAMMPS's Horner differentiation order to limit rounding differences.
 g=coeffs[:,5]*c;der=5*coeffs[:,5]*c
 for order in (4,3,2):
  g+=coeffs[:,order];der+=order*coeffs[:,order];g*=c;der*=c
 g+=coeffs[:,1];der+=coeffs[:,1];g*=c;g+=coeffs[:,0]
 return g,der,segment

def calc(h,per_triple=False):
 x=np.asarray(x0.astype(np.longdouble)+np.longdouble(h)*D.astype(np.longdouble),dtype=float)
 bond=x[nei]+sh-x[:,None,:];length=np.linalg.norm(bond,axis=2);unit=bond/length[:,:,None]
 angle=np.stack([np.sum(unit[:,i]*unit[:,j],axis=1) for i,j in ((0,1),(0,2),(1,2))],axis=1)
 # gSpline is called once per ordered edge and its two other neighbors.
 c=np.sum(unit[:,[0,0,1]]*unit[:,[1,2,2]],axis=2)
 g,dg,seg=g_eval(c.ravel());g=g.reshape(N,3);dg=dg.reshape(N,3);seg=seg.reshape(N,3)
 gmat=np.empty((N,3,3));dmat=np.empty((N,3,3));smat=np.empty((N,3,3),int)
 for k,(p,q) in enumerate(((0,1),(0,2),(1,2))):gmat[:,p,q]=gmat[:,q,p]=g[:,k];dmat[:,p,q]=dmat[:,q,p]=dg[:,k];smat[:,p,q]=smat[:,q,p]=seg[:,k]
 ur=unit[ii,slot];vr=unit[jj,reverse];r=length[ii,slot];VA=-np.sum(bij[None,:]*np.exp(-r[:,None]*beta[None,:]),axis=1)
 assert np.max(abs(r-length[jj,reverse]))<1e-10
 F=np.zeros((N,3));records=[]
 for ci,cj,edge_slot,others in ((ii,jj,slot,other),(jj,ii,reverse,np.array([[z for z in range(3) if z!=s] for s in reverse]))):
  gsum=gmat[ci[:,None],edge_slot[:,None],others].sum(axis=1)
  pij=(1+gsum)**(-.5) # PCCf[2][0] = 0 for PairREBO; all Nij=2, NijH=0.
  assert np.all((gsum>-.5)&(gsum<2))
  u=unit[ci,edge_slot];rr=length[ci,edge_slot]
  for col in range(2):
   kk=nei[ci,others[:,col]];v=unit[ci,others[:,col]];rk=length[ci,others[:,col]];cc=np.sum(u*v,axis=1)
   dgdir=dmat[ci,edge_slot,others[:,col]];segment=smat[ci,edge_slot,others[:,col]]
   coef=VA*.25*pij**3*dgdir
   fj=coef[:,None]*(v-cc[:,None]*u)/rr[:,None]
   fk=coef[:,None]*(u-cc[:,None]*v)/rk[:,None]
   fi=-fj-fk
   np.add.at(F,ci,fi);np.add.at(F,cj,fj);np.add.at(F,kk,fk)
   if per_triple:
    contrib=np.einsum('ij,ij->i',fi,B[ci,:,comp])+np.einsum('ij,ij->i',fj,B[cj,:,comp])+np.einsum('ij,ij->i',fk,B[kk,:,comp])
    records.append(np.stack([ci,cj,kk,cc,segment,contrib],axis=1))
 return B.reshape(-1,81).T@F.ravel(),np.concatenate(records) if per_triple else None

arch=np.load(R/'ud-sync/graphite-analysis'/f'{case}_projected.npz');f0,triples=calc(0,True)
ref=arch['projected_forces'][list(arch['modes']).index('rebo1'),0];rows=[]
for h in (8e-5,4e-5,2e-5,1e-5,5e-6,2.5e-6,1.25e-6):
 fp,tp=calc(h,True);f2p,t2p=calc(2*h,True);fm,tm=calc(-h,True);f2m,t2m=calc(-2*h,True)
 s=-((-3*f0+4*fp-f2p)-(3*f0-4*fm+f2m))/(2*h)
 st=-((-3*triples[:,5]+4*tp[:,5]-t2p[:,5])-(3*triples[:,5]-4*tm[:,5]+t2m[:,5]))/(2*h)
 changed=np.any(np.stack([tp[:,4],t2p[:,4],tm[:,4],t2m[:,4]],axis=1)!=triples[:,4,None],axis=1)
 crossing=float(np.sum(st[changed]));noncross=float(np.sum(st[~changed]));top=np.argsort(-abs(st))[:12]
 if h==2e-5:
  active=np.flatnonzero(typ[triples[:,0].astype(int)]==1)
  ids=triples[active,:3].astype(int)
  order=np.lexsort((ids[:,2],ids[:,1],ids[:,0]));active=active[order];ids=ids[order]
  records=(triples,tp,t2p,tm,t2m)
  np.savez_compressed(R/f'{case}_python_middle_records.npz',ids_1based=ids+1,
       cos_A=np.stack([z[active,3] for z in records],axis=1),
       segment=np.stack([z[active,4] for z in records],axis=1),
       projected_force_eV_per_A=np.stack([z[active,5] for z in records],axis=1))
 rows.append({'h_A':h,'angular_side_fixed_eV_per_A2':float(s[comp]),'angular_side_max_eV_per_A2':float(np.max(abs(s))),'branch_calls_plus_minus':int(np.sum(tp[:,4]!=tm[:,4])),'changed_segment_calls_in_full_stencil':int(np.sum(changed)),'changed_segment_side_fixed_eV_per_A2':crossing,'unchanged_segment_side_fixed_eV_per_A2':noncross,'triple_side_sum_consistency_eV_per_A2':float(np.sum(st)-s[comp]),'top_triples':[{'center_atom_1based':int(triples[k,0])+1,'bond_atom_1based':int(triples[k,1])+1,'angle_atom_1based':int(triples[k,2])+1,'cos_baseline':float(triples[k,3]),'segment_baseline':int(triples[k,4]),'segment_plus':int(tp[k,4]),'segment_minus':int(tm[k,4]),'S_eV_per_A2':float(st[k])} for k in top] if h==2e-5 else []})
result={'case':case,'status':'SOURCE_EQUATION_DIRECT_ANGULAR_TERM_ONLY','source_potential_sha256':hashlib.sha256(original.read_bytes()).hexdigest(),'n_bonds':len(edges),'gSpline_angular_calls_per_sample':len(triples),'baseline_full_rebo1_norm_eV_per_A':float(np.linalg.norm(ref)),'baseline_direct_angular_norm_eV_per_A':float(np.linalg.norm(f0)),'baseline_direct_angular_fixed_eV_per_A':float(f0[comp]),'angle_cosine_minmax':[float(np.min(triples[:,3])),float(np.max(triples[:,3]))],'rows':rows}
print(json.dumps(result,indent=2));(R/f'{case}_direct_angular_trace.json').write_text(json.dumps(result,indent=2)+'\n')
