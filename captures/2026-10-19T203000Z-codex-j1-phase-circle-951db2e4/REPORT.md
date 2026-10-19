# J1 phase-aware quadratic output certificate

**DERIVED / EXACT CONDITIONAL.** Development — no registry entry. Constructor verification only; independent review outstanding; physical promotion **0**. Refs #218 and #136. Append-only extension of the fixed distributed-port scalar-wave benchmark. PR #236 passed capture-integrity CI and merged as `e02d5df67393d861470e2f863e65f7ed559db6ff`; its integration with concurrent main passed the repository verifier and had matching public/local tree `5ce1ae4c16b45a766ab2dd93f7b41468824cc4d2`.

## Result and scope

The existing equilibrated flux supplies more information than its Hermitian norm alone. Its exact complex bilinear square yields a new output center and a smaller guaranteed disk. At omega=4.5 the phase-circle radius is about **8.17868**, versus 16.35735 around the previous corrected output; at omega=5 it is **1.77815**, versus 3.55629. These radii refer to **different reported centers**. The old output bounds do not automatically halve.

At omega=4, the new phase-circle radius is 74.8495, so the inherited 23.4767 radius is retained. All dynamic selected disks still fail the 1/10 absolute-accuracy gate. A rational outer-polygon intersection was checked as an additional candidate; it improved neither the old-center radius nor the chosen disk in these fixtures.

No PDE solve, flux optimization, mesh refinement or hardware experiment is performed here. Frozen PR236 state, flux and result inputs are reused byte-identically. New work consists of exact mixed flux integration, covariance checks, a continuum output theorem and audited binary64 proxy centers.

## The continuum identity

Let A be the positive meanfree Neumann Laplacian on normalized J1, with real L2-orthonormal eigenfunctions phi_j, eigenvalues lambda_j>=4, and real orthonormal gradient fields

$$g_j=\frac{\nabla\phi_j}{\sqrt{\lambda_j}}.$$

The continuum gap floor 4 is inherited from the convex-domain Poincare bound; it is not a mesh eigenvalue. Let

$$z=-a+ib,\quad a=\omega^2,\quad b=2\gamma\omega,\quad \gamma>0.$$

For the frozen conforming state v and equilibrated physical flux tau, put d=tau-grad v. The exact conditions div tau=zv-F and tau.n=0 imply

$$r(w)=\ell(w)-b_z(v,w)=\int d\cdot\nabla w\,d\mu.$$

Set d_j=integral d dot g_j. The complex-symmetric corrected output J(v)=2ell(v)-b_z(v,v) obeys

$$H-J(v)=\sum_j\frac{\lambda_j}{\lambda_j+z}\,d_j^2.$$

Squares here are bilinear complex squares, without conjugation. The Hermitian error budget is

$$N=\|d\|_{L^2}^2=\eta^2.$$

Let T_z act by f_z(lambda)=lambda/(lambda+z) on each real gradient eigenfield, and by zero on the real orthogonal complement of their closed span. Then H-J(v)=integral d dot T_z d. This zero eigenvalue matters: the flux error may have a solenoidal component, which must remain in both the norm budget and the bilinear square.

## Spectral-circle theorem

For nonzero omega, define

$$c_z=\frac12-\frac{ia}{2b},\qquad
\delta_z^2=|c_z|^2=\frac{a^2+b^2}{4b^2}.$$

For every real lambda with lambda+z nonzero,

$$\left|\frac\lambda{\lambda-a+ib}-c_z\right|^2=\delta_z^2.$$

To verify the identity, multiply by 4b² times |lambda-a+ib|². Its numerator becomes

$$b^2\lambda^2+(a^2+b^2-a\lambda)^2
=(a^2+b^2)((\lambda-a)^2+b^2).$$

Also |0-c_z|=delta_z, so the same closed disk covers the solenoidal eigenvalue. Thus ||T_z-c_z I||<=delta_z. Define the exactly computable bilinear flux-error square

$$q=\int d\cdot d\,d\mu.$$

Cauchy-Schwarz and the normal spectral multiplier bound give

$$\boxed{|H-[J(v)+c_zq]|\le\delta_z N.}$$

At omega=0, choose c_0=1/2 and delta_0=1/2: T_0 is the real orthogonal gradient projection, with spectrum {0,1}. For the actual real static fixture this disk reduces to the midpoint/radius form of the prior static bracket J<=H<=J+N. It is a recentering of that certificate, not a new tightening of its interval.

For negative omega, z, c_z, q and the center conjugate, while N and delta remain unchanged. The implementation checks this symmetry on the recorded fixtures.

## Exact covariance construction

Write d=d_R+i d_I and record

$$D_R=\|d_R\|^2,\quad D_I=\|d_I\|^2,\quad C=\langle d_R,d_I\rangle.$$

Then N=D_R+D_I and q=D_R-D_I+2iC. The code checks D_R>=0, D_I>=0 and D_R D_I>=C², hence |q|<=N. The latter is a validity check, not a discarded complex phase.

The PR236 exact polynomial quadrature, affine maps, physical metric diag(1,1,1/2), state and flux coefficients are retained. Mixed flux products are added. Integration by parts gives

$$D_R=\|\tau_R\|^2+\|v_R\|_V^2-2a\|v_R\|^2-2b\langle v_R,v_I\rangle-2\ell(v_R),$$

$$D_I=\|\tau_I\|^2+\|v_I\|_V^2-2a\|v_I\|^2+2b\langle v_R,v_I\rangle,$$

$$C=\langle\tau_R,\tau_I\rangle+\langle\nabla v_R,\nabla v_I\rangle
-2a\langle v_R,v_I\rangle-b(\|v_I\|^2-\|v_R\|^2)-\ell(v_I).$$

All products are exact rational integrals of the decoded frozen coefficients. Their sum reproduces the prior eta² exactly. The inherited direct assembled divergence/trace audit, source/output identities and FLUX_RESULTS.json replay remain unchanged. `PR236_flux2.py` preserves the original audit source so the covariance-only extension in `phase_flux.py` is reviewable by diff.

## Reported centers and acceptance

The exact center J+cq is rounded to a recorded pair of binary64 hex words. Its Euclidean evaluation discrepancy is bounded by an outward rational square root and added once to delta*N. This is an actual frozen-proxy audit, not an all-input IEEE implementation theorem. New proxy values do not replace the stored raw or corrected FEM output records.

|omega, gamma=1/10|selected reported center, approximate|selected certified radius|method|1/10 gate|
|---|---|---:|---|---|
|0|1.190866726110414 + 0i|0.0151442611|phase circle|PASS|
|4|12.284942625176583 - 12.862627136256403i|23.4767331|inherited disk|FAIL|
|4.5|-1.0621157918589583 - 8.36649467970336i|8.1786766|phase circle|FAIL|
|5|-1.872157438067351 - 1.997771905281516i|1.7781474|phase circle|FAIL|

Exact fractions and reported hex words govern, not the display decimals. A failed gate means the certificate is too wide; it does not establish actual physical or numerical error above the target. The selected proxies satisfy the exact passive-sign test -omega Im(center)>=0 in these fixtures; no universal passivity of the phase-circle center is claimed.

At each dynamic sample, the old guaranteed disk is intersected with the new one using 32 rational outward halfplanes per disk. Convex clipping is exact. Every final polygon vertex is checked against every halfplane. Bounding the polygon about its bounding-box midpoint gives an additional candidate output disk; bounding it about the old reported center checks whether the old output can be certified more tightly. Neither improves the selected values here. Disk-intersection consistency is not used as a substitute for proving either input disk.

## Band stopping bound and a sharpness limit

For |omega|<=6 and gamma>=1/10,

$$\delta_z=\frac12\sqrt{1+\frac{\omega^2}{4\gamma^2}}
\le\frac{\sqrt{901}}2.$$

Thus a sufficient uniform 1/10 rule for the new proxy, with uniform evaluation budget epsilon_eval<=10^-10, is

$$\boxed{\sup_{\rm band}\eta^2
\le\frac{2(1/10-10^{-10})}{\sqrt{901}}
\approx0.00666296604.}$$

This doubles the sufficient eta² budget relative to the prior origin-centered quadratic enclosure. It does not establish uniform residual control, frequency coverage, a mesh rate or termination. Only four frozen frequency fixtures are evaluated. In particular, the dynamic fixtures have not met their pointwise thresholds.

When a=omega²>=4, the circle factor is minimax sharp among scalar shifts covering the abstract symbols {0} union {lambda/(lambda+z):lambda>=4}. The admissible value at lambda=a is -ia/b, and the limit as lambda tends to infinity is 1. Their distance is sqrt(1+a²/b²)=2delta. Any enclosing disk must have radius at least half this distance, while the derived circle attains it. This concerns the worst-case spectral class with only the gap premise; it does not assert that the actual J1 operator has an eigenvalue exactly a. Further reduction in this family requires extra spectral information or a smaller flux error, rather than a smaller universal scalar factor.

## Verification and controls

`phase_flux.py` replays the prior root plus144-patch flux reconstruction and all prior checks, adds exact mixed norms, verifies covariance positivity, and reproduces FLUX_RESULTS.json. `phase_circle.py` verifies source linkage, output identities, covariance algebra, conjugacy, outward rounding and rational polygon containment.

Additional theorem controls include 48 scalar spectral identities/inequalities, eight complex modal examples with a nonzero solenoidal coordinate, four polynomial coefficient identities, and four endpoint sharpness identities. Adversarial controls reject a wrong rotation sign at resonance, an omitted solenoidal norm budget, an inward square-root proposal, an indefinite covariance and zero damping. These are constructor checks, not independent review.

```sh
python3 phase_flux.py .
python3 phase_circle.py .
```

Stored-results replay is read-only and disables bytecode. No generation mode is allowed in the covariance extension. Copied source/state/flux inputs are byte-identical to the merged capture; hashes are listed in CONTRACT.json and the machine-readable results. New files and event preserve append-only evidence.

## Open work and governance

The next accuracy task is a globally coupled or overlapping flux correction that changes coarse-interface traces, or additional certified spectral information. The current zero-normal patch hierarchy still has no estimator-convergence or stopping-termination proof. Full-band accuracy, an independent mathematical review, native UD action/source/units selection and experimental calibration remain open.

The uploaded coefficient ledger's Q169-Q179 support/incidence mathematics does not select this scalar-wave action or its damping. The uploaded CRL2 subdivision document remains a governance proposal, and has not been enacted by citation. No uploaded source bytes or registry entries are changed. `Gap2_FINAL_Finite_Genesis.png` remains unavailable and was not read or used; reupload was requested.

Native Project #218 is In review / Scientific OPEN / Constructor checked / Development. Its next gate was saved and reloaded to request independent review, tighter coarse-interface flux for the phase-aware resonance1/10 target or additional spectral information, full-band precision, stopping termination and the native action bridge. Screenshot and receipt accompany the capture. Physical promotion remains **0**.
