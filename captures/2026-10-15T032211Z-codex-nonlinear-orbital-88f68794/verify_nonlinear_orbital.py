#!/usr/bin/env python3
"""Exact algebra supporting written nonlinear averaging proof; numerical diagnostic separate."""
from pathlib import Path
import sympy as s
import numpy as np
import json,hashlib
from scipy.integrate import solve_ivp
from mode_model import graph,reduction,fast_rank
O=Path(__file__).resolve().parent;checks=[]
def check(name,x):
    assert bool(x),name
    checks.append(name);print('PASS',name,flush=True)
def zero(X):return all(s.simplify(x)==0 for x in X)
g=graph();A=g['A'];B=g['B'];R=g['R'];C=g['C'];K=g['K'];k=g['k'];S=g['S'];M=g['M'];Lp,PT,P0=reduction(g)
Gamma=s.diag(*[(-1)**(len(t)-1) for t in g['simplices']])
check('bipartite_parity_anticommutes',Gamma*A*Gamma==-A and Gamma*Gamma==s.eye(15))
check('stationary_vertex_mode',A*k==s.zeros(15,1) and Gamma*k==k)
check('Gauss_and_gauge_identities',R*M.T==S*A and M*R.T==-A*S)
check('matter_force_field_support',S*M==s.zeros(15,28) and M.T*A*M==s.zeros(28))

# General complex edge current identity for two co-moving vectors.
f,F,h,H,d,D,e,E,U,V,b=s.symbols('f F h H d D e E U V b')
q=2*(F*d+D*f) # 4 Re(bar f d)
subs={f:-b*U*h,F:-b*V*H,d:-b*U*e,D:-b*V*E}
dq=s.expand(sum(s.diff(q,x)*subs[x] for x in [f,F,d,D]))
J=2*b*(F*U*e+D*U*h+f*V*E+d*V*H)
check('exact_bilinear_charge_current_balance',s.expand(dq+J)==0)
# Finite rank-two unitary connection fixture, including noncommuting frames.
I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Z=s.diag(1,-1);Q=s.Matrix([[1,1],[1,-1]])/s.sqrt(2)
frames=[I,X,Z,Q,s.diag(1,s.I)]*3
Dt=s.zeros(30)
for idx,(i,j) in enumerate(g['edges']):
    T=frames[(idx+2)%15]*frames[(idx+5)%15].H
    Dt[2*i:2*i+2,2*j:2*j+2]=B[i,j]*T
AU=Dt.H-Dt;GG=s.kronecker_product(Gamma,I)
check('rank_two_curved_parity_identity',zero(GG*AU*GG+AU))
p=s.Matrix([s.Rational(i+1,17)+s.I*s.Rational(i%5,13) for i in range(30)])
w=s.Matrix([s.Rational(2-i,19)-s.I*s.Rational(i%3,11) for i in range(30)])
check('co_moving_Gram_overlap_conserved',s.simplify(((AU*p).H*w+p.H*(AU*w))[0])==0)
check('co_moving_norms_conserved',s.simplify(((AU*p).H*p+p.H*(AU*p))[0])==0)
hh=s.I*AU
check('conjugate_matter_Hamiltonian_is_difference',s.simplify(((GG*w).H*hh*(GG*w)+w.H*hh*w)[0])==0)
check('dark_force_cancels_each_incidence',all(Gamma[i,i]*Gamma[j,j]==-1 for i,j in g['edges']))

B1=B[:4,4:10];Pg=B1.T*B1/4;Pc=s.eye(6)-Pg;ks=[0,6,6-s.sqrt(2),6+s.sqrt(2),4-s.sqrt(2),4+s.sqrt(2)]
wg=[s.Rational(28,17),0,s.Rational(3,17)+s.sqrt(2)/34,s.Rational(3,17)-s.sqrt(2)/34,0,0]
wc=[0,0,0,0,1+s.sqrt(2)/2,1-s.sqrt(2)/2]
QM=M[4:10,:]
for j in range(6):
    expected=s.expand(sum(ww*q**j for ww,q in zip(wg,ks)))*Pg+s.expand(sum(ww*q**j for ww,q in zip(wc,ks)))*Pc
    check('full_edge_spectral_moment_'+str(j),zero(QM*K**j*QM.T-expected))
t=s.symbols('t',positive=True)
fg=-2*(t-1)*(7*t-4)/(34*t*t-48*t+16);fc=2*(5*t-4)/(14*t*t-32*t+16)
check('gradient_residue_from_spectral_weights',s.simplify(sum(ww/(t*q-4) for ww,q in zip(wg,ks))-fg)==0)
check('cycle_residue_from_spectral_weights',s.simplify(sum(ww/(t*q-4) for ww,q in zip(wc,ks))-fc)==0)
check('residue_zeros_disjoint',s.degree(s.gcd(s.fraction(fg)[0],s.fraction(fc)[0]),t)==0)
for tt in [s.Rational(1,2),s.Integer(1),s.Rational(4,5),s.Rational(4,7)]:
    Resol=(tt*K-4*s.eye(28)).inv();Zslow=M*PT*Resol*PT*M.T-S*Lp*S
    average=(P0*Zslow*P0-A*Zslow*A/4)/2
    edge=s.zeros(15);edge[4:10,4:10]=fg.subs(t,tt)*Pg+fc.subs(t,tt)*Pc
    desired=(P0*edge*P0-A*edge*A/4)/2
    check('Coulomb_corrected_average_'+str(tt),zero((average-desired)*P0))
    for label,P,residue in [('gradient',Pg,fg),('cycle',Pc,fc)]:
        dvec=s.zeros(15,1);dvec[4:10,:]=P[:,0]
        check('averaged_matter_drift_'+label+'_'+str(tt),zero(4*s.I*average*dvec-2*s.I*residue.subs(t,tt)*dvec))

# Initial normalization and exact Gauss admissibility of the mismatch seeds.
eps,alpha,nu=s.symbols('epsilon alpha nu',positive=True)
F2=4*alpha**2-eps**2*nu
check('fixed_species_norm_seed',s.expand(F2+eps**2*nu-4*alpha**2)==0)
check('initial_disjoint_vertex_edge_charge_zero',all(k[i]==0 for i in range(4,10)))
check('native_stroboscopic_period',s.exp(A*s.pi)==s.eye(15))
# Four dark-sector resonant field eigenvectors, constructed with spectral polynomials.
z=s.symbols('z');Kpowers=[K**j for j in range(6)];resonant=[]
for kap in ks[2:]:
    poly=s.Poly(s.prod((z-q)/(kap-q) for q in ks if q!=kap),z,extension=s.sqrt(2))
    Proj=s.zeros(28)
    for (power,),coef in poly.terms():Proj+=coef*Kpowers[power]
    P=Pg if s.simplify(kap-6) in [-s.sqrt(2),s.sqrt(2)] else Pc
    dv=s.zeros(15,1);dv[4:10,:]=P[:,0]
    field=(Proj*M.T*dv).applyfunc(s.simplify)
    check('dark_resonant_eigenfield_'+str(kap),zero(K*field-kap*field) and field!=s.zeros(28,1))
    check('dark_resonant_drift_nonzero_'+str(kap),not zero(M*field))
    resonant.append({'stiffness':str(kap),'t':str(4/kap),'drift':'i M v / 2 !=0'})

exact={'status':'PASS','type':'EXACT constructor algebra supporting written universal and averaging proofs','check_count':len(checks),'checks':checks,'new_invariant':'In mu-rotating frame, w=Gamma bar(chi), both psi,w evolve by the same anti-Hermitian generator; their full 2x2 Gram matrix is conserved.','nonlinear_orbital_instability_domain':'all a>0, alpha>0 and kappa>=0, except the six positive values of t=a*kappa/r explicitly left open','unresolved_positive_t':['2/3','8/3','16/(6-sqrt(2))','16/(6+sqrt(2))','16/(4-sqrt(2))','16/(4+sqrt(2))'],'generic_drift':'d f_bar/d tau at (alpha k,D_j) = 2 i a alpha^2 f_j(t) D_j','resonant_dark_cases':resonant,'proof_scope':'A finite-Fourier averaging lemma, parameter domain, fixed-norm admissible seeds and gauge-invariant departure observable are proved in the manuscript. Finite checks are not a computer verification of a long-time nonlinear theorem.','review':'Constructor only; no independent review','physical_promotion':0,'verifier_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'graph_model_sha256':hashlib.sha256((O/'mode_model.py').read_bytes()).hexdigest()}
(O/'NONLINEAR_EXACT_VERIFICATION_v0.1.json').write_text(json.dumps(exact,indent=2)+'\n')

# Separate numerical demonstrations; no theorem rests on these trajectories.
Rn=np.array(R).astype(float);Cn=np.array(C).astype(float);Kn=np.array(K).astype(float);Mn=np.array(M).astype(float)
Lpn=np.array(Lp).astype(float);PTn=np.array(PT).astype(float);kn=np.array(k).astype(float).ravel();bn=np.array([int(B[i,j]) for i,j in g['edges']]);edges=g['edges']
Pgn=np.array(Pg).astype(float);Pcn=np.array(Pc).astype(float)
def rhs(time,y,epsilon,kappa,dark=False):
    th=y[:28].real;el=y[28:56].real;f=y[56:71];d=y[71:86];Ue=np.exp(1j*epsilon*th)
    At=np.zeros((15,15),complex);current=np.zeros(28)
    for e,(i,j) in enumerate(edges):
        At[i,j]=-bn[e]*Ue[e];At[j,i]=bn[e]*Ue[e].conjugate()
        current[e]=4*bn[e]*np.real(np.conj(f[i])*Ue[e]*d[j]+np.conj(d[i])*Ue[e]*f[j])
    charge=4*epsilon*np.real(np.conj(f)*d);lam=-Lpn@charge
    return np.r_[el,-kappa*Cn.T@np.sin(epsilon*Cn@th)/epsilon-PTn@current,At@f+1j*lam*f,At@d+1j*lam*d]
def observables(y,epsilon,kappa):
    th=y[:28].real;el=y[28:56].real;f=y[56:71];d=y[71:86];Ue=np.exp(1j*epsilon*th)
    charge=4*epsilon*np.real(np.conj(f)*d);Et=epsilon*el+Rn.T@Lpn@charge
    matter=0.
    for e,(i,j) in enumerate(edges):matter+=4*epsilon*bn[e]*np.imag(np.conj(f[i])*Ue[e]*d[j]+np.conj(d[i])*Ue[e]*f[j])
    H=.5*np.dot(Et,Et)+kappa*np.sum(1-np.cos(epsilon*Cn@th))+matter
    return H,2*(np.vdot(f[4:],f[4:]).real+epsilon**2*np.vdot(d[4:],d[4:]).real),np.vdot(f,d),np.vdot(f,f).real,np.vdot(d,d).real,float(np.max(abs(Rn@Et-charge)))
campaigns=[]
for name,kappa,P in [('generic_cycle',1.,Pcn),('cycle_cancellation_gradient',.8,Pgn),('dark_field_resonance',4/(4+np.sqrt(2)),Pcn)]:
    d0=np.zeros(15);d0[4:10]=P[:,0];d0/=np.linalg.norm(d0);dark=name=='dark_field_resonance'
    if dark:
        vals,vecs=np.linalg.eigh(Kn);sub=vecs[:,abs(vals-(4+np.sqrt(2)))<1e-9]
        th0=sub@sub.T@Mn.T@d0;th0/=np.linalg.norm(th0);d0*=0
    else:th0=np.linalg.solve(kappa*Kn-4*np.eye(28),4*PTn@Mn.T@d0)
    rows=[]
    for n in [1,2,4,8,16]:
        T=n*np.pi;epsilon=.02/T;aa=np.sqrt(1-epsilon**2*np.vdot(d0,d0).real/4)
        y0=np.r_[aa*th0 if not dark else th0,np.zeros(28),aa*kn,d0].astype(complex)
        sol=solve_ivp(lambda time,y:rhs(time,y,epsilon,kappa),(0,T),y0,method='DOP853',rtol=2e-11,atol=2e-13)
        assert sol.success
        obs=[observables(v,epsilon,kappa) for v in sol.y.T];h0=obs[0][0];Nf=obs[0][3];Nd=obs[0][4]
        rows.append({'n_pi':n,'epsilon':epsilon,'time':T,'initial_excited_stock':obs[0][1],'final_excited_stock':obs[-1][1],'energy_max_absolute_drift':float(max(abs(v[0]-h0) for v in obs)),'Gram_inner_max_absolute_drift':float(max(abs(v[2]) for v in obs)),'f_norm_max_absolute_drift':float(max(abs(v[3]-Nf) for v in obs)),'D_norm_max_absolute_drift':float(max(abs(v[4]-Nd) for v in obs)),'Gauss_reconstruction_max_absolute_residual':float(max(v[5] for v in obs)),'physical_phase_max_norm':float(epsilon*np.max(np.linalg.norm(sol.y[:28].real,axis=0)))})
        assert max(rows[-1][key] for key in ['energy_max_absolute_drift','Gram_inner_max_absolute_drift','f_norm_max_absolute_drift','D_norm_max_absolute_drift'])<2e-8
    assert rows[-1]['final_excited_stock']>1e-5 and rows[-1]['initial_excited_stock']<rows[-1]['final_excited_stock']/100
    campaigns.append({'name':name,'a':1,'kappa':kappa,'alpha':1,'r':1,'slow_time':.02,'rows':rows})
num={'status':'PASS','type':'NUMERICAL diagnostic; no empirical data','method':'DOP853 full nonlinear Coulomb equations in scaled variables; t=n*pi, epsilon=.02/(n*pi); fixed species norms four','campaigns':campaigns,'scope':'Corroborates finite-departure scaling and exact invariants. No numerical trajectory proves Lyapunov instability.','physical_promotion':0}
(O/'NONLINEAR_NUMERICAL_CROSSCHECK_v0.1.json').write_text(json.dumps(num,indent=2)+'\n')
print(json.dumps({'status':'PASS','exact_checks':len(checks),'campaigns':[{ 'name':c['name'],'last':c['rows'][-1]} for c in campaigns]},indent=2))
