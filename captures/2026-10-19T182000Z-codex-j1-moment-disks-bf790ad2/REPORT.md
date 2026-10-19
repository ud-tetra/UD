# J1 continuum moment disks and explicit output acceptance test

**DERIVED / EXACT CONDITIONAL.** Exact enclosure construction passes; dynamic accuracy target remains **OPEN**. Development — no registry entry. Constructor verification only; physical promotion **0**. Refs #218 #136; append-only extension of PR223/225/226/228/229. PR229 passed CI and merged at `88b76a35e741f9a5da786effd9a38d6cc80e6b53` before this capture.

## Outcome

The same fixed-port scalar-wave model now has stronger output enclosures from continuum passivity and source moments. Intersecting these with the existing flux certificate reduces the certified reported corrected-output radius at omega4 from168.9371 to23.4963 and at omega4.5 from77.9723 to21.5641. Omega5 retains the previous12.3891 radius because the moment polygon is looser there. These are rigorous necessary-condition enclosures under the declared model, not accurate resonance measurements.

The **constructor-set audit target** is absolute output error1/10 in the declared dimensionless normalization. It is a computational acceptance target, not an experimental preregistration, user-specified physical tolerance or independently reviewed standard. The static sample meets it; all three dynamic samples fail. A sufficient uniform stopping test is derived below, but entire-band coverage and algorithm termination remain unproved.

This return does not perform a new floating solve. INPUT_RESULTS.json is byte-identical to the merged PR229 posterior certificate; its source hash is checked and recorded. The new operations are exact rational transformations of those certified bounds and analytic continuum identities.

## Continuum prerequisites and moments

Let L be the positive meanfree Neumann Laplacian for the same normalized J1 domain, gradient norm and volume measure. Source and readout are the fixed distributed F=10(x+y). Retain the continuum lower bound lambda>=4 from the convex Poincare theorem. Let

$$z=-t+ib,\quad t=\omega^2,\quad b=2\gamma\omega>0,\quad
H=\langle F,(L+z)^{-1}F\rangle=x+iy.$$

For positive frequencies the positive source spectral measure nu satisfies

$$H=\int_{[4,\infty)}\frac{d\nu(\lambda)}{\lambda-t+ib},\quad
m=\int d\nu=20,\quad M=\int\lambda\,d\nu=400.$$

The mass m is ||F||L2²=20. The first moment M is ||grad F||L2²=200 mu(Omega)=400. F belongs to the form domain, which suffices for this first moment; no second spectral moment or Neumann boundary condition on F is assumed. The static certificate gives

$$S_0=H(0)=\int\lambda^{-1}d\nu\le\overline S=\frac{241373}{200000}=1.206865.$$

The PDE energy identity gives

$$y=-b\|(L+z)^{-1}F\|_{L^2}^2\le0,\quad
E=x-\frac tb y=\|(L+z)^{-1}F\|_V^2.$$

All these are conditional continuum-model quantities. No finite-element eigenvalue, empirical fit, native UD constitutive law or topological damping identification enters the argument.

## Four continuum disks

**Source mass.** Cauchy-Schwarz in L2 gives

$$|H|^2\le-\frac mb y.$$

This is the disk centered at -im/(2b), radius m/(2b).

**Static energy.** Cauchy-Schwarz in the energy space gives

$$|H|^2\le\overline S\left(x-\frac tb y\right).$$

Its center is overline S(1-it/b)/2 and its squared radius is overline S²(1+t²/b²)/4.

**Gap-weighted first moment.** Put L0=4 and A=M-L0 m=320. Positivity of lambda-L0 and weighted Cauchy-Schwarz give

$$|m-(z+L_0)H|^2\le A\left(x-\frac{t-L_0}{b}y\right).$$

With d=(t-L0)²+b², its center is

$$c_x=\frac{A-2m(t-L_0)}{2d},\qquad
c_y=-\frac{2mb+A(t-L_0)/b}{2d},$$

and its squared radius is c_x²+c_y²-m²/d. The spectral gap also yields the half-plane x-(t-L0)y/b>=0.

**Joint energy Gram disk.** In the energy Hilbert space, use the two vectors u0=L^-1F and F. Their Gram matrix is [[S0,m],[m,M]]. Their inner products with u=(L+z)^-1F are H and m-zH. The full three-vector Gram matrix is positive semidefinite. Replacing S0 by its upper bound preserves that property. The leading2x2 block is positive definite because

$$\Delta=\overline S M-m^2>0.$$

Its Schur complement therefore gives

$$M|H|^2-2m\operatorname{Re}[\overline H(m-zH)]
+\overline S|m-zH|^2\le\Delta E.$$

This proof remains valid even if the actual two-vector Gram matrix is singular. Define

$$C=M-2mt+\overline S(t^2+b^2)
=\overline S[(t-m/\overline S)^2+b^2]+M-m^2/\overline S>0.$$

The resulting disk has center

$$c_x=\frac{\Delta+2m^2-2\overline Smt}{2C},\qquad
c_y=-\frac{2\overline Smb+\Delta t/b}{2C},$$

and squared radius c_x²+c_y²-overline S m²/C.

`moment_identities.py` verifies three generic polynomial coefficient identities exactly over Q[m,M,S,t,b,x,y,L]: the complex norm expansion, gap-weighted disk numerator and joint Gram numerator. These are algebra checks; positivity and model prerequisites are supplied by the preceding argument, not by fixture sampling.

## Combining the disks with the flux certificate

For the stored conforming field v, the corrected output is J(v)=2ell(v)-b_z(v,v). PR229 certifies

$$|H-J(v)|\le\kappa\eta^2,$$

with the continuum spectral factor kappa and an exactly equilibrated RT1 flux estimator eta. This is a fifth disk, centered at the exact rational J(v). It remains valid for an inexact Galerkin solve; the stored evaluation-error bound separately covers the actual reported floating output.

For each disk center c and squared radius r², every integer direction n supplies the necessary half-plane

$$n\cdot H\le n\cdot c+\sqrt{r^2\|n\|^2}.$$

The code uses32 directions, rounds each square root upward on a10^-18 rational grid, and clips a source-mass bounding square using Fraction arithmetic. Passive sign and continuum-gap half-planes are also applied. The resulting polygon is an **outer approximation** of the disk intersection. No floating optimizer or dense spectral scan is used, and polygon facets are not misidentified as exact arcs.

Every polygon vertex is checked against all162 rational half-planes. For a bounded convex polygon, the maximum distance from a fixed center is attained at a vertex; convexity proves that its maximum vertex distance bounds all points. This gives a rational outward radius about J(v). The final exact bound takes the minimum of that radius and the prior posterior radius, then adds the recorded corrected-output evaluation error once. The raw-output certificate adds the already certified raw/corrected offset instead. Both reported-output conventions remain auditable.

At zero frequency, use the certified real static interval and the prior flux bound; no division by b occurs. Negative frequencies follow by H(-omega)=conj H(omega); three exact conjugation checks confirm identical radii for the stored fixtures. There is no claim that testing these fixtures establishes an entire-band maximum.

## Results and precision gate

Display values below are rounded approximations; RESULTS.json contains exact rational upper bounds. gamma=1/10 throughout. The bounds concern the reported corrected output; the raw-output certificates are also stored.

|omega|previous radius|combined radius|absolute1/10 target|
|---|---:|---:|---|
|0|0.0838211|0.0838211|PASS|
|4|168.9371|23.4963|FAIL|
|4.5|77.9723|21.5641|FAIL|
|5|12.3891|12.3891|FAIL|

The unchanged static continuum bracket is1.123043<=H(0)<=1.206865. The new enclosures do not locate a resonance or imply that the computed dynamic outputs are accurate to1/10. They narrow the conservative uncertainty region while explicitly retaining failed precision outcomes.

## Explicit acceptance threshold and stopping limits

Let epsilon=1/10 and let delta_eval be the certified corrected-output evaluation error. A sufficient pointwise test is

$$\eta^2\le\frac{\epsilon-\delta_{\rm eval}}{\kappa},\qquad
\delta_{\rm eval}\le\epsilon.$$

The polygon-based radius can also pass the same target independently if it is smaller. The script records both decisions rather than interpreting a mathematically valid large enclosure as a precision certificate.

For the entire declared band |omega|<=6, gamma in[1/10,1], kappa<=sqrt901. With evaluation allowance delta0=10^-10, a sufficient **uniform** condition is

$$\sup_{\rm band}\eta^2\le
\frac{1/10-10^{-10}}{\overline{\sqrt{901}}}
\approx0.00333148301993,\qquad
\sup_{\rm band}\delta_{\rm eval}\le10^{-10},$$

where the square-root bar denotes the exact rational upward bound in RESULTS.json. This is a sufficient stopping condition, not a proved termination theorem. It requires coverage of the continuous band; four samples cannot satisfy that coverage obligation. The earlier h->0 Galerkin theorem does not automatically imply decay of the chosen hierarchical flux estimator or automatic satisfaction of floating solve tolerances.

## Verification and source alignment

- Exact rational replay verifies all disk parameters, outward supports, clipping, vertex inequalities, distance bounds and unchanged source-certificate hash.
- Three formal generic polynomial identities pass.
- A two-atom source measure with weights10 at lambda12 and28 has mass20, energy400 and static moment25/21<=overline S. At all three dynamic frequencies it lies inside all four continuum disks exactly. It is a mathematical control measure, not the J1 spectrum or experimental data.
- Three rejection/gate controls: an active upper-half-plane transfer fails passivity; an inward square-root proposal is rejected; a25-unit valid envelope and a value just above1/10 fail the precision gate, while the boundary value is accepted.
- Three negative-frequency conjugation controls pass. Stored results replay without writes.

```sh
python3 moment_identities.py
python3 disk_check.py .
```

This checker uses only the Python standard library. INPUT_RESULTS.json reuses the already audited merged finite witnesses; it does not rerun their floating solve. Source hashes and lineage are in CONTRACT.json. Exact arithmetic validates the enclosure construction, not the physical model or an independent review.

The attached coefficient ledger's incidence/support results remain distinct from this externally declared scalar-wave action. The attached CRL2 subdivision amendment is still a governance proposal, not silently enacted policy. No registry or uploaded-source bytes are changed. Missing image Gap2_FINAL_Finite_Genesis.png was not read or used; reupload was requested.

Project218 remains In review / Scientific OPEN / Constructor checked / Development. Its next gate explicitly requests independent review, dynamic1/10 accuracy plus entire-band coverage, stopping termination and a native UD action bridge. Screenshot and saved/reloaded UI receipt accompany this capture. Physical promotion remains0.
