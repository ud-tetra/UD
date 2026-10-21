# Regime Boundary Condition Packet v1.0

## Status: DERIVED / OPEN FOR REFINEMENT

---

## The Core Object

A bounded agent with cycle length T, pattern (T−1) work + 1 reset.

Per-tick performance:

    J(T) = [V(T) − ρ] / T

where V(T) = total value from T−1 work slots, ρ = reset cost.

Two loss mechanisms compete:

- **Decay** (η per tick): value of later work slots degrades.
- **Compounding** (β per tick): accumulated error grows and penalizes.

---

## Class I: Decay-Dominated

Value per tick t: v(t) = η^t. Total value: V(T) = (1−η^{T−1})/(1−η).

Optimal T satisfies:

    η^{T*} · (1 + T*·ln(1/η)) ≈ 1 − ρ(1−η)

Scaling: **T\* ≈ 1/(1−η)** when ρ ≈ 1.

| η | T\* | Interpretation |
|---|---|---|
| 0.50 | 4 | Very fast decay → reset every 4 |
| 0.70 | 5 | Fast decay |
| 0.85 | 6 | Moderate decay |
| 0.95 | 10 | Slow decay |
| 0.99 | 21 | Very slow decay → long cycles |

**Control variable**: max\_work\_streak. The T-th work slot produces η^{T−1}. Adding it is worthwhile only if η^{T−1} > ρ/T. Beyond that, every additional slot wastes capacity. Score correlates r ≈ −0.92 with max streak.

---

## Class II: Accumulation-Dominated

Error per tick: e(t+1) = (1+β)·e(t) + α. Value degrades as v₀ − κ·e(t).

Most work slots produce ≈ v₀ (error is small early in cycle). The binding constraint is the *last* few slots where error has compounded.

Total value ≈ v₀·(T−1) − correction. Per tick ≈ v₀·(T−1)/T = v₀ × work\_ratio.

Optimal T satisfies:

    (1+β)^{T*} · [1 − T*·ln(1+β)] ≈ 1 + ρβ/(κα)

Scaling: T\* grows as β shrinks.

| β | T\* | Interpretation |
|---|---|---|
| 0.50 | 9 | Fast compounding → moderate cycles |
| 0.20 | 13 | Moderate compounding |
| 0.10 | 16 | Slow compounding |
| 0.02 | 22 | Very slow → long cycles |
| 0.00 | 25+ | No compounding → maximize work ratio |

**Control variable**: work\_ratio = (T−1)/T. Score correlates r ≈ +0.96 with work ratio.

---

## The Crossover

**Dimensionless crossover parameter:**

    Φ = ln(1/η) / ln(1+β) = (decay rate) / (compounding rate)

| Φ range | Regime | Optimal T\* | Governing variable |
|---|---|---|---|
| Φ ≫ 1 | Class I | Short (2–5) | max\_work\_streak |
| Φ ≈ 1 | Boundary | Intermediate (6–8) | mixed |
| Φ ≪ 1 | Class II | Long (10–25) | work\_ratio |

When an environment has **both** decay and compounding, the regime is determined by which rate dominates. The crossover Φ ≈ 1 is where the marginal cost of one more work slot from decay equals the marginal cost from error accumulation.

**Boundary character**: model-dependent. In the exponential-decay × linear-compounding family, the transition is gradual (T\* changes by 1 per ~0.3 change in Φ). Not a sharp phase transition — a smooth crossover.

---

## Why Global Correlations Cancel (Simpson's Paradox)

| Variable | Class I correlation | Class II correlation | Pooled |
|---|---|---|---|
| work\_ratio | −0.6 | +0.96 | ≈ 0 |
| max\_streak | −0.92 | +0.75 | ≈ 0 |
| reset\_density | +0.6 | −0.99 | ≈ 0 |

Opposite-signed within-class effects average to zero when pooled. Any analysis that does not first classify the environment into Class I vs Class II will find no predictive signal. This is why the global sweep in the reset-gap reanalysis showed r ≈ −0.03 to −0.06.

**The correct procedure**: measure Φ → classify regime → apply regime-specific predictor.

---

## Falsification Conditions

The two-regime law would be falsified by:

1. **Simultaneous positive correlation** of score with both max\_streak and work\_ratio in the same environment. (Currently they are always opposite-signed or decorrelated.)

2. **Non-monotonic crossover**: optimal T\* jumps discontinuously as Φ crosses 1, rather than transitioning smoothly.

3. **Nested/compound cycle beats simple cycle** in any environment. (Currently falsified 10/10.)

4. **Third regime** with a control variable that is neither max\_streak nor work\_ratio.

5. **Φ fails to predict** in environments with non-exponential decay or non-linear compounding. (Φ is model-family specific; the two-regime structure may persist under different Φ definitions.)

---

## Plain-Language Interpretation

Every bounded agent faces a tension: reset too often and you waste time on overhead; reset too rarely and accumulated damage degrades your work.

If your main problem is **forgetting** (information decays while you work), you need short cycles. The question is: "how many work slots still produce good output before quality collapses?" That's max\_work\_streak.

If your main problem is **error buildup** (mistakes compound but early work is productive), you need long cycles. The question is: "what fraction of my time is actual production?" That's work\_ratio.

The boundary between these regimes is where the rate of forgetting equals the rate of error compounding. On one side, reset often. On the other, reset rarely. The exact cycle length depends on the specific rates — no integer is universally privileged.

---

## What This Packet Does Not Contain

- Any claim about the number 7.
- Any connection to calendar units.
- Any numerological structure.
- Any assumption about human biology.

The crossover condition Φ = ln(1/η)/ln(1+β) is a property of the agent-environment interaction, not of any specific integer, time unit, or cultural convention.
