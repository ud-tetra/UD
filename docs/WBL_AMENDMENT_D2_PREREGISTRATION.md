# Proposed Amendment — Winding-Burden Discriminator

**Target sections:** §7.22 (frozen discriminator), §7.29 (protocol freeze)
**Status:** PRE-DATA PRE-REGISTRATION DRAFT
**Physical promotion:** 0 (unchanged — this amends a protocol, not a claim)
**Constraint:** must be frozen before any hardware run to retain falsifying power

---

## 1. Motivation

The current discriminator resolves WBL1 vs WBQ1 via the two-slip ratio

```
R_B = ε₁ / ε₀       WBL1 → 1,  WBQ1 → 3
```

Two deficiencies are identified:

**(a) R_B cannot validate the receipt-linear family itself.** Any law affine in the verified receipts `(I, T, B_k) = (1/4, 3/4, k/2)` is necessarily affine in `k`, since `I` and `T` are `k`-independent and `B_k` is linear in `k`. A measured `R_B` between 1 and 3 is currently read as inconclusive when it in fact denotes a specific intermediate law.

**(b) R_B is degenerate against burden-dependent formation.** See §3 below. `R_B = 3` is satisfied by WBQ1 *and* by a purely autocatalytic law. The current protocol cannot separate them.

---

## 2. The receipt-linear family is a line, not two points

With the verified receipts, any receipt-linear cost is

```
ε_k = A + Ck          f_W(n) = An + (C/2)·n(n−1)
```

- `C = 0`   → WBL1, `f_W(n) = An`
- `C = 2A`  → WBQ1, `f_W(n) = An²`
- otherwise → an unnamed intermediate law

Therefore `R_B = 1 + C/A`, i.e. **R_B is a continuous readout of `C/A`, not a binary flag.** Amendment: report `C/A = R_B − 1` as a measured quantity with uncertainty, rather than a WBL1/WBQ1 verdict.

---

## 3. New pre-registered candidate: WBX1 (burden-dependent)

Every candidate in §7.14–7.22 makes `ε_k` a function of winding number only. None permits dependence on the burden **already stored** at the site. Define:

```
WBX1:   ε_k = A + Ck + κ · f_W(k)
        f_W(n) = Σ_{k<n} ε_k ,  f_W(0) = 0
```

Self-referential, hence a recursion rather than a closed sum:

```
f_W(n) = (1+κ)·f_W(n−1) + A + C(n−1)
```

This grows geometrically in `n` rather than polynomially — a qualitatively distinct functional form. `κ = 0` recovers the receipt-linear family exactly, so WBX1 is a strict one-parameter extension, not a replacement.

**Open dependency:** if the additive source law `Δρ = B J_B + s_B` (§7.24) is fixed upstream in the v1.9 base with `s_B` required independent of `ρ⁻`, WBX1 is excluded *for that stated reason* and this section should record the exclusion rather than the candidate. This must be resolved from the v1.9 source before freeze.

---

## 4. The degeneracy (why the amendment matters)

Writing `c = C/A`:

```
R_B  = 1 + c + κ            ← c and κ enter ONLY as the sum
D₂/A = κ(c + κ)             ← breaks the degeneracy
```

where `D₂ ≡ ε₂ − 2ε₁ + ε₀`.

| law | c | κ | R_B | D₂/A | ε₃/A |
|---|---|---|---|---|---|
| WBL1 linear | 0 | 0 | 1 | 0 | 1 |
| WBQ1 quadratic | 2 | 0 | **3** | **0** | **7** |
| WBX1 pure autocatalytic | 0 | 2 | **3** | **4** | **27** |
| WBX1 mixed | 1 | 1 | 3 | 2 | 15 |
| WBX1 weak | 2 | 0.5 | 3.5 | 1.25 | 12.9 |

Rows 2 and 3 are **indistinguishable under the current protocol** and differ by a factor of ~4 in `ε₃`. This is the concrete gap the amendment closes.

---

## 5. Amended measurement set

```
Slips required:  0→1, 1→2, 2→3, (3→4)     same site, consecutive
Observables:     ε₀, ε₁, ε₂, (ε₃)
```

**Tier 1 — family validity (parameter-free).**
`D₂ = ε₂ − 2ε₁ + ε₀`. Predicted **exactly zero** for every receipt-linear law, for all `(A,C)`. A significant nonzero `D₂` falsifies WBL1, WBQ1, and every intermediate law simultaneously.

**Tier 2 — parameter extraction.**
```
s = R_B − 1 ;    κ = (D₂/A)/s ;    c = s − κ
```
Three slips determine `(A, c, κ)` exactly.

**Tier 3 — out-of-sample falsification (optional 4th slip).**
With `(A,c,κ)` fixed by Tier 2, `ε₃` is fully predicted with no remaining freedom:
```
ε₃/A = (1+κ)³ + c(κ² + 3κ + 3)
```
Measuring `ε₃` is a genuine out-of-sample test of the entire extended family.

---

## 6. Frozen decision rule

```
D₂ consistent with 0  →  receipt-linear family retained;
                          report C/A = R_B − 1 with uncertainty.
D₂ significantly ≠ 0  →  receipt-linear family REJECTED;
                          report κ, c per Tier 2; WBX1 candidate.
Tier 3 disagrees      →  extended family REJECTED; return to
                          source-law construction (§7.24).
```

No post-hoc selection among `(c, κ)` is permitted; both are outputs, not fitted choices.

---

## 7. Precision requirements

Per-slip relative calorimetry error `σ`:

| σ | WBL1 vs WBQ1 separation | D₂ curvature detectable at 3σ |
|---|---|---|
| 20% | ~3.5σ | \|D₂/A\| > 1.5 |
| 10% | ~7σ | \|D₂/A\| > 0.73 |
| 5% | ~14σ | \|D₂/A\| > 0.37 |
| 2% | — | \|D₂/A\| > 0.15 |

The binary discriminator is not precision-limited. **The family falsifier is** — and it is the more valuable measurement. Precision budget should be set by Tier 1, not Tier 2.

---

## 8. Cost

One additional slip on existing hardware (two for Tier 3). No new apparatus. Converts a model-*selection* test into a model-*validity* test.

---

## 9. What this does not claim

No physical identification of `ε_k`, `A`, `C`, or `κ` with any measured energy scale. `D₂` and `R_B` are dimensionless internal ratios; their promotion to calorimetric observables depends entirely on the §7.26 bridge, which remains a stated CRL-2 assumption. Physical promotion remains 0.
