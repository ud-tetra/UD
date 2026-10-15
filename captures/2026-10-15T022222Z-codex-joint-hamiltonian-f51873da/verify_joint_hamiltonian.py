#!/usr/bin/env python3
"""Constructor checks for the conditional joint Hamiltonian theorem.

Exact algebraic checks and a separately typed numerical integration.  No data fit.
"""
from pathlib import Path
from itertools import combinations
import hashlib,json
import sympy as s
import numpy as np
from scipy.integrate import solve_ivp
O=Path(__file__).resolve().parent
checks=[]
def check(name,condition):
    assert bool(condition),name
    checks.append(name)
def zero(M):return all(s.simplify(x)==0 for x in M)
simp=[t for k in range(1,5) for t in combinations(range(4),k)]
n=len(simp);B=s.zeros(n)
for j,t in enumerate(simp):
    if len(t)>1:
        for k in range(len(t)):B[simp.index(t[:k]+t[k+1:]),j]=(-1)**k
edges=[(i,j) for i in range(n) for j in range(n) if B[i,j]]
m=len(edges);R=s.zeros(n,m)
for e,(i,j) in enumerate(edges):R[i,e]=1;R[j,e]=-1
diamonds=[]
for i,a in enumerate(simp):
    for k,c in enumerate(simp):
        if len(c)==len(a)+2 and set(a)<set(c):
            mids=[j for j in range(n) if B[i,j] and B[j,k]]
            diamonds.append((i,*mids,k))
C=s.zeros(len(diamonds),m)
for d,(i,j,h,k) in enumerate(diamonds):
    for edge,sg in [((i,j),1),((j,k),1),((i,h),-1),((h,k),-1)]:C[d,edges.index(edge)]+=sg
check('source_graph_15_nodes_28_links_18_diamonds',(n,m,len(diamonds))==(15,28,18))
check('maximum_degree_four',max(sum(abs(R[i,e]) for e in range(m)) for i in range(n))==4)
check('ordinary_divergence_rank_14',R.rank()==14)
check('diamond_curl_rank_14',C.rank()==14)
check('boundary_of_diamond_zero',R*C.T==s.zeros(n,len(diamonds)))

# Canonical complex coordinates: bars are independent during differentiation.
p,P,q,Q,c,A,d,F=s.symbols('p P q Q c A d F')
u,v=s.symbols('u v'); b=s.symbols('b',real=True)
H=-s.I*b*(P*u*q-Q*v*p)+s.I*b*(A*v*d-F*u*c)
variables=[(p,P),(q,Q),(c,A),(d,F)]
def pb(f,g):return s.expand(-s.I*sum(s.diff(f,z)*s.diff(g,Z)-s.diff(f,Z)*s.diff(g,z) for z,Z in variables))
Jp=b*(P*u*q+Q*v*p);Jc=b*(A*v*d+F*u*c)
check('fundamental_head_stock_current',s.expand(pb(P*p,H)+Jp)==0)
check('antifundamental_head_stock_current',s.expand(pb(A*c,H)-Jc)==0)
check('fundamental_tail_stock_current',s.expand(pb(Q*q,H)-Jp)==0)
check('antifundamental_tail_stock_current',s.expand(pb(F*d,H)+Jc)==0)
derivtheta=s.I*u*s.diff(H,u)-s.I*v*s.diff(H,v)
check('reciprocal_link_force',s.expand(derivtheta-Jp-Jc)==0)
g=-P*p+A*c
check('fundamental_Gauss_generator',pb(p,g)==s.I*p)
check('antifundamental_Gauss_generator',pb(c,g)==-s.I*c)
check('head_Gauss_constraint_preservation',s.expand(-derivtheta-pb(P*p-A*c,H))==0)
check('tail_Gauss_constraint_preservation',s.expand(derivtheta-pb(Q*q-F*d,H))==0)
check('each_species_norm_bracket',pb(P*p+Q*q,H)==0 and pb(A*c+F*d,H)==0)

# Noncommuting rank-two matrices: independently check signs, covariance and force.
I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Z=s.diag(1,-1)
K=s.Matrix([[1,1],[1,-1]])/s.sqrt(2);phase=s.diag(1,s.I)
frames=[I,X,Z,K,phase]*3
U=[frames[(e+1)%n]*frames[(e+3)%n].H for e in range(m)]
E=[s.Matrix([[e+1,s.I],[-s.I,1-e]])/13 for e in range(m)]
psi=[s.Matrix([s.Rational(i+1,7)+s.I/5,s.Rational(2-i,11)-s.I/3]) for i in range(n)]
chi=[s.Matrix([s.Rational(3-i,9)-s.I/7,s.Rational(i+2,13)+s.I/5]) for i in range(n)]
def gauss(U,E,p,c):
    G=[-p[i]*p[i].H+s.conjugate(c[i])*c[i].T for i in range(n)]
    for e,(i,j) in enumerate(edges):G[i]+=E[e];G[j]-=U[e].H*E[e]*U[e]
    return G
def potential(U):
    W=[]
    for i,j,h,k in diamonds:
        path=U[edges.index((i,j))]*U[edges.index((j,k))]
        other=U[edges.index((i,h))]*U[edges.index((h,k))]
        W.append(other.H*path)
    return W
Ug=[frames[i]*U[e]*frames[j].H for e,(i,j) in enumerate(edges)]
Eg=[frames[i]*E[e]*frames[i].H for e,(i,j) in enumerate(edges)]
pg=[frames[i]*psi[i] for i in range(n)]
cg=[s.conjugate(frames[i])*chi[i] for i in range(n)]
G=gauss(U,E,psi,chi);Gp=gauss(Ug,Eg,pg,cg)
check('U2_Gauss_covariance_all_nodes',all(zero(Gp[i]-frames[i]*G[i]*frames[i].H) for i in range(n)))
W=potential(U);Wp=potential(Ug)
check('U2_diamond_holonomy_covariance',all(zero(Wp[d]-frames[k]*W[d]*frames[k].H) for d,(_,_,_,k) in enumerate(diamonds)))
check('U2_electric_energy_invariance',s.simplify(sum(s.trace(T*T) for T in E)-sum(s.trace(T*T) for T in Eg))==0)
check('U2_summed_trace_Gauss_neutrality',s.simplify(sum(s.trace(T) for T in G)-sum((chi[i].H*chi[i])[0]-(psi[i].H*psi[i])[0] for i in range(n)))==0)
check('U2_nonzero_neutral_initial_data',all(zero(T) for T in gauss(U,[s.zeros(2) for _ in edges],psi,[s.conjugate(z) for z in psi])))
forces=[];covariant=True;work=True;balance=True
T=s.Matrix([[2,1+s.I],[1-s.I,-1]])
for e,(i,j) in enumerate(edges):
    sg=B[i,j];p0=psi[i];p1=psi[j];z0=s.conjugate(chi[i]);z1=s.conjugate(chi[j]);V=U[e]
    force=sg*(V*p1*p0.H+p0*p1.H*V.H+V*z1*z0.H+z0*z1.H*V.H)
    forces.append(force)
    # Explicit directional derivative of the two edge Hamiltonians.
    dV=s.I*T*V;dVH=-s.I*V.H*T
    delta=-s.I*sg*(p0.H*dV*p1)[0]+s.I*sg*(p1.H*dVH*p0)[0]
    delta+=-s.I*sg*(z0.H*dV*z1)[0]+s.I*sg*(z1.H*dVH*z0)[0]
    work &= s.simplify(delta-s.trace(force*T))==0
    dp0=-sg*V*p1;dp1=sg*V.H*p0;dz0=sg*V*z1;dz1=-sg*V.H*z0
    drho0=dp0*p0.H+p0*dp0.H-dz0*z0.H-z0*dz0.H
    drho1=dp1*p1.H+p1*dp1.H-dz1*z1.H-z1*dz1.H
    balance &= zero(-force-drho0) and zero(V.H*force*V-drho1)
    pp0=pg[i];pp1=pg[j];zz0=s.conjugate(cg[i]);zz1=s.conjugate(cg[j]);Vg=Ug[e]
    fg=sg*(Vg*pp1*pp0.H+pp0*pp1.H*Vg.H+Vg*zz1*zz0.H+zz0*zz1.H*Vg.H)
    covariant &= zero(fg-frames[i]*force*frames[i].H)
check('U2_matter_force_directional_derivative_all_links',work)
check('U2_matter_force_covariance_all_links',covariant)
check('U2_matrix_local_Gauss_balance_all_links',balance)
check('U2_matter_force_Hermitian',all(zero(F-F.H) for F in forces))

# Exact curvature seed from neutral matter at vertex 0 and edge 01.
seed=s.zeros(n,1);i=simp.index((0,));j=simp.index((0,1));seed[i]=seed[j]=1
force=s.Matrix([4*B[i,j]*seed[i]*seed[j] for i,j in edges])
accel=-force;se=edges.index((i,j))
check('neutral_seed_norms_equal_two',(seed.T*seed)[0]==2)
check('neutral_seed_single_link_acceleration_four',accel[se]==4 and sum(abs(x) for x in accel)==4)
curvaccel=C*accel
affected=[d for d,x in enumerate(curvaccel) if x]
check('neutral_seed_two_diamonds_curvature_acceleration',len(affected)==2 and all(abs(curvaccel[d])==4 for d in affected))
check('curvature_defect_fourth_derivative_48',all(s.factorial(4)*s.Rational(1,2)*(curvaccel[d]/2)**2==48 for d in affected))

# Separate numerical cross-check: the full scalar constrained equations.
Rn=np.array(R).astype(float);Cn=np.array(C).astype(float);Bn=np.array(B).astype(float)
def dynamics(t,y):
    theta=y[:m];mom=y[m:2*m];p=y[2*m:2*m+n];c=y[2*m+n:]
    A=np.zeros((n,n),complex);curr=np.zeros(m)
    for e,(i,j) in enumerate(edges):
        V=np.exp(1j*theta[e].real);sg=Bn[i,j]
        A[i,j]=-sg*V;A[j,i]=sg*V.conjugate()
        curr[e]=2*sg*np.real(np.conj(p[i])*V*p[j]+np.conj(c[i])*V.conjugate()*c[j])
    return np.r_[mom,-Cn.T@np.sin(Cn@theta.real)-curr,A@p,-A.conjugate()@c]
def observables(y):
    theta=y[:m].real;mom=y[m:2*m].real;p=y[2*m:2*m+n];c=y[2*m+n:]
    hm=0.
    for e,(i,j) in enumerate(edges):
        V=np.exp(1j*theta[e]);sg=Bn[i,j]
        hm+=2*sg*np.imag(np.conj(p[i])*V*p[j])-2*sg*np.imag(np.conj(c[i])*V.conjugate()*c[j])
    return (.5*np.dot(mom,mom)+np.sum(1-np.cos(Cn@theta))+hm,
            Rn@mom-abs(p)**2+abs(c)**2,np.vdot(p,p).real,np.vdot(c,c).real)
y0=np.r_[np.zeros(2*m),np.array(seed).astype(complex).ravel(),np.array(seed).astype(complex).ravel()]
sol=solve_ivp(dynamics,(0,1),y0,method='DOP853',rtol=2e-12,atol=2e-14,t_eval=np.r_[0,1e-3,.002,np.linspace(.01,1,100)])
assert sol.success
ob=[observables(y) for y in sol.y.T];h0,g0,np0,nc0=ob[0]
num={'status':'PASS','type':'NUMERICAL','method':'DOP853; a=kappa=1, mu=0, r=1; s in [0,1]',
     'energy_max_absolute_drift':float(max(abs(v[0]-h0) for v in ob)),
     'Gauss_max_absolute_residual':float(max(np.max(abs(v[1])) for v in ob)),
     'species_norm_max_absolute_drift':float(max(max(abs(v[2]-np0),abs(v[3]-nc0)) for v in ob)),
     'early_curvature_over_s_squared':[float((Cn@sol.y[:m,k].real)[affected[0]]/sol.t[k]**2) for k in [1,2]],
     'exact_expected_signed_limit':float(curvaccel[affected[0]]/2),
     'physical_promotion':0}
assert max(num[k] for k in ['energy_max_absolute_drift','Gauss_max_absolute_residual','species_norm_max_absolute_drift'])<1e-8
report={'status':'PASS','type':'EXACT constructor checks supporting written proofs','check_count':len(checks),'checks':checks,
        'graph':{'vertices':n,'links':m,'diamonds':len(diamonds),'max_degree':4},
        'seed':{'occupied_simplices':[[0],[0,1]],'psi_equals_chi':'real amplitudes one at both occupied nodes','N_psi':2,'N_chi':2,'E_initial':0,'U_initial':1,'selected_link_E_dot':4,'affected_diamond_count':2,'absolute_curvature_second_derivative':'4a','defect_leading_coefficient':'2a^2 s^4'},
        'review':'Constructor verification; no independent review, no empirical data or physical identification.',
        'physical_promotion':0,'verifier_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(O/'HAMILTONIAN_EXACT_VERIFICATION_v0.1.json').write_text(json.dumps(report,indent=2)+'\n')
(O/'HAMILTONIAN_NUMERICAL_CROSSCHECK_v0.1.json').write_text(json.dumps(num,indent=2)+'\n')
print(json.dumps({'exact':report,'numerical':num},indent=2))
