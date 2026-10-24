# A source-to-path bound for spectral leakage under widely linear response and polynomial distortion

Version 0.1 · 24 October 2026 · Conditional mathematical theorem

## 1. Signal class and conventions

For a finite complex Borel measure μ on the real frequency line, define

\[
\mathcal F^{-1}\mu(t)=\int_{\mathbb R}e^{2\pi i f t}\,d\mu(f),
\qquad \|\mu\|_{\mathrm{TV}}=|\mu|(\mathbb R).
\]

The measure has voltage units when its Fourier–Stieltjes transform is a complex voltage. Its norm bounds the voltage uniformly in time. A bounded Borel multiplier H acts on measures by d(Hμ)=H dμ, with norm at most sup|H|. Here conjugation of a signal corresponds to reflection and conjugation of its measure and preserves total variation. Multiplication of two such signals corresponds to convolution of their finite measures, whose norm satisfies

\[
\|\mu*\nu\|_{\mathrm{TV}}\le\|\mu\|_{\mathrm{TV}}\|\nu\|_{\mathrm{TV}}.
\]

All measures below are fixed descriptions of the source and path, not reconstructions inferred from finitely many target samples. Bounds on their norms are assumptions requiring separate physical evidence in an application.

## 2. Source-to-path leakage theorem

Let the input have decomposition u=b+s+r, with respective finite complex measures μ_b, μ_s, μ_r and

\[
\|\mu_b\|_{\mathrm{TV}}\le B,\qquad
\mu_s=\sum_{\ell=1}^{K}a_\ell\delta_{f_\ell},\quad
\sum_\ell|a_\ell|\le A,\qquad
\|\mu_r\|_{\mathrm{TV}}\le R.
\]

The frequencies f_l are distinct and fixed. Let U=B+A+R. Suppose the complex output is exactly

\[
z=H_+u+H_-\overline u
+\sum_{d=2}^{D_*}\ \sum_{m+n=d}
 c_{mn}V_*\left(\frac{u}{V_*}\right)^m
                  \left(\frac{\overline u}{V_*}\right)^n+w,
\]

where H_± denote fixed spectral multipliers, V_*>0 is a reference voltage, the coefficients c_mn are dimensionless and fixed, and w has a finite measure μ_w. Assume

\[
\sup_f|H_+(f)|\le M,\quad
\sup_f|H_-(f)|\le J,\quad
\sum_{m+n=d}|c_{mn}|\le\beta_d,\quad
\|\mu_w\|_{\mathrm{TV}}\le D.
\]

The multiplier bounds need only hold on the support of the measures they multiply, but that support must be established independently. In the absence of such a support restriction, a global bound is required. Omitted orders, memory effects, start-up transients, drift, additive terms and any primary-reference subtraction error must be included in the finite-measure remainder; a pointwise residual or RMS fit is insufficient.

Define the ideal residual q=z−H_+b. Then q=p+e, where

\[
p(t)=\sum_\ell H_+(f_\ell)a_\ell e^{2\pi i f_\ell t},
\]

and e has a finite measure satisfying

\[
\boxed{\quad
T_{\mathrm{out}}:=\|\mu_e\|_{\mathrm{TV}}
\le MR+JU+\sum_{d=2}^{D_*}\beta_d\frac{U^d}{V_*^{d-1}}+D.
\quad}
\tag{1}
\]

This is a bound on the entire remainder measure; it is therefore also an upper bound on its restriction outside the declared finite mode set. It permits remainder mass on that set and does not assume an orthogonal spectral projection. Moreover,

\[
\|\mu_q\|_{\mathrm{TV}}\le MA+T_{\mathrm{out}}.
\tag{2}
\]

**Proof.** The input measure satisfies ||μ_u||_TV≤U. Expanding the stated output model and subtracting H_+b leaves H_+s as the finite component. The linear source impurity H_+r has norm at most MR. The image term H_- conjugate(u) has norm at most JU. For every monomial, convolution submultiplicativity and preservation of norm under conjugate reflection give

\[
\left\|\mathcal M\!\left[
 c_{mn}V_*\left(\frac u{V_*}\right)^m
                 \left(\frac{\overline u}{V_*}\right)^n
\right]\right\|_{\mathrm{TV}}
\le |c_{mn}|\frac{U^{m+n}}{V_*^{m+n-1}},
\]

where M[·] denotes its representing finite measure. Summing at each degree and adding μ_w proves (1). The finite component has norm Σ|H_+(f_l)a_l|≤MA. The triangle inequality proves (2). Every term in (1) has voltage units. ∎

The full input U is essential. For b=1 V and s=a exp(2πift), quadratic distortion has constant, mixed and second-harmonic terms. Budgeting only β₂A²/V_* omits the primary-driven distortion, including the mixed coefficient 2ba. Even perfect subtraction of the **linear** primary does not remove these terms. Likewise, image response acts on the full input, not only its small residual.

## 3. Sample-norm feasibility corollary

Let Φ_jl=exp(2πif_l t_j), G=Φ*Φ/N, and suppose λ_max(G)≤Λ. Let ||a||₂≤a₂ and let y_j=q(t_j)+v_j with complex sample error ||v||_d≤ε, where ||x||_d²=N⁻¹Σ|x_j|². Then

\[
\boxed{\quad \|y\|_d\le\sqrt\Lambda\,M a_2+T_{\mathrm{out}}+\varepsilon.\quad}
\tag{3}
\]

**Proof.** For h_l=H_+(f_l)a_l, the sampled finite component has norm squared h*Gh≤Λ||h||₂²≤ΛM²a₂². The remainder is uniformly bounded by T_out, so its sampled norm is at most T_out. Add the sample error by the triangle inequality. ∎

For the previously derived 1024-sample design, the row-sum argument gives both λ_min(G)≥9/10 and λ_max(G)≤11/10. Thus √Λ≤21/20 is a rational upper bound. The design permits mode indices100–199, a one-second nominal cyclic span, per-mode errors≤5 mHz, relative affine timing error≤10 ppb and per-sample residual≤10 ns. An arbitrary common frequency shift and epoch leave this Gram bound invariant; they do not establish physical band membership or absolute phase.

## 4. Exact proposed instance

Take a 1 V primary TV bound, 100 finite lines each of amplitude 1/400000 V, independently bounded source impurity R=1/10⁶ V, M=51/50, J=1/10⁶, V_*=1 V, β₂=β₃=1/10⁶ and D=1/500000 V. The aggregate line bounds are A=1/4000 V and a₂=1/40000 V. These are requirements for a source-controlled calibration fixture, not measured apparatus properties.

Equation (1) gives

\[
T_{\mathrm{out}}\le
\frac{6021506252019813251}{10^{24}}\,\mathrm V
\approx6.021506252020\,\mu\mathrm V
<10\,\mu\mathrm V.
\]

With ε=20 µV, equation (3) gives

\[
\|y\|_d\le
\frac{52796506252019813251}{10^{24}}\,\mathrm V
\approx52.796506252020\,\mu\mathrm V
<55\,\mu\mathrm V.
\]

The same source assumptions already give the stronger direct tail-TV bound MA+T_out≈0.261021506253 mV. Consequently this engineered fixture tests consistency of the measurement path and the conditional monitor theorem; it does not infer an unknown native dynamics or obtain source completeness from monitor data. The inherited general monitor ceiling0.90675 mV remains valid under its separate55/20/10 µV ceilings.

## 5. Scope of physical use

A finite set of gain/distortion measurements does not by itself establish the uniform multiplier, coefficient and spectral-remainder bounds assumed above. A measured PSD, noise RMS, or pointwise polynomial-fit residual is not automatically a deterministic complex spectral-TV bound. If such bounds cannot be justified, the theorem remains conditional.

For example, nominal sampling at j/1024 cannot distinguish opposite atoms at100 and1124 Hz: their sum vanishes at every sample, while the source spectral variation can be arbitrarily large. Source preparation and outside-model evidence must therefore come from independently justified restrictions, not the same output FFT. A prospective calibration fixture supplies no retrospective transfer to an unresolved historical run.

Mathematical status: constructor-proved conditional theorem; independent review pending. No empirical source/path bound, native action scale, or physical identification is asserted.
