# J1 metric-sensitive scalar-wave benchmark v0.1

**DERIVED / EXACT CONDITIONAL. Development — no registry entry.** Constructor verification, no independent review, physical promotion0. Refs #218 and #136. This selects an explicit benchmark functional; it does not claim that UD primitives select it. Source geometry and incidence investigation: PR219, capture2026-10-19T160000Z-codex-j1-geometry-6f18a924. That pending capture remains immutable.

## 1. The declared comparison contract

Set a=1 for calculation. Label apex0 and square vertices1,2,3,4 cyclically as in the user coordinates. Use four models: J1 triangulated along13; J1 along24; J1 with square center5 and four tetrahedra; and two regular edge-a tetrahedra sharing face(0,1,3), with opposite vertices2,4. The regular comparison is a triangular bipyramid, not the same outer physical boundary as J1. Common labels define the same port prescription across geometries, not a geometric isometry or equal aperture shape. All four models have the same total volume2Vref, Vref=sqrt2 a³/12.

Let u be a real scalar field continuous and affine on each tetrahedron, with nodal coordinates q. Declare a homogeneous lossless scalar-wave action

    L = (1/2) integral_V [u_t² - c² |grad u|²] dV + external port work,

and natural homogeneous Neumann conditions on the exterior except for the explicitly applied nodal loads. This is a conditional field theory/P1 discretization benchmark. It is not automatically a model of acoustic pressure, Maxwell fields, UD support, or actuator energy. c is a declared wave speed, not a derived UD constant. Use tau=ct/a. Divide all integrals by Vref; all reported K,M are dimensionless.

For a tetrahedron with barycentric basis phi_i, volume ratio v=Vtet/Vref, and dimensionless coordinates:

    K_ij += v (grad phi_i) dot (grad phi_j),
    M_ij += v(1+delta_ij)/20.

The mass identity is the exact barycentric simplex integral. Compute each gradient Gram by inverting the3x3 edge Gram; all entries are rational because all squared lengths are rational. Each J1 diagonal cell and each regular cell has v=1; each center cell has v=1/2. No mass lumping, fitted stiffness or frequency tuning is used.

Dynamics: M q'' + K q = p f. Energy E=(q'^T M q'+q^T K q)/2 satisfies E'=f p^T q'. The force/output pair is f and y=p^T q, so supplied work is explicit. M is positive definite; K is positive semidefinite with only the constant null mode. The constant drift is a Neumann gauge mode, not a resonance gain. Positive-frequency unforced modes are conservative, not decaying attractors.

## 2. Fixed boundary port and exact result

Use p=(0,1,0,-1,0)^T (append0 for center), a balanced nodal force at vertices1 and3 and readout y=q1-q3. Center refinement transfer copies the five boundary values and sets q5=0 for this odd mode. This transfer is exact on the investigated port subspace; it is not asserted to intertwine full dynamics.

Direct rational matrix identities give:

| Model | M p | K p | Exact H(s)=y(s)/f(s), zero initial state | H(0) |
|---|---|---|---|---|
| Either J1 diagonal | p/10 | 2p | 20/(s²+20) | 1 |
| J1 center refinement | p/10 | 2p | 20/(s²+20) | 1 |
| Regular Kminus | p/10 | 4p | 20/(s²+40) | 1/2 |

Proof: multiply the displayed eigenvector identities into (s² M+K)q=p f. The exact driven subspace is span(p), giving q=10p f/(s²+omega²); p^T p=2. The readout is consequently20f/(s²+omega²). This is a rational identity, not a finite frequency sweep. Isolated singularities elsewhere in the full resolvent do not create poles in this port transfer when the uncoupled mode is unforced/unobserved. Interpret imaginary-axis poles as ideal lossless resonances; no finite resonant gain or dissipation is certified.

For initial q=p and q'=0, y(tau)=2 cos(sqrt20 tau) for J1 and2 cos(sqrt40 tau) for regular Kminus. Dimensional omega=(c/a)sqrt20 or(c/a)sqrt40. Their ratio sqrt2 is derived within this chosen gradient-energy and consistent-mass model; it is not a newly identified universal UD coupling, clock or selection constant. The geometry test distinguishes models that the prior unit-chain incidence spectrum did not distinguish.

The other J1 square port r=(0,0,1,0,-1) also satisfies Mr=r/10 and Kr=2r. Cross transfer r^T(s²M+K)^(-1)p is identically zero: the two-dimensional span(p,r) is invariant and M/K are scalar on it. This is exact two-channel degeneracy/decoupling for the three declared J1 refinements, not a claim about arbitrary meshes, loss, heterogeneous materials or full three-dimensional continuum solutions.

## 3. Refinement and symmetry controls

Quarter-turn rotation exchanges the two J1 diagonal models and conjugates their full K,M exactly. Neither single-diagonal mesh individually retains the full square action, but their spectra agree. The center mesh is D4 invariant. The selected port transfer agrees across all three despite full spectra changing:

| Model | Squared frequencies in normalized tau |
|---|---|
| Either diagonal J1 | 0,20,20,40,80 |
| Regular Kminus | 0,15,40,40,40 |
| Center J1 | 0,20,20,40,40,160 |

Thus full-spectrum equality is false under refinement; the scoped port result survives. Every J1 mesh exactly integrates the affine x,y fields, giving normalized gradient energy2 and consistent mass1/10 for each. This checks metric and quadrature normalization independently of the chosen port.

Static elimination of center gives K_eff=K_bb-K_bc K_cc^(-1)K_cb and the same selected static compliance1. This is not a general dynamic elimination: exact frequency elimination requires the Schur complement of K+s²M, including the frequency-dependent interior response. No quasistatic center transfer is claimed for arbitrary states. The exact odd port has zero center coordinate by the matrix identities above.

## 4. What this closes and what remains

Closed within this declared model: a metric-sensitive operator, common energy-conjugate force/readout, equal total volume, exact normalized mass/stiffness matrices, two diagonal symmetry controls, a center refinement control, a robust two-channel J1 subspace, and an exact contrasting regular-Kminus port law.118 constructor assertions pass, including positive pivots, zero modes, exact characteristic polynomials, factorizations, port identities and resolvent checks at five rational parameters.

Open: derivation of this action from native UD source variables; a mapping between this scalar field and UD chain-register state; convergence/error bounds to a continuum boundary-value problem; finite aperture/distributed-source implementation; loss and calibration; arbitrary-refinement robustness; finite-throat horn transmission; physical correspondence. No claim of preferred clustering, persistence against noise or natural shape selection is made. A conservative normal mode is not a growth or attraction theorem.

Next decisive return: bound the response under passive damping/port perturbations and additional conforming refinements, while deriving or rejecting a source-bound connection to the UD operator. Keep source selection distinct from the successful conditional discrimination result. The governance attachment remains labeled a proposal; this work creates no registry entry.

## Replay and provenance

Run `python3 verify_metric.py` and compare parsed JSON to RESULTS.json. Standard-library Fraction arithmetic constructs all matrices and characteristic polynomials exactly. Fresh code only; no archived program executed. Prior ledger F03/Q169-Q179 and geometry capture are comparisons/premises, not evidence that UD has selected this field action. The current attachments are unchanged from the prior turn; no new content or missing image is assumed.
