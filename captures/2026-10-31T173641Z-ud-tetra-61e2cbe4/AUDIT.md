# UD Native Shell Response / Residual Vector Audit v0.1
Status: EXACT (ratio identity and scoped no-go), NUMERICAL (diagnostic), OPEN (native response and physical bridge)
Date: 2026-10-31
Physical promotion: 0
Lane: DEVELOPMENT / NO PHYSICAL REGISTRY PROMOTION

## Historical usage
The six-page Unified Dynamics v2.2 historical manuscript Part X uses Q_obs=Q0*(1+z_Q) and calls z_Q "dressing". Its Part IV lists C_QCD*C_EW*C_grav regime factors without independently derived functions. Prior UD_28_PREDICTIONS_DRESSING_LEDGER_v1.0_REPAIRED required native source derivation before matching. Later governance disallowed post-hoc fitted dressing, replacing it with typed shell response language and diagnostic-only residuals. Do not reinstate generic dressing as an admitted physics correction.

## Exact definitions, restricted domain
For a dimensionless positive observable Q with a proposed native bare value Q0>0 and matched measured value Q_obs>0:
  e_Q=(Q_obs/Q0)-1         (comparison-only relative residual)
  d_Q=ln(Q_obs/Q0)         (comparison-only log residual)
These measure disagreement; they do NOT derive its mechanism. Without matching carrier, units, scale, scheme, and readout there is no physical comparison. ns is cosmological rather than a lab quantity.

## Measurement-facing diagnostic examples
Source bare values: alpha0=7/960; mu/e=4343/21; tau/mu=101/6; tau/e=438643/126; ns0=185/192.
Measured context: CODATA 2022 inverse alpha 137.035999177; m_e 0.51099895069 MeV; m_mu 105.6583755 MeV; PDG2025 m_tau 1776.93 MeV; Planck2018 ns=0.9649.
Relative residual e_Q:
  alpha     +0.000779780251167  (+0.0779780251 percent)
  mu/e      -0.000199415869719  (-0.0199415870 percent)
  tau/mu    -0.000929197328025  (-0.0929197328 percent)
  tau/e     -0.001128427901050  (-0.1128427901 percent) [DEPENDENT RATIO]
  ns        +0.001409729729730  (+0.1409729730 percent) [COSMOLOGY]
These residuals have differing signs and magnitudes, so no single numerical scalar makes every source quantity equal to its observed counterpart.

## EXACT lepton ratio theorem: universal scalar obstruction
Let r_te=r_tm*r_me hold for both source ratios and lab masses. If a common nonzero positive scalar c multiplies each of r_me,r_tm,r_te, compatibility implies c*r_te^0=c^2*r_te^0, hence c=c^2 and c=1. Therefore the same nontrivial universal ratio multiplier is impossible under these hypotheses. A single scalar applied to all lepton masses cancels out of all mass ratios, so it also cannot repair ratio discrepancies.

## Exactly lawful log-response vector (not yet a physical mechanism)
Let d_me=log[(mu/e)_obs/(mu/e)_0], d_tm similarly, d_te similarly. Then EXACT:
  d_te=d_tm+d_me.
Fix arbitrary state-reference psi_e=0 and set psi_mu=d_me, psi_tau=d_te.
  psi_lepton=(0,-0.000199435756,-0.001129065055)
  psi_tau-psi_mu=-0.000929629299.
This is a two-degree-of-freedom product-of-ratios coordinate, NOT a new gauge field or native UD dynamical source. The reference shift psi_l->psi_l+c leaves ratios unchanged; no absolute native mass-scale derived by the shift.

## Error of measurement versus structural mismatch
Measured uncertainty sigma_obs is NOT the physical response e_Q. Under independent measured and theoretical errors, a standardized residual uses (Qobs-Qpred)/sqrt(sigma_obs^2+sigma_th^2); for correlated rows use r^T C^-1 r with full typed covariance and independent degrees of freedom. The tau/e ratio is not independent of mu/e and tau/mu. Without a derived physical mapping and source/uncertainty model, the large lab precision alone does not make z_Q a physical UD correction.

## What would establish a common native response?
An admissible pre-exposure sector map would be d_Q^pred=sum_a M_Qa*s_a, with M determined from source operators and s_a from native packet state/transport/holonomy rather than solving backwards from measured discrepancies. Freeze operators, readouts, schemes, energy scales, uncertainty covariance, controls and acceptance thresholds before any held-out target comparison. A single residual vector cannot establish a rank-one mechanism; repeated contexts or independent source-derived loading directions are required.

## Sources and limits
- Historical v2.2 uploaded PDF, Parts IV, VI, X; original corrected arithmetic in draft PR #466.
- UD coefficient ledger v0.39 dated 2026-08-22: C02, C06, C07, C08 and C10; physical promotion zero. Newer v0.65 and v0.85 ledgers are distinct source versions.
- NIST CODATA 2022 https://physics.nist.gov/cuu/pdf/wall_2022.pdf
- NIST mu/e https://physics.nist.gov/cgi-bin/cuu/Value?mmusme
- PDG 2025 tau https://pdg.lbl.gov/2025/web/viewer.html?file=..%2Flistings%2Frpp2025-list-tau.pdf
- Planck 2018 https://doi.org/10.1051/0004-6361/201833887
- Full local output UD_SHELL_RESPONSE_RESIDUAL_AUDIT_v0.1.zip SHA256 fb240089e54edf12ab149f6370afbda3bc5580f3851eb9e440fce98e1b13dba1; local PDF absent (not requested), includes full Markdown, numeric JSON receipt, replay Python and SHA manifest. This GitHub text capture is a smaller mirror, NOT the full local ZIP.
- All numerical comparisons are conditional; no source-to-physical bridge established. Independent review pending.
