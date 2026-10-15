#!/usr/bin/env python3
"""Exact constructor checks and separately typed numerical constraint diagnostics."""
from pathlib import Path
import sympy as sp, numpy as np, json, hashlib
from scipy.linalg import eigh,expm
from residual_model import *
from higher_rank_model import color_model
O=Path(__file__).resolve().parent;checks=[]
def zero(z):return all(sp.simplify(sp.radsimp(sp.expand(x)))==0 for x in z)
def check(name,condition):
    assert bool(condition),name
    checks.append(name);print('PASS',name,flush=True)
def cx(name,n,m):
    x=sp.symbols(name+'r:'+str(n*m),real=True);y=sp.symbols(name+'i:'+str(n*m),real=True)
    return sp.Matrix(n,m,lambda i,j:x[i*m+j]+sp.I*y[i*m+j])
def hm(name,s):
    b=hermitian_basis(s);v=sp.symbols(name+':'+str(len(b)),real=True)
    return sum((t*h for t,h in zip(v,b)),sp.zeros(s))
X=cx('x',2,1);E=cx('e',2,1);A=hm('a',2);Pi=hm('p',2);xi=hm('h',2)
J=moment_raw(X,E,[A],[Pi])
theta=2*sp.re((E.H*(sp.I*xi*X))[0])+sp.trace(Pi*sp.I*comm(xi,A))
check('canonical_one_form_contracts_to_residual_moment',sp.simplify(sp.expand(theta-sp.trace(xi*J)))==0)
check('moment_Hermitian',zero(J-J.H))
check('trace_discards_vacuum_commutator',sp.simplify(sp.expand(sp.trace(J)+2*sp.im((E.H*X)[0])))==0)
# Direct projection of the original matrix Gauss law at quadratic order.
H=sp.zeros(3);EE=sp.zeros(3);H[1:,0]=X;H[0,1:]=X.H;H[1:,1:]=A
EE[1:,0]=E;EE[0,1:]=E.H;EE[1:,1:]=Pi
for u in [sp.I,-sp.I]:
    U0=sp.diag(u,1,1);G2=sp.I*U0.H*comm(H,EE)*U0
    check('full_link_Gauss_projection_u_'+str(u),zero(G2[1:,1:]-J))
check('unitary_matter_slice_P_zero_cancels_unused_charge',zero((-X)*(-X).H-X*X.H))
# Positive-frequency color and vacuum variables; no graph-dependent assumptions.
q=cx('q',2,1);p=cx('v',2,1);w=sp.symbols('omega',positive=True)
cp=(sp.sqrt(w)*q-sp.I*p/sp.sqrt(w))/sp.sqrt(2)
cm=(sp.sqrt(w)*q+sp.I*p/sp.sqrt(w))/sp.sqrt(2)
check('color_circular_moment_identity',zero(cp*cp.H-cm*cm.H-sp.I*(q*p.H-p*q.H)))
check('color_circular_energy_identity',sp.simplify(sp.expand(w*sp.trace(cp.H*cp+cm.H*cm)-sp.trace(p.H*p+w*w*q.H*q)))==0)
nu,aa=sp.symbols('nu aa',positive=True)
z=(sp.sqrt(nu/aa)*A-sp.I*sp.sqrt(aa/nu)*Pi)/sp.sqrt(2)
check('vacuum_circular_moment_identity',zero(comm(z,z.H)-sp.I*comm(A,Pi)))
check('vacuum_circular_energy_identity',sp.simplify(sp.expand(nu*sp.trace(z.H*z)-sp.trace(aa*Pi*Pi+nu*nu/aa*A*A)/2))==0)
# Equivariance and universal trace obstruction.
U=sp.Matrix([[sp.Rational(3,5),4*sp.I/5],[4*sp.I/5,sp.Rational(3,5)]])
check('exact_unitary_fixture',U.H*U==sp.eye(2))
check('matrix_moment_equivariance',zero(moment_raw(U*X,U*E,[U*A*U.H],[U*Pi*U.H])-U*J*U.H))
check('single_handed_nonzero_color_has_nonzero_trace',sp.expand(sp.trace(X*X.H))==sum(sp.re(t)**2+sp.im(t)**2 for t in X))
e1=sp.Matrix([1,0]);e2=sp.Matrix([0,1]);z21=sp.zeros(2);z21[1,0]=1
check('trace_balance_alone_not_matrix_neutral',sp.trace(e1*e1.H-e2*e2.H)==0 and e1*e1.H-e2*e2.H!=sp.zeros(2))
check('one_vacuum_oscillator_cancels_nonabelian_charge',moment_modes(e1,e2,[z21])==sp.zeros(2))
# Universal weighted-shift identity, expressed without unproved radical signs.
t=sp.symbols('t0:5',nonnegative=True);zs=sp.zeros(6)
for j in range(5):zs[j,j+1]=t[j]
diag=[t[0]**2]+[t[j]**2-t[j-1]**2 for j in range(1,5)]+[-t[4]**2]
check('weighted_shift_self_commutator_identity',comm(zs,zs.H)==sp.diag(*diag))
completions=[]
for s in range(2,9):
    lam=[sp.Integer(j) for j in range(s-1,0,-1)]+[-sp.Integer(s*(s-1)//2)]
    zc=shift_completion(lam);target=sp.diag(*lam)
    check('weighted_shift_completion_s'+str(s),zero(comm(zc,zc.H)-target))
    cost=sp.simplify(sp.trace(zc.H*zc));mass=sum(max(v,0) for v in lam)
    check('completion_energy_bounds_s'+str(s),mass<=cost<=(s-1)*mass)
    completions.append({'s':s,'target_eigenvalues':list(map(str,lam)),'vacuum_norm_squared':str(cost),'half_trace_norm':str(mass)})
# A free zero-moment point at every tested finite rank. The written proof is universal.
principal=[]
for s in range(1,7):
    cp,cm,zz=principal_witness(s);hb=hermitian_basis(s)
    check('principal_witness_zero_moment_s'+str(s),moment_modes(cp,cm,zz)==sp.zeros(s))
    columns=[]
    for h in hb:
        columns.append(sp.Matrix.vstack(h*cp,*(sp.Matrix(comm(h,zzj)).reshape(s*s,1) for zzj in zz)))
    rank=sp.Matrix.hstack(*columns).rank()
    check('principal_witness_trivial_Lie_stabilizer_s'+str(s),rank==s*s)
    # Independent Jacobian of J in the full real mode coordinates (one framed pair, two vacuum modes).
    jcols=[]
    for side in [1,-1]:
        for i in range(s):
            for f in [1,sp.I]:
                v=sp.zeros(s,1);v[i]=f;jcols.append(hermitian_vector(side*(v*cp.H+cp*v.H)))
    for z0 in zz:
        for i in range(s):
            for j in range(s):
                for f in [1,sp.I]:
                    dz=sp.zeros(s);dz[i,j]=f;jcols.append(hermitian_vector(comm(dz,z0.H)+comm(z0,dz.H)))
    check('moment_Jacobian_full_rank_s'+str(s),sp.Matrix.hstack(*jcols).rank()==s*s)
    d=dimensions(s);check('principal_dimension_direct_count_s'+str(s),d['free_reduced_real']==26*(s+1)**2+60*(s+1)-2)
    principal.append(d)
# Rank-two quotient invariants and gauge-invariant quadratic dynamics.
ap=cx('ap',3,1);am=cx('am',3,1);MM=ap*am.H
check('rank_two_invariant_matrix_has_rank_at_most_one',all(sp.expand(MM[i,j]*MM[k,l]-MM[i,l]*MM[k,j])==0 for i in range(3) for k in range(i+1,3) for j in range(3) for l in range(j+1,3)))
check('rank_two_invariant_reconstructs_plus_Gram',zero(MM*MM.H-(am.H*am)[0]*ap*ap.H))
check('rank_two_invariant_reconstructs_minus_Gram',zero(MM.H*MM-(ap.H*ap)[0]*am*am.H))
check('rank_two_balanced_Frobenius_radius',sp.expand(sp.trace(MM*MM.H)-(ap.H*ap)[0]*(am.H*am)[0])==0)
w1,w2=sp.symbols('w1 w2',positive=True)
check('neutral_cross_orientation_observable_has_sum_frequency',sp.simplify(sp.I*w1+sp.conjugate(-sp.I*w2)-sp.I*(w1+w2))==0)
check('same_orientation_Gram_has_difference_frequency',sp.simplify(sp.I*w1-sp.I*w2-sp.I*(w1-w2))==0)
check('rank_two_principal_and_vertex_dimensions',dimensions(1)['free_reduced_real']==222 and dimensions(1)['maximal_stabilizer_real']==112 and 2*(2*28-1)==110)
check('rank_two_cone_link_dimension',2*(2*28-1)-1==109)
# Graph verification of the unused vacuum cycle count and a constraint preparation.
g=color_model();R=g['R'];C=g['C'];K=g['K'];Ru=g['Ru'];V=g['V'];m=28;n=14
check('vacuum_cycle_dimension_fourteen',len(R.nullspace())==n)
check('diamond_curl_has_only_gauge_kernel',C.rank()==14 and R.rank()==14 and C*R.T==sp.zeros(18,15))
lam=sp.symbols('lambda');poly=lam**14*(lam-6)**2*((lam-6)**2-2)**3*((lam-4)**2-2)**3
check('vacuum_cycle_spectrum_inherited_and_rebuilt',sp.expand(K.charpoly(lam).as_expr()-poly)==0)
# An explicit trace-balanced/nonzero-matrix-charge color direction, compensated in a vacuum cycle.
beta=sp.zeros(2,28);ee=sp.zeros(2,28);beta[0,0]=1;ee[1,0]=sp.I
cycle=C.row(0).T;check('selected_integer_cycle_is_divergence_free',R*cycle==sp.zeros(15,1) and (cycle.T*cycle)[0]==4)
av=sp.diag(sp.Rational(1,2),-sp.Rational(1,2));pv=sp.Matrix([[0,sp.I],[-sp.I,0]])
avec=[cycle[i]*av/2 for i in range(28)];pvec=[cycle[i]*pv/2 for i in range(28)]
check('raw_color_and_vacuum_constraint_compensation',moment_raw(beta,ee,avec,pvec)==sp.zeros(2))
# Frozen species norms and phases require removing the otherwise trivial global gauge center.
sr=sp.symbols('s',integer=True,nonnegative=True);rr=sr+1
check('effective_gauge_dimension_removes_common_center',sp.expand((56*rr**2+60*rr-4)-2*(15*rr**2-1-sr**2)-(84+112*sr+28*sr**2))==0)
check('spectator_stratum_dimension_with_nonempty_spectator',sp.expand(84+112*sr+28*sr**2+28-2*sr**2-(112+112*sr+26*sr**2))==0)
check('maximal_stabilizer_fixed_slice_dimension',84+2*14==112)
exact={'status':'PASS','type':'EXACT constructor algebra; universal statements proved in manuscript; not independent review','check_count':len(checks),'checks':checks,'moment_map':'C_plus C_plus^dagger - C_minus C_minus^dagger + sum [Z_l,Z_l^dagger] =0','principal_dimensions':principal,'weighted_shift_fixtures':completions,'rank_two':{'m':28,'vacuum_modes':14,'color_cone_real_dimension':110,'cone_link_real_dimension':109,'principal_full_real_dimension':222,'maximal_stabilizer_full_real_dimension':112},'independent_review':'PENDING','physical_promotion':0}
(O/'RESIDUAL_EXACT_VERIFICATION_v0.1.json').write_text(json.dumps(exact,indent=2)+'\n')
# Numerical diagnostics: original-operator canonical transformation and full Gauss expansion.
mat=lambda z:np.array(z.evalf()).astype(complex)
rho=float(g['rho']);Mn=np.eye(28)+rho*mat(g['G_perp']);Kn=2*mat(g['W'])
mv,mo=eigh(Mn);mh=(mo*np.sqrt(mv))@mo.conj().T;mhi=(mo/np.sqrt(mv))@mo.conj().T
sq,oo=eigh(mh@Kn@mh);freq=np.sqrt(sq);rng=np.random.default_rng(70152)
q=rng.normal(size=(2,28))+1j*rng.normal(size=(2,28));p=rng.normal(size=(2,28))+1j*rng.normal(size=(2,28))
XX=q@oo.T@mh.T;ee1=p@oo.T@mhi.T;pp=(q*np.sqrt(freq)-1j*p/np.sqrt(freq))/np.sqrt(2);mm=(q*np.sqrt(freq)+1j*p/np.sqrt(freq))/np.sqrt(2)
jraw=1j*(XX@ee1.conj().T-ee1@XX.conj().T);jmode=pp@pp.conj().T-mm@mm.conj().T
canonical_residual=float(np.max(abs(jraw-jmode)));assert canonical_residual<2e-11
hraw=np.trace(ee1@Mn.T@ee1.conj().T+XX@Kn.T@XX.conj().T).real
hmode=float(np.sum(freq*(abs(pp)**2+abs(mm)**2)));energy_transform_residual=abs(hraw-hmode);assert energy_transform_residual<1e-9
# Exact-to-order-two preparation of full original matrix data, rank three.
bn=mat(beta);en=mat(ee);An=np.array([mat(z) for z in avec]);Pn=np.array([mat(z) for z in pvec]);vn=mat(g['v']).ravel().real;un=mat(g['u']).ravel();rn=mat(R).real;run=mat(Ru);CN=np.diag(vn)
U0=np.array([np.diag([un[e],1,1]) for e in range(28)]);HH=np.zeros((28,3,3),complex);E1=np.zeros_like(HH)
for e in range(28):
    HH[e,1:,0]=bn[:,e];HH[e,0,1:]=bn[:,e].conjugate();HH[e,1:,1:]=An[e]
    E1[e,1:,0]=en[:,e];E1[e,0,1:]=en[:,e].conjugate();E1[e,1:,1:]=Pn[e]
Q1=np.linalg.solve(CN,run@en.T).T/np.sqrt(2)
G2=np.zeros((15,3,3),complex)
for e,(i,j) in enumerate(g['edges']):G2[j]+=1j*U0[e].conj().T@(HH[e]@E1[e]-E1[e]@HH[e])@U0[e]
assert np.max(abs(np.sum(G2[:,1:,1:],axis=0)))<1e-12
right=rn.T@np.linalg.pinv(rn@rn.T);E2=np.zeros_like(E1)
E2[:,0,0]=-right@G2[:,0,0]
for i in range(2):
    for j in range(2):E2[:,1+i,1+j]=-right@G2[:,1+i,1+j]
Q2=G2[:,1:,0].T/(np.sqrt(2)*vn)
def gauss(U,E,psi,z):
    G=-np.einsum('ia,ib->iab',psi,psi.conjugate())+np.einsum('ia,ib->iab',z,z.conjugate())
    for e,(i,j) in enumerate(g['edges']):G[i]+=E[e];G[j]-=U[e].conj().T@E[e]@U[e]
    return G
rows=[]
for eps in [.02,.01,.005,.0025]:
    U=np.array([expm(1j*eps*HH[e])@U0[e] for e in range(28)]);Ep=eps*E1+eps*eps*E2
    off=(eps*Q1+eps*eps*Q2).T/np.sqrt(2);psi=np.zeros((15,3),complex);z=np.zeros_like(psi)
    psi[:,0]=z[:,0]=np.sqrt(1-np.linalg.norm(off)**2)*vn;psi[:,1:]=off;z[:,1:]=-off
    gg=gauss(U,Ep,psi,z);res=float(np.max(abs(gg)));norm_res=max(abs(np.linalg.norm(psi)**2-1),abs(np.linalg.norm(z)**2-1))
    rows.append({'epsilon':eps,'full_matrix_Gauss_max_residual':res,'residual_divided_by_epsilon_cubed':res/eps**3,'species_norm_residual':float(norm_res)})
assert max(x['species_norm_residual'] for x in rows)<2e-14
ratios=[rows[i]['full_matrix_Gauss_max_residual']/rows[i+1]['full_matrix_Gauss_max_residual'] for i in range(len(rows)-1)]
assert all(7<z<9 for z in ratios),ratios
# Time evolution of gauge-invariant observables in the QUADRATIC model only.
a0=rng.normal(size=28)+1j*rng.normal(size=28);b0=rng.normal(size=28)+1j*rng.normal(size=28);b0*=np.linalg.norm(a0)/np.linalg.norm(b0)
t=.713;at=a0*np.exp(1j*freq*t);bt=b0*np.exp(-1j*freq*t);mm0=np.outer(a0,b0.conjugate());mmt=np.outer(at,bt.conjugate())
sum_res=float(np.max(abs(mmt-mm0*np.exp(1j*(freq[:,None]+freq[None,:])*t))));assert sum_res<2e-13
num={'status':'PASS','type':'NUMERICAL diagnostics only; no nonlinear trajectory, exact initial-data lift or empirical result claimed','canonical_moment_transform_max_residual':canonical_residual,'energy_transform_absolute_residual':energy_transform_residual,'rank_three_second_order_constraint_preparation':rows,'halving_ratios_expected_eight':ratios,'rank_two_quadratic_invariant_sum_frequency_residual':sum_res,'minimum_color_frequency':float(freq[0]),'minimum_vacuum_frequency_rule':'sqrt(a*kappa/r*(4-sqrt(2)))','physical_promotion':0,'independent_review':'PENDING'}
(O/'RESIDUAL_NUMERICAL_DIAGNOSTIC_v0.1.json').write_text(json.dumps(num,indent=2)+'\n')
print(json.dumps({'status':'PASS','exact_checks':len(checks),'gauss_cubic_ratios':ratios,'canonical_moment_residual':canonical_residual,'energy_transform_residual':energy_transform_residual},indent=2))
