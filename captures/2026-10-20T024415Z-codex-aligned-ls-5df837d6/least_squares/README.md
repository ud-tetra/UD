# Saved floating least-squares step: finite posterior certificate

Both fixed PR256 saved shifts are within about 3.0e-14 in operator norm of the exact least-squares solution for their own saved lagged U factors. This is a finite posterior arithmetic certificate, with no new estimator calls or raw records.

| Fixed case | Positive lower bound on lambda_min(A^T A) | Normal residual operator upper | LS-step distance upper |
| --- | ---: | ---: | ---: |
| null_top1_alternating | 0.9642472166969365 | 2.888633811516826e-14 | 2.9957398491767956e-14 |
| null_top2_alternating | 0.9642472166969306 | 2.882566856634085e-14 | 2.989447941066855e-14 |

The certificate's exact rational bounds are authoritative; table decimals are displays. A=U[:-2], B=U[2:], and the saved T are the same finite dyadic matrices produced by the earlier estimator. Exact integer chunk arithmetic forms Gamma=A^T A and N=A^T(AT-B). The positive eigenvalue floor is the larger of exact Gershgorin and 1 minus an outward bound on ||Gamma-I||F; the latter is selected for both cases. The normal Frobenius bound conservatively bounds its operator norm. Since Tstar=A^dagger B and Gamma(T-Tstar)=N, the reported distance is ||N||F/lambdaLower, rounded outward.

This does not say that the raw lag residual vanishes. A nonzero lag residual can be orthogonal to every column of A, yielding exact LS optimality and zero normal residual. The controls explicitly verify that distinction. It also does not identify an exact spectrum(T), certify a generator or six-ratio calibration, or establish uniform rounding accuracy of a backend. All previous phase/reconstruction results and the original top2 Frobenius admission HOLD remain unchanged.

Protocol, core arithmetic, source pins and 13 synthetic controls were frozen before computing either actual saved normal. Root and independent reviewer released execution. Both complete 209x209 Gamma and N integer matrices, denominator metadata and canonical hashes are retained in deterministic lossless JSON-gzip witnesses. Numerical U/T factors are read from the immutable source capture without copies. No estimator, rank selection, perturbation or raw-record generation occurs.

The two compressed witnesses total 4,091,335 bytes. Primary certificate/resource plus witnesses total 4,098,269 bytes. The primary exact arithmetic run took 20.802 seconds and peaked at 580,268 KiB process RSS on this host; these are measurements, not performance guarantees.

Replay the frozen arithmetic into a new output directory:

```
PYTHONDONTWRITEBYTECODE=1 python certify.py --repo /ABS/PATH/ud-repo --out /ABS/NEW/OUTPUT
```

The output guard rejects this package, its descendants, all MANIFEST-bearing ancestors and corresponding resolved symlink destinations. Each write is exclusive. Root owns replay/publication. Separate review recomputes Gamma and Cross=A^T B with independent binary64 decoding, then N=Gamma T-Cross, and compares every retained integer entry. Physical Promotion = 0; development only; no registry entry.
