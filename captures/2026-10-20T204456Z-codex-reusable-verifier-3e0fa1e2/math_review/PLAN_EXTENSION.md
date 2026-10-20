# Pre-exercise extension: nonzero exact dyadic metrics

Added before exercising the new implementation. This supplements the frozen initial plan without changing its bytes or expected results.

- Positive small-tail fixture: m=n=2, N=diag(2^49,1), denominator exponent48, singular=[2,0], U=e1, right_transpose=I2. Both retained residuals and Gram defects are zero; the discarded output norm and full error bound are exactly2^-48. It must pass the default2^-41 accuracy and2^-24 cutoff gates.
- Positive small-retained-residual fixture: m=n=2, N=diag(2^49+1,0), denominator exponent48 and the same saved factors/proposals. Both equation residuals are exactly2^-48, tail bound0, compression c=2^-48, off-diagonal conservative enclosure e=2^-48, and retained/full error bound2^-47. The actual leading singular error is2^-48, so this is a valid conservative certificate. It must pass default gates.
- Negative large-tail counterpart: m=n=2, N=diag(2,1), denominator exponent0 with the same saved factors/proposals. The actual second singular value is1. The tail bound is1, so full2^-41 and original actual-cutoff gates must not certify. A sorted saved list alone cannot hide the large tail.

These are designed exact arithmetic fixtures, not new research preparations, model fits or empirical validation. Expected root-grid wrappers at180 bits are exact for these dyadic examples.
