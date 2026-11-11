# THM-534 v0.7 execution and publication receipt — 2026-10-21

**Artifact:** THM534_BURDEN_GATE_CURVATURE_CONTINUITY_v0.7.
**Status:** constructor PASS_SCOPED / development / no registry entry. **Physical promotion: 0.**
**Theorem manuscript:** [S18–S22](THM534_BURDEN_GATE_CURVATURE_CONTINUITY_v0.7.md)
**Proof/dependency delta:** [v0.7 claim ledger](THM534_BURDEN_GATE_CLAIM_LEDGER_DELTA_v0.7.md)
**Upstream provenance:** UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2), Q153, Q155, Q156, Q158, Q162; distinct Q163 time/mixing normalization not imported.

## Exact constructor check
[Symbolic verifier](verify_thm534_burden_gate_curvature_v0_7.py): PASS.
- Signed chain identities and unit-edge Hodge identity.
- 64 gate masks × four vertex unit burdens (256 exact basis cases).
- Entrywise nonnegativity, total-burden continuity, double-stochastic update, nonexpanding variance.
- Rank distribution for B2ᵀ H B1ᵀ: 0—2, 1—12, 2—38, 3—12.
- Only all-off and all-on binary masks are flat for *all* burden sources.
- Six signed edge-orientation rebasings preserve redistribution and typed face circulation.
- Exact masked witness: j=(0,1/4,1/4,0,0,0), rho'=(1/2,0,1/4,1/4), F=(-1/4,-1/4,0,0).
- Exact Hodge receipt: 4||j||²=1/2=3/8+1/8.
- Exact discrete cochain closure B3ᵀ F=0.

## Additional numerical time-varying-mask control
[Multistep verifier](verify_thm534_burden_multistep_v0_7.py): PASS (constructor only).
- Eight seeded nonnegative initial states × 128 evolving binary gate masks = **1,024 finite steps**, seed 534070. Gate masks are randomized controls, not a physically derived rule.
- 157 steps yielded nonzero face circulation above the declared numerical threshold.
- Maximum total-stock drift 2.220446049250313e-16.
- Maximum closed-cochain residual 6.938893903907228e-18.
- Maximum Hodge identity error 6.938893903907228e-18.
- Maximum burden-variance increase 0.0.

## Local release-byte SHA-256 (not GitHub blob hashes)
- THM534_BURDEN_GATE_CURVATURE_CONTINUITY_v0.7.md: 763b2422e5380263963497e2f6dd56da38c48105a1b3b455702d4f8abf7c5df4.
- verify_thm534_burden_gate_curvature_v0_7.py: 2e964bf0b788400639c7ae13539127a8b993f3ac718f4d67025e1be94099363f.
- verify_thm534_burden_multistep_v0_7.py: ba32b0bd42b79a26f377716c5a7eefd4293fbf1d9997eaf8f8073ee404e289f6.

A local reproducible release ZIP also contains the actual locally executed scripts and a JSON manifest. Separately reconstructed GitHub verifier scripts were API read-back verified, **not asserted byte-identical** to the ZIP. Exact mathematical checks are reported for local execution; GitHub read-back is a file-publication check, not an independent compute replay.

## Claim boundary / decision
**Earned:** nonuniform hard-gated normalized K4 relaxation can produce nonzero **abelian face circulation** while vertex burden remains nonnegative and conserved under the declared one-event rule. Uniform gates produce zero face circulation from pure gradients. The current is not the physical phase-quadrature source of v0.6, and B2ᵀj is **not** the v0.6 covariant nilpotency defect B1N.

**Unresolved:** derive hard-gate masks from actual UD (rho,theta,chi,sigma,b) dynamics; select seam U(1) phase normalization and physical action/time units; prove physical retained-burden plus radiative/latent/vacuum and boundary continuity; specify empirical readout independent of historical THM-534 weights; obtain non-constructor adversarial review. Do not promote to electromagnetic curvature, mass-energy or quantum probabilities.

**Exposure:** historical THM-534 known before this target-exposed development, not target-blind independent physical validation. **Physical promotion 0.**
