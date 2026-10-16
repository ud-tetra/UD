"""Exact curved-branch operators and rational symmetry sections."""
import sympy as s
from itertools import permutations
from mode_model import graph

def model():
 g=graph();d=s.sqrt(10);rho=s.sqrt(8+2*d);ell=16*(10+d)/9
 q=s.Matrix([[1,rho/3,(1+d)/3,4*(1+d)/(3*rho)][len(t)-1] for t in g['simplices']]);v=q/s.sqrt(ell);V=s.diag(*v)
 T=g['B'].applyfunc(abs);T=T+T.T;L=rho*s.eye(15)-T;R=g['R'];K=g['K'];w0=rho*(10-d)/480
 D=s.diag(*[{1:s.Integer(1),2:(1+d)/3,3:(8-d)/3}[len(g['simplices'][i])] for i,j in g['edges']]);W=w0*D
 # V^-1 L V^-1 is exact and real. Evaluate elementwise to avoid nested-radical inversions.
 Q=s.zeros(15)
 for i in range(15):
  for j in range(15):
   if L[i,j]:Q[i,j]=s.radsimp(s.simplify(ell*L[i,j]/(q[i]*q[j])))
 G=(R.T*Q*R/4).applyfunc(s.simplify)
 A=(28+17*d)/9;B=(26+10*d)/3
 lp=(A+s.sqrt(A*A-4*B))/2;lm=(A-s.sqrt(A*A-4*B))/2
 return {**g,'rho':rho,'ell':ell,'q':q,'v':v,'V':V,'T':T,'L':L,'w0':w0,'D':D,'W':W,'G':G,'lambda_plus':lp,'lambda_minus':lm,'kappa_critical_per_N':4*w0/lp,'lambda_sum':A,'lambda_product':B}

def sign(p):return (-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
def link_action(g,p):
 mp=[g['simplices'].index(tuple(sorted(p[x] for x in t))) for t in g['simplices']];F=s.zeros(28)
 for e,(i,j) in enumerate(g['edges']):F[g['edges'].index((mp[i],mp[j])),e]=1
 return F

def symmetry_sections(g):
 pp=list(permutations(range(4)));acts=[link_action(g,p) for p in pp];P0=sum(acts,s.zeros(28))/24;h3=[p for p in pp if p[0]==0]
 h8=[p for p in pp if {frozenset((p[0],p[2])),frozenset((p[1],p[3]))}=={frozenset((0,2)),frozenset((1,3))}]
 Ps={'trivial':P0,'standard':sum((link_action(g,p) for p in h3),s.zeros(28))/6-P0,'two_dimensional':sum((link_action(g,p) for p in h8),s.zeros(28))/8-P0,'sign_standard':sum((sign(p)*link_action(g,p) for p in h3),s.zeros(28))/6}
 out={}
 for name,P in Ps.items():
  Z=s.Matrix.hstack(*P.columnspace());left=(Z.T*Z).inv()*Z.T
  out[name]={'projector':P,'basis':Z,'left':left,'D':left*g['D']*Z,'K':left*g['K']*Z,'G':left*g['G']*Z,'dimension':{'trivial':1,'standard':3,'two_dimensional':2,'sign_standard':3}[name]}
 return out

def critical_pattern(g,a,lam):
 d=s.sqrt(10);c=(1+d)/3;h=(8-d)/3;gamma=-lam+(5+4*d)/3;out=[]
 for i,j in g['edges']:
  lo=g['simplices'][i];hi=g['simplices'][j];added=next(u for u in hi if u not in lo)
  if len(lo)==1:out.append(a[lo[0]]+3*a[added])
  elif len(lo)==2:out.append(gamma*sum(a[u] for u in lo)+(2*gamma-4/c)*a[added])
  else:out.append(4*(1-c*gamma)/h*a[added])
 return s.Matrix(out)
