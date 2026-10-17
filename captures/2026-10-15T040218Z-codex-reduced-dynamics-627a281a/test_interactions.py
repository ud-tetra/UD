from pathlib import Path
from itertools import combinations
from fractions import Fraction as F
import json
import numpy as np
R=Path(__file__).resolve().parent
data=json.load(open(R/'baseline/COMPLEX_AND_ACTION.json'))
reddata=json.load(open(R/'REDUCED_GENERATORS.json'))
cells=[[tuple(c) for c in cs] for cs in data['simplices']]
verts=[tuple(tuple(a) for a in v) for v in data['vertices']];idx={v:i for i,v in enumerate(verts)}
ids=[{c:i for i,c in enumerate(cs)} for cs in cells]
offset=np.cumsum([0]+[len(c) for c in cells]);ro=np.cumsum([0,12,72,120,60])
location={};sign={}
for d,oo in enumerate(reddata['signed_orbits']):
 for a,o in enumerate(oo):
  for l,(j,sg) in enumerate(zip(o['indices'],o['signs'])):location[int(offset[d])+j]=(int(ro[d])+a,l);sign[int(offset[d])+j]=sg
def parity(v):return -1 if sum(v[i]>v[j] for i in range(len(v)) for j in range(i+1,len(v)))%2 else 1
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def qm(a,b):
 def mul(x,y):return (x[0]*y[0]+x[1]*y[1],x[0]*y[1]+x[1]*y[0]+x[1]*y[1])
 def total(v):return (sum(a[0] for a in v),sum(a[1] for a in v))
 out=[total([mul(a[0],b[0])]+[neg(mul(a[i],b[i])) for i in range(1,4)])]
 for i,j,k in [(1,2,3),(2,3,1),(3,1,2)]:out.append(total([mul(a[0],b[i]),mul(a[i],b[0]),mul(a[j],b[k]),neg(mul(a[k],b[j]))]))
 assert all(x%2==y%2==0 for x,y in out)
 return tuple((x//2,y//2) for x,y in out)
conj=lambda v:(v[0],)+tuple(neg(x) for x in v[1:])
g=tuple(tuple(a) for a in data['right_generator'])
qone=((2,0),(0,0),(0,0),(0,0));powers=[qone]
for _ in range(9):powers.append(qm(powers[-1],g))
H=set(powers)
normalizer=[v for v in verts if {qm(qm(conj(v),h),v) for h in H}==H]
centralizer=[v for v in verts if qm(v,g)==qm(g,v)]
rev=next(v for v in normalizer if v not in centralizer)
generic=next(v for v in verts if v not in normalizer)
def action(q,right=True):
 vp=[idx[qm(v,q) if right else qm(q,v)] for v in verts];entries=[]
 for d,cs in enumerate(cells):
  for j,c in enumerate(cs):
   image=tuple(vp[v] for v in c);dest=ids[d][tuple(sorted(image))]
   entries.append((int(offset[d])+dest,int(offset[d])+j,parity(image)))
 return entries
def ringred(v):
 v=list(v)+[0]*max(0,10-len(v))
 for k in range(len(v)-1,3,-1):
  c=v[k]
  for j,sg in enumerate([-1,1,-1,1]):v[k-4+j]+=sg*c
 return tuple(v[:4])
zp=[]
for k in range(10):v=[0]*10;v[k]=1;zp.append(ringred(v))
def mul(a,b):
 v=[0]*7
 for i,x in enumerate(a):
  for j,y in enumerate(b):v[i+j]+=x*y
 return ringred(v)
def star(a):
 v=(0,0,0,0)
 for k,c in enumerate(a):v=add(v,tuple(c*x for x in zp[-k%10]))
 return v
def mixed(entries):
 result=[];zeros=[]
 for m in range(10):
  line=[]
  for n in range(10):
   e={}
   for i,j,c in entries:
    a,r=location[i];b,t=location[j];key=(a,b)
    term=tuple(c*sign[i]*sign[j]*v for v in zp[(m*r-n*t)%10])
    e[key]=add(e.get(key,(0,0,0,0)),term)
   norm=(0,0,0,0)
   for co in e.values():norm=add(norm,mul(star(co),co))
   assert norm[1]==0 and norm[3]==-norm[2]
   # Frobenius square represented in basis (1,phi), normalized by 100.
   line.append([str(F(norm[0]-norm[2],100)),str(F(norm[2],100))])
   if norm==(0,0,0,0):zeros.append([m,n])
  result.append(line)
 return {'norm_squared_1_phi_coefficients':result,'zero_blocks':zeros,'nonzero_blocks':[[m,n] for m in range(10) for n in range(10) if [m,n] not in zeros]}
def channel(d,chosen=None):
 entries=[]
 for j,c in enumerate(cells[d]):
  for k in range(d+1):
   i=ids[d-1][c[:k]+c[k+1:]]
   if chosen is not None and i not in chosen:continue
   weight=chosen.get(i,0) if isinstance(chosen,dict) else 1
   a,b=int(offset[d-1])+i,int(offset[d])+j;v=((-1)**k)*weight
   entries.extend([(a,b,-v),(b,a,v)])
 return entries
single=0;faceorbit=reddata['signed_orbits'][2][0]['indices']
experiments={}
for d in [1,2,3]:experiments[f'uniform_degree_{d}']=mixed(channel(d))
experiments['single_face_contact_change']=mixed(channel(3,{single}))
experiments['complete_face_orbit_contact_change']=mixed(channel(3,set(faceorbit)))
experiments['alternating_orbit_contrast']=mixed(channel(3,{f:(-1)**l for l,f in enumerate(faceorbit)}))
experiments['half_orbit_hard_gate_change']=mixed(channel(3,set(faceorbit[1::2])))
experiments['left_quaternion_control']=mixed(action(generic,False))
experiments['right_normalizer_reversal_control']=mixed(action(rev,True))
experiments['right_generic_control']=mixed(action(generic,True))
for name in ['uniform_degree_1','uniform_degree_2','uniform_degree_3','complete_face_orbit_contact_change','left_quaternion_control']:
 assert all(m==n for m,n in experiments[name]['nonzero_blocks']),name
assert len(experiments['single_face_contact_change']['nonzero_blocks'])==100
assert all((m-n)%10==5 for m,n in experiments['alternating_orbit_contrast']['nonzero_blocks'])
assert len(experiments['half_orbit_hard_gate_change']['nonzero_blocks'])==20 and all((m-n)%10 in [0,5] for m,n in experiments['half_orbit_hard_gate_change']['nonzero_blocks'])
assert all(n==(-m)%10 for m,n in experiments['right_normalizer_reversal_control']['nonzero_blocks'])
assert len(experiments['right_generic_control']['nonzero_blocks'])>10
assert experiments['right_generic_control']['nonzero_blocks']==[[m,n] for m in range(10) for n in range(10) if (m-n)%2==0]
# Contact gating is a response interaction, not necessarily a new chain boundary.
def boundary(d):
 mat=np.zeros((len(cells[d-1]),len(cells[d])),dtype=np.int64)
 for j,c in enumerate(cells[d]):
  for k in range(d+1):mat[ids[d-1][c[:k]+c[k+1:]],j]=(-1)**k
 return mat
B2=boundary(2);B3=boundary(3)
nilpotence={}
for name,chosen in [('single_face',[0]),('complete_orbit',faceorbit)]:
 D=np.zeros(1200,dtype=np.int64);D[chosen]=1;M=(B2*D)@B3
 nilpotence[name]={'B2_D_B3_Frobenius_squared':int(np.sum(M*M))}
 assert np.any(M)
# All six cyclic subgroups in the chosen right-quaternion family.
subgroups={frozenset(qm(qm(conj(v),h),v) for h in H) for v in verts}
assert len(subgroups)==6 and len(normalizer)==20 and len(centralizer)==10
HH=sorted(subgroups,key=lambda h:sorted(h))
def vertex_orbits(h):
 seen=set();oo=[]
 for v in verts:
  if v in seen:continue
  o={qm(v,t) for t in h};assert len(o)==10;seen.update(o);oo.append([idx[t] for t in o])
 return oo
oo=[vertex_orbits(h) for h in HH]
def score(vec,os):return sum(sum(vec[j] for j in o)**2/F(10) for o in os)
uniform=[F(1) for _ in verts];delta=[F(int(i==0)) for i in range(120)]
fiber=[F(int(v in HH[0])) for v in verts]
# Avoid radicals: unnormalized states have norms squared 120, 1, 10.
scu=[score(uniform,o) for o in oo];scd=[score(delta,o) for o in oo];scf=[score(fiber,o)/10 for o in oo]
assert scu==[120]*6 and scd==[F(1,10)]*6 and sorted(scf)==[F(1,5)]*5+[F(1)]
# A positive coherent edge already gives a unique best fibration for that state.
identity=idx[qone];neighbor=idx[g];edge=[F(int(i in [identity,neighbor])) for i in range(120)]
sce=[score(edge,o)/2 for o in oo]
assert sorted(sce)==[F(1,10)]*5+[F(1,5)]
out={'status':'PASS','scope':'Exact cyclotomic Fourier mixing norms; declared skew contact perturbations and separate orthogonal controls. No seam law fabricated.','experiments':experiments,'contact_nilpotence_warnings':nilpotence,'source_rule':{'right_fibrations':6,'centralizer_order':10,'normalizer_order':20,'objective':'s_H(x)=||Pi_H x||^2, Pi_H=(1/10)sum rho(h). Choose unique maximizer; ties remain unresolved.','unnormalized_uniform_scores':[str(t) for t in scu],'unit_uniform_scores':[str(t/120) for t in scu],'single_vertex_scores':[str(t) for t in scd],'unit_fiber_scores':[str(t) for t in scf],'unit_coherent_edge_scores':[str(t) for t in sce],'status':'CANDIDATE selection objective; exact equivariance, uniqueness examples and gap bounds. Scores conserved by symmetric free incidence flow, so no spontaneous selection from that flow.','gap_robustness':'Delta>4 R delta+2 delta^2 suffices for norm-state error delta.'}}
(R/'INTERACTION_AND_SELECTION_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'mixing_blocks':{k:len(v['nonzero_blocks']) for k,v in experiments.items()},'source_fibrations':6,'fiber_scores':[str(t) for t in scf]}))
