# J1 local hierarchical flux and continuum spectral output bound

Status: **DERIVED / EXACT CONDITIONAL**, with four audited numerical witnesses. Constructor verification only; physical promotion **0**. Refs #218 and #136; extends PR223/225/226 without changing prior evidence. PR226 passed CI and merged at `a7148c31d847c3d091f54eac05e41a82d509bac7` before this capture.

## Result and limitations

A conforming 30-node/64-tetrahedron interior enrichment now has an explicitly equilibrated RT1 flux assembled from one parent solve and16 separate local patch solves. At the four sampled frequencies, the flux estimators improve over the14-node mesh. A spectral argument replaces the earlier `B/beta²` output factor by a smaller factor kappa. The improved resonance intervals remain too wide for meaningful spectral accuracy. This is a conditional scalar-wave benchmark, not a derivation of a native UD law, horn gain, topological damping, GR/QFT correspondence, or physical realization.

The barycenter subdivision preserves all parent faces and edges. Its maximum cell diameter remains unchanged. Repeating this operation alone is **not** the h->0 refinement family required by the prior continuum-convergence theorem. No convergence rate or explicit mesh-to-tolerance constant is promoted.

## Fixed continuum model

Use the same normalized J1 domain, meanfree H1 space V, normalized volume measure mu(Omega)=2, and distributed source/readout F=10(x+y). The V norm is the gradient norm. The nonnegative self-adjoint meanfree Neumann Laplacian L has compact resolvent and eigenvalues lambda_j>=4, using the convex-domain Poincare bound pi²/2>4. Damping gamma>0 is externally declared. Set z=-omega²+2i gamma omega and solve (L+z)u=F. The physical time normalization is tau=ct/a; no dimensional material calibration is supplied.

For a real eigenbasis, use complex-symmetric bilinear b_z(w,v)=integral(grad w dot grad v+z w v)dmu and linear ell(v)=integral Fv dmu. For any conforming meanfree v, including an inexact computed field, define

$$J(v)=2\ell(v)-b_z(v,v),\quad e=u-v,\quad r=F-(L+z)v.$$

Symmetry gives the exact identity H-J(v)=b_z(e,e). This does not require discrete Galerkin orthogonality. In eigen-coordinates,

$$H-J(v)=\sum_j\frac{r_j^2}{\lambda_j+z},\qquad
\|r\|_{V'}^2=\sum_j\frac{|r_j|^2}{\lambda_j}.$$

The square in the first expression is an ordinary complex square; the second uses absolute squares. Consequently,

$$|H-J(v)|\le\kappa(\omega,\gamma)\|r\|_{V'}^2,
\quad \kappa=\sup_{\lambda\ge4}\frac{\lambda}{\sqrt{(\lambda-\omega^2)^2+4\gamma^2\omega^2}}.$$

An H(div) flux with zero exterior normal trace and divergence z v-F gives r(w)=integral(tau-grad v) dot grad w dmu and hence ||r||V'<=eta=||tau-grad v||L2. Thus the **corrected output certificate is kappa eta²**. The recorded floating corrected-output evaluation error is added separately. The raw output also adds |ell(v)-b_z(v,v)| and its own evaluation error.

## Sharp factor for the declared continuum gap

Put t=omega² and d=4gamma²>0. For t>0 the unconstrained maximizing lambda is t+d; at t=0 the ratio is identically1. Therefore

$$\kappa^2=\begin{cases}
\dfrac{16}{(4-t)^2+dt},&t+d<4,\\
\dfrac{t+d}{d},&t+d\ge4.
\end{cases}$$

This is sharp over **all real lambda>=4**, not a computed exact norm for the actual J1 spectrum. Two coefficient identities prove the majorant without spectral sampling. With a general lower bound L0>0 and D(lambda)=(lambda-t)²+dt:

$$(t+d)D(\lambda)-d\lambda^2=t(\lambda-t-d)^2;$$

$$L_0^2D(\lambda)-\lambda^2D(L_0)
=t(\lambda-L_0)[(2L_0-t-d)\lambda-L_0(t+d)].$$

The second right side is nonnegative when lambda>=L0>t+d. `spectral_check.py` checks both polynomial identities exactly over the rational coefficient ring, plus seven maximizer/boundary fixtures and deliberate half-factor rejections. On |omega|<=6 and gamma in[1/10,1], kappa<=sqrt(901). This replaces the old band factor B*/beta*²=11713. It does not make eta small or certify precise resonance locations.

## Local flux construction

The16-tet parent mesh is split at each cell barycenter into four children, preserving conformity. Exact determinant volumes are1/32 in normalized measure per child. Exact stiffness/mass/source pullback identities confirm that the parent P1 space and distributed port embed unchanged.

On parent T, write v=v_l+delta w, where v_l interpolates the four parent vertices and w is1 at the barycenter and0 at the corners. Exact local moments give the parent L2 projection Pi_1 w=1/4. The code checks the moment identities. The parent flux has divergence z(v_l+delta/4)-F, zero exterior trace and continuous normal trace. Its240 coefficients satisfy196 constraints of rank195, leaving45 proposal variables.

Each four-child patch adds a flux with divergence z delta(w-1/4), zero normal trace on the parent boundary and continuous child-interface trace. A unit particular solution and nullspace are reconstructed exactly from46 constraints of rank45 on60 coefficients, leaving15 proposal variables. Parent flux coefficients are repeated onto the children in the same global polynomial basis. Separate floating minimum-norm proposals choose the free variables; exact reconstruction imposes all constraints afterwards. The final960 coefficients are audited directly against676 assembled constraints for both real and imaginary parts at all four fixtures: **5408 scalar exact flux checks**. This final check is independent of the hierarchical constraint assembly, but remains constructor verification.

Local minimization is separate per patch after the parent solve. This is neither a global960-variable optimizer nor an adaptive element-selection algorithm. Floating proposal optimality is not required for validity and is not asserted exactly.

## Witness results

All entries below are readable approximations; RESULTS.json stores exact rationals and outward bounds. gamma=1/10 throughout. The output radius applies to H around the reported corrected output, with the tiny recorded evaluation error also included in the machine result.

| omega | prior eta² (16 cells) | current eta² (64 cells) | current corrected-output error radius |
|---|---:|---:|---:|
|0|0.193326|0.178437|0.178437|
|4|5.734706|5.684336|113.828731|
|4.5|51.763529|40.022444|901.393929|
|5|2.313663|2.007284|50.222240|

The last-column rounded display is informational; the exact rational upper bounds are authoritative. At omega4.5 the prior mesh/old-factor bound was about165091, so both the flux and factor improve. A radius901 around a response of order15 remains scientifically loose.

The exact static energy identity, valid for any real v, gives the outward continuum bracket

$$\boxed{1.030380\le H(0)\le1.208818}.$$

This improves the previous[1.022727,1.216053] bracket. The worst end-to-end **algebraic** raw-output error bound is3.012035e-12, below the declared1e-10 budget. This is distinct from the much larger continuum discretization radius.

## Verification and replay

- 5437 exact checks in the main replay, including5408 flux constraints; exact nested matrices/source, geometric volumes, projection moments and output algebraic budget checks.
- Three expected rejection controls: under-solved zero state, nonfinite input, and truncated flux proposal.
- Two exact spectral coefficient identities and seven maximizer fixtures.
- Stored coefficients and reported outputs are decoded from binary64 hex; all posterior inequalities use Fraction arithmetic with upward square-root rounding. Backend is measured NumPy2.3.5/Python as recorded in WITNESS.json. Audit does not need NumPy; generation does.

Run from this capture directory:

```sh
python3 patch_flux.py .
python3 spectral_check.py
python3 patch_controls.py WITNESS.json patch_flux.py
```

The main replay checks existing RESULTS.json without rewriting it and disables bytecode before importing the helper. Negative controls use isolated temporary directories. `--generate` is for a new unpublished output directory; never regenerate into frozen captures. No all-input IEEE rounding theorem is claimed.

## Project state and remaining work

Project1 issue218 remains In review / Scientific OPEN / Constructor checked / Development. The saved next gate requests independent review, adaptive refinement to tighten resonance intervals, a certified mesh family, and the native UD action bridge. Proof is in PROJECT_RECEIPT.json and PROJECT_IN_REVIEW.jpg. Prior records are preserved; no authoritative scientific registry promotion occurs.

Next substantive work is an h-reducing conforming mesh hierarchy with error-driven refinement, ideally combined with a certified lower spectral enclosure above4 or an output-specific dual certificate. The local flux architecture is now implemented for the finite enrichment. A quantitative polyhedral regularity/interpolation constant remains open; edge dihedral angles alone do not determine the full3D vertex regularity problem. Native action/source/units selection, external calibration and independent review remain separate gates.
