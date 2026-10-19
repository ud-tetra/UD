# Coefficient-weighted graph certificate: review candidate

Same-team mathematical review. Development only; physical promotion 0.
This file derives sufficient conditions, not a numerical PASS. No parent
artifacts, radius, gate, fits, or estimator are changed.

## 1. Orthogonal source coordinates

Let L=QC, Q^T Q=I_q, C full row rank, and let alpha<=sigma_min(C),
M>=||C||_2. Let Btilde=L+Delta, e>=||Delta||_2,
f>=||Delta^T Q||_F, w>=||Delta C^dagger||_F.
An F certificate for Delta supplies f; alternatively f<=sqrt(q)e.

In the orthogonal coordinates [Q,Qperp], partition H=Btilde Btilde^T
into H11,H12,H21,H22 and set R=CC^T. Then

    ||H22||_2 <= e^2
    ||H11-R||_2 <= 2Me+e^2
    ||H12||_2 <= e(M+e)
    ||H21 R^-1||_F <= z := w+ef/alpha^2.

The last identity follows from
H21 R^-1=Qperp^T Delta C^dagger+
Qperp^T Delta Delta^T Q R^-1. This is where coefficient weighting
replaces the coarse ||Delta||_F/alpha estimate.

## 2. Existence, not merely a graph inequality

Define a=(2Me+2e^2)/alpha^2 and b=e(M+e)/alpha^2. Choose x>0
satisfying all strict/non-strict gates

    z+a*x+b*x^2 <= x
    a+2*b*x < 1
    alpha > 2e
    ((alpha-e)^2-2e(M+e)x)/(1+x^2) > e^2.

The Riccati map

    T(W)=H21 R^-1+H22 W R^-1
         -W(H11-R)R^-1-W H12 W R^-1

maps the Frobenius ball ||W||_F<=x to itself and has Lipschitz
constant at most a+2bx there. Banach gives a unique invariant graph.
Its Rayleigh quotient is at least the left side of the final gate.
By minmax, lambda_(q+1)(H)<=||H22||_2<=e^2. The invariant q-graph
is therefore the leading left singular subspace, not an unspecified
invariant subspace.

For its principal angles, tan(theta_i)=s_i(W), and
2(1-cos(theta_i))<=tan(theta_i)^2. A common orthogonal alignment
therefore has operator and Frobenius distances both at most x.

## 3. Parent nonorthogonal basis

For parent L=U0 C0, put G=U0^T U0 and Q=U0 G^-1/2.
Then C=G^1/2 C0 and C^dagger=C0^dagger G^-1/2.
The parent eta0 bounds ||G-I||_2, so ||G^-1/2||_2<=1/sqrt(1-eta0).

To certify C0^dagger, propose a dyadic Z and form K=C0^T Z EXACTLY.
If rho=||C0K-I||_2<1, K lies exactly in row(C0), and

    C0^dagger=K(C0K)^-1.

Thus ||Delta C^dagger||_F is at most
||Delta K||_F/((1-rho)sqrt(1-eta0)). An arbitrary right inverse
without certified row-space membership cannot be substituted here.

## 4. Whole encoded-ball weighting

At raw radius delta=2^-48, each encoded 62-vector perturbation is
zero or plus/minus one coordinate quantum. Set T=S K. Preparation a
uses row indices 37c+a, c=0,...,61. Then

    ||Eraw S K||_F <= delta sqrt(n) sum_a max_c ||T[37c+a,:]||_2.

This is an encoded-lattice theorem; it is not automatically a theorem
for arbitrary real perturbations in the same Euclidean ball.
For real perturbations the safe analogous bound uses the operator
norm of each 62-by-q preparation block instead of its largest row norm.

An optional sharper lattice bound squares the per-time expression:
h_a=max_c||t_ac||_2^2, g_ab=max_cd|<t_ac,t_bd>| imply
||Eraw T||_F^2<=n delta^2(sum_a h_a+2 sum_(a<b)g_ab).

The baseline weighted norm ||(B0-U0C0)K||_F is separately computable
by exact cross-Grams. Add it to the raw-noise weighted bound.
A returned-helper F error epsilonF contributes at most epsilonF||K||_2;
an operator-only error epsilon2 instead contributes at most
epsilon2||K||_F. Apply the pseudoinverse/polar denominator above.

## 5. Shift consequence and limits

For ideal top-q basis, take d_2,d_F<=x. In the parent's returned-factor
lane retain its existing polar adjustment d_2,d_F<=x+2p(eta).
The unchanged Frobenius exact-LS shift bound is

    Jgraph=sqrt(1+eta)[sigma0,F+(1+M0)(x+2p(eta))].

The normal-residual Pythagorean correction for a returned shift remains
separate. No uniform floating-library success is implied. Whether this
passes the published allowance requires fresh validated constants and
all graph gates; it is not established in this review.

There is no general large reduction of the shift-difference constant
from source isometry alone: admitted period-four raw signs have lag-two
multiplier -1, nearly opposite the low-frequency source multiplier.

