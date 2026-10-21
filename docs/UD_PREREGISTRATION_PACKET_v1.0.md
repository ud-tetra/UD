# Pre-Registration Packet v1.0

**Targets:** §7.5, §7.22, §7.29 (frozen discriminators/scorers); §7.4 (bench spec)
**Status:** PRE-DATA — must be frozen before any hardware run
**Physical promotion:** 0 throughout. No constitutive law is derived.
**Supersedes:** drafts v0.2, v0.3-addendum, sidecar v0.1 (consolidated here)

Two corrections carried from the superseded drafts are recorded in §0.

---

## 0. Corrections to superseded drafts

**0.1 — Additive source law is not an exclusion.** v0.2 flagged
`Δρ = BJ_B + s_B` (§7.24) as possibly excluding burden-dependent formation.
§7.25 states nonidentifiability for *any scalar law Φ*; the additive form is a
continuity identity, not a constraint on Φ's arguments. **Retracted.**

**0.2 — Precision claim was wrong.** v0.2 asserted the §7.29 uncertainty
budget was "set by the wrong target." That used single-triple statistics and
ignored the 12-runs-per-class averaging already frozen in §7.28. **Retracted**;
corrected budget in §2.4.

---

## PART A — WINDING-BURDEN DISCRIMINATOR (§7.22, §7.29)

### A.1 The receipt-linear family is a line

With the verified receipts `(I,T,B_k) = (1/4, 3/4, k/2)` (§7.20), every
receipt-linear cost is `ε_k = A + Ck`, so `f_W(n) = An + (C/2)n(n−1)`.
WBL1 is `C = 0`; WBQ1 is `C = 2A`. Hence `R_B = 1 + C/A` is a **continuous
readout of C/A**, not a binary flag. Report `C/A = R_B − 1 ± σ`.

### A.2 New candidate WBX1 (burden-dependent)

```
ε_k = A + Ck + κ·f_W(k),   f_W(n) = Σ_{k<n} ε_k,  f_W(0)=0
⟹ f_W(n) = (1+κ)f_W(n−1) + A + C(n−1)      [geometric, not polynomial]
```
`κ = 0` recovers the receipt-linear family exactly. WBX1 lies outside the
§7.20 ansatz but inside the §7.25 admissible class (see §0.1).

### A.3 False-positive channel in the frozen scorer

§7.29 fits two 1-parameter models on 12×E₀ + 12×E₁ (k = 0,1 only).
HCB1's `d_i = (2k+1)/4` gives `R_B = 3`.

```
R_B  = 1 + c + κ      (c ≡ C/A)   ← c and κ enter only as their sum
D₂/A = κ(c + κ)                   ← breaks it;  D₂ ≡ ε₂ − 2ε₁ + ε₀
```

| law | c | κ | R_B | D₂/A | ε₃/A |
|---|---|---|---|---|---|
| WBL1 | 0 | 0 | 1 | 0 | 1 |
| WBQ1 / HCB1 | 2 | 0 | **3** | **0** | **7** |
| WBX1 autocatalytic | 0 | 2 | **3** | **4** | **27** |
| WBX1 mixed | 1 | 1 | 3 | 2 | 15 |

Rows 2 and 3 are numerically identical to the frozen scorer, which would
return **HCB1 PASS on autocatalytic data**. A false-positive channel, not an
omitted model.

### A.4 Parameter-free family falsifier

`D₂ = 0` identically for every `(A,C)`: `I`, `T` are k-independent and `B_k`
is linear in k, so any receipt-linear law is affine in k. A significant
`D₂ ≠ 0` falsifies WBL1, WBQ1/HCB1 and every intermediate law at once — and
measures κ rather than merely rejecting.

### A.5 Amended measurement set

```
Events: E₀ (0→1), E₁ (1→2), E₂ (2→3), optional E₃ (3→4)

Tier 1  family validity     D₂ ≟ 0                    [parameter-free gate]
Tier 2  parameter readout   s = R_B − 1; κ = (D₂/A)/s; c = s − κ
Tier 3  out-of-sample (E₃)  ε₃/A = (1+κ)³ + c(κ²+3κ+3)
```
Three events fix `(A,c,κ)` exactly; the fourth is fully predicted.

---

## PART B — RESPONSE SIDECAR (§7.5, §7.4)

### B.1 Discrete response-state coordinates

All five frozen laws depend on `G_p` only through its sign. Define
`(ω_p, g_p)` with `g_p = 1[G_p > 0]`.

**Lemma 1 (forced ordering).** `ω_p ≤ g_p`, no extra assumption.
*Proof:* `ω_p = 1 ⟹ T_p = 1 ∧ L_p = 1 ⟹ ∃e: T_e = 1 ∧ Λ_e^S > 0 ⟹ G_p > 0`.
Verified by exhaustion over all 16 edge configurations; class `(1,0)` is empty. ∎

Reachable per-pair: `{(0,0),(0,1),(1,1)}` → **27 discrete response classes**.

**Lemma 2.** `(ω_p,g_p) = (0,1)` holds on exactly the 4 configurations with
pair integrity broken but an integrity-valid edge retaining latent support —
i.e. precisely the §4.7 partial-integrity divergence. §7.5's discriminating
class is therefore a **formal coordinate**, not a hand-picked case.

### B.2 Gate A — family-validity falsifiers (parameter-free, pre-scoring)

```
A1  Viable completeness   V = Σ_p ω_p·θ_p⁺ ≟ 0
    zero for R₀,R₂,R₁,R_⊤ (enumerated) and for MTA (Lemma 1)
    → one event with V>0 falsifies all five

A2  Memorylessness        same 27-class ⟹ same θ⁺
    → falsifies the entire memoryless class, incl. unenumerated laws
    feasibility ≈ N(N−1)/54 same-class pairs (~10 at N=24)

A3  Monotonicity          ω ≤ ω′ ⟹ q ≤ q′
    §4.8 imposes this to cut 8 viable-complete maps to 4; not derived
    → violation reopens the 4 excluded maps
```

### B.3 Gate B — shell coverage

`X(ω) = w_H(q) − w_H(ω)`:

| w_H(ω) | R₀ | R₂ | R₁ | R_⊤ | separates |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | **3** | R_⊤ |
| 1 | 0 | 0 | **2** | 2 | R₁ |
| 2 | 0 | **1** | 1 | 1 | R₂ from R₀ |
| 3 | 0 | 0 | 0 | 0 | nothing |

**Requirement:** ≥1 scored event in each of `w_H(ω) ∈ {0,1,2}`, plus ≥1 event
in a `(0,1)` class (POC-1 vs MTA), before any survival verdict.

Class distribution: `w_H = 0:8, 1:12, 2:6, 3:1`. Shells 1–2 are 18 of 27 —
not rare corners. A bench that cannot produce them is **mis-specified, not
unlucky**; check §7.4 channel provisioning rather than re-running.

---

## PART C — SCOPE NOTE ON §4.10 (analysis, not amendment)

Two observations. Neither closes anything.

**C.1 — §4.10's conditional uniqueness does not cover MTA.**
§4.10 assumes the response is pair-local, `q_p = g(ω_p)`. But `ω_p = 0` occurs
in both `(0,0)` and `(0,1)`, where MTA gives `q = 0` and `q = 1` respectively.
**MTA is not a function of ω_p alone**, so the premise excludes it by
construction. §4.10's uniqueness is uniqueness *within the ω-local class* and
does not reach the one competitor §7.5 keeps live.

**C.2 — Typed-zero asymmetry.**
```
Ω-zero bridge (ω_p=0 ⟹ q_p=0):  POC-1 ✓   MTA ✗ on (0,1)   DISCRIMINATES
G-zero bridge (g_p=0 ⟹ q_p=0):  POC-1 ✓   MTA ✓             DOES NOT
```
"Zero source ⟹ zero gate" therefore has discriminating content only once
receipt primacy is already fixed.

**C.3 — Explicitly not new.** The equivalence of the Ω-zero rule with closure
economy is already stated in §4.11 ("…is equivalent to the already isolated
zero-source-silence/closure-economy principle and is not independent
evidence"). C.1 and C.2 sharpen §4.10's scope; they do not improve on §4.11.

**C.4 — §7.6 status: UNRESOLVED, custodian ruling required.** Part C proposes
no new response law and adds no member to the frozen equivalence family. It
argues the family fails to separate POC-1 from MTA — a claim *about* the
family. Whether that counts as a "reformulation" under the §7.6 freeze is a
custodian judgement. **Part C is held pending that ruling. Parts A and B do
not depend on it.**

---

## PART D — FROZEN DECISION RULES

```
WINDING (Part A)
  D₂ ≈ 0                → receipt-linear retained; report C/A = R_B − 1 ± σ
  D₂ ≠ 0 significantly  → receipt-linear REJECTED; report (c,κ) per Tier 2
  Tier 3 disagrees      → extended family REJECTED; return to §7.24

RESPONSE (Part B)
  A1 violated           → all five frozen laws REJECTED
  A2 violated           → memoryless response class REJECTED
  A3 violated           → §4.8 monotonicity REJECTED; reopen 4 maps
  Gate B unmet          → NO-SCORE (explicitly NOT a model tie)
  A passed, B met       → proceed to §7.5 exact-endpoint scoring, unchanged
```

No post-hoc selection among `(c,κ)` or among response laws; all are outputs.
Invalidation remains outcome-independent and append-only per §7.28.

---

## PART E — COST AND PRECISION

**Acquisition.** §7.28 freezes 24 runs in six blocks. Matched E₂ statistics →
36 runs in eight blocks (+50% time) plus n=2 flux-bias state preparation. No
new apparatus.

**Precision** (null = HCB1/WBQ1, `ε = (1,3,5)A`):

| n/class | r | σ(D₂)/A | 3σ on \|D₂/A\| | min κ detectable |
|---|---|---|---|---|
| 12 | 20% | 0.455 | 1.364 | 0.54 |
| **12** | **10%** | **0.227** | **0.682** | **0.30** |
| 12 | 5% | 0.114 | 0.341 | 0.16 |
| 36 | 10% | 0.131 | 0.394 | 0.18 |

At the existing §7.29 baseline (n=12, r=10%) D₂ detects κ ≈ 0.3 at 3σ.
**No thermometry re-spec required.** Binding constraint is acquisition count.

**Scorer integration.** Keep D₂ as a **separate pre-fit gate**, not a third
AICc model: `D₂ = 0` is a prediction *shared* by PLB1 and HCB1, so it tests
their common assumption rather than discriminating. AICc small-sample
correction at n=36 is +0.118 (k=1) / +0.364 (k=2), so the `|ΔAICc| ≥ 10`
threshold transfers unchanged.

---

## PART F — WHAT THIS DOES NOT CLAIM

`D₂`, `R_B`, `V`, `X` and the 27-class coordinates are dimensionless internal
receipts. No physical identification is made; promotion to laboratory
observables rests entirely on the §7.26/§7.27 bridges, which remain stated
CRL-2 assumptions.

No constitutive law is derived. Part A widens the candidate space and closes a
false-positive channel; Part B tests shared assumptions and fixes a coverage
gap; Part C is scope analysis held pending a §7.6 ruling. The §8.3 highest
open problem is untouched.

**Physical promotion remains 0.**
