# UD PRED-02 — Source-compatible 12-bit microstate lift and dual-control protocol, v0.4

**Date:** 2026-10-31  
**Lane:** D0 DEVELOPMENT / P0 candidate. **Physical promotion:** 0. **Non-constructor review:** deferred.

## 1. Source and types

Grounded source: `ud-tetra/UD/docs/UD_PREREGISTRATION_PACKET_v1.0.md` Part B §§B.1–B.3 and D (blob `c5ddbb6f4df4ba3ff5c6b39895b58c6e955fc82b`), with mandatory `docs/UD_PACKET_v1.1_ERRATA.md` §E.3 (blob `6961b917f4f1ca470127aa0b7d3c1b59693f4373`); prior formal schedules in UD PR #477. The source requires \(\omega_p\le g_p\), with \((\omega_p,g_p)\in\{(0,0),(0,1),(1,1)\}\), a 27-class three-pair alphabet, one of each shell \(w_H(\omega)\in\{0,1,2\}\), and at least one partial-integrity \((0,1)\) event. The source counts four of 16 edge configurations in the partial-integrity class but does not fix this addendum's entire Boolean encoding.

Define **new candidate binary interface per pair**:

\[
 x_p=(T_a,T_b,L_a,L_b)\in\{0,1\}^4,
 \quad g_p=(T_aL_a)\lor(T_bL_b),
 \quad\omega_p=T_aT_b(L_a\lor L_b).
\]

Interpret \(T_a,T_b\) as respective edge-integrity flags, \(L_a,L_b\) as latent-support-presence flags; the multiplication denotes Boolean AND, \(\lor\) is OR. This *source-compatible realization* instantiates the stated order and four partial cases. It is **not** proved to equal the original primitive UD edge transport/latent mechanism, and raw support could require additional real-valued thresholds in an eventual apparatus.

## 2. Exact 16-state result and three-pair lift

Enumerating all 16 raw configurations gives:

| \((\omega,g)\) | Raw configurations | Meaning in this assumed Boolean lift |
|---|---:|---|
| (0,0) | 9 | No intact supported edge |
| (0,1) | 4 | At least one intact supported edge, but not both integrity flags |
| (1,1) | 3 | Both edges intact and at least one supported |

The forbidden state (1,0) has zero representatives, so \(\omega\le g\) is exact. Three independent pair interfaces have **12 raw input bits**, \(16^3=4096\) raw configurations, and all \(3^3=27\) response classes. The class multiplicity is the product of 9, 4 and 3 from its pair labels, ranging from \(3^3=27\) to \(9^3=729\). Full enumeration and an independent standalone check match.

If raw 12-bit configurations are selected **independently and uniformly**, class probabilities are not uniform. With \(p=(9/16,4/16,3/16)\),

\[
 \boxed{\Pr(\text{same class on two raw draws})=\left(\frac{53}{128}\right)^3
 =\frac{148877}{2097152}},
\]
\[
 \boxed{\mathbb E[M\mid N=24]\;=\binom{24}{2}\left(\frac{53}{128}\right)^3
 =\frac{10272513}{524288}\approx19.59.}
\]

This exceeds the uniform-class expectation \(92/9\), but **more expected collisions do not guarantee source coverage**. At 24 iid uniform-raw draws, the probability of missing every shell-2 state is \((1-351/4096)^{24}\), approximately 11.6%. If sampling is not iid or the 12-bit interface is not truly independently controllable, neither expectation is applicable.

## 3. A formal 81-event design that separates hidden states from memory

The earlier v0.3 **54-event two-pass design** repeats each of the 27 formal class labels. But a class may contain 27–729 distinct raw configurations; a class-level replay mismatch is not necessarily temporal memory. It may reflect hidden raw inputs removed by coarse-graining. Therefore construct three passes:

- **A baseline:** one 12-bit canonical raw representative for each of the 27 classes.
- **B exact raw replay:** repeat the *identical 12-bit word* in each class (after time/order randomization); this tests fixed-microstate repeatability under controlled context.
- **C within-class challenge:** choose a different 12-bit word from the same 27-class equivalence class; this challenges whether the class label alone is a sufficient predictor.

This gives \(3\times27=81\) formal observations. Under the stated requirement of two identical-raw measurements plus a distinct raw representative **for every class**, 81 is minimal. Every class has at least 27 raw preimages, so the alternate representative exists in the Boolean model. The source's three shell gates and partial-integrity gate are covered in each pass. This is **not** a validated experimental schedule or a replacement for the source-frozen 24-run protocol.

### Counterexample to class-level memory identification

Take \(x_a=(0,0,0,0)\) and \(x_b=(0,0,1,0)\). Both map to \((\omega,g)=(0,0)\), yet the entirely **memoryless** raw-state response \(\theta^+(x)=L_a\) produces \(0\) and \(1\). Thus identical \((\omega,g)\) labels with different outputs can falsify **class sufficiency**, but do not alone prove temporal memory. Comparing A/B versus A/C separates these failure modes under controlled nuisance variation.

## 4. Critical output typing: q is not automatically theta-plus

The packet uses both gate vectors \(q\) and a viable-completeness readout \(\theta^+\), with \(V=\sum_p\omega_p\theta_p^+\). In the previous illustrative vector-law branch, \(R_\top\) may output \(q=(1,1,1)\) at \(\omega=(1,1,1)\). If one **incorrectly identifies** \(\theta^+\equiv q\), the calculation gives \(V=3\), contradicting the source's claimed five-law null \(V=0\). Therefore \(q\) and \(\theta^+\) must remain distinct readout channels unless the complete native source proves an explicit map; the v0.3 representative q-laws were X-table-compatible **illustrations**, not the full source law.

The formal response alphabet depends on each pair's \((\omega,g)\); it is not a proof that the native K4 \(\mathbb Z_2^3\) parity fiber provides twelve independent source-qualified bits. That carrier interface remains **OPEN_GATED**.

## 5. Measurable interface and candidate apparatus (not constructed)

A minimally programmable **digital state-preparation bench** could use six edge stations, each providing an independently preset integrity bit \(T\) and support bit \(L\), or 12 discrete input channels. Separate independent paths would acquire \(q\in\{0,1\}^3\), \(\theta^+\in\{0,1\}^3\), and leakage records \(\Lambda_0,\ldots,\Lambda_3\). The leakage custodian receives neither burden values nor candidate labels, consistent with source errata E.1. This is a **candidate apparatus design**, not evidence that such physical edge observables or UD matter carriers exist. A conventional FPGA, logic simulator, or P4 software switch can validate implementation of the Boolean truth table but not the physical correspondence.

| Field | Exact definition now | Physical measurement still required |
|---|---|---|
| \(T_a,T_b\) | assumed integrity-bit interface | instrument and integrity threshold with false-classification rate |
| \(L_a,L_b\) | assumed support-bit interface | independently calibrated latent support or proxy, units and threshold |
| \(g,\omega\) | defined Boolean gates | source-qualified mapping and preparation fidelity |
| \(q\) | three-bit gate output | independently identified output and timing |
| \(\theta^+\) | separately typed three-bit viable-output | independent sensor, baseline/null and uncertainty |
| \(\Lambda_k\) | independently returned leakage | source-blind provider, covariance, physical unit scale |
| \(n\) | formal observation index | no physical time map implied |

**Example error budget, not an empirical specification:** If the 12 raw input bits for each of 54 observations have independent flip probability \(p=10^{-5}\), then \(\Pr(\text{at least one input error})=1-(1-p)^{648}\approx0.00646\), and the union bound is exactly \(648p=81/12500\). A 1% familywise target would need an explicit calibrated sensor test; the raw-bit independence model itself is unverified. For the full 81-event A/B/C design, the bound becomes \(972p=0.00972\) at the same assumed \(p\). These are design tolerances, **not** measured capabilities.

## 6. Proposed rejection rules and controls

1. **Input qualification:** independent raw-bit label acquisition, blind to the output and candidate model; reject runs whose assigned class differs from measured class. Track boundary cases and analog threshold drift.
2. **A/B comparison:** identical 12-bit inputs, matched nuisance and boundary state, separated in acquisition order. Persistent differences falsify full-raw deterministic response under the declared apparatus model; stochasticity or drift may also explain discrepancies.
3. **A/C comparison:** class label fixed but raw microstate deliberately changed. Differences falsify class sufficiency, **not necessarily temporal memory**.
4. **Gate comparison:** only after source law maps q to a declared \(\theta^+\) may the complete five-law null \(V=0\) be tested; otherwise hold.
5. **PRED-01 leakage control:** source-blind \(\Lambda_k\) acquisition, preregistered nuisance controls and covariance. Distinguish a nonzero \(D_2(\varepsilon)\) due to nonlinear source from nonstationary leakage and quartic-action alternatives. Reserve independent \(E_3\) for WBX1 family tests; no post-exposure tuning promoted.
6. **S3 audit:** permutation-equivalence of a chosen toy law does not establish physical channel interchangeability; run explicit channel-permutation challenges before using the 20-orbit v0.3 shortcut.

## 7. Disposition

**EXACT_CONDITIONAL:** the raw Boolean lift, 9/4/3 count, 4096→27 map, iid expected replay count, three-pass 81 observation design, and counterexample to class-memory inference.  
**NUMERICAL:** finite grid / model preparation code replay and diagnostic noise budgets.  
**OPEN:** native K4 interface, independent leakage provider, separate q and theta-plus physical sensors, actual hardware or empirical test, SI units, clock and independent adjudication.  
**Physical promotion = 0.**
