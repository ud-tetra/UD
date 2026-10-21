# Independent review of the source-bound actions

PASS within the stated fixed-source Linux64/GMP reference model. The forward and adjoint implementations supply uniform absolute error bounds below2^-68 on state ball2048 and data ball2049. This qualifies the mathematical action-oracle slots in C29, subject to the explicit build/runtime assumptions. It does not establish completion, accuracy or runtime of the full8192-step decoder, nor physical/input admission.

## Source and numerical proof

The reviewer rebuilt every one of the14880 integer H entries and the ordered unique62-coordinate observer directly from pinned JSON data. The reconstructed bytes agree with the admitted OPERATOR hash. Skewness,1800 weighted chain-square columns, max absolute H-row sum24 and boundary squared-norm caps24,15,15 are independently checked. Pair-annihilating chain channels imply normK<=sqrt24<5. A row-sum bound alone would not prove that spectral estimate, and arbitrary matrices accepted by the raw CLI are not admitted source operators.

The degree40 tail begins at41 and has the correct geometric ratio5/84. Its exact upper is approximately6.5729998966e-34. Each fixed-point term division introduces vector error below52*2^-128. The elementary recurrence gives the first three term bounds1,9/4,23/8 times that quantity and bounds every later term by3 times it. Forty terms therefore contribute less than6240*2^-128. Integer multiplication and accumulation introduce no further rounding under the assumed GMP semantics.

The global argument is sound. Compare a rounded step with the exact skew exponential at the current computed input, then propagate prior errors isometrically. The loose computed-state cap2^18 is closed by induction from exact forward states<=2048, exact normalized adjoint partial sums<=2049, and accumulated error<1. The adjoint partial-sum bound uses Cauchy-Schwarz over the complete data norm and1/64 normalization. It does not assume per-time data amplitudes are separately small.

All encoding shifts agree with the implementation: external96 to internal128 uses32; forward normalization/delivery uses38; adjoint injection uses26 exactly; final adjoint delivery uses32. The reverse injection/negative-propagation order gives precisely the intended F-transpose sum. No adjoint injection rounding is omitted.

Five independent exact rational error fractions match the source certificate. Including final delivery, the forward upper is approximately7.121319393e-25 and the adjoint upper7.064268972e-25. Both are below2^-79 and hence below the required2^-68. The rounded actions need not be exactly linear or transposes; their pointwise uniform-domain error bounds suffice. A composed normal action has error at most2^-67 because normF<=1 and a computed forward output lies inside data ball2049.

## Independent actual-backend evidence

The reviewer executed the compiled half-step binary on its own synthetic seeds: zero, dense signed dyadics, and a selected-tetrahedron state exactly at the norm2048 boundary, for both signs. All15840 delivered coordinates match a separate Python-bigint implementation with explicit signed truncation. That reference evaluates633600 term-coordinate divisions; the binary's intermediate terms are not exported or claimed compared. Source, operator and binary endpoint hashes remain equal. Runtime probes identify GMP6.3.0 and64-bit unsigned long under the recorded16-byte ABI struct model.

Independent checks of the full action artifacts also pass:

| Evidence | Independent review |
|---|---|
| Two actual4096 forward records and one adjoint record | Input/output hashes, dimensions and exact input norms agree |
| Full-size duality residual and scale128 discrepancy | Recomputed exactly; within the proved budgets |
| Actual forward prefixes j0,j1,j2 for two inputs | All372 selected coordinates match independent internal-grid Taylor evaluation |
| Source/binary binding and out-of-domain rejection | Three adapter failure probes pass before a trajectory call |
| Source/constants, two actual trajectory outputs and final tests | Six replay pairs are byte-identical |
| Final actual2640-state two-step integration | Source/build/input/output bindings and5280 Arb checks verified |

The two-step integration uses one forward and two adjoint actions through the unchanged C29 decoder interface. Its output matches the initial numerical run exactly. It is an N=2 wiring/arithmetic test, not the N=8192 convergence experiment. The reviewer did not rerun a full4096 trajectory or the complete decoder, and did not execute the producer's Python certificate/test drivers.

## Build binding, implementation scope and limits

The source review found an executable-binding gap in the initial adapter: it pinned the operator but could accept any executable. The final version requires a trusted expected executable hash and checks both executable and source bytes before every call. The integration now verifies the source/build receipt and binds the exact adapter, binary and build receipt. Wrong expected-binary hashes are rejected. Initial sources/results remain construction history; the arithmetic and numerical algorithm did not change. No frozen mathematical retraction is needed.

The build identity receipt is not trusted-computing attestation. Correct compiler/GMP execution, the recorded Linux64 ABI, trusted build provenance and stable intended files remain premises. The finite probes do not constitute a formal proof of every runtime input or a race-free executable snapshot. The raw CLI's acceptance alone is not the source-bound action certificate. The admitted operator, domains and audited executable are essential.

Observed timed replays report about64.69 seconds/14600KiB peak child RSS for the near-domain forward action and57.13 seconds/14216KiB for the adjoint. These are hash-bound empirical receipts, not independent timing measurements by this reviewer, worst-case bounds or total Python-wrapper/pipeline memory figures. No full matrix F, F-transpose F or287-GiB Hankel is used by this reference. The full8192 decoder requires16383 actions, so its performance remains a material open task.

The unavailable Boost build was not executed; the actual backend uses GMP and is explicitly platform-bound. The source-bound algorithm and finite full-size actions are now concrete. Full8192 execution, any different optimized/floating backend and every physical preparation, timing, noise or constitutive premise remain HOLD. Nominal641 hidden components are not certified reconstructed. No old six-ratio/Hankel/physical gate is transferred.

Development — no registry entry. Reference action certificate and two-step integration PASS. Full8192 execution/performance and physical/input evidence HOLD. External review PENDING. Physical Promotion=0.
