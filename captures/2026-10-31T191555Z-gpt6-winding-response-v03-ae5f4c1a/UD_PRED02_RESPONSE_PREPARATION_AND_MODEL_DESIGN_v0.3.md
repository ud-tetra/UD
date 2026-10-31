# UD PRED-02 — 27-state response preparation, model-discrimination and replay protocol v0.3

**Date:** 2026-10-31  
**Evidence:** EXACT_CONDITIONAL class counting / code-distance / \(S_3\) orbit enumeration; no physical apparatus certification.  
**Status:** D0 development / assumption-scoped P0 design, non-constructor review deferred, physical promotion **0**.

## 1. Source and mathematical objects

Source: `ud-tetra/UD/docs/UD_PREREGISTRATION_PACKET_v1.0.md`, Part B §§B.1–B.3 and D (blob `c5ddbb6f4df4ba3ff5c6b39895b58c6e955fc82b`), read with `UD_PACKET_v1.1_ERRATA.md` §E.3 (blob `6961b917f4f1ca470127aa0b7d3c1b59693f4373`). The source states \(\omega_p\le g_p\), per pair \((\omega_p,g_p)\in\{(0,0),(0,1),(1,1)\}\), three pairs, 27 formal classes and three major falsifier types: viable completeness \(V=\sum_p\omega_p\theta_p^+=0\), deterministic same-class replay, and optional monotonicity \(\omega\le\omega'\implies q\le q'\).

**Typed state:** \(x=((\omega_1,g_1),(\omega_2,g_2),(\omega_3,g_3))\in\mathcal X\) with \(|\mathcal X|=3^3=27\). The output \(q(x)\in\{0,1\}^3\) is a proposed response/gate vector. These are mathematical classes, **not** calibrated physical preparations or readouts.

The formal shell weight is \(w_H(\omega)=\omega_1+\omega_2+\omega_3\); the 27-class counts for weights \(0,1,2,3\) are \((8,12,6,1)\). Exactly 19 classes contain at least one partial-integrity pair \((0,1)\). The source's Gate B requires at least one event from each of shells 0,1,2 plus one partial-integrity event; its omega-only X table does not apply directly to MTA.

## 2. Minimal gate and replay feasibility: four formal observations

A shell-0 partial-integrity class plus a shell-1 and a shell-2 class satisfies the three shell gates and the partial condition in **three distinct formal preparations**:

- \(s_0=((0,1),(0,0),(0,0))\), shell 0 and partial-integrity;
- \(s_1=((1,1),(0,0),(0,0))\), shell 1;
- \(s_2=((1,1),(1,1),(0,0))\), shell 2.

Repeating \(s_0\) gives a **four-observation** formal gate-and-one-replay schedule. The lower bound is four only under the requirement of three distinct shells and one repeated identical class, with one event permitted to satisfy multiple gates. This is **not** a full five-law scoring protocol and not a noise-qualified apparatus test.

## 3. Explicit endpoint representative laws and a six-class error-separation design

**Additional modeling assumption P2-R:** To turn the source's Hamming-weight \(X\) table into fully specified *vector* outputs for a toy discrimination design, select representatives

\[
\begin{aligned}
q_{R_0}(\omega,g)&=\omega,\\
q_{R_2}(\omega,g)&=\begin{cases}\omega,&w_H(\omega)\le1\\(1,1,1),&w_H(\omega)\ge2,\end{cases}\\
q_{R_1}(\omega,g)&=\begin{cases}(0,0,0),&w_H(\omega)=0\\(1,1,1),&w_H(\omega)\ge1,\end{cases}\\
q_{R_\top}&=(1,1,1),\qquad q_{\mathrm{MTA}}=g.
\end{aligned}
\]

**EXACT conditional:** For every one of the 27 inputs, these chosen laws reproduce the source table for \(X(\omega)=w_H(q)-w_H(\omega)\), and the MTA law uses \(g\), as required by the v1.1 errata. **Crucial scope restriction:** the source's scalar X table does not uniquely determine every component of its original response rules; the selected vector formulas are *illustrative X-table-consistent representatives*, not a verified transcription of §7.5's full rule text. Use source-frozen law code before any formal experimental registration.

Define output separation between two models on an ordered schedule \(\mathcal S\) by the Hamming distance of their concatenated three-bit predictions:

\[
d(f_i,f_j;\mathcal S)=\sum_{x\in\mathcal S}\|q_{f_i}(x)-q_{f_j}(x)\|_1.
\]

**Minimal six-state design for distance at least 3 across the five chosen representatives:**

| Index | \((\omega,g)\) pair triple (00,01,11 notation) | Shell |
|---|---|---:|
| 1 | (01,01,01) | 0 |
| 2 | (11,00,00) | 1 |
| 3 | (00,11,00) | 1 |
| 4 | (11,11,00) | 2 |
| 5 | (11,00,11) | 2 |
| 6 | (00,11,11) | 2 |

The ten pairwise Hamming distances have minimum **3 bits**. The lower bound on six observations for distance ≥3 is **EXACT within P2-R:** \(R_0/R_2\) differ by exactly one bit only at shell-2 states (requiring at least three such observations); \(R_2/R_1\) differ by exactly two bits only at shell-1 states (requiring at least two); \(R_1/R_\top\) differ by three bits only at shell-0 states (requiring at least one). These are disjoint shell obligations, so at least \(3+2+1=6\) observations are required. The table attains the bound and provides at least three partial bits in its first state to distinguish \(R_0\) from MTA.

Repeat all six preparations in a second pass (reordered) for **12 formal observations** and two same-class readings per chosen state. The repeated deterministic prediction signatures have minimum Hamming distance **6**. This is a mathematical coding separation; apparatus bit errors, leakage, response stochasticity, correlated noise and class mispreparation are not characterized, so no empirical detection probability is claimed.

## 4. Complete two-pass coverage: 54 formal observations

For an assumption-light *class coverage* protocol, visit each of the 27 states twice. The generated file `RESULTS.json` contains the full 54 ordered observations, with seed `20261031`. The first pass is a seeded permutation; the second is a cyclic rotation by 9, giving a repeat-index separation of at least 18 (at least 17 other observations between the two readings). By construction: all 27 classes have multiplicity 2, the shell totals are \((16,24,12,2)\), and 38 of the 54 observations contain a partial \((0,1)\) pair. The design covers class identity but **does not certify physical attainability** or eliminate systematic memory and drift.

**Proposed controls (new, not source-frozen):** independently certify each input's pair-state label from raw instrumentation; insert repeated sham/null controls and known positive references; randomize/separate repeats to expose time dependence; preserve preparation history and baseline instrument drift; test pair permutations with independent physical channels. Do not blend state preparation, classification and outcome scoring into one fitted model. A qualified apparatus must declare uncertainties and false-classification rates before any CRL-2b register.

## 5. Symmetry-reduced branch: 10 orbits, 20 repeat observations

Permuting the three pair slots by \(S_3\) acts on the 27 formal classes. Orbit types are **3 orbits of size 1**, **6 orbits of size 3**, and **1 orbit of size 6**, totaling 10 orbits and 27 members. Under the **additional assumption** that the physical preparation, dynamics and readout are \(S_3\)-equivariant, testing one representative from each orbit twice requires 20 formal observations. The five illustrative endpoint laws pass algebraic equivariance under all six permutations on all 27 states.

**NO-GO for unjustified quotienting:** Equivariance of an *assumed mathematical law* is not empirical equivariance of the underlying source preparation or apparatus. A 20-run representative schedule cannot itself detect all symmetry-violating channel-dependent behaviors. Add explicit permutation challenge controls or return to the 54-class protocol if the symmetry gate is not independently earned. A quotient branch never silently replaces the source's original frozen acquisition schedule.

## 6. Measurable contract and decision matrix (all OPEN_GATED at the physics boundary)

| Quantity | Mathematical definition | Required independent source |
|---|---|---|
| Pair integrity and latent indicator | \((\omega_p,g_p)\) | Raw edge/support measurements and source-qualified classifier |
| Outcome | \(\theta_p^+\) or declared binary \(q_p\) | Independent sensor, zero/one threshold, error rate and timing |
| Viable completeness | \(V=\sum\omega_p\theta_p^+\) | Verified paired input/output and null rejection |
| Replay mismatch | Same exact 27-class input, different output | Replicated source history, instrument variance and independence |
| Monotonicity | Comparable \(\omega\le\omega'\), compare \(q\) | Controlled matched nuisance, context state and channel order |
| Endpoint-family separation | Predicted output codewords under **chosen** q-laws | Full native response map, not merely X table |
| \(S_3\) permutation | \(q(\pi x)\overset?=\pi q(x)\) | Relabelled physical carrier and calibrated channel symmetry |

**Evidence/status:** Mathematical class and schedule proofs EXACT_CONDITIONAL; sensor and carrier maps OPEN_GATED; experimental threshold design OPEN; no blind/held-out run; independent review deferred; physical promotion 0. Source-complete native state preparation is the next physical bridge, not a claim that 12 or 54 laboratory events already exist.

## 7. Executable artifacts

`carrier_and_preparation.py` generates exact 27-state and 10-orbit enumeration, the four-gate schedule, 12-observation six-class discrimination schedule and 54-observation two-pass schedule, with S3 equivariance and pairwise Hamming-distance checks. `test_carrier_and_preparation.py` contains deterministic numerical and exact tests. No existing source scorecard or §7.5 acquisition was modified.
