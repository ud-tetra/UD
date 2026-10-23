# Collective mass and cross-potential audit

**23 October 2026 UTC · NUMERICAL conventional comparison · No UD physical promotion**

The 14-upper/14-lower atom bilayer has a relative rigid translation $x$. A per-upper-atom curvature $k$ means total potential $14kx^2/2$. With both layers moving by $+x/2$ and $-x/2$, kinetic energy is $14m_C(\dot x/2)^2 = (7m_C)\dot x^2/2$. Thus the mass compatible with **per-upper-atom** $k$ is $m_C/2$. A lower layer held fixed instead assigns $m_C$ per upper atom. The unit-edge cochain Gram matrix has no authority to alter this physical mass.

| Source and protocol | Shear wavenumber (cm$^{-1}$) | Equivalent curvature (meV Å$^{-2}$/upper atom) |
| --- | ---: | ---: |
| Our KC plus plate, clamped at relaxed heights; both mobile for conversion | 9.309 | 1.911869 |
| Our KC plus plate, heights statically eliminated; both mobile for conversion | 8.732 | 1.682530 |
| Minkin et al. KC (2,1), rigid-height PES [1] | 9.153 | 1.848494 |
| Lebedeva et al. vdW-DF3 rigid (2,1) [2] | 0.404 | 0.003601 |
| Lebedeva et al. vdW-DF3 out-of-plane relaxation [2] | 0.510 | 0.005739 |
| Lebedeva et al. vdW-DF3 relaxation with two atoms constrained [2] | 0.590 | 0.007681 |

For the two in-repository rows, the original nonlinear calculation fixed the lower layer; the table uses a **hypothetical two-mobile-layer mass conversion of its per-atom curvature** for like-unit comparison. It does not make the upper/lower dynamical model symmetric. The actual fixed-lower shear conversions are 6.582 and 6.175 cm$^{-1}$. The DFT frequencies are authors' Fourier-PES-derived predictions with $m_C/2$, not a direct friction measurement. The DFT study itself finds KC strongly overestimates PES corrugation and reverses the (2,1) registry type. The values use different equilibrium separations and relaxation protocols; do not interpret ratios as measured residuals, uncertainties, or universal renormalization factors.

The approximately 293-fold ratio between our statically relaxed curvature and the vdW-DF3 out-of-plane curvature invalidates an **unqualified physical graphite amplitude** based on the conditional KC plus plate result. It does not invalidate the exact seven-cell angular geometry, conditional cochain identity, Schur algebra, or no-Ohmic-DC conclusion for a finite closed harmonic model. It means the present $G$, $dG/dP$, mode frequencies and pressure identifiability are diagnostics of a particular *KC plus plate* numerical construction only. Its $d$ remains unknown; no kinetic friction or observed load response follows.

Next material gate: fit a pressure-resolved, independently assessed (2,1) PES and mixed lateral/height Hessian at stated normal separation and relaxation constraints; calculate a bath spectral density or mode linewidths independently; freeze the conventional force protocol before considering a signed UD residual. The 2026 Chen experimental force curves and uncertainties are still unavailable in this audit.

Sources: [1] [Minkin et al. 2023](https://arxiv.org/pdf/2308.06302), Eq. (4), Table II, and discussion of KC limitations. [2] [Lebedeva et al. 2025](https://arxiv.org/pdf/2511.01338), Tables 2, 3, 4 and 6 and Secs. 3.1–3.4. Both are primary research papers; [2] is a preprint as checked here. Reproduce conversion with `python3 reproduce_mass_map.py`.
