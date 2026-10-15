#!/usr/bin/env python3
"""Exact sector and drift checks; separate full nonlinear diagnostic at six values."""
from pathlib import Path
import sympy as s
import numpy as np
from scipy.integrate import solve_ivp
import json,hashlib
from symmetry_sectors import graph,reduction,sectors,embedded_resolvent
O=Path(__file__).resolve().parent;g=graph();ss=sectors(g);checks=[]
def check(name,ok):
    assert bool(ok),name
    checks.append(name);print('PASS',name,flush=True)
def zero(X):return all(s.simplify(x)==0 for x in X)
A=g['A'];B=g['B'];R=g['R'];C=g['C'];K=g['K'];M=g['M'];S=g['S'];k=g['k'];Lp,PT,P0=reduction(g)
x=s.symbols('x');t=s.symbols('t',positive=True)
fg=-2*(t-1)*(7*t-4)/(34*t*t-48*t+16);fc=2*(5*t-4)/(14*t*t-32*t+16)
report_sectors={}
for name,sec in ss.items():
    P=sec['matter'];Q=sec['links'];W=sec['cycle'];D=sec['seed_D'];KH=sec['small_K']
    for j,(rho,node,link) in enumerate(sec['actions']):
        check(name+'_signed_boundary_'+str(j),rho*B==B*rho)
        check(name+'_ordinary_Gauss_incidence_'+str(j),node*R==R*link)
        check(name+'_stiffness_equivariance_'+str(j),link*K==K*link)
        check(name+'_source_intertwiner_'+str(j),rho*M==M*link)
    check(name+'_orthogonal_projectors',P*P==P and P.T==P and W*W==W and W.T==W)
    check(name+'_matter_dimension_three',P.rank()==3)
    check(name+'_matter_basis',P*k==k and P*D==D and P*A*D==A*D and s.Matrix.hstack(k,D,A*D).rank()==3)
    check(name+'_cycle_support',R*W==s.zeros(15,28) and K*W==W*K)
    char=s.factor(KH.charpoly(x).as_expr())
    expected=x*x-12*x+34 if name.startswith('S3') else (x-6)*(x*x-8*x+14)
    check(name+'_restricted_stiffness_characteristic',s.expand(char-expected)==0)
    if name.startswith('S3'):check(name+'_gradient_seed',zero(B[:4,4:10].T*B[:4,4:10]*D[4:10,:]/4-D[4:10,:]))
    else:check(name+'_cycle_seed',B[:4,4:10]*D[4:10,:]==s.zeros(4,1))
    # Rational unit phases constant on link orbits: direct nonlinear fixture.
    orbits=[];seen=set()
    for e in range(28):
        if e in seen:continue
        orbit={int(next(i for i in range(28) if z[i,e])) for _,_,z in sec['actions']}
        seen|=orbit;orbits.append(orbit)
    U=[s.Integer(1)]*28
    phases=[s.Integer(1),(3+4*s.I)/5,(-5+12*s.I)/13,s.I]
    for j,orbit in enumerate(orbits):
        for e in orbit:U[e]=phases[j%len(phases)]
    Dtw=s.zeros(15)
    for e,(i,j) in enumerate(g['edges']):Dtw[i,j]=B[i,j]*U[e]
    AU=Dtw.H-Dtw
    f=P*s.Matrix([s.Rational(i+1,13)+s.I*s.Rational(i%3,7) for i in range(15)])
    d=P*s.Matrix([s.Rational(4-i,17)-s.I*s.Rational(i%4,11) for i in range(15)])
    J=s.Matrix([4*B[i,j]*s.re(s.conjugate(f[i])*U[e]*d[j]+s.conjugate(d[i])*U[e]*f[j]) for e,(i,j) in enumerate(g['edges'])])
    hol=[]
    for row in range(18):
        val=s.Integer(1)
        for e in range(28):
            if C[row,e]:val*=U[e]**int(C[row,e])
        hol.append(s.im(s.simplify(val)))
    magnetic=C.T*s.Matrix(hol);q=s.Matrix([4*s.re(s.conjugate(f[i])*d[i]) for i in range(15)])
    Lam=-Lp*q;fdot=AU*f+s.I*s.diag(*Lam)*f;ddot=AU*d+s.I*s.diag(*Lam)*d
    check(name+'_nonlinear_matter_tangent_fixture',zero(P*fdot-fdot) and zero(P*ddot-ddot))
    check(name+'_nonlinear_current_tangent_fixture',zero(Q*J-J) and zero(W*PT*J-PT*J))
    check(name+'_nonlinear_magnetic_tangent_fixture',zero(Q*magnetic-magnetic) and zero(W*magnetic-magnetic))
    check(name+'_Gauss_source_invariant_fixture',zero(sec['nodes']*q-q))
    report_sectors[name]={'group_order':len(sec['group']),'matter_fixed_complex_dimension':3,'ordinary_link_fixed_dimension':len(orbits),'cycle_field_dimension':KH.rows,'restricted_K_characteristic':str(char),'edge_seed_unnormalized':[str(v) for v in D[4:10,:]],'native_matter_basis':'k,D,A D'}

cases=[('stiffness6_frequency2',s.Rational(2,3),'S3_vertex_stabilizer',fg),
       ('stiffness6_frequency4',s.Rational(8,3),'S3_vertex_stabilizer',fg),
       ('cycle_minus_frequency4',16/(4-s.sqrt(2)),'S3_vertex_stabilizer',fg),
       ('cycle_plus_frequency4',16/(4+s.sqrt(2)),'S3_vertex_stabilizer',fg),
       ('gradient_minus_frequency4',16/(6-s.sqrt(2)),'C4_vertex_cycle',fc),
       ('gradient_plus_frequency4',16/(6+s.sqrt(2)),'C4_vertex_cycle',fc)]
rows=[]
for name,tvalue,sector,function in cases:
    sec=ss[sector];D=sec['seed_D'];KH=sec['small_K']
    dets=[]
    for frequency in [0,2,4]:
        det=s.simplify(s.radsimp((tvalue*KH-frequency**2*s.eye(KH.rows)).det()))
        check(name+'_restricted_inverse_frequency_'+str(frequency),det!=0)
        dets.append(str(det))
    RH=embedded_resolvent(sec,tvalue,4)
    Z=M*RH*M.T-S*Lp*S
    average=(P0*Z*P0-A*Z*A/4)/2
    val=s.simplify(s.radsimp(function.subs(t,tvalue)))
    check(name+'_nonzero_residue',val!=0)
    check(name+'_exact_averaged_drift',zero(4*s.I*average*D-2*s.I*val*D))
    theta=(4*RH*M.T*D).applyfunc(s.simplify)
    check(name+'_seed_angle_in_exact_sector',zero(sec['cycle']*theta-theta) and R*theta==s.zeros(15,1))
    check(name+'_zero_initial_particular_momentum',M.T*A*D==s.zeros(28,1))
    rows.append({'case':name,'t':str(s.radsimp(tvalue)),'sector':sector,'restricted_determinants_at_frequencies_0_2_4':dets,'residue':str(val),'averaged_drift':'2 i a alpha^2 residue D !=0','status':'DERIVED CONDITIONAL NONLINEAR ORBITAL INSTABILITY'})
epsilon,alpha=s.symbols('epsilon alpha',positive=True)
check('fixed_species_norm_seed_identity',s.simplify(4*(alpha**2-epsilon**2/4)+epsilon**2-4*alpha**2)==0)
check('pointwise_initial_Gauss_neutrality',all(k[i]==0 for i in range(4,10)))
exact={'status':'PASS','type':'EXACT constructor checks supporting universal equivariance and written nonlinear averaging proof','check_count':len(checks),'checks':checks,'sectors':report_sectors,'resolved_cases':rows,'remaining_resonant_cases_in_requested_set':[],'corollary':'Under the declared action the nonzero neutral flat stationary family is nonlinearly orbitally unstable for every a>0,kappa>=0,finite r and alpha>0. At positive stiffness fixed higher-simplex stock witnesses departure; at zero stiffness an exact holonomy drift does.','scope':'Specific background family; no classification of other backgrounds; no action modification; no physical identification. Exact finite checks are not independent proof review or machine verification of an averaging theorem.','physical_promotion':0,'verifier_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'sector_module_sha256':hashlib.sha256((O/'symmetry_sectors.py').read_bytes()).hexdigest(),'graph_module_sha256':hashlib.sha256((O/'mode_model.py').read_bytes()).hexdigest()}
(O/'RESONANCE_EXACT_VERIFICATION_v0.1.json').write_text(json.dumps(exact,indent=2)+'\n')

# Full nonlinear equations; no symmetry projection is applied to the RHS.
Rn=np.array(R).astype(float);Cn=np.array(C).astype(float);Lpn=np.array(Lp).astype(float);PTn=np.array(PT).astype(float);kn=np.array(k).astype(float).ravel();bn=np.array([int(B[i,j]) for i,j in g['edges']]);edges=g['edges']
def rhs(time,y,eps,kappa):
    theta=y[:28].real;el=y[28:56].real;f=y[56:71];d=y[71:86];Ue=np.exp(1j*eps*theta)
    AU=np.zeros((15,15),complex);J=np.zeros(28)
    for e,(i,j) in enumerate(edges):
        AU[i,j]=-bn[e]*Ue[e];AU[j,i]=bn[e]*Ue[e].conjugate()
        J[e]=4*bn[e]*np.real(np.conj(f[i])*Ue[e]*d[j]+np.conj(d[i])*Ue[e]*f[j])
    q=4*eps*np.real(np.conj(f)*d);Lam=-Lpn@q
    return np.r_[el,-kappa*Cn.T@np.sin(eps*Cn@theta)/eps-PTn@J,AU@f+1j*Lam*f,AU@d+1j*Lam*d]
def obs(y,eps,kappa):
    theta=y[:28].real;el=y[28:56].real;f=y[56:71];d=y[71:86];Ue=np.exp(1j*eps*theta)
    q=4*eps*np.real(np.conj(f)*d);E=eps*el+Rn.T@Lpn@q
    hm=sum(4*eps*bn[e]*np.imag(np.conj(f[i])*Ue[e]*d[j]+np.conj(d[i])*Ue[e]*f[j]) for e,(i,j) in enumerate(edges))
    h=.5*np.dot(E,E)+kappa*np.sum(1-np.cos(eps*Cn@theta))+hm
    return h,2*(np.vdot(f[4:],f[4:]).real+eps**2*np.vdot(d[4:],d[4:]).real),np.vdot(f,f).real,np.vdot(d,d).real,np.vdot(f,d),float(np.max(abs(Rn@E-q)))
campaigns=[]
for name,tvalue,sector,function in cases:
    sec=ss[sector];Pm=np.array(sec['matter']).astype(float);Wn=np.array(sec['cycle']).astype(float)
    D0=np.array(sec['seed_D']).astype(float).ravel();D0/=np.linalg.norm(D0)
    RH=np.array(embedded_resolvent(sec,tvalue,4).evalf()).astype(float)
    baseangle=4*RH@np.array(M).astype(float).T@D0;kappa=float(tvalue)
    runs=[]
    for n in [1,2,4,8,16]:
        T=n*np.pi;eps=.02/T;aa=np.sqrt(1-eps**2/4)
        y0=np.r_[aa*baseangle,np.zeros(28),aa*kn,D0].astype(complex)
        sol=solve_ivp(lambda time,y:rhs(time,y,eps,kappa),(0,T),y0,method='DOP853',rtol=2e-11,atol=2e-13);assert sol.success
        values=[obs(v,eps,kappa) for v in sol.y.T];h0=values[0][0];nf=values[0][2];nd=values[0][3]
        leakage=max(float(np.max(abs((np.eye(28)-Wn)@sol.y[:28]))),float(np.max(abs((np.eye(15)-Pm)@sol.y[56:71]))),float(np.max(abs((np.eye(15)-Pm)@sol.y[71:86]))))
        row={'n_pi':n,'epsilon':eps,'time':T,'initial_excited_stock':values[0][1],'final_excited_stock':values[-1][1],'energy_max_absolute_drift':float(max(abs(v[0]-h0) for v in values)),'f_norm_max_absolute_drift':float(max(abs(v[2]-nf) for v in values)),'D_norm_max_absolute_drift':float(max(abs(v[3]-nd) for v in values)),'Gram_inner_max_absolute_residual':float(max(abs(v[4]) for v in values)),'Gauss_reconstruction_max_absolute_residual':float(max(v[5] for v in values)),'sector_leakage_max_absolute':leakage}
        assert max(row[key] for key in ['energy_max_absolute_drift','f_norm_max_absolute_drift','D_norm_max_absolute_drift','Gram_inner_max_absolute_residual','sector_leakage_max_absolute'])<3e-8
        runs.append(row)
    assert runs[-1]['final_excited_stock']>1e-5 and runs[-1]['initial_excited_stock']<runs[-1]['final_excited_stock']/100
    campaigns.append({'case':name,'t':str(s.radsimp(tvalue)),'sector':sector,'slow_time':.02,'leading_slow_time_Taylor_excited_stock':float(8*function.subs(t,tvalue)**2*.02**2),'runs':runs})
num={'status':'PASS','type':'NUMERICAL diagnostic; no empirical data','method':'DOP853 full nonlinear Coulomb equations in scaled variables, no enforced subgroup projection; a=r=alpha=1; tau=.02 and epsilon=.02/(n*pi); fixed species norms four','campaigns':campaigns,'scope':'Tests nonlinear trajectory scaling, conserved quantities, Gauss reconstruction and leakage from the mathematically invariant sectors. The written proof supplies the nonlinear conclusion, not these finite runs.','physical_promotion':0}
(O/'RESONANCE_NUMERICAL_CROSSCHECK_v0.1.json').write_text(json.dumps(num,indent=2)+'\n')
print(json.dumps({'status':'PASS','exact_check_count':len(checks),'campaigns':[{'case':v['case'],'last':v['runs'][-1]} for v in campaigns]},indent=2))
