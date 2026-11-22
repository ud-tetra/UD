# PB3 and PB5 unit radial memory gaps

CYCLE-088 (#592) · PB5 (#593) · PB3 (#594) · **Physical Promotion = 0**

The comparison uses the unit coefficient metric, the uniform cell-average subspace, the radial edge-trace projector, unit radial coupling and zero exterior coupling. Rates are in inverse carrier time.

| Carrier | Dimension of stable sector | Stable spectral gap | Leading memory pole rate |
| --- | ---: | ---: | ---: |
| PB3 | 16 | 0.289753482825 | 0.289753482825 |
| PB5 | 26 | 0.182555891568 | 0.182555891568 |

PB5 has about 63% of PB3's asymptotic rate under these conditions. The gap comparison is numerical at the registered coupling. It establishes no monotonic law in ring size or coupling.

## Operator and pole test

Let $U$ contain the cell vertex indicators, $P=U(U^\mathsf TU)^{-1}U^\mathsf T$, $Q=I-P$, $A=\partial-\partial^\mathsf T$, and $D=MM^+$ the radial edge projector. Set $L=QAQ-D$ and $B=QAU$. The stable characteristic polynomial on $\operatorname{im}Q$ is obtained by removing the resolved zero factors and the exact undamped factors from the full characteristic polynomial. Its roots characterize the stable-sector spectral gap.

The memory transform has the same poles as $B^\mathsf T(zI-L)^{-1}B$. Passing to an orthonormal cell-average basis amounts to invertible factors on either side. The exact numerator matrices follow from the moments $B^\mathsf TL^jB$ and Cayley–Hamilton. Cancelling factors common to all numerator entries gives the monic least common denominator of the memory transform.

| Carrier | Exact reduced memory denominator (up to nonzero scalar) |
| --- | --- |
| PB3 | $(5z^2+5z+24)(z^3+z^2+5z+2)$ |
| PB5 | $(7z^2+7z+40)(z^6+2z^5+10z^4+13z^3+23z^2+18z+4)$ |

Exact cancellation removes several stable modes, and root evaluation finds that the rightmost stable poles survive in both memory kernels. The reported pole rates describe the asymptotic exponential envelope. The comparison supplies neither a finite settling horizon nor a time-local error estimate.
