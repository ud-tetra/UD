# UD-PM-PRED02-001 v1.0 — Exact iid class-collision bound

Kind: THEOREM, exact conditional.
Proof status: VERIFIED_SCOPED (independent method re-derivation; non-constructor review deferred).
Physical promotion: 0.
Source: UD preregistration v1.0 Part B, errata v1.1 E.3 and PRED02 research PR #475 (unmerged).

## Statement

Let S have 27 formal response labels, S = {(0,0),(0,1),(1,1)}^3. Assume X_1,...,X_N are independent and identically distributed S-valued observations from a fixed probability vector (p_1,...,p_27), each p_i >= 0 and sum_i p_i=1. Let M count unordered pairs (a,b), a<b, for which X_a=X_b.

Then E[M] = binomial(N,2)*sum_i(p_i^2) >= binomial(N,2)/27.
Equality occurs exactly at uniform probabilities p_i=1/27. For N=24,
E[M] >= 276/27 = 92/9.

## Proof

For any a<b, independence gives
P(X_a=X_b)=sum_i P(X_a=i)P(X_b=i)=sum_i p_i^2.
Linearity of expectation across all binomial(N,2) unordered pairs proves the identity. Cauchy-Schwarz implies
1=(sum_i p_i)^2 <=27*sum_i p_i^2.
Equality requires all p_i equal. For N=24 there are 276 observation pairs, giving 276/27=92/9. QED.

## Counterexample and limits

This expectation bound does not guarantee any matches in a specific run. A deliberately prepared sequence with 24 distinct labels has M=0; it is not iid and does not contradict the theorem. Under uniform iid sampling, that no-match event still has positive probability. Two observations in each of 27 classes force exactly 27 within-class matching pairs, conditional on the physical feasibility of such class preparation.

## Verification and disposition

A separate exact rational check recomputed 276/27 = 92/9. The algebraic argument is unconditional *within the declared iid probabilistic model*, but iid sampling, source class realizability, measurement apparatus, class stability and independently controlled leakage remain unverified physical assumptions.

Result: VERIFIED_SCOPED EXACT_CONDITIONAL; outside review DEFERRED; physical promotion 0. The historical phrase approximately 10 replay pairs must remain an iid expectation, not a deterministic acquisition guarantee.
