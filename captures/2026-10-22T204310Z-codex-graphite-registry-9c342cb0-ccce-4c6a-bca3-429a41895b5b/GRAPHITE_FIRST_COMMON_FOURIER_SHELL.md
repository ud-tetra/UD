# The first surviving graphite registry shell and an exact load–height identity

22 October 2026. **EXACT conditional rigid-bilayer Fourier calculation; exact equilibrium identity; physical promotion 0.** This capture supplies a quantitative *conventional* reference for the seven-cell (2,1) graphite paper. It does not infer a UD residual or convert an energy barrier into experimental friction.

## 1. Rigid infinite-layer Fourier selection

Use triangular direct lattice coordinates with unit primitive vectors at 60°, reciprocal labels (h=(h_1,h_2)\in\mathbb Z^2), and plane waves (e^{2\pi i h\cdot y}). The angle in draft PR #414 uses

\[
R=\frac17\begin{pmatrix}8&3\\-3&5\end{pmatrix},\qquad
\tau_A=0,\quad\tau_B=(1/3,1/3).
\tag{1}
\]

For an infinite bottom honeycomb and a rigid top layer, write the **pairwise translationally invariant** interlayer potential as (v(y,z)), with planar transform (\widehat v(G_h,z)). Let (A_0) be the Bravais primitive-cell area and (V_h(z)=\widehat v(G_h,z)/A_0) (energy units for one top Bravais cell). The bottom structure factor is (B_b(-h)=1+e^{-2\pi i(h_1+h_2)/3}). The rotated top factor is (B_t(h)=1+e^{2\pi i(R^Th)_1/3+2\pi i(R^Th)_2/3}). Averaging the top layer over its seven Bravais cosets within one coincidence cell yields

\[
 E(t,z)=\sum_{h\in\mathbb Z^2}\!V_h(z)B_b(-h)B_t(h)
 \mathbf1_{R^Th\in\mathbb Z^2}e^{2\pi i h\cdot t}.
\tag{2}
\]

Here (E) is energy per top Bravais cell and (t) is the lateral translation in bottom direct coordinates. The indicator is an exact finite-character sum for the ideal periodic interface. With (R^T h=((8h_1-3h_2)/7,(3h_1+5h_2)/7)), its condition is

\[
 h_1-3h_2\equiv0\pmod7.
\tag{3}
\]

Thus the ordinary substrate first reciprocal shell (h=(\pm1,0),(0,\pm1),(\pm1,\pm1)) cancels in the area average. Edges, disorder, relaxation and a finite patch can invalidate that exact cancellation.

## 2. The six first surviving harmonics

The reciprocal squared-length form, in units (g_0^2=|G_{(1,0)}|^2), is (Q(h)=h_1^2-h_1h_2+h_2^2). The nonzero solutions of (3) with minimal length have (Q=7), namely the sign pairs of ((3,1),(-1,2),(-2,-3)). Therefore their magnitude is (g_*=\sqrt7\,g_0). Put (\omega=e^{2\pi i/3}). For this chosen (C_3) orbit, (h\cdot(1,1)\equiv1\pmod3) and ((R^Th)\cdot(1,1)\equiv2\pmod3), so

\[
 B_b(-h)B_t(h)=(1+\omega^2)^2=\omega^2,
 \qquad |B_b(-h)B_t(h)|=1.\tag{4}
\]

Assume a real isotropic pair potential, giving the same real (V_*(z)) on this reciprocal shell. Its complete first-shell corrugation is

\[
 E_1(t,z)=2V_*(z)\operatorname{Re}\!\left[
 \omega^2\sum_{h\in\mathcal H_3} e^{2\pi i h\cdot t}\right],
 \quad \mathcal H_3=\{(3,1),(-1,2),(-2,-3)\}.\tag{5}
\]

The origin shift (t_0=(1/21,4/21)) makes each (e^{2\pi i h\cdot t_0}=\omega), removing the common basis phase. Since the three (h\)'s sum to zero, (\sum_j\cos\phi_j) spans from (-3/2) to (3), with (\sum_j\phi_j=0\pmod{2\pi}). In this **first-shell-only rigid model** the lateral energy range is therefore

\[
\boxed{\Delta E_1(z)=9|V_*(z)|.}\tag{6}
\]

The numerical 9 is the exact barrier multiplier for the stated normalization, not a friction force, measured graphite amplitude, or UD coefficient. Other reciprocal shells and contact edges can change the full barrier. Suppression at larger reciprocal wavevector depends on the physical (V_h(z)); geometry alone gives the first allowed (g_*), not an exponential decay constant.

## 3. Load versus relaxed height: an exact conditional identity

Let (L>0) denote compressive normal force **per top Bravais cell**, with relaxed energy at lateral registry (t)

\[
 \mathcal H(t,L)=\min_z\{E(t,z)+Lz\}.
\tag{7}
\]

Assume smooth stable minima in (z), and follow a smooth lateral barrier top (t_+(L)) and bottom (t_-(L)) without branch switching. The stationary conditions and envelope theorem give

\[
\boxed{\frac{d\Delta\mathcal H}{dL}
=\frac{d}{dL}\left[\mathcal H(t_+,L)-\mathcal H(t_-,L)\right]
=z_+(L)-z_-(L).}\tag{8}
\]

The identity is independent of UD and of the form of (v). A small load slope of this *relaxed barrier* is equivalent to a small separation difference between its extremal registries on a smooth branch. At switching points a classical derivative need not exist; one-sided slopes come from the corresponding heights. The paper's abstract mentions negligible load dependence of **measured friction peaks** and stable interlayer separation, but it does not equate their friction estimator with (\Delta\mathcal H) or supply a numeric height bound [1]. Equation (8) cannot be applied directly to the measured friction slope.

For a controlled weak first-shell corrugation, write (E(t,z)=E_0(z)+2V_*(z)\sum_j\cos\phi_j(t)), let (E_0'(z_0)+L=0), and set (k_z=E_0''(z_0)>0). To leading order in corrugation,

\[
 \Delta\mathcal H=9|V_*(z_0)|+O(V_*'^2/k_z),\qquad
 z_+-z_-=-\frac{9\,\partial_z|V_*(z_0)|}{k_z}+O(\text{higher corrugation}),
\tag{9}
\]

and, where (V_*\ne0),

\[
 \partial_L\log\Delta\mathcal H
 \simeq -\frac{\partial_z\log|V_*|}{k_z}.
\tag{10}
\]

If the **additional model assumption** (V_*(z)=V_0e^{-\kappa z}) holds over the load range, the leading relation becomes (\partial_L\log\Delta\mathcal H\simeq\kappa/k_z). The symbols (V_0,\kappa,k_z) require independent material data; none is fixed by the seven-cell geometry or the octahedral UD chain.

## 4. Consequence for the UD manuscript

The conventional model now accounts for the paired angle, seven-cell count, disappearance of primitive Fourier corrugation, the first permitted registry shell, and an exact load–height relation for an equilibrium barrier. An additional UD hypothesis must modify a **specified** Fourier coefficient or the dissipation channel in draft PR #415, with a sourced coupling and frozen prediction after subtracting these conventional effects. Merely reproducing Eq. (6) or (8) is not a UD explanation. Physical promotion remains 0.

[1] W. Chen *et al.*, “Observation of Superlubricity at Commensurate Moiré Graphite Interfaces,” *Phys. Rev. Lett.* **137**, 166201 (2026), [doi:10.1103/ly48-b4l2](https://doi.org/10.1103/ly48-b4l2), public abstract (full text and supplement subscription restricted on 22 October 2026).
