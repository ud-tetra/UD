"""Exact Fraction review closure and conditional full-chain face recovery.

No external packages, archived-code imports, numerical fitting or physical units.
"""
from fractions import Fraction as F
from itertools import combinations, permutations, product
from pathlib import Path
import json

def zeros(n,m): return [[F(0) for _ in range(m)] for _ in range(n)]
def eye(n): return [[F(i==j) for j in range(n)] for i in range(n)]
def tr(a): return list(map(list,zip(*a)))
def mm(a,b): return [[sum((a[i][k]*b[k][j] for k in range(len(b))),F(0)) for j in range(len(b[0]))] for i in range(len(a))]
def mv(a,v): return [sum((x*y for x,y in zip(row,v)),F(0)) for row in a]
def norm(v): return sum((x*x for x in v),F(0))
def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def solve(a,b):
 a=[list(map(F,row))+[F(v)] for row,v in zip(a,b)];n=len(b)
 for j in range(n):
  k=next(k for k in range(j,n) if a[k][j]);a[j],a[k]=a[k],a[j]
  d=a[j][j];a[j]=[x/d for x in a[j]]
  for k in range(n):
   if k!=j:
    d=a[k][j]
    if d:a[k]=[x-d*y for x,y in zip(a[k],a[j])]
 return [row[-1] for row in a]
def det(a):
 a=[r[:] for r in a];n=len(a);out=F(1)
 for j in range(n):
  k=next((k for k in range(j,n) if a[k][j]),None)
  if k is None:return F(0)
  if k!=j:a[j],a[k]=a[k],a[j];out=-out
  d=a[j][j];out*=d
  for k in range(j+1,n):
   t=a[k][j]/d
   for l in range(j+1,n):a[k][l]-=t*a[j][l]
 return out

V=list(combinations(range(4),1));E=list(combinations(range(4),2))
FC=list(combinations(range(4),3));T=[(0,1,2,3)]
def boundary(lower,upper):
 a=zeros(len(lower),len(upper))
 for j,s in enumerate(upper):
  for k in range(len(s)):a[lower.index(s[:k]+s[k+1:])][j]=F((-1)**k)
 return a
B=boundary(V,E);B2=boundary(E,FC);B3=boundary(FC,T)
assert mm(B,B2)==zeros(4,4) and mm(B2,B3)==zeros(6,1)
Lface=mm(tr(B2),B2);tc=mm(B3,tr(B3))
assert [[Lface[i][j]+tc[i][j] for j in range(4)] for i in range(4)]==[[4*F(i==j) for j in range(4)] for i in range(4)]
Ledge=mm(tr(B),B);ct=mm(B2,tr(B2))
assert [[Ledge[i][j]+ct[i][j] for j in range(6)] for i in range(6)]==[[4*F(i==j) for j in range(6)] for i in range(6)]

def generator(h,full=False,face_enabled=True):
 a=zeros(15 if full else 10,15 if full else 10)
 blocks=[(B,0,4,h)]
 if full:
  if face_enabled:blocks.append((B2,4,10,[1]*4))
  blocks.append((B3,10,14,[1]))
 for b,u,v,gate in blocks:
  for i in range(len(b)):
   for j in range(len(b[0])):a[u+i][v+j]=b[i][j]*gate[j];a[v+j][u+i]=-b[i][j]*gate[j]
 assert tr(a)==[[-x for x in row] for row in a]
 return a
def shared_permission_generator(h):
 a=generator(h,True)
 for e in range(6):
  for j in range(4):a[4+e][10+j]=h[e]*B2[e][j];a[10+j][4+e]=-h[e]*B2[e][j]
 return a
def cayley(z,a,eps=F(1,4)):
 n=len(z);az=mv(a,z);t=eps/2
 return solve([[F(i==j)-t*a[i][j] for j in range(n)] for i in range(n)],[z[i]+t*az[i] for i in range(n)])
def ready(z):return [v*y for v,y in zip(mv(tr(B),z[:4]),z[4:10])]
def mask(z):return [int(q>0) for q in ready(z)]
def stocks(rho,r,h):
 j=[-F(h[e],4)*v for e,v in enumerate(mv(tr(B),rho))]
 bj=mv(B,j);p=[a+b for a,b in zip(rho,bj)]
 return [F(3,4)*p[i]+r[i]/4 for i in range(4)],[p[i]/4+F(3,4)*r[i] for i in range(4)],p,j,mv(tr(B2),j)
def visible(z,h,full=False):return norm(z[:4])+sum((h[i]*z[4+i]**2 for i in range(6)),F(0))+(norm(z[10:]) if full else F(0))
def latent(z,h):return sum(((1-h[i])*z[4+i]**2 for i in range(6)),F(0))
def signed_relabel(z,perm):
 out=[F(0)]*len(z);offset=0
 for basis in [V,E,FC,T]:
  if offset==len(z):break
  for i,s in enumerate(basis):
   q=tuple(perm[k] for k in s);sign=(-1)**sum(q[i]>q[j] for i in range(len(q)) for j in range(i+1,len(q)))
   out[offset+basis.index(tuple(sorted(q)))]=sign*z[offset+i]
  offset+=len(basis)
 return out

z=list(map(F,[-3,-4,-1,-2,-3,1,-2,-1,-3,1]))
rho=list(map(F,[1,0,0,0]));r=list(map(F,[1,1,1,0]));events=[]
for h in product((0,1),repeat=6):
 zp=cayley(z,generator(h));assert norm(zp)==55 and visible(zp,h)==visible(z,h) and latent(zp,h)==latent(z,h)
 # Test the general circulation budget on every vector via all principal minors.
 bh=[[B[i][e]*h[e] for e in range(6)] for i in range(4)]
 L=mm(bh,tr(B));P=[[F(i==j)-L[i][j]/4 for j in range(4)] for i in range(4)]
 fm=mm(tr(B2),tr(bh));fm=[[-v/4 for v in row] for row in fm]
 PP=mm(P,P);ff=mm(tr(fm),fm)
 K=[[F(i==j)-PP[i][j]-ff[i][j] for j in range(4)] for i in range(4)]
 for k in range(1,5):
  for ids in combinations(range(4),k):assert det([[K[i][j] for j in ids] for i in ids])>=0
for n in range(8):
 h=mask(z);zp=cayley(z,generator(h));hp=mask(zp);mid=[(a+b)/2 for a,b in zip(z,zp)]
 change=norm(zp[:4])-norm(z[:4]);assert change==F(1,2)*dot(h,ready(mid))
 assert visible(zp,hp)-visible(z,h)==sum(((hp[e]-h[e])*zp[4+e]**2 for e in range(6)),F(0))
 rp,rr,p,j,face=stocks(rho,r,h)
 assert norm(face)>0 and sum(rp+rr)==4 and min(rp+rr)>=0
 oldE=norm([x-F(1,2) for x in rho+r]);newE=norm([x-F(1,2) for x in rp+rr])
 assert oldE-newE>=norm(face)+F(3,8)*norm([a-b for a,b in zip(p,r)])
 events.append({'event':n,'mask':''.join(map(str,h)),'face_nonzero':True,'budget_pass':True,'vertex_support_change':str(change),'vertex_support_change_sign':int(change>0)-int(change<0)})
 z,rho,r=zp,rp,rr
assert [e['mask'] for e in events]==['110000','110000','110000','101000','001000','011000','011000','001000']
assert events[7]['vertex_support_change_sign']==-1

# Full-chain all-off recovery: the x,y values were absorbing in the truncated model.
z0=list(map(F,[3,2,1,0,1,1,1,1,1,1,-3,-3,0,0,0]))
assert mask(z0)==[0]*6 and norm(z0)==38
A0=generator([0]*6,True);zp=cayley(z0,A0)
assert zp[:4]==z0[:4] and norm(zp)==38 and mask(zp)==[1,0,0,0,0,0]
assert zp[4:10]==list(map(F,['-8/17','29/17','30/17','4/17','5/17','16/17']))
assert mv(B,zp[4:10])==mv(B,z0[4:10])
full_event=[];z=z0[:];rho=list(map(F,[1,0,0,0]));r=list(map(F,[1,1,1,0]))
for n in range(8):
 h=mask(z);zn=cayley(z,generator(h,True));mid=[(a+b)/2 for a,b in zip(z,zn)];hp=mask(zn)
 assert norm(zn)==38
 dlatent=latent(zn,h)-latent(z,h)
 predicted=F(1,2)*dot([(1-h[e])*mid[4+e] for e in range(6)],mv(B2,mid[10:14]))
 assert dlatent==predicted and visible(zn,h,True)-visible(z,h,True)==-dlatent
 assert visible(zn,hp,True)-visible(zn,h,True)==sum(((hp[e]-h[e])*zn[4+e]**2 for e in range(6)),F(0))
 rp,rr,p,j,face=stocks(rho,r,h)
 oldE=norm([v-F(1,2) for v in rho+r]);newE=norm([v-F(1,2) for v in rp+rr])
 assert oldE-newE>=norm(face)+F(3,8)*norm([a-b for a,b in zip(p,r)])
 assert min(rp+rr)>=0 and sum(rp+rr)==4
 full_event.append({'event':n,'mask':''.join(map(str,h)),'next_mask':''.join(map(str,hp)),'support_norm':'38','stock_total':'4','latent_dynamic_receipt':str(dlatent),'passive_budget_pass':True})
 z,rho,r=zn,rp,rr

# Full-chain fixed-mask norm, including all-off. S37's fixed-mask latent constancy does NOT extend.
for h in product((0,1),repeat=6):
 assert norm(cayley(z0,generator(h,True)))==38
 assert norm(cayley(z0,shared_permission_generator(h)))==38
assert shared_permission_generator([1]*6)==generator([1]*6,True)
assert cayley(z0,shared_permission_generator([0]*6))[:10]==z0[:10]
assert mm([[B[i][e]*int(e==0) for e in range(6)] for i in range(4)],B2)!=zeros(4,4)
for perm in permutations(range(4)):
 z=signed_relabel(z0,perm);assert mask(z)==[0]*6
 assert cayley(z,generator([0]*6,True))==signed_relabel(zp,perm)
 # Nontrivial selected mask after reopening, not just the all-off generator.
 z=signed_relabel(zp,perm)
 assert cayley(z,generator(mask(z),True))==signed_relabel(cayley(zp,generator(mask(zp),True)),perm)
 assert cayley(z,shared_permission_generator(mask(z)))==signed_relabel(cayley(zp,shared_permission_generator(mask(zp))),perm)

# General first-off-event formula and exact face-budget boundary.
y=z0[4:10];cty=mv(ct,y)
for eps in [F(-1,2),F(0),F(1,8),F(1,4),F(1)]:
 f=list(map(F,[2,-1,3,4]));z=z0[:10]+f+[F(3)];zn=cayley(z,A0,eps)
 k=eps/(1+eps**2);d=eps**2/(2*(1+eps**2));bf=mv(B2,f)
 assert zn[4:10]==[y[e]-d*cty[e]+k*bf[e] for e in range(6)]
 assert all(norm(B2[e])==2 for e in range(6))
b=[y[e]-cty[e]/34 for e in range(6)];k=F(4,17)
thresholds=[v*v/(2*k*k) for v in b];assert min(thresholds)==8
boundary_state=z0[:10]+list(map(F,[-2,-2,0,0,0]));assert norm(boundary_state[10:14])==8
assert mask(cayley(boundary_state,A0))==[0]*6
# Rational family f=(-a,-a,0,0) reaches the sharp infimum from above.
for a in [F(2),F(201,100),F(5,2),F(3)]:
 z=z0[:10]+[-a,-a,F(0),F(0),F(0)];zn=cayley(z,A0)
 assert (mask(zn)[0]==1)==(a>2)
assert cayley(z0,generator([0]*6,True,False))[:10]==z0[:10]
uniform=[F(1)]*4+z0[4:]
for _ in range(8):
 assert mask(uniform)==[0]*6;uniform=cayley(uniform,A0)
 assert uniform[:4]==[F(1)]*4

result={'status':'PASS_EXACT_CONDITIONAL','physical_promotion':0,'outside_peer_review':False,
 'old_model_review':{'fixed_mask_receipts':64,'circulation_budget_PSD_masks':64,'principal_minors_per_mask':15,'events':events,'nonzero_face_events':8,'passive_budget_events':8},
 'face_extension':{'all_64_mask_norm_checks':True,'signed_S4_relabels':24,'initial_full_support':'38','one_event_y':list(map(str,zp[4:10])),'first_reopened_mask':'100000','events':full_event,'face_budget_sharp_infimum_squared':'8','strict_opening_requires_budget_gt_infimum':True,'uniform_vertex_obstruction':True,'face_permissions_off_control':True,'competing_shared_permission_generator_checked':True,'mixed_mask_chain_nilpotency_not_assumed':True,'native_face_permission_law':'OPEN','time_step_physical_map':'OPEN'},
 'arithmetic':'Standard-library Fraction; all assertions exact; no stochastic or physical claims'}
out=Path(__file__).with_name('RESULTS.json');out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'review_face_events':8,'review_budget_events':8,'reopened_mask':'100000','full_support':'38','face_budget_infimum_squared':'8','physical_promotion':0}))
