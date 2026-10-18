# Gauge-invariant preparation certificate — GPC v0.1

Development; DERIVED CONDITIONAL; constructor verification; independent review pending; physical promotion 0.

The eight-page manuscript proves a constructive global upper bound on distance to the frozen neutral critical gauge/species-phase orbit. A rooted spanning tree supplies 14 full cycle holonomies and two matter coherences. Electric energy, two coherence scalars, 14 real cycle traces and ten active cycle moments give 27 real gauge-invariant inputs. Their exact score satisfies d²≤P globally when the first coherence is nonzero. Within d≤1/8, P≤(442425/49)d²≤10000d². P vanishes exactly on the reference orbit. This separates that orbit, not all states.

Guaranteed rational scalar enclosures give an upper score without a local state-chart assumption. A score at most δ²=Nη⁴/(1600 max(a,25N)) certifies entry into the frozen endpoint robustness theorem's initial ball, conditional on its other model/error/admissibility premises. The simple uniform allocation ε≤δ²/180 is sufficient under the explicitly stated ideal-centered interval contract. Its unit example is about 2.93e-43 in mathematical units: neither necessary precision nor laboratory calibration.

Two exact obstructions explain the additional inputs: configuration readouts miss arbitrary zero-Gauss electric circulations at every rank; for rank≥2, the complete history of active dressed loops and densities misses independent unused-color dynamics. This is distinct from the record-only observer/sketch kernels in other workstreams.

## Replay

- `python3 verify_preparation.py` uses the Python standard library. It regenerates 46 exact finite-topology and rational-arithmetic checks, four accepted/rejected interval fixtures and two invalid-input controls in PREPARATION_CERTIFICATE_v0.1.json. Analytic geometric inequalities and all-time block invariance are proved in the manuscript, not established by finite tests.
- `OPENBLAS_NUM_THREADS=1 python3 check_preparation_geometry.py` additionally uses NumPy and SciPy. Eight full-matrix perturbation fixtures (ranks 1,2,3,5; scales 1e-3 and 1e-9), four zero-Gauss hidden-electric controls and three unused-color configuration controls are floating diagnostics. Random perturbations need not be zero Gauss because the distance bound holds on the full fixed-norm manifold. Direct residual norms avoid trace-subtraction cancellation.
- `python3 preparation_certificate.py RECORD.json --target-squared RATIONAL` returns a rigorous arithmetic upper score conditional on certified input enclosures. Format is in the frozen certificate fixtures. A failure to certify is inconclusive. Input realizability, joint coverage, model identification, norm/Gauss validity and coefficient/drift limits remain external obligations. The calculator does not silently clip corrupt intervals.

The unchanged parity and endpoint budget helpers and frozen endpoint certificate retain their original proof scope. No physical dataset is ingested or reanalyzed, no coefficient ledger/action changes occur, and no physical GUT conclusion is promoted. The next mathematical priorities are proof review, tighter preparation/energy bounds and a residual-admissibility theorem before physical mapping/data work.
