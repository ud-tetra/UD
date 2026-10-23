# Lateral coverage of the published DFT archive and a finite-probe limit

**Development — no registry entry. Physical promotion 0.** Read-only audit of six publicly archived Quantum ESPRESSO input sets, followed by an exact conditional algebraic counterexample. No new DFT calculation, force trace, material coefficient or UD-specific loss was inferred.

## What the six archives actually cover

The first-carbon relative upper-minus-lower Cartesian coordinate supplies a common rigid lateral marker. Take the archived AB reference $(0,-1.0762682221329958)$ Å, scan tangent $t=(\sqrt3/2,1/2)$ and normal $n=(1/2,-\sqrt3/2)$. SHA-check each of the six source tarballs before reading `struct.in` and, when available, QE XML `output/atomic_structure/atomic_positions`. The XML coordinates are in Bohr; the audit converts them with 0.529177210903 Å/Bohr. **It does not execute archived scripts.**

| Archive (prefix `qe-21-vdw-df3-`) | Input structures | XML structures | Tangent displacement from AB (Å) | Largest normal displacement (Å, input/XML) |
| --- | ---: | ---: | ---: | ---: |
| `3.4022A-h30A` | 37 | 37 | 0 to 1.614402 | $4.96\times10^{-16}$ / $8.88\times10^{-16}$ |
| `3.34A-h30A` | 37 | 37 | 0 to 1.614402 | $4.96\times10^{-16}$ / $8.88\times10^{-16}$ |
| `ab` | 31 | 31 | 0 | $4.96\times10^{-16}$ / $1.92\times10^{-16}$ |
| `aa` | 31 | 31 | +0.538134 | $3.89\times10^{-16}$ / $5.83\times10^{-16}$ |
| `sp` | 31 | 31 | −0.269067 | $4.02\times10^{-16}$ / $3.89\times10^{-16}$ |
| `opt-dist` | 83 | 54 | 0 | $4.96\times10^{-16}$ / $1.92\times10^{-16}$ |

Total: 250 archived input geometries, 221 XML geometries (29 `opt-dist` inputs without corresponding XML in this archive). Every checked lateral marker is collinear with the original high-symmetry scan to floating precision. The `sp` set samples the extension on the negative tangent, not an independent transverse direction. Thus these six archives do not supply a transverse energy difference or Hessian. This conclusion is scoped to the enumerated SHA-checked archives; it does not assert that no other calculations exist. `ARCHIVE_COVERAGE_RESULTS.json` contains source digests, counts and projections; `audit_archive_lateral_coverage.py` reproduces them against the source tarballs.

## Exact finite-probe nullspace

The preceding v8 protocol proposes central and $\pm0.04,\pm0.08$ Å energies at the line index-30 saddle. It is valuable: a *negative* symmetric contrast at a tested displacement establishes an off-line energy decrease there, and a result can reject a specified first-shell-plus-one-parameter alternative. But even exact energies and exact forces at those five positions do not uniquely fix the infinitesimal transverse Hessian if arbitrary symmetry-allowed higher harmonics remain possible.

Write $f(u,v)=2\cos v\cos u+\cos2v$, $F(u,v)=(1-\cos(u-3v))(1-\cos(u+3v))(1-\cos2u)$ as in the preceding line-nullspace result. The archived line obeys $u=3t$, $v=2\pi/3+t$, so $F=0$ throughout. At its index-30 saddle $s=(5\pi/2,3\pi/2)$, $f(s)=f_0=-1$. Along the physical normal $n$ at displacement $h$, set $\beta(h)=\sqrt3 k_yh$ and $f_h=f_0+4\sin^2[\beta(h)/2]$. Define

$$
G(u,v)=F(u,v)\prod_{h_j\in\{0.04\,{\rm Å},0.08\,{\rm Å}\}}
\left[\frac{f(u,v)-f_{h_j}}{f_0-f_{h_j}}\right]^2.
$$

Every factor is a periodic sixfold-invariant scalar; $G$ retains the PES translations and point symmetry. It vanishes along the **entire** old scan because $F=0$. At $s\pm h_jn$, its factor for $h_j$ vanishes *quadratically*, so both $G$ and its full gradient vanish. At $s$, $F$ has a quadratic zero and the product of normalized factors equals one; consequently $G(s)=0$, its gradient vanishes and its transverse Hessian equals that of $F$:

$$
\partial_n^2 G(s)=48k_y^2.
$$

At AB, $F$ vanishes to sixth order, and the normalized factors are finite, so the original AB Hessian is also unaffected. Therefore $U_1f+\varepsilon G$ matches the entire old scan **and the five proposed energy/force probes** for any $\varepsilon$, yet its saddle transverse curvature is $k_y^2(6U_1+48\varepsilon)$, which changes sign at $\varepsilon/U_1=-1/8$. This is an exact non-identifiability construction; it is deliberately high harmonic and is **not** a plausible fitted graphite potential without independent material evidence. The verifier checks cancellation, numerical derivatives and the analytic Hessian factor.

**Quantitative two-step limit.** For a per-upper-atom normal energy $E(h)$ that is $C^6$ on $[-0.08,0.08]$ Å, set $k(h)=D(h)/h^2$ and $\widehat\kappa=[b^2k(a)-a^2k(b)]/(b^2-a^2)$ with $a=0.04$, $b=0.08$ Å. If $|E^{(6)}(h)|\le M_6$ throughout that interval, Taylor's theorem gives a truncation bound

$$
|\widehat\kappa-E''(0)|\le \frac{M_6}{360}\,
\frac{b^2a^4+a^2b^4}{b^2-a^2}
=4.7407407\times10^{-8}\,M_6\ {\rm Å}^4.
$$

The numerical coefficient multiplies $M_6$ in μeV per upper atom Å$^{-6}$ to yield μeV per upper atom Å$^{-2}$. No bound on $M_6$ is supplied by the line archive; the exact $G$ construction demonstrates why such a bound matters. If the five independently recalculated per-atom energies each have standard uncertainty $\sigma_E$, then $\widehat\kappa=\alpha D(a)+\beta D(b)$ has $\alpha=833.3333$ Å$^{-2}$, $\beta=-52.08333$ Å$^{-2}$, $\operatorname{Cov}[D(a),D(b)]=4\sigma_E^2$ through the shared center, and $\sigma_{\widehat\kappa}=1958.50\,\sigma_E$ Å$^{-2}$. At the *hypothetical* $\sigma_E=0.001$ μeV per atom, that is $1.9585$ μeV Å$^{-2}$ per atom: the illustrative $\widehat\kappa=-4.2562$ is only 2.17 standard deviations from zero **before** truncation/systematic error. The 5.20-standard-deviation negative finite-step contrast at 0.08 Å in v8 must not be described as a 5σ local-Hessian determination.

## Decision gate for the graphite paper

1. Keep the v8 ±0.04/±0.08 Å calculation as a **discriminating finite-step test** of its named first-shell and $F$ alternatives. A negative contrast directly invalidates a transverse local-minimum claim over that finite step, subject to energy-difference uncertainty. A positive contrast rejects the illustrative negative-$\varepsilon F$ forecast at those positions if the numerical difference is resolved.
2. For a **local Hessian claim**, predeclare a controlled Fourier cutoff or an independent bound on the fourth and higher normal derivatives, then report a step-convergence sequence with error and covariance. The two-step $h^2$ extrapolation in v8 is an estimator under that regularity assumption, not an exact certificate from five points.
3. For a **two-dimensional barrier or load prediction**, validate the selected PES against off-line positions away from a single normal and under more than one separation/pressure. No finite unbounded-harmonic sample set gives a unique global minimax path; a material model and its validation domain are required.
4. Only after this conventional static baseline is bounded should pressure-resolved loss measurements and a source-fixed UD rule be compared to held-out kinetic force data. Neither the angle pairing nor a fitted static correction is itself a UD residual.

**Status:** EXACT conditional algebraic no-go for finite-probe uniqueness; NUMERICAL read-only six-archive coverage and analytic-check replay; OPEN actual higher harmonics, normal-force uncertainty, open-system damping, and kinetic friction. Constructor verification is not independent review.
