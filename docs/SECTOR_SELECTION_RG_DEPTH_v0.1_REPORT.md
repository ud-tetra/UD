# SECTOR_SELECTION_RG_DEPTH_v0.1

**Status:** CONDITIONAL_PASS_PENDING_ARCHIVE_VERIFICATION
**Type:** Disciplined gate / conditional derivation attempt
**Source:** Loki seed (Mechanism 2, depth-test), validated for gate formation by Cato/Aster
**Frame:** Loki-seed → firewall processing → proper UD gate under standard discipline

---

## Proposal

A UD observable couples to the support sector determined by its IFS depth:

- **UV / local / depth-0** observables couple to **S₀ = 43/7** (pointlike support, χ(pt) = 1).
- **IR / global / depth ≥ 1** observables couple to **S_Λ = 44/7** (boundary support, χ(∂K_4) = 2).

**Structural rationale.** Depth-0 observables are evaluated within a single K_4 cell, so their support is the closed cell — pointlike. IR/global observables require the boundary structure of K_4 (∂K_4 = S²) to be exposed, which happens only after at least one IFS contraction step. Their support therefore includes the boundary closure residue, raising S₀ by exactly `χ(∂K_4)/Δ − χ(pt)/Δ = (2−1)/7 = 1/7`. The +1/7 difference between S_Λ and S₀ is exactly the boundary residue.

## Pre-Registered Candidates

| ID | Rule |
|----|------|
| C0 | All observables use S₀ = 43/7 |
| C1 | All observables use S_Λ = 44/7 |
| **C2** | **UV/local observables use S₀; IR/global use S_Λ (M2 / RG-depth)** |
| C3 | Sector support interpolates continuously between S₀ and S_Λ |
| C4 | Framing torsion content (AX4) determines sector (M1) |
| C5 | Homology / open-boundary status determines sector (M3) |

C2 is the proposal under test.

## Pre-Registered Selection Tests

| ID | Test |
|----|------|
| T1 | Must not use observed Λ residual to determine the rule |
| T2 | Must classify Λ-sector BEFORE numerical evaluation |
| T3 | Must classify known UD observables consistently |
| T4 | Must explain why S_Λ appears only when boundary data required |
| T5 | Must produce falsifiers |

## Pre-Classification of UD Observables

Classification by structural reasoning (what does the observable probe?), BEFORE numerical Λ check:

| Observable | Class | Predicted Sector | Rationale |
|-----------|-------|------------------|-----------|
| Koide neutrino mass (ν₀ = 83.19 keV) | UV/local | S₀ | Intra-cell lepton-sector relation; no boundary data |
| τ/μ corrector (61 = d²Δ − 2) | UV/local | S₀ | 1D anomaly identity within lepton-mass cell |
| Spectral anomaly H = 16 + (d − d_s)/2 = 101/6 | IR/global | S_Λ | Uses asymptotic d_s = 4/3 (deep-IR fixed point) |
| F_IFS = 1/(3π) = d_s / (2π χ(∂K_4)) | IR/global | S_Λ | Explicit χ(∂K_4) dependence |
| Brans-Dicke γ − 1 (~10⁻⁹⁶) | IR/global | S_Λ (tentative) | Asymptotic gravitational scale |
| **Cosmological constant Λ** | **IR/global** | **S_Λ** | **Ultimate IR observable; dominates at cosmic scales** |
| Z₃ character signature n=7 | UV/structural | S₀ (or out of scope) | Structural constraint, may not couple to support sector |

**Note:** Λ classified as IR/global → S_Λ BEFORE numerical evaluation. Per T1, classification did not use the observed residual.

## Numerical Verification

| Component | Value |
|-----------|-------|
| ν₀ | 8.319 × 10⁴ eV |
| M_Pl | 1.22091 × 10²⁸ eV |
| F_IFS = 1/(3π) | 0.1061032954 |
| Δ | 7 |
| S₀ | 43/7 = 6.142857 |
| S_Λ | 44/7 = 6.285714 |
| Numerator (ν₀ · F_IFS^Δ / M_Pl)⁴ | 1.132292 × 10⁻¹²⁰ |

| Quantity | Value | Residual vs Λ_obs = 2.888137 × 10⁻¹²² |
|----------|-------|---------------------------------------|
| Λ_UD with S₀ | 3.000665 × 10⁻¹²² | **+3.896%** |
| Λ_UD with S_Λ | 2.865821 × 10⁻¹²² | **−0.773%** |

Rule C2 selects S_Λ for Λ, giving −0.773% residual.

## Falsifier Application

| ID | Falsifier | Status |
|----|-----------|--------|
| F1 | Deep-IR UD observable uses S₀ successfully | **PENDING** (archive verification) |
| F2 | UV/local seed observable requires S_Λ | **PENDING** (archive verification) |
| F3 | Λ can be evaluated entirely at depth 0 (no boundary data) | **NOT TRIGGERED** — F_IFS explicitly contains χ(∂K_4) |

F3 is structurally settled in-session: Λ-formula evaluation already uses boundary data through F_IFS, so Λ cannot be a depth-0 observable. This is consistent with rule C2.

F1 and F2 require Aster/Lumi to verify support-sector usage for other UD observables in the master archive.

## Test Results

| Test | Result |
|------|--------|
| T1 (no Λ residual used to set rule) | ✓ PASSED |
| T2 (classify Λ before numerical evaluation) | ✓ PASSED |
| T3 (consistent classification across observables) | ⊘ PARTIAL — pending archive verification of UV-observable support sectors |
| T4 (explain S_Λ vs S₀ via boundary data requirement) | ✓ STRUCTURAL EXPLANATION PROVIDED |
| T5 (produce falsifiers) | ✓ PASSED |

## Status

```text
ARTIFACT: SECTOR_SELECTION_RG_DEPTH_v0.1
STATUS:   CONDITIONAL_PASS_PENDING_ARCHIVE_VERIFICATION

EARNED:
  - Pre-registration discipline followed (C0-C5, T1-T5, F1-F3)
  - Rule C2 internally consistent under non-circular classification
  - Λ classified as IR/global → S_Λ before numerical evaluation
  - Λ evaluation with S_Λ produces -0.773% residual (improvement
    over S₀'s +3.896%)
  - Structural rationale (S_Λ - S₀ = boundary residue 1/Δ) is
    natural and explanatory
  - Falsifier F3 structurally not-triggered
  - Triple-convergence intuition (M1+M2+M3) partially formalized

NOT YET EARNED:
  - Status DERIVED (requires archive completion of T3 and F1/F2)
  - Operational definition of "depth" beyond intuitive UV/IR
  - Operational definition of "requires boundary data"
  - Manuscript-ready promotion
  - RC1 update to use S_Λ as canonical Λ sector

OUTSTANDING ARCHIVE PULLS:
  - Koide / lepton mass derivation: which support sector?
  - τ/μ corrector: which support sector?
  - Any other UD observable explicitly tagged with S_0 or S_Λ?
  - Brans-Dicke γ-1 constraint: which sector?
```

## Manuscript-Safe Language (Draft)

If archive verification supports the rule, the manuscript could state:

> "The cosmological constant couples to the boundary support `S_Λ = 44/7` rather than the pointlike support `S_0 = 43/7`. This sector selection follows the general RG-depth rule for UD observables: depth-0 (UV/local) observables couple to pointlike support `S₀`, while depth ≥ 1 (IR/global) observables couple to boundary support `S_Λ`. The difference `S_Λ − S_0 = 1/Δ` is exactly the additional boundary closure residue `χ(∂K_4)/Δ − χ(pt)/Δ = (2−1)/7`. Because the Λ formula evaluation requires boundary data through `F_IFS = d_s/(2π χ(∂K_4))`, Λ is unambiguously a depth ≥ 1 observable. Under this rule, `Λ_UD = 2.866 × 10⁻¹²²`, in agreement with the observed value `Λ_obs ℓ_Pl² = 2.888 × 10⁻¹²²` at the level of 0.77%."

This language is conditional on archive completion. Do NOT promote to manuscript without F1/F2 falsifier results.

## What This Gate Means for the Λ Chain

If archive verification supports C2:
- The Λ chain upgrades from RC1 (S₀, +3.9%) to a candidate RC2 (S_Λ, −0.77%)
- The sector-selection question — previously the major remaining hinge — is structurally resolved
- The RG-depth rule becomes a transferable UD principle applicable to other observables

If archive verification breaks C2:
- The rule weakens or fails for the proposed UV/IR partition
- Alternative formulations (M1 framing-torsion, M3 homology) may still hold
- RC1 with S₀ remains the published Λ result

## Compliance with Loki Firewall Discipline

This gate originated from a Loki seed (Mechanism 2, depth-test response). The seed was processed through the standard discipline pipeline:

1. **Loki output:** raw conjecture, no derivation claim, labeled "speculative seed generator"
2. **Salvage audit (Cato + Aster):** identified M2 as highest-priority for formalization; recommended gate creation
3. **Gate construction (Aster):** pre-registration of C0-C5, T1-T5, F1-F3
4. **Gate execution (Cato, this artifact):** pre-classification, numerical verification, falsifier application
5. **Status determination:** CONDITIONAL_PASS_PENDING_ARCHIVE_VERIFICATION

The Loki seed is acknowledged as the inspiration, not as primary evidence. The gate is evaluated on its own pre-registered standards.

---

**Author:** Cato (Claude, session-local arbiter)
**Date of execution:** 2026-01 (session timestamp)
**Aster validation:** TBD (cross-architecture mirror check)
**Lumi archive verification:** PENDING (F1, F2, T3 archive items)
