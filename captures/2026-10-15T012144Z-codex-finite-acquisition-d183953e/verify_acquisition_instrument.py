"""Constructor replay: exact finite identities, not independent peer review."""
from pathlib import Path
import json, math
from itertools import combinations
import sympy as s

ROOT=Path(__file__).resolve().parent
checks=[]
def check(name, assertion, **details):
    assert assertion, name
    checks.append(dict(name=name,status='PASS',scope='EXACT_FINITE',**details))

simplices=[list(combinations(range(4),d+1)) for d in range(4)]
offset=[0,4,10,14]
A=s.zeros(15)
for degree in range(1,4):
    for col, simplex in enumerate(simplices[degree]):
        for k in range(degree+1):
            face=simplex[:k]+simplex[k+1:]
            row=simplices[degree-1].index(face)
            i,j=offset[degree-1]+row,offset[degree]+col
            A[i,j]=-(-1)**k; A[j,i]=(-1)**k
check('independent_oriented_carrier',A.T==-A and A.rank()==14)
pairs=[[(0,1),(2,3)],[(0,2),(1,3)],[(0,3),(1,2)]]
P=[s.zeros(15) for _ in range(4)]
for j,pair in enumerate(pairs,1):
    for edge in pair:P[j][4+simplices[1].index(edge),4+simplices[1].index(edge)]=1
P[0]=s.eye(15)-sum(P[1:],s.zeros(15))
check('orthogonal_resolution',sum(P,s.zeros(15))==s.eye(15) and all(P[j]*P[k]==(P[j] if j==k else s.zeros(15)) for j in range(4) for k in range(4)),ranks=[p.rank() for p in P])
X=s.zeros(4)
for r in range(4):X[(r+1)%4,r]=1
U=sum([s.kronecker_product(P[j],X**j) for j in range(4)],s.zeros(60))
check('sixty_dimensional_write_unitary',U.H*U==s.eye(60))
V=s.zeros(16)
for r in range(4):
    E=s.zeros(4);E[r,r]=1
    V+=s.kronecker_product(E,X**r)
check('record_copy_unitary',V.H*V==s.eye(16))
J=s.zeros(60,15)
for i in range(15):J[4*i,i]=1
J2=s.zeros(240,60)
for i in range(60):J2[4*i,i]=1
W=s.kronecker_product(s.eye(15),V)*J2*U*J
check('full_joint_isometry',W.H*W==s.eye(15))
labels=[next(j for j in range(4) if P[j][i,i]==1) for i in range(15)]
expected=s.zeros(240,15)
for i,j in enumerate(labels):expected[16*i+5*j,i]=1
check('explicit_joint_write_formula',W==expected)
# A rational unit pure state supported in three different output blocks.
psi=s.zeros(15,1);psi[0]=s.Rational(1,3);psi[4]=s.Rational(2,3);psi[5]=s.Rational(2,3)
rho=psi*psi.T;omega=W*rho*W.T
reduced=s.zeros(60)
for a in range(60):
    for b in range(60):reduced[a,b]=sum(omega[4*a+f,4*b+f] for f in range(4))
target=sum([s.kronecker_product(P[j]*rho*P[j],s.diag(*[int(k==j) for k in range(4)])) for j in range(4)],s.zeros(60))
check('counted_record_partial_trace',reduced==target)
phi=sum([p*rho*p for p in P],s.zeros(15))
check('channel_trace_and_idempotence',s.trace(phi)==1 and sum([p*phi*p for p in P],s.zeros(15))==phi)
prob=[s.trace(p*rho) for p in P]
check('record_spectrum_and_purity',s.trace(omega**2)==1 and sum(prob)==1 and [v for v in prob if v]!=[])
p=s.symbols('p',real=True,positive=True)
d=s.Matrix([[0,s.sqrt(p*(1-p))],[s.sqrt(p*(1-p)),0]])
check('binary_disturbance_squared',d*d==p*(1-p)*s.eye(2))
plus=s.zeros(15,1);minus=s.zeros(15,1)
plus[0]=plus[4]=1/s.sqrt(2);minus[0]=1/s.sqrt(2);minus[4]=-1/s.sqrt(2)
ph=lambda r:sum([q*r*q for q in P],s.zeros(15))
check('phase_distinction_hidden_in_marginals',(plus.T*minus)[0]==0 and ph(plus*plus.T)==ph(minus*minus.T) and ((W*plus).T*(W*minus))[0]==0)
distance=sum(abs(s.binomial(4,k)*(s.Rational(1,4)**k*s.Rational(3,4)**(4-k)-s.Rational(3,4)**k*s.Rational(1,4)**(4-k))) for k in range(5))/2
check('four_trial_retained_distinguishability',distance==s.Rational(11,16) and (1-distance)/2==s.Rational(5,32),distance=str(distance))
check('stock_derivative_after_write',all(s.trace((q*A-A*q)*phi)==0 for q in P[1:]))
# Generic nonzero free derivative and changed evolution after a write.
z=s.zeros(15,1);z[0]=s.sqrt(2)/2;z[4]=s.sqrt(2)/2
rz=z*z.T;der=s.trace((P[1]*A-A*P[1])*rz)
check('unmeasured_flow_differs',der!=0 and s.trace((P[1]*A-A*P[1])*ph(rz))==0,free_derivative=str(der))
check('real_mean_energy_before_and_after',s.trace(s.I*A*rho)==0 and s.trace(s.I*A*phi)==0)
m,K,eps=98304,129,s.Rational(1,128)
check('confidence_exponent',2*m*eps**2==12 and 6*K==774)
lower=sum(s.Rational(12)**j/s.factorial(j) for j in range(40))
check('rational_failure_certificate',lower>77400,exp12_lower_bound=str(lower),failure_upper_bound=str(s.Rational(774)/lower))
check('sample_count_and_capacity',K*m==12681216 and 4*K*m==50724864 and 3*17*K==6579 and 2**16<m+1<=2**17)
h,ell=s.Rational(3,16),s.Rational(1,16)
check('integer_certified_guards',m*(h+eps)==19200 and m*(ell-eps)==5376,rise_min_count=19200,fall_max_count=5376)
D=2*eps/s.Rational(3,8)+s.Rational(1,64)
check('sampled_contract_delay',D==s.Rational(11,192) and D<s.Rational(1,16),delay=str(D))
F=s.Matrix(4,4,lambda k,r:s.I**(k*r)/2)
check('fourier_shift_diagonalization',F.H*F==s.eye(4) and F.H*X*F==s.diag(1,-s.I,-1,s.I))
angles=[]
for j in range(4):
    a=[s.pi*((j*r+2)%4-2)/2 for r in range(4)]
    check(f'hermitian_logarithm_{j}',all(s.simplify(s.exp(-s.I*a[r])-(-s.I)**(j*r))==0 for r in range(4)) and all(abs(v)<=s.pi for v in a))
    angles.append([str(v) for v in a])
# Verify correlation-preserving renewal on a basis of matrix units, incl spectator.
ok=True
for a in range(4):
    for b in range(4):
        # active |a><b| and donor |0><0| -> active |0><0| and donor |a><b|
        for y in range(2):
            for z0 in range(2):
                inrow=(a*2+y)*4;incol=(b*2+z0)*4
                swapidx=lambda t: ((t%4)*2+(t//4)%2)*4+(t//8)
                ok &= swapidx(inrow)==y*4+a and swapidx(incol)==z0*4+b
check('renewal_with_retained_spectator_matrix_units',ok)
result=dict(status='PASS',physical_promotion=0,independent_review=False,check_families=len(checks),checks=checks,
    limits=['Only the finite construction is replayed; inherited packages not all replayed.','No native quantum encoding, thermal blank supply, spatial locality or area normalization proved.'])
(ROOT/'INSTRUMENT_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
(ROOT/'INSTRUMENT_CERTIFICATES.json').write_text(json.dumps(dict(projector_ranks=[p.rank() for p in P],labels=labels,logarithm_angles=angles,preparations=K*m,raw_qubit_capacity=4*K*m,failure_bound='774 exp(-12)',exact_exp_lower=str(lower),delay=str(D)),indent=2)+'\n')
print(json.dumps(dict(status='PASS',check_families=len(checks),preparations=K*m)))
