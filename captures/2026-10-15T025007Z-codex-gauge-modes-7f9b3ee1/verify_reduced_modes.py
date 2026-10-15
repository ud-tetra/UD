#!/usr/bin/env python3
"""Exact constructor verification, separate diagnostic numerical witness."""
from pathlib import Path
import json,hashlib
import sympy as s
from sympy.polys.matrices import DomainMatrix
import numpy as np
from scipy.linalg import expm
from mode_model import graph,scalar,transverse,reduction,fast_rank
O=Path(__file__).resolve().parent;checks=[]
def check(name,v):
    assert bool(v),name
    checks.append(name)
    print('PASS',name,flush=True)
def zero(M):return all(s.simplify(x)==0 for x in M)
g=graph();B=g['B'];A=g['A'];R=g['R'];C=g['C'];K=g['K'];k=g['k'];S=g['S'];M=g['M']
z=s.symbols('z');t=s.symbols('t',real=True)
check('source_boundary_nilpotence',B*B==s.zeros(15))
check('native_kernel_and_square',A*k==s.zeros(15,1) and A*A==-4*(s.eye(15)-k*k.T/4))
check('closed_graph_ranks',fast_rank(R)==14 and fast_rank(C)==14)
check('diamond_divergence_identity',R*C.T==s.zeros(15,18))
check('background_stationary_and_neutral',A*k==s.zeros(15,1) and all(k[i]*k[j]==0 for i,j in g['edges']))
check('linear_Gauss_identity',R*M.T==S*A)
check('linear_gauge_identity',M*R.T==-A*S)
check('matter_parity_feedback_vanishes',M.T*A*M==s.zeros(28))
expectedK=z**14*(z-6)**2*((z-6)**2-2)**3*((z-4)**2-2)**3
check('full_exact_diamond_stiffness_characteristic',s.expand(K.charpoly(z).as_expr()-expectedK)==0)
ks=[s.Integer(0),s.Integer(6),6-s.sqrt(2),6+s.sqrt(2),4-s.sqrt(2),4+s.sqrt(2)]
Q=M[4:10,:];Pg=B[:4,4:10].T*B[:4,4:10]/4;Pc=s.eye(6)-Pg
check('edge_projectors_rank_three',Pg*Pg==Pg and Pc*Pc==Pc and fast_rank(Pg)==fast_rank(Pc)==3)
V=s.Matrix([[q**p for q in ks] for p in range(6)])
known_weights={'gradient':s.Matrix([s.Rational(28,17),0,s.Rational(3,17)+s.sqrt(2)/34,s.Rational(3,17)-s.sqrt(2)/34,0,0]),'cycle':s.Matrix([0,0,0,0,1+s.sqrt(2)/2,1-s.sqrt(2)/2])}
moment_matrices=[Q*K**j*Q.T for j in range(6)]
weights={};resolvents={}
for name,P in [('gradient',Pg),('cycle',Pc)]:
    w=known_weights[name];weights[name]=w
    # The six distinct eigenvalues and invertible Vandermonde identify every
    # spectral-projector weight from these full 6x6 moment identities.
    for j in range(6):
        target=s.expand(sum(wi*q**j for wi,q in zip(w,ks)))*P
        check(name+'_full_matrix_spectral_moment_'+str(j),zero(P*moment_matrices[j]-target))
    f=s.factor(sum(wi/(t*q-4) for wi,q in zip(w,ks)))
    resolvents[name]=f
fg=-2*(t-1)*(7*t-4)/(34*t*t-48*t+16)
fc=2*(5*t-4)/(14*t*t-32*t+16)
check('gradient_resolvent_closed_form',s.simplify(resolvents['gradient']-fg)==0)
check('cycle_resolvent_closed_form',s.simplify(resolvents['cycle']-fc)==0)
check('no_shared_residue_zero',s.degree(s.gcd(s.fraction(fg)[0],s.fraction(fc)[0]),t)==0)
check('coupled_resonance_weights_positive',all(wi>0 for wi in [weights['gradient'][2],weights['gradient'][3],weights['cycle'][4],weights['cycle'][5]]))
check('six_eigenvalue_field_sector_uncoupled',weights['gradient'][1]==weights['cycle'][1]==0)

L,G,T=scalar(g,kappa=s.Rational(1,2))
check('scalar_Gauss_constraint_and_gauge_ranks_15',fast_rank(G)==fast_rank(T)==15)
check('scalar_Gauss_preservation',G*L==s.zeros(15,116))
check('scalar_pure_gauge_stationary',L*T==s.zeros(116,15) and G*T==s.zeros(15))
Lp,PT,P0=reduction(g)
check('Coulomb_projector_exact',PT*PT==PT and R*PT==s.zeros(15,28) and fast_rank(PT)==14)
check('global_phase_projector_exact',P0*P0==P0 and P0*k==s.zeros(15,1) and fast_rank(P0)==14)
# Explicit quotient map from temporal-gauge perturbations to Coulomb variables.
th=slice(0,28);ee=slice(28,56);xx=slice(56,71);uu=slice(71,86);yy=slice(86,101);vv=slice(101,116)
Qred=s.zeros(116);Qred[th,th]=PT;Qred[ee,ee]=PT
Qred[xx,xx]=s.eye(15);Qred[xx,uu]=s.eye(15)
Qred[uu,xx]=s.eye(15);Qred[uu,uu]=-s.eye(15)
Qred[yy,yy]=s.eye(15);Qred[yy,vv]=s.eye(15)
Qred[vv,yy]=P0;Qred[vv,vv]=-P0;Qred[vv,th]=-2*P0*S*Lp*R
Lred=s.zeros(116);Lred[th,ee]=s.eye(28);Lred[ee,th]=-K/2;Lred[ee,xx]=2*PT*M.T
Lred[xx,uu]=A;Lred[uu,xx]=A;Lred[yy,vv]=A;Lred[yy,th]=2*M
Lred[vv,yy]=P0*A;Lred[vv,uu]=-4*P0*S*Lp*S
expected_defect=s.zeros(116,15);expected_defect[vv,:]=-2*P0*S*Lp
check('explicit_Coulomb_map_annuls_all_gauge_directions',Qred*T==s.zeros(116,15))
check('explicit_reduced_equations_modulo_Gauss',Qred*L-Lred*Qred==expected_defect*G)
# Full characteristic cross-check at one nonresonant rational parameter.
field=(z*z+6*t)**2*((z*z+6*t)**2-2*t*t)**3*((z*z+4*t)**2-2*t*t)**3
expected=s.Poly(z**32*(z*z+4)**28*field.subs(t,s.Rational(1,2)),z)
actual=DomainMatrix.from_Matrix(L).charpoly()
check('full_116_dimensional_characteristic_crosscheck',actual==expected.all_coeffs())
Lt,Gt,Tt=transverse(g,kappa=s.Rational(1,2))
check('transverse_color_Gauss_and_gauge_ranks_15',fast_rank(Gt)==fast_rank(Tt)==15)
check('transverse_color_Gauss_preservation',Gt*Lt==s.zeros(15,86))
check('transverse_color_pure_gauge',Lt*Tt==s.zeros(86,15) and Gt*Tt==s.zeros(15))
expT=s.Poly(z**30*(z*z+4)**14*field.subs(t,s.Rational(1,2)),z)
domainT=DomainMatrix.from_Matrix(Lt,extension=True)
actualT=domainT.charpoly()
check('full_86_complex_transverse_characteristic',[domainT.domain.to_sympy(x) for x in actualT]==expT.all_coeffs())

nullities=[]
fixtures=[('generic',s.Rational(1,2),[44,56,56]),('gradient_zero',s.Integer(1),[50,56,56]),('gradient_zero_4over7',s.Rational(4,7),[50,56,56]),('cycle_zero',s.Rational(4,5),[50,56,56]),('uncoupled_resonance',s.Rational(2,3),[48,60,60]),('coupled_resonance',4/(4+s.sqrt(2)),[44,56,62])]
for name,value,expect in fixtures:
    F,GG,TT=scalar(g,kappa=value);P=F*F+4*s.eye(116)
    result=[116-fast_rank(P**j) for j in [1,2,3]]
    check('Jordan_primary_nullities_'+name,result==expect)
    nullities.append({'fixture':name,'a':1,'effective_kappa':str(value),'nullities_L_squared_plus_four_powers':result})

# Exact nongauge, Gauss-admissible real Jordan witness at a=kappa=alpha=1.
F,GG,TT=scalar(g);P=F*F+4*s.eye(116)
basis=DomainMatrix.from_Matrix(P*P).to_field().nullspace().to_Matrix()
w=next(basis[row,:].T for row in range(basis.rows) if P*basis[row,:].T!=s.zeros(116,1))
w=w/max(abs(x) for x in w);v=P*w;growth=-F*v/8
check('exact_real_Jordan_witness',P*P*w==s.zeros(116,1) and v!=s.zeros(116,1))
check('witness_satisfies_linear_Gauss',GG*w==s.zeros(15,1) and GG*growth==s.zeros(15,1))
check('witness_fixed_species_norm_tangent',(k.T*w[56:71,:])[0]==0 and (k.T*w[71:86,:])[0]==0)
Qphys=s.eye(116)-TT*(TT.T*TT).inv()*TT.T
check('witness_growth_not_gauge',Qphys*growth!=s.zeros(116,1))
eta=growth[86:101,:]+growth[101:116,:]
check('witness_neutral_phase_sum_grows',eta!=s.zeros(15,1))
witness={'coordinate_order':['theta(28)','E(28)','Re delta psi(15)','Re delta chi(15)','Im delta psi(15)','Im delta chi(15)'],'parameters':{'a':1,'kappa':1,'alpha':1,'r':1,'mu_rotating_frame':0},'w':[str(x) for x in w],'growth_per_internal_time_at_s_equals_n_pi':[str(x) for x in growth],'exact_identity':'exp(L n pi) w = w + n pi growth, for every integer n','linear_Gauss':'PASS','growth_not_pure_gauge':True,'physical_promotion':0}
(O/'EXACT_JORDAN_WITNESS_v0.1.json').write_text(json.dumps(witness,indent=2)+'\n')
Fn=np.array(F).astype(float);wn=np.array(w).astype(float).ravel();gn=np.array(growth).astype(float).ravel();Qn=np.array(Qphys).astype(float)
errs=[];norms=[]
for j in [0,1,2,4]:
    numerical=expm(Fn*(j*np.pi))@wn;exact=wn+j*np.pi*gn
    errs.append(float(np.max(abs(numerical-exact))));norms.append(float(np.linalg.norm(Qn@numerical)))
assert max(errs)<1e-9
num={'status':'PASS','type':'NUMERICAL diagnostic only','method':'dense matrix exponential of exact linearization; compares exact Jordan identity','times_in_pi_units':[0,1,2,4],'max_absolute_identity_errors':errs,'gauge_orthogonal_solution_norms':norms,'nonlinear_stability_inference':'NONE from this numerical check','physical_promotion':0}
(O/'NUMERICAL_JORDAN_CROSSCHECK_v0.1.json').write_text(json.dumps(num,indent=2)+'\n')
report={'status':'PASS','type':'EXACT constructor checks supporting written universal proofs','check_count':len(checks),'checks':checks,'stiffness_spectrum':{'6':2,'6-sqrt(2)':3,'6+sqrt(2)':3,'4-sqrt(2)':3,'4+sqrt(2)':3,'0_removed_as_gradients':14},'scalar_regular_reduced_real_dimension':86,'general_rank_symplectic_slice_real_dimension':'28 r^2 + 56 r + 2; residual U(r-1) reduction remains for r>1','residue_functions':{'gradient':str(fg),'cycle':str(fc)},'Jordan_primary_fixtures':nullities,'vacuum_nonlinear_stability':'written conserved-functional proof for kappa>0; kappa=0 exact drift counterexample','nonzero_family':'spectrally stable but linearly unbounded for all a>0, kappa>=0, alpha>0; nonlinear Lyapunov status OPEN','review':'Constructor only, no independent review','physical_promotion':0,'verifier_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'model_sha256':hashlib.sha256((O/'mode_model.py').read_bytes()).hexdigest()}
(O/'REDUCED_MODES_EXACT_VERIFICATION_v0.1.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':'PASS','check_count':len(checks),'Jordan_fixtures':nullities,'numerical':num},indent=2))
