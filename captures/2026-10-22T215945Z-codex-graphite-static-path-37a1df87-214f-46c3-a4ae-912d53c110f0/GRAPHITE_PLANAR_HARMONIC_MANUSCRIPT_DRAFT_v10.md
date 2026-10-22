# A planar harmonic carrier for commensurate graphite interfaces

**Research manuscript draft v10 · 22 October 2026**

## Abstract

Graphite interfaces exhibit sharp but weak-load-dependent friction peaks near 21.8° and 38.2° at the (2,1) commensurate moiré orientation [1]. The paired angles follow exactly from triangular-lattice geometry, with cosine 13/14, and are not a new dynamical prediction. We construct the periodic seven-cell honeycomb interface as a 14-vertex, 21-bond, seven-hexagon cellular torus. Its unit-metric chain complex has Betti numbers (1,2,1), and its two harmonic edge coordinates admit an explicit, normalized, rotation-equivariant map from lateral vectors. A bilayer therefore has a selected relative-translation port without identifying the atoms with a three-dimensional tetrahedral subdivision. We also show that the rigid first common reciprocal shell has magnitude $\sqrt7$ times the primitive reciprocal length and, for a real isotropic pair potential truncated to that shell, a global corrugation range $9|V_*|$ per Bravais cell. The minimum-energy-path saddle barrier is $|V_*|$ for positive $V_*$ and $8|V_*|$ for negative $V_*$. The relaxed saddle barrier’s load derivative equals the saddle-to-minimum separation difference. These are conventional geometric and equilibrium identities. The first-shell local stiffness is (3/2)|V_*|g_*² or 3|V_*|g_*² according to the unknown Fourier sign; its exact normal-load slope depends on the vertical derivative and curvature. At a C3-fixed registry, a scalar normal displacement cannot couple bilinearly to the lateral port, whereas a shear E doublet can supply conditional static softening and positive low-frequency damping. An incidence-only exact or coexact source has identically zero harmonic projection; a weighted-gradient source with nonuniform C3 edge-orbit weights can activate it. Its isotropic response depends on only one quadratic combination of seven weights, so friction alone cannot identify the source. The closed cellular generator has no dissipative response on its harmonic port; a material-derived interlayer amplitude, bath, physical time scale and force estimator are required for a distinct residual friction prediction.

## 1. Experimental target and the lattice baseline

Chen *et al.* report sharp peaks at 21.8° and 38.2° associated with the (2,1) commensurate graphite moiré, with negligible measured load dependence relative to the coaligned state [1]. Their public abstract also describes small modeled residual sliding barriers and stable interlayer spacing. We use only the accessible abstract; peak amplitudes, force-versus-load uncertainties and supplemental curves are unavailable here. A friction peak at these angles is not an identically zero force.

Let $a_1,a_2$ be equal-length planar primitive vectors making 60°. The (2,1) vectors $u=2a_1+a_2$ and $v=a_1+2a_2$ have squared length (7a^2) and inner product (13a^2/2). Hence

\[
 \theta_+=\arccos(13/14)=21.786789298\ldots^\circ,
 \qquad \theta_-=60^\circ-\theta_+=38.213210702\ldots^\circ.\tag{1}
\]

The direct-coordinate rotation and coincidence index are

\[
 R=\frac17\begin{pmatrix}8&3\\-3&5\end{pmatrix},\qquad
 [\Lambda:\Lambda\cap R\Lambda]=7.\tag{2}
\]

Thus one ideal supercell contains seven Bravais sites and 14 honeycomb atoms in each layer. The complementarity and locations in Eq. (1) belong to the conventional baseline.

## 2. A cellular chain built from the interface itself

Label Bravais sites by $k=p-2q\pmod7$, so unit steps $a_1,a_2$ advance labels by 1 and 5. Place honeycomb atom $A_k$ at the Bravais site and $B_k$ at (A_k+$a_1+a_2$/3). Nearest-neighbor edges connect $B_k$ to $A_k,A_{k+1},A_{k+5}$. The seven periodic hexagons complete a torus cellulation with

\[
 (\dim C_0,\dim C_1,\dim C_2)=(14,21,7),\qquad
 \partial_1\partial_2=0,\qquad (b_0,b_1,b_2)=(1,2,1).\tag{3}
\]

An exact construction uses the dual seven-vertex triangular quotient, whose oriented triangles are ([k,k+1,k+5]) and ([k+1,k+6,k+5]). Its 1-skeleton is $K_7$. Transposing its two signed boundary matrices and correcting edge orientations gives the honeycomb boundaries. Their ranks are 13 and 6, proving Eq. (3) without a continuum approximation.

For unit cellular metrics, the vertex graph Laplacian has eigenvalues (0), (6), and $3\pm\sqrt2$, with multiplicities 1, 1, 6 and 6 respectively. The seven-face Laplacian has eigenvalues 0 and 7, with multiplicities 1 and 6. The skew cellular Hodge–Dirac characteristic polynomial is

\[
 \det(\lambda I-A)=\lambda^4(\lambda^2+6)
 (\lambda^4+6\lambda^2+7)^6(\lambda^2+7)^6.\tag{4}
\]

Its four zero modes include the two harmonic 1-cochains. The nonzero spectral values are structural eigenvalues in a declared unit metric, not measured graphite frequencies.

## 3. An explicit lateral map into the harmonic sector

In direct lattice units $a=1$, orient every bond from (A) to (B). Its three possible vectors are

\[
 d_0=(1/3,1/3),\quad d_1=(-2/3,1/3),\quad
 d_2=(1/3,-2/3),\quad \sum_jd_j=0.\tag{5}
\]

Let $G=\begin{pmatrix}1&1/2\\1/2&1\end{pmatrix}$. For a lateral vector (u) define the edge cochain ((Mu)_e=d_e^TGu). The exact signed boundaries satisfy

\[
 \partial_1M=0,\qquad\partial_2^TM=0,\qquad
 M^TM=\frac72 G.\tag{6}
\]

Because the harmonic 1-space has dimension two, (M) maps the entire lateral plane onto it. The normalized geometric readout of any edge state (q) is

\[
 u_{\rm geom}=\frac27G^{-1}M^Tq.\tag{7}
\]

The construction is covariant under the actual 120° lattice rotation. For two identical ideal layers, each with its rotated bond geometry, the common and relative translation planes are their sum and difference. At equal unit-edge weights, the relative lift $u_1=-u/2,u_2=u/2$ has squared cochain norm (7u^TGu/4). This is a geometric representation of the relative displacement port; uniform intralayer translation does not strain intralayer bonds. Atomic inertia, boundary conditions and unequal layers would change the physical metric.

For the closed unit-metric Hodge–Dirac operator, any harmonic $q=Mu$ satisfies (A(0,q,0)=0). Thus topology and incidence select a zero sector and a readout, while leaving the lateral pinning energy and energy loss unspecified.

## 4. Conventional corrugation, saddle barrier and normal load

For a rigid, infinite, pairwise translationally invariant bilayer, averaging over the seven rotated Bravais cosets kills a bottom reciprocal index $h=$h_1,h_2$$ unless

\[
 R^Th\in\mathbb Z^2\quad\Longleftrightarrow\quad h_1-3h_2\equiv0\pmod7.\tag{8}
\]

The primitive reciprocal shell fails Eq. (8). The first surviving six indices are the signs of $(3,1),(-1,2),(-2,-3)$, at reciprocal magnitude $\sqrt7\,g_0$. The two-site basis has a unit-modulus product factor on this shell. For a real isotropic interlayer pair Fourier coefficient $V_*(z)$, omitting all other corrugation terms and shifting the lateral origin gives

\[
 U(a,b;z)=2V_*(z)[\cos a+\cos b+\cos(a+b)].\tag{9}
\]

Choose the oriented reciprocal vectors as $g_1,g_2,g_3=-(g_1+g_2)$, with pairwise angles 120° and sum zero. Cosine evenness turns $\cos(g_3\cdot x)$ into the displayed $\cos(a+b)$; the sign convention does not change the energy or Hessian.

The bracket $S$ has global maximum $3$, two minima $-3/2$, and three connecting saddles $-1$ on a phase torus. Therefore the *global max-to-min range* is $9|V_*|$, while the lowest connecting saddle gives the minimum-energy-path barrier

\[
 \boxed{\Delta U_{\rm mp}=c_\pm|V_*|,\qquad
 c_+=1\ (V_*>0),\quad c_-=8\ (V_*<0).}\tag{10}
\]

For $V_*>0$, a minimum at $S=-3/2$ is separated from its neighbors by a saddle at $S=-1$, so the barrier is $V_*$. For $V_*<0$, the minimum at $S=3$ is separated from the next periodic copy by the same saddle, so the barrier is $8|V_*|$. The sign of the graphite coefficient is not determined by lattice geometry. Finite edges, reconstruction and additional harmonics can change both values. The former manuscript's factor 9 was a correct **global range**, but its use as a sliding-barrier multiplier was erroneous; the corrected stationary-point derivation is supplied separately [2].

Let $L>0$ be compressive normal force per top Bravais cell and define registry enthalpy $\mathcal H(t,L)=\min_z[E(t,z)+Lz]$. Along smooth lateral saddle and minimum branches, the exact envelope identity is

\[
 \frac{d\Delta\mathcal H_{\rm mp}}{dL}=z_{\rm saddle}(L)-z_{\rm min}(L).\tag{11}
\]

In a weak first-shell regime with mean normal curvature $k_z>0$, this gives $d\Delta\mathcal H_{\rm mp}/dL=-c_\pm\partial_z|V_*|/k_z$ at leading order. If an independently established material law has $V_*(z)=V_0e^{-\kappa z}$, then $\partial_L\log\Delta\mathcal H_{\rm mp}\simeq\kappa/k_z$ at that order. Equation (11) concerns an equilibrium *saddle barrier*. A sliding dynamics and force estimator are necessary before comparing its slope to the observed friction load response.

## 4a. A numerical conventional comparator at the exact paired angle

Minkin *et al.* independently calculated the infinite rigid twisted bilayer PES with a registry-dependent Kolmogorov–Crespi potential at fixed layer separation 3.46 Å [9]. Their (2,1) entry has $N_c=7$, $\theta=21.787^\circ$, and a first-star fit, per **upper-layer carbon atom**, $\delta U=U_1[\cos(g_1\cdot x)+\cos(g_2\cdot x)+\cos(g_3\cdot x)]$ with $U_1=-2.02\times10^{-5}$ eV/atom. Their reported fit RMS is 1.04% of the total corrugation, and their reported shear wavenumber and shear strength are 9.153 cm$^{-1}$ and 16.7 MPa [9]. The complementary 38.213° orientation follows from the same sixfold geometric equivalence, not a separately fitted coefficient. Their public raw PES dataset [10] is now independently fitted in the following section; no archived plotting code was executed.

Our Eq. (9) instead measures energy per **two-atom upper-layer Bravais cell**. Therefore $U_{\rm cell}=2U_{\rm atom}$ and $V_*=U_1=-20.2$ μeV/cell, not $U_1/2$ or $2U_1$. With the negative branch, $a=\sqrt3(1.42)$ Å and $g_*=\sqrt7\,4\pi/(\sqrt3a)$, our exact shape factors imply:

| Quantity | Fixed-height KC comparator | Meaning |
| --- | ---: | --- |
| First-star coefficient | $-20.2$ μeV per two-atom cell | Imported potential fit [9] |
| Max-to-min PES corrugation | $90.9$ μeV/atom | $(9/2)|U_1|$; not a path barrier |
| Minimum-path *sliding* saddle barrier | $80.8$ μeV/atom | $4|U_1|$; equivalently $161.6$ μeV/cell |
| Rotation to incommensurate mean | $60.6$ μeV/atom | $3|U_1|$; distinct path, matches [9] |
| Isotropic lateral curvature | $1.8456\times10^{-3}$ eV Å$^{-2}$/atom | $\tfrac32|U_1|g_*^2$ |
| Rigid bilayer shear wavenumber | $9.14$ cm$^{-1}$ | computed with $m_C=12.011$ u; [9] quotes 9.153 cm$^{-1}$ |
| Ideal periodic static shear strength | $16.7$ MPa | first-star maximum path force/atom divided by atomic area; matches [9] |

These values reproduce the published magnitude and sign convention without fitting the 2026 graphite traces. The $9.14$ vs $9.153$ cm$^{-1}$ difference follows rounded published $U_1$, bond length and mass choices. The directly fitted first-star RMS (0.941 μeV/atom in that KC model) contains ordinary higher harmonics and simulation artifacts; it is not an observed UD residual. Another reasonable interlayer potential in the same study gave (2,1) corrugation below their calculation accuracy [9], so the KC numbers are potential-dependent rather than universal material constants. Its periodic static shear strength is not a measured kinetic friction peak.

A single fixed separation supplies neither $\partial_z U_1$ nor the normal stiffness $K_z$ for Eq. (13); it supplies no bath damping time or weighted-source coefficient for Eqs. (19)–(22). A two-height energy series at 21.787° plus the unmodulated normal EOS would make the equilibrium load derivative computable, while a dissipative simulation or measured force-speed trace is required for a dynamic friction response. A distinct UD claim must be judged against a conventional baseline including higher harmonics, relaxation, finite contact and dynamics, not against zero corrugation.

## 4b. Direct raw-grid test of the conventional harmonic remainder

We downloaded the CC BY 4.0 public archive identified by DOI 10.17632/svnpzbjc3t.1 and SHA-256 `b1ccf62a3e75928e1382cbdd6c669b99675fef9ad5f077e79057a142a0a07875`, read only its `(2,1)` X/Y/Z text grids, and did not execute its Mathematica plotting file [10,11]. The grid contains $128\times129$ samples at a single $z=3.46$ Å. Its archive folder says `pes21_10x10_Rc=16`, whereas the paper’s Table I lists an $18\times18$ simulation cell for (2,1); we have not resolved whether the folder label denotes a different run or processing choice. This limits run-level identity while leaving the archived grid’s own Fourier audit reproducible. The dataset page describes Z as μeV, but its own plotting script multiplies $Z-\min Z$ by 1000 and labels the result μeV. The stored range is 0.09104359 in Z units, i.e. **91.04359 μeV/atom** under the script's conversion; treating stored Z directly as μeV would create a thousand-fold error. Its large constant energy offset is removed by the regression intercept.

We used the exact index-seven common shell at $|g|=\sqrt7\,4\pi/(\sqrt3a)$ and the archive grid's orientation. A free sine/cosine fit of its three directed waves gives magnitudes $(20.2267,20.2502,20.2659)$ μeV/atom with a phase-closure error of $2.47\times10^{-4}$ rad. A symmetry-constrained common-amplitude/translation fit gives $U_1=-20.2476$ μeV/atom, consistent with the source's rounded $-20.2$ μeV/atom and *conventional* negative branch. The unconstrained first-shell RMS is 0.9410 μeV/atom, 1.034% of the raw 91.044 μeV/atom range, consistent with the paper's rounded 1.04% value.

| Reciprocal norm $|g|^2/g_*^2$ retained | Plane waves | Training RMS (μeV/atom) | Interlaced holdout RMS (μeV/atom) |
| --- | ---: | ---: | ---: |
| $1$ | 3 | 0.94096 | 0.94119 |
| $1,3$ | 6 | 0.42333 | 0.42330 |
| $1,3,4$ | 9 | 0.42190 | 0.42186 |
| $1,3,4,7$ | 15 | 0.42159 | 0.42155 |

Each plane wave has separate sine and cosine coefficients; the three added $|g|^2/g_*^2=3$ waves have amplitudes 0.670–0.705 μeV/atom. Thus this ordinary next common reciprocal shell removes about $1-(0.42330/0.94119)^2=79.8\%$ of the first-shell *squared residual* at the same height. The holdout uses every fourth interlaced grid point from the **same simulation**; it checks interpolation, not another force field or experiment. The remaining 0.422 μeV/atom RMS can include other allowed shells, cutoff/discretization artifacts or physics of the KC model. No UD term was fit or detected. Energetic RMS cannot be used as friction-force RMS without differentiating a validated potential along a specified path and accounting for contact dynamics. Only one height occurs in this archive, so $\partial_z V_*$, $K_z$, damping and load response remain open.

**Static path consequence.** Fitting the full grid with first shell only, solving the nearby stationary minimum and one-index saddles in the three nearest lattice directions, gives barriers $80.95$–$81.03$ μeV/atom. Adding the norm-three reciprocal shell yields $78.21$–$78.24$ μeV/atom, a conventional reduction of roughly $2.8$ μeV/atom (about 3.5%). The corresponding maximum tangential force **on each straight line connecting periodic minima**, divided by area per carbon atom, changes from $16.73$–$16.75$ to $16.22$–$16.23$ MPa. These nearby saddles have one negative and one positive Hessian eigenvalue. The calculation does not prove a global minimum-energy path for the two-shell potential, and a straight-line peak slope is not necessarily the force along a relaxed curved path. This quantifies how a small *ordinary* higher harmonic affects the static comparator before any UD residual is posed [12].

## 5. Typed harmonic stiffness and load response

The adopted UD mathematical method [3] requires us to distinguish the exact planar representation from a material law. Take a physical relative Cartesian displacement $x$ in metres and primitive length $a$ in metres. Each oriented honeycomb bond contributes the dimensionless row $d_e^T/a$ to $M_X$, so $q=M_X x$ has metres in the chosen unit-edge metric. For identical layers the relative lift $I_Xx=(-M_Xx/2,+M_Xx/2)$ has $I_X^TI_X=(7/4)I_2$. The adjoint readout is $x=(4/7)I_X^Tq$ on the two-dimensional relative plane. It annihilates the other 40 edge directions, without a claim about lost information or atomic bond strain.

At the stable registry of Eq. (9), the three oriented reciprocal vectors have magnitude $g_*=\sqrt7g_0$ and $\sum_jg_jg_j^T=(3/2)g_*^2I_2$. Their cosine is $-1/2$ for $V_*>0$ and $1$ for $V_*<0$. Therefore the exact *conditional* lateral Hessian and its orthonormal harmonic-port representation are

\[
 k_x=\begin{cases}(3/2)|V_*|g_*^2,&V_*>0,\\3|V_*|g_*^2,&V_*<0,\end{cases}
 \qquad k_q=\frac47k_x.\tag{12}
\]

Both have units of energy per length squared; the $4/7$ is a coordinate-normalization factor, not a UD material prediction. With the fixed-height minimum-path barrier in Eq. (10), the conventional first-shell shape constraint is $k_x/\Delta U_{\rm mp}=(3/2)g_*^2$ on the positive branch or $(3/8)g_*^2$ on the negative branch. This ratio is undefined for $V_*=0$ and changes with higher shells or interface relaxation.

Let $z_m(L)$ be the minimum's stable vertical height under compressive force $L$ per Bravais cell, and let $K_z^m=E_0''(z_m)+2S_mV_*''(z_m)>0$ with $S_m=-3/2$ or $3$ according to the sign of $V_*$. The mixed $x,z$ Hessian vanishes at this registry because $\nabla_xS=0$. The implicit stationary equation gives the following *exact result within Eq. (9) plus $E_0(z)$*, even after vertical relaxation:

\[
 \frac{d\log k_x}{dL}=-\frac{\partial_z\log|V_*(z_m)|}{K_z^m},\qquad
 \frac{dk_x}{dL}=-\beta_sg_*^2\frac{\partial_z|V_*(z_m)|}{K_z^m},\quad
 (\beta_+,\beta_-)=(3/2,3).\tag{13}
\]

It requires an independently sourced $V_*(z)$ and $E_0(z)$ to yield a number. Eq. (11) is the distinct saddle-barrier envelope, whose logarithmic slope agrees with Eq. (13) only to leading order for weak corrugation. A small friction-load slope does not follow from either equilibrium identity without sliding dynamics and a force estimator. The typed object inventory, exact rational checks, failure modes and open material inputs are in the corrected [5].

## 6. Symmetry-selected bath and a conditional damping test

At a C3-fixed stable registry, the lateral relative harmonic port is a real two-dimensional E representation. A scalar vertical or breathing mode is trivial under C3. An invariant bilinear energy $x^Tcz$ would require a fixed vector $c$ in E, so $c=0$. Thus the previously derived $x$–$z$ mixed Hessian vanishes there for a *symmetry reason*, not just the first-shell trigonometric identity. Vertical height may still modulate lateral stiffness through $z|x|^2$; broken symmetry or motion away from the registry changes the selection argument.

For one material shear doublet $y$ that also transforms as E, let $C=aI+bJ$ be its C3-invariant bilinear coupling in Cartesian coordinates, $J=\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}$ and $\rho^2=a^2+b^2$. Take clamped lateral curvature $k_0$, bath curvature $\kappa>0$, bath mass $m_b$, bare damping $\gamma_0$ and bath Rayleigh damping $d\ge0$. Eliminating $y$ at frequency $\omega$ gives

\[
 D_{\rm eff}(\omega)=k_0-m_x\omega^2-i\omega\gamma_0-
 \frac{\rho^2}{\kappa-m_b\omega^2-i\omega d}.\tag{15}
\]

At low frequency and a stable quadratic equilibrium $k_0\kappa>\rho^2$,

\[
 k_{\rm rel}=k_0-\Delta k,\quad
 \Delta k=\frac{\rho^2}{\kappa},\quad
 \gamma_{\rm add}=\frac{d\rho^2}{\kappa^2},\quad
 \frac{\gamma_{\rm add}}{\Delta k}=\frac d\kappa\equiv\tau_b\quad(\Delta k>0).\tag{16}
\]

The last ratio has units of seconds; it is a *conditional passive-bath identity*, not a UD constant or a friction measurement. A sum of independent shear doublets gives a softening-weighted mean of their bath times. A scalar vertical mode cannot contribute through this bilinear mechanism, but bare damping, nonlinear processes and defects remain possible. C3 permits the shear coupling amplitude; it does not determine it or its load response.

The `V_*` used in Eq. (12) must represent *clamped-bath* curvature before Eq. (16)'s softening is subtracted. If the conventional atomistic energy already relaxes $y$, its Hessian is $k_{\rm rel}$ and a second subtraction double-counts the same physics. Ordinary shear modes belong to the conventional baseline unless a separately derived UD source law gives a restriction beyond it. The typed derivation, exact rational symmetry and low-frequency checks, and scope limits are in [6].

## 7. Exact source projection and seven-orbit coupling

The selected Hodge plane is `H=ker B1 ∩ ker B2^T` under the declared unit-edge metric. For the exact lateral map M, `M^T B1^T=M^T B2=0`, so a source of the form `B1^T φ+B2 ψ` has **zero** lateral harmonic projection. This limits incidence-only linear forcing; a local edge field with a harmonic component is still permitted. In particular, take `W=diag(w_e)` with one real value on each of the seven C3 orbits of edges. Then

\[
 K(w)=M^T W B_1^T=\sum_{r=0}^6w_rK_r,\qquad
 K_{\rm cart}(w)K_{\rm cart}(w)^T=\alpha(w)I_2.\tag{17}
\]

The exact orbit order and integer matrix Q are specified in [7]. The scalar has the equivalent connected-orbit-graph form

\[
 \alpha(w)=w^TQw=\frac14\sum_{i<j}c_{ij}(w_i-w_j)^2,\quad
 c_{ij}=-4Q_{ij}\in\{0,1,2\}.\tag{18}
\]

The orbit graph is connected, so alpha vanishes precisely when all seven weights are equal. An overall common weight does not source the harmonic port. The seven values and their scale are **material inputs**, not supplied by K7 or C3.

For the equal-layer relative lift with independent identical 14-component vertex baths on both layers, define an *additional* bilinear energy using a material coefficient `g_c` (J/m² per Bravais cell) and the above weighted gradient. Its Cartesian coupling has `CC^T=g_c² alpha(w) I/2`. Under the same isotropic bath assumptions as Eq. (16),

\[
 \Delta k=\frac{g_c^2\alpha(w)}{2\kappa},\qquad
 \gamma_{\rm add}=\frac{d g_c^2\alpha(w)}{2\kappa^2}.\tag{19}
\]

The factor 1/2 is the equal-layer relative-lift normalization. A single top-layer bath has 1/4 instead. This construction quantifies **which source asymmetry is necessary** but does not choose an orbit pattern, a physical amplitude or a bath time. A fully relaxed conventional atomistic baseline may already contain these contributions. The exact matrix and verifier in [7] make the zero and nonzero cases reproducible.

## 8. Identifiability and a controlled contrast test

The assumed isotropic, degenerate two-layer vertex bath makes the *entire* lateral linear-response denominator depend on the seven orbit weights through only one scalar:

\[
 D_{\rm eff}(\omega;w)=k_0-m_x\omega^2-i\omega\gamma_0-
 \frac{g_c^2\alpha(w)/2}{\kappa-m_b\omega^2-i\omega d}.\tag{20}
\]

Because Q has rank six but the observable depends on just alpha, static softening, damping and even a full frequency sweep cannot invert the six orbit contrasts under this bath assumption. The Jacobian of `(Delta k,gamma_add)` with respect to w has rank one for nonuniform w, and zero at uniform w. Explicit inequivalent patterns `w=e_1` and `w=e_2` in the specified orbit order both have `alpha=1`, equal mean and norm, but differ in their incident weighted-orbit-graph edges [8]. Fitting either to graphite friction cannot choose between them.

A way to test the *source operator* in a mapped simulation is to perturb individually labeled vertex bath coordinates and record both lateral cross-Hessian components. This determines the full K(w), not merely `K K^T`. If its material prefactor is independently known, the contrast vector can be recovered modulo a common offset through

\[
 b_i=\tfrac12\operatorname{tr}[G^{-1}K_iK(w)^T]
 =\sum_jQ_{ij}w_j,\qquad Qw=b,\quad\mathbf1^Tw=0.\tag{21}
\]

The solution is unique under the last gauge because `ker Q=span(1)`. If the measured cross Hessian lies outside the span of the seven K_i, the weighted-gradient source ansatz fails under its declared metric. An actual experiment requires a separate physical identification of the proposed vertex bath variables.

For a C3-preserving, separately imposed weight contrast `w=w_0 1+epsilon v`, the *conditional* static softening and damping are exactly even and quadratic in epsilon. For `v=e_1-e_2`, `v^TQv=5/2`, giving

\[
 \Delta k=\frac{5g_c^2}{4\kappa}\epsilon^2,\qquad
 \gamma_{\rm add}=\frac{5dg_c^2}{4\kappa^2}\epsilon^2.\tag{22}
\]

This describes the declared shear-bath channel with fixed coefficients, not total measured friction under arbitrary strain. A conventional material bath could satisfy the same law; a UD-specific residual still requires an independently sourced restriction beyond that baseline [8].

## 9. Constitutive hypothesis and discriminating test

The planar chain suggests a bounded hypothesis: represent interlayer translation by the **relative harmonic 1-sector**, lift its conservative degeneracy with the ordinary registry potential in Eq. (9), and couple it to an explicitly sourced dissipative environment. For a stable local linearized response with internal stiffness $K\succ0$, damping $D\succeq0$, bare lateral damping $\Gamma_x\succeq0$ and translation-to-internal coupling (C), eliminating the internal coordinates gives

\[
 \Gamma_{\rm eff}=\Gamma_x+CK^{-1}DK^{-1}C^T\succeq0.\tag{23}
\]

A $C_3$-symmetric preparation makes this symmetric two-dimensional damping a scalar matrix. The scalar vertical bath has zero bilinear C by the selection theorem; E-sector bath coupling remains free. Its value and normal-load derivative remain arbitrary without measured or computed (C,K,D) and a physical time calibration. Equation (23) is a conditional open-system law, not a consequence of the closed Hodge–Dirac spectrum. Its local velocity response is not automatically a finite-speed friction coefficient.

A discriminating experiment or simulation would first fix the ordinary honeycomb registry model, measured separation curve, contact geometry, temperature, speed and force estimator independently of held-out traces. The candidate UD coupling must then be fixed from a separate material source and yield a signed, dimensioned residual $F_{\rm obs}-F_{\rm conventional}$ or load derivative at both paired angles. The even angular pairing and a small equilibrium height difference are already conventional controls. The present theory does not supply a parameter-free residual; hence the graphite findings do not yet validate a UD material law.

## 10. Relation to the tetrahedral-octahedral study

The edge-midpoint octahedron is an exact refinement of a three-dimensional tetrahedral chain and remains useful for studying metric transfer. It is not the interface's native planar cellulation. Its 84 active chain coordinates happen to match the 84 three-dimensional atomic displacement coordinates of an ideal 28-atom bilayer, but their $C_3$ representation characters differ: any full-space symmetry-preserving map has rank at most 80. The planar cellular construction instead uses the actual single-layer atom graph and selects the two-dimensional relative translation port by Hodge theory. Neither mathematical construction alone fixes graphite damping or a UD-specific friction residual.

## Reproducibility and scope

The accompanying exact verifier constructs the signed dual and honeycomb boundaries, checks ranks and cellular spectrum, and verifies the harmonic map, its Gram matrix and rotation covariance. A separate seven-cell Fourier calculation verifies shell filtering and the global range; a subsequent stationary-point audit verifies the minimum-path barrier and its load response [2]. These are algebraic results for ideal periodic carriers and specified constitutive assumptions. The new rational verifiers check the two stiffness branches, load derivatives, C3 scalar-mode obstruction, a conditional E-bath response, the seven-orbit source quadratic form, and its inverse-observable rank. The 2023 fixed-height *simulation PES* is fitted in [11]; no 2026 friction curve, independent graphite Hessian, or UD coefficient is used.

### Reference

[1] W. Chen, J. Wang, Q. Zheng and Z. Wu, “Observation of Superlubricity at Commensurate Moiré Graphite Interfaces,” *Physical Review Letters* **137**, 166201 (2026), [doi:10.1103/ly48-b4l2](https://doi.org/10.1103/ly48-b4l2), public abstract.

[2] Exact stationary-point correction and verifier, UD capture `2026-10-22T211956Z-codex-graphite-saddle-bc6b8d85-b918-41a4-9cee-e8fb590d02fa` (this revision).

[3] User-supplied *UD mathematical analysis protocol v1.0*, copied in the new capture; methodological guidance, not a physical law.

[4] Typed BOOT REPORT, exact stiffness/load derivation, and calculation receipt in capture `2026-10-22T212436Z-codex-graphite-method-curvature-6c41e9d2-32a902bf-4e8a-4a8e-9c1f-d090114741c9`.

[5] Oriented-star correction and updated calculation receipt in capture `2026-10-22T212912Z-codex-graphite-star-orientation-f35ed2c0-043c52cd-41cb-42df-a5bf-a410d294cd17`; the sign of the third vector leaves the cosine landscape and Hessian unchanged. This version supersedes v3.

[6] C3 bath-selection theorem, passive elimination, exact checker and method receipt in capture `2026-10-22T213252Z-codex-graphite-c3-bath-7a2d9e16-275252f3-45bf-4752-9517-22de924a34f4` (development only).

[7] Exact weighted-source projection, seven-orbit matrix and checker in capture `2026-10-22T214428Z-codex-graphite-harmonic-source-49d5bb28-64263b7c-7b88-4f45-a8a9-e0cb34f52956`; weights and material damping remain OPEN.

[8] Exact identifiability obstruction, controlled contrast intervention and rational checker in capture `2026-10-22T214903Z-codex-graphite-identifiability-623c4b92-ec0cc8df-242d-4c1b-b6cc-25a083755248`.

[9] A. S. Minkin, I. V. Lebedeva, A. M. Popov, S. A. Vyrko, N. A. Poklonski and Y. E. Lozovik, “Interlayer interaction, shear vibrational mode, and tribological properties of two-dimensional bilayers with a commensurate moiré pattern,” *Phys. Rev. B* **108**, 085411 (2023), [arXiv:2308.06302](https://arxiv.org/abs/2308.06302), especially Eqs. (3)–(7), Tables I–II. Conventional KC simulation, not Chen *et al.* experimental data.

[10] Minkin *et al.*, [raw PES contour data](https://data.mendeley.com/datasets/svnpzbjc3t/1), doi:10.17632/svnpzbjc3t.1 (2023), X/Y in Å; the supplied plotting script converts stored Z differences by 1000 before labeling them μeV. See [11] for a reproducible read-only data fit.

[11] Read-only raw-grid fitting script, JSON results and SHA provenance in this capture. Its residuals belong solely to the imported 2023 KC calculation at fixed height; they have no experimental force units.

[12] Reproducible stationary-point and straight-path derivative replay and JSON in this capture. Requires the exact SHA-checked [10] archive; no source archive program is executed.
