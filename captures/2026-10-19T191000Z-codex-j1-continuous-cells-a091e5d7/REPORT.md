# J1 continuous parameter cells and partial precision coverage

**DERIVED / EXACT CONDITIONAL.** Continuous enclosures pass; full-band1/10 precision remains **OPEN**. Development — no registry entry. Constructor verification only; physical promotion **0**. Refs #218 #136; append-only extension of PR223/225/226/228/229/230.

PR230 passed CI and merged at `3f8518b0c6a82235d3b675599ea919823a9df7a2`. Before merging, its integration with concurrent mainc4f82ce was verified locally; the merged tree equals the verified tree78f86b1b941e5e3f40b66e017d208b5becf68de3. The concurrent retained-cutoff/phase-certificate contribution is preserved. No prior bytes are rewritten.

## New result and interpretation

An exact checker now covers the positive parameter rectangle [0,6]x[1/10,1] by221 continuous cells, and negative frequencies by conjugation. Every cell has a valid conditional enclosure. **Nine low-frequency strips meet the declared1/10 absolute output target.** The remaining212 cells do not meet that target with these certificates.

In particular, throughout

$$\boxed{|\omega|\le\frac{23983}{250000}=0.095932,\qquad
\frac1{10}\le\gamma\le1,}$$

the constant output proxy centered at

$$\widehat H=\frac{582477}{500000}=1.164954$$

has absolute continuum error at most1/10. The recorded binary64 representation of this center and its exact evaluation-error bound are included, so the statement also covers that reported floating surrogate.

This is an output approximation derived from the static enclosure, not a new conforming field or finite-element solve. The source, port and continuum model are unchanged. No resonance accuracy, native UD mechanism or hardware interpretation is inferred.

The prior global gain bound already supplied coarse enclosure everywhere. What is new here is a checked parameter-cell propagation procedure and a continuous region satisfying the precision target. Valid coarse coverage must not be confused with full-band accuracy.

## Low-frequency theorem

Use the same positive meanfree Neumann Laplacian L, fixed distributed source F=10(x+y), normalized J1 measure, continuum spectral floor4 and z=-omega²+2i gamma omega. Let nu be the positive source spectral measure. The static certificate gives

$$S_0=H(0)\in[\underline S,\overline S]
=[1.123043,1.206865].$$

Set c=(underline S+overline S)/2=1.164954 and r=(overline S-underline S)/2=0.041911. For |omega|<=d<2 and0<gamma<=g,

$$H(z)-H(0)=-z\int\frac{d\nu(\lambda)}{\lambda(\lambda+z)}.$$

Since lambda>=4 and Re(lambda+z)>=lambda-d²>0,

$$|\lambda+z|\ge\lambda-d^2\ge4-d^2.$$

Also |z|<=d sqrt(d²+4g²). Hence

$$|H(z)-c|\le
r+\frac{\overline S\,d\sqrt{d^2+4g^2}}{4-d^2}.$$

Let delta_c be the exact upper bound on rounding c to its recorded binary64 value. A sufficient condition for the reported proxy to meet epsilon=1/10 is

$$\overline S^2d^2(d^2+4g^2)
\le(\epsilon-r-\delta_c)^2(4-d^2)^2.$$

Every quantity is nonnegative on the stated domain, so squaring is equivalent to the sufficient inequality; no sign ambiguity is introduced. The checker uses exact fractions for this decision and an upward square root for the final radius. The variation numerator increases and its positive denominator decreases as d increases below2, so the passing set is an interval. A rational bisection identifies the largest10^-6-grid d passing this particular sufficient test; the next grid value fails the test. This is **not** a physical frequency cutoff or a proof that the actual error exceeds1/10 beyond that point.

Applying the bound at the maximum damping of each closed interval yields:

|gamma interval|certified absolute omega upper|
|---|---:|
|[0.10,0.15]|0.381951|
|[0.15,0.20]|0.350759|
|[0.20,0.25]|0.317026|
|[0.25,0.30]|0.284149|
|[0.30,0.40]|0.228396|
|[0.40,0.50]|0.187564|
|[0.50,0.60]|0.158072|
|[0.60,0.80]|0.119566|
|[0.80,1.00]|0.095932|

All nine final reported-proxy radii are at most1/10. The worst-damping bound applies to the entire damping range [1/10,1], establishing the boxed uniform strip. Wider strips require their stated damping restrictions.

## Resolvent propagation from an anchor

For a certified anchor z0, let H(z0) lie in a disk centered at h0 of radius R0, and let

$$Q_0\ge\|(L+z_0)^{-1}F\|_{L^2}^2.$$

The fixed-source resolvent identity and Cauchy-Schwarz give

$$|H(z)-H(z_0)|\le|z-z_0|\sqrt{Q(z)Q_0}.$$

For the declared damping range, lambda>=4 and gamma>=1/10 imply the prior denominator bound

$$|\lambda-\omega^2+2i\gamma\omega|^2\ge\frac{399}{2500}=:D_*^2.$$

One proof is the completed-square identity, with t=omega²,

$$(\lambda-t)^2+\frac t{25}
=(t-\lambda+1/50)^2+\frac{\lambda-4}{25}+\frac{399}{2500}.$$

Because ||F||L2²=20, Q(z)<=20/D_*². Therefore every z with |z-z0|<=Delta obeys

$$|H(z)-h_0|\le R_0+\Delta\sqrt{\frac{20Q_0}{D_*^2}}.$$

This is an analytic neighborhood bound, not interpolation inferred from adjacent numerical samples. It remains conservative when an anchor is inaccurate.

For a nonnegative-frequency rectangle [a,b]x[g_a,g_b] and anchor(omega0,gamma0), coordinate monotonicity gives

$$\Delta^2=\max\{(a^2-\omega_0^2)^2,(b^2-\omega_0^2)^2\}
+\max\{(2g_a a-2\gamma_0\omega_0)^2,
(2g_b b-2\gamma_0\omega_0)^2\}.$$

The two coordinate maxima need not occur at the same corner; their sum is a safe upper bound. All four actual corner distances are checked, while monotonic coordinate ranges justify the full interior. The formulas require the stated nonnegative frequency cells; negative cells are obtained by conjugation.

## Certified anchor norms

The zero-frequency anchor uses h0=c, R0=r and Q0<=overline S/4 from lambda>=4. Its value is independent of damping at omega0=0.

The three dynamic anchors are the merged PR230 certificates at omega4,4.5,5 and gamma1/10. Their exact rational corrected-output centers and radii are recovered from the prior certificates, without treating floating evaluation error as a physical residual. For b0=2gamma0 omega0>0,

$$Q_0=-\frac{\operatorname{Im}H(z_0)}{b_0}.$$

The prior outer polygon supplies a rigorous lower bound on Im H, so its lowest vertex gives an upper bound on Q0. This uses the actual continuum anchor enclosure; no discrete eigenvalue or exact numerical output is substituted for H.

The cell checker compares all four propagated disks and the prior global gain disk |H|<=1000/sqrt399. It retains the smallest certified radius and adds the exact binary64 rounding bound for its selected rational center. Choosing between valid enclosures does not require proof of optimizer optimality.

## Continuous partition and results

The damping intervals in the table partition [1/10,1]. In each interval, the first frequency cell is its certified low-frequency strip. The remaining interval up to6 is partitioned using quarter-frequency grid endpoints, starting exactly at the strip boundary. Exact endpoint comparisons verify no missing intervals or unintended interior overlap. Shared closed-cell boundaries are harmless.

The result contains:

- 221 positive-frequency cells, covering the entire declared positive rectangle;
- 9 cells passing the1/10 target by the static spectral-variation theorem;
- 92 cells using anchor-resolvent propagation, currently too wide for1/10;
- 120 cells retaining the prior global gain disk, also too wide for1/10.

For negative frequency, H(-omega,gamma)=conj H(omega,gamma) follows from real L and F. Conjugating the centers preserves all radii and gives coverage of [-6,0]. Thus the enclosures cover the full band, but **full-band1/10 precision is false for the recorded certificate set**. This is a failure to certify precision, not proof that the actual approximations are inaccurate.

The largest coarse radius is the upward bound on1000/sqrt399, about50.0626174. The nine passing strips occupy a small part of the parameter rectangle. No probability or physical frequency-distribution interpretation is assigned to that area.

## Audit and replay

`INPUT_SOLVES.json` is byte-identical to PR230's input solve certificate, and `INPUT_ENCLOSURES.json` is byte-identical to PR230's exact moment-polygon certificate. Their hash linkage is checked. No new floating PDE solve or experiment is performed.

The standard-library checker uses Fraction arithmetic and upward square-root bounds for every propagated radius. Each selected output center has a stored binary64 hex representation; its exact decoded distance from the rational center is added to the certificate. All cell endpoints and flags are reproducible.

Controls reject a deliberately missing cell, a zero-damping out-of-scope rectangle and the next microstep above each sufficient low-frequency threshold. The completed-square coefficient checks, all anchor corner distances, source hashes, whole partition and each passing precision inequality are checked. Captured read-only replay compares the full result without writes.

```sh
python3 band_check.py .
```

Exact construction checks are not independent review. The proof does not establish convergence of the prior hierarchical flux estimator, preservation of later solver tolerances, a stopping-termination theorem or native constitutive dynamics.

The attached coefficient ledger's incidence/support operators remain distinct from the externally declared scalar-wave benchmark. The CRL2 subdivision attachment remains a governance proposal; no authority or registry status is silently advanced. The unavailable image Gap2_FINAL_Finite_Genesis.png was not read or used; reupload was requested. Uploaded source bytes are preserved.

Project218 remains In review / Scientific OPEN / Constructor checked / Development. The saved/reloaded next gate asks for independent review, extension of the precision strips into resonance using refined/dual solves, full-band accuracy, stopping termination and the native UD action bridge. Screenshot and receipt accompany this capture. Physical promotion remains0.
