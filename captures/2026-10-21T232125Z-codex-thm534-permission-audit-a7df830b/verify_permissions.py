"""Exact diagonal-contact chain classification and conditional maximal completion.

Effective chain compatibility is an additional hypothesis, not a native UD law.
"""
from fractions import Fraction as F
from itertools import combinations,product,permutations
from pathlib import Path
import json

def zero(n,m):return [[F(0) for _ in range(m)] for _ in range(n)]
def transpose(a):return list(map(list,zip(*a)))
def multiply(a,b):return [[sum((a[i][k]*b[k][j] for k in range(len(b))),F(0)) for j in range(len(b[0]))] for i in range(len(a))]
def apply(a,v):return [sum((x*y for x,y in zip(row,v)),F(0)) for row in a]
def norm(v):return sum((x*x for x in v),F(0))
def solve(a,b):
 a=[list(map(F,row))+[F(v)] for row,v in zip(a,b)];n=len(b)
 for j in range(n):
  k=next(k for k in range(j,n) if a[k][j]);a[k],a[j]=a[j],a[k]
  d=a[j][j];a[j]=[v/d for v in a[j]]
  for k in range(n):
   if k!=j:
    d=a[k][j]
    if d:a[k]=[v-d*w for v,w in zip(a[k],a[j])]
 return [row[-1] for row in a]
V=list(combinations(range(4),1));E=list(combinations(range(4),2));FC=list(combinations(range(4),3));C=[(0,1,2,3)]
def boundary(lo,hi):
 a=zero(len(lo),len(hi))
 for j,s in enumerate(hi):
  for k in range(len(s)):a[lo.index(s[:k]+s[k+1:])][j]=F((-1)**k)
 return a
B=boundary(V,E);B2=boundary(E,FC);B3=boundary(FC,C)
assert multiply(B,B2)==zero(4,4) and multiply(B2,B3)==zero(6,1)
assert [[B2[i][j] for j in (0,1,2)] for i in (3,4,5)]==[[F(i==j) for j in range(3)] for i in range(3)]
def operators(h,a,t):
 return [[B[i][e]*h[e] for e in range(6)] for i in range(4)],[[B2[e][f]*a[f] for f in range(4)] for e in range(6)],[[t[f]*B3[f][0]] for f in range(4)]
def defects(h,a,t):
 d1,d2,d3=operators(h,a,t);return multiply(d1,d2),multiply(d2,d3)
def flat(h,a,t):
 q,r=defects(h,a,t);return q==zero(4,4) and r==zero(6,1)
def predicted(h,a,t):
 mono=[len({h[E.index(e)] for e in combinations(f,2)})==1 for f in FC]
 return all(not a[f] or mono[f] for f in range(4)) and len({a[f]*t[f] for f in range(4)})==1
all6=list(product((0,1),repeat=6));all4=list(product((0,1),repeat=4))
counts={'tested':0,'flat':0,'all23off':0,'all23on':0};distribution={}
for h in all6:
 mono=sum(len({h[E.index(e)] for e in combinations(f,2)})==1 for f in FC)
 distribution[mono]=distribution.get(mono,0)+1
 for a in all4:
  for t in all4:
   actual=flat(h,a,t);assert actual==predicted(h,a,t)
   counts['tested']+=1;counts['flat']+=actual
   counts['all23off']+=actual and t==(0,)*4
   counts['all23on']+=actual and t==(1,)*4
assert counts=={'tested':16384,'flat':1652,'all23off':162,'all23on':66}
assert distribution=={4:2,2:12,1:32,0:18}

def complete(h):return [1]*4 if len(set(h))==1 else [0]*4
for h in all6:
 valid=[a for a in all4 if flat(h,a,(1,)*4)]
 best=max(sum(a) for a in valid);maximizers=[a for a in valid if sum(a)==best]
 assert maximizers==[tuple(complete(h))]

def generator(h,a,t=(1,)*4):
 out=zero(15,15);d1,d2,d3=operators(h,a,t)
 # Full-chain chart of PR370. Its cell sign is opposite the isolated A23 chart.
 for b,u,v in [(d1,0,4),(d2,4,10),(d3,10,14)]:
  for i in range(len(b)):
   for j in range(len(b[0])):out[u+i][v+j]=b[i][j];out[v+j][u+i]=-b[i][j]
 return out
def cayley(z,a):
 az=apply(a,z);t=F(1,8)
 return solve([[F(i==j)-t*a[i][j] for j in range(15)] for i in range(15)],[z[i]+t*az[i] for i in range(15)])
def gate(z):return [int(x*y>0) for x,y in zip(apply(transpose(B),z[:4]),z[4:10])]
def relabel(z,p):
 out=[F(0)]*15;offset=0
 for basis in [V,E,FC,C]:
  for i,s in enumerate(basis):
   q=tuple(p[k] for k in s);sgn=(-1)**sum(q[i]>q[j] for i in range(len(q)) for j in range(i+1,len(q)))
   out[offset+basis.index(tuple(sorted(q)))]=sgn*z[offset+i]
  offset+=len(basis)
 return out

z0=list(map(F,[3,2,1,0,1,1,1,1,1,1,-3,-3,0,0,0]));z=z0[:];history=[]
for n in range(8):
 h=gate(z);a=complete(h);assert flat(h,a,(1,)*4)
 A=generator(h,a);zn=cayley(z,A);hp=gate(zn)
 assert norm(zn)==38
 mid=[(x+y)/2 for x,y in zip(z,zn)];d1,d2,d3=operators(h,a,(1,)*4)
 old_latent=sum((1-h[e])*z[4+e]**2 for e in range(6));new_latent=sum((1-h[e])*zn[4+e]**2 for e in range(6))
 assert new_latent-old_latent==F(1,2)*sum((1-h[e])*mid[4+e]*v for e,v in enumerate(apply(d2,mid[10:14])))
 history.append({'event':n,'h01':''.join(map(str,h)),'a12':''.join(map(str,a)),'t23':'1111','next_h01':''.join(map(str,hp)),'chain_defects_zero':True,'support_norm':'38','latent_transfer_exact':str(new_latent-old_latent)})
 if n in (0,1,3):
  for p in permutations(range(4)):
   zr=relabel(z,p);hr=gate(zr);ar=complete(hr)
   assert cayley(zr,generator(hr,ar))==relabel(zn,p)
 z=zn
assert history[0]['h01']=='000000' and history[0]['next_h01']=='100000'
assert history[1]['a12']=='0000'
for h in all6:assert norm(cayley(z0,generator(h,complete(h))))==38

# Reconcile the old direct-permission opening and the isolated face-core branch.
h=[1,0,0,0,0,0];q,r=defects(h,[1]*4,[1]*4)
assert norm([v for row in q for v in row])==4 and r==zero(6,1)
assert flat(h,[0]*4,[1]*4)
for h in all6:assert flat(h,[0]*4,[1]*4)
# A23 chart is a cell-amplitude sign conjugacy, not identification of preparations.
R=[F(1)]*14+[F(-1)]
A=generator([0]*6,[0]*4);Ag=[[R[i]*A[i][j]*R[j] for j in range(15)] for i in range(15)]
assert all(Ag[10+f][14]==-B3[f][0] and Ag[14][10+f]==B3[f][0] for f in range(4))

# Audit the newer isolated-face-core receipt witness without executing its source.
d=[F(-1),F(1),F(-1),F(1)];w=list(map(F,[1,1,0,0]));a=F(1);t=F(0)
h=[0]*6;rho=list(map(F,[1,0,0,0]));reserve=[F(1)]*4;isolated=[]
for n in range(14):
 z=[w[f]+d[f]*a/2 for f in range(4)];an=F(15,17)*a-F(8,17)*t;tn=F(8,17)*a+F(15,17)*t
 zn=[w[f]+d[f]*an/2 for f in range(4)];receipt=[F(1,2)*d[f]*(z[f]+zn[f])/2*(t+tn)/2 for f in range(4)]
 assert all(zn[f]**2-z[f]**2==-receipt[f] for f in range(4))
 assert tn**2-t**2==sum(receipt) and norm(zn)+tn**2==3
 cur=[-F(h[e],4)*v for e,v in enumerate(apply(transpose(B),rho))];face=apply(transpose(B2),cur)
 p=[v+b for v,b in zip(rho,apply(B,cur))];rn=[F(3,4)*p[i]+reserve[i]/4 for i in range(4)];rr=[p[i]/4+F(3,4)*reserve[i] for i in range(4)]
 assert sum(rn+rr)==5 and min(rn+rr)>=0
 Eold=norm([v-F(5,8) for v in rho+reserve]);Enew=norm([v-F(5,8) for v in rn+rr])
 assert Eold-Enew>=norm(face)+F(3,8)*norm([p[i]-reserve[i] for i in range(4)])
 isolated.append({'event':n,'burden_mask':''.join(map(str,h)),'support':'3','stock_total':'5','budget_pass':True})
 chi=int(sum(receipt)>0);bits=[int(v>0) for v in receipt]
 h=[chi*int(all(bits[f] for f,s in enumerate(FC) if set(e).issubset(s))) for e in E]
 if n==0:assert receipt==list(map(F,['-18/289','50/289','16/289','16/289'])) and h==[0,0,1,0,1,1]
 a,t,rho,reserve=an,tn,rn,rr
assert isolated[7]['burden_mask']=='010101'

result={'status':'PASS_EXACT_CONDITIONAL','physical_promotion':0,'permission_family':'D1=B1 diag(h), D2=B2 diag(a), D3=diag(t) B3','classification':counts,'monochromatic_face_distribution':distribution,'flatness_source_requirement':'OPEN; tested as an additional condition','unique_completion_requires':'all t23=1, effective chain identities, maximize number of a12 contacts','completion_history':history,'completion_covariance_checks':72,'all64_completion_norm_checks':True,'isolated_v1_1_audit':isolated,'shared_preparation_or_unit_map_between_models':False,'outside_peer_review':False}
Path(__file__).with_name('RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'classification':counts,'completion_first_opening':history[0]['next_h01'],'isolated_receipt_events':14,'physical_promotion':0}))
