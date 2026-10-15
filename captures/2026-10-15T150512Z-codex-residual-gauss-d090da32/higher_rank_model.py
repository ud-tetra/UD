"""Active-to-empty color operators and exact twisted symmetry sections."""
import sympy as s
from itertools import permutations
from curved_mode_model import model,sign

def color_model():
 from mode_model import graph
 g=graph();d=s.sqrt(10);rho=s.sqrt(8+2*d);ell=16*(10+d)/9
 q=s.Matrix([[1,rho/3,(1+d)/3,4*(1+d)/(3*rho)][len(t)-1] for t in g['simplices']]);v=q/s.sqrt(ell);V=s.diag(*v);T=g['B'].applyfunc(abs);T=T+T.T;w0=rho*(10-d)/480
 D=s.diag(*[{1:s.Integer(1),2:(1+d)/3,3:(8-d)/3}[len(g['simplices'][i])] for i,j in g['edges']]);W=w0*D
 u=s.Matrix([-s.I*g['B'][i,j] for i,j in g['edges']]);R=s.zeros(15,28);F=s.zeros(15,28)
 for e,(i,j) in enumerate(g['edges']):R[i,e]=1;R[j,e]=-u[e];F[i,e]=-s.I*v[j];F[j,e]=g['B'][i,j]*v[i]
 L0=rho*s.eye(15)+s.I*g['A']
 squares={1:s.Integer(1),2:(8+2*d)/9,3:(11+2*d)/9,4:(32-4*d)/9}
 Q0=s.diag(*[s.expand(s.radsimp(ell/(2*squares[len(t)]))) for t in g['simplices']])
 for e,(i,j) in enumerate(g['edges']):
  f=s.expand(s.radsimp(20/((5+d)*D[e,e])));Q0[i,j]=-s.I*g['B'][i,j]*f;Q0[j,i]=s.I*g['B'][i,j]*f
 G=(R.H*Q0*R).applyfunc(s.expand)
 asum=(28+17*d)/9;bprod=(26+10*d)/3;lp=(asum+s.sqrt(asum*asum-4*bprod))/2
 return {**g,'rho':rho,'ell':ell,'q':q,'v':v,'V':V,'T':T,'w0':w0,'D':D,'W':W,'kappa_critical_per_N':4*w0/lp,'u':u,'Ru':R,'L0':L0,'F_perp_N1':F,'G_perp':G,'Q0_perp':Q0}

def twisted_action(g,p):
 mapping=[];sg=[]
 for t in g['simplices']:
  pp=[p[x] for x in t];mapping.append(g['simplices'].index(tuple(sorted(pp))));sg.append((-1)**sum(pp[a]>pp[b] for a in range(len(pp)) for b in range(a+1,len(pp))))
 node=s.zeros(15);link=s.zeros(28)
 for i,j in enumerate(mapping):node[j,i]=sg[i]
 for e,(i,j) in enumerate(g['edges']):link[g['edges'].index((mapping[i],mapping[j])),e]=sg[i]
 return node,link

def color_sections(g):
 pp=list(permutations(range(4)));acts={p:twisted_action(g,p)[1] for p in pp};zero=s.zeros(28)
 P0=sum(acts.values(),zero)/24;Pe=sum((sign(p)*acts[p] for p in pp),zero)/24;H3=[p for p in pp if p[0]==0];H8=[p for p in pp if {frozenset((p[0],p[2])),frozenset((p[1],p[3]))}=={frozenset((0,2)),frozenset((1,3))}]
 P={'trivial':P0,'standard':sum((acts[p] for p in H3),zero)/6-P0,'two_dimensional':sum((acts[p] for p in H8),zero)/8-P0,'sign_standard':sum((sign(p)*acts[p] for p in H3),zero)/6-Pe,'sign':Pe};out={}
 for name,proj in P.items():
  Z=s.Matrix.hstack(*proj.columnspace());left=(Z.T*Z).inv()*Z.T
  out[name]={'projector':proj,'basis':Z,'left':left,'D':left*g['D']*Z,'G':left*g['G_perp']*Z,'irrep_dimension':{'trivial':1,'standard':3,'two_dimensional':2,'sign_standard':3,'sign':1}[name]}
 return out
