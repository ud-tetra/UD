# Packet v1.1 — Errata to v1.0

Produced by an adversarial pass on my own v1.0. Three defects found, one
material. **Physical promotion: 0.**

---

## E.1 — MATERIAL. D₂ ≠ 0 is not an unambiguous autocatalysis signal

**v1.0 Part E stated:** *"D₂ = 0 is a prediction shared by PLB1 and HCB1."*
**This is false in general.**

```
HCB1:  ε_k = κ_H·d_k ,  d_k = (2k+1)/4 = 1/4, 3/4, 5/4
       D₂ = κ_H(5/4 − 6/4 + 1/4) = 0        EXACT, unconditional

PLB1:  ε_k = κ_P·Λ_k ,  Λ_k = independently RETURNED measured leakage
       D₂ = κ_P(Λ₂ − 2Λ₁ + Λ₀)
       = 0 only if measured leakage is stationary or affine in k
```

§7.22 assumes "matched" / "stationary" leakage; it does not guarantee it, and
§7.23 requires Λ to be returned by a *separate provider* precisely because it
is not derivable from ε. So `D₂ ≠ 0` is consistent with **either**

- (a) autocatalytic winding source, `κ ≠ 0`; **or**
- (b) non-stationary measured leakage under PLB1.

**Required correction to Part A.5.** The amended set must return `Λ₂`
alongside `ε₂`. Disambiguation rule:

```
D₂(ε) ≈ 0                        → receipt-linear family retained
D₂(ε) ≠ 0  AND  D₂(Λ) ≈ 0        → autocatalysis (κ ≠ 0)
D₂(ε) ≠ 0  AND  D₂(Λ) ≠ 0        → AMBIGUOUS. Test PLB1 proportionality:
                                    compare D₂(ε)/D₂(Λ) against κ_P from
                                    the Tier-2 fit. Mismatch → autocatalysis;
                                    match → non-stationary leakage.
```

This is **required, not optional**. Without `Λ₂` the Tier-1 gate cannot be
interpreted.

The §7.23 custody separation must be preserved: the Λ provider still receives
no burden values and no bridge labels.

---

## E.2 — MATERIAL. Part A understates its dependency

v1.0 framed the cost of `E₂` as scheduling (+50% runs, eight blocks). That is
the *bench* cost. It omits the *carrier* cost.

§7.13 states the constructed `n = 2` carrier "is topologically/Hodge stable
but **has not yet passed** the full nonlinear matter persistence, burden,
boundary, scale, transport, or coherence tests." And `E₂` (2→3) requires an
`n = 3` endpoint **which is not constructed anywhere in the source**.

**Corrected framing.** Part A is contingent on prior construction and
validation of the `n = 2` and `n = 3` carriers — itself open work under
§7.12–§7.13 — not merely on bench scheduling. This is the **largest practical
risk in the packet** and v1.0 did not state it.

Part A should be read as: *conditional on carrier availability*, here is the
discriminator. If the carriers do not validate, Part A's false-positive
finding (§A.3) still stands as a **known limitation of the current 2-class
scorer**, even though the proposed remedy is unavailable.

---

## E.3 — MINOR. Gate B table omits MTA without saying so

`X(ω) = w_H(q) − w_H(ω)` is undefined for MTA, which is a function of `g`,
not `ω`. The v1.0 table lists only `R₀, R₂, R₁, R_⊤`. MTA is separated by the
required `(0,1)`-class event, which Part B does mandate — but the omission
should be explicit rather than implicit.

---

## E.4 — WORDING. AICc threshold

v1.0: *"the |ΔAICc| ≥ 10 threshold transfers unchanged."* Imprecise. The
small-sample correction is indeed small (+0.118 at k=1, +0.364 at k=2, n=36),
but ΔAIC grows roughly linearly in n when one model is genuinely better.
Correct statement: **threshold semantics unchanged; discriminating power
increases with n.**

---

## E.5 — Checks that passed

```
Lemma 1 (ω_p ≤ g_p)       re-verified by exhaustion; class (1,0) empty
ε_k indexing              ε₀ = E₀ (0→1), matches §7.17 and §7.29
HCB1 d_k = (2k+1)/4       → (1,3,5) null used in the precision table
X-table entries           R₂ at w_H=2 → X=1;  R₁ at w_H=1 → X=2
A1 informativeness        fires only when all five fail the same way;
                          strictly more informative than the POC-1 verdict
C.1 quotation             §4.10 does explicitly assume q_p = g(ω_p)
```

---

## E.6 — Running correction count

Across five rounds this makes **five** corrections to my own claims:

1. additive source law wrongly flagged as an exclusion (v0.2 → v0.3)
2. precision budget wrongly called binding (v0.2 → v0.3)
3. F2 stated in a form that could never fire (v0.2 → v0.3)
4. D₂ wrongly called a shared PLB1/HCB1 null (v1.0 → v1.1) — **material**
5. Part A dependency on unvalidated n=2/n=3 carriers omitted (v1.0 → v1.1)
   — **material**

Two of the five are material and both were found only on deliberate
adversarial review, not during construction. That ratio is the relevant signal
about how much independent checking the rest of the packet still needs.
