"""Formal coefficient checks over Q[m,M,S,t,b,x,y,L]."""
import json
from fractions import Fraction as F
N=8
zero=(0,)*N
one={zero:F(1)}
def var(i):return {tuple(int(j==i) for j in range(N)):F(1)}
def add(a,b,k=1):
 c=a.copy()
 for e,v in b.items():c[e]=c.get(e,F(0))+k*v
 return {e:v for e,v in c.items() if v}
def mul(a,b):
 c={}
 for e,v in a.items():
  for f,w in b.items():
   g=tuple(x+y for x,y in zip(e,f));c[g]=c.get(g,F(0))+v*w
 return {e:v for e,v in c.items() if v}
def scale(a,k):return {e:v*k for e,v in a.items() if v*k}
def total(*args):
 r={}
 for a in args:r=add(r,a)
 return r
sq=lambda a:mul(a,a)
m,M,S,t,b,x,y,L=[var(i) for i in range(N)]
R=add(sq(x),sq(y));d=add(sq(t),sq(b));Delta=add(mul(S,M),sq(m),-1)
mod=add(sq(total(m,mul(t,x),mul(b,y))),sq(add(mul(t,y),mul(b,x),-1)))
expanded=total(sq(m),scale(mul(mul(m,t),x),2),scale(mul(mul(m,b),y),2),mul(d,R));assert mod==expanded
GN=total(mul(M,R),scale(mul(m,total(mul(m,x),mul(t,R))),-2),mul(S,mod))
C=total(M,scale(mul(m,t),-2),mul(S,d));X=total(Delta,scale(sq(m),2),scale(mul(mul(S,m),t),-2))
lhs=total(mul(b,add(GN,mul(Delta,x),-1)),mul(mul(Delta,t),y))
rhs=total(mul(mul(b,C),R),scale(mul(mul(b,X),x),-1),mul(total(scale(mul(mul(S,m),sq(b)),2),mul(Delta,t)),y),mul(mul(b,S),sq(m)));assert lhs==rhs
A=add(M,mul(L,m),-1);tl=add(t,L,-1);dd=add(sq(tl),sq(b))
modgap=add(sq(total(m,mul(tl,x),mul(b,y))),sq(add(mul(tl,y),mul(b,x),-1)))
lhs=total(mul(b,modgap),scale(mul(mul(A,b),x),-1),mul(mul(A,tl),y))
rhs=total(mul(mul(b,dd),R),mul(mul(b,add(scale(mul(m,tl),2),A,-1)),x),mul(total(scale(mul(m,sq(b)),2),mul(A,tl)),y),mul(b,sq(m)));assert lhs==rhs
print(json.dumps({'status':'PASS','ring':'Q[m,M,S,t,b,x,y,L]','identities':['complex norm expansion','joint Gram disk numerator','gap-weighted moment disk numerator'],'exact_coefficient_identities':3,'scope':'Formal algebra only; positive spectral measure, continuum gap and source/static moments are declared/proved prerequisites in REPORT.md.','independent_review':False,'physical_promotion':0},indent=2))
