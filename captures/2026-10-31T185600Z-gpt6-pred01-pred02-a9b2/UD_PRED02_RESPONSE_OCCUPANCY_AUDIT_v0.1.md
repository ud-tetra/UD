# UD PRED-02 — Formal response-class occupancy and replay coverage audit v0.1

**Created:** 2026-10-31  
**Lane:** D0 DEVELOPMENT / exact formal sampling analysis. **Physical promotion:** 0.  
**Source:** `ud-tetra/UD/docs/UD_PREREGISTRATION_PACKET_v1.0.md`, Part B §§B.1–B.3 and `docs/UD_EXTERNAL_REVIEW_BRIEF.md`, concern 1. Review must read the v1.1 errata §E.3 for MTA's distinct input type.

## 1. Source-bound formal class space

Take three independent *formal coordinates* indexed by packet pairs, each in
\[
\mathcal S=\{(\omega,g)=(0,0),(0,1),(1,1)\}.
\]
The full formal state space is \(\mathcal S^3\), of size \(3^3=27\). Counting by \(w_H(\omega)\), the number of pairs with \(\omega=1\), gives exactly
\[
|w_H=0,1,2,3|=(8,12,6,1).
\]
This reproduces the source's shell counts. **No assertion is made that all 27 states can be physically prepared.**

## 2. Replay collisions — exact expectation and its limit

Assume \(N\) observations are independent and identically distributed across class labels, with unknown fixed class probabilities \(p_1,\ldots,p_{27}\), \(p_i\ge0\), \(\sum p_i=1\). Count unordered equal-class pairs \(M=\sum_{a<b}\mathbf 1\{X_a=X_b\}\). By linearity of expectation,
\[
\mathbb E[M]=\binom{N}{2}\sum_{i=1}^{27}p_i^2.
\]
By Cauchy--Schwarz, \(\sum p_i^2\ge 1/27\), equality only for uniform sampling. Thus at \(N=24\),
\[
\boxed{\mathbb E[M]\ge\binom{24}{2}/27=\frac{92}{9}\approx10.2222.}
\]
**EXACT:** under iid fixed-probability sampling, the often-quoted "about 10" is the **minimum expected replay-pair count**, not an overestimate caused by skewed occupancy. For example, \(p_1=9/10\), all other \(p_i=1/260\), gives \(\mathbb E[M]=145383/650\approx223.666\), but loses diverse class coverage.

**CRITICAL LIMIT:** expectation is not an observed guarantee. A prescribed schedule of 24 distinct classes has zero replay pairs (possible because 24<27). An arbitrary non-iid/adversarial time series can also avoid repeats. Even uniform iid has a nonzero, albeit small, chance of no repeats. Physical feasibility and temporal independence are not established by an occupancy formula.

## 3. A constructive formal schedule (conditional on state preparation)

A complete one-pass sweep of all 27 formal classes guarantees all \(w_H\) shells and at least one \((0,1)\) class, but zero same-class replay pairs. A two-pass sweep, each of 27 classes repeated exactly twice, uses **54 scored formal observations**, guarantees the required shell and MTA discrimination coverage, and yields exactly **27** same-class unordered replay pairs, one in each class.

This is not claimed to be the minimum physical number of events. Carriers, preparation constraints, independence, readout noise, time cost and multi-run blocking are OPEN. A smaller targeted schedule may be possible once a class-preparation graph is known.

## 4. Decision and next gate

**DERIVED:** the uniform-occupancy expectation is conservative for iid replay *count* but says nothing about shell coverage quality or laboratory implementation. Prefer targeted class preparation and explicit replay quotas rather than relying on a distributional mean. A frozen memoryless-model test should reserve independent re-preparations of identical formal classes and track drift/covariates; a full two-pass 54-class schedule is a sufficient mathematical design if preparation is possible.

**OPEN_GATED:** state-preparation existence for all classes, cross-run comparability, MTA input type, laboratory apparatus, and independent reproducibility. No source-level selector theorem or physical gain established. Non-constructor review deferred.

## 5. Reproduction

```
python3 pred02_occupancy.py --out pred02_results.json
python3 -m unittest discover -v
```

The script uses Python standard-library `Fraction`, `itertools.product` and `Counter`, and preserves the full exact iid no-repeat probability in JSON.
