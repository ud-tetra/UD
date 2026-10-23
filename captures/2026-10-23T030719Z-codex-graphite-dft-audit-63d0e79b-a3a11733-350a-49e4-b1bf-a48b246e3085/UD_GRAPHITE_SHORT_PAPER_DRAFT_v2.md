# A planar harmonic port for commensurate moiré graphite: geometry, material response, and a falsifiable UD hypothesis

**Short working paper v2 · 23 October 2026 · Development draft; corrects v1 material-scale discussion**

## Abstract

Friction experiments on graphite report sharp peaks near twist angles $21.8^\circ$ and $38.2^\circ$ whose load response is small relative to the coaligned interface [1]. We separate three claims often combined in interpreting these observations. First, the complementary angles arise exactly from a conventional $(2,1)$ triangular coincidence lattice: $\theta=\arccos(13/14)$ and $60^\circ-\theta$. Second, that lattice has a seven-cell honeycomb quotient with two harmonic 1-cochains, and an explicit map identifies them with lateral displacement coordinates. This is a natural **Unified Dynamics (UD) carrier and readout**, without a new force law. Third, energy loss requires material degrees of freedom and an open-system response. A registered 14-height Kolmogorov–Crespi (KC) plus illustrative plate model has a locally relaxed lateral curvature of $1.68253$ meV Å$^{-2}$ per upper atom; two height-mode doublets account for its local height correction. The resulting two-mobile-layer shear scale is $8.73$ cm$^{-1}$, while a recent independent vdW-DF3 calculation for the same $(2,1)$ cell gives $0.404$–$0.590$ cm$^{-1}$ across its distinct relaxation protocols. This large material-model discrepancy prevents promotion of the KC amplitude to a graphite prediction. Its finite closed harmonic version produces no Ohmic drag. When unspecified Rayleigh loss is added, the per-unit-loss coefficient and its local load derivative can be computed, but neither is a measured friction force or a UD-specific residual. We state the distinct material source rule and held-out test needed to make the UD hypothesis predictive.

## 1. Observation and the $60^\circ$ pairing

Chen *et al.* report **peaks**, rather than an identically vanishing force, at $21.8^\circ$ and $38.2^\circ$. Other tested commensurate $(m,n)$ orientations have no detectable signal, and the two peaks have negligible reported load dependence relative to the coaligned state [1]. The accessible abstract does not provide force tables, fitted uncertainty or mode linewidths for a quantitative residual analysis. Its article text and supplement displayed subscription restrictions in the source audit [8].

Let $a_1,a_2$ be equal-length primitive vectors of a triangular Bravais lattice, separated by $60^\circ$. The $(2,1)$ directions $u=2a_1+a_2$ and $v=a_1+2a_2$ obey $|u|^2=|v|^2=7a^2$ and $u\cdot v=13a^2/2$. Thus

\[
 \theta=\arccos(13/14)=21.786789298\ldots^\circ,
 \qquad 60^\circ-\theta=38.213210702\ldots^\circ. \tag{1}
\]

The sum is significant as a **sixfold lattice equivalence**. It motivates a planar triangular and honeycomb carrier. It does not alone select a tetrahedron, octahedron, dissipation mechanism or UD-specific material coefficient. The ordinary lattice and moiré theory already determine the angular locations.

The coincidence index is seven: one ideal quotient contains seven Bravais sites and 14 honeycomb atoms per layer. Reciprocal coset averaging eliminates primitive interlayer harmonics; the first common reciprocal shell has magnitude $\sqrt7$ times the primitive reciprocal magnitude. Conventional registry-dependent interactions therefore already have an angle-selective but small potential-energy corrugation [2]. No UD residual should be assigned to the pairing or first-shell survival.

## 2. A planar UD carrier selected by the actual interface

Treat the seven-cell honeycomb quotient as a cellular torus with 14 vertices, 21 oriented bonds and seven hexagonal faces. Its signed boundary maps satisfy $\partial_1\partial_2=0$, with ranks 13 and 6. Consequently

\[
 (b_0,b_1,b_2)=(1,21-13-6,1)=(1,2,1). \tag{2}
\]

The two-dimensional harmonic 1-space is $H^1=\ker\partial_1\cap\ker\partial_2^T$ for the declared unit-edge metric. This exact finite construction has a reproducible boundary verifier [3]. In direct lattice coordinates the three oriented bond vectors can be taken as $d_0=(1/3,1/3)$, $d_1=(-2/3,1/3)$ and $d_2=(1/3,-2/3)$. With $G=\left(\begin{smallmatrix}1&1/2\\1/2&1\end{smallmatrix}\right)$ and $(Mu)_e=d_e^TGu$, the verified identities are

\[
 \partial_1M=0,\qquad\partial_2^TM=0,\qquad M^TM=\tfrac72G. \tag{3}
\]

Thus $M$ is an explicit, rotation-covariant encoding of the two lateral coordinates into the harmonic 1-sector, with readout $u=(2/7)G^{-1}M^Tq$ on that sector. For a bilayer, an equal-layer relative displacement lifts with opposite signs on the two copies. The construction supplies a *geometric port*: it does not assert that these cochains are atomic bond extensions or supply physical inertia and force constants. The unit-metric closed Hodge–Dirac generator annihilates the harmonic sector. Interlayer registry energy must be added by a material law.

## 3. What symmetry permits, and what a material law must supply

At a $C_3$-fixed registry, the lateral translation port transforms as a real two-dimensional $E$ representation. A single scalar normal height mode cannot couple to it through an invariant bilinear term $x^Tcz$, because no nonzero vector $c$ is fixed by a $120^\circ$ rotation. A height *doublet* in the same representation can couple. This symmetry statement does not prohibit vertical modulation of lateral stiffness, coupling away from the fixed registry, broken-symmetry terms or other dissipative channels.

For lateral coordinate $x$, internal coordinates $h$, clamped curvature $H_{xx}$, positive internal stiffness $K$, and mixed Hessian $C$, equilibrium height elimination gives

\[
 H_{xx}^{\rm rel}=H_{xx}-CK^{-1}C^T. \tag{4}
\]

If an independently sourced passive Rayleigh matrix $D_h$ acts on the internal modes, the additional *linear-response* damping at low frequency is

\[
 \Gamma_{\rm add}=CK^{-1}D_hK^{-1}C^T\succeq0. \tag{5}
\]

A finite closed harmonic model has $D_h=0$ and no Ohmic DC coefficient: its off-resonant response is real and even in frequency. Equation (5) is a constitutive **conditional** law. Graphite does not acquire a material damping rate from a Hodge eigenvalue, a tetrahedral ratio or the fact that $H^1$ has dimension two.

A proposed UD source refines this statement. Exact or coexact incidence forcing has zero projection into the harmonic port. With seven rotational edge orbits, write $B_1=\partial_1$ and assign a diagonal source weight $W=\operatorname{diag}(w_e)$. The projected source coupling is then $K(w)=M^TWB_1^T$. Its isotropic quadratic strength has the verified connected-orbit form $\alpha(w)=\tfrac14\sum_{i<j}c_{ij}(w_i-w_j)^2$, $c_{ij}\ge0$. It vanishes for equal weights. This is a useful **selection rule**: a source contrast must exist before this particular port responds. Neither the weights, their physical amplitude nor their loss rates follow from the topology. Ordinary material heterogeneity may produce the same pattern. The registered seven-orbit source alone accounts for only 53.39% of the full local quadratic height-softening correction in the declared numerical model; omitted and cross contributions remain material [4]. It cannot be used as a complete measured graphite force law.

## 4. A conditional material calculation, with its actual scope

To put units on the response, a development calculation uses a three-neighbor local-normal KC interlayer pair potential, a fixed 16 Å pair roster around the reference registry, a rigid lower sheet and a 14-site bending plate with an illustrative $D=1.44$ eV. All 14 upper heights and two lateral coordinates are relaxed at a selected **tensile numerical reference** of about $-10.734$ MPa on ideal atom area; this is not an experimental zero-pressure point [4]. At that stationary state, in meV Å$^{-2}$ per mean upper atom,

| Calculated quantity | Value | Meaning |
| --- | ---: | --- |
| Clamped lateral curvature | 1.91187 | Local second derivative with heights fixed at their relaxed state |
| Height Schur correction | 0.229339 | $\tfrac12\operatorname{tr}(CK^{-1}C^T)$ |
| Relaxed lateral curvature | 1.68253 | Local second derivative of height-minimized energy |
| Static curvature load slope | $7.76\times10^{-4}$ per MPa | meV Å$^{-2}$/atom per MPa near the numerical reference |

**Collective mass and independent material audit.** If $x$ is the relative shift of the 14 upper atoms against 14 lower atoms, and $k$ is the curvature *per upper atom*, then $E=14kx^2/2$. For two equally moving rigid layers, each translates by $\pm x/2$, so $T=\tfrac12(7m_C)\dot x^2$ and the effective mass per upper atom is $\mu=m_C/2$. If the lower layer is fixed, the mass per upper atom is $m_C$. With $m_C=12u$, $1$ meV Å$^{-2}=0.01602176634$ N m$^{-1}$ and $\tilde\nu=(2\pi c)^{-1}\sqrt{k/\mu}$, the clamped and height-relaxed two-mobile-layer values are **9.309** and **8.732 cm$^{-1}$**, respectively; for a fixed lower layer they are **6.582** and **6.175 cm$^{-1}$**. The published rigid-height KC calculation reports **9.153 cm$^{-1}$** for $(2,1)$ [2]. Agreement at this scale checks mass bookkeeping inside broadly related KC calculations; it is **not independent validation** of their graphite amplitude.

A separate vdW-DF3 first-principles study of the same seven-cell $(2,1)$ structure [9] reports **0.404, 0.510 and 0.590 cm$^{-1}$** for rigid, out-of-plane relaxed and more fully relaxed constrained structures. Its rigid equilibrium spacing is 3.4022 Å; the 2023 KC source uses about 3.46 Å and our plate calculation uses a distinct tensile reference and a rigid lower sheet. The DFT study also finds the opposite registry type from KC. The shared two-mobile-layer mass convention maps those three DFT frequencies to curvatures of **0.00360, 0.00574 and 0.00768 meV Å$^{-2}$ per upper atom**, respectively, versus our conditional relaxed **1.68253**. The $\sim293$ ratio against the DFT out-of-plane curvature is a **cross-model discrepancy**, not an error bar or a measured residual. DFT estimates themselves still require experimental checking [9]. Since $C$, $K$, and loss may change with the PES and layer spacing, multiplying our Rayleigh coefficient or its load slope by a single amplitude ratio is unjustified. The conventional material baseline must be calibrated anew before predicting a physical friction force.

This stiffness slope is **not** a friction-load slope. Reoptimization, finite-difference Hessians and 14/16/18 Å cutoff checks support it only inside the chosen KC plus plate model [4]. A mode decomposition has two active $E$ doublets out of 14 height modes. Their mass-converted frequencies, roughly 9.37 and 25.59 THz under a fixed lower layer and a $^{12}$C assumption, are *illustrations of this plate model*, not independently observed graphite phonons [5].

If one additionally **assumes** a pressure-independent scalar Rayleigh loss $D_h=dI$, define the dimensionless $G(P)=C(P)K(P)^{-2}C(P)^T$. The scalar part at the reference is $\tfrac12\operatorname{tr}G=5.28545\times10^{-4}$, and its computed derivative is $4.26035\times10^{-7}\,\mathrm{MPa}^{-1}$. Thus its logarithmic slope is $8.0605\times10^{-4}\,\mathrm{MPa}^{-1}$, while $d$ remains unknown [6]. If $d$ changes with pressure, $\Gamma_{\rm add}'=dG'+d'G$; the second term can alter the sign and size of the response. A local velocity damping coefficient is not yet the finite-speed force that Chen *et al.* measured.

The two active doublets give one further practical limit. A DC observation contains the combination $a_1d_1+a_2d_2$ with $(a_1,a_2)=(4.950856\times10^{-4},3.345914\times10^{-5})$ and cannot separate the two losses. Across five pressure points, the two-column matrix has condition number approximately $2.71\times10^4$ after unit-column normalization. A *model-based* weak-loss, off-resonant response at zero frequency and twice the first active-mode frequency instead gives a two-channel matrix with condition number about 5 in channel-contribution coordinates [7]. That apparent improvement requires verified resonances, independent background subtraction and a calibrated complex susceptibility; it is a design calculation, not an executed graphite measurement.

## 5. A discriminating UD hypothesis and test

**Hypothesis.** The graphite interface admits a selected relative harmonic translation port. A physical edge-source contrast can couple that port to internal $E$ modes; a sourced open environment can then dissipate energy. The exact geometry specifies which channels are permitted and which uniform sources cancel. It does not set the friction amplitude. This hypothesis becomes distinctly UD only if an independently defined source pattern imposes a restriction on the *signed residual* beyond a full conventional moiré, contact and material-bath model.

A test has four stages:

1. Freeze a conventional honeycomb/moiré and **independently checked material PES** baseline, contact size and edge model, temperature, normal separation, sliding speed and the measured-force estimator using data that exclude the held-out paired-angle force curves. KC and vdW-DF3 disagree strongly for the same $(2,1)$ cell [2,9]; carry this model uncertainty explicitly.
2. Obtain the internal stiffness, lateral mixed response and mode-resolved loss spectrum from an independent atomistic or dynamic measurement. Determine whether the proposed seven-orbit source spans the observed coupling; preserve any complement instead of assigning it to UD by default.
3. Declare the UD source rule and its coefficients from independent source measurements. Predict the signed $F_{\rm obs}-F_{\rm conventional}$ and its load derivative at **both** $\theta$ and $60^\circ-\theta$, with a specified uncertainty and force protocol, before viewing those held-out data.
4. Reject or narrow the proposed material bridge if the source-span condition fails, the residual disappears after conventional controls, or the signed predictions fail the held-out comparison.

The currently accessible abstract supplies neither the required force uncertainties nor a source-resolved loss spectrum [1,8]. Consequently there is **no parameter-free UD prediction of the remaining friction or load slope yet**. The paired angles and their symmetry equivalence are fully explained by ordinary lattice geometry; the origin of the observed weak load response remains a material and dynamical question. This working paper states a mathematical carrier and a route to a falsifiable additional law, not an empirical UD validation.

## Reproducibility and data boundary

The exact torus construction and checker [3], local KC and height-relaxation replay [4], finite-spectrum replay [5], pressure sweep [6], and two-loss identifiability calculation [7] are retained as immutable, versioned repository captures. The public 2023 KC source archive is SHA checked when used; imported archive code is not executed. Model uncertainties due to the lower rigid layer, bending-plate dispersion, local-normal rule, finite cell, pressure reference, contact edges and open-system bath are distinct from numerical step/cutoff sensitivity. The mass and DFT audit [9,10] adds a much larger cross-potential uncertainty: a numerically stable KC replay is not a reliable graphite-scale PES calibration. No 2026 experimental force trace was ingested. The scientific claim remains a development hypothesis pending independent material sourcing and review.

## References

[1] W. Chen, J. Wang, Q. Zheng and Z. Wu, “Observation of Superlubricity at Commensurate Moiré Graphite Interfaces,” *Physical Review Letters* **137**, 166201 (2026), [doi:10.1103/ly48-b4l2](https://doi.org/10.1103/ly48-b4l2), public abstract.

[2] A. S. Minkin *et al.*, “Interlayer interaction, shear vibrational mode, and tribological properties of two-dimensional bilayers with a commensurate moiré pattern,” *Physical Review B* **108**, 085411 (2023), [arXiv:2308.06302](https://arxiv.org/abs/2308.06302). Its 2023 KC results are a conventional comparator, not the 2026 experiment.

[3] UD capture `2026-10-22T211409Z-codex-graphite-honeycomb-5e20b9a6-101b-4fce-8c91-a1d4070ba2d8`, `verify_honeycomb_h1.py` and `RESULTS.json`; exact conditional cellular construction.

[4] UD capture `2026-10-23T015602Z-codex-graphite-nonlinear-relax-a7f309c2-f7597bc1-0620-488b-97f4-3eabbc7815d0`, nonlinear KC plus bending plate replay. See its source provenance and its explicit conditional material assumptions.

[5] UD capture `2026-10-23T023854Z-codex-graphite-finite-spectrum-4c8b18e3-68bdd1a3-441a-4a35-ac05-a26af9803d0c`, finite height spectrum and closed-harmonic DC-damping no-go.

[6] UD capture `2026-10-23T024735Z-codex-graphite-loss-load-60d8705c-babb19e4-d2fd-435f-abd7-86602cecf7fc`, pressure-resolved conditional per-unit-loss results.

[7] UD capture `2026-10-23T025317Z-codex-graphite-mode-identifiability-318a7d4e-7c29d6d8-ce6e-413f-b5fc-b0a5d0ed272d`, two-channel loss identifiability and measurement design.

[8] Source-access audit bundled with [7], dated 23 October 2026 UTC; the publisher abstract is accessible while article text and supplement display subscription requirements. Access may change.

[9] I. V. Lebedeva *et al.*, “Robust structural superlubricity of twisted graphene bilayer and domain walls between commensurate moiré pattern domains from first-principles calculations,” [arXiv:2511.01338](https://arxiv.org/abs/2511.01338), Tables 2, 4 and 6 (2025 preprint; checked 23 October 2026). The tabulated shear values are **calculations**, not graphite measurements.

[10] This capture, `reproduce_mass_map.py` and `MASS_MAP_RESULTS.json`, standard-library mass/unit replay; source numbers transcribed from [2,9].
