"""Exact C3 selection, metric commutant and passive bath algebra."""
from fractions import Fraction as F
import json


def mm(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def tr(a):
    return [list(row) for row in zip(*a)]


def sub(a,b):
    return [[a[i][j]-b[i][j] for j in range(2)] for i in range(2)]

I=[[F(1),F(0)],[F(0),F(1)]]
R=[[F(-1),F(-1)],[F(1),F(0)]]
G=[[F(1),F(1,2)],[F(1,2),F(1)]]
assert mm(R,mm(R,R))==I
assert mm(tr(R),mm(G,R))==G
# (R-I)c=0 has zero kernel, as det(R-I)=3.
A=sub(R,I)
assert A[0][0]*A[1][1]-A[0][1]*A[1][0]==3
# Any commuting matrix [[u,v],[w,t]] has v=-w, u=t-w.
for t,w in [(F(2),F(3)),(F(1,3),F(-5,7)),(F(0),F(1))]:
    C=[[t-w,-w],[w,t]]
    assert mm(C,R)==mm(R,C)
    rho2=t*t-t*w+w*w
    assert mm(tr(C),mm(G,C))==[[rho2*G[i][j] for j in range(2)] for i in range(2)]
    k0,kappa,d=F(13),F(5),F(2)
    delta=rho2/kappa
    gamma=d*rho2/(kappa*kappa)
    assert gamma==delta*d/kappa
    # Stability condition is separate; it need not hold for every sample.
    if k0*kappa>rho2:
        assert 0<=delta<k0
# The frequency expansion (kappa-i omega d)^-1 = kappa^-1
# + i omega d kappa^-2 + O(omega^2): exact formal first-order coefficients.
for kappa,d,rho2 in [(F(5),F(2),F(7,3)),(F(3),F(0),F(1))]:
    inv0=1/kappa
    inv1=d/(kappa*kappa)
    assert kappa*inv0==1
    assert kappa*inv1-d*inv0==0
    assert rho2*inv1==d*(rho2*inv0)/kappa
# Weighted relaxation-time bound for two doublets using exact rationals.
weight=[F(3,7),F(5,11)]
tau=[F(1,4),F(7,6)]
avg=sum(w*t for w,t in zip(weight,tau))/sum(weight)
assert min(tau)<=avg<=max(tau)
print(json.dumps({'status':'EXACT_CONDITIONAL_CONSTRUCTOR_CHECK',
                  'c3_fixed_scalar_linear_coupling':'zero',
                  'E_commutant_dimension':2,
                  'C3_invariant_norm':'t^2-t*w+w^2 in lattice coordinates',
                  'damping_to_softening':'d/kappa',
                  'checks':['R^3=I','metric isometry','scalar no-go',
                            'commutant examples','passive low-frequency expansion',
                            'stability condition','two-bath relaxation bound']},indent=2))
