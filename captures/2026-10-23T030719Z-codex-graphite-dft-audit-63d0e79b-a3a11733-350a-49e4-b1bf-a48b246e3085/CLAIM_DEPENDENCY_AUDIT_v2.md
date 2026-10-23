# Claim and dependency audit for the short graphite paper v2

**Constructor review · 23 October 2026 UTC · Development lane · No registry entry · Physical promotion 0**

| Claim in short paper | Type | Direct dependency | Remaining test or limitation |
| --- | --- | --- | --- |
| Angles $\arccos(13/14)$ and $60^\circ-\theta$ | EXACT conventional lattice geometry | Triangular vectors $(2,1)$ and $(1,2)$ | No distinct UD prediction; check the experimental angle uncertainty when full data become accessible. |
| Honeycomb $(14,21,7)$, Betti $(1,2,1)$ and map $M$ | EXACT within periodic quotient and unit-edge metric | Signed cellular boundaries; exact verifier in [3] | Physical map from cochains to displacement and mass is a separate assumption. |
| First surviving reciprocal shell $\sqrt7g_0$ | DERIVED conventional infinite rigid lattice | Seven-coset averaging and isotropic interlayer Fourier law | Finite edges, reconstruction and higher shells can dominate measured forces. |
| Scalar normal bilinear channel absent at $C_3$ registry | EXACT conditional symmetry selection | Unbroken $C_3$ and scalar versus $E$ transformation laws | Does not eliminate normal modulation of stiffness or broken-symmetry coupling. |
| $H_{xx}^{\rm rel}=H_{xx}-CK^{-1}C^T$ | EXACT conditional static algebra | Stationarity, positive $K$, same energy normalization | Check whether a baseline already includes relaxation before subtracting. |
| $CK^{-1}DK^{-1}C^T$ | DERIVED conditional passive open response | Material $D\succeq0$, linearized Markovian dynamics | $D$ and time calibration absent; no microscopic UD damping from ledger Q120/Q128/Q163. |
| 1.68253 meV Å$^{-2}$/atom and 0.229339 correction | NUMERICAL conventional local model | v20 three-neighbor KC, 16 Å fixed roster, rigid lower, illustrative plate | Not a 2026 measured curvature, barrier or kinetic friction. |
| Four laterally active model modes | NUMERICAL conditional | v21 Hessian and C3-symmetric local setup | Other substrate, contact, long-wavelength, thermal modes may couple. |
| $G=5.28545\times10^{-4}$, logarithmic pressure slope $8.0605\times10^{-4}$ MPa$^{-1}$ | NUMERICAL conditional | v22 stationary pressure sweep, $D_h=dI$ with $d'=0$ | This is per-unit loss at a tensile numerical reference, not a force/load prediction. |
| Pressure identification condition $\sim2.71\times10^4$; two-frequency condition $\sim5$ | NUMERICAL conditional design | v23 two-doublet reduction, weak loss and independent background subtraction | Model coordinates and resonances need validation before using this measurement design. |
| Sharp peaks, small load response at paired angles | EMPIRICAL abstract-level statement | Chen *et al.* 2026 PRL public abstract | Obtain article/supplement or author data for amplitudes, force curves, error bars, speed and contact geometry. |
| KC two-mobile-layer 8.732 cm$^{-1}$ mass map | NUMERICAL conditional cross-check | $m_C/2$ per upper atom and prior v20 $k_{\rm rel}$ | Within-KC coherence near published 9.153 cm$^{-1}$ is not independent material validation. |
| vdW-DF3 (2,1) 0.404–0.590 cm$^{-1}$ | NUMERICAL independent potential comparison | Lebedeva *et al.* Tables 2, 4, 6; author-derived shear | Different equilibrium spacing and relaxation protocols; cross-potential discrepancy forbids KC physical amplitude promotion. |
| UD-specific signed residual | OPEN | Independent material source rule plus complete conventional comparator and held-out force data | No current coefficient, measured loss spectrum, or residual prediction. |

## Constructor checks performed

- Re-ran the exact honeycomb verifier: `PASS_EXACT_CONDITIONAL`, ranks 13/6, Betti 1/2/1, Gram factors 7/2 and 7/4, C3 equivariance.
- Re-read v20–v23 numerical JSON and checked the figures quoted in the short paper against their recorded scalar entries. Reused prior fixed-roster pressure, cutoff and Hessian step audits; this editorial pass is not independent atomistic validation.
- Rechecked the primary publisher abstract. It says **friction peaks** near the angles, with negligible load dependence relative to coalignment. The sum to 60° is a conventional lattice complement.
- Removed the longer manuscript's unsourced visual intuition as a physical explanation; tetrahedral and octahedral subdivisions are not needed for the planar carrier.
- Restricted claims about the loss spectrum to the local finite-height model. A source-only projection of 53.39% of total quadratic softening cannot be promoted to a complete UD coupling.

## Review decision

Version 2 adds a decisive cross-potential material-scale caveat. The short paper can be circulated as a clearly labeled **working mathematical hypothesis**. It is not a standalone physical explanation of the measured load-independent friction, and the present construction has no UD-specific numerical residual. Independent review should first inspect the source-to-material map and whether the selected seven-orbit source has predictive content beyond the full conventional Hessian. If that bridge is supplied, freeze coefficients and the force estimator before seeing the paired-angle validation traces.
