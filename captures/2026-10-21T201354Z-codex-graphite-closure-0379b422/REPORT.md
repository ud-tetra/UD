# Axial-observable dynamical closure audit v0.1

RESULT: SCOPED_NONCLOSURE for both the signed axial bond-vector observable and its graph-cycle component in all36 tested material configurations. Verification passes; autonomous-channel hypothesis fails its frozen criterion. Physical promotion0.

## Frozen model and closure criterion

The maps are geometry-fixed linearizations from the preceding atom-to-chain audit. C maps the constrained primitive-periodic vertical displacement q into signed axial bond-vector increments; C_cycle applies the graph cycle projector to each Cartesian edge component. The same linear maps apply to displacement rates. Each geometry and material Hessian is frozen at the corresponding relaxed configuration. All carbon masses are equal and the replication/projection bases are orthonormal, so the common scalar mass can be absorbed into time without changing invariant subspaces. No physical clock conversion is inferred.

Write H=Q^T Ksym Q and qddot=−Hq. The state observable is(Cq,Cqdot). An autonomous linear second-order law yddot=−L y exists for all states exactly when

    C H = L C,

equivalently ker(C) is H-invariant. Necessity follows because two states differing by a hidden h in ker(C), with the same observed initial position and velocity, must have the same observed acceleration. Sufficiency defines L(Cq)=CHq, well-defined when hidden differences are annihilated. For symmetric H this is also rowspace invariance, tested by Vr^T H N=0 for orthonormal visible/hidden bases. A velocity-only first-order closure is not asserted.

The frozen primary statistic is ||Vr^T H N||F/||H||F, with pass limit1e-8. Each observed failure also exceeds10 times the coarse/fine operator discrepancy. SVD rank threshold is max(1e-12,1e-8*smax), with relative1e-6 and1e-10 rank diagnostics. All ranks are stable across this diagnostic bracket.

| Observable | Tests | Resolved nonclosure | Rank pairs (observable/material) |
| --- | ---: | ---: | --- |
| Axial bond vector | 36 | 36 | 26/27;50/51 |
| Cycle-projected axial vector | 36 | 36 | 26/27;50/51 |

## Observed leakage

| Observable | Minimum closure residual | Maximum closure residual | Minimum residual/operator-step ratio |
| --- | ---: | ---: | ---: |
| axial | 1.089780101e-03 | 1.469167484e-03 | 3.824079e+06 |
| cycle_axial | 1.089780101e-03 | 1.469167484e-03 | 3.824079e+06 |

These dimensionless residuals measure normalized operator coupling. They are not friction, energy loss or measured probabilities. The operator-step discrepancy is a numerical diagnostic, not a rigorous total error bound. Their separation is more than3.82million-fold in every case, with consistent coarse/fine results.

## A source-independent hidden-state witness

Both observables omit the same relative-layer uniform breathing coordinate b. It is defined by one constant vertical displacement per layer with opposite signs, then projected into the translation quotient and normalized. Every intralayer bond difference annihilates it, so Cb=0 and C_cycle b=0 exactly in the map algebra. The material interlayer stiffness does not preserve that hidden line.

For prepared states(q,qdot)=(0,0) and(b,0), the observed initial position and velocity agree, while their observed accelerations differ by−CHb. All72 witness checks give nonzero visible acceleration above the declared tolerance. This is a specific counterexample to autonomous closure. It is a mathematical linearized-state preparation, not an executed experiment.

The geometry-selected Householder split using b corroborates the SVD rowspace, while iterative least-squares cycle projections corroborate witness accelerations. The projector onto the numerical hidden line agrees with bb^T within1e-10.

## Minimal augmentation corollary

Numerical rank is n−1, where n=27 or51 is the full constrained material quotient. The hidden space is span(b). The tested observable rowspace is not invariant. Any invariant linear superspace containing an(n−1)-dimensional space is either that space or the full n-space; noninvariance excludes the first option. Thus the minimal autonomous linear augmentation containing these observable coordinates is the full quotient. Adding b^T q and b^T qdot restores all remaining constrained state information:54 or102 phase-space coordinates in total.

This is an exact conditional linear-algebra corollary once the rank and noninvariance hypotheses hold. Its numerical hypotheses are corroborated here. It was inferred after the primary outcomes and is explicitly not a separately preregistered test. Augmentation restores state completeness; it does not establish a smaller independently protected channel. The dimensions27/51 here are material quotient counts, not native UD chain-register identities.

## Verification, scope and disposition

All37 input hashes match:36 material matrices and the earlier map package. Constructor verification checks72 observable cases using an independent geometry-fixed basis, least-squares projector and explicit witness acceleration. Earlier response-map values agree to the frozen1e-12 relative threshold. Verification passing is separate from the scientific nonclosure result. Non-constructor review remains pending.

The calculation concerns a frozen-geometry, undamped, linearized retained sector with fixed lateral coordinates. It does not test omitted Bloch sectors, finite-amplitude geometry changes, load/temperature-dependent bath maps, nonlinear closures or exact reduced dynamics with memory. A forced model would require its input map as well; the zero-input hidden-state counterexample already defeats the claimed homogeneous closure.

DERIVED: the closure criterion, hidden-state counterexample and minimal-augmentation corollary. NUMERICAL: all72 cases resolve nonclosure at the frozen tolerance within the supplied matrices. NO-GO scope: interpreting this particular axial/cycle observable as an autonomous reduced channel in this retained model. OPEN: native material/carrier dictionary and physical damping. This does not refute all UD mechanisms or predict nonzero friction.

Next: derive the observed/hidden breathing equations and their exact memory kernel. The present finite conservative dynamics supplies no irreversible damping coefficient by itself. Earlier numerical qualifications, negative results and physical HOLD remain unchanged.
