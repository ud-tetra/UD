# Conditional metric and observable selection: exact checks

Status: development theorem / constructor-team verification. Physical promotion: 0.
No claim that a native UD source already selects the additional axioms below.

Let the source subdivision map be S:C→C′, let R:C′→C be the affine barycentric
chain retraction, RS=I, and set Q=I−SR. Then Q²=Q, RQ=0, QS=0, and every fine
vector decomposes uniquely as x=S(Rx)+Qx. Here dim C=15, dim C′=149 and
dim ker R=134. Both S and R intertwine the respective boundaries.

## Complete metric family after fixing the retraction

First, the complete compatibility conditions themselves induce a retraction.
For any SPD H satisfying SᵀHS=G and A′_H S=S A_G, use B′S=SB to remove the
downward term. The remaining adjoint equation is
B′ᵀHS=HS G⁻¹BᵀG. Set R_H=G⁻¹SᵀH. Isometry gives R_H S=I; transposing the
adjoint equation and multiplying by G⁻¹ gives R_H B′=B R_H. Thus R_H is a
chain retraction. With Q_H=I−SR_H, the same orthogonal split proves
H=R_HᵀG R_H+Q_HᵀH Q_H. Conversely, any chain retraction R together with
a positive complement pairing gives all three compatibility identities through
the construction below. Hence the full compatible metric class is parameterized
by a chain retraction and a positive complement pairing, with graded choices
required if one also demands that chain degrees remain orthogonal. Fixed source
S and G alone do not select either item.

Let G be the coarse positive definite metric. Require that the already fixed
R is the metric adjoint of S, namely HS=RᵀG. This condition makes im S orthogonal
to ker R and entails SᵀHS=G. Every symmetric positive definite such H has the
form

H=RᵀGR+QᵀWQ,

where W is a symmetric pairing positive definite on ker R. Conversely every
such pairing gives a positive definite H with HS=RᵀG. Only W restricted to
ker R matters; extensions of W outside that subspace do not change H.

Proof: in x=S(Rx)+Qx, the cross term is
(Rx)ᵀSᵀHQx=(Rx)ᵀGRQx=0. The code term equals (Rx)ᵀG(Rx), so taking W=H
proves necessity. The same split formula proves sufficiency and positivity:
both terms vanish only when Rx=0 and Qx=0, hence x=0.

The boundary-adjoint intertwining follows without selecting W:
B′ᵀHS=B′ᵀRᵀG=RᵀBᵀG=HS(G⁻¹BᵀG).
Consequently A′_H S=S A_G for the boundary-minus-adjoint convention used
consistently on both spaces (or its simultaneous negative). Boundary chain
compatibility, isometry and generator compatibility all hold. A graded pairing
W preserves the original degree registers. The family is conditional on fixing
R; compatibility alone need not fix that retraction or its complement pairing.

For G=I, H_w=RᵀR+wQᵀQ with every w>0 supplies a one-parameter nonunique family.
H₁ and H₂ are invariant under all 24 source S4 relabelings. For the fine vertex
at barycenter {0,1}, x=e_{({0,1})}, Rx=(e₀+e₁)/2, and
Qx=x−(e_{({0})}+e_{({1})})/2. Thus ||Rx||²=1/2 and ||Qx||²=3/2, giving
xᵀH₁x=2 while xᵀH₂x=7/2. Symmetry and all three compatibility conditions
therefore do not select the metric.
Both examples induce exactly the same affine R_H=SᵀH_w=R; their difference
comes solely from the complement pairing, not a changed coarse retraction.

## Observable selection is a separate operational axiom

At the fixed metric H₁, define K_λ=RᵀR+λQᵀQ, 0≤λ≤1. These positive quadratic
observables obey K_λ≤H₁ and SᵀK_λS=I. They all give the calibrated coarse norm
on im S but assign the barycenter vector values 1/2, 5/4 and 2 at λ=0,1/2,1.
Consequently positivity, norm domination and code calibration do not select
the observable even after fixing H.

If the source additionally declares that a positive quadratic readout is
blind to ker R and calibrates it to the coarse positive semidefinite observable
D, its unique extension is K=RᵀDR. Precisely: K≥0, SᵀKS=D, and QᵀKQ=0.
Positivity implies KQ=0 (by the positive square root, or the Cauchy-Schwarz
inequality for the K pairing). The split decomposition then yields
xᵀKx=(Rx)ᵀD(Rx), proving uniqueness by polarization. This theorem derives the
observable from the added operational rule; it does not supply that rule's
native provenance. A calibrated linear readout with LQ=0 similarly has the
unique extension L=ℓR. None of these facts identifies quadratic chain norm
with local event stock, energy or a probability law.

## Positive diagonal metric locality no-go

For the ordinary oriented subdivision S, no strictly positive diagonal fine
metric can intertwine the weighted boundary adjoint with the old unit adjoint.
Take the old vertex 0. Its subdivision is exactly the fine singleton {0}.
Take the fine edge flag ({1},{0,1}). This flag does not contain singleton {0},
so (H⁻¹B′ᵀH S e₀) has zero coefficient there for every positive diagonal H.
But the coarse raising operator Bᵀe₀ contains −edge(0,1). The subdivision of
edge(0,1) is flag({0},{0,1})−flag({1},{0,1}); therefore S Bᵀe₀ has coefficient
+1 on the chosen flag. Hence the adjoint intertwining identity fails. Isometry
also forces h_{{i}}=1, but the locality contradiction does not depend on
the remaining diagonal values. Both downward terms agree by the chain-map
identity, so the generator intertwining fails as well.

This no-go concerns the full old unit generator and ordinary source S. A
different observable algebra, retraction, carrier or dynamics would be a new
source programme rather than an escape inside this fixed problem.

## Replay

selection-parallel-check.py imports only the freshly generated current
subdivision_metric.py and uses exact Fraction arithmetic. It checks both
metrics, complete-family identities, all 24 S4 actions, observable values and
the support-based diagonal contradiction. No archived program is executed.
