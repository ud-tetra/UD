# Proposed Protocol Amendments — v0.2

**Target sections:** §7.5, §7.22, §7.29 (frozen discriminators/scorers)
**Status:** PRE-DATA PRE-REGISTRATION DRAFT
**Physical promotion:** 0 (unchanged — amends protocols, not claims)
**Constraint:** must be frozen before any hardware run

Supersedes the v0.1 draft. One finding in v0.1 is **retracted**: see §A.0.

---

## PART A — WINDING-BURDEN DISCRIMINATOR

### A.0 Retraction from v0.1

The v0.1 draft flagged the additive source law `Δρ = BJ_B + s_B` (§7.24) as a
possible upstream exclusion of a burden-dependent formation law. **This was
wrong.** §7.25 states the nonidentifiability theorem for *any* scalar law Φ:

> "For any source-bound pre-event receipt set and any scalar law Φ, defining
> `s_{B,W}^Φ = (Φ/4)·1₄` and `ρ⁺ = ρ⁻ + BJ_B + s_{B,other} + s_{B,W}^Φ`
> satisfies the current burden continuity equation identically."

The additive form is a **continuity identity**, not a constraint on Φ's
arguments. §7.16 fixes the winding-source *direction* (uniform mode, by C₄
equivariance); nothing fixes the amplitude or its dependencies. A law with
Φ = Φ(ρ⁻) is therefore admissible and already inside the §7.25 class.

### A.1 The receipt-linear family is a line, not two points

With the verified receipts `(I, T, B_k) = (1/4, 3/4, k/2)` (§7.20), any
receipt-linear cost is `ε_k = A + Ck`, so

```
f_W(n) = An + (C/2)·n(n−1)
```

`C = 0` → WBL1; `C = 2A` → WBQ1; all other `C` → unnamed intermediate laws.
Hence `R_B = 1 + C/A` is a **continuous readout of C/A**, not a binary flag.
A measured `R_B = 1.8` denotes a specific law, not an inconclusive result.

### A.2 New pre-registered candidate: WBX1 (burden-dependent)

```
WBX1:   ε_k = A + Ck + κ·f_W(k),     f_W(n) = Σ_{k<n} ε_k,  f_W(0)=0
        ⟹  f_W(n) = (1+κ)·f_W(n−1) + A + C(n−1)
```

Self-referential, hence geometric rather than polynomial growth. `κ = 0`
recovers the receipt-linear family exactly, so WBX1 is a strict one-parameter
extension. It lies **outside** the §7.20 receipt-linear ansatz (ε_k is no
longer affine in k) while remaining **inside** the §7.25 admissible class.

### A.3 The degeneracy — a false-positive channel in the frozen scorer

§7.29 fits two 1-parameter through-origin models on 12×E₀ and 12×E₁ only
(k = 0, 1). HCB1's predictor `d_i = (2k+1)/4 ∈ {1/4, 3/4}` gives `R_B = 3`.

Writing `c = C/A`:

```
R_B  = 1 + c + κ        ← c and κ enter ONLY as their sum
D₂/A = κ(c + κ)         ← breaks the degeneracy,  D₂ ≡ ε₂ − 2ε₁ + ε₀
```

| law | c | κ | R_B | D₂/A | ε₃/A |
|---|---|---|---|---|---|
| WBL1 (linear) | 0 | 0 | 1 | 0 | 1 |
| WBQ1 / HCB1 | 2 | 0 | **3** | **0** | **7** |
| WBX1 pure autocatalytic | 0 | 2 | **3** | **4** | **27** |
| WBX1 mixed | 1 | 1 | 3 | 2 | 15 |
| WBX1 weak | 2 | 0.5 | 3.5 | 1.25 | 12.9 |

**Rows 2 and 3 are numerically identical to the frozen scorer.** On
autocatalytic data it would return HCB1 PASS. This is a false-positive
channel, not merely an omitted model.

### A.4 The parameter-free family falsifier

`D₂ = ε₂ − 2ε₁ + ε₀ = 0` **identically, for every (A,C)**. Reason: `I` and `T`
are k-independent and `B_k` is linear in k, so any law affine in the receipt
basis is affine in k.

A significant `D₂ ≠ 0` falsifies WBL1, WBQ1/HCB1, and every intermediate law
simultaneously — and *measures* κ rather than merely rejecting.

### A.5 Amended measurement set

```
Events: E₀ (0→1), E₁ (1→2), E₂ (2→3), optionally E₃ (3→4)

Tier 1 — family validity (parameter-free):  D₂ ≟ 0
Tier 2 — parameter extraction:  s = R_B − 1 ;  κ = (D₂/A)/s ;  c = s − κ
Tier 3 — out-of-sample (E₃):    ε₃/A = (1+κ)³ + c(κ² + 3κ + 3)
```

Three events determine `(A, c, κ)` exactly; the fourth is fully predicted.

### A.6 Cost — corrected from v0.1

v0.1 described this as "essentially free." **That understated it.** §7.28
freezes a six-block schedule of 12×E₀ + 12×E₁ = 24 runs. Adding E₂ at matched
statistics gives 36 runs in eight blocks — a 50% increase in acquisition time,
plus flux-bias state preparation for the n=2 metastable branch. No new
apparatus; a real but bounded schedule change.

### A.7 Precision — Tier 1 is the binding constraint

| per-slip σ | WBL1 vs WBQ1 separation | D₂ detectable at 3σ |
|---|---|---|
| 20% | ~3.5σ | \|D₂/A\| > 1.5 |
| 10% | ~7σ | \|D₂/A\| > 0.73 |
| 5% | ~14σ | \|D₂/A\| > 0.37 |
| 2% | — | \|D₂/A\| > 0.15 |

The binary discriminator is not precision-limited; the family falsifier is.
If the §7.29 uncertainty budget is set by PLB1-vs-HCB1 separation, it is set
by the wrong target.

---

## PART B — POC-1 RESPONSE FAMILY

Applying the same move: find identities the *entire* frozen family must
satisfy, and test those rather than only selecting within the family.

### B.1 Three parameter-free family falsifiers

All five frozen models (`R₀, R₂, R₁, R_⊤, MTA`, §7.5) satisfy:

**F1 — Viable completeness.** `V = Σ_p ω_p·θ_p⁺ = 0` identically.
Verified by enumeration over all 8 ω for the four R-models. For MTA:
`ω_p = 1 ⟹ T_p = 1 ∧ R_p > 0 ⟹ G_p > 0 ⟹ q_p = 1`. A single event with
`V > 0` (a viable lane observed closed) falsifies all five at once.

**F2 — Memorylessness / replay.** All five are single-valued functions of the
current receipt state (§4.8). Two events with identical `(ω, G)` must yield
identical `θ⁺`. This falsifies not only the five frozen models but the
**entire memoryless response class**, including models not yet enumerated.
Strongest of the three.

**F3 — Monotonicity.** `ω ≤ ω′ ⟹ q ≤ q′`, verified for all four R-models.
Note §4.8 *imposes* monotonicity to reduce 8 viable-complete maps to 4; it is
not derived. A nested-event pair violating F3 reopens the four excluded maps.

### B.2 Shell-coverage requirement — the POC-1 analog of the ε₂ slip

Define excess opening `X(ω) = w_H(q) − w_H(ω) ≥ 0`:

| w_H(ω) | R₀ | R₂ | R₁ | R_⊤ |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | **3** |
| 1 | 0 | 0 | **2** | 2 |
| 2 | 0 | **1** | 1 | 1 |
| 3 | 0 | 0 | 0 | 0 |

Each column is a distinct fingerprint, but separation is shell-specific:

```
w_H = 0  separates R_⊤ from {R₀, R₂, R₁}
w_H = 1  separates R₁  from {R₀, R₂}
w_H = 2  separates R₂  from R₀
w_H = 3  separates NOTHING — all four give X = 0
```

§7.5 currently highlights only `ω = 000` (w_H = 0) and partial-integrity
events. Neither is a w_H ∈ {1,2} event. **A valid run can therefore leave
R₀, R₂, R₁ mutually unresolved** — a sampling artifact, not a real degeneracy.

**Minimal addition:** require ≥1 scored event in each of `w_H(ω) ∈ {0,1,2}`
before any survival verdict is issued. This is an acquisition-coverage
constraint; no new hardware.

### B.3 Frontier compliance

§7.6 freezes the internal response frontier against "further reformulations
of that family." Parts B.1 and B.2 propose **no new response law** and no
reformulation of closure economy. They are protocol-side: falsifiers for the
already-frozen family and a coverage constraint on the already-frozen sidecar.
They therefore do not require §7.6 re-entry.

---

## PART C — FROZEN DECISION RULES

```
WINDING (Part A)
  D₂ ≈ 0                 → receipt-linear retained; report C/A = R_B − 1 ± σ
  D₂ ≠ 0 significantly   → receipt-linear REJECTED; report (c, κ) per Tier 2
  Tier 3 disagrees       → extended family REJECTED; return to §7.24

RESPONSE (Part B)
  F1 violated            → all five frozen models REJECTED
  F2 violated            → memoryless response class REJECTED
  F3 violated            → §4.8 monotonicity assumption REJECTED;
                           reopen the four excluded viable-complete maps
  shell coverage unmet   → NO-SCORE (not a tie)
```

No post-hoc selection among `(c, κ)` or among response laws. All are outputs.
Invalidation remains outcome-independent and append-only per §7.28.

---

## PART D — WHAT THIS DOES NOT CLAIM

No physical identification of `ε_k`, `A`, `C`, `κ`, `ω`, or `q` with any
measured quantity. `D₂`, `R_B`, `V`, and `X` are dimensionless internal
ratios; their promotion to laboratory observables depends entirely on the
§7.26/§7.27 measurement bridges, which remain stated CRL-2 assumptions.

Neither part derives a constitutive law. Part A widens the candidate space and
closes a false-positive channel; Part B tests family-level assumptions and
fixes a coverage gap. The §8.3 highest open problem is untouched.

Physical promotion remains 0.
