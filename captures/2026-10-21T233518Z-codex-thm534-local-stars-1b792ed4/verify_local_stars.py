"""Exact local face-star support events and schedule nonuniqueness."""
from fractions import Fraction as F
from itertools import combinations,permutations,product
from pathlib import Path
import json

def zero(n,m):return [[F(0) for _ in range(m)] for _ in range(n)]
def tr(a):return list(map(list,zip(*a)))
def mm(a,b):return [[sum((a[i][k]*b[k][j] for k in range(len(b))),F(0)) for j in range(len(b[0]))] for i in range(len(a))]
def mv(a,v):return [sum((x*y for x,y in zip(row,v)),F(0)) for row in a]
def norm(v):return sum((x*x for x in v),F(0))
def solve(a,b):
 a=[list(map(F,row))+[F(v)] for row,v in zip(a,b)];n=len(b)
 for j in range(n):
  k=next(k for k in range(j,n) if a[k][j]);a[k],a[j]=a[j],a[k];d=a[j][j];a[j]=[v/d for v in a[j]]
  for k in range(n):
   if k!=j:
    d=a[k][j]
    if d:a[k]=[v-d*w for v,w in zip(a[k],a[j])]
 return [row[-1] for row in a]
faces=sorted(set(combinations((0,1,2,3),3))|set(combinations((0,1,2,4),3)))
cells=[(0,1,2,3),(0,1,2,4)];orientation=[1,-1];D=zero(7,2)
for j,s in enumerate(cells):
 for i in range(4):D[faces.index(s[:i]+s[i+1:])][j]=orientation[j]*(-1)**i
contacts=[(f,t) for f in range(7) for t in range(2) if D[f][t]]
assert len(contacts)==8 and D[0]==[F(-1),F(1)]
def gen(mask):
 a=zero(9,9)
 for h,(f,t) in zip(mask,contacts):a[f][7+t]=-h*D[f][t];a[7+t][f]=h*D[f][t]
 assert tr(a)==[[-v for v in row] for row in a]
 return a
EPS=F(1,4)
def step(z,mask):
 a=gen(mask);v=mv(a,z);t=EPS/2
 return solve([[F(i==j)-t*a[i][j] for j in range(9)] for i in range(9)],[z[i]+t*v[i] for i in range(9)])
def receipt(z,zp,mask):
 mid=[(x+y)/2 for x,y in zip(z,zp)];J=zero(7,2)
 for h,(f,t) in zip(mask,contacts):J[f][t]=2*EPS*h*D[f][t]*mid[f]*mid[7+t]
 assert all(zp[f]**2-z[f]**2==-sum(J[f]) for f in range(7))
 assert all(zp[7+t]**2-z[7+t]**2==sum(J[f][t] for f in range(7)) for t in range(2))
 def weight(f,t):return F(int(set(faces[f]).issubset(cells[t])),sum(set(faces[f]).issubset(c) for c in cells))
 deltas=[]
 for t in range(2):
  delta=zp[7+t]**2-z[7+t]**2+sum(weight(f,t)*(zp[f]**2-z[f]**2) for f in range(7))
  assert delta==sum(J[f][t]-weight(f,t)*sum(J[f]) for f in range(7));deltas.append(delta)
 assert sum(deltas)==0
 return J,deltas

def face_mask(f):return [int(ff==f) for ff,t in contacts]
def local_formula(z,f,h=(1,1)):
 cs=[D[f][t]*h[t] for t in range(2)];m=sum(x*x for x in cs);t=EPS/2
 fp=((1-m*t*t)*z[f]-2*t*sum(cs[j]*z[7+j] for j in range(2)))/(1+m*t*t)
 out=z[:];out[f]=fp
 for j in range(2):out[7+j]+=t*cs[j]*(z[f]+fp)
 return out
# Every contact mask: independent exact nine-coordinate solve and local receipts.
control=[F(i-2,7) for i in range(9)]
for mask in product((0,1),repeat=8):
 zp=step(control,mask);assert norm(zp)==norm(control);receipt(control,zp,mask)
# Primitive stars are exact sparse restrictions of that same generator.
for f in range(7):
 for h in product((0,1),repeat=2):
  mask=[h[t] if ff==f else 0 for ff,t in contacts]
  out=local_formula(control,f,h);assert out==step(control,mask)
  assert all(out[i]==control[i] for i in range(9) if i!=f and i not in [7+t for t in range(2) if D[f][t]*h[t]])
  receipt(control,out,mask)
# Native v1.2 S52 two-event reset witness; asymmetrically admitted seed contact.
src=[F(0)]*9;src[0]=1;src[faces.index((0,1,3))]=1
m0=[int((f,t)==(faces.index((0,1,3)),0)) for f,t in contacts];s1=step(src,m0)
assert s1[7]==F(16,65) and norm(s1)==2
m1=[int((f,t) in [(faces.index((0,1,3)),0),(0,0)]) for f,t in contacts]
s2=step(s1,m1);J,owned=receipt(s1,s2,m1)
assert J[0][0]==F(-61824,511225) and J[0][1]==0
assert owned==[F(-30912,511225),F(30912,511225)]
# A distinct symmetric preparation exposes contact ordering without an external target.
z0=[F(0)]*9;z0[0]=1
pair0=[int((f,t)==(0,0)) for f,t in contacts];pair1=[int((f,t)==(0,1)) for f,t in contacts]
u=step(z0,pair0);forward=step(u,pair1);receipt(z0,u,pair0);receipt(u,forward,pair1)
v=step(z0,pair1);reverse=step(v,pair0)
joint=step(z0,face_mask(0));receipt(z0,joint,face_mask(0))
def chart(z):return [z[0],-z[7],z[8]]
assert chart(forward)==[F(3969,4225),F(1040,4225),F(1008,4225)]
assert chart(reverse)==[F(3969,4225),F(1008,4225),F(1040,4225)]
assert chart(joint)==[F(31,33),F(8,33),F(8,33)]
assert norm(forward)==norm(reverse)==norm(joint)==1
contrast=forward[7]**2-forward[8]**2;assert contrast==F(65536,17850625)
assert joint[7]**2-joint[8]**2==0
# Disjoint stars commute exactly; stars sharing a cell need not commute.
pf0=faces.index((0,1,3));pf1=faces.index((0,1,4));shared=0
assert step(step(control,face_mask(pf0)),face_mask(pf1))==step(step(control,face_mask(pf1)),face_mask(pf0))
assert step(step(control,face_mask(shared)),face_mask(pf0))!=step(step(control,face_mask(pf0)),face_mask(shared))
# All 12 signed automorphisms of the glued complex, including apex exchange.
def action(perm):
 q2=zero(7,7);q3=zero(2,2)
 for i,s in enumerate(faces):
  u=tuple(perm[j] for j in s);sgn=(-1)**sum(u[i]>u[j] for i in range(3) for j in range(i+1,3));q2[faces.index(tuple(sorted(u)))][i]=sgn
 for i,s in enumerate(cells):
  u=tuple(perm[j] for j in s);j=cells.index(tuple(sorted(u)));sgn=(-1)**sum(u[a]>u[b] for a in range(4) for b in range(a+1,4));q3[j][i]=orientation[i]*sgn*orientation[j]
 assert mm(q2,D)==mm(D,q3)
 q=zero(9,9)
 for i in range(7):
  for j in range(7):q[i][j]=q2[i][j]
 for i in range(2):
  for j in range(2):q[7+i][7+j]=q3[i][j]
 return q
for p in permutations(range(3)):
 for swap in (False,True):
  perm=list(p)+([4,3] if swap else [3,4]);q=action(perm)
  assert step(mv(q,z0),face_mask(0))==mv(q,joint)
# Compare native generator sign convention explicitly: actual core current is positive into core.
assert J[0][0]<0
result={'status':'PASS_EXACT_CONDITIONAL','physical_promotion':0,'contact_masks_verified':256,'local_star_formula_controls':28,'signed_automorphisms':12,
 'source_S52_replay':{'shared_current':str(J[0][0]),'owned_deltas':list(map(str,owned))},
 'symmetric_order_witness':{'initial_norm':'1','coordinate_chart':'shared face, -tau0 core, +tau1 core','pair0_then_pair1':list(map(str,chart(forward))),'pair1_then_pair0':list(map(str,chart(reverse))),'simultaneous_star':list(map(str,chart(joint))),'ordered_owned_support_contrast':str(contrast),'joint_owned_support_contrast':'0'},
 'locality':{'single_star_unchanged_outside_incident_coordinates':True,'disjoint_stars_commute':True,'overlapping_stars_order_dependent':True},
 'native_event_selection':'OPEN','event_step':'epsilon=1/4 protocol convention, no physical clock','outside_peer_review':False}
Path(__file__).with_name('RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
