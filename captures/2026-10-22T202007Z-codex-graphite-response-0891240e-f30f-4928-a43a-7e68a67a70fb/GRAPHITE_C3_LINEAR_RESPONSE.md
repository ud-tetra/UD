# A symmetry-allowed sliding response and its identifiability limit

22 October 2026. **EXACT conditional linear-response calculation; NO-GO for a parameter-free graphite residual; physical promotion 0.** This addendum follows the planar seven-cell character audit in draft PR #414. Its purpose is to make the missing force/readout law precise, not to fit the graphite experiment.

## 1. The translation port survives the 84-dimensional mismatch

At the ideal zero-offset (2,1) bilayer, the in-plane rigid translation $x=(x_1,x_2)^T$ of one layer relative to the other is a real two-dimensional rotation representation of $C_3$. The active refined octahedral chain has (26) such real rotation planes and (32) trivial lines. Therefore an intertwiner from the chain to this **one** translation plane is symmetry allowed. The rank-at-most-80 obstruction to an *invertible map of the whole 84-dimensional chain onto all 84 atomic displacements* does not forbid a two-coordinate sliding readout. It neither selects an intertwiner nor sets its scale.

## 2. Minimal passive port with an explicit bath

Take $q\in\mathbb R^{84}$ for the active finite-chain coordinates and $x\in\mathbb R^2$ for prescribed lateral displacement, using a fixed physical length normalization for both. For a locally stable linearized state, stipulate a real symmetric stiffness $K\succ0$, internal bath matrix $D\succeq0$, translation stiffness $K_x$, bare translation damping \(\Gamma_x\succeq0\), and stiffness coupling $C\in\mathbb R^{2\times84}$. In a Laplace variable $s$, assume

\[
\begin{pmatrix}f_x\\0\end{pmatrix}
=\begin{pmatrix}K_x+s\Gamma_x&-C\\-C^T&K+sD\end{pmatrix}
\begin{pmatrix}x\\q\end{pmatrix}.
\tag{1}
\]

The symmetric static Schur complement $K_x-CK^{-1}C^T$ should be positive for a strictly stable pinned linearization. A translation-invariant periodic sliding problem instead has a zero rigid-translation mode and requires a registry-dependent nonlinear potential; Eq. (1) is only a local small-frequency force response. If $x,q$ have length units, $K,K_x,C$ have force/length units and $D,\Gamma_x$ have force·time/length units. This bath is a **constitutive assumption**; the closed UD Hodge–Dirac operator alone does not generate it.

Eliminating $q=(K+sD)^{-1}C^Tx$ yields

\[
K_{\rm eff}$s$=K_x+s\Gamma_x-C(K+sD)^{-1}C^T
=K_x-CK^{-1}C^T+s\underbrace{\bigl(\Gamma_x+CK^{-1}DK^{-1}C^T\bigr)}_{\Gamma_{\rm eff}}+O(s^2).
\tag{2}
\]

For any lateral vector $y$, $y^T(\Gamma_{\rm eff}-\Gamma_x)y=(K^{-1}C^Ty)^TD(K^{-1}C^Ty)\ge0$. Thus the stipulated bath contributes nonnegative local dissipation. For harmonic slow motion, the velocity-proportional force is $\Gamma_{\rm eff}\dot x$, and the cycle-averaged dissipated power is $\langle\dot x^T\Gamma_{\rm eff}\dot x\rangle$. Turning this *local* coefficient into a measured finite-speed friction force still needs the full periodic registry potential, drive, contact and readout.

## 3. Rotation covariance and load response

Assume the zero-offset preparation respects $C_3$: $R_xC=CU$, $U^TKU=K$, $U^TDU=D$, and $R_x^T\Gamma_xR_x=\Gamma_x$, where $R_x$ is planar 120° rotation and $U$ is the signed-simplex action on active (q). Then $R_x^T\Gamma_{\rm eff}R_x=\Gamma_{\rm eff}$. Because $\Gamma_{\rm eff}$ is symmetric, it must be a scalar matrix:

\[
\Gamma_{\rm eff}=\gamma$L$I_2,\qquad
\gamma=\tfrac12\operatorname{tr}\Gamma_x+\tfrac12\operatorname{tr}(CK^{-1}DK^{-1}C^T)\ge0.
\tag{3}
\]

The scalar can depend on normal load $L$. Put $A=K^{-1}$, and use a prime for \(\partial_L\). The exact derivative of this specified low-frequency response is

\[
\gamma'=\tfrac12\operatorname{tr}\{\Gamma_x'+2C'ADA C^T
+C[A D'A-AK'ADA-ADA K'A]C^T\}.
\tag{4}
\]

The factor 2 in the $C'$ term follows from trace cyclicity and symmetry; the $K'$ terms must both be retained. For a single coupled rotation plane with $K=kI_2,D=dI_2,C=cI_2,\Gamma_x=\gamma_0I_2$ and all other chain planes decoupled, Eq. (3) becomes

\[
\gamma=\gamma_0+\frac{c^2d}{k^2},\qquad
\gamma'=\gamma_0'+\frac{c^2d}{k^2}\left(2\frac{c'}c+\frac{d'}d-2\frac{k'}k\right)
\tag{5}
\]

when $c,d,k>0$. Equation (5) provides a **conditional cancellation test** for small load slope. It is not a prediction that the slope vanishes. The coefficients and their load derivatives are absent from the UD geometry and the accessible graphite abstract.

## 4. A sharp non-identifiability result

Choose any $k,d>0$ and any $c\ge0$, with $K_x\succ c^2I_2/k$ in the single-plane example. These choices obey the same $C_3$ symmetry and stability constraint, yet produce any nonnegative bath contribution $c^2d/k^2$ (including zero when (c=0)). Smooth positive choices (c$L$,d$L$,k$L$) also yield zero, positive or negative \(\gamma'$L$\) at a given load while keeping \(\gamma\ge0\). Hence **geometry, the 84-to-84 rank obstruction, positivity and $C_3$ symmetry do not determine a nonzero residual friction coefficient or its load slope**. A distinct UD prediction requires a material-derived (C,K,D), normal-load law and physical time calibration, fixed before held-out data.

At mirror-related angles \(\theta_+=\arccos(13/14)\) and \(\theta_-=60^\circ-\theta_+\), a mirror-covariant preparation and constitutive law give equal scalar response. This evenness is already allowed by the conventional honeycomb/moiré model and thus is a **null control**, not evidence for UD. A preparation that breaks the mirror need not obey it. Angular sharp peaks, finite sliding barriers and speed-dependent forces are outside this local port until a registry potential and force estimator are specified. The public abstract reports sharp peaks with negligible load dependence, but supplies no numeric force curves or uncertainty series for an independent test [1].

## 5. What to place in the manuscript

The revised paper should state Eqs. (2)–(5) as an explicit candidate constitutive bridge and label the non-identifiability as the current physical boundary. The next *empirical* input is a conventional calibrated interlayer registry potential and a measured or computed force-constant/damping response under load; only then can one freeze a UD-specific $C,K,D$ and compare residuals. Do not infer them from the observed near-flat load response.

[1] W. Chen *et al.*, “Observation of Superlubricity at Commensurate Moiré Graphite Interfaces,” *Phys. Rev. Lett.* **137**, 166201 (2026), [doi:10.1103/ly48-b4l2](https://doi.org/10.1103/ly48-b4l2), public abstract.
