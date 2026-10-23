# Measurement-ready oscillatory loss port and data boundary

**Development — no registry entry · Constructor checked · Physical promotion 0 · 23 October 2026 UTC**

## Derivation

Let $\bar E$ be energy per **upper atom** for a 14-upper-atom periodic coincidence cell. With lateral relative coordinate $x$ in Å, height coordinates $h\in\mathbb R^{14}$ in Å, and $H,C,K$ in meV Å$^{-2}$ per upper atom, the fixed-lower model has height mass $M_h=(m_C/14)I$ in mean-energy coordinates. If a passive Rayleigh bath $D_h$ in meV ps Å$^{-2}$ per upper atom is independently provided, harmonic height elimination gives the retarded inverse-response contribution $-C(K-\omega^2M_h-i\omega D_h)^{-1}C^T$. At low frequency this is $-CK^{-1}C^T-i\omega CK^{-1}D_hK^{-1}C^T+O(\omega^2)$, when $K$ is invertible. The additional damping tensor is positive semidefinite for $D_h\succeq0$. The closed model has $D_h=0$ and no Ohmic DC damping.

For one scalar direction and a prescribed $x(t)=A\cos\omega t$ well within a local potential minimum, the force quadrature magnitude is $14\Gamma_{\rm add}A\omega$, and the energy dissipated over one cycle is $14\pi\Gamma_{\rm add}A^2\omega$. These use the **full cell**; leaving out 14 would give a per-upper-atom force and work. The oscillatory drag is not kinetic friction across the periodic PES.

In the v22 KC plus plate numerical model with $D_h=dI$, $G=\Gamma_{\rm add}/d=5.28544758\times10^{-4}$. If $d$ has numeric value 1 in meV ps Å$^{-2}$ per upper atom, the cell's drag is 0.007399626612 meV ps Å$^{-2}=1.1855508858\times10^{-16}$ kg/s. At an **illustrative** $A=0.01$ Å and $\omega=1$ rad/ps, force quadrature is $7.399626612\times10^{-5}$ meV/Å and work per cycle $2.3246612604\times10^{-6}$ meV. The amplitude is small relative to the $(2,1)$ PES period; the chosen drive is a unit example, not an experiment. The pressure reference is tensile ($P\simeq-10.734$ MPa in the model's compression-positive convention), not experimental zero.

The mean-energy mass of one orthonormal upper-height mode is $m_C/14=0.0888365971$ meV ps$^2$ Å$^{-2}$ for carbon-12; in the isolated weakly damped oscillator law $d_j=\mu_h\Delta\omega_j$, an illustrative 1 THz full-width linewidth in cycles/s corresponds to $\Delta\omega_j=2\pi$ rad/ps and $d_j=0.5581768019$ meV ps Å$^{-2}$. The same coefficient is not automatically the physical linewidth of a graphite flake or multilayer. Degenerate doublets, lower-sheet motion, instrumental broadening and mode mixing must be resolved.

At fixed $d$, the v22 per-unit-loss slope is $G'/G=+8.0605264\times10^{-4}$ MPa$^{-1}$. Exactly flat, *background-subtracted local oscillatory* loss within the conditional model would require $d'/d=-G'/G$. There is no measured $d(P)$, and the independent vdW-DF3 PES scale differs sharply from KC. No claim about finite-speed friction, the Chen peak load slope, or a UD-specific residual follows.

## Measurement inputs and failure conditions

| Input | Route | Why it matters |
| --- | --- | --- |
| $K(P)$ and $C(P)$ of a physical contact | Independent DFT/atomistic calculation or calibrated response | KC plus plate $G$ is not a transferable material constant. |
| Mode mass and linewidths $\Delta\omega_j(P)$ | Mode-resolved spectral measurement with background deconvolution | Supplies $D_h$ only if the mode model and normalization are valid. |
| Lateral force amplitude and phase under a small relative displacement | Calibrated oscillatory drive across load points | Separates force quadrature from static curvature. |
| Sliding force at fixed speed and contact geometry | Independent held-out kinetic protocol | Needed to translate any local response into the actual 2026 observable. |

A force quadrature consistent with the conventional transfer law supports the stated *material response model*, not a UD-specific effect. A discrepancy first requires tests of conventional contact edges, mode completeness, nonlinear sliding and higher PES harmonics. Exact honeycomb carrier geometry and proposed seven-orbit UD source remain distinct layers of the hypothesis.

Sources: Chen *et al.*, [PRL 137, 166201 (2026)](https://doi.org/10.1103/ly48-b4l2), public abstract only; Minkin *et al.*, [arXiv:2308.06302](https://arxiv.org/pdf/2308.06302); Lebedeva *et al.*, [arXiv:2511.01338](https://arxiv.org/pdf/2511.01338); immutable v20–v23 UD KC plus plate captures. The attached ledger v0.39 bars using Q120/Q128/Q163 as a graphite damping rate. The supplied CRL-2 subdivision proposal labels this development work without a registry promotion.
