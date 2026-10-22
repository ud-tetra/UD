# THM-534 v2.4 — Unrestricted Cotangent No-Go and a Positive Complex-Carrier Alternative

**Date:** 2026-10-22 · **Lane:** development, no registry promotion · **Status:** EXACT/NO-GO under declared hypotheses; EXACT CONDITIONAL on a changed carrier; candidate physical interface only · **Physical promotion:** **0**.

## Versioned source and dependency

- Baseline: [THM-534 v2.3, bounded potential and isolated opening](https://github.com/ud-tetra/UD/pull/391), `captures/2026-10-22T143000Z-codex-thm534-finite-potential-f7a3c6d2/THM534_BOUNDED_POTENTIAL_DEPLETION_AND_OPENING_v2.3.md`.
- Parent: v2.2 Hamiltonian wake [PR #390](https://github.com/ud-tetra/UD/pull/390); v2.0 canonical-gate construction preserved as `SOURCE_CANONICAL_GATE_v2.0.md` in the v2.3 capture.
- Source strata: frozen `UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md` Q169–Q173, Q177–Q179 (real support/ownership); historical THM-534 six-edge stochastic micro-law **SOURCE-BLOCKED**.
- v2.4 is **target-exposed mathematical exploration**. Its complex-carrier construction is an explicit new branch, not a silent amendment to the real cotangent model.

## Fixed network data and typed carriers

The two-cell filled simplicial carrier `Kminus` has 7 unique oriented faces and 2 oriented cells, with signed face–cell incidence `D=B3 ∈ R^{7×2}`. There are 8 nonzero incidences. Let `x∈R^9` be the original real face/core support amplitude and `y∈R^9` its independent cotangent dual; `q,p∈R^8` are gate coordinates and conjugate momenta. Let `A_e∈so(9)` be the real unit signed generator supported on the two incident coordinates, `P_e` the diagonal orthogonal projector onto those two coordinates, and `A(q)=Σ_e χ_e(q_e) A_e`. The v2.3 gate profile `χ` is a supplied smooth 0–1 plateau profile and the potential `U_e(q)=2β_e/[1+(q+1)²]` has `β_e>0` supplied. Physical time, energy and original THM-534 probabilities are **not** declared by these coordinates.

## THM-534-P3 — Unrestricted cotangent positivity obstruction (EXACT / NO-GO)

**Hypotheses:** use the *standard constant canonical Poisson bracket* on `(x,y,q,p)`, insist that the **exact original support equation** `dot x=A(q)x` hold for every `y∈R^9`, and permit any smooth additional Hamiltonian terms depending on `x,q,p` but not on `y`.

**Conclusion:** on any state with `A(q)x≠0`, the Hamiltonian is unbounded below as `y` varies. In particular, no bounded `y`-independent potential or nonnegative `q`-only gate store repairs global positivity while retaining the stated equation on unrestricted `y`.

**Proof:** the canonical identity `dot x=∂H/∂y=A(q)x` forces by integration over connected `R^9`

`H=yᵀA(q)x+K(x,q,p)`.

For `y=−λA(q)x`, `λ>0`, one has `H=−λ||A(q)x||²+K→−∞`. QED.

**Sharp hypothesis:** restricting the allowed `y`, changing its Poisson bracket, or changing `dot x` creates a **new branch** and does not falsify this no-go. Adding a quadratic dual term `µ||y||²/2`, `µ>0`, instead gives `dot x=A(q)x+µy`, so it does not retain the frozen support equation.

**Exact counterexample:** take one on contact `χ=1`, support `x=e_f`, `β=1`, `q=1`, `p=0` and dual `y=−mA_ex`, giving `H=−m+1/5` for `m=1,10,100` (or any `m>0`). The added bounded positive v2.3 potential does not prevent divergence.

## New mathematical carrier (NOT a repair inside P3 hypotheses)

Take **instead** a complex nine-component support field `ψ∈C^9`, with canonical Hermitian amplitude symplectic structure `i dot ψ = ∂𝓗/∂bar ψ`, and real gate pairs `q,p∈R^8`. This has **18+16=34 real coordinates**, as did `(x,y,q,p)`, but its symplectic and readout types differ. Define

`S_e(ψ)=ψ†P_e ψ` and `N=ψ†ψ`,

`R(q,ψ)= Σ_e [U_e(q_e)/2] S_e(ψ)`,

`G(q)= 4 I_9 + i A(q) + 1/2 Σ_e U_e(q_e) P_e`,

`𝓗(ψ,q,p)= 1/2 Σ_e p_e² + ψ†G(q)ψ`.

The additive `4N` is the exact **maximum incidence-degree upper bound** (`max_i |{e:i is an endpoint of e}|=4`) for `Kminus`. It is a mathematical energy-origin shift, not a derived physical rest energy or action quantum. The real support variable `x` from v2.3 is not identified with `ψ`; where `ψ` is complex, its natural support stocks are `|ψ_i|²`.

## THM-534-P4 — Global nonnegative Hamiltonian and bound (EXACT CONDITIONAL)

**Conclusion:** for any `q∈R^8`, supplied `β_e>0`, any `ψ∈C^9`, and any real `p`,

`𝓗 ≥ 1/2||p||² + R(q,ψ) ≥ 0`.

**Proof:** each `iA_e` is Hermitian, `||iA_e||_op=1`, and `|ψ†iA_eψ|≤ψ†P_eψ`. Thus

`|ψ†iA(q)ψ| ≤ Σ_e χ_e ψ†P_eψ ≤ 4||ψ||²`.

The last inequality counts contact incidence: an interior cell contacts four faces, and a shared face contacts two cells. Therefore `ψ†(4I+iA)ψ≥0`, and `R≥0` follows from the supplied positive U. QED. In particular, at fixed initial `𝓗` the complete gate-momentum norm obeys `||p(s)||²≤2𝓗(0)`.

## THM-534-P5 — Conservative complex-chain dynamics and source distinction (EXACT CONDITIONAL)

Hamilton's equations are

`i dot ψ=G(q)ψ`, `dot q_e=p_e`,

`dot p_e=−χ'_e(q_e) ψ†iA_eψ −[U'_e(q_e)/2] S_e(ψ)`.

They conserve `𝓗` and `N=||ψ||²`. For face f and cell τ the support receipt from contact e=(f,τ) is

`J_e=2 d_e χ_e(q_e) Re(conj(ψ_f) ψ_τ)`;

`d|ψ_f|²/ds=−Σ_{e∋f} J_e`, `d|ψ_τ|²/ds=Σ_{e∋τ} J_e`.

The diagonal potential and `4I` contribute only local phases to `dot ψ` and cancel from squared-stock derivatives. Summing the contacts gives exact global support conservation; the existing Q177–Q179 equal-share **ownership bookkeeping** extends algebraically with `|ψ|²`. **This is a complex-valued extension:** the frozen real Q171 bilinear `2d z_f t_τ` is recovered only when the relative phases are zero. A complex extension is **not** source-derived UD particle dynamics, and this model does not assert conservation of the earlier real `||x||²` as the same typed object.

**Proof:** `G†=G`; the Schrödinger equation yields `dN/ds=0`. Canonical Hamilton's equations conserve `𝓗`. For each amplitude, `2Re(conjψ_i dotψ_i)` eliminates diagonal Hermitian terms and leaves only the real-part antisymmetric signed contact products. This gives the exact local receipt and ownership balance. QED.

The full vector field is smooth/Lipschitz on bounded sets, `N` and `𝓗` are conserved, `p` is bounded by P4, and `q` can grow at most linearly on any finite interval. Therefore finite initial data admit a global-in-model-parameter solution (although the gate can coast indefinitely and no reset is implied).

## THM-534-P6 — Recovery of isolated zero-dual funding under an explicit preparation (EXACT CONDITIONAL)

Restrict to one isolated face–cell contact with initial `ψ` real up to one global phase, `q=p=0` and total pair norm `S>0`; require all other contacts absent or structurally inactive without overlapping potential. The scalar potential `U/2` acts as identity on the pair, so the internal ψ evolution differs from the original real rotation only by a common phase. Consequently `ψ†iA_eψ=0` throughout, and

`K+R=βS/2`, with `K=p²/2`, `R=U(q)S/2`.

The gate accelerates from rest with `ddot q(0)=βS/2`; v2.3's isolated opening argument applies exactly. At `q=1`, `(K,R)=(3βS/10,βS/5)`, i.e. 3/5 of the initial potential in gate kinetic stock and 2/5 remains. **This is a conditional isolated comparison**, not a uniquely selected source profile or physical funding law.

## THM-534-P7 — No exclusive shared-contact selection from symmetric rest (EXACT / NO-GO)

Take only the shared face `f=012` nonzero with `ψ_f=1` real and both incident cell amplitudes zero. Set the two adjacent contact gate states to `q=p=0`, `β_0=β_1=β>0`, with symmetric gate profile and all other support components zero. Because χ(0)=χ'(0)=0, the initial backreaction term vanishes on both contacts; since `U'_e(0)=−β`, their canonical accelerations are both

`ddot q_(f,τ0)(0)=ddot q_(f,τ1)(0)=β/2>0`.

The full equations are equivariant under the carrier automorphism exchanging the two apices, provided signed orientations are transported. Uniqueness of the ODE preserves the symmetry: this preparation cannot select *exactly one* of the two shared-face contacts. It opens both equivalently if the common trajectory reaches the on plateau, or neither; the result is not a single-contact selection law. QED. An asymmetric preparation, independently chosen contact, or extra symmetry-breaking register is outside this no-go.

## THM-534-P8 — Positive-resource audit is not a native packet action (OPEN_GATED)

The complex-carrier construction **solves one mathematical resource-boundedness problem by changing the symplectic carrier**. It does **not** recover the real 9-vector model as a type-identical action; identify a unique gate-opening source, assign physical action units, solve exclusive contact selection, produce a reset and memory ledger, prove original THM-534 `(1/2,1/6,1/12)` transition probabilities, or give any empirical field/particle recovery. The additive `4N` is an algebraic bound convention, not an observable cosmological or physical energy. The original v2.3 cotangent NO-GO P3 remains valid.

## Exact and numerical reproduction

- [`verify_v24.py`](verify_v24.py): standard Python/SymPy exact checks of the Kminus 8 contact operators, 56=6,561 mixed profile words χ∈{0,1/2,1}^8 for nonnegative diagonal-dominance bound, explicit unbounded cotangent controls, symmetric double waking and exact isolated `3/5`–`2/5` funding.
- [`verify_v24_numeric.py`](verify_v24_numeric.py): 256 binary network Hermitian eigenchecks (smallest numerical eigenvalue 1.7639320225), and 250 separate complex preparations checking canonical energy-rate, norm-rate and all nine local squared-stock rates (maximum discrepancy 7.11×10^-15).
- Both run by the same constructor; no non-constructor proof review or physical experiment. Historical target exposed; no CRL or physical promotion.

**Recommended next test:** Require the actual frozen UD source to choose between real cotangent and complex symplectic carriers, and derive an admission/reset/record law with unique contact selection. Do not infer that a positive shifted mathematical Hamiltonian already supplies a positive physical reservoir or global UD completion.