# Proposed Amendment to §7.5 — Sidecar Coverage and Family-Validity Gates

**Target:** §7.5 (pretarget multi-model response sidecar), §7.4 (bench spec)
**Status:** PRE-DATA PRE-REGISTRATION DRAFT — protocol text
**Physical promotion:** 0 (amends acquisition/scoring, introduces no response law)
**§7.6 compliance:** adds no member to the frozen response family; see §5 below

---

## 1. Response-state coordinates

All five frozen laws (`R₀, R₂, R₁, R_⊤, MTA`) depend on the continuous
receipt `G_p = Σ_{e∈M_p} T_e Λ_e^S` only through its sign. Define the
**discrete response-state coordinate** per opposite-edge pair:

```
(ω_p , g_p) ,      g_p = 1[G_p > 0]
```

**Lemma 1 (forced ordering).** `ω_p ≤ g_p`, with no additional assumption.

> *Proof.* `ω_p = 1 ⟹ T_p = 1 ∧ L_p = 1 ⟹ ∃e ∈ M_p : T_e = 1 ∧ Λ_e^S > 0
> ⟹ G_p > 0 ⟹ g_p = 1.* Verified by exhaustion over all 16 edge
> configurations `(T_{e1}, 1[Λ_{e1}>0], T_{e2}, 1[Λ_{e2}>0])`: the class
> `(1,0)` is empty. ∎

Reachable per-pair states are therefore `{(0,0), (0,1), (1,1)}`, giving
**27 discrete response classes** across the three matchings.

**Lemma 2 (identification of the (0,1) class).** `(ω_p, g_p) = (0,1)` holds
exactly on the four edge configurations in which pair integrity is broken
(`T_p = 0`) while some integrity-valid edge retains latent support
(`T_e = 1 ∧ Λ_e^S > 0`).

This is precisely the §4.7 partial-integrity divergence. The coordinate
system makes §7.5's special discriminating class a **formal coordinate**
rather than a hand-selected case.

---

## 2. Gate A — family-validity falsifiers (parameter-free)

These test assumptions shared by all five frozen laws. Each is a null
prediction with no fitted quantity.

**A1 — Viable completeness.**
```
V = Σ_p ω_p · θ_p⁺  ≟  0
```
Predicted zero by `R₀, R₂, R₁, R_⊤` (verified by enumeration over all 8 ω)
and by MTA (Lemma 1). **One event with `V > 0` falsifies all five.**

**A2 — Memorylessness / replay.**
Two events in the same one of the 27 classes must yield identical `θ⁺`.
Falsifies the entire memoryless response class, including laws not yet
enumerated. Feasibility: ≈ `N(N−1)/54` same-class pairs under uniform
occupancy; ~10 usable pairs at N = 24, more under realistic non-uniform
occupancy.

**A3 — Monotonicity.**
For a nested pair `ω ≤ ω′`, require `q ≤ q′`. §4.8 *imposes* monotonicity to
reduce 8 viable-complete maps to 4; it is not derived. A violation reopens
the four excluded maps.

Gate A is evaluated **before** any model-survival scoring.

---

## 3. Gate B — shell-coverage requirement

Define excess opening `X(ω) = w_H(q) − w_H(ω) ≥ 0`.

| w_H(ω) | R₀ | R₂ | R₁ | R_⊤ | separates |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | **3** | R_⊤ |
| 1 | 0 | 0 | **2** | 2 | R₁ |
| 2 | 0 | **1** | 1 | 1 | R₂ from R₀ |
| 3 | 0 | 0 | 0 | 0 | — nothing |

Each column is a distinct fingerprint, but separation is shell-specific.
§7.5 currently highlights only `ω = 000` (w_H = 0) and partial-integrity
events; neither is a `w_H ∈ {1,2}` event.

**Requirement.** At least one scored event in each of
`w_H(ω) ∈ {0, 1, 2}`, plus at least one event in a `(0,1)` class
(POC-1 vs MTA), before any survival verdict is issued.

**Feasibility.** The 27 classes distribute as `w_H = 0 : 8`, `1 : 12`,
`2 : 6`, `3 : 1`. Shells 1 and 2 comprise 18 of 27 classes — they are not
rare corners. A bench that cannot produce them is **mis-specified, not
unlucky**, and §7.4 channel provisioning should be checked rather than the
run repeated.

---

## 4. Frozen decision rule

```
Gate A violated         → the corresponding family REJECTED:
                            A1 → all five frozen laws
                            A2 → the memoryless response class
                            A3 → §4.8 monotonicity; reopen 4 excluded maps
Gate B unmet            → NO-SCORE  (explicitly NOT a model tie)
Gate A passed, B met    → proceed to §7.5 exact-endpoint survival scoring,
                          unchanged
```

A tie among `R₀, R₂, R₁` with Gate B unmet is a **sampling artifact** and
must not be reported as a model-resolution result. Invalidation remains
outcome-independent and append-only per §7.28.

---

## 5. §7.6 compliance statement

This amendment introduces **no new response law** and **no reformulation of
closure economy**. It supplies:

1. a coordinate system for the already-frozen receipt data (Lemmas 1–2);
2. null-prediction gates on assumptions the frozen family already makes;
3. an acquisition-coverage constraint on the already-frozen sidecar.

It is therefore protocol-side and should not require §7.6 frontier re-entry.
**This is submitted as a judgement for the custodian to confirm, not
assumed.**

---

## 6. What this does not claim

`V`, `X`, and the 27-class coordinates are dimensionless internal receipts.
No physical identification is made. The amendment does not derive a
constitutive response law and does not narrow the §8.3 highest open problem.
It reduces the probability that a valid run returns an uninformative tie, and
raises the probability that a wrong shared assumption is caught.

Physical promotion remains 0.
