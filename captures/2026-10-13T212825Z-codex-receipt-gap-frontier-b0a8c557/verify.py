"""Exact corrected-clock propagation and dimensionless Gibbs gap frontier."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
import json,math
root=Path(__file__).resolve().parent
faces=json.loads((root/'boundary_source.json').read_text())['boundary_face_labels']
N=len(faces);assert N==12;full=(1<<N)-1
neighbors=[[j for j in range(N) if j!=i and len(set(faces[i])&set(faces[j]))==2] for i in range(N)]
assert all(len(x)==3 for x in neighbors)
trans=[]
for m in range(1<<N):
 row=[]
 for i in range(N):
  ones=sum((m>>j)&1 for j in neighbors[i]);major=int(ones>=2)
  q=1 if abs(2*ones-3)==3 else 7
  w=q if (1-((m>>i)&1))!=major else 28-q
  row.append((m^(1<<i),w))
 row.append((m,336-sum(w for _,w in row)));assert all(w>=0 for _,w in row)
 assert sum(w for _,w in row)==336;trans.append(row)
def step(v):
 out=defaultdict(int)
 for m,w in v.items():
  for t,a in trans[m]:out[t]+=a*w
 return dict(out)
def gap(prob):
 return math.log(float((1-prob)/prob)) if 0<prob<F(1,2) else None
loc=F(1,100);q=F(1,10000);p3=3*loc**2-2*loc**3;u4=(1-(1-2*q)**4)/2
p={0:1};den=1;rows=[]
for r in range(33):
 if r in (10,32):
  d=F(sum(abs(p.get(m,0)-p.get(m^full,0)) for m in range(1<<N)),2*den)
  e0=(1-d)/2;assert sum(p.values())==den
  s=(F(1,100)-e0)/(1-2*e0)
  robust=(s-4*q-3*loc**2)/(3*(1-2*loc))
  exact=(s-u4-(1-2*u4)*p3)/((1-2*u4)*(1-2*p3))
  cases=[]
  for c in (F(1,100000),F(1,10000)):
   a=loc**2+c*(1-2*loc);m=p3+c*(1-2*p3)
   seed=m+u4-2*m*u4;err=e0+(1-2*e0)*seed
   bound=e0+(1-2*e0)*(3*a+4*q);assert err<=bound
   cases.append({'c_exact':str(c),'final_error_exact':str(err),'final_error':float(err),'exact_pass':err<=F(1,100),'robust_bound':float(bound),'robust_pass':bound<=F(1,100),'beta_Delta_c':gap(c)})
  rows.append({'storage_updates':r,'write_slots':34,'total_slots':34+r,'ideal_storage_error_exact':str(e0),'ideal_storage_error':float(e0),'seed_ceiling_exact':str(s),'robust_c_ceiling_exact':str(robust),'exact_c_ceiling_exact':str(exact),'robust_c_ceiling':float(robust),'exact_c_ceiling':float(exact),'robust_beta_Delta_c_min':gap(robust),'exact_beta_Delta_c_min':gap(exact),'cases':cases})
 if r<32:p=step(p);den*=336
assert rows[1]['ideal_storage_error_exact']==json.loads((root/'baseline.json').read_text())['storage_error_32_exact']
assert rows[1]['cases'][0]['exact_pass'] and not rows[1]['cases'][1]['exact_pass']
assert rows[0]['cases'][1]['exact_pass']
def h(x):return -float(x)*math.log(float(x))-(1-float(x))*math.log(1-float(x))
c=F(1,100000);energy=float(c)*gap(c)+3*float(loc)*gap(loc)+4*float(q)*gap(q)
entropy=h(c)+3*h(loc)+4*h(q)
logZ=-math.log(1-float(c))-3*math.log(1-float(loc))-4*math.log(1-float(q))
assert abs(entropy-energy-logZ)<1e-12
out={'status':'PASS conditional declared apparatus','physical_promotion':0,'independent_review':'OPEN','G_input':False,'clock':'one primitive gate or complete collision/refresh round per declared slot; post-readout reset excluded','beta_Delta_p':gap(loc),'beta_Delta_q':gap(q),'rows':rows,'incoming_flags':{'count':8,'beta_mean_energy':energy,'entropy_nats':entropy,'log_partition':logZ,'interpretation':'incoming equilibrium inventory, not dissipated work or complete cycle cost'},'native_gap_selection':'OPEN','dimensional_normalization':'OPEN'}
(root/'results.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
