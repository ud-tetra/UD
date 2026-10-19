"""Exact coefficient identities for the scalar continuum spectral majorant."""
from fractions import Fraction as F
import json
# Polynomial ring Q[lambda,t,d,L]; no numerical sampling in the two identities.
def add(a,b,s=1):
 c=a.copy()
 for e,v in b.items():c[e]=c.get(e,F(0))+s*v
 return {e:v for e,v in c.items() if v}
def mul(a,b):
 c={}
 for e,v in a.items():
  for f,w in b.items():
   g=tuple(x+y for x,y in zip(e,f));c[g]=c.get(g,F(0))+v*w
 return {e:v for e,v in c.items() if v}
def scale(a,s):return {e:v*s for e,v in a.items() if v*s}
one={(0,0,0,0):F(1)}
l,t,d,L=[{tuple(int(i==j) for j in range(4)):F(1)} for i in range(4)]
sq=lambda p:mul(p,p)
D=add(sq(add(l,t,-1)),mul(d,t));DL=add(sq(add(L,t,-1)),mul(d,t));td=add(t,d)
a=add(mul(td,D),mul(d,sq(l)),-1);b=mul(t,sq(add(l,td,-1)));assert a==b
c=add(mul(sq(L),D),mul(sq(l),DL),-1)
e=mul(mul(t,add(l,L,-1)),add(mul(add(scale(L,2),td,-1),l),mul(L,td),-1));assert c==e
# Boundary, interior maximizer, omega=0, and both signs of omega.
records=[]
for om,ga in [(F(0),F(1,10)),(F(1),F(1,10)),(F(4),F(1,10)),(F(-4),F(1,10)),(F(9,2),F(1,10)),(F(5),F(1,10)),(F(0),F(1))]:
 tt=om*om;dd=4*ga*ga;ll=max(F(4),tt+dd)
 k2=(tt+dd)/dd if tt+dd>=4 else 16/((4-tt)**2+dd*tt)
 assert k2==ll*ll/((ll-tt)**2+dd*tt)
 assert k2<=901 # only these fixtures; the report proves the full declared band
 assert k2/4<ll*ll/((ll-tt)**2+dd*tt) # deliberate half-factor rejects at maximizer
 records.append({'omega':str(om),'gamma':str(ga),'maximizer_lambda':str(ll),'factor_squared':str(k2),'half_factor_rejected':True})
print(json.dumps({'status':'PASS','exact_polynomial_identities':2,'maximizer_fixtures':records,'scope':'The identities, with t>=0,d>0,L=4, prove the bound for all lambda>=4. Fixture checks illustrate boundary cases; no mesh eigenvalue substitutes for the continuum gap.','independent_review':False,'physical_promotion':0},indent=2))
