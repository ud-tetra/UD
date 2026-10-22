# Graphite switching-width robustness v0.2

RESULT: PASS_SCOPED_WIDTH_ROBUSTNESS. Physical promotion0; bath inference HOLD.

Local suites: 36/36 pass, comprising24 new and12 inherited configurations. Fine energy controls: 576/576 new and 288/288 inherited. Width comparison gates: 36/36. Cutoff endpoint gates: 12/12. Isolated-pair implementation controls:72/72 pass.

## Width comparisons

Relative Frobenius changes use the larger-width matrix norm in the denominator. Acceptance limits are K<=1e-4 and g<=1e-3 for every individual case/cutoff/width pair. The table reports the maximum over all three width pairs and all four cases at each cutoff. These are numerical sensitivity limits, not measured physical error bars.

| Cutoff Å | Maximum K relative change | Maximum g relative change | Maximum response relative change |
| --- | ---: | ---: | ---: |
| 16 | 1.627726e-07 | 1.170538e-04 | 6.157464e-04 |
| 20 | 5.332415e-08 | 2.894551e-05 | 1.247156e-04 |
| 24 | 5.843194e-08 | 4.680415e-06 | 1.610329e-05 |

Response means the constrained stationary response K inverse g, evaluated after removing uniform vertical translation. Its comparison is diagnostic only; no acceptance threshold was imposed, and it is not friction or dissipation.

| Width Å | Maximum20-to24Å K relative change | Maximum20-to24Å g relative change |
| --- | ---: | ---: |
| 1 | 4.054183e-08 | 2.894777e-05 |
| 2 | 5.080919e-08 | 7.978076e-06 |
| 3 | 4.942616e-08 | 4.982135e-06 |

## Model and execution

The same fixed-normal KCz raw pair energy is multiplied by a C2 quintic switch over width w in{1,2,3}Å: S=1−10t³+15t⁴−6t⁵ for t=(r−(rc−w))/w in[0,1], with constant extensions. The force includes the full product rule, with dS/dr=−30t²(1−t)²/w. Width changes only this declared parameter; cutoff values, source structures, CC.KC/CH.rebo bytes, relaxation settings, force steps, retained sector and all derivative/energy tolerances remain inherited. No width was fitted to a friction target.

The1Å and3Å models were freshly relaxed and checked at all four configurations and all three cutoffs. The2Å matrix/energy/log bytes are reused from the completed v0.1 model and protected by60 hashes. Reuse is not independent replication. The parameterized2Å compiled implementation also passes24 isolated-pair controls. The new protocol was frozen before exposing1Å/3Å outcomes; the2Å baseline was already known. This is constructor-only protocol freezing, not blinded or independently reviewed preregistration.

Every local suite uses h=1e-4 and5e-5Å. Every energy suite evaluates first/last Helmert and breathing directions, including both slide axes, at h=.002,.001,.0005Å, with both finest steps required. Each case/cutoff contributes24 fine energy controls. Four subprocesses run concurrently, with one numerical thread each. All outcomes and logs are retained.

## Verification and limits

Maximum local g step discrepancy over36 configurations: 5.336844e-09 eV/Å². Maximum fine mixed energy discrepancy: 6.515422e-06 eV/Å². Maximum residual vertical force after numerical relaxation: 1.593587e-06 eV/Å. Retained positive eigenvalues are finite-precision pointwise results, not interval stability certificates.

Constructor verification recomputes projected raw-array consistency, spectra in a Helmert basis, finite energy stencils, gate flags, width/cutoff differences and input hashes. The response diagnostic is separately checked in a Householder basis. No independent reviewer or physical dataset was introduced.

DERIVED: the quintic endpoints yield C2 energy and the stated product-rule force. NUMERICAL: results apply only to widths1,2,3Å, cutoffs16,20,24Å and the four primitive-periodic vertical sectors. OPEN: arbitrary widths, infinite-range limits, omitted Bloch sectors, independent review and physical bath identification. CANDIDATE: UD-specific dissipative protection still requires a native rule selecting the dissipative coupling. No physical promotion follows from regulator robustness. Legacy hard-cutoff failures remain unchanged.

Source: GPL plugin derives from LAMMPS fixed-normal KCz source at111817ce3255b756025a0c57389908a2b719cd6b; installed runtime20250722. The2Å baseline capture is2026-10-21T174721Z-codex-graphite-smooth-53bce208. Main observed before work:06d75de17187a453a3590f3c92a7c56be7e707c5; governance unchanged.

Next: state a falsifiable, source-bound bath-selection requirement that distinguishes the proposed UD mechanism from conventional damping. Keep physical bath inference HOLD until such a rule and an independent bridge exist.
