# THM-534 forward finite-incidence event programme — exact theorem addendum
**Version:** v0.3 | **Date:** 2026-10-21 | **Status:** exact internal derivation + scoped NO-GO | **Lane:** development, no registry promotion | **Physical promotion:** 0

**Relations:** [THM-534 historical source-law gate v0.2](THM534_MICRO_SOURCE_RECOVERY_AND_NO_GO_v0.2.md) · [Parent theorem suite v0.1](UD_THM534_SESSION_DISCOVERIES_THEOREM_PACKET_v0.1.md) · [PR #346](https://github.com/ud-tetra/UD/pull/346) · [Issue #347](https://github.com/ud-tetra/UD/issues/347)

## Exposure / source governance
The historical THM-534 transition weights and spectrum **were known before this programme**. Consequently this is *not* a confirmatory target-blind preregistration. It is an explicitly **target-exposed, source-first mathematical exploration**: its chosen generators come from unweighted tetrahedral incidence, not from tuning the transport probabilities to the historical target. Source results and negative controls are preserved regardless of match. Independent non-constructor review is pending.

Carrier: the complete filled oriented tetrahedron `K=Δ³` on `{0,1,2,3}`, with unoriented edge readout `E=\{01,02,03,12,13,23\}`. Its chain spaces are `C₀≅R⁴`, `C₁≅R⁶`, `C₂≅R⁴`, `C₃≅R`, equipped with unit-weight orthonormal oriented simplex bases. `B₁:C₁→C₀`, `B₂:C₂→C₁`, `B₃:C₃→C₂` are standard alternating simplicial boundary maps. All stochastic matrices below act on the **edge readout** `R^E`, not on the full signed chain state or on a quantum Hilbert-space density operator. The update index counts finite incidence events; it is not calibrated physical time.

## Primitive event rules (source-first)
**Event A — lower incidence (vertex-mediated).** Starting at edge e, choose one of its two endpoints uniformly; choose one of the three edges incident to that vertex uniformly, with replacement. Read out resulting edge f. The intermediate endpoint is logged, and independent uniform sampling is an explicit **assumption**.

**Event B — upper incidence (face-mediated).** Starting at edge e, choose one of its two triangular cofaces uniformly; choose one of the three edges in that face uniformly, with replacement. Read out resulting edge f. The intermediate face is logged. This is a second *mathematically defined* rule, not independent experimental evidence.

Both events use only multiplicities from the incidence matrices. No phase, burden, apparatus, local relaxation, closure receipt or physical constants enter. The rules are *candidate control models*, not recovered historical THM-534 primitives.

Let `A=|B₁|∈\{0,1\}^{4×6}` and `F=|B₂|∈\{0,1\}^{6×4}` be absolute-value (unsigned) incidence matrices. Their induced Markov kernels are `P_down=AᵀA/6` and `P_up=FFᵀ/6`.

## THM-534-N5 — Lower/upper incidence mobility equivalence (EXACT)
**Claim.**
```text
P_down = P_up = P = (1/3) I₆ + (1/6)(J₆−I₆−S),
spec(P) = {1 (×1), 0 (×2), 1/3 (×3)},
```
where S exchanges the three pairs of disjoint edges, J is the all-ones 6×6 matrix, and the three eigenspaces are the constant edge vector `V₀`, the symmetric-pair zero-sum `V₊`, and the antisymmetric-pair `V₋`.

**Proof.** Each edge has two incident vertices and two triangular cofaces; each vertex has three edges and each triangle three edges. Both two-stage rules assign probability `2/(2·3)=1/3` to the original edge; each adjacent edge shares exactly one vertex and exactly one triangle with it and therefore has probability `1/(2·3)=1/6`; a disjoint opposite edge shares neither and has probability zero. This establishes both equality and the explicit formula. The orbit-spectrum formula of THM-534-N1 with `(a,b,c)=(1/3,0,1/6)` gives `(1,0,1/3)` with multiplicities `1,2,3`. QED.

**Independence caveat.** The mechanisms have different intermediate carriers (vertices versus triangular faces) but the **same marginalized one-step edge channel**. Their hidden intermediate records are not identified. The resulting equality is a combinatorial incidence duality on `Δ³`, not a physical equivalence of event processes.

## THM-534-N6 — No-go for arbitrary independent incidence step-count mixtures (EXACT / NO-GO)
**Hypotheses.** Fix P from N5. At each macrostep, independently choose an integer `k≥0` with a nonnegative edge-independent probability mass `p_k`, `Σ_{k≥0}p_k=1`. Execute exactly k iid elementary P steps (k=0 is a hold). Marginalize the length. Then the macrostep Markov operator is `Q=Σ_{k≥0}p_kP^k`, convergent entrywise.

**Conclusion.** Its eigenvalues on `V₊` and `V₋` satisfy
```text
λ₊(Q)=p₀;
λ₋(Q)=p₀+Σ_{k≥1}p_k·3^(−k) ≥ λ₊(Q).
```
Consequently no such independent random-length incidence walk equals the historically declared THM-534 T, which has `λ₊(T)=1/2 > 1/3=λ₋(T)`.

**Proof.** P annihilates V₊ and acts by 1/3 on V₋. On V₊, `P^0=I` contributes only `p₀` and every positive power acts as zero. On V₋, `P^k` acts by `3^(−k)` including k=0. Nonnegative weights imply the inequality. Since the historical ordering is reversed, equality is impossible. QED.

**Scope.** The obstruction applies only to independent, nonnegative *length mixtures of this particular P* on the unoriented edge readout. It does not exclude orientation-sensitive events, phase-bearing amplitudes, state-dependent routing, event memory, additional carrier sectors, distinct generators or signed/non-stochastic evolution. Changing any such assumption creates a new branch and must not erase this no-go.

**Control receipts:** `P` has (self, opposite, adjacent) probabilities `(1/3,0,1/6)`; `P²` has `(2/9,1/9,1/6)`; `P³` has `(5/27,4/27,1/6)`. No length of this walk introduces a positive `V₊` eigenvalue.

## THM-534-N7 — Signed unit-Hodge edge Laplacian cancellation (EXACT / SCOPED NO-GO)
**Hypotheses.** Work on the *complete filled simplex* `Δ³`, with the declared signed alternating boundary matrices and unit chain inner products. Set
```text
L₁ = B₁ᵀ B₁ + B₂ B₂ᵀ : C₁→C₁.
```
**Conclusion.** `L₁=4I₆`. Hence the edge-only Hodge heat flow `d x/ds = −L₁ x` acts as `x(s)=e^(−4s)x(0)`, with no mixing between distinct edge coordinates.

**Proof.** Each edge has two endpoint incidences and two face incidences, so both diagonal contributions equal 2. Distinct opposite edges share neither a vertex nor a face, giving zero off-diagonal contributions. Adjacent edges share one vertex and one triangle. By the boundary orientation convention, their vertex-incidence inner product and face-incidence inner product have opposite signs (equivalently the simplex identity `L₁(Δ³)=4I₆`), so they cancel exactly. QED.

**Scope firewall.** This does not block Hodge–Dirac transport **between chain degrees**, nonunit inner products, incomplete complexes, open-system operators, phase/seam interactions or nonlinear dynamics. It only rules out interpreting this *specific full unit-Hodge edge Laplacian* as a nontrivial edge-to-edge hop generator.

## Decision and next admissible branch
The native unweighted incidence programme yields a fully source-specified elementary event but **fails** to derive the historical THM-534 matrix. More strongly, all nonnegative independent event-length mixtures of that walk are excluded. The signed unit-Hodge edge Laplacian supplies no edge mixing on the fully filled `Δ³`.

The strongest open bifurcation is to find an **independently sourced additional microscopic operation** (e.g. oriented seam transport or a source-derived inter-sector readout) that is not representable as `f(P)` with nonnegative step-count coefficients, and prove its probability/metric/rate normalization without reverse-engineering the target. Before evaluating its historical weights, freeze state space, event alphabet, update scheduling, source/boundary receipts, memory model, control operators, and interpretation rules. A new target-blind *confirmatory* test requires a held-out source family or independently frozen future observable because the historical matrix is already exposed.

## Reproduction
`thm534_forward_incidence_verify_v0_3.py` performs the exact `B₁B₂=0`, `B₂B₃=0`, `L₁=4I`, lower/upper unsigned mobility equality, target/control spectrum checks, finite path-length receipts and 24 `S₄` relabelings. Local execution: PASS, 2026-10-21. Standard Python plus SymPy. No external physical validation; no independent reviewer; no registry/physical promotion.
