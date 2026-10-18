from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parent;j=lambda n:json.loads((P/n).read_text());v=j('VALIDATION.json')
(P/'RESULT_SUMMARY.json').write_text(json.dumps({'status':'RECORD_WISE_ACTUAL_FLOATING_CONTRACT_VERIFIED','physical_promotion':0,'independent_review':'pending','cases':v['rows'],'new_estimator_runs':0,'raw_records_audited':3,'exact_sketch_raw_projection_replays':2,'raw_eligibility_readings_checked':3*18790154,'raw_eligibility_readings_with_replays':6*18790154,'uniform_floating_convergence_claimed':False,'negative_control_evaluations':4,'fit_carrier':'8191×321 sketch, not full raw record or Hankel','frozen_verifier_unchanged':True,'postexecution_structure_guard':'structure.py'},indent=2))
(P/'README.md').write_text('''# Record-wise admission of actual floating two-step outputs

**Two archived floating outputs pass the new frozen contract:** raw-noise eligibility, exact sketch-fit quality, and actual phase matching. An archived outside-ball record remains HOLD even though its earlier phase certificate passes. This narrows actual-output admission without claiming uniform floating convergence.

| Archived control | Raw vector error in units2^-48 | Exact sketch-fit residual upper | New two-step phase upper | Contract |
|---|---:|---:|---:|---|
| PR197 baseline |0|6.960e-13|1.268e-8 rad|PASS|
| PR201 cyclic unit |1|7.603e-13|1.691e-8 rad|PASS|
| PR200 dense unit |sqrt62|Not evaluated here|Not evaluated here|HOLD: raw noise ball|

The fit envelope is<3.209e-12 for the **8191×321 sketch**. It is not a full raw-record or Hankel residual. Every62-vector must have raw norm≤2^-48 relative to the encoded PR195 stress baseline. The retained source cutoff remains2^-24/order209. No order is forced.

The new certificate compares actual basis arrays through validated polar alignment, charges BOTH saved transition residuals and eigensystem backward error, and checks actual emitted2^-60 arguments against all209 source targets. Neither saved floating transition is assumed exact least squares. Fresh case-specific source-frame reductions are not used; only the pinned parent reference reduction/inverse is reused. The new phase bounds are conservative admission bounds and do not replace the tighter earlier source-aware phase receipts.

## Evidence and controls

These are known archived records/outputs. **No new proposer run, new apparatus data, blinding or independent review is claimed.** The protocol was frozen before the new measurements, with all archived input hashes pinned.

All three raw records have18,790,154 differences checked each; raw eligibility is replayed for all three. Exact raw-projected sketch Grams for the two eligible records are separately reproduced. Their actual saved-array phase certificates replay identically; the outside-ball HOLD also replays. For each eligible case, a zero coefficient proposal violates the exact fit gate and a zero inverse yields||V0−I||F=sqrt209≥1, refusing the inverse gate. These are four counterfactual evaluations across two cases, not four independent experiments. Original files remain unchanged.

All available archived basis/meta/phase arrays, exact Grams and untrusted alignment/coefficient proposals are retained. A structural packaging guard added after execution checks exact array dimensions and finite entries; it does not change frozen numerical code, gates or outcomes. The original frozen code and freeze hash remain intact.

## Replay

Extract CORE and every WITNESS ZIP into one empty folder, install requirements.txt with Python3.12, and run:

```bash
OPENBLAS_NUM_THREADS=1 python replay_entry.py
```

This runs structural intake, verifies all package/array hashes, recomputes basis/cross-Grams and exact fit/alignment arithmetic, replays both actual-output phase certificates, preserves the outside-ball HOLD and checks all four negative controls. It does not reread omitted raw records or rerun a proposer. Independent external replay is pending.

For full raw replay, recover the three parent records using their captured recipes and exact hashes in PROTOCOL_FREEZE.json. Stage them at the specified sibling paths, then run `python project.py --raw-replay` in a separate copy with only generated replay receipts removed. The completed raw replay receipts are already included. Each raw record is150321232 bytes; reproducible raw records and temporary caches are omitted from GitHub.

## Scope and next return

This is a record-wise floating-output acceptance contract, not a promise that every floating fit in the PR201 ideal noise ball will pass. Larger-noise phase success cannot override raw eligibility. The older204/205 instrument-noise contract HOLD, full-Hankel acceptance, original-frequency ambiguity moduloπ, physical source/preparation/clock/metric mapping and nominal747-dimensional dynamical observer kernel are unchanged.

Next: certify the exact projection-to-floating singular-subspace step and extend the frozen intake to separately selected records; seek an independent raw/witness replay. All O03 tolerances remain protocol controls. Physical promotion0; development — no registry entry; same-team verification only.
''')
(P/'CLAIM_LEDGER.json').write_text(json.dumps({'physical_promotion':0,'claims':[{'type':'EXACT','claim':'Three archived raw records have every difference checked; two eligible raw-projected sketch Grams are reproduced.','evidence':'results/*/{RAW_ELIGIBILITY,RAW_REPLAY,PROJECTION_REPLAY}.json'},{'type':'DERIVED','claim':'Measured polar alignment, both actual shift residuals and eigenpair/inverse/argument bounds certify actual returned phases under the stated gate conditions.','evidence':'THEOREMS.md'},{'type':'NUMERICAL','claim':'Baseline and cyclic-unit archived outputs pass; dense-unit HOLDs on raw eligibility while its previous phase certificate remains valid.','evidence':'VALIDATION.json'},{'type':'OPEN','claim':'Uniform floating convergence; independent raw/witness review; apparatus qualification and original noise/full-Hankel contracts.'},{'type':'PROTOCOL_CONTROL','claim':'All O03 budgets and quality thresholds are controls, not theory constants.'}]},indent=2))
(P/'PROVENANCE.json').write_text(json.dumps({'source_main':j('PROTOCOL_FREEZE.json')['source_main'],'protocol_freeze_sha256':hashlib.sha256((P/'PROTOCOL_FREEZE.json').read_bytes()).hexdigest(),'archived_controls_known_before_freeze':True,'new_proposer_runs':0,'frozen_code_changed':False,'postexecution_helpers':['structure.py','replay_entry.py','finalize.py','build_capture.py'],'parent_captures':['2026-10-18T181950Z-codex-two-step-adapter-39ce61a8','2026-10-18T184202Z-codex-two-step-noise-c54b7a12','2026-10-18T192301Z-codex-uniform-two-step-8a71c9d3'],'physical_promotion':0,'independent_review':'pending'},indent=2))
print(json.dumps(v,indent=2))
