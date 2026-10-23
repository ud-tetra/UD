# What a high-symmetry graphite scan does not determine

**Development — no registry entry. Physical promotion 0.** This is an exact symmetry counterexample with a separate numerical minimax illustration. It is not a proposed graphite interaction or a UD coefficient.

## Source and issue

The original vdW-DF3 authors fit a first Fourier shell to one 37-point high-symmetry line of the $(2,1)$ lateral PES and use that **two-dimensional first-shell model** to estimate ideal static shear strength along a minimum-energy path [Lebedeva et al., arXiv:2511.01338, Eq. 2 and Table 5](https://arxiv.org/abs/2511.01338). Our earlier capture replayed two complete 37-point scans and found the fit close, with RMS residuals of 1.65% and 1.21% of the respective observed peaks. Those small on-line residuals do not independently constrain the energy transverse to the measured line.

The line contains both the AA excursion and a lower saddle segment. The raw 3.4022 Å energies rise by approximately 0.04670 μeV/upper atom from index 24 to index 30; at 3.34 Å the corresponding sampled rise is approximately 0.10335 μeV/upper atom. The first-harmonic minimum-energy-path barrier is $U_1/2$, or 0.03967 and 0.08347 μeV/upper atom, respectively. The direct saddle differences have small absolute discrepancies but relatively large fractions of those tiny barriers. The line includes a candidate minimum-energy segment; its energies alone do not verify transverse stability.

## Explicit periodic symmetry-compatible nullspace

Use the original first-shell phase coordinates $u=k_x x'$, $v=k_y y'$ with $k_x=\sqrt3 k_y$. Express energy in units of the fitted $U_1>0$:

$$
f(u,v)=2\cos v\cos u+\cos 2v,\qquad
F(u,v)=\bigl[1-\cos(u-3v)\bigr]\bigl[1-\cos(u+3v)\bigr]\bigl[1-\cos 2u\bigr].
$$

The perturbation also equals $[\cos u-\cos 3v]^2[1-\cos 2u]\geq0$. The three wavevectors $(k_x,-3k_y)$, $(k_x,3k_y)$ and $(-2k_x,0)$ form a rotation orbit of allowed reciprocal vectors. Thus $F$ is periodic under the PES translations $(u,v)\mapsto(u+2\pi,v)$ and $(u,v)\mapsto(u+\pi,v+\pi)$, invariant under $120^\circ$ rotation and inversion (and hence the generated sixfold point action). It adds higher reciprocal-shell content while respecting those symmetries.

The archive's entire straight scan is $u=3t$, $v=2\pi/3+t$, $0\leq t\leq\pi$. There $u-3v=-2\pi$, so **$F=0$ for every point on the full line**, not merely the 37 samples. Its tangential derivatives also vanish. Near an AB minimum $F$ vanishes to sixth order, leaving the local first-shell Hessian unchanged. Therefore $U_1 f+\varepsilon F$ gives the same line profile, fit coefficient and local AB curvature for every $\varepsilon$.

At the line's first-shell saddle (index 30), the transverse curvature in physical coordinates is

$$
\left.\partial_n^2(U_1f+\varepsilon F)\right|_{\rm saddle}
   = k_y^2\,[6U_1+48\varepsilon].
$$

For $\varepsilon/U_1<-1/8$ the transverse curvature switches sign, although all measured line values remain identical. This **exact** sign change establishes that the scan plus the specified symmetry cannot certify the saddle's transverse stability or the two-dimensional path.

## Numerical illustration and scope

For $\varepsilon=-0.2U_1$, a periodic eight-neighbor grid minimax search between adjacent AB minima changes the barrier from $0.50000U_1$ (first shell) to $0.43033U_1$ at a $960\times960$ grid. Results converge across grids of 120, 240, 480 and 960; every sampled grid retains minimum energy $-1.5U_1$ at AB. At the 3.4022 Å fitted amplitude, those model barriers are about 0.03967 and 0.03414 μeV/upper atom. **The grid search is an illustration**, not a continuum proof, DFT prediction or fitted second-shell correction. The exact result is the identical line profile with different off-line transverse curvature; one-dimensional data cannot select $\varepsilon$.

The static-strength ratio 2.104 reported in the prior capture is valid **within the two-dimensional first-harmonic model**, whose amplitudes were fit to the data. It is not uniquely inferred from the 37-point scans and symmetry alone. A two-dimensional energy grid, off-line forces/curvatures, or an independently validated microscopic PES must supply the omitted information before the minimum-energy path and any higher-harmonic correction can be determined. Kinetic friction and UD-specific damping require further dynamical measurements.

## Replay and provenance

The script verify_2d_line_nullspace.py checks exact-line cancellation numerically at all 37 positions, period and point symmetry at test coordinates, the analytic transverse threshold, and the converging grid minimax example. LINE_NULLSPACE_RESULTS.json records its values. The first-shell coefficient comes from the previous full-profile capture. **Status:** EXACT algebraic counterexample; NUMERICAL minimax illustration; NO-GO for identifying a general two-dimensional PES from this single line; OPEN actual material higher harmonics and kinetic response.
