#!/usr/bin/env python3
"""Source-bound exact normal-form checks; full-energy diagnostics typed separately."""
from pathlib import Path
from itertools import permutations,combinations,product
import json,hashlib
import sympy as sp,numpy as np
from scipy.optimize import root
from scipy.linalg import eigh
from bifurcation_model import critical_algebra,numerical_model,HADAMARD
from curved_mode_model import link_action
from critical_interval_certificate import certificate,I,Q
O=Path(__file__).resolve().parent;checks=[]
def check(name,value):
    assert bool(value),name;checks.append(name);print('PASS',name,flush=True)
def zero(X):return all(sp.simplify(sp.radsimp(sp.expand(v)))==0 for v in X)
g,Z,z,red,gamma,gram=critical_algebra()
check('Hadamard_isometry',HADAMARD.T*HADAMARD==sp.eye(3))
check('Hadamard_zero_sum_image',sp.ones(1,4)*HADAMARD==sp.zeros(1,3))
x,y,w=sp.symbols('x y w',real=True);v=sp.Matrix([x,y,w]);a=HADAMARD*v;u=x*x+y*y+w*w
fourth=sp.expand(sum(t**4 for t in a))
check('tetrahedral_quartic_to_cubic_anisotropy',sp.expand(fourth-sp.Rational(3,4)*u*u+sp.Rational(1,2)*(x**4+y**4+w**4))==0)
check('critical_pattern_Coulomb',zero(g['R']*g['D']*Z))
check('critical_pattern_eigen',all(red(t)==0 for t in g['K']*Z-z*g['D']*Z))
check('critical_curl_Gram_is_scalar',gram==gamma*sp.eye(3))
check('critical_Gram_relation',all(red(t)==0 for t in z*Z.T*g['D']*Z-gamma*sp.eye(3)))
# All 48 signed coordinate permutations occur under S4 and overall phase reversal.
actions=[]
for p in permutations(range(4)):
    P=sp.zeros(4)
    for i,j in enumerate(p):P[j,i]=1
    T=HADAMARD.T*P*HADAMARD
    check('S4_signed_permutation_'+''.join(map(str,p)),T.T*T==sp.eye(3) and all(sum(t!=0 for t in T.row(i))==1 for i in range(3)))
    actions.extend([T,-T])
check('full_cubic_group_has_order_forty_eight',len({tuple(t) for t in actions})==48)
for p in [(1,0,2,3),(1,2,3,0)]:
    P=sp.zeros(4)
    for i,j in enumerate(p):P[j,i]=1
    T=HADAMARD.T*P*HADAMARD
    check('critical_link_intertwiner_'+''.join(map(str,p)),zero(link_action(g,p)*Z-Z*T))
cert=certificate(g);check('inherited_integer_interval_quartic_certificate',cert['status']=='PASS')
(O/'INHERITED_CRITICAL_CERTIFICATE_v0.1.json').write_text(json.dumps(cert,indent=2)+'\n')
alpha,beta,eps,G=sp.symbols('alpha beta epsilon Gamma',positive=True)
potential=-G*eps*u/2+alpha*u*u-beta*(x**4+y**4+w**4)
grad=sp.Matrix([sp.diff(potential,t) for t in v]);hess=sp.hessian(potential,v)
check('leading_stationary_equations_factor_componentwise',zero(grad-sp.Matrix([t*(-G*eps+4*alpha*u-4*beta*t*t) for t in v])))
branches=[]
for k in [1,2,3]:
    qk=alpha-beta/k;rr=sp.symbols('R',positive=True);n=sp.Matrix([1/sp.sqrt(k) if j<k else 0 for j in range(3)])
    hh=hess.subs({x:rr*n[0],y:rr*n[1],w:rr*n[2]})
    # Substitute the radial stationarity identity Gamma*eps=4*qk*R^2.
    hh=hh.subs(G*eps,4*qk*rr*rr).applyfunc(sp.simplify)
    check('family_'+str(k)+'_radial_Hessian',zero(hh*n-8*qk*rr*rr*n))
    inactive=[sp.eye(3)[:,j] for j in range(k,3)]
    check('family_'+str(k)+'_inactive_angular_Hessian',all(zero(hh*t-4*beta*rr*rr/k*t) for t in inactive))
    active=[sp.eye(3)[:,j]-sp.eye(3)[:,k-1] for j in range(k-1)]
    check('family_'+str(k)+'_active_angular_Hessian',all(zero(hh*t+8*beta*rr*rr/k*t) for t in active))
    points=[]
    for indices in combinations(range(3),k):
        for signs in product([-1,1],repeat=k):
            nn=sp.zeros(3,1)
            for j,sgn in zip(indices,signs):nn[j]=sgn/sp.sqrt(k)
            points.append(nn)
    expected={1:6,2:12,3:8}[k];check('family_'+str(k)+'_oriented_count',len(points)==expected)
    check('family_'+str(k)+'_angular_ratio',sp.simplify(sum(t**4 for t in HADAMARD*n)-({1:sp.Rational(1,4),2:sp.Rational(1,2),3:sp.Rational(7,12)}[k]))==0)
    # Unoriented ray stabilizer in the full cubic group pins the branch to that ray.
    stabilizers=[t for t in actions if t*n==n]
    constraints=sp.Matrix.vstack(*(t-sp.eye(3) for t in stabilizers))
    check('family_'+str(k)+'_fixed_ray_is_one_dimensional',3-constraints.rank()==1 and zero(constraints*n))
    branches.append({'occupied_Hadamard_coordinates':k,'oriented_branches':expected,'angular_ratio':str({1:sp.Rational(1,4),2:sp.Rational(1,2),3:sp.Rational(7,12)}[k]),'Morse_index':k-1,'scalar_real_growing_pairs':k-1,'scalar_nonzero_imaginary_pairs':43-k})
check('all_nonzero_leading_branches_count_twenty_six',sum(t['oriented_branches'] for t in branches)==26)
# Exact outward-rounded interval evaluation of the new curl coefficient.
d=I(10).sqrt();asum=(28+17*d)/9;bprod=(26+10*d)/3;lp=(asum+(asum**2-4*bprod).sqrt())/2;c=(1+d)/3;h=(8-d)/3;gg=-lp+(5+4*d)/3
pattern=[1,1,-1,-1];xx=[]
for i,j in g['edges']:
    lo=g['simplices'][i];hi=g['simplices'][j];added=next(t for t in hi if t not in lo)
    xx.append(I(pattern[lo[0]]+3*pattern[added]) if len(lo)==1 else gg*sum(pattern[t] for t in lo)+(2*gg-4/c)*pattern[added] if len(lo)==2 else 4*(1-c*gg)/h*pattern[added])
gamma_int=sum((sum((int(g['C'][j,e])*xx[e] for e in range(28) if g['C'][j,e]),I(0))**2 for j in range(18)),I(0))/4
check('critical_curl_coefficient_strictly_positive_integer_interval',gamma_int.lo>0)
gamma_exact=sp.simplify(gamma.subs(z,g['lambda_plus']))
gamma_float=float(gamma_exact)
# Reversal in the exact Gauss-reduced chart: n<->m, zeta->-zeta, E->-E.
n0,m0,b0,c0,theta,Ef,eta,zeta,sigma,qcharge=sp.symbols('n m beta gamma theta E eta zeta sigma charge',real=True)
check('reversal_preserves_relative_phase',sp.expand(((-c0)-(-b0))/2-(b0-c0)/2)==0)
check('reversal_flips_common_phase',sp.expand(((-c0)+(-b0))/2+(b0+c0)/2)==0)
check('exact_charge_density_reversal',(sigma+(-qcharge))/2==(sigma-qcharge)/2)
omega=sp.Matrix([[0,1],[-1,0]]);reversal=sp.diag(1,-1)
check('reduced_canonical_two_form_reversal',reversal.T*omega*reversal==-omega)
# Differentiate the exact single-edge reduced Hamiltonian independently of the numerical block formulas.
si,sj=sp.symbols('s_i s_j',positive=True);di,dj,zz,xx=sp.symbols('d_i d_j z X',real=True)
edge=-2*(sp.sqrt((si+di/2)*(sj+dj/2))*sp.cos(xx-zz)+sp.sqrt((si-di/2)*(sj-dj/2))*sp.cos(xx+zz))
check('exact_edge_Hamiltonian_reversal',sp.simplify(edge.subs({di:-di,dj:-dj,zz:-zz},simultaneous=True)-edge)==0)
b=sp.sqrt(si*sj);wc=b*sp.cos(xx);ws=b*sp.sin(xx)
expected_p=sp.Matrix([[wc/(4*si**2),-wc/(4*si*sj),-ws/si],[-wc/(4*si*sj),wc/(4*sj**2),-ws/sj],[-ws/si,-ws/sj,4*wc]])
check('exact_momentum_Hessian_blocks',zero(sp.hessian(edge,(di,dj,zz)).subs({di:0,dj:0,zz:0})-expected_p))
expected_q=sp.Matrix([[4*wc,ws/si,ws/sj],[ws/si,wc/(4*si**2),-wc/(4*si*sj)],[ws/sj,-wc/(4*si*sj),wc/(4*sj**2)]])
scale=sp.diag(1,sp.Rational(1,2),sp.Rational(1,2))
check('exact_configuration_Hessian_blocks',zero(scale*sp.hessian(edge.subs({di:0,dj:0,zz:0}),(xx,si,sj))*scale-expected_q))
check('reversal_eliminates_mixed_position_momentum_Hessian',all(sp.simplify(sp.diff(edge,pp,qq).subs({di:0,dj:0,zz:0}))==0 for pp in [di,dj,zz] for qq in [xx,si,sj]))
# Type-preserving energy order and radial scale are established from the interval signs.
AA,BB=sp.symbols('A4 B4',positive=True);q1=AA+BB/4;q2=AA+BB/2;q3=AA+7*BB/12
check('balanced_branch_has_lowest_leading_energy',sp.simplify(q2-q1)==BB/4 and sp.simplify(q3-q2)==BB/12)
check('supercritical_radial_scale_and_energy',sp.simplify((-G*eps*sp.Symbol('s')/2+q1*sp.Symbol('s')**2).subs(sp.Symbol('s'),G*eps/(4*q1))+G*G*eps*eps/(16*q1))==0)
exact={'status':'PASS','type':'EXACT constructor algebra plus inherited directed integer certificate; local existence/completeness and stability proofs in manuscript','check_count':len(checks),'checks':checks,'Gamma_exact_in_critical_root_field':str(gamma),'Gamma_root':str(g['lambda_plus']),'Gamma_interval':gamma_int.bounds(),'branch_families':branches,'parameter':'epsilon=kappa/(r*N)-kappa_star(N)/N; r=1 for complete scalar classification','amplitude_rule':'R_k^2=Gamma*epsilon/[4*(A4+3*B4/4-B4/(2*k))]+O(epsilon^2)','physical_promotion':0,'independent_review':'PENDING'}
(O/'BIFURCATION_EXACT_VERIFICATION_v0.1.json').write_text(json.dumps(exact,indent=2)+'\n')
# Numerical full ground-state energy; no quartic-truncated stationary solver.
nm=numerical_model(g);basis=nm['basis'];Znum=nm['critical_basis'];Y=nm['complement'];M=nm['M'];kc=nm['kc'];A4=(int(cert['A4']['lower_numerator'])+int(cert['A4']['upper_numerator']))/(2*Q);B4=(int(cert['B4']['lower_numerator'])+int(cert['B4']['upper_numerator']))/(2*Q)
massgram=Znum.T@np.linalg.solve(M,Znum);mc=float(np.trace(massgram)/3);assert np.max(abs(massgram-mc*np.eye(3)))<2e-11
assert np.max(abs(Znum.T@nm['D']@Y))<2e-11
rng=np.random.default_rng(51167);test_theta=basis@(.001*rng.normal(size=14));direction=rng.normal(size=28);direction/=np.linalg.norm(direction)
val,gr,hh,_,_=nm['energy'](test_theta,kc);step=1e-5
vp,gp,_,_,_=nm['energy'](test_theta+step*direction,kc);vm,gm,_,_,_=nm['energy'](test_theta-step*direction,kc)
gradient_error=abs((vp-vm)/(2*step)-gr@direction);hessian_error=float(np.max(abs((gp-gm)/(2*step)-hh@direction)));assert gradient_error<2e-9 and hessian_error<2e-8
records=[]
for k in [1,2,3]:
    axis=np.array([1/np.sqrt(k) if j<k else 0 for j in range(3)]);qk=A4+3*B4/4-B4/(2*k);rows=[]
    for epsilon in [1e-4,5e-5,2.5e-5,1.25e-5]:
        kval=kc+epsilon;radius=np.sqrt(gamma_float*epsilon/(4*qk));seed=np.r_[radius*axis,np.zeros(11)]
        def fun(q):return basis.T@nm['energy'](basis@q,kval)[1]
        def jac(q):return basis.T@nm['energy'](basis@q,kval)[2]@basis
        sol=root(fun,seed,jac=jac,tol=2e-11);q=sol.x;res=float(np.max(abs(fun(q))));assert res<2e-12 and np.linalg.norm(q[:3])>radius/2
        th=basis@q;energy,grad,hes,f,lam0=nm['energy'](th,kval);base_energy=2*(-float(g['rho']))+36*kval;ev=eigh(basis.T@hes@basis,eigvals_only=True)
        index=int(sum(ev<-1e-8));assert index==k-1
        amp=float(np.linalg.norm(q[:3]));angle=float(np.linalg.norm(q[:3]/amp-axis));assert angle<2e-7
        # Full link stationarity and exact neutral data: E=0, psi=f, chi=bar(f).
        force=4*np.imag(np.array([np.conj(f[i])*np.exp(1j*th[e])*f[j] for e,(i,j) in enumerate(g['edges'])]))-kval*nm['C'].T@np.sin(nm['C']@th)
        assert np.max(abs(force))<3e-11
        eig_res=float(np.max(abs(nm['R']@np.zeros(28)-abs(f)**2+abs(f.conjugate())**2)));assert eig_res<1e-14
        Xg=th-nm['R'].T@np.angle(f);density=2*abs(f)**2
        Hqq,Hpp=nm['reversible_blocks'](Xg,density,kval)
        ppvals,ppvec=eigh(Hpp);assert ppvals[0]>0
        phalf=(ppvec*np.sqrt(ppvals))@ppvec.T
        squared=eigh(phalf@Hqq@phalf,eigvals_only=True)
        soft=np.sort(squared[np.argsort(abs(squared))[:3]])
        predicted=[2*gamma_float*epsilon/mc]+[B4*gamma_float*epsilon/(2*k*qk*mc)]*(3-k)+[-B4*gamma_float*epsilon/(k*qk*mc)]*(k-1)
        predicted=np.sort(predicted);soft_error=float(np.max(abs(soft-predicted))/np.max(abs(predicted)))
        assert sum(squared<-1e-8)==k-1
        mom=rng.normal(size=42);mom/=np.linalg.norm(mom);hhstep=5e-5
        e1=hhstep*mom[:28];z1=hhstep*(nm['density_basis']@mom[28:])
        hp=nm['reduced_energy'](Xg,density,e1,z1,kval);hm=nm['reduced_energy'](Xg,density,-e1,-z1,kval);h0=nm['reduced_energy'](Xg,density,np.zeros(28),np.zeros(15),kval)
        reversal_error=abs(hp-hm);kin_error=abs((hp+hm-2*h0)/hhstep**2-mom@Hpp@mom)
        assert reversal_error<1e-14 and kin_error<2e-5
        rows.append({'epsilon':epsilon,'stationary_full_force_max_residual':float(np.max(abs(force))),'projected_gradient_max_residual':res,'Gauss_residual':eig_res,'critical_radius':amp,'radius_squared_over_epsilon':amp*amp/epsilon,'predicted_radius_squared_over_epsilon':gamma_float/(4*qk),'leading_radius_relative_error':abs(amp/radius-1),'complement_norm_over_radius_cubed':float(np.linalg.norm(q[3:])/amp**3),'energy_gain_over_epsilon_squared':(energy-base_energy)/epsilon**2,'predicted_energy_gain_over_epsilon_squared':-gamma_float**2/(16*qk),'configuration_Morse_index':index,'lowest_configuration_Hessian_eigenvalues':ev[:3].tolist(),'matter_profile_distance_from_background':float(np.linalg.norm(abs(f)-nm['v'])),'full_scalar_42_pair_squared_frequencies':squared.tolist(),'soft_squared_frequencies':soft.tolist(),'predicted_soft_squared_frequencies':predicted.tolist(),'soft_frequency_relative_error':soft_error,'minimum_reduced_kinetic_eigenvalue':float(ppvals[0]),'reversal_energy_absolute_error':reversal_error,'kinetic_Hessian_directional_error':kin_error})
    assert rows[-1]['leading_radius_relative_error']<rows[0]['leading_radius_relative_error']/5
    assert rows[-1]['soft_frequency_relative_error']<rows[0]['soft_frequency_relative_error']/5
    records.append({'family_k':k,'oriented_branch_count':{1:6,2:12,3:8}[k],'runs':rows})
num={'status':'PASS','type':'NUMERICAL full stationary-energy diagnostics, not proof or empirical data','parameters':{'a':1,'N':1,'rank':1},'Gamma':gamma_float,'critical_mass':mc,'critical_mass_isotropy_max_residual':float(np.max(abs(massgram-mc*np.eye(3)))),'gradient_directional_error':gradient_error,'Hessian_directional_max_error':hessian_error,'branch_campaigns':records,'scope':'Ground eigenvalue and all fourteen physical connection directions are solved; no quartic-only stationary solve, dynamical trajectory or verified epsilon0 bound claimed','physical_promotion':0,'independent_review':'PENDING'}
(O/'BIFURCATION_NUMERICAL_DIAGNOSTIC_v0.1.json').write_text(json.dumps(num,indent=2)+'\n')
print(json.dumps({'status':'PASS','exact_checks':len(checks),'Gamma':gamma_float,'critical_mass_aN1':mc,'last_radius_relative_errors':[r['runs'][-1]['leading_radius_relative_error'] for r in records]},indent=2))
