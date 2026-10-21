# Amendment Addendum v0.3 (append-only)

Corrects two errors in v0.2 and adds the action/clock audit.
**Physical promotion: 0.**

---

## C.1 RETRACTION — v0.2 §A.7 precision claim was wrong

v0.2 stated: *"The binary discriminator is not precision-limited; the family
falsifier is. If the §7.29 uncertainty budget is set by PLB1-vs-HCB1
separation, it is set by the wrong target."*

**This was wrong.** The quoted table used single-triple statistics and ignored
the 12-runs-per-class averaging already frozen in §7.28.

Correct budget, null = HCB1/WBQ1 (`ε = (1,3,5)·A`, `D₂ = 0`):

| n/class | per-run r | σ(D₂)/A | 3σ threshold \|D₂/A\| | min detectable κ |
|---|---|---|---|---|
| 12 | 20% | 0.455 | 1.364 | 0.54 |
| **12** | **10%** | **0.227** | **0.682** | **0.30** |
| 12 | 5% | 0.114 | 0.341 | 0.16 |
| 24 | 10% | 0.161 | 0.482 | 0.22 |
| 36 | 10% | 0.131 | 0.394 | 0.18 |

At the existing §7.29 baseline (n = 12, r = 10%), D₂ already detects
autocatalysis down to **κ ≈ 0.3** at 3σ. **No thermometry re-spec is
required.** The binding constraint is **acquisition count** — obtaining a
third event class — not per-run precision.

## C.2 CORRECTION — v0.2 §B.1 F2 was not executable as stated

v0.2 stated F2 as: *"Two events with identical (ω, G) must yield identical θ⁺."*

`G_p = Σ_{e∈M_p} T_e Λ_e^S` is **continuous-valued**. Exact coincidence
between two events has measure zero, so F2 as written can never fire.

**Fix.** All five frozen laws depend on `G` only through `1[G_p > 0]`. The
response-relevant state is therefore the discrete pair

```
(ω_p , g_p),   g_p = 1[G_p > 0]
```

with `ω_p ≤ g_p` **forced, not assumed**:
`ω_p = 1 ⟹ T_p = 1 ∧ R_p > 0 ⟹ ∃e: T_e Λ_e^S > 0 ⟹ G_p > 0`.

Per pair the reachable states are `{(0,0), (0,1), (1,1)}` → 3 options →
**27 discrete response classes** over three pairs.

**F2 restated (executable):** two events falling in the same one of the 27
classes must yield identical `θ⁺`. A within-class disagreement falsifies the
entire memoryless response class — including laws not yet enumerated.

Feasibility: N events over 27 classes give ≈ N(N−1)/54 same-class pairs under
uniform occupancy (~10 usable pairs at N = 24; more under realistic
non-uniform occupancy). F2 is executable after restatement.

## C.3 Scorer integration — keep D₂ outside the AICc comparison

```
current : 24 runs, 2 models × 1 param, dof 23
amended : 36 runs, dof 35 (1-param) / 34 (WBX1, 2-param)
AICc small-sample correction at n=36: +0.118 (k=1), +0.364 (k=2)
⟹ the |ΔAICc| ≥ 10 threshold transfers without re-derivation
```

**Recommendation:** run D₂ as a **separate pre-fit validity gate (Tier 1)**,
not as a third model inside the AICc comparison. `D₂ = 0` is a prediction
*shared* by both frozen models, so it tests their common assumption rather
than discriminating between them. Folding it into AICc would conflate model
validity with model selection.

## C.4 Action/clock audit (§7.7, §5.3) — verified

Independently checked against the canonical v2.40 source:

```
J = A/2,  J² = −P₂ globally                          ✓
active sector dim = 14, J² = −I restricted there     ✓
A³ + 4A = 0                                          ✓
α_A = A₀/2 via I_Hodge route                         ✓ (identity)
α_A = A₀/2 via (H=a, E=(A₀/τ₀)a, rate 2/τ₀) route    ✓ (agrees)
one recurrence: Δφ̃=2π, a=1 ⟹ S = πA₀                ✓
```

`η_A = A₀/ħ = 2` is arithmetically exact and self-consistent, but it is a
**consequence of the QPB-1 bridge postulate**, not a derivation. §7.7 says so
explicitly. `A₀` is unanchored, so `η_A` is currently **untestable** — it
becomes a prediction only once `A₀` is fixed without using quantum-action
targets.

Clock scoping (§5.3) verified: the single filled `K₄` cell has all nonzero
frequencies equal to 2, hence exact period π. On the glued A/B/C relay the
spectra are `√3, √5` and `√2, √5`; since `√(5/3)` and `√(5/2)` are irrational
there is no finite `T` with `e^{TA} = I`. **The clock is a single-cell-only
property and gluing destroys it.** The manuscript scopes this correctly.

## C.5 Not audited

The **Δ⁴ cochain prototype** advertised on the landing page as the current
"action/clock update" is **not present in the canonical v2.40 source** and is
not publicly indexed. It could not be verified. Any claim resting on it is
outside this audit.
