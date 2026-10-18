from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parent;j=lambda n:json.loads((P/n).read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
v1=j('UNIFORM_CERTIFICATE.json');v2=j('UNIFORM_V2_CERTIFICATE.json');row=next(x for x in v2['rows'] if x['delta']==[1,1<<48]);actual=j('results/cyclic_unit/CERTIFICATE.json');direct=j('results/cyclic_unit/DIRECT_ERROR.json')
summary={'status':'POSITIVE_UNIFORM_IDEAL_TWO_STEP_PHASE_TOLERANCE_CERTIFIED','uniform_estimator':'Exact top209 SVD and exact least squares; actual floating convergence remains open','physical_promotion':0,'independent_review':'pending','uniform_per62vector_noise_budget':[1,1<<48],'uniform_ideal_two_step_phase_error_upper':row['ideal_two_step_phase_error_upper'],'next_larger_grid':[1,1<<47],'next_larger_grid_status':'HOLD_SUFFICIENT_BOUND_NOT_FAILURE_PROOF','actual_control':'cyclic_unit','actual_primary_two_step_phase_error_upper':actual['two_step_phase_error_radians_upper'],'actual_supplemental_assigned_error_upper':direct['circular_two_step_error_upper'],'source_cutoff_unchanged':[1,1<<24],'validation':j('VALIDATION_V2.json')['status'],'baseline_raw_projection_replay':j('RAW_SOURCE_REPLAY.json')['status'],'raw_noise_regeneration':j('RAW_NOISE_REGENERATION.json')['status'],'post_v1_refinement_disclosed':True,'uniform_actual_floating_convergence_claimed':False}
(P/'RESULT_SUMMARY.json').write_text(json.dumps(summary,indent=2))
(P/'README.md').write_text('''# Uniform ideal two-step phase tolerance

**Certified: arbitrary additive noise of norm≤2^-48 per62-channel vector preserves unique209-target matching for the ideal two-step estimator, with circular phase error<2.618e-7 radians per two-step sample.** The frozen2^-47 grid row remains HOLD; this is a sufficient-bound limit, not a demonstrated failure or optimal boundary.

The exact encoded-baseline low-rank residual is<6.960e-13. Exact matrix-power bounds reduce the noise multiplier from<1080.819 (v1) to<707.294 (v2). Both versions are retained. Unlike v1's2^-49 ball, the refined2^-48 ball reaches one nonzero raw encoding increment: at most one coordinate may change by±1 quantum in each62-vector, with arbitrary positions/signs. Real perturbations with the stated Euclidean bound are also covered. This is relative to the encoded PR195 stress record.

| Scope | Noise norm per62-vector | Two-step phase error upper | Status |
|---|---:|---:|---|
| v1 uniform ideal estimator |2^-49|2.145e-7 rad|PASS; below one raw quantum|
| v2 uniform ideal estimator |2^-48|2.618e-7 rad|PASS|
| v2 next-larger frozen grid |2^-47|4.621e-7 rad|HOLD: sufficient separation bound|
| Fresh cyclic control, actual floating output |2^-48|9.323e-10 rad|PASS; one finite record|

The supplemental validated actual assigned-target error is<7.571e-15 radians; it does not replace the primary certificate. The actual run and ideal theorem are separate evidence. Uniform floating convergence remains OPEN. Original frequencies remain ambiguous moduloπ; no SI conversion is supplied.

## What changed

Instead of inheriting the conservative source-generation error floor, the proof checks an exact low-rank approximation of the encoded baseline via cross-Grams. It explicitly charges the residual of the saved binary64 comparison shift, which is not assumed to be exact least squares. The same-team review caught and repaired that draft assumption before the original proof freeze.

The v2 refinement was motivated after seeing v1's sub-quantum result, then separately frozen before evaluation. Only the exact operator-norm upper bound for the unchanged sketch was strengthened using integer Gram powers1,2,4. Both grids, thresholds, original code and outcomes remain unchanged and retained. This is disclosed same-team proof development, not blinded or independent validation.

The fresh cyclic control was frozen before fitting. It cycles a single±quantum through the62 channels. All18,790,154 raw differences were checked and a separate generation reproduces its exact hash/gates. A separate baseline raw projection reproduces both exact cross-Grams and the raw sketch norm. Two actual original/instrumented runs emit byte-identical phases; saved-array actual proof replay agrees. Both32-row uniform grids replay, and zero coefficient proposals force every phase row to HOLD in both versions. No full Hankel matrix was allocated.

## Portable replay

Extract CORE and every WITNESS ZIP into one empty directory. Install requirements.txt with Python3.12 and run:

```bash
OPENBLAS_NUM_THREADS=1 python replay_package_v2.py
```

This verifies all package/array hashes, actual baseline basis Gram, exact cross-Gram residual arithmetic, both uniform grids, the actual floating phase witness/emission certificate and both zero-factor controls. It does not regenerate omitted raw records or claim independent execution.

For full raw recovery, recover the PR195 stress record using its pinned generation recipe and SHA256 in PROTOCOL_FREEZE.json. Stage it at the sibling path floating-timing-work/records/ramp_clock_stress.i64le. `python baseline.py --raw-replay` rechecks exact source cross-Grams and norm. `python make_record.py --regenerate /new/empty/path/cyclic_unit.i64le` regenerates the new record and compares every raw difference/hash. The completed RAW_SOURCE_REPLAY.json and RAW_NOISE_REGENERATION.json are retained. To reproduce actual fitting, run the propose.py commands in RUN_EXECUTIONS.json into fresh output folders; their source is unchanged from PR197.

Reproducible raw records and temporary caches are omitted; all actual floating arrays, baseline basis arrays, exact Grams, coefficient proposal, source receipts and PASS/HOLD outcomes are retained. See THEOREMS.md, RESULT_SUMMARY.json, PROTOCOL_FREEZE.json and REFINEMENT_FREEZE.json.

Physical promotion0. Development — no registry entry. Same-team review only; independent review and apparatus qualification remain pending. The old204/205 noise-cutoff HOLD, full-Hankel acceptance, observer/metric mapping and nominal747-dimensional hidden space are unchanged. O03 budgets are protocol controls, not theory constants.
''')
(P/'TEAM_REVIEW.json').write_text(json.dumps({'reviewer':'timing_review','scope':'Same-team read-only derivation and frozen-code audit','independent_review':False,'findings':['Saved binary64 T0 is not proven exactLS; charge sigma and use Mbar=(1+sigma)/beta. Repaired before initial protocol freeze.','Exact cross-Gram cancellation scales and parent witness hash bindings are sound.','v1 positive2^-49 ball contains no distinct int64/2^48 record.','v2 exact Gram powers1,2,4 and min outward norm bound are valid;2^-48 now reaches one quantum.','Uniform ideal estimator and finite actual floating certificate must remain separate.'],'physical_promotion':0},indent=2))
(P/'CLAIM_LEDGER.json').write_text(json.dumps({'physical_promotion':0,'claims':[{'type':'EXACT','claim':'Integer cross-Grams and exact cancellation determine encoded baseline residual; raw reprojections agree.','evidence':['baseline/PROJECTION.json','RAW_SOURCE_REPLAY.json']},{'type':'DERIVED','claim':'Uniform ideal209-target matching for arbitrary per62-vector noise≤2^-48; phase error<2.618e-7 radians per2steps.','evidence':['UNIFORM_V2_CERTIFICATE.json','THEOREMS.md']},{'type':'NUMERICAL','claim':'Fresh cyclic-unit actual floating output passes unchanged primary certificate; not all-ball floating convergence.','evidence':['results/cyclic_unit/CERTIFICATE.json','RAW_NOISE_REGENERATION.json']},{'type':'OPEN','claim':'Uniform actual-floating convergence, independent review/replay, original acquisition contract, apparatus and source/metric mapping.'},{'type':'PROTOCOL_CONTROL','claim':'All grids, noise budgets and accuracy gates remain O03 controls, not derived physical constants.'}]},indent=2))
(P/'PROVENANCE.json').write_text(json.dumps({'source_main':j('PROTOCOL_FREEZE.json')['source_main'],'parent_captures':['2026-10-18T181950Z-codex-two-step-adapter-39ce61a8','2026-10-18T184202Z-codex-two-step-noise-c54b7a12'],'protocol_freeze_sha256':sha(P/'PROTOCOL_FREEZE.json'),'refinement_freeze_sha256':sha(P/'REFINEMENT_FREEZE.json'),'initial_frozen_code_unchanged':True,'post_v1_refinement_disclosed':True,'postnumerical_packaging_helpers':['validate_v2.py','replay_package_v2.py','finalize.py','build_capture.py'],'independent_review':'pending','physical_promotion':0},indent=2))
print(json.dumps(summary,indent=2))
