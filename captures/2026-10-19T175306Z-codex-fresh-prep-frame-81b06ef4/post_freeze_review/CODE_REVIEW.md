# Prospective source-frame campaign: same-team code review

Status: no material mathematical defect found in the reviewed draft. This is
prospective same-team review, not external independent review. No transform,
raw record, estimator, or main experiment was executed. Physical promotion 0.

Reviewed: records.py, kernel.py, common.py, FIXED_BUDGET.json,
PARENT_UNIFORM.json, BASE_GENERATION.json, and the pinned parent estimator.

## Source-family and error bounds

The same-parity maps preserve the declared per-preparation rate/jitter family.
For b in class s, y_b(k)=p_s(k)R(o_b)B_b. Its transformed coefficient is
sum_b T_ab R(o_b)B_b; origins can be absorbed without changing p_s. If a new
explicit origin is desired, left-multiply that coefficient by its inverse
origin rotation. This is a statement about the frozen principal-band synthetic
model, not physical state preparation or a native parity law.

records.transforms verifies exact orthogonality of the integer numerator matrix
and its parity support. The rational map has disjoint blocks (3u-4v,4u+3v)/5;
the unpaired final even preparation is unchanged. Both outputs are formed from
the original input pair, so there is no in-place update error.

nominal() uses integer floor division and rem>=3. For denominator 5 this is
exact nearest rounding for positive and negative integers; half-ties cannot
occur. Its exact |5*rounded-numerator|<=2 check is appropriate. The scalar
source error (7/5)d0+(2/5)2^-48 and subsequent vector bound
62*d_nom^2+2*d_nom*2^-48+2^-96 are correct. Signed permutations add no rounding.
Using this rational bound also for the unrotated final row is conservative.

The 7*max_abs_raw<2^63 guard bounds every rotation multiply/add partial sum.
Noise is added only after nominal rounding, one signed quantum at one channel
per preparation/time vector. The second pass verifies that exact difference
against the correct new nominal and checks every scalar. New raw hashes are
frozen before any estimator call. All RNG seeds, call order, transform kinds,
runtime versions, and fixed caps must be in the prospective freeze.

The old baseline-centered raw ball is not the fresh input domain. Neither
orthogonality nor the new nominal one-quantum check implies old-ball eligibility.
Orthogonality preserves aggregate preparation energy, not each preparation norm
unless the relevant preparation Gram supplies that stronger property.

## Estimator and proof boundary

kernel.project checks integer partial sums, requires |numerator|<2^53, then
casts and scales exactly by 2^-55. The SVD/lag-two least-squares/eigenvalue/angle
core matches the pinned parent arithmetic. The cutoff remains 2^-24 and the
selected floating order is not forced. New sketch excitation can change despite
the unchanged full raw temporal span; the fixed sketch is not covariant under
general preparation mixing.

Runtime note: the pinned parent sets OPENBLAS_NUM_THREADS=1 before NumPy/SciPy;
kernel.py does not set it itself. If runtime continuity or repeatable floating
arithmetic is intended, pin it in the launcher before imports and record it.
This does not invalidate a posteriori certificates of actual saved arrays.

The kernel explicitly says full_SVD_certificate_executed=False. That limitation
must remain visible: a floating learned-order count is not a validated exact
spectral count, and retained source-frame geometry is not a full SVD proof.
Order other than 209 must produce an applicability HOLD for the fixed reference.

The fixed source-frame theorem applies through actual measured U relative to U0
without old-ball membership. Preserve these exact inherited caps:

- retained Gram Frobenius defect <=2^-43;
- normal residual <= the old three-output maximum, about 3.0785144547e-14;
- raw source-frame residual strictly below about 2.4895818841e-10;
- derived returned shift strictly below about 5.5632064091e-10.

The dyadic fractions in FIXED_BUDGET.json are authoritative. The normal cap was
only an old finite observed maximum; new outputs need to meet it. No resetting
to the new maximum or post-outcome alignment-budget change is allowed. An
auxiliary X can be proposed after U is returned because its exact residual is
verified without an accuracy/inverse assumption.

Passing this route certifies a measured source-frame/returned-shift property.
It does not execute or certify the other seven policy gates, complete phase
matching, exact full rank, future floating convergence, or physical/SI transfer.
Source-frame displacement includes input effects and numerics, not just roundoff.

## Recommended finite controls before generation

1. Reject an orthogonal swap across parity classes; orthogonality alone is not
   enough for the single-clock-family claim. Reject repeated permutation columns.
2. Check the exact rational block products and denominator-5 rounding on
   negative and positive residues, especially numerator -2 and -3. Deliberate
   wrong floor rounding should fail the residue predicate.
3. Reject two noisy coordinates or a two-quantum change in one 62-vector;
   accept one signed quantum relative to its own new nominal. Check counts and
   flattening layout (k,c,a) -> raw coordinate 37c+a with a small exact toy.
4. Reject a changed hash, truncated input, and duplicated/missing sample; do not
   infer complete custody merely from a shape declaration.
5. Retain source-frame equality as HOLD when the frozen predicate is strict;
   retain closed Gram/normal cap predicates exactly as published. Do not infer
   an actual phase failure from a sufficient frame-budget HOLD.
6. A zero auxiliary X must fail the small principal-angle requirement; a learned
   order other than 209 must not enter the fixed 209-space certificate.
7. Independently regenerate frozen new raw hashes and nominal hashes, then
   replay exact source-frame/normal fractions from saved factors. Keep every
   family and every PASS/HOLD; do not choose new seeds or sketches after results.

These are control recommendations, not executed control results. No new case
outcome or pre-existing external review is claimed.

## Follow-up draft audit: measured verifier and replay

Reviewed the subsequently added validate.py, controls.py, align.py and replay.py
without executing them. kernel.py now pins OPENBLAS_NUM_THREADS and
OMP_NUM_THREADS to 1 before NumPy/SciPy imports, addressing the runtime note
above. No record/results were viewed or generated in this follow-up.

The direct residual uses U1 and U0*X at the common exact binary scale; its
squared denominator is 2^(2*max(bu,b0+bx)). The normal residual numerator is
H*2^bt-G*T_integer with denominator 2^(2bu+bt), and its squared denominator
is correctly 2^(4bu+2bt). The actual raw-shift quadratic form denominator is
2^(2bu+2bt). Its nonnegative numerator is checked before taking a square root.
These expressions match the reviewed Frobenius theorem and do not assume
floating least squares is exact.

bound() applies retained Gram normalization, the common principal-angle
distance, source-comparison residual bound, deleted-row lower margin and exact
normal-residual correction correctly. classify() separately retains actual
order applicability, closed retained-Gram/normal caps, strict frame cap and
strict returned-shift allowance. A diagnostic direct shift PASS cannot override
a fixed normal/frame cap failure. It states no new full SVD/order/phase/all-gates
certificate. The five predetermined classifier controls cover those fixed
caps and strict frame boundary; their results are not yet claimed here.

align.py freezes the auxiliary coordinates and source run/data hashes before
exact measurement. X is untrusted, so no solve accuracy or inverse premise is
needed. A changed learned order skips this fixed-reference proposal. The saved
numeric witness hashes are checked before use, and wrong-order outputs remain
available rather than being forced or replaced.

replay.py distinguishes saved-witness-only replay from optional full raw and
exact-projection regeneration; it performs no new SVD. That distinction must
remain in the completion report. Fresh exact source-frame replay is not a new
complete raw acquisition or all-seven-gates admission.

Robustness item before freeze: kernel.run currently has no per-case exception
receipt if SVD/eig/inverse fails. Such an exception would abort the remaining
cases, although raw and possibly SVD data are already retained. A fixed
catch-and-HOLD driver may record the failing stage and preserve continuation
without introducing any fallback, refit, rank forcing, seed change or retuning.
This is a prospective workflow recommendation, not an observed failure.

## Final pre-freeze check

The requested per-case exception policy is now implemented: projection/SVD/
phase-stage exceptions produce HOLD_ESTIMATOR_EXECUTION with the exception
type/message and no retry, replacement or fallback. Saved evidence is retained
and later frozen cases continue. align.py skips those incomplete runs, and
validate.py retains their explicit HOLD rather than attempting missing arrays.
Integrity/hash failures remain hard refusals. The prior workflow item is resolved.

Final disposition: acceptable to freeze and execute within the stated limited
source-frame scope. No mathematical or acceptance-code defect was found in this
prospective review. This statement is not a prediction of any new case outcome,
an executed control result, or independent external review.
