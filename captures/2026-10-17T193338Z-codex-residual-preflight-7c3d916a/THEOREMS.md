# Exact residual preflight for the record-only spectral certificate

Status: EXACT derivation plus constructor execution tests. Physical promotion 0.
The theorem concerns the current finite, normalized record and its proposed modal fit;
it does not identify a physical system, recover hidden states, or decide a record's
true spectral signature after a failed fit.

## 1. Norm and phase convention

The record is `Y[a,k,c]/2^48`, with 37 preparations, 8191 times and 62 channels.
The normalized Hankel has entries `Y[a,i+j,c]/(4096*2^48)`.
For a proposed temporal model, the existing verifier encloses every sine and cosine
by a dyadic multiple of 2^-60 with error strictly below 2^-60. Coefficients are
int64 numerators scaled by 2^-60. Let `C` be the sum of the largest absolute
coefficient over all 2294 channel/preparation coordinates, separately for each
nonstationary sine/cosine row. The stationary row has no phase error.

Let `w_k=min(k+1,8191-k,4096)`. After checking every reading exactly, define

\[
 F=\frac{\sum_{k,c,a}w_k\,(P_k C_{c,a}-2^{72}Y_{a,k,c})^2}
          {4096^2\,2^{240}}.
\]

Here `P_k` is the integer dyadic-phase row and `C_{c,a}` in the numerator denotes
the coefficient column, not the nonnegative bound `C` above. This is the exact
squared Frobenius norm of the dyadic-phase model's Hankel residual. There is no
SVD tolerance or sampled subset in this computation.

The difference between the dyadic-phase model and the exact-phase model obeys

\[
 \|H_{\rm phase}-H_{\rm dyadic}\|_F
 < e:=48C\,2^{-120},
\]

because `sqrt(37*62)<48`, `sum_k w_k=4096^2`, and each scalar phase-induced
model difference has magnitude at most `C*2^-120`. If `C=0` this difference is zero.
Using `<=e` uniformly also covers this case. This norm refers to the modal phase
approximation, not measurement noise or the contract's source-defined shape gate.

## 2. Exact square-root bracket and early-HOLD theorem

Write `F=u/v>=0` in lowest terms and fix `b=100`. Compute using integer arithmetic

\[
 n=\operatorname{isqrt}\left(\left\lfloor\frac{u2^{2b}}v\right\rfloor\right),\qquad
 \ell=n2^{-b}.
\]

Then `ell^2<=F<(ell+2^-b)^2`. Define `L=max(0,ell-e)`.
By the reverse triangle inequality, the true exact-phase proposed residual
has Frobenius norm at least `L`. The frozen selection threshold is

\[
 T=9093197064441289377/604462909807314587353088.
\]

**Theorem.** If `L>T`, the existing residual-budget certificate for this same
proposal cannot return `CERTIFIED_NUMERIC_RECORD_SIGNATURE`. It is sound to
return `HOLD` before modal factors, factor Grams, Cholesky and core SVD.

**Proof.** The existing proof uses a validated upper enclosure of
`sqrt(F)+phase_error_upper`, plus a nonnegative truncation allowance, as its
residual budget. This upper budget bounds the true proposed residual, which is
at least `L>T`. Therefore its required strict test `total_error<T` cannot pass.
All other outcomes of the old verifier, including an inconclusive arithmetic
step, are already HOLD. Cases where `L<=T` execute the identical old `verify`
function. Thus every accepted outcome is preserved, provided its unchanged proof
executes successfully; the preflight alone can never create a new acceptance.
This theorem presumes the original phase checks and exact residual calculation
have completed and the final input-identity check succeeds. QED.

Equality and unresolved floor-resolution cases continue. No float is used for the
gate. A large residual is a Frobenius residual of a particular approximation;
no inference that a particular true singular value is too large follows. Another
proposal can succeed. The preflight also does not prove fitting convergence,
experimental acquisition admission, independent review, or a leakage mechanism.

## 3. Implementation scope

`residual_preflight.py` implements the integer/rational theorem.
`certify_record.py` calls it only after all 18,790,154 readings and phase components
are checked. The positive branch calls the byte-unchanged `proof_math.py`.
Both branches perform the original final record/contract/proposal SHA-256 recheck.
Early HOLD supplies no fabricated singular-value or condition bounds.
`RESIDUAL_PREFLIGHT.json` is separate from the full positive certificate, so the
existing positive certificate schema/bytes can be compared directly.

The code and planned controls were frozen before these new full executions,
although the constructed control records and their old outcomes were already
known. This is a constructor regression benchmark, not a blinded independent run.
