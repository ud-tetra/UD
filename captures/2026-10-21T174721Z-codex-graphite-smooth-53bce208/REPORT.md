# Graphite smooth-cutoff model v0.1

RESULT: PASS_SCOPED_SMOOTH_MODEL. Bath inference HOLD; physical promotion0.

All 12/12 local derivative suites pass. Fine directional energy controls: 288/288 pass. All four endpoint gates pass: True.

| Case | Cutoff Å | Max local g step error | Max energy mixed error | Min retained eigenvalue |
| --- | ---: | ---: | ---: | ---: |
| 21_dir_0 | 16 | 4.470368e-09 | 1.292076e-06 | 0.280652306 |
| 21_dir_0 | 20 | 4.469536e-09 | 3.020173e-06 | 0.280652264 |
| 21_dir_0 | 24 | 4.466168e-09 | 1.819295e-06 | 0.280652227 |
| 21_dir_10024 | 16 | 5.336844e-09 | 1.169449e-06 | 0.280730277 |
| 21_dir_10024 | 20 | 5.334764e-09 | 7.079646e-07 | 0.280730250 |
| 21_dir_10024 | 24 | 5.335607e-09 | 1.716311e-06 | 0.280728894 |
| 31_dir_10084 | 16 | 4.975915e-09 | 1.082537e-06 | 0.281046324 |
| 31_dir_10084 | 20 | 4.972998e-09 | 4.127132e-06 | 0.281046369 |
| 31_dir_10084 | 24 | 4.975179e-09 | 3.272330e-06 | 0.281046378 |
| 31_dir_10134 | 16 | 5.039570e-09 | 2.318946e-06 | 0.281139247 |
| 31_dir_10134 | 20 | 5.041130e-09 | 6.515422e-06 | 0.281139210 |
| 31_dir_10134 | 24 | 5.039861e-09 | 2.469513e-06 | 0.281139169 |

All entries in the last three columns use eV/Å². Eigenvalues use normalized sector coordinates, without mass weighting.

| Case | 20→24 Å K relative change | 20→24 Å g relative change |
| --- | ---: | ---: |
| 21_dir_0 | 8.270627e-09 | 4.531141e-06 |
| 21_dir_10024 | 5.080919e-08 | 7.978076e-06 |
| 31_dir_10084 | 8.205426e-09 | 5.166397e-06 |
| 31_dir_10134 | 8.965689e-09 | 5.248665e-06 |

## Model and frozen tests

The new model multiplies the unshifted fixed-normal KCz energy by S(t)=1−10t³+15t⁴−6t⁵ over the outermost2Å, with S=1 inside and0 outside. Exact rational elimination gives this unique polynomial of degree at most5 from six endpoint value/slope/curvature constraints. The full force includes −U_raw S_prime r_vector/r. This yields C2 pair energy away from r=0. Width2Å is imposed for this diagnostic: it is neither UD-derived nor fitted to physical data.

This is a different model from the legacy energy-shifted hard cutoff. It preserves raw forces below switch onset but changes tail forces and total energies. Every configuration was freshly relaxed from its original source structure, so same-cutoff matrix differences combine model and relaxation effects. Original legacy arrays and failures are unchanged.

The model and all tolerances were declared in FREEZE.json before new model results. This was constructor-only freezing after the legacy failures, not blinded physical testing or independently reviewed preregistration. Tests cover four pointwise primitive-periodic vertical sectors at cutoffs16/20/24Å. Local force derivatives use h=1e-4 and5e-5Å. Energy checks use first/last Helmert and breathing directions at h=.002,.001,.0005Å; both finest steps must pass. Endpoint norm limits remain K<=1e-4 and g<=1e-3 for20 versus24Å.

24 isolated-pair cases check compiled energies and all force components against separately evaluated formulas and finite energy derivatives at contact, switch onset/interior and cutoff sides. Constructor verification recomputes projected arrays, Helmert spectra, stencil arithmetic, local/endpoint flags and hashes. It is not non-constructor review.

## Baseline comparison

| Cutoff Å | Max same-cutoff K relative change | Max same-cutoff g relative change | Max centered z change Å |
| --- | ---: | ---: | ---: |
| 16 | 2.556009e-06 | 2.030946e-04 | 2.597536e-05 |
| 20 | 7.188627e-07 | 7.249823e-04 | 7.440308e-06 |
| 24 | 2.248881e-07 | 1.840432e-05 | 2.264650e-06 |

Maximum residual vertical force after CG is 1.593587e-06 eV/Å. Relaxation is numerical, not an exact stationarity certificate. Global translation is removed only for geometry comparisons and the spectrum.

## Claim boundaries

DERIVED: C2 switch polynomial and product-rule force. NUMERICAL: qualification only as reported above, within this model, finite cutoffs and retained sector. OPEN: switch-width robustness, omitted Bloch-sector stability, infinite-range behavior, physical damping and independent review. CANDIDATE: UD-specific dissipative protection remains without an independent native constraint. This audit supplies no friction prediction or empirical bridge.

Source: compute adapted from GPL LAMMPS KCz at111817ce3255b756025a0c57389908a2b719cd6b; compiled plugin inherits installed parameter parsing and neighbor setup. Installed runtime20250722 is bridged numerically by pair checks, not asserted source-byte-identical. Main observed before work: cc50f6cf0e97c86e072b80fbf884199f8029cde6; governance unchanged. Historical ledger v0.39 and CRL2 amendment do not supersede current project state; CRL2 attachment identifies itself as a proposal.

Next: freeze and test switch-width sensitivity before any bath inference. No original failure is promoted to PASS. See REPRODUCE.md and the full package for scripts, parameters, matrices and logs.
