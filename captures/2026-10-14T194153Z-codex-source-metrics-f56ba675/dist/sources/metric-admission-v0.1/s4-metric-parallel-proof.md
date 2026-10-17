# Signed S4 and degree-isotropic metric: parallel constructor check

Status: exact finite mathematical verification. Constructor-team AI audit, not
independent human review. Physical promotion 0. No archived source code executed.

Primary text read: atlas catalog C0190 (Exact S4 chain projectors), C0200 (full
versus skew commutant), and C0258 (Paper III draft 1.1.1, section 2.3). These
sources retain separate operator selection and physical realization debts.

## Carrier and exact checks

Increasing simplex orientation gives chain dimensions (4,6,4,1). The signed
vertex-permutation action has 24 orthogonal matrices. New generated Fraction
code builds boundaries and checks all actions. Let A_k=D_k^T-D_k on adjacent
degrees. Boundary ranks are (3,3,1), skew ranks (6,6,2). The matrices satisfy
A_i A_j=0 for i unequal j, A_k^2=-4P_k, and P_0+P_1+P_2+P_3=I. The orthogonal
projector ranks are (1,6,6,2). Positive frequency multiplicities are (3,3,1).

The full character inner product (1/24) sum_g trace(R_g)^2 is 13. An explicit
13-member rational commuting basis has rank 13: P_0 plus, for each k,
Q_(k-1)P_k, (I-Q_(k-1))P_k, Q_(k-1)A_k-A_k Q_(k-1), A_k. The first ten are
symmetric and the last three skew. Thus full/symmetric/skew dimensions are
13/10/3, matching the source classification.

For G=diag(g_0 I_4,g_1 I_6,g_2 I_4,g_3 I_1), g_k>0, the boundary adjoint is
D^dagger=G^-1 D^T G. The weighted skew operator A_G=D^dagger-D is G-skew and
commutes with the signed action. With ratios r_k=g_(k-1)/g_k,

    det(lambda I-A_G)=lambda (lambda^2+4r_1)^3
                            (lambda^2+4r_2)^3 (lambda^2+4r_3).

The checker verifies all 16 characteristic coefficients for four rational
positive metrics, rather than comparing rounded numerical eigenvalues. Under
the metric normalization S=G^(1/2), S A_G S^-1 has channel coefficients
sqrt(r_k). These coefficients are mathematical family coordinates, not newly
selected native couplings.

Any positive S4-invariant metric also has a square root commuting with R_g.
Consequently any real G-skew S4-equivariant operator becomes unit-metric skew
equivariant under that normalization and has at most three distinct positive
bands. Arbitrary invariant metrics may mix equivalent representation copies;
the displayed ratio formula, unlike this band-count argument, is specifically
for degree-isotropic metrics and the declared boundary-adjoint generator.

## Exact spectral-cover relaxation

For even programmed-clock gate count n=2M, its distinct positive spectral
targets in kappa units are 2,4,...,2M. A three-band candidate may be relaxed to
three unrestricted positive centers together with a fixed zero center. The
optimal nearest-center radius is

    r_M=min { integer r>=0 : M <= floor(r/2)+3(r+1) }.

Proof: at radius epsilon, fixed zero covers at most floor(epsilon/2) positive
targets; each free interval of width 2epsilon covers at most
floor(epsilon)+1 targets at spacing 2. Hence their union covers at most
floor(epsilon/2)+3(floor(epsilon)+1). This count can increase only at integer
epsilon. Conversely, at integer r, assign a prefix of at most floor(r/2)
targets to zero and partition the rest into at most three consecutive blocks,
each of size at most r+1. Center each block at its endpoint midpoint. Every
assigned distance is at most r. This proves the formula, including sharpness.

An independent exhaustive ordered-partition computation for M=1,...,64 tests
722,864 partitions, computing the exact maximum of the fixed-zero prefix cost
and free-block half spans. It agrees with the formula. For the default M=5,
radius 1 is attained by free centers (3,7,10). A radius below 1 would allow only
one positive target per free center, so cannot cover five positive targets.

These centers are deliberately an unconstrained relaxation witness. No source
selects that metric, and no full isometry with native multiplicities or locality
has been constructed. The relaxation yields a lower bound on the declared
generator residual comparison, not on endpoint evolution error.

## Exact embedding scope

For even n>=8, the programme has at least four distinct positive bands. One
signed fifteen-coordinate S4-equivariant skew carrier has at most three.
Identical uncoupled copies and one common rate do not introduce additional
distinct bands. Exact full-generator invariant isometric embedding is therefore
impossible in that class. Different metrics on different copies, symmetry
breaking, inter-copy coupling, larger complexes, restricted-input endpoint
comparisons or capture mechanisms are different classes and are not excluded
by this statement.

No source-selected parameter, physical clock calibration, energy, local
implementation, protected record export or restart supply is certified.
