# Write faults and a common deadline

2026-10-13. Benjamin Walker Mayes, AI-assisted development. Development — no registry entry. Physical promotion 0; independent review OPEN.

## Result and declared scope

The next best step tests the retention comparison against two previously idealized choices: unequal write latency and faultless gate execution. Ground encoding still retains substantially more information on the same boundary at a common deadline. However, its nominal one-percent-error margin is narrow and places a strict requirement on the initial carrier-to-seed operation.

The clocks and error probabilities below are declared test inputs, not empirical rates or native UD predictions. The fault environment's energy and control costs are not derived, so earlier ideal cost thresholds are not silently applied to noisy gates. G05/G06 and the native recording source remain open. G is unused.

## 1. Common deadline rather than equal post-write exposure

Define one complete write-gate round and one complete thermal collision/refresh round to take one slot each. This equal-duration choice is a candidate clock ratio, not a physical calibration. Isolate the memory from its storage bath during writing, as in the prior local protocol.

At a deadline of 44 slots from the beginning of writing, one-hot finishes its one-gate write and then undergoes 43 storage updates. Ground fanout finishes its twelve-gate write and then undergoes 32 storage updates. Both occupy A=12a0.

| Ideal common-deadline result | One-hot | Ground |
|---|---:|---:|
| Write slots | 1 | 12 |
| Storage updates | 43 | 32 |
| Optimal readout error | 0.43482158 | 0.00923883 |
| Retained information, nats | 0.01666994 | 0.66761023 |
| Information density | 0.00138916/a0 | 0.05563419/a0 |
| Fresh bath qubits in the specified stream | 86 | 64 |
| Fresh uniform site-control cells | 43 | 32 |

The clock cost is explicit. Ground is thermally isolated longer during its write, which is part of this protocol, not an unqualified encoding advantage. If bath leakage during the write is allowed, or gate durations differ, a different kernel and deadline must be evaluated.

The replay independently propagates the one-hot state through 43 updates; it does not extrapolate the earlier 32-update result. Exact rational probabilities are stored, with logarithmic quantities displayed as floating values.

## 2. Exact seed bottleneck

Let R be the original fair carrier label and let the written seed be

\[
S=R\mathbin{\mathrm{XOR}}E_s,\qquad E_s\sim\mathrm{Bernoulli}(p_s),\quad0\le p_s\le1/2.
\]

After this initial operation all fanout, thermalization and memory readout act downstream of S. Let p_0 and p_1 be the final memory distributions conditional on a correct seed value. Then the distributions conditional on the original R are

\[
\tilde p_0=(1-p_s)p_0+p_sp_1,\qquad
\tilde p_1=p_sp_0+(1-p_s)p_1.
\]

Their difference is (1−2p_s)(p_0−p_1). Hence the full-memory trace distance and optimal equal-prior error obey exactly

\[
\boxed{D(p_s)=(1-2p_s)D(0),\quad
e(p_s)=p_s+(1-2p_s)e(0).}
\]

In particular e>=p_s. Also R→S→M is a Markov chain, so I(R:M)<=ln2−h(p_s). Subsequent copies cannot correct an incorrect source seed because they contain no independently acquired information about R.

With perfect fanout and 32 ground storage updates, e0 is the previous exact rational error. To meet the declared final-error criterion epsilon=1/100,

\[
p_s\le\frac{\epsilon-e_0}{1-2e_0}
\approx0.000775497742.
\]

The inequality is exact with the replay's rational e0; the decimal is display only. A seed error of 1/1000 already violates the criterion, yielding final error approximately 0.01022035. The earlier perfect-write pass is therefore conditional on a much better source write than one-percent or one-per-thousand errors.

## 3. Independent fanout errors and the entropy distinction

Declare an independent target-bit XOR error after each of the eleven memory CNOTs, before the target bonds are restored, with probability q. The seed bit is untouched by those eleven faults. In the tree encoding, each child-parent parity equals its own gate error. Thus the eleven independent error bits are in bijection with the resulting word at a fixed seed value.

Consequently, immediately after fanout,

\[
H(M\mid S)=11h(q),\quad
H(M)=\ln2+11h(q),\quad
I(R:M)=\ln2-h(p_s).
\]

The original label is accessed through the seed bit, so extra fanout randomness does not increase source information. It does increase marginal memory entropy. Counting that increase as additional record formation would count control noise as physical evidence about the carrier.

The noisy initial words are propagated through the same finite thermal kernel using exact integer probability weights. Global complement symmetry relates the distributions for S=0 and S=1. The checker verifies the fanout conditional entropy formula, the seed-error law, and exact criterion comparisons.

| Ground encoding, 32 storage updates | Seed error p_s | Fanout target error q | Final optimal error | Retained information, nats |
|---|---:|---:|---:|---:|
| Ideal | 0 | 0 | 0.00923883 | 0.66761023 |
| Seed stress | 1/1000 | 0 | 0.01022035 | 0.66071146 |
| Fanout stress | 0 | 1/100 | 0.01832168 | 0.64062030 |
| Larger fanout stress | 0 | 1/20 | 0.05786802 | 0.53769125 |
| Feasible declared budget | 1/10000 | 1/2000 | 0.00978596 | 0.66541124 |

The last row passes the one-percent criterion by exact rational comparison. It is a conditional gate-quality budget, not a measured performance claim. Non-independent or correlated faults require a new joint law.

## 4. A source-redundancy candidate, distinguished from copying

The mathematical bottleneck suggests three independently acquired seed receipts rather than a larger fanout of one receipt. Under an explicitly independent binary-error model with single-receipt error p, majority error is

\[
p_3=3p^2-2p^3.
\]

Enumerating the eight fault patterns gives, for p=1/1000, p3=1499/500000000; for p=1/100, p3=149/500000. Both are below the perfect-fanout seed ceiling above. This could make source acquisition more robust without pretending downstream copies add evidence.

This is a separate candidate source protocol, not an implemented part of the present retention replay. It needs a carrier hold/readout rule, genuinely independent receipt errors, a reversible majority/control circuit, additional time and apparatus resources, and a revised common deadline. Perfectly correlated receipt errors would give p3=p and remove the advantage. Its energy cost cannot be inferred from the binomial polynomial.

## 5. Cost and closure boundary

The common-deadline comparison changes thermal stream consumption: one-hot needs 43 collision/refresh rounds while ground needs 32. Gate noise additionally introduces an unspecified environment that stores error flags and may exchange work or heat. The marginal entropy 11h(q) is not evidence that its energetic cost is free, nor that every noisy operation dissipates kBT times that entropy. A Hamiltonian/resource model is required.

Therefore ideal write–store–reset cost laws from the previous release remain scoped to their faultless write. They cannot be declared complete cost laws for the noisy cases. This release closes exact information/error propagation under a declared noise channel and clock ratio, not autonomous apparatus cost or physical source calibration.

CHECKED: common deadline; exact seed error floor; fanout entropy; correlated finite-memory propagation; feasible declared error budget; independent three-receipt majority polynomial.

OPEN: native source write, independence of actual receipts, energetic fault model, gate-time calibration, thermal leakage during writing, controller/readout/reset costs, extensive logical density, refinement and horizon map. No registry, ledger, site or repository changes. Physical promotion 0; independent review OPEN. Gap2_FINAL_Finite_Genesis.png was unavailable and unused.

Next best mathematical source task: construct the independent source-receipt/majority interaction and include its latency and resource state. The immediate bottleneck is fidelity of carrier acquisition, not the number of downstream copies.
