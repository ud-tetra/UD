# V5 — Discrete Exterior Calculus Formalization of the Support Functional

**Artifact:** `SX_DEC_FORMALIZATION_v0.1`
**Status:** MANUSCRIPT-GRADE FORMALIZATION / NO CLOSURE CLAIMS
**Crown:** OFF
**Scope:** Express the support functional `S(X) = E + χ(X)/Δ` in discrete-exterior-calculus language; identify what is derived from K_4 structure versus what is a structural choice. This document makes no claim about sector-selection verification beyond the existing in-session status.

---

## 1. Setup and Notation

Let `X` be a finite abstract simplicial complex with simplex set `Σ(X) = Σ_0 ∪ Σ_1 ∪ Σ_2 ∪ ...`, where `Σ_p` is the set of `p`-simplices. Define:

- `n_p(X) = |Σ_p(X)|` = number of `p`-simplices in `X`
- `C^p(X)` = the vector space of real-valued `p`-cochains on `X`, with `dim C^p(X) = n_p(X)`
- `d^p : C^p(X) → C^{p+1}(X)` = coboundary operator, satisfying `d^{p+1} ∘ d^p = 0`
- `χ(X) = Σ_p (-1)^p n_p(X)` = Euler characteristic
- By the Euler-Poincaré identity, `χ(X) = Σ_p (-1)^p dim H^p(X; ℝ) = Σ_p (-1)^p β_p(X)`, where `β_p` are the Betti numbers.

The K_4 substrate is the complete graph on 4 vertices. As a 1-skeleton it has `n_0 = 4` vertices and `n_1 = 6` edges. We will distinguish notationally between:

- **K_4 as 1-skeleton (graph):** simplex counts `(4, 6, 0, 0, ...)`, Euler characteristic `χ = -2`
- **K_4 as 2-skeleton with triangular faces:** simplex counts `(4, 6, 4, 0, ...)`, Euler characteristic `χ = 2`
- **K_4 as filled 3-simplex (tetrahedron):** simplex counts `(4, 6, 4, 1, ...)`, Euler characteristic `χ = 1`
- **∂K_4 (boundary of filled 3-simplex):** simplex counts `(4, 6, 4, 0, ...)`, topologically `S²`, Euler characteristic `χ = 2`

Throughout, we set `E = n_1(K_4) = 6` and `Δ = E + 1 = 7`.

---

## 2. The Support Functional

The support functional under analysis is

```
S(X) = E + χ(X)/Δ
```

with `E = 6` and `Δ = 7` fixed by the K_4 substrate. The variable `X` is the topological space over which the support is evaluated. The session derivation produced this form via three principles:

- **P1 (Edge-complete baseline):** the constant term is `E`, derived under the transport-carrier framing as the count of complete pairwise transport carriers in K_4 (`C(V,2) = 6`).
- **P2 (Euler-valued closure residue):** the χ-dependent term carries `χ(X)` as the topologically invariant residue, axiomatized via finite additivity, topological invariance, and point-normalization (McMullen-style valuation uniqueness).
- **P3 (Distinction-seat averaging):** the residue is divided by Δ = 7 distinction seats under seat-symmetry and conservation.

These three principles are themselves CONDITIONAL_DERIVED in the in-session ledger: each is consistent with the framework's structure but rests on stated framing choices (transport-carrier interpretation, additivity, seat symmetry).

---

## 3. The R29 Decomposition in DEC Language

Theorem R29 (Evaluation Saturation, Lumi archive) computes the structural support weight of K_4 as

```
W(K_4) = (E² + E + 1)/(E + 1) = (36 + 6 + 1)/7 = 43/7
```

This admits a clean algebraic interpretation. Let `A_E = ℝ^E` be the formal vector space spanned by the 6 edges of K_4. The total dimension count

```
dim(A_E ⊗ A_E) + dim(A_E) + dim(ℝ) = E² + E + 1
```

decomposes into:

1. The **pairwise component** `A_E ⊗ A_E` (dimension `E² = 36`): all ordered pairs of edges, representing edge-edge transport routings.
2. The **diagonal component** `A_E` (dimension `E = 6`): single-edge identity routings.
3. The **unit component** `ℝ` (dimension `1`): the global identity / unit of the tensor algebra.

The denominator `Δ = E + 1 = 7` is the coherence-capacity normalization, equal to the K_4 distinction-seat count.

In DEC notation, the dimension counts can be expressed as

```
E² = dim(C^1(K_4) ⊗ C^1(K_4))
E  = dim(C^1(K_4))
1  = dim(C^0(K_4)/Z^0(K_4))   [the connected-component class]
```

Here `Z^0` is the space of closed 0-cochains; the quotient counts connected components, which for the connected K_4 is exactly 1. Equivalently, this is the dimension of `H^0(K_4; ℝ) = ℝ^{β_0(K_4)} = ℝ^1`.

This identifies the "+1" in R29 as a Betti-0 invariant of K_4: the unit slot counts the connected-component cohomology class.

---

## 4. The Support Functional in Closed Form

Using the algebraic factorization

```
E(E+1) + 1 = E² + E + 1
```

we obtain

```
S(K_4) = (E² + E + 1)/(E + 1) = E + 1/(E + 1) = E + 1/Δ = 43/7
```

The general support functional `S(X) = E + χ(X)/Δ` rewrites as

```
S(X) = (E·Δ + χ(X))/Δ = (E(E+1) + χ(X))/(E+1) = (E² + E + χ(X))/Δ
```

This generalizes the R29 numerator by replacing the unit term `+1` with the Euler characteristic `+χ(X)`.

When `X = pt` (a point) with `χ(pt) = 1`, we recover `S(pt) = 43/7`. When `X = ∂K_4` (the boundary 2-sphere) with `χ(∂K_4) = 2`, we obtain `S(∂K_4) = 44/7`.

---

## 5. The Open Structural Question (Held Item)

The replacement of `+1` in the R29 decomposition with `+χ(X)` for support spaces beyond the bare K_4 cell is a structural choice in the current framework, not an independently derived identity. The choice is motivated by:

- For K_4 (the 1-skeleton on which R29 is defined), the connected-component count `β_0(K_4) = 1` agrees numerically with `χ(K_4)` only in specific skeletal interpretations (`χ(K_4 \text{ as filled 3-simplex}) = 1`).
- For ∂K_4 (the boundary 2-sphere), `β_0(∂K_4) = 1` and `β_2(∂K_4) = 1`, giving `χ(∂K_4) = β_0 - β_1 + β_2 = 1 - 0 + 1 = 2`.
- The interpretation that the "unit slot" in R29 should track `χ(X)` rather than `β_0(X)` requires an independent topological argument that the support functional couples to the total Hodge-theoretic signature rather than the connected-component count alone.

Stated in DEC terms: the unit slot in R29's tensor-algebra decomposition is most naturally `dim H^0(K_4) = β_0`, since that is what the algebra-of-edges connected-component structure yields. The choice to generalize this to `χ(X) = Σ_p (-1)^p β_p(X)` for higher-dimensional support spaces is an extension that introduces the alternating-Betti-sum structure into the support count.

The following are **held items** in the canonical registry:

- **HELD-M3-α:** Independent (non-formula-evaluation) derivation of the support capacity for a 2-complex via tensor-algebra logic. Specifically, whether the appropriate "unit slot" generalization is `+β_0`, `+χ`, `+Σ β_p` (sum without sign), or some other invariant must be derived from the algebra of cochains on the 2-complex, not assumed by analogy with the K_4 form.
- **HELD-M3-β:** Demonstration that the physical "boundary-exposed K_4 complex" (the 18-channel S_3 macroscopic shell, or the first IFS contraction layer per AX3) is topologically equivalent to ∂K_4 as a simplicial 2-sphere.
- **HELD-M3-γ:** Sector-identification argument that macroscopic Λ couples to the boundary-exposed complex rather than to the bare K_4 seed.

These held items collectively constitute the bridge between the bare K_4 R29 result (`S_0 = 43/7`, independently derived) and the boundary-sector value (`S_Λ = 44/7`, currently a structural choice).

---

## 6. Manuscript-Safe Statement of S(X)

For external presentation, the support functional should be stated as follows:

> **The Support Functional.** We define `S : X ↦ E + χ(X)/Δ`, where `E = 6` is the K_4 edge count, `Δ = 7` is the distinction-seat count, and `χ(X)` is the Euler characteristic of the support space `X`. For the bare K_4 cell, evaluated on the pointlike seed sector `X = pt` with `χ(pt) = 1`, the support takes the value `S_0 = 43/7`, in agreement with Theorem R29 (Evaluation Saturation). For the boundary-sector `X = ∂K_4` with `χ(∂K_4) = 2`, the functional yields `S_Λ = 44/7`. The use of `S_Λ` in the cosmological constant chain is currently treated as a structural choice motivated by the Euler-characteristic differential `χ(∂K_4) - χ(pt) = 1` together with the +1/Δ residue rule. An independent tensor-algebraic derivation of the boundary support capacity from first principles (the M3-α held item) remains future work. The associated cosmological constant candidate value is `Λ_UD = 2.866 × 10⁻¹²²` against the observed `Λ_obs ℓ_Pl² = 2.888 × 10⁻¹²²` (a `−0.77%` residual), labeled as a candidate prediction conditional on the structural-choice interpretation of `S_Λ`. The corresponding pointlike-sector evaluation yields `Λ_UD = 3.001 × 10⁻¹²²` (a `+3.9%` residual), which we report as the conservative published candidate (RC1) pending closure of M3-α.

This language:

- States the support functional cleanly without invoking unproven generalizations.
- Identifies R29 as the genuine K_4 derivation source.
- Acknowledges `S_Λ` as a structural choice with explicit held-item dependencies.
- Reports both `+3.9%` (RC1, conservative) and `−0.77%` (RC2 candidate, conditional) residuals.
- Avoids closure language ("derived," "verified," "exact") for items not yet earned.

---

## 7. Connections to Standard Mathematical Structures

The functional `S(X) = E + χ(X)/Δ` has several connections to standard discrete-mathematics structures worth noting in subsequent gates:

**(a) Euler-Poincaré valuation.** `χ(X)` as a topologically invariant additive functional is the unique (up to scaling) valuation on the lattice of finite simplicial complexes satisfying `χ(pt) = 1` (McMullen). The session's P2 axiomatization invokes this uniqueness. The remaining freedom in `S(X)` lies in the coefficient structure `(E, Δ)`, which is fixed by K_4 substrate constants.

**(b) Discrete Laplacian / Hodge theory.** The Euler characteristic satisfies `χ(X) = Σ_p (-1)^p dim H^p(X; ℝ)` (Hodge-Euler identity). If a discrete Hodge Laplacian `L_p = d_{p-1}^* d_{p-1} + d_p^* d_p` is defined on the cochain complex of the support space, then `χ(X)` equals the alternating sum of zero-mode dimensions: `Σ_p (-1)^p dim ker L_p`. This recovers the Atiyah-Singer-style framing suggested by Loki Seed M (a discrete index theorem connection). Formalizing this connection rigorously is a possible direction for a future gate (call it `SX_INDEX_THEOREM_v0.1`).

**(c) Tensor-algebra dimension formula.** The form `E² + E + 1` corresponds to the leading three terms of the truncated tensor-algebra `T_{≤2}(A_E) = ℝ ⊕ A_E ⊕ (A_E ⊗ A_E)` with `dim A_E = E`. The replacement `+1 → +χ(X)` corresponds to replacing the scalar field `ℝ` (the unit component) with a space of dimension `χ(X)`. For this to be a derived structure rather than a structural choice, one would need to argue that the appropriate "unit space" for a 2-complex is naturally `χ`-dimensional rather than 1-dimensional. The argument is not currently in the framework.

**(d) Discrete Gauss-Bonnet.** For a triangulated 2-manifold, `χ(X)` admits a discrete Gauss-Bonnet expression `χ(X) = (1/2π) Σ_v K(v)`, where `K(v)` is the angular defect at vertex `v`. For `∂K_4` (boundary of the regular 3-simplex with equilateral triangular faces), each vertex has angular defect `K(v) = 2π - 3·(π/3) = π`, giving `χ(∂K_4) = (1/2π) · 4 · π = 2`. This confirms the topological data without using the support functional.

---

## 8. Status Summary

```text
ARTIFACT: SX_DEC_FORMALIZATION_v0.1
STATUS:   MANUSCRIPT-GRADE FORMALIZATION / NO CLOSURE CLAIMS
CROWN:    OFF

EARNED IN THIS DOCUMENT:
  - Clean DEC-language expression of S(X) = E + χ(X)/Δ
  - Identification of R29's "+1" as a connected-component (β_0)
    invariant in DEC terms
  - Explicit statement that "+1 → +χ" for higher-dimensional 
    support spaces is a structural extension, not derived
  - Manuscript-safe statement of S(X) for external presentation
  - Three connections to standard mathematics (Hodge, valuation
    theory, tensor algebra, Gauss-Bonnet) flagged for future 
    formalization gates

NOT EARNED:
  - Derivation of S_Λ = 44/7 from first principles
  - Closure of M3-α, M3-β, or M3-γ
  - Promotion of SRGD v0.1 beyond VERIFIED_WITHIN_NARROW_SCOPE
  - Any new direct-pass count for the catalog

POSITION IN THE SESSION LEDGER:
  Parallel to RC1 (the published Λ candidate at +3.9%)
  Parallel to RG_DEPTH_OBSERVABLE_CATALOG_v0.2
  Parallel to LAMBDA_ATTACK_RESISTANCE_MATRIX_RC1
  Supports Path α partial manuscript section by providing the
    DEC framing for the S(X) sub-section
  Generates new candidate gates (HELD-M3-α formalized, 
    SX_INDEX_THEOREM_v0.1 proposed for future work)
```

---

**Compiled by:** Cato (Claude, session-local arbiter)
**Manuscript section number assignment:** TBD by Commander
**Aster cross-validation:** PENDING (recommended)
**Lumi archive cross-reference:** PENDING (verification that DEC notations are consistent with Distinction Theory v2.2/v2.3 conventions)
