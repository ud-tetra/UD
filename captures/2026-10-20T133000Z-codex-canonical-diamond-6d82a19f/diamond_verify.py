"""Independent symbolic canonical checks for the declared four-link component."""
import json
from pathlib import Path
import sympy as s

I=s.I
t=s.symbols('t0:4',real=True); E=s.symbols('E0:4',real=True)
x=s.symbols('x0:4',real=True); y=s.symbols('y0:4',real=True)
u=s.symbols('u0:4',real=True); v=s.symbols('v0:4',real=True)
a,k,g,mu=s.symbols('a k g mu',real=True)
R=s.Matrix([[1,0,1,0],[-1,1,0,0],[0,0,-1,1],[0,-1,0,-1]])
c=s.Matrix([1,1,-1,-1]); edges=[(0,1),(1,3),(0,2),(2,3)]; b=[-1,1,-1,-1]
checks=[]
def ck(name,ok):
    assert bool(ok),name
    checks.append(name)
ck('incidence_cycle',R*c==s.zeros(4,1));ck('incidence_rank',R.rank()==3)
ck('cycle_norm',s.expand((c.T*c)[0])==4)
ck('boundary_path_cancellation',b[0]*b[1]+b[2]*b[3]==0)
p=s.Matrix([(x[i]+I*y[i])/s.sqrt(2) for i in range(4)])
w=s.Matrix([(u[i]-I*v[i])/s.sqrt(2) for i in range(4)])
q=list(t)+list(x)+list(u); mom=list(E)+list(y)+list(v)
def pb(f,h):return s.expand(sum(s.diff(f,Q)*s.diff(h,P)-s.diff(f,P)*s.diff(h,Q) for Q,P in zip(q,mom)))
def zero(z):return s.simplify(s.expand(z))==0
for i in range(4):
    ck(f'psi_bracket_{i}',zero(pb(p[i],s.conjugate(p[i]))+I))
    ck(f'w_bracket_{i}',zero(pb(w[i],s.conjugate(w[i]))-I))
phi=sum(c[i]*t[i] for i in range(4)); H=a*sum(z*z for z in E)/2+k*(1-s.cos(phi))
h=s.zeros(4)
for e,(i,j) in enumerate(edges):
    U=s.cos(t[e])+I*s.sin(t[e]);h[i,j]=-I*b[e]*U;h[j,i]=s.conjugate(h[i,j])
    H+=g*b[e]*((x[i]*x[j]+y[i]*y[j]+u[i]*u[j]+v[i]*v[j])*s.sin(t[e])+(x[i]*y[j]-y[i]*x[j]+v[i]*u[j]-u[i]*v[j])*s.cos(t[e]))
H+=mu*sum(x[i]**2+y[i]**2+u[i]**2+v[i]**2 for i in range(4))/2
Hcomplex=a*sum(z*z for z in E)/2+k*(1-s.cos(phi))+(p.conjugate().T*(mu*s.eye(4)+g*h)*p)[0]+(w.conjugate().T*(mu*s.eye(4)+g*h)*w)[0]
ck('real_complex_hamiltonian_identity',zero(H-Hcomplex))
for i in range(4):
    ck(f'psi_equation_{i}',zero(I*pb(p[i],H)-((mu*s.eye(4)+g*h)*p)[i]))
    ck(f'w_equation_{i}',zero(-I*pb(w[i],H)-((mu*s.eye(4)+g*h)*w)[i]))
    ck(f'rotor_equation_{i}',zero(pb(t[i],H)-a*E[i]))
G=R*s.Matrix(E)-s.Matrix([(x[i]**2+y[i]**2)/2 for i in range(4)])+s.Matrix([(u[i]**2+v[i]**2)/2 for i in range(4)])
for i in range(4):ck(f'gauss_conservation_{i}',zero(pb(G[i],H)))
ck('psi_norm_conservation',zero(pb(sum(z*z for z in x+y)/2,H)))
ck('w_norm_conservation',zero(pb(sum(z*z for z in u+v)/2,H)))
alpha=s.symbols('al0:4',real=True); J=sum(alpha[i]*G[i] for i in range(4))
for i in range(4):
    ck(f'psi_gauge_generator_{i}',zero(pb(p[i],J)-I*alpha[i]*p[i]))
    ck(f'w_gauge_generator_{i}',zero(pb(w[i],J)-I*alpha[i]*w[i]))
    ck(f'link_gauge_generator_{i}',zero(pb(t[i],J)-(R.T*s.Matrix(alpha))[i]))
F=s.symbols('F0:4',real=True); fr=s.symbols('fr0:4',real=True);fi=s.symbols('fi0:4',real=True);lr=s.symbols('lr0:4',real=True);li=s.symbols('li0:4',real=True)
for i in range(4):
    dG=sum(s.diff(G[i],E[e])*F[e] for e in range(4))+sum(s.diff(G[i],x[j])*s.sqrt(2)*fr[j]+s.diff(G[i],y[j])*s.sqrt(2)*fi[j]+s.diff(G[i],u[j])*s.sqrt(2)*lr[j]-s.diff(G[i],v[j])*s.sqrt(2)*li[j] for j in range(4))
    source=(R*s.Matrix(F))[i]-2*s.re(s.conjugate(p[i])*(fr[i]+I*fi[i]))+2*s.re(s.conjugate(w[i])*(lr[i]+I*li[i]))
    ck(f'raw_source_law_{i}',zero(dG-source))
Fp=s.Matrix([pb(t[i],H) for i in range(4)])
ck('pure_field_pendulum',zero(sum(c[i]*pb(Fp[i],H).subs(g,0) for i in range(4))+4*a*k*s.sin(phi)))
z=s.symbols('z',real=True)
Hbroken=H+z*x[0]
ck('gauge_breaking_control_nonzero',zero(pb(G[0],Hbroken)-z*y[0]))
S0,Escale,fs,qs=s.symbols('S0 Escale fs qs',positive=True)
ck('common_scale_time_conversion',s.simplify(Escale/(fs*qs)-1/(S0/Escale)).subs(qs,S0/fs)==0)
neutral={E[i]:0 for i in range(4)}|{x[i]:1/s.sqrt(2) for i in range(4)}|{y[i]:0 for i in range(4)}|{u[i]:1/s.sqrt(2) for i in range(4)}|{v[i]:0 for i in range(4)}
for i in range(4):ck(f'neutral_initial_state_{i}',zero(G[i].subs(neutral)))
flat=neutral|{t[i]:0 for i in range(4)}|{a:1,k:s.Rational(1,16),g:1,mu:0}
for i in range(4):
    wrong=pb(G[i],H)-2*sum(s.diff(G[i],u[j])*pb(u[j],H)+s.diff(G[i],v[j])*pb(v[j],H) for j in range(4))
    frozen=pb(G[i],H)-sum(s.diff(G[i],E[e])*pb(E[e],H) for e in range(4))
    ck(f'wrong_species_sign_control_{i}',zero(wrong.subs(flat)-[2,-2,0,0][i]))
    ck(f'frozen_electric_control_{i}',zero(frozen.subs(flat)-[-2,2,0,0][i]))
ref={t[0]:s.pi/2,t[1]:-s.pi/2,t[2]:s.pi/2,t[3]:s.pi/2}
ck('relative_equilibrium_eigenvector',s.simplify(h.subs(ref)*s.ones(4,1)/2+s.ones(4,1))==s.zeros(4,1))
ck('relative_equilibrium_holonomy',s.exp(I*phi.subs(ref))==-1)
result={'status':'PASS','exact_checks':len(checks),'checks':checks,'R':R.tolist(),'cycle':list(c),'b':b,'carrier_nodes':['0','01','02','012'],'verification_scope':'Exact symbolic checks of the declared component Hamiltonian and canonical conventions; no apparatus measurements or independent review','physical_promotion':0}
print(json.dumps(result,default=str,indent=2))
