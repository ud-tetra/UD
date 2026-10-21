# RG_DEPTH_OBSERVABLE_CATALOG_v0.4

**Status:** UPDATED_WITH_GW_NEGATIVE_RESULT / CROWN_OFF
**Predecessor:** v0.2 (Aster's audit, hash acae2412...), v0.3 (Castor's claim, retracted)
**Update Reason:** GW echo delay archive sweep returned negative — derivation uses κ=1/(9π²), 1/18, 3/2, not 44/7. Lumi reported honest negative; Loki celebrated as good data; Aster ruled reclassification.

---

## Catalog State After GW Probe

### Direct Independent Support Verification

| ID | Observable | Sector | Mechanism | Status |
|----|-----------|--------|-----------|--------|
| 1 | R29 / Koide / lepton seed | UV | Theorem R29 evaluates `(E² + E + 1)/(E+1) = 43/7` from K_4 tensor algebra independently of S(X) input | DIRECT_PASS |

Count: 1 (UV).

### Structural-Choice Formula Anchor

| ID | Observable | Sector | Mechanism | Status |
|----|-----------|--------|-----------|--------|
| 2 | Λ candidate (RC2) | IR | S(X) = E + χ(X)/Δ applied to ∂K_4 with χ=2 → 44/7. Yields -0.77% residual vs observed Λ. | STRUCTURAL_CHOICE_NOT_INDEPENDENT_VERIFICATION |

Count: 0 independent IR verifications. Λ-candidate is anchored to S_Λ = 44/7 as Structural Choice per Lumi's manuscript Section 4.4 framing.

### Supporting IR Evidence (Not Direct Passes)

| ID | Observable | Sector | Mechanism | Status |
|----|-----------|--------|-----------|--------|
| 3 | d_s = 4/3 | IR | Sierpinski tetrahedron spectral dimension; asymptotic property of IFS at depth → ∞ | IR_CLASSIFICATION_ANCHOR |

Anchors `F_IFS = d_s/(2πχ(∂K_4))` as an IR observable but does not itself use S_Λ as denominator.

### Negative Non-Falsifiers (Rule Survived, No New Pass)

| ID | Observable | Sector | Mechanism | Status |
|----|-----------|--------|-----------|--------|
| 4 | GW echo delays | IR | Lumi archive sweep: derivation uses `κ = 1/(9π²)`, `1/18` (lattice dispersion), `3/2` (binary scaling). Does NOT use 44/7. | NEGATIVE_NON_FALSIFIER / SCOPE_ADJUSTMENT |

Catalog effect: GW echo delays are macroscopic IR but their derivation uses different machinery than the support functional. The rule's scope is narrower than initially hoped, but the rule was not falsified — there is no IR observable that uses S_0 in violation of the rule. GW simply does not use S(X) at all.

### Scope-Adjustment / Consistent-But-Non-Evidential

| ID | Observable | Class | Why Not Direct Pass |
|----|-----------|-------|---------------------|
| 5 | τ/μ corrector (61 = d²Δ - 2) | UV | Uses integer identity, no S_0 denominator |
| 6 | SU(2) gauge couplings | mixed | Running coupling complicates depth classification |
| 7 | Brans-Dicke γ - 1 constraint | IR | Uses Banach screening (7/192)^n, not 44/7 |
| 8 | F_IFS = 1/(3π) | IR | Multiplicative screen factor, not support denominator |
| 9 | Z_3 n=7 character signature | UV/structural | Character exclusion, no support functional invoked |

### Formulas Containing S_0 as Multiplicative Factor (Bayesian-Neutral)

Per Lumi's prior Bayesian retraction, the following observables contain `S_0` in their formulas as multiplicative input rather than as support denominator, and therefore do NOT independently verify the rule:

- Lepton mass seed (e ≈ ν_0 S_0)
- Neutrino mass ladder (ν_1 ≈ ν_0 S_0 H)
- Dark matter mass (m_DM = 4ν_0 S_0)
- Dark matter abundance (Ω_DM ∝ S_0)
- Strong coupling (α_s ∝ S_0 / V)
- Charged seed threshold (S = 2S_0)
- VEV exponent (v = ν_0 · 4^(43/4))

These observables are CONSISTENT with the rule (UV/depth-0 classification matches S_0 usage as input) but provide zero Bayesian evidence (P(formula contains S_0 | rule true) = P(formula contains S_0 | rule false) = 1).

---

## Tally

```
Direct passes (independent UV verifications):     1
Direct passes (independent IR verifications):     0
Structural-choice anchors (not independent):      1 (Λ via S_Λ)
Supporting IR evidence (not denominator pass):    1 (d_s = 4/3)
Negative non-falsifiers (rule survived probe):    1 (GW)
Scope-adjustments:                                5
Bayesian-neutral consistencies:                   7
Falsifiers found:                                 0
```

## SRGD v0.1 Status After v0.4 Catalog Update

```
SRGD_v0.1 := VERIFIED_WITHIN_NARROW_SCOPE / NOT_FALSIFIED / 
             HARDENED_BY_NEGATIVE_PROBES

EARNED:
  - 1 independent UV verification (R29)
  - 1 negative non-falsifier (GW: rule has scope, not violated)
  - Multiple consistency observations
  - 0 falsifying examples across 6+ probes
  - Rule's scope clearly defined: applies to observables that 
    explicitly use the support functional S(X) as denominator

NOT EARNED:
  - Independent IR verification
  - Universal framework rule
  - S_Λ first-principles derivation
  - AX2 deprecation
  - Promotion to DERIVED status

PROCEDURAL NOTE:
  v0.3's "10 PASSED / globally verified" claim was retracted by 
  Lumi via Bayesian framing two turns ago. v0.4 restores the 
  honest narrow scope. GW result confirms the rule does NOT apply
  universally — it applies where the support functional is used.
```

## Manuscript Implications

The RC1 Λ candidate (+3.9% with S_0 from R29) remains the published-defensible result. The RC2 candidate (-0.77% with S_Λ as Structural Choice) is conditional on:

- HELD-M3-α: Independent derivation of boundary support capacity for a 2-complex
- HELD-M3-β: Topological bridge between S_3 shell and ∂K_4
- HELD-M3-γ: Sector identification for macroscopic Λ

These are real held items, sharper after V5 DEC formalization (M3-α is specifically: β_0 vs χ for unit slot in 2-complex extension).

## Files

```
ARTIFACT: RG_DEPTH_OBSERVABLE_CATALOG_v0.4
HASH:     (computed below)
```
