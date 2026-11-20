# Constitutive action selection v0.4 — mainline DEVELOPMENT capture
Date: 2026-11-15. Historical March packet inputs are preserved in inputs/. Previous development PRs: https://github.com/ud-tetra/UD/pull/514 and https://github.com/ud-tetra/UD-Physics/pull/388.

DERIVED_CONDITIONAL: March stylized sine two-site phase update is gradient descent of E=kappa[1-cos(phi)] under continuous symmetric two-site assumptions. This energy alone does not fix a stochastic stock-transfer readout or phase noise.

EXACT_CONDITIONAL: for a finite reversible generator Q_st=c_st/pi_s, each nonnegative symmetric edge conductance is an allowed dynamical mobility. The quadratic Onsager current action has a unique current at FIXED c but does not select c. Its quadratic entropy is monotone for every such c.

NO-GO_SCOPED: two 672-state generators share admitted support, invariant phase equilibrium pi_d=(16,4,1,4)/25, the same total phase traffic 4/5, stock conservation and detailed balance. Burden readout correlations match through order 3 and differ at order 4 by 729/400. A phase-blind control makes the distinction vanish. Donor nonlinear response remains separately free.

Assumed inverse phase noise beta=ln4 is illustrative for exact rational arithmetic, NOT a native source-derived constant. The two channel p=(1+cos phi)/2 law remains a candidate readout, NOT a forced physical coupling. The original master_action.md is an effective coarse-grained action, not this constructed Onsager action. No G05/G06, metric, SI clock, Born, gravity, cosmology or physical bridge promotion.

Complete test scripts, dual check receipts, historical inputs and SHA-256 manifest are inside this capture; no originals overwritten. Local tests PASS. Non-constructor review and repository CI NOT_RUN. Physical Promotion=0.
