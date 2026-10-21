# Reset-Gap Reanalysis — Bounded-Agent Cycle Structure

## Status: RESOLVED

---

## Part 1: What Died, What Survived

### Dead

- **Universal 7-cycle attractor**: k=7 ranks 5th overall. Wins 1/10 environments.
- **c/7/week as physics**: Type III (invalid map) + Type IV (observer-relative). Closed.
- **"Bounded agents rediscover 7"**: Falsified across 10 environments, 38 cycle structures, ~300 trials each.
- **Reset-gap grammar as unified invariant**: Not confirmed. No single dimensionless variable predicts across all environments.
- **Nested reset architecture**: Falsified. Simple (k−1)+1 cycles beat all compound and nested structures 10/10.

### Survived

- **Two-regime structure**: Decay-dominated (Class I) and accumulation-dominated (Class II) environments have different optimal cycles and different control variables.
- **Short cycles dominate Class I**: k=2–4 win when information decays, saturates, or must be refreshed frequently. Predictor: max work streak.
- **Long cycles dominate Class II**: k=7–15 win when value accumulates and resets are costly. Predictor: work ratio.
- **k=7 wins exactly once**: B_compound (fast error compounding, rate 0.2/step). It is the error-overflow boundary for that specific rate. At rate 0.08, k=12 wins. At rate 0.3+, k=5 wins.

---

## Part 2: The Dimensionless Variables

Within-environment correlations with score:

| Environment class | Best predictor | Correlation | Meaning |
|---|---|---|---|
| Class I (decay) | max_work_streak | r = −0.87 to −0.95 | Shorter streaks → better |
| Class II (accumulation) | work_ratio | r = +0.86 to +0.999 | More work slots → better |

These are *different* control variables. There is no unified "reset density" or "gap cadence" that governs both classes. The two regimes have genuinely different physics.

### Variables tested

| Variable | Global r | Within-Class I | Within-Class II | Verdict |
|---|---|---|---|---|
| reset_density | −0.034 | ~+0.6 | ~−0.99 | Sign flips between classes |
| period | −0.055 | ~−0.6 | ~+0.9 | Sign flips between classes |
| max_work_streak | −0.057 | ~−0.92 | ~+0.75 | Strong in Class I only |
| work_ratio | — | ~−0.6 | ~+0.96 | Strong in Class II only |
| gap_cadence | — | ~−0.8 | ~+0.8 | Moderate in both, not best in either |

The global correlations are near zero because pooling across regimes averages out opposite-signed effects.

---

## Part 3: The Fractal-Reset Hypothesis

### Tested

"Does nested reset architecture (micro-resets inside macro-resets) explain performance better than raw cycle length?"

### Result: **Falsified.**

Raw k-cycles won 10/10 environments. Neither buildup+reset (b+r) patterns nor nested structures (e.g., 3+1 inside 12+1) ever beat the simplest (k−1)+1 pattern. Complexity did not help.

This means the "fractal unfolds from reset" idea — at least in the form of literal nested reset slots — does not describe the simulation landscape. The optimal structure is always a flat cycle, not a hierarchical one.

### Why nested loses

Each reset slot costs productivity (0.5 units in our model). Micro-resets inside a macro cycle add cost without proportional benefit, because the macro reset already clears the state. The information-theoretic gain from partial mid-cycle resets is always dominated by the cost of the wasted slot.

---

## Part 4: Mutation Map

| Environment | Best k | Class | 7 in top 5? | Stable feature |
|---|---:|---|---|---|
| A_decay | 3 | I | no | short refresh, fast decay |
| A_slow | 3 | I | no | short refresh, slow decay |
| B_compound | **7** | II | **WIN** | max work before error overflow |
| B_slow_err | 12 | II | no | long buildup, slow compounding |
| C_coord | 12 | II | no | long buildup, drift-tolerant |
| C_slow_drift | 15 | II | no | max work, minimal sync cost |
| D_saturate | 2 | I | no | immediate refresh, saturation |
| D_slow_sat | 4 | I | no | short buildup, slow saturation |
| E_slot | 4 | I | no | short refresh, slot structure |
| E_slow_slot | 3 | I | no | short refresh, slow slot decay |

---

## Part 5: What k=7 Actually Is

k=7 is the error-overflow boundary for compounding rate ≈ 0.2/step.

With 6 work slots: accumulated error ≈ 2.4 (safe).
With 7 work slots: accumulated error ≈ 3.0 (at the edge).
With 8 work slots: accumulated error ≈ 3.7 (degraded).

The extra work slot from k=7 vs k=6 adds enough productive value to offset the higher error, but k=8 tips over. This is specific to the compounding rate. Change the rate and 7 disappears.

---

## Part 6: Verdict

**"Reset-gap grammar is NOT the true invariant. The true invariant is regime-dependent cycle tuning."**

Two regimes, two control variables:

| Regime | What dominates | Optimal strategy | Control variable |
|---|---|---|---|
| Class I (decay) | Information loss between resets | Reset frequently | max_work_streak |
| Class II (accumulation) | Value growth between resets | Reset rarely | work_ratio |

The *boundary* between these regimes — the point where the cost of losing information equals the cost of wasting a reset slot — is the structurally meaningful object. Not 7. Not any specific integer. The crossover point.

k=7 happens to sit at that crossover for one specific error-compounding rate. It is a contingent realization of a regime boundary, not a universal attractor and not a fractal grammar.

### On the number 7

| Claim | Status |
|---|---|
| Universal attractor | Dead |
| Fractal reset grammar | Falsified |
| Local optimum | Yes, exactly 1 environment |
| Regime boundary marker | Yes, for compounding rate ≈ 0.2 |
| Structurally distinguished | No more than 6 or 8 |
