# A planar harmonic carrier for commensurate graphite interfaces

**Research manuscript draft v23 · 22 October 2026**

## Abstract

Graphite interfaces exhibit sharp but weak-load-dependent friction peaks near 21.8° and 38.2° at the (2,1) commensurate moiré orientation [1]. The paired angles follow exactly from triangular-lattice geometry, with cosine 13/14, and are not a new dynamical prediction. We construct the periodic seven-cell honeycomb interface as a 14-vertex, 21-bond, seven-hexagon cellular torus. Its unit-metric chain complex has Betti numbers (1,2,1), and its two harmonic edge coordinates admit an explicit, normalized, rotation-equivariant map from lateral vectors. A bilayer therefore has a selected relative-translation port without identifying the atoms with a three-dimensional tetrahedral subdivision. We also show that the rigid first common reciprocal shell has magnitude $\sqrt7$ times the primitive reciprocal length and, for a real isotropic pair potential truncated to that shell, a global corrugation range $9|V_*|$ per Bravais cell. The minimum-energy-path saddle barrier is $|V_*|$ for positive $V_*$ and $8|V_*|$ for negative $V_*$. The relaxed saddle barrier’s load derivative equals the saddle-to-minimum separation difference. These are conventional geometric and equilibrium identities. The first-shell local stiffness is (3/2)|V_*|g_*² or 3|V_*|g_*² according to the unknown Fourier sign; its exact normal-load slope depends on the vertical derivative and curvature. At a C3-fixed registry, a scalar normal displacement cannot couple bilinearly to the lateral port, whereas a shear E doublet can supply conditional static softening and positive low-frequency damping. An incidence-only exact or coexact source has identically zero harmonic projection; a weighted-gradient source with nonuniform C3 edge-orbit weights can activate it. Its isotropic response depends on only one quadratic combination of seven weights, so friction alone cannot identify the source. The closed cellular generator has no dissipative response on its harmonic port; a material-derived interlayer amplitude, bath, physical time scale and force estimator are required for a distinct residual friction prediction. A three-neighbor local-normal KC extension changes the seven-orbit source fit from 97.59% to 92.50% of squared mixed-Hessian norm; a declared 1.44 eV discrete flexural model softens the local quadratic lateral curvature; nonlinear height minimization changes that tangent result materially and gives a conditional static stiffness load slope. A finite-height spectral calculation at the nonlinear stationary state finds four laterally active modes and zero Ohmic coefficient for the closed harmonic system. The per-unit-loss height response also has a numerically stable conditional load slope near the declared reference, but its conversion to friction requires an independent pressure-dependent loss law and force estimator. A two-channel identifiability audit shows that pressure sweeps alone weakly distinguish the active height-mode losses, while a separately calibrated dynamic response could distinguish them under a stated weak-loss law. None of these conventional results fixes a UD-specific kinetic friction residual.

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

## 4c. Angular controls and the selectivity baseline

Chen *et al.* report detectable friction peaks at the paired index-seven angles and no detectable signal at their other studied commensurate patterns [1]. The independent 2023 fixed-height KC calculations already produce a steep hierarchy. Reading three further raw X/Y/Z grids from the same SHA-checked archive, the index-specific common reciprocal wavevectors at $|g|=\sqrt{N_c}g_0$ recover the first-harmonic coefficient signs and approximate reported static shear strengths [9,10,13]:

| Pattern | $N_c$ | Angle (degrees) | Fitted $U_1$ (μeV/upper atom) | Ideal first-shell static shear (MPa) | Ratio to (2,1) |
| --- | ---: | ---: | ---: | ---: | ---: |
| (2,1) | 7 | 21.787 | $-20.2475$ | 16.741 | 1 |
| (3,1) | 13 | 32.204 | $+4.6600$ | 1.119 | 0.0668 |
| (3,2) | 19 | 13.174 | $+0.43385$ | 0.1259 | 0.00752 |
| (5,1) | 31 | 42.103 | $+0.0011469$ | 0.000425 | $2.54\times10^{-5}$ |

The sign is recoverable from the sum of the three fitted phases: approximately $\pi$ modulo $2\pi$ for (2,1), and zero for the positive-coefficient controls. The source Table II gives rounded coefficients $-20.2$, $+4.66$, $+0.434$, and $+0.00115$ μeV/atom, with strengths 16.7, 1.12, 0.126, and 0.000425 MPa. The amplitude decrease is large enough to make a unique index-seven detection *plausible under a finite threshold*, but neither the threshold nor a conversion from ideal periodic static shear to the 2026 experiment's moving-contact force is available. The complement of each orientation is a sixfold honeycomb geometry relation and does not provide a separate fit. The 2023 archive folder labels disagree with the article's Table I cell sizes for (2,1), (3,1), and (3,2); these are reproducible archive-grid fits, not an assertion of identical calculation runs [13].

Consequently the paired angles, their selectivity, and nonzero index-seven static corrugation are **conventional control results**. A distinct UD material hypothesis must pre-register a source-derived coupling and force observable, then beat a baseline with normal-height relaxation, higher reciprocal shells, finite contact, temperature, rate, and error bars. A failure to see index-thirteen friction cannot by itself select the seven-orbit UD source weights.

## 4d. An independently reconstructed KC height derivative

The source's accessible arXiv bundle contains a supplemental equation and Table S1 parameters for its KC pair interaction [9,14]. For rigid flat layers, $r=(\rho^2+z^2)^{1/2}$ and, in meV and Å,

\[
 v(r,\rho)=-A(z_0/r)^6+\left[C+2e^{-(\rho/\delta)^2}\sum_{n=0}^2C_{2n}(\rho/\delta)^{2n}\right]e^{-\lambda(r-z_0)},\quad
 (A,z_0,C,C_0,C_2,C_4,\delta,\lambda)=(10.238,3.34,3.030,15.71,12.29,4.933,0.578,3.629).\tag{14a}
\]

A separate read-only replay [14] enumerates the 14 top carbon atoms in one coincidence cell with the exact index-seven rotation, sums interactions with a sufficiently extended lower sheet under a declared spherical cutoff, and regresses the resulting $E(x,z)$, $\partial_zE$, and $\partial_z^2E$ on the *same* first common reciprocal star. The analytic derivatives of Eq. (14a) pass a fixed-neighbor finite-difference check. At $z=3.46$ Å and cutoff 16 Å, this reconstruction has first-shell amplitude $19.49$ μeV/upper atom versus $20.25$ μeV/atom in the deposited PES (3.8% low); their sampled spatial fields have correlation 0.99935 after subtracting constants, but a 1.29 μeV/atom centered RMS difference and a $-0.501$ meV/atom mean offset. Therefore the reconstruction is a **qualified comparator** rather than an exact recovery of the source's simulation implementation. Cutoff conventions and run size may differ; the raw grid's energy zero also need not be physically anchored. An explicit constant per retained pair of $A(z_0/R_c)^6=0.00084718$ meV at $R_c=16$ Å, as in one LAMMPS fixed-normal convention, changes the mean reconstruction-minus-grid difference from $-0.50084$ to $-0.25290$ meV/atom, but increases the centered spatial RMS from $1.29210$ to $1.38895$ μeV/atom on the sampled grid [19,20]. It therefore does not establish the archive implementation or repair the corrugation mismatch; the mean offset alone is not evidence of one cutoff convention. Results at 14 and 18 Å bound a small *within-implementation* variation; these choices do not quantify physical model uncertainty.

Let $A_*(z)=|U_1(z)|$ in energy per upper atom, $K_z^m=\partial_z^2E$ at the first-shell negative-branch minimum (meV Å$^{-2}$/atom), and $\sigma=\sqrt3a^2/4$ the area per upper carbon atom. A pressure $P$ in MPa gives compressive force per atom $f=P\sigma/160217.6634$ eV Å$^{-1}$. For positive $K_z^m$, the implicit stationary equation and Eq. (13) imply the *local equilibrium stiffness* response

\[
 \frac{d\ln k_x}{dP}=-\frac{\sigma}{160217.6634\,[K_z^m]_{\rm eV/\AA^2}}\frac{d\ln A_*}{dz}.\tag{14b}
\]

| Pair-sum cutoff | $A_*(3.46\,\AA)$ (μeV/atom) | $d_z\ln A_*$ (Å$^{-1}$) | $K_z^m$ (meV Å$^{-2}$/atom) | $d_P\ln k_x$ (MPa$^{-1}$) |
| --- | ---: | ---: | ---: | ---: |
| 14 Å | 19.02 | −3.917 | 140.413 | $4.56\times10^{-4}$ |
| 16 Å | 19.49 | −3.826 | 140.414 | $4.45\times10^{-4}$ |
| 18 Å | 19.28 | −3.866 | 140.415 | $4.50\times10^{-4}$ |

The first-shell negative-branch fixed-height sliding barrier is $4A_*$ **per atom**. In the weak-corrugation approximation, the same logarithmic slope yields a barrier increment of about $0.0347$ μeV/atom per MPa and a saddle-to-minimum separation difference of about $0.00212$ Å at the reference state. Eq. (11), rather than Eq. (14b), is exact for a fully relaxed saddle; these numbers are leading-order proxies. The fitted second shell changes the fixed-height barrier already, and its height derivative was not extracted here. Contact pressure and measured friction force are also not available. In particular $4.45\times10^{-4}$ MPa$^{-1}$ must **not** be relabeled the Chen *et al.* friction-load slope or a UD prediction. Its practical value is as a concrete conventional comparator for future matched force-versus-load data.

## 4e. Two-shell stationary saddle response to normal load

The previous first-shell load slope is sensitive to the assumed lateral landscape. We extend the **conventional** rigid KC reconstruction to the first and next allowed reciprocal shells (six independent cosine/sine waves), fitting the source SI pair sum's \(E\), \(\partial_z E\), and \(\partial_z^2 E\) on 272 sampled grid positions at \(z_0=3.46\) Å. A quadratic Taylor polynomial in \(z-z_0\) defines a local three-dimensional surrogate. At each of three nearby index-neighbor saddles, we solve both lateral stationarity and \(\partial_z E+L=0\), and independently solve the corresponding minimum. The reference load \(L_0\) is selected to put that reconstructed minimum at 3.46 Å. It is **not a calibrated experimental zero**: at the 16 Å cutoff, \(L_0=-0.17555\) meV Å\(^{-1}\)/atom, equivalent to about \(-10.74\) MPa using the ideal area per atom. Thus the derivative below is a local response to an *increment* in pressure around that reference state; the reference itself is tensile under the declared compression-positive sign.

With pressure increment \(\delta P\), write \(L=L_0+\delta P\,\sigma\,1000/160217.6634\) in meV Å\(^{-1}\)/atom. For each continued saddle \(s\) and minimum \(m\), the enthalpy is \(E(x,z)+L(z-z_0)\), and its **stationary-branch** derivative is

\[
 \frac{d\Delta\mathcal H_s}{dP}
 =\frac{10^6\sigma}{160217.6634}\,[z_s-z_m]
 \quad\text{in }\mu\text{eV atom}^{-1}\text{MPa}^{-1}.\tag{14c}
\]

| Pair cutoff | Three locally relaxed barriers (μeV/atom) | \(z_s-z_m\) (Å) | Local barrier slope (μeV/atom/MPa) |
| --- | ---: | ---: | ---: |
| 14 Å | 73.92–74.04 | 0.0020316–0.0020317 | 0.033215–0.033216 |
| 16 Å | 75.16–75.21 | 0.0020324–0.0020325 | 0.033228–0.033229 |
| 18 Å | 73.75–73.78 | 0.0020317 | 0.033216 |

At 16 Å, a centered \(\pm5\) MPa continuation gives the same slope as Eq. (14c) within \(1.1\times10^{-12}\) μeV/atom/MPa. The two-shell slope is about **4.3% lower** than the prior leading first-shell proxy of 0.03472 μeV/atom/MPa. The barrier's larger cutoff sensitivity and its difference from the deposited-grid fixed-height two-shell barrier (~78.2 μeV/atom) track the already disclosed source reconstruction mismatch. The source method specifies a 16 Å cutoff for this pattern, but the deposited folder is labeled 10x10 while the paper's Table I states 18x18; the exact simulation run and cutoff implementation cannot be established from these inputs.

Equation (14c) is exact for stationary branches of the **declared local surrogate**; the numbers inherit its two-shell truncation, second-order height approximation, rigid sheets, local saddle selection and KC implementation mismatch. We have not proved a global relaxed minimum-energy path or converted this barrier derivative into kinetic friction. Neither the absolute 2026 contact pressure nor its force traces are available. These numbers therefore sharpen a conventional comparator; they do not determine the remaining UD residual or its damping [15].

## 4f. A force-observable counterexample

The two-shell pressure derivative is a derivative of a conservative stationary enthalpy barrier. To make the missing force-observable step explicit, consider a **declared illustrative one-dimensional overdamped model** with period \(\ell\), barrier \(\Delta(P)>0\), drag \(\gamma(P)>0\), and constant applied drive \(F\):

\[
 U(x,P)=\frac{\Delta(P)}2[1-\cos(2\pi x/\ell)],\qquad
 \gamma(P)\dot x=F-\partial_x U,\qquad
 F_c(P)=\frac{\pi\Delta(P)}{\ell}.\tag{14d}
\]

For \(F>F_c\), one period takes \(T=\gamma\int_0^\ell dx/[F-F_c\sin(2\pi x/\ell)]=\gamma\ell/\sqrt{F^2-F_c^2}\). Thus, at prescribed mean speed \(v=\ell/T\), the required total drive and its pressure derivative are exactly

\[
 F_{\rm drive}(P,v)=\sqrt{F_c(P)^2+[\gamma(P)v]^2},\qquad
 \left.\frac{\partial F_{\rm drive}}{\partial P}\right|_v
 =\frac{F_cF_c'+\gamma\gamma'v^2}{F_{\rm drive}}.\tag{14e}
\]

If the instrument defines interfacial excess force as \(F_{\rm excess}=F_{\rm drive}-\gamma v\), its derivative is Eq. (14e) minus \(\gamma'v\). These are different observables when damping depends on pressure. For pressure-independent \(\gamma\), put \(u=\gamma v/F_c\); the positive barrier-derived depinning slope is suppressed by \(1/\sqrt{1+u^2}\). At any finite \(v\), a local smooth positive drag law can also make the *total* force slope vanish exactly: \(\gamma'/\gamma=-(F_c'/F_c)u^{-2}\). A distinct choice, \(\gamma'/\gamma=(F_c'/F_c)[u(\sqrt{1+u^2}-u)]^{-1}\), makes the *excess* force slope vanish. These constructions are local counterexamples, not fits or claims about graphite damping.

For scale only, take \(\ell=0.929608\) Å from a nearest translation in the 2023 grid [12] and set the model barrier to the 16 Å **reconstructed** value \(\Delta=75.18\) μeV/atom with \(\Delta'=0.033228\) μeV/atom/MPa from Sec. 4e. This gives \(F_c=254.07\) μeV Å\(^{-1}\)/atom or 15.54 MPa on ideal atom area, with \(F_c'=0.11229\) μeV Å\(^{-1}\)/atom/MPa. The sinusoidal path is an intentionally simplified surrogate and does not inherit the actual two-shell force shape:

| Reduced speed \(u=\gamma v/F_c\) | Fixed-\(\gamma\) slope factor | Illustrative total-force slope (shear MPa / normal MPa) |
| ---: | ---: | ---: |
| 0.1 | 0.9950 | 0.006834 |
| 1 | 0.7071 | 0.004857 |
| 10 | 0.09950 | 0.0006834 |

The replay [16] checks the analytic period integral by numerical quadrature, its pressure derivative by centered differences, and both zero-slope drag identities. It demonstrates **non-identifiability**: a PES and barrier-load derivative do not alone fix a moving-contact force slope. Neither \(\gamma\), physical velocity, finite-contact path, temperature nor Chen *et al.*'s force estimator is established here. An eventual UD test must freeze the conventional dynamic force model and measured drag from independent controls, then derive a distinct UD material coupling and compare held-out force-versus-pressure curves at *both* paired angles. A small measured slope by itself does not isolate UD dynamics.

## 4g. Driven response along the reconstructed two-shell path

The sinusoid in Sec. 4f illustrates the force-observable obstruction, but its force shape was stipulated. We now keep the **two-shell reconstructed KC lateral shape** from Sec. 4e at the 16 Å cutoff, with its fitted \(E_0(x)\), \(E_{z0}(x)\), and \(K_z(x)=E_{zz0}(x)\) at \(z_0=3.46\) Å. The local quadratic height surrogate can be minimized analytically at each lateral position:

\[
 z_*(x,L)-z_0=-\frac{E_{z0}(x)+L}{K_z(x)},\qquad
 E_{\rm eff}(x,L)=E_0(x)-\frac{[E_{z0}(x)+L]^2}{2K_z(x)}+Lz_0.\tag{14f}
\]

Choose each of three nearest **straight periodic translation paths** \(x(s)=x_m+s\hat d\), \(0\le s<\ell=0.929608\) Å, through the reference stationary minimum. For positive drive, let \(f(s,P)=\partial_sE_{\rm eff}\) and \(F_c(P)=\max_s f(s,P)\). When drag \(\gamma\) is independent of pressure, overdamped deterministic transport at prescribed mean velocity \(v\) requires the unique drive \(F>F_c\) satisfying

\[
 \gamma v=
 \left[\frac1\ell\int_0^\ell\frac{ds}{F-f(s,P)}\right]^{-1}.\tag{14g}
\]

This is a force estimator for the **declared path and drive protocol**, not a replacement for an instrument model. The same reference load as Sec. 4e puts the reconstructed minimum at 3.46 Å: \(-10.74\) MPa on the compression-positive convention. Numerical integration and root solving with 8,192 periodic samples, using centered \(\pm5\) MPa increments, give:

| Path | \(F_c\) (ideal shear MPa) | \(dF_{\rm drive}/dP\) at \(\gamma v/F_c=0.1\) | At 1 | At 10 |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 15.557 | 0.006850 | 0.004862 | 0.0006832 |
| 2 | 15.582 | 0.006850 | 0.004863 | 0.0006827 |
| 3 | 15.551 | 0.006850 | 0.004862 | 0.0006835 |

The three right columns are dimensionless ratios of ideal shear MPa to pressure MPa, **not measured coefficients of friction**. The local depinning-force slope is \(0.11254\) μeV Å\(^{-1}\)/atom/MPa, nearly equal across the three paths. The direct path at reduced speed 1 gives 0.004862, versus 0.004857 in Sec. 4f's sinusoid with the same approximate barrier and period. Thus the speed suppression in this **model** is not caused by choosing a single sinusoid. Grid counts 2,048/4,096/8,192 agree in the path-1 speed-1 slope to better than \(4\times10^{-11}\) meV Å\(^{-1}\)/atom/MPa; pressure halfspans 1, 2, and 5 MPa differ by less than \(5\times10^{-10}\) in the same units [17].

The result inherits the 1.29 μeV/atom centered RMS mismatch to the deposited KC grid, the 16 Å cutoff convention, second-order height Taylor approximation, rigid layers, arbitrarily constrained straight path, zero temperature and constant unmeasured drag. The three paths are related by near-symmetry of this reconstruction; they do not sample three independently measured angles. A free two-dimensional sliding path, moving finite contact, laboratory force protocol, rate and pressure series, and material-derived UD damping are still required. Equation (14g) supports a **conditional conventional dynamic comparator**; it does not demonstrate a UD residual.

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

## 7a. Fixed-normal atom-height probe and the limit of seven edge orbits

The weighted-gradient source in Eq. (17) has so far carried undetermined material coefficients. A conditional atom-height probe is possible without treating it as UD evidence: continue the **flat-layer reconstructed KC pair law** from Sec. 4d to individual vertical displacements \(z_j\) of the 14 upper-layer atoms while holding all upper and lower surface normals fixed along $\hat z$. This is a declared fixed-normal extension resembling KC/z [19], not the full KC deformation energy [21]. At the fixed-height two-shell lateral minimum, form the mixed Hessian of the **mean energy per upper atom**

\[
 C_{\alpha j}^{\rm KC,z}
   =\left.\frac{\partial^2 E_{\rm KC,z}/\partial x_\alpha\partial z_j}
                   {14\ {\rm upper\ atoms}}\right|_{x_m,z_j=3.46\,{\rm\AA}},
 \qquad \alpha=1,2,\quad j=1,\ldots,14.\tag{24a}
\]

Here \(E_{\rm KC,z}\) in the numerator is the *total* cell interaction energy before division by 14. Thus \(C^{\rm KC,z}\) has units meV Å\(^{-2}\) **per upper atom of the cell average**. A uniform vertical displacement corresponds to the sum of its 14 columns. The reconstructed finite-patch sum gives a small uniform mixed term \((0.00201,0.000783)\) meV Å\(^{-2}\)/atom, versus a Frobenius norm of approximately 15.88 in those units. Its small nonzero value reflects this finite implementation; the ideal \(C_3\)-fixed scalar channel vanishes exactly by symmetry.

Registration matters. The rotated upper coincidence cell has intrinsic primitive quotient \(k=q-2p\pmod7\) after swapping primitive labels to match the carrier's bond classes \(0,1,5\). Its Cartesian carrier map is \(K_r^{\rm cart}=(A R S)^{-T}K_r\), with \(A\) the primitive basis matrix and \(S\) the swap. Of seven cyclic label offsets, **offset 2** is selected by the independent \(C_3\) covariance check: its normalized equivariance defect is 0.00143, while the other offsets range 1.527–1.528. This selection uses the physical rotation, not the fit of \(C^{\rm KC,z}\) to the source family. A source-space projection at an arbitrary unregistered offset would have produced a false 88.5% norm residual.

With the symmetry-selected registration, least squares projects \(C^{\rm KC,z}\) onto \(\operatorname{span}\{K_r^{\rm cart}\}_{r=0}^6\), fixing the common-weight gauge by \(\sum_r b_r=0\). The source subspace has rank six. At the 16 Å cutoff and lateral step \(10^{-4}\) Å, the fit has a **15.5176% Frobenius norm residual**, hence captures **97.5921% of the squared norm**. The gauge-fixed coefficient products are approximately

\[
 b=(-0.3355,\ 1.2266,\ -10.0096,\ 18.2371,\
       -10.0096,\ 1.2266,\ -0.3355)
 \quad {\rm meV\,\AA^{-1}\ per\ upper\ atom}.\tag{24b}
\]

The percentage and coefficients hold only for this frozen-normal, rigid-lower-sheet probe. In full KC [21], $\rho_{ij}^2=r_{ij}^2-(r_{ij}\cdot n_i)^2$ depends on the *local upper normal* $n_i(\{z_l\})$. At the initially flat state, writing $r_{ij}=(s_{ij},z)$ and $n_i=\hat z$, the difference from the fixed-normal continuation for an upper height $z_l$ is

\[
 \left.\frac{\partial \rho_{ij}^2}{\partial z_l}\right|_{\rm full}
 -\left.\frac{\partial \rho_{ij}^2}{\partial z_l}\right|_{\rm fixed}
 =-2z\,s_{ij}\cdot\frac{\partial n_i}{\partial z_l}.\tag{24c}
\]

Each pair therefore supplies an additional derivative $e^{-\lambda(r-z_0)}f'(\rho_{ij}^2)(-2z\,s_{ij}\cdot\partial_{z_l}n_i)$, whose lateral derivative enters the mixed Hessian. Neighbor heights rotate normals even when pair distance $r_{ij}$ itself is unchanged. The three-neighbor and semilocal prescriptions can differ [21], and an intralayer force law is needed to relax the heights. The sign and size of the resulting change to the 15.5176% residual or its coefficient vector depend on the local-normal prescription; the three-neighbor case is calculated in Sec. 7b. The exact $8$-versus-$6$ representation count does not depend on this constitutive choice; its quantified projection does. A specified local-normal implementation must validate derivatives, include intralayer stiffness, and recompute the registered $2\times14$ map before its coefficients enter a damping law.

The products are not separately identified UD orbit weights and coupling strength. The residual norm varies by less than \(1.1\times10^{-6}\) across cutoffs 14, 16 and 18 Å and lateral differences \(10^{-3}\)–\(10^{-5}\) Å. The \(C_3\) symmetry-breaking part is only 0.000827 of the matrix norm; after averaging it away, the symmetry-allowed residual is still 0.155173. This is therefore an unresolved **allowed coupling channel within the declared conventional reconstruction**, not merely a finite-difference artifact [18].

There is also an exact dimensional obstruction to universal completeness of Eq. (17). Under the carrier's \(C_3\) action, the 14 scalar vertex coordinates comprise two fixed vertices and four three-vertex cycles. Each cycle contributes two real equivariant maps into the lateral E plane, so \(\dim\operatorname{Hom}_{C_3}(\mathbb R^{14},E)=8\), whereas the seven-orbit weighted-gradient span has rank six. Two symmetry-allowed real directions are missing even if the weights are freely chosen. A material model may supply them, but they cannot be attributed to Eq. (17) or called a UD-specific signature. The source Hessian is a **fixed-normal conventional control**, not the full KC or experimentally constrained coupling. A normal-mode stiffness and physical dissipative kernel are required to obtain \(\gamma_{\rm add}\), and a distinct UD law still needs an independently fixed restriction beyond the conventional model.

## 7b. Three-neighbor local-normal KC extension

To test the missing term rather than infer it, choose the **local three-neighbor** normal permitted by the original KC construction [21]. For each upper atom $i$, let $d_{ik}$ be its three planar nearest-neighbor vectors of bond length $b=1.42$ Å, separated by $120^\circ$, and let $h_k$ be the corresponding neighboring height perturbations. Averaging the normalized cyclic cross products of the three atom-to-neighbor bond vectors, and then normalizing their sum, has the linearization

\[
 n_i=\hat z-\frac{2}{3b^2}\sum_{k\in N(i)}d_{ik}(h_k-h_i)+O(h^2)
     =\hat z-\frac{2}{3b^2}\sum_{k\in N(i)}d_{ik}h_k+O(h^2).\tag{25a}
\]

The central-height term cancels because $\sum_kd_{ik}=0$. Neighbor heights outside the 14-atom coincidence cell are mapped periodically to its corresponding labeled sites. The lower sheet and its normals remain rigid. Equation (25a) selects **one** KC local-normal convention; it does not model a semilocal normal, intralayer elasticity, or self-consistent height relaxation. Substituting (25a) into Eq. (24c) gives the missing pair contribution to the derivative with respect to a neighbor height, with $u=\rho^2/\delta^2$:

\[
 \delta_{n}\frac{\partial E}{\partial h_k}
 =\frac1{14}\sum_{i:k\in N(i)}\sum_{j\in\text{lower}}
 \frac{4z}{3b^2}
 e^{-\lambda(r_{ij}-z_0)}
 \frac{e^{-u}}{\delta^2}
 [C_2+2C_4u-(C_0+C_2u+C_4u^2)]
 (s_{ij}\cdot d_{ik}),\tag{25b}
\]

where the pair sum is restricted to the declared spherical cutoff and normalized by 14 for a cell-average energy. Taking a central lateral difference of Eq. (25b) yields the added $2\times14$ mixed Hessian. A separately coded nonlinear full pair energy with these height-dependent normals verifies its height-force vector to $1.5\times10^{-9}$ meV Å$^{-1}$/atom and its mixed Hessian by independent four-point energy differences to $2.94\times10^{-7}$ meV Å$^{-2}$/atom. Finite-differencing the cross-product normal itself checks Eq. (25a) to $1.1\times10^{-11}$ Å$^{-1}$ [22].

At the same reconstructed two-shell minimum, with the same C3-selected label offset 2 and source basis as Sec. 7a, the numerical comparison is:

| Upper normal rule | $\|C\|_F$ (meV Å$^{-2}$/atom) | Seven-orbit residual $\|C-P_{\mathcal K}C\|_F/\|C\|_F$ | Squared norm in source span | C3 defect |
| --- | ---: | ---: | ---: | ---: |
| Fixed $\hat z$ | 15.8810 | 0.155176 | 97.5921% | 0.001433 |
| Three-neighbor local normal | 20.9090 | 0.273806 | 92.5031% | 0.001471 |

The normal-rotation correction alone has norm $6.40387$ meV Å$^{-2}$/atom, **40.324% of the frozen-normal Hessian norm**. At cutoff 16 Å, the fitted gauge-fixed products change from approximately $(-0.3355,1.2266,-10.0096,18.2371,-10.0096,1.2266,-0.3355)$ to

\[
 b^{(3N)}=(3.6066,-3.8330,-12.8077,26.0681,-12.8077,-3.8330,3.6066)
 \quad{\rm meV\,\AA^{-1}\ per\ upper\ atom}.\tag{25c}
\]

The selected offset's C3 defect is 0.001471; all six other cyclic offsets exceed 1.5269. Repeating the calculation at cutoffs 14, 16 and 18 Å gives full-normal residuals 0.273805–0.273807; varying lateral difference from $10^{-3}$ to $10^{-5}$ Å leaves the 16 Å residual within $2\times10^{-7}$. These are *implementation checks*, not uncertainty bounds on real graphite. The large change from the fixed-normal projection demonstrates that its 97.6% overlap cannot be treated as a robust material signature. The rank-six source remains an incomplete subset of the exact eight-dimensional C3-allowed map space.

This calculation supplies a **conventional static cross-Hessian for one declared local-normal KC variant**. It does not supply the 14-height stiffness matrix, an intralayer force field, damping kernel, contact model or measured load-dependent sliding force. Semilocal normals or a different interlayer potential can change the coefficients again. No UD-specific residual or friction prediction follows from the fit alone [22].

## 7c. A conditional flexural stiffness and quadratic relaxation

A static height coupling becomes a *lateral response* only after the height stiffness is specified. We add a transparent discrete plate law, not a fitted UD term. For upper-site heights $h\in\mathbb R^{14}$, let $L=3I-A$ be the periodic nearest-neighbor honeycomb graph Laplacian, $b=1.42$ Å, and $a_{\rm atom}=3\sqrt3 b^2/4$. Its acoustic long-wave expansion is $Lh\simeq-(3b^2/4)\nabla^2h$. Discretizing the continuum bending energy $(D/2)\int(\nabla^2h)^2dA$ as a 14-site mean energy gives

\[
 E_{\rm bend}/14=\frac{D a_{\rm atom}}{28}
   \left(\frac4{3b^2}\right)^2\|Lh\|^2,\qquad
 K_{\rm bend}(D)=\frac{D a_{\rm atom}}{14}
   \left(\frac4{3b^2}\right)^2 L^2.\tag{26a}
\]

Here $D$ has energy units. The graph spectrum is $0,6,3-\sqrt2,3+\sqrt2$ with multiplicities $1,1,6,6$. Equation (26a) has the correct flexural $q^4$ *acoustic* limit, while its optical and finite-wave behavior is a chosen discretization. Published monolayer bending values include a theoretical 1.44 eV [24] and a measured/model range 1.2–1.7 eV [25]; using them at this 14-site wavelength is an illustrative transfer, not a calibration of an atomistic force field.

Let $C$ be the registered $2\times14$ mixed Hessian from Sec. 7b, $H_{hh}^{\rm KC}$ the nonlinear pair energy's height Hessian per mean upper atom, and $H_{xx}$ its fixed-height lateral Hessian. When $K(D)=H_{hh}^{\rm KC}+K_{\rm bend}(D)$ is positive definite, minimizing the **local quadratic Taylor model** over $h$ gives

\[
 H_{xx}^{\rm quad-rel}(D)=H_{xx}-C K(D)^{-1}C^T,\qquad
 \Delta H(D)=C K(D)^{-1}C^T\succeq0.\tag{26b}
\]

The nonzero reference height force sets the linear shift; a compression-positive uniform load can cancel its uniform component. Its nonuniform component changes the quadratic reference heights by $-K^{-1}(g_h-\bar g_h\mathbf1)$. This is a tangent approximation: no nonlinear minimization or force-versus-load trace is claimed. The lower sheet stays rigid.

Four-point energy differences of the same reconstructed pair sum give $\lambda_{\min}(H_{hh}^{\rm KC})=-8.3814$ meV Å$^{-2}$ per mean atom for the three-neighbor normal rule; the isolated interlayer height form is therefore indefinite. The declared plate contribution stabilizes this cell at $D>0.0221$ eV, according to the Schur complement of the uniform mode. At $D=1.44$ eV the smallest eigenvalue of $K$ is 9.98 meV Å$^{-2}$/atom. A cutoff-sensitive $10^{-3}$ Å lateral energy difference spuriously gave a negative lateral eigenvalue: it crosses the sharp 16 Å pair roster. The local $10^{-4}$ Å difference has $H_{xx}\simeq1.59203 I_2$ meV Å$^{-2}$/atom and agrees with $3\times10^{-4}$ Å. This cutoff step check is necessary before interpreting the softening [23].

| Normal rule | $D$ (eV) | $\Delta H$ scalar (meV Å$^{-2}$/atom) | $H_{xx}^{\rm quad-rel}$ scalar (same units) | Fractional softening |
| --- | ---: | ---: | ---: | ---: |
| Frozen | 1.44 | 0.106856 | 1.485174 | 6.712% |
| Three-neighbor | 1.20 | 0.270253 | 1.321777 | 16.975% |
| Three-neighbor | 1.44 | 0.226362 | 1.365668 | 14.218% |
| Three-neighbor | 1.70 | 0.192497 | 1.399533 | 12.091% |

The Euclidean source-space fit in Sec. 7b does **not** measure coverage of the relaxed response. Write $C=C_{\mathcal K}+R$ for its orthogonal Frobenius projection onto the rank-six seven-orbit space and its complement. At $D=1.44$ eV the isotropic softening in Eq. (26b) decomposes algebraically as

\[
 \Delta H=\underbrace{C_{\mathcal K}K^{-1}C_{\mathcal K}^T}_{0.116112}
 +\underbrace{RK^{-1}R^T}_{0.046524}
 +\underbrace{C_{\mathcal K}K^{-1}R^T+RK^{-1}C_{\mathcal K}^T}_{0.063726}
 =0.226362\ I_2
 \quad(\mathrm{meV\,\AA^{-2}/atom}).\tag{26d}
\]

The source-only term is **51.3% of the full softening**, even though $C_{\mathcal K}$ carries 92.5% of $C$'s ordinary squared norm. The cross term has no unique source-versus-complement attribution; it is kept separately. In the fixed-normal control, the corresponding source-only fraction is 70.8%. Thus the seven-orbit ansatz cannot replace the omitted symmetry-allowed coupling directions when predicting relaxation under this declared stiffness.

The $C_3$-equivariant tensor is isotropic up to the small finite-patch discrepancy. For the three-neighbor $D=1.44$ eV case, the linear nonuniform height shift is at most 0.00418 Å. Repeating the height Hessian with 0.001 and 0.003 Å steps changes its entries by at most $2.4\times10^{-4}$ meV Å$^{-2}$/atom. These are numerical checks of this reconstruction, not error bars for graphite [23].

A passive *stipulated* height Rayleigh matrix $D_h=dI_{14}$ in the same mean-energy coordinates gives the low-frequency bath contribution

\[
 \Gamma_{\rm add}=C K^{-1}D_hK^{-1}C^T,
 \qquad \left.\frac{\Gamma_{\rm add}}d\right|_{D=1.44\,{\rm eV},\ 3N}
 \simeq 5.2471\times10^{-4}I_2.\tag{26c}
\]

The corresponding frozen-normal factor is $2.1494\times10^{-4}I_2$. These dimensionless ratios multiply an **unknown, unmeasured** $d$; they are not damping in physical units until that loss law and time scale are independently established. They also do not yield the measured friction-load slope. The plate stiffness affects static softness, but neither its conventional provenance nor the $C_3$ carrier selects a UD-specific residual. Independent atomistic intralayer force constants, normal-rule validation and a measured or computed loss spectrum are the next material inputs.

## 7d. Nonlinear local height relaxation and pressure derivative

The Schur result above is a tangent at the flat reference state, which has a nonuniform vertical force. To determine its range of validity, retain the same three-neighbor KC pair law, the 14-site $D=1.44$ eV plate, and the **fixed set $\mathcal R$ of 4106 interlayer pairs inside the 16 Å cutoff at the reference registry**. This fixed-roster analytic continuation removes pair-entry jumps while keeping the local pair formula. For the mean energy per upper atom and a uniform normal force $\ell$ per atom, minimize

\[
 \mathcal E(x,h;\ell)=\bar E_{\rm KC}^{\mathcal R}(x,h)
 +\tfrac12 h^T K_{\rm bend} h
 +\ell\,\frac{\mathbf1^Th}{14},\qquad
 \ell_0=-\sum_j\partial_{h_j}\bar E_{\rm KC}^{\mathcal R}(x_0,0).
 \tag{27a}
\]

The reference $\ell_0=-0.175482$ meV Å$^{-1}$/atom is about **$-10.734$ MPa** on the ideal atom area, compression positive. It is a tensile numerical reference selected to cancel the flat collective-height force, **not** an experimental zero-load condition. The bounded local search allows two lateral and all 14 upper height coordinates to move; the lower layer stays rigid. At $\ell_0$, it converges with maximum gradient $6.1\times10^{-7}$ meV Å$^{-1}$/atom. The lateral displacement from the v19 reference is $(0.000330,0.000128)$ Å, while upper height offsets range from $-0.004163$ to $+0.002165$ Å (mean $-0.001430$ Å). The original hard-cutoff pair membership is unchanged at the optimum and all five pressure points below [26].

At this stationary state, the Hessian Schur formula is the *local derivative of the nonlinear height-minimized energy*:

\[
 H_{xx}^{\rm nonlin-rel}
 =H_{xx}^*-C_*K_*^{-1}C_*^T,
 \quad K_*=\partial_h^2\mathcal E(x_*,h_*;\ell_0)>0.
 \tag{27b}
\]

| Evaluation point | Clamped lateral curvature | Height relaxation correction | Relaxed lateral curvature |
| --- | ---: | ---: | ---: |
| Flat tangent, Eq. (26b) | 1.59203 | 0.22636 | 1.36567 |
| Nonlinear stationary state, Eq. (27b) | 1.91187 | 0.22934 | 1.68253 |

All entries are isotropic scalar parts in meV Å$^{-2}$ per mean upper atom. Thus carrying the flat-state $1.36567$ through as a *nonlinearly relaxed prediction* would miss a nonlinear value **23.2% above that tangent**; most change comes from the clamped curvature evaluated at the new heights, rather than failure of Schur elimination. Two independent Hessian step choices $(\delta x,\delta h)=(10^{-4},10^{-3})$ and $(3\times10^{-4},3\times10^{-3})$ Å give 1.68253 and 1.68254. Independently minimizing heights at each displaced lateral position gives a centered profile curvature 1.68251 at $\delta x=0.002$ Å. The smallest height-stiffness eigenvalue is approximately 10.00 meV Å$^{-2}$/atom [26].

Normal-load increments $\delta P$ map to $\delta\ell=(a_{\rm atom}\,1000/160217.6634)\delta P=0.0163489\,\delta P$ meV Å$^{-1}$/atom with $\delta P$ in MPa. At each load the **same** local model is minimized again:

| $\delta P$ (MPa) | Mean upper height offset (Å) | Relaxed curvature (meV Å$^{-2}$/atom) |
| ---: | ---: | ---: |
| −5 | −0.000846 | 1.678647 |
| −2.5 | −0.001138 | 1.680591 |
| 0 | −0.001430 | 1.682532 |
| +2.5 | −0.001722 | 1.684472 |
| +5 | −0.002013 | 1.686413 |

Centered slopes over $\pm2.5$ and $\pm5$ MPa are respectively $0.00077612$ and $0.00077665$ meV Å$^{-2}$/atom/MPa. The local logarithmic slope is about $4.61\times10^{-4}$ MPa$^{-1}$ at the numerical reference. Repeating the base nonlinear relaxation at cutoffs 14 and 18 Å gives 1.68935 and 1.67968 meV Å$^{-2}$/atom, versus 1.68253 at 16 Å, with each cutoff's reference pair roster held fixed. This is a within-model cutoff sensitivity, not a physical uncertainty interval.

The registered seven-orbit projection remains incomplete after relaxation: it captures **93.16% of the ordinary squared cross-Hessian norm**, but the projected source by itself supplies only **53.39% of the nonlinear-state quadratic softening** (0.122437 of 0.229339 meV Å$^{-2}$/atom). Complement-only and cross terms supply 0.043384 and 0.063518 respectively; the cross term has no unique attribution. The omitted directions cannot be ignored in this declared static response [26].

These values are local stiffnesses and derivatives near a *tensile numerical reference*. They are not a minimum-energy sliding barrier, finite-speed friction force, or the experiment's load slope. The fixed-roster continuation, chosen flexural dispersion at the supercell wavelength, finite lower sheet, source PES mismatch, ideal pressure area and lower-layer rigidity all remain material assumptions. The paired-angle geometry and ordinary KC commensurability still form the baseline; no independent UD damping or signed residual is established.

## 7e. Finite-height spectrum and the dissipation boundary

The v20 stationary Hessian admits a direct finite-mode audit. For the declared 16 Å fixed-roster model, let $K_*\in\mathbb R^{14\times14}$ and $C_*\in\mathbb R^{2\times14}$ denote the height block and lateral-height block of Eq. (27b). With orthonormal height modes $K_*v_j=\kappa_jv_j$ and $c_j=C_*v_j$, the eliminated **retarded conservative** stiffness correction is

\[
 \Sigma(\omega)=C_*[K_*-\mu(\omega+i0^+)^2I]^{-1}C_*^T
 =\sum_{j=1}^{14}\frac{c_jc_j^T}{\kappa_j-\mu(\omega+i0^+)^2},
 \qquad \mu=m_{\rm C}/14.\tag{28a}
\]

Here the energy is normalized per 14 upper atoms, so the kinetic energy in those units is $\frac12(m_{\rm C}/14)\dot h^T\dot h$; the lower layer remains rigid. The mass choice $m_{\rm C}=12u$ converts the *assumed model* eigenvalues to illustrative frequencies $f_j=(2\pi)^{-1}\sqrt{14\kappa_j/m_{\rm C}}$, using the 2022 CODATA units [27]. This mass assignment and the chosen bending plate are not measured phonon data. $K_*$ is positive, with smallest eigenvalue $9.9990$ meV Å$^{-2}$ per mean upper atom, so no zero-frequency height pole is hidden in the reduction.

| Height modes, ascending $\kappa$ | $\kappa$ (meV Å$^{-2}$/atom) | Illustrative $f$ (THz) | Contribution to $\tfrac12\mathrm{tr}\,\Sigma(0)$ (meV Å$^{-2}$/atom) |
| --- | ---: | ---: | ---: |
| 5–6, E doublet | 307.9743 each | 9.3709 | 0.0762368 each |
| 8–9, E doublet | 2297.2933 each | 25.5937 | 0.0384327 each |
| Remaining 10 modes | 9.9990–4250.9784 | 1.6885–34.8152 | $<1.2\times10^{-15}$ combined |
| All 14 | — | — | **0.2293391** |

The two active doublets exhaust the lateral coupling to numerical precision under this symmetric, declared normal rule. The softer active doublet supplies **66.48%** of the static Schur correction. The apparently softer 1.6885 THz model height mode is symmetry decoupled here; calling it the dominant sliding channel would be incorrect. Summing the 14 mode residues reproduces $C_*K_*^{-1}C_*^T$ elementwise, approximately $0.22933910 I_2$ with off-diagonal magnitude below $4\times10^{-10}$ meV Å$^{-2}$/atom. A second Hessian step choice gives $0.2293308$ and the same active mode indices; cutoffs 14/16/18 Å give respectively $0.22933868$, $0.22933910$, $0.22933919$ in their separately stationary local models [28]. These are numerical checks, not an independently calibrated uncertainty.

For frequencies below the first active pole the finite conservative resolvent is analytic and real:

\[
 \Sigma(\omega)=C_*K_*^{-1}C_*^T
 +\mu\omega^2 C_*K_*^{-2}C_*^T+O(\omega^4),
 \qquad \lim_{\omega\to0^+}\frac{\operatorname{Im}\Sigma(\omega)}{\omega}=0.\tag{28b}
\]

Real-frequency poles represent reversible energy exchange and discrete spectral lines, not a finite DC drag coefficient. This is a **NO-GO for Ohmic damping from this finite, closed, locally harmonic height model**; it does not exclude dissipation from nonlinear thermal dynamics, a substrate, an infinite bath or other open material channels. It also does not turn a stationary stiffness derivative into a friction-load derivative.

If an independently supplied material model instead adds a Rayleigh height loss $D_h=dI$ in these mean-energy coordinates, the conditional low-frequency coefficient would be

\[
 \Gamma_{\rm add}=d\,C_*K_*^{-2}C_*^T
 \simeq d\,(5.28545\times10^{-4})I_2.\tag{28c}
\]

The softer active doublet contributes **93.67%** of this *per-unit-$d$* coefficient, and the other doublet contributes the balance. The value of $d$, its mode dependence and time units are **OPEN**. For mode-dependent linewidths $d_j$, Eq. (28c) generalizes to $\sum_j d_jc_jc_j^T/\kappa_j^2$ only when the loss law is diagonal in this basis. A computed or measured linewidth for the laterally active channels, with the lower layer and long-wavelength modes restored, is the next material input; the carrier geometry alone cannot provide it.

## 7f. Conditional load susceptibility of the dissipative channel

The modal calculation fixes the conservative blocks $C_*(P)$ and $K_*(P)$ at each relaxed normal load, but does not fix the loss operator. To quantify precisely what is available before that input, hold the **unmeasured** mean-energy Rayleigh coefficient $D_h=dI$ constant across a narrow pressure interval. Then the candidate *per-unit-loss* tensor is

\[
 G(P)=C_*(P)K_*(P)^{-2}C_*(P)^T,
 \quad \Gamma_{\rm add}(P)=dG(P),\quad
 \frac{d\Gamma_{\rm add}}{dP}=dG'(P)
 \quad\text{only if }d'(P)=0.\tag{29a}
\]

$G$ is dimensionless in this normalization; $d$ carries damping units. The pressure is the v20 ideal atom-area conversion, referenced to the tensile numerical load $\ell_0=-0.175482$ meV Å$^{-1}$/atom (about $-10.734$ MPa compression positive). It is not an experimental zero. At each increment the 16-coordinate state is reoptimized with the same fixed pair roster and then its $K,C$ blocks are differentiated numerically. The four active height modes remain modes 5, 6, 8 and 9 throughout $\pm5$ MPa [29].

| $\delta P$ (MPa) | $\frac12\operatorname{tr}G(P)$ | Static Schur correction (meV Å$^{-2}$/atom) |
| ---: | ---: | ---: |
| $-5$ | $5.26415856\times10^{-4}$ | 0.22839291 |
| $-2.5$ | $5.27479989\times10^{-4}$ | 0.22886584 |
| $0$ | $5.28544758\times10^{-4}$ | 0.22933910 |
| $+2.5$ | $5.29610163\times10^{-4}$ | 0.22981267 |
| $+5$ | $5.30676189\times10^{-4}$ | 0.23028656 |

Centered differences at $\pm2.5$ and $\pm5$ MPa give $G'_{\rm iso}=4.2603480\times10^{-7}$ and $4.2603333\times10^{-7}$ MPa$^{-1}$ respectively. Thus, under **constant $d$ only**, the dimensionless logarithmic pressure slope of the added *linear-response damping coefficient* is $G'_{\rm iso}/G_{\rm iso}=8.0605\times10^{-4}$ MPa$^{-1}$ near this tensile numerical reference. It differs from the v20 **static curvature** logarithmic slope of $4.61\times10^{-4}$ MPa$^{-1}$; neither number is an experimental friction-force derivative.

Writing $Y=K^{-1}C^T$ gives an eigenvector-phase-independent derivative check:

\[
 G=Y^TY,\quad
 Y'=K^{-1}C'^T-K^{-1}K'Y,\quad
 G'=Y'^TY+Y^TY'.\tag{29b}
\]

With centered $\pm2.5$ MPa differences in the Hessian blocks, the $C'$ contribution to $\frac12\operatorname{tr}G'$ is $+4.465243\times10^{-7}$ MPa$^{-1}$ and the $K'$ contribution is $-0.204894\times10^{-7}$ MPa$^{-1}$. Their sum $4.260349\times10^{-7}$ agrees with direct finite differences. The $14/16/18$ Å fixed-roster cutoffs yield slopes $(4.260386,4.260348,4.260334)\times10^{-7}$ MPa$^{-1}$; the second Hessian-step calculation at 16 Å gives $4.260113\times10^{-7}$ MPa$^{-1}$. These are within-model numerical sensitivities, not uncertainty in a measured graphite loss rate [29].

For a real pressure-dependent bath, the complete identity is $\Gamma_{\rm add}'=dG'+d'G$ under isotropic Rayleigh loss; mode-dependent damping additionally requires its own $D_h(P)$ and matrix derivative. Hence a weak experimental friction-load slope cannot identify, confirm or exclude this channel using $G'$ alone. A signed UD residual at the paired angles requires an independently sourced, pressure-resolved material loss operator and a validated relation between the resulting response and the measured finite-speed force. The present calculation remains **development — no registry entry; physical promotion 0**.

## 7g. Two-channel loss identifiability and a measurement design

The v21 spectrum contains two laterally active $E$ doublets in the declared 14-height model. If a separately sourced bath damps each doublet with scalar Rayleigh coefficient $d_1$ or $d_2$, symmetry makes the isotropic retarded correction

\[
 \Sigma_{\rm iso}(\omega)
 =\sum_{a=1}^{2}\frac{r_a}{\kappa_a-\mu\omega^2-i\omega d_a},
 \quad (\kappa_1,\kappa_2)=(307.9743,2297.2933),
 \quad(r_1,r_2)=(46.9580,176.5825).\tag{30a}
\]

The displayed stiffnesses are in meV Å$^{-2}$ per mean upper atom and residues in squared stiffness units. The numerical representation is isotropic to Hessian precision, and the ideal symmetry form is a conditional model. Its low-frequency drag *if the bath exists* contains only one combination,

\[
 \Gamma_{\rm add,iso}=a_1d_1+a_2d_2,
 \quad a_a=r_a/\kappa_a^2,
 \quad (a_1,a_2)=(4.9508562\times10^{-4},3.3459138\times10^{-5}).\tag{30b}
\]

Hence a single DC coefficient cannot identify two nonnegative loss rates: it fixes a line segment $a_1d_1+a_2d_2=\Gamma_{\rm add,iso}$ in the first quadrant if the other channels have been removed. Over the five v22 pressure points, $a_1(P)/a_2(P)$ shifts only from 14.798265 to 14.795182 between $-5$ and $+5$ MPa. The $5\times2$ design matrix formed from $(a_1(P),a_2(P))$ has two-norm condition number about **$2.02\times10^5$** in the raw $d_a$ coordinates, or **$2.71\times10^4$** after normalizing each column to unit norm. The latter removes arbitrary parameter scale; both diagnose severe separation sensitivity to measurement and model errors. Cutoffs 14 and 18 Å give normalized-column condition numbers 27148 and 27145, compared with 27149 at 16 Å [30]. This is an identifiability calculation, not a fitted linewidth.

A dynamic measurement can change the rank. The dissipative part of the **model** transfer function is

\[
 L(\omega):=\frac{\operatorname{Im}\Sigma_{\rm iso}(\omega)}{\omega}
 =\sum_{a=1}^{2}\frac{r_a d_a}{(\kappa_a-\mu\omega^2)^2+(\omega d_a)^2}.
 \tag{30c}
\]

In the weak-loss, off-resonant regime, set $t_a=a_ad_a$ and $\omega_1^2=\kappa_1/\mu$. Samples near $\omega=0$ and $\omega=2\omega_1$ then obey, to leading order in the linewidths,

\[
 \begin{pmatrix}L(0)\\L(2\omega_1)\end{pmatrix}
 \simeq
 \begin{pmatrix}1&1\\1/9&4.64955\end{pmatrix}
 \begin{pmatrix}t_1\\t_2\end{pmatrix}.\tag{30d}
\]

The determinant is 4.53844 and the two-norm condition number in the **$t_a$ coordinates** is 5.01. For the chosen illustrative $^{12}$C and fixed lower sheet, $2f_1\approx18.74$ THz; this is a **model design frequency**, not a verified graphite resonance. An exceptional nonzero frequency near 12.44 THz in this model makes the two weak-loss weights equal, so two arbitrarily chosen frequencies need not distinguish the channels. Actual design must first locate the two active resonances and check $|\omega d_a|\ll|\kappa_a-\mu\omega^2|$ at any off-resonant samples.

Equation (30d) would require a calibrated complex lateral susceptibility with the clamped lateral response, substrate, other phonon baths and instrument transfer removed or independently constrained. Two frequencies do not determine two $d_a$ if those extra unknowns remain. Independent mode-resolved linewidths, verified conservative residues and a finite-speed force estimator would make a **conventional** friction prediction testable. A UD-specific residual still needs an independently derived source restriction that predicts an outcome beyond the conventional fit at *both* complementary angles without using their held-out force traces [30]. The calculation stays in the development lane, with no registry entry and physical promotion 0.

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

[13] SHA-checked four-pattern raw-grid first-shell fitting script, source run-label caveats and JSON table in this capture. The ideals are periodic static shear strengths, not fitted 2026 friction data.

[14] Source-supplement provenance, analytic pair derivatives, pressure conversion, source-grid comparison, cutoff sensitivity, standalone replay script and JSON in this capture; the public arXiv source archive has SHA-256 `adea7468f311c648a0d25abf4f5eecacd8eebe1b6fc7761ffcea7d073b2f460b`. No archived code was executed.

[15] Two-shell vertical Taylor saddle continuation, derivative and finite-pressure check, and source qualification in this capture. Replays with the SHA-checked [10] data archive.

[16] Conditional deterministic driven-washboard force-observable derivation, quadrature and finite-difference replay in this capture. The numerical barrier inputs are from the qualified conventional [15] reconstruction; no experiment or UD damping has been fit.

[17] Direct two-shell straight-path vertical relaxation and driven-force replay in this capture; SHA-checked public 2023 grid supplies the sampled positions, while the KC source SI parameters supply the reconstructed energies. No 2026 experimental force data are used.

[18] Fixed-normal atom-height KC cross-Hessian reconstruction, symmetry registration, seven-orbit least-squares projection, exact/numerical dimension check, step and cutoff sensitivity in capture `2026-10-22T224639Z-codex-graphite-material-projection-fcd6e90e-4531aa0e-8487-4d43-b0dd-cfe246d1b6b4`. The prior exact carrier verifiers supply the source basis; no 2026 friction trace is used.

[19] LAMMPS, [Kolmogorov–Crespi z-axis pair style](https://docs.lammps.org/pair_kolmogorov_crespi_z.html), fixed normals and a constant per-pair cutoff shift; this implementation document does not establish what produced [10].

[20] Reproducible cutoff-shift sensitivity in this capture; the source ZIP is hash checked, and archived source code is not executed.

[21] A. N. Kolmogorov and V. H. Crespi, [*Phys. Rev. B* **71**, 235415 (2005)](https://doi.org/10.1103/PhysRevB.71.235415), local normals and transverse distances; compare LAMMPS [full local-normal pair style](https://docs.lammps.org/pair_kolmogorov_crespi_full.html). The source 2023 flat-layer energy formula alone does not choose an off-plane normal prescription.

[22] Three-neighbor local-normal conventional KC replay, SHA-checked public archive provenance, finite-difference cross-product normal check, nonlinear full-pair-energy derivatives, symmetry registration and cutoff/step sensitivity in the v18 predecessor capture. Development result; no force trace or UD damping fit.

[23] Registered 14-site bending-Laplacian, finite-difference pair-energy height Hessian, cutoff-step audit, exact quadratic Schur reduction and parameter sweep in the v19 predecessor capture. No measured drag, full nonlinear relaxation or experimental force-load data.

[24] Y. Wei, B. Wang, J. Wu, R. Yang and M. L. Dunn, “Bending Rigidity and Gaussian Bending Stiffness of Single-Layered Graphene,” *Nano Letters* **13**, 26–30 (2013), [doi:10.1021/nl303168w](https://doi.org/10.1021/nl303168w), reports 1.44 eV for its specified theoretical treatment.

[25] E. Han *et al.*, “Ultrasoft slip-mediated bending in few-layer graphene,” *Nature Materials* **19**, 305–309 (2020), [doi:10.1038/s41563-019-0529-7](https://doi.org/10.1038/s41563-019-0529-7), reports 1.2–1.7 eV for a monolayer.

[26] Nonlinear 16-coordinate local minimization, fixed-pair-roster construction, three cutoff checks, independent minimized-energy curvature, five pressure points and registered source/complement response replay in capture `2026-10-23T015602Z-codex-graphite-nonlinear-relax-a7f309c2-f7597bc1-0620-488b-97f4-3eabbc7815d0`. This is a conditional continuation of [22] and [23], not 2026 experimental data.

[27] NIST, [2022 CODATA recommended values](https://physics.nist.gov/cuu/pdf/JPCRD2022CODATA.pdf), atomic mass constant $u=1.66053906892(52)\times10^{-27}$ kg and exact electron-volt-to-joule conversion. The $12u$ isotope is an illustrative mass input, not a sample composition measurement.

[28] Capture `2026-10-23T023854Z-codex-graphite-finite-spectrum-4c8b18e3-68bdd1a3-441a-4a35-ac05-a26af9803d0c`: SHA-checked finite-mode spectrum replay script and 14/16/18 Å JSON results. The v20 source model and numerical reference remain unchanged; no experimental linewidth or 2026 force trace is imported.

[29] This capture: SHA-checked stationary pressure-sweep replay, five loads at each of 14/16/18 Å fixed reference rosters, two Hessian step sizes, mode-selection and product-rule derivative checks. Conditional conventional model only; no 2026 force trace or measured linewidth.

[30] This capture: two-active-doublet identifiability replay and JSON, using only the immutable v21 and v22 conditional model results. No 2026 force curve, linewidth or article supplement was imported.
