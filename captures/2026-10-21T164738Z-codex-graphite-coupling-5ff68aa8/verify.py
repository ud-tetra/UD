from fractions import Fraction as F
import json, math
from pathlib import Path
out=[]
for m,n in [(1,1),(2,1),(3,1)]:
 N=m*m+m*n+n*n
 c=F(m*m+4*m*n+n*n,2*N); t=F(m*m-n*n,2*N)
 T=[[c-t,2*t],[-2*t,c+t]]
 found=[]
 for h in range(-12,13):
  for k in range(-12,13):
   if h==k==0: continue
   v=[row[0]*h+row[1]*k for row in T]
   if all(x.denominator==1 for x in v): found.append((h*h+k*k-h*k,h,k))
 q=min(x[0] for x in found)
 assert F(169,2)>q # outside box, norm>= (h*h+k*k)/2 >=169/2
 assert q=={(1,1):1,(2,1):7,(3,1):13}[(m,n)]
 assert T[0][0]*T[1][1]-T[0][1]*T[1][0]==1
 out.append(dict(pattern=[m,n],cos_theta=str(c),theta_deg=math.degrees(math.acos(float(c))),Nc=1 if m==n else N,common_reciprocal_norm_squared=q,shortest_vectors=[list(x[1:]) for x in found if x[0]==q],reciprocal_rotation=[[str(x) for x in row] for row in T]))
def quad(v,g):return sum(v[i]*g[i][j]*v[j] for i in range(2) for j in range(2))
f=[1,0]; g0=[[0,0],[0,1]]; g1=[[1,0],[0,0]]
assert quad(f,g0)==0 and quad(f,g1)==1
assert sum([1,-1])==0 and quad([1,-1],[[1,0],[0,1]])==2
for e in [F(0),F(1,10),F(-1,3),F(2)]:assert quad([1,e],g0)==e*e
result={'status':'PASS_SCOPED','geometry':out,'exact_controls':{'same_static_potential_different_damping':[0,1],'zero_net_force_nonzero_local_square':2,'declared_leakage':'epsilon^2'},'scope':'Rigid infinite periodic identical honeycomb layers; exact reciprocal enumeration with global lower-shell exclusion. No material Hessian, damping, empirical friction or native UD map supplied.','physical_promotion':0}
Path(__file__).with_name('RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
