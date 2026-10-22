# Graphite mathematical-method receipt: harmonic port and local curvature

22 October 2026 · development, no registry entry · exact conditional result · physical promotion 0.

## BOOT REPORT

**Question.** After the conventional honeycomb and moiré model explains the paired angles, what local lateral stiffness and normal-load response follow from its first Fourier shell when represented in the planar UD harmonic port? Does the port supply a further material coefficient?

**Typed objects.** `K7`: the oriented seven-hexagon honeycomb cellular torus, with `C_k(K7;Q)` and signed boundary maps `B1:C1→C0`, `B2:C2→C1`; 14 vertices, 21 oriented A-to-B edges, seven faces, periodic boundaries. `H1`: the two-dimensional harmonic real edge-cochain plane, with the *chosen* Euclidean unit-edge metric; its generator is the closed unit Hodge–Dirac operator, zero on `H1`. The integer geometry is exact; response coefficients live in real symbolic functions of height. `X`: a physical Cartesian relative lateral displacement in metres; `Z`: vertical separation in metres. `M_X:X→H1` has 21 rows, one per bond, each the dimensionless bond direction vector `(r_B-r_A)/a` dotted with `x`; hence its output has metres. `I_X:X→H1⊕H1` is the equal-layer relative lift `x↦(-M_X x/2,+M_X x/2)`, with the second layer's rotated copy expressed in the common Cartesian frame. This is a geometrical readout convention, not a map from atomic displacement to bond strain.

`U`: rigid lateral energy per *top Bravais cell* (joules), with three reciprocal vectors `g_j` of common magnitude `g*=√7 g0` (inverse metres) and `g3=g1+g2`; `V(z)` is their common real Fourier amplitude in joules per top Bravais cell. The same first-shell amplitude is assumed for the three directions, and all other shells, finite-size effects, reconstructions and relaxation are omitted. `L` is positive compressive normal force per top Bravais cell (newtons), with enthalpy `E+Lz`; `E0(z)` is mean vertical energy per top Bravais cell. Smooth stable vertical and lateral branches are assumed; `V≠0` and its sign remains fixed over the load interval.

**Applicable techniques.** Exact chain/harmonic geometry, rational Gram calculation, `C3` group covariance, symbolic spectral Hessian, physical units, projection, and fit/null sensitivity. Clock, modular arithmetic, prime factorization, register parity, hierarchy, and continuum limit: N/A to this question. There is no physical clock or dissipative bath sourced here. No quantity is fitted. The intended physical bridge is only the *conditional* import of `V(z)` and `E0(z)` into the geometric readout; no measured force estimator is specified.

**Source IDs.** `S1` is the previous seven-cell planar capture and verifier in draft PR #417. `S2` is the corrected first-shell stationary landscape in draft PR #418. `S3` is the user-provided `UD_MATHEMATICAL_METHOD_v1.0.md`, copied byte-for-byte in this capture; it supplies analysis rules, not a graphite constitutive parameter. `S4` is Chen *et al.*, *PRL* **137**, 166201 (2026), DOI `10.1103/ly48-b4l2`, public abstract only. `S5` is governance proposal CRL-2; its proposed rules are not assumed adopted. None supplies the sign or magnitude of `V`, physical damping, or raw friction traces.

## Exact geometric normalization

Let the physical primitive vectors be `a1=a(1,0)`, `a2=a(1/2,√3/2)`, where `a>0` has metres. Each of seven Bravais sites contributes the three A-to-B bond vectors `d0=(a1+a2)/3`, `d1=(-2a1+a2)/3`, `d2=(a1-2a2)/3`. With `M_X` rows `d_jᵀ/a`, repeated seven times,

\[
M_X^T M_X=7\sum_{j=0}^2 d_jd_j^T/a^2=\frac72 I_2,
\quad I_X^T I_X=\frac74 I_2,
\quad x=\frac47 I_X^T q_{\rm rel}\quad(q_{\rm rel}\in\operatorname{im}I_X). \tag{1}
\]

These are exact under the chosen unit-edge metric. The full readout `(4/7)I_Xᵀq` annihilates the orthogonal complement of the relative plane; it has rank two, with kernel dimension 40 in the 42-dimensional bilayer edge space. This kernel dimension is *not* an information-loss percentage. The `x` coordinate has metres and the `q` coordinate has metres under this normalization. Reweighting edges or including unequal layers changes the number `7/4`; the physical pinning stiffness must transform with the coordinate choice.

## Conditional first-shell material coupling

Define `S=cos(g1·x)+cos(g2·x)+cos((g1+g2)·x)` and `E(x,z)=E0(z)+2V(z)S`. The three physical `g_j` have 120-degree star symmetry and obey `Σ_j g_jg_jᵀ=(3/2)g*²I`. At a lateral *stable* registry the cosine of all three phases is `-1/2` when `V>0`, and `1` when `V<0`. Thus the physical lateral Hessian and its restriction to the unit-metric harmonic relative lift are

\[
H_x=\nabla_x^2E=k_x I_2,\quad
k_x=\begin{cases}\frac32 Vg_*^2,&V>0,\\3|V|g_*^2,&V<0,\end{cases}
\qquad H_{q\mid\mathrm{im}I_X}=k_q I_2,\quad k_q=\frac47 k_x. \tag{2}
\]

The latter scalar uses *orthonormal coordinates* on `im I_X`, so its units are joules/metre². In unnormalized `x` coordinates the stiffness remains `k_x`. A general edge-state extension away from `im I_X` is not determined. In particular, the closed Hodge–Dirac generator has zero response there and does not create `k_x` or a damping constant.

The first-shell minimum-path barrier at fixed height is `ΔU=c_s|V|`, with `c_+=1` for `V>0`, `c_-=8` for `V<0` (`S2`). Eliminating the *same* `|V|` gives an exact baseline shape check:

\[
\frac{k_x}{\Delta U}=
\begin{cases}(3/2)g_*^2,&V>0,\\(3/8)g_*^2,&V<0.\end{cases} \tag{3}
\]

The ratio has inverse-square-length units and uses a rigid fixed-height barrier. It is a test of the first-shell truncation and sign branch, **not** an independent UD prediction. At `V=0`, `ΔU=0` and this ratio is undefined. All these values change when additional Fourier shells or relaxation enter.

## Height relaxation and load

At a stable registry `S_m∈{-3/2,3}`, let `z_m(L)` solve

\[
E_0'(z_m)+2S_mV'(z_m)+L=0,\qquad
K_z^m=E_0''(z_m)+2S_mV''(z_m)>0. \tag{4}
\]

The cross Hessian `E_xz=2V'(z)∇_xS` vanishes *at the stationary registry*. The relaxed lateral Hessian's vertical Schur correction therefore vanishes at that point (though generally not away from it). Implicit differentiation gives `dz_m/dL=-1/K_z^m`, and, on a fixed-sign branch,

\[
k_x(L)=\beta_s |V(z_m)|g_*^2,\quad
\frac{dk_x}{dL}=-\beta_s g_*^2\frac{\partial_z|V|(z_m)}{K_z^m},\quad
\frac{d\log k_x}{dL}=-\frac{\partial_z\log|V|(z_m)}{K_z^m},\quad
\beta_+=\frac32,\ \beta_-=3. \tag{5}
\]

The derivative in Eq. (5) is exact *within this separable first-shell energy*, even after vertical relaxation, provided the stationary branch remains stable. Its smallness is **not** implied by the torus or by `C3`: it requires a small `∂zV`, a large vertical curvature, or both. For comparison, the relaxed saddle barrier has `dΔℋ_mp/dL=z_s-z_m` (`S2`), and its logarithmic slope approaches Eq. (5)'s slope only at leading order in weak corrugation with a common mean height. Neither equilibrium derivative is a measured friction-load slope.

## Damping and the requested residual

If a separately sourced physical law gives an isotropic lateral Rayleigh damping `Γ_x` (newton·second/metre), the chosen normalized harmonic coordinate represents it as `Γ_q=(4/7)Γ_x`. This is a coordinate conversion. The earlier optional passive elimination `Γ_eff=Γ_x+CK⁻¹DK⁻¹Cᵀ` leaves `C,K,D`, and hence `Γ_eff` and its load derivative, unconstrained by the planar topology. A force estimator, speed, bath and physical time scale are also absent. Consequently `F_obs-F_conventional` and its load slope are **OPEN**, not zero and not a UD-specific quantitative prediction. Eq. (3) is a useful baseline check for simulations before fitting a residual law.

## Checks, limits and follow-up

`verify_curvature_port.py` uses independent symbolic Cartesian bond and reciprocal vectors to check the Gram, stationary Hessian, `C3` isotropy, energy-to-curvature ratios, and branchwise implicit load derivatives exactly. This is constructor verification, not independent review. The source of `V(z)` and the inferred branch sign remain open. A useful next physical input is an independently computed or measured two-dimensional registry energy surface at several separations, plus a rate-dependent force trace and its uncertainty. Freeze its ordinary first-shell and higher-shell baseline on training data before testing any UD-specific residual on held-out load/speed traces.
