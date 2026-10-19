# Prospective preparation-transform source review

Same-team mathematical review before new record generation. No new records,
fits, or outputs were executed. Physical promotion 0.

## Clock family

For preparation b in rate class s=(-1)^b, write its exact source series as

    y_b(k)=p_s(k) R(o_b) B_b,

where p_s contains the stationary mode and sine/cosine pairs with rate
1+s*mu and jitter s*(-1)^k*j. For a rational orthogonal preparation transform
T mixing only indices of the same parity,

    y'_a(k)=sum_b T_ab y_b(k)
           =p_s(k) sum_b T_ab R(o_b) B_b.

Thus each new preparation retains the same rate/jitter family. Different
origins are absorbed into coefficients. If a particular new origin o'_a is
declared, set B'_a=R(-o'_a) sum_b T_ab R(o_b) B_b.

Cross-parity mixing still lies in the combined 209-function family but
generally is not a single-clock preparation. Restricting to parity classes
preserves the stronger single-clock statement. Here parity means preparation
index/rate class, not a derived physical orientation symmetry.

## Encoded transform and rounding

Let qraw=2^-48 and let each old encoded scalar differ from its exact old modal
waveform by at most d0. A signed permutation is exact on integer records and
adds no rounding error; its nominal scalar error remains at most d0.

For one disjoint pass of blocks

    [[3/5,4/5],[-4/5,3/5]],

round each final rational integer value once to nearest integer. Its denominator
is 5 (or a divisor), so there are no half-ties; the rounding error is at most
2/5 integer units, sharper than 1/2. The row L1 norm is 7/5, giving

    d_nom <= (7/5)*d0+(2/5)*qraw.

After adding at most one signed raw quantum per 62-vector, the final squared
vector discrepancy from the transformed exact source is bounded by

    62*d_nom^2+2*d_nom*qraw+qraw^2.

For an unrotated signed-permutation row use d_nom=d0. The looser bound
(sqrt(62)*d_nom+qraw)^2 is also valid.

For compositions, use the actual final rational row L1 norm and its denominator;
the one-pass constants do not automatically survive multiple overlapping
rotations. If the common reduced denominator is d, nearest rounding has
maximum error floor(d/2)/d integer units. Exact arithmetic must precede the one
final rounding; intermediate rounding changes both the model and error bound.

## Aggregate and sketch errors

Because T is orthogonal, transforming the old error tensor exactly preserves
its aggregate Frobenius norm over preparations. For r_rot rotated preparation
rows in one disjoint pass, a conservative full-record source error is

    sqrt(37*n*62)*d0
      +(2/5)*qraw*sqrt(r_rot*n*62)
      +qraw*sqrt(37*n),

where n=8191. Multiplying this by a validated ||S||2 bounds the transformed
source discrepancy in the fixed sketch, in both operator and Frobenius norms.
No statistical independence is assumed. If all integer differences are
measured, exact post-generation bounds can be tighter without changing the
declared recipe or acceptance thresholds.

## Excitation and admission

An exact invertible preparation transform preserves the full raw temporal
column space before new rounding, but it need not preserve the excitation or
singular spectrum after multiplication by the fixed sketch S. Fresh sketched
order/conditioning must be checked. The old encoded baseline vector ball is
not preserved by a changed nominal preparation; old admission does not follow.

The direct measured-source-frame theorem can still certify actual returned
U relative to the pinned U0, without an old-input-ball premise. Its existing
retained Gram, measured normal-residual, frame-displacement, order/applicability,
and strict source budget gates must all be retained, with every HOLD preserved.
Source displacement includes fresh input/model effects and numerics, not just
roundoff. No uniform future floating convergence is implied.

Orthogonal mixing preserves total squared preparation norm, not each individual
norm in general. A physical state-preparation or stock-normalization statement
would require the actual preparation Gram/source map and is not established
by transforming these recorded series. No old full-Hankel signature or physical
promotion transfers merely from temporal span preservation.
