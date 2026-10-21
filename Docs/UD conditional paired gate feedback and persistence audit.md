The retrieved conditional pair-swap rule can select a gate change from a nonzero prepared burden state. With a one-sample history window, every positive-gain swap reduces memory of that current contrast under the resulting fixed gate operator. A finite feedback replay also shows continuing gate changes while the burden approaches uniformity. These results separate changing gate organization from persistence of a nonuniform burden pattern.

History changes the conclusion: an explicit supplied two-sample history produces a positive window-score gain while increasing memory of the current pattern. The rule therefore cannot be classified as universally persistence-seeking or universally dispersive without specifying its history window and state trajectory.

Claim bin: CANDIDATE_DEVELOPMENT_MATHEMATICS. Correspondence: NOT_PROPOSED. Physical promotion: 0. Independent review: PENDING. This is append-only development, not promotion of an autonomous primitive runtime.

## Source and declared scope

UD_Tetrahedral_Packet_Complex_JPhysA.tex defines the pre-gate quadratic burden pair scores as sums of squared edge gradients across a declared history window. On vertices 0,1,2,3, the opposite pairs are:

| Pair | Edges |
| --- | --- |
| A | 01 and 23 |
| B | 02 and 13 |
| C | 03 and 12 |

For each pair, W is the sum of squared burden differences on its two edges, accumulated over the declared samples. The conditional rule closes the unique minimum-score open pair and reopens the unique maximum-score closed pair when the gain is strictly positive and selected integrity gates pass. It preserves Hamming weight. Ties and nonpositive gains produce no event.

This replay supplies nonnegative burden, an existing paired closure state, passing selected integrity gates, and a history window. It does not form the burden, create the first closed pair, generate transport integrity, choose the history window, or derive a native event clock. The gate response is state-selected within those declared premises.

The burden propagator uses Q162's source-free generator L=B diag(h) B transpose /4. This is its dimensionless source clock, not the distinct 1/3 neighbor clock or a physical time constant.

## Exact one-sample witness

Use burden b=(0,1,2,4), total stock 7, and Theta=(0,0,1), so pair C is initially closed. The pair scores are (5,13,17). The rule closes A, reopens C, and selects Theta=(1,0,0). The score increases from 9/2 to 15/2, a gain of 3.

The mean is 7/4 and the squared contrast norm N is 35/4. Every one-closed-pair K4 has contrast rates 1/2, 1/2, and 1. Let z=exp(-s/2). The normalized contrast memories under frozen before and after gates are:

```text
Mbefore = (34/35) z + (1/35) z squared
Mafter  = (2/7) z + (5/7) z squared
Mbefore - Mafter = (24/35)(z - z squared) > 0 for finite s>0.
```

Integrated memory falls from 69/35 to 9/7. The burden and its norm are identical at the instant of the gate comparison; only the gate operator changes.

## General singleton-window result

For a nonuniform prepared burden, let x=b-mean(b) and N=norm(x) squared. For Hamming weight one, the slow spectral weight is Wclosed/(2N); the remaining weight has rate 1. A positive-gain swap reduces that slow weight by 2 gain/N. Therefore it strictly reduces the normalized contrast memory for every finite positive s.

For Hamming weight two, one matching is open. Its rate-1/2 weight is Wopen/(2N), and the remaining weight is stationary because the matching graph is disconnected. A positive-gain swap increases the decaying weight and reduces stationary memory by 2 gain/N. Again, normalized memory is strictly lower at every finite positive s. Both integrals may remain infinite when stationary weight persists; pointwise memory decrease does not imply two finite lifetime integrals.

With singleton scores, the gate score equals x transpose L x. The source-free contrast energy derivative is -2 times this score. The positive score gain therefore produces faster immediate relaxation of the same state. It is not a rule that maximizes memory of that state.

These are analytic finite-carrier statements. They do not generalize to an arbitrary history window, protected reversible modes, exchange with other carriers, or native clustering and shape formation.

## Exhaustive bounded controls

The replay covers all 625 nonnegative burden preparations in the grid {0,1,2,3,4} to the fourth power, each with all eight Theta states: 5000 cases.

| Outcome | Cases |
| --- | --- |
| Positive-gain swap | 1320 |
| No event because an open or closed class is absent | 1250 |
| No event because a required extremum is tied | 1350 |
| No event because gain is nonpositive | 1080 |

The swaps comprise 840 Hamming-one and 480 Hamming-two cases. No-event categories are replay outcomes for this conditional rule, not inferred native admission HOLD receipts. Counts are census results, not probabilities or independent experimental observations.

The verifier checks source score gains, preserved Hamming weight, exact spectral relations, the all-time memory-difference coefficient, selected integrity precondition rejection, and simultaneous vertex/matching relabeling covariance. Rational exponential coordinates supply additional exact fixtures; they are not fitted coefficients.

## Bounded feedback trace

At each of 24 externally sampled ticks, use the current burden as the singleton window, run the rule, then propagate with the selected gate. The main diagnostic uses z=1/2, corresponding to an external source-clock interval 2 log(2).

The exact propagator is:

```text
T = Pmean + z Pslow + z squared Pfast.
```

It preserves nonnegative burden and total stock, while the contrast norm strictly decreases at every step. State and gate continuity between successive trace receipts is checked explicitly.

The main trace makes 24 swaps. It uses closed-A, closed-B, and closed-C states 9, 8, and 7 times respectively. After 24 steps, squared contrast norm is exactly 77/295147905179352825856. The carrier remains one supplied K4 throughout; no cell growth or geometric embedding is performed.

Two additional external cadence controls also run for 24 ticks:

| Exponential coordinate z | Swap count | No-event count |
| --- | --- | --- |
| 1/4 | 24 | 0 |
| 1/2 | 24 | 0 |
| 3/4 | 23 | 1 |

The cadence changes event history, so these event counts cannot be assigned native timing significance.

For any sequence of Hamming-one gates on this fixed K4, every generator has contrast spectral gap 1/2 and conserves the same mean. Hence, over elapsed source clock s, contrast norm is at most exp(-s/2) times its initial norm. If elapsed clock grows without bound, every nonuniform contrast vanishes. Switching need not stop for the burden to approach uniformity. This proof does not require the three chosen sampling cadences, but it does require this connected, source-free mixer stratum.

The trace is a conditional state-to-gate-to-state feedback loop. First closure, burden origin, native window/cadence, full packet admission, and multi-cell synchronization remain outside it.

## Longer-history counterexample

Prepare two samples with the same total stock 14:

```text
Older burden:   (0,8,2,4)
Current burden: (7/4,11/4,15/4,23/4)
```

The current burden differs from the singleton witness only by a uniform shift, so its contrast and instantaneous scores remain unchanged. Take Theta=(1,0,0), with A closed.

The two-sample accumulated pair scores are (73,33,69). The source rule closes B, reopens A, and selects Theta=(0,1,0). Window score gain is +10, while the current-state score gain is -2.

The current slow memory weight rises by 16/35. Consequently:

```text
Mafter(current,s) - Mbefore(current,s)
  = (16/35)(exp(-s/2) - exp(-s)) > 0 for finite s>0.
```

Thus optimizing the accumulated source score need not optimize current relaxation or current persistence in the same direction. This is a prepared-history counterexample, not a certified native trajectory between the two samples. Equal total stock does not certify dynamical reachability.

A native history-window law is a substantive missing dependency, not a harmless implementation detail. A longer source-certified feedback replay is needed before drawing a general conclusion about the rule's persistence preference.

## Stage evidence

| Stage | Evidence | Remaining gap |
| --- | --- | --- |
| Nonzero burden preparation | Exact nonnegative inputs | Source-owned formation |
| Gate decision | Conditional rule selects paired swaps | First closure and integrity generation |
| State propagation | Exact Q162 semigroup | Other coupled modes and physical clock |
| Feedback | 72 finite steps at three external cadences | Native sampling, window, and scheduler |
| Persistence comparison | Singleton theorem and longer-history counterexample | Certified multi-sample trajectories |
| Cluster or shape selection | No new result | Growth admission and topology update |

The present evidence does not select a cube, a regular tetrahedral assembly, a stopping size, or a physical object. It clarifies which objective a declared update actually optimizes and which inputs control its interpretation.

## Verification and source provenance

The standard-library replay performs 30331 exact assertions. It verifies 5000 source-rule cases, 1320 positive swaps, spectral identities and exact memory inequalities, vertex/matching covariance, 72 feedback propagation steps, inter-step continuity, cadence sensitivity, and the supplied two-sample counterexample.

Run python verify_pair_swap_feedback_v0_1.py. Results retain event counts, the explicit witness, all three bounded feedback traces, and the history counterexample. The source snapshots preserve the paper's pair gates, pair-event theorem, newly retrieved pre-gate history-score definition, and prior Q156/Q162 ledger/pipeline envelope. Source sections are retained at their observed versions; no canonical edit is made.

The analytical proofs support their stated scope beyond the finite grid, but assertion counts are not independent review or physical observations.

## Retained risks and next target

The accompanying risk register retains failed interpretations: increased source score means increased persistence; continuing gate swaps prove nonuniform burden survival; one-sample theorem applies to all windows; equal stock certifies a supplied history; chosen cadence is native time; a state-selected conditional update is a complete primitive runtime; one-cell feedback proves multi-cell synchronization; paired gating proves full coherent agreement; relaxation creates or finances burden; internal feedback selects physical geometry.

The next target should certify a longer history by generating every sample from the admitted Q162 propagation and the same paired-event rule. Compare source-window score, current memory, contrast energy, gate occupancy, and event timing together. Preserve the distinction between observer-selected sampling and a native scheduler, and keep formation and physical promotion open.
