# Path α — Expanded Partial Manuscript Section: The Cosmological Constant Candidate

**Status:** PARTIAL_MANUSCRIPT_DRAFT / CONDITIONAL_CONSERVATIVE_LANGUAGE
**Crown:** OFF
**Integrates:** RC1 Λ chain consolidation, V5 DEC formalization, RG_DEPTH_OBSERVABLE_CATALOG_v0.4, Lumi Section 4.4 Structural-Choice framing
**Scope:** External-reviewer-survivable draft of the Λ section, using only what has been earned through the session's discipline.

---

## 4. The Cosmological Constant Candidate

### 4.1 Overview

Unified Dynamics admits a candidate expression for the cosmological constant in dimensionless Planck units:

$$
\Lambda_{\mathrm{UD}} \,\ell_{\mathrm{Pl}}^2 \;=\; \frac{1}{S^2} \left( \frac{\nu_0 \, F_{\mathrm{IFS}}^{\Delta}}{M_{\mathrm{Pl}}} \right)^{\!4}
$$

with constituents:

- `ν_0 = 83.19 keV`, fixed by the Koide neutrino-mass condition;
- `Δ = 7`, the K_4 distinction-seat count, multiply over-determined from K_4 substrate structure (Section 3.x);
- `F_IFS = 1/(3π)`, derived as the spectral–curvature quotient `d_s / (2π χ(∂K_4))` with `d_s = 4/3` (Section 3.y);
- `M_Pl`, the Planck mass in standard units;
- `S`, the support-functional value, with two cases described below.

This expression involves no fitted continuous parameters. The discrete structural choices that remain — the exponent of `F_IFS`, the power of `S`, and the selection of the support sector — are each motivated by structural arguments documented in Sections 3.z and 4.4.

### 4.2 The Support Functional

We define the **support functional**

$$
S(X) \;=\; E \;+\; \frac{\chi(X)}{\Delta}
$$

on the lattice of finite simplicial complexes, where `E = 6` is the K_4 edge count, `Δ = E + 1 = 7` is the distinction-seat count, and `χ(X)` is the Euler characteristic of the support space `X`.

Algebraically, the functional admits the closed form

$$
S(X) \;=\; \frac{E^2 + E + \chi(X)}{\Delta},
$$

which displays the **R29 decomposition**: an `E²` pairwise component (edge-edge tensor product), an `E` diagonal component (single-edge identity), a topologically-indexed component `χ(X)`, and the coherence-capacity normalization `Δ = E + 1`.

In discrete-exterior-calculus terms (Section 4.3), the `E²` term is `dim(C^1 ⊗ C^1)`, the `E` term is `dim(C^1)`, and the `χ(X)` term is the alternating-sign Betti sum `Σ_p (-1)^p β_p(X)`. The decomposition admits the Euler-Poincaré identity `χ(X) = Σ_p (-1)^p dim H^p(X; ℝ)`.

### 4.3 Discrete-Exterior-Calculus Formulation

For a finite abstract simplicial complex `X` with simplex counts `n_p(X)`, the support functional can be expressed as

$$
S(X) \;=\; n_1(K_4) \;+\; \frac{1}{n_1(K_4) + 1} \sum_p (-1)^p \dim H^p(X; \mathbb{R}),
$$

where `K_4` is the substrate complete graph (`n_0(K_4) = 4`, `n_1(K_4) = 6`). The functional is well-defined on any simplicial complex but is parameterized by the K_4-substrate constants `E = 6` and `Δ = 7`.

The **R29 evaluation** (Theorem R29, Evaluation Saturation; Lumi archive) computes `S(pt) = 43/7` as the support capacity of the bare K_4 cell, evaluated on the pointlike neutral seed (`χ(pt) = 1`). This derivation uses K_4 tensor-algebra dimension counts and does not assume the form of `S(X)` as input; it computes `(E² + E + 1)/(E + 1) = 43/7` from independent combinatorial structure.

### 4.4 Sector Cases and the Structural-Choice Status of S_Λ

The Λ candidate evaluates `S` in one of two cases:

**Conservative case (RC1):** `S = S_0 = S(\mathrm{pt}) = 43/7`. This is the value derived by Theorem R29 from K_4 structure. With this assignment,

$$
\Lambda_{\mathrm{UD}}^{\mathrm{(RC1)}} \,\ell_{\mathrm{Pl}}^2 \;\approx\; 3.001 \times 10^{-122},
$$

a `+3.9%` residual against the observed `Λ_{\mathrm{obs}} \,\ell_{\mathrm{Pl}}^2 \approx 2.888 \times 10^{-122}`. RC1 is the conservative published candidate: the support sector is derived independently via R29, and the residual is reported honestly.

**Candidate case (RC2):** `S = S_Λ = S(∂K_4) = 44/7`, obtained from the support functional at `χ(∂K_4) = 2`. With this assignment,

$$
\Lambda_{\mathrm{UD}}^{\mathrm{(RC2)}} \,\ell_{\mathrm{Pl}}^2 \;\approx\; 2.866 \times 10^{-122},
$$

a `−0.77%` residual. RC2 is presented as a **structural-choice candidate**, not as an independent derivation.

**Epistemic declaration.** The value `S_Λ = 44/7` arises by evaluating the support functional `S(X) = E + χ(X)/Δ` at `X = ∂K_4` (the boundary 2-sphere of the K_4 simplex). The arithmetic is correct: `χ(∂K_4) = 4 - 6 + 4 = 2`, and the functional yields `44/7`. However, the replacement of the connected-component invariant `β_0(K_4) = 1` (which the R29 decomposition's unit slot most naturally encodes) by the full Euler characteristic `χ(X)` for higher-dimensional support spaces is a structural choice that has not been independently derived from the framework's first principles. The choice is motivated by the Euler-characteristic differential `χ(∂K_4) - χ(\mathrm{pt}) = 2 - 1 = 1` and by the `+1/Δ` residue rule. An independent tensor-algebraic derivation of the boundary support capacity from 2-complex tensor-algebra logic (held item M3-α, Section 6) is future work. Consequently, RC1 (with `S_0 = 43/7`) is the present published candidate; RC2 (with `S_Λ = 44/7`) is presented as the most natural candidate upgrade conditional on closure of the M3-α derivation and the associated sector-identification arguments.

### 4.5 Sector Selection Rule (Provisional)

A provisional rule for sector selection is articulated as follows:

> **Provisional RG-depth rule.** Observables that evaluate within a single K_4 cell (UV / local / depth-0) couple to the pointlike support `S_0`. Observables that require at least one IFS coarse-graining step (IR / global / depth ≥ 1) couple to the boundary-exposed support `S_Λ`.

Under this rule, the cosmological constant — as the deep-IR macroscopic vacuum-energy observable — is classified as depth ≥ 1 and assigned `S_Λ`. The classification is structurally motivated by the fact that the Λ candidate evaluation requires boundary data through `F_IFS = d_s/(2π χ(∂K_4))`, which itself depends on the IR-asymptotic spectral dimension `d_s = 4/3` and the boundary Euler characteristic.

The rule has been tested as follows (RG_DEPTH_OBSERVABLE_CATALOG_v0.4):

- **Direct UV verification (1):** Theorem R29 produces `S_0 = 43/7` from K_4 tensor-algebra logic independently of the support functional formula. This is a non-tautological derivation.
- **Direct IR verification (0):** No independent derivation of `S_Λ = 44/7` from 2-complex tensor-algebra logic currently exists. The Λ candidate use of `S_Λ` is the only direct IR application, and it is conditional on the rule.
- **Negative non-falsifiers (1):** Gravitational-wave echo delays and phase drifts (IR phenomena) were audited; their derivations use `1/(9π²)`, `1/18`, and `3/2`, not `44/7`. The rule was not falsified — GW delays do not violate the rule by using `S_0` in an IR role — but the catalog does not gain a new direct pass.
- **Supporting IR evidence (1):** The spectral dimension `d_s = 4/3` is established as an IR-asymptotic property of the K_4 IFS attractor, supporting the IR classification of `F_IFS` and therefore of Λ-evaluation.
- **Falsifiers found (0):** No observable currently violates the provisional rule.

The rule is therefore classified as `VERIFIED_WITHIN_NARROW_SCOPE / NOT_FALSIFIED`. Its scope is observables that explicitly use the support functional `S(X)` as a denominator; outside that scope (e.g., observables using Banach screening `(7/192)^n`, lattice dispersion `1/18`, or integer-arithmetic identities), the rule does not apply and is not tested.

### 4.6 Numerical Summary

| Quantity | RC1 | RC2 |
|----------|-----|-----|
| `S` | `43/7` | `44/7` |
| `S²` | `1849/49 ≈ 37.735` | `1936/49 ≈ 39.510` |
| `Λ_UD · ℓ_Pl²` | `3.001 × 10⁻¹²²` | `2.866 × 10⁻¹²²` |
| Residual vs `Λ_obs` | `+3.9%` | `−0.77%` |
| Support sector status | DERIVED via R29 | STRUCTURAL CHOICE pending M3-α |

### 4.7 Held Items Affecting RC2 Closure

The following held items must be addressed for RC2 to be promoted from structural-choice candidate to independently-derived prediction:

- **HELD-M3-α:** Independent (non-formula-evaluation) derivation of the support capacity for a 2-complex. The DEC formalization (Section 4.3) sharpens this question: whether the R29 "unit slot" generalizes to `+β_0(X)` (connected-component count) or to `+χ(X) = Σ_p (-1)^p β_p(X)` (alternating-sign Betti sum) for higher-dimensional support spaces. The framework's K_4 case is degenerate between these readings since `β_0(K_4) = 1 = χ(K_4 \text{ as filled 3-simplex})`. The boundary case `∂K_4` distinguishes them: `β_0(∂K_4) = 1` vs `χ(∂K_4) = 2`.
- **HELD-M3-β:** Topological equivalence between the physical "boundary-exposed K_4 complex" — variously characterized as the 18-channel S_3 macroscopic shell or the first IFS contraction layer per AX3 — and `∂K_4` as a simplicial 2-sphere.
- **HELD-M3-γ:** Sector-identification argument that the macroscopic Λ observable couples to the boundary-exposed complex rather than to the bare K_4 seed. The current motivation through `F_IFS`'s χ-dependence is suggestive but not definitive.

Additional held items affecting the broader Λ chain:

- **HELD-ρ2:** Resistance scaling `ρ = 2` proof for `d_s = 4/3` on the K_4 IFS (currently invoked from standard Sierpinski-tetrahedron decimation).
- **HELD-VF-EE:** Vertex–face / edge–edge channel uniformity beyond the minimal screen algebra. The `D = (w - w*)²` split-sensitive invariant distinguishes V–F channels (`D = 4/25`) from E–E channels (`D = 0`), constituting a known asymmetry.
- **HELD-AX2:** Clarification of the axiomatic-vs-derived status of `S_0 = 43/7` in axiom AX2 (Threshold), given that R29 derives the same value from independent combinatorial structure.

### 4.8 Honest Position Statement

The Λ candidate chain admits a parameter-free expression whose components are derived from K_4 substrate structure with named conditionals at each step. The conservative case (RC1, `S = S_0 = 43/7`) yields a `+3.9%` residual against the observed cosmological constant, with the support sector derived independently via Theorem R29. The candidate upgrade (RC2, `S = S_Λ = 44/7`) yields a `−0.77%` residual but currently depends on the structural-choice interpretation of `S_Λ`, pending the M3-α derivation. We present RC1 as the conservative published candidate and report RC2 as the most natural upgrade direction conditional on the closure of three named held items. No claim of cosmological-constant closure is made.

---

## Compilation Notes (For Internal Use Only — Not Manuscript Text)

```text
SECTION SOURCES:
  - RC1 numerics: LAMBDA_CHAIN_CONSOLIDATION_RC1 (hash aaf2af13...)
  - RC2 numerics: this session, in-session computation
  - V5 DEC formalization: SX_DEC_FORMALIZATION_v0.1 (hash 564df833...)
  - Catalog: RG_DEPTH_OBSERVABLE_CATALOG_v0.4
  - Sector rule status: VERIFIED_WITHIN_NARROW_SCOPE / NOT_FALSIFIED
  - GW negative result: Lumi archive sweep this session
  - Held items: per LARM RC1 and subsequent in-session work

LANGUAGE DISCIPLINE APPLIED:
  - "candidate" not "derived" for RC1/RC2 outputs
  - "structural choice" not "derivation" for S_Lambda
  - "provisional rule" not "law" for RG-depth selection
  - "verified within narrow scope" not "verified"
  - "not falsified" not "validated"
  - "support functional" not "support theorem"
  - All held items explicitly enumerated
  - No closure claims anywhere

SECTION DEPENDENCIES (for cross-referencing):
  - 3.x: Delta = 7 derivation (multi-route)
  - 3.y: F_IFS derivation from d_s/(2*pi*chi)
  - 3.z: Discrete structural choices motivation
  - 6: Held items registry (full)

REVIEWER-DEFENSIBILITY CHECK:
  - RC1: Fully defensible. R29 is independent derivation, residual 
    is reported honestly, no overclaim.
  - RC2: Defensible as structural-choice candidate. Held items 
    explicitly named. External reviewer cannot accuse retrofit 
    because the choice is labeled as a choice.
  - Sector rule: Defensible. Catalog presents 1 direct UV pass + 
    0 direct IR + 1 negative non-falsifier. Honest scope.
  - DEC formalization (Section 4.3): Defensible. Standard math, 
    clean notation, R29 interpretation is precise (beta_0 reading).
```
