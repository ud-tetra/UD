from pathlib import Path
import json,hashlib,datetime,uuid,subprocess,shutil,gzip
P=Path('/workspace/scratch/f3d1c2f040c9');R=P/'ud-repo';H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();J=lambda p:json.loads(p.read_text());review=P/'c31_review';rr=J(review/'FINAL_REVIEW.json');assert rr['status'].startswith('PASS')
for n,h in rr['source_hashes'].items():assert H(P/n)==h
assert rr['root_theorem_sha256']==H(P/'c31_THEOREM.md')
for line in(review/'VERIFICATION_HASH_MANIFEST.sha256').read_text().splitlines():
 h,n=line.split(None,1);assert H(review/n.strip())==h
it=J(P/'c31_integration_results/INTEGRATION.json');assert it['steps']==16 and it['decoder_receipt']['whole_step_coordinates_checked']==42240 and not it['full8192_accuracy_claim'];assert(P/'c31_test_final/CONFORMANCE.json').read_bytes()==(P/'c31_test_final_replay/CONFORMANCE.json').read_bytes()
now=datetime.datetime.now(datetime.timezone.utc);base=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip();cid=now.strftime('%Y-%m-%dT%H%M%SZ')+'-codex-native-actions-'+uuid.uuid4().hex[:8];C=R/'captures'/cid;C.mkdir();parent=R/'captures/2026-10-21T013801Z-codex-source-actions-9c7b87b9'
for n in ['c31_action.cpp','c31_certify.py','c31_tests.py','c31_integration.py','c31_run_timed.py','c31_benchmark.py','c31_reproduce.py']:shutil.copyfile(P/n,C/n)
shutil.copyfile(parent/'c30_oracles.py',C/'c30_oracles.py');shutil.copyfile(parent/'OPERATOR.txt.gz',C/'OPERATOR.txt.gz')
for src,dst in [('c31_THEOREM.md','THEOREM.md'),('c31_FREEZE.json','INITIAL_FREEZE.json'),('c31_NATIVE_FREEZE.json','NATIVE_FREEZE.json'),('c31_INTEGRATION_FREEZE.json','INTEGRATION_FREEZE.json'),('c31_FINAL_FREEZE.json','FINAL_FREEZE.json'),('c31_BUILD_RECEIPT.json','BUILD_RECEIPT.json'),('c31_REPLAY_RECEIPT.json','REPLAY_RECEIPT.json'),('c31_forward_final_runtime.json','FORWARD_RUNTIME.json'),('c31_adjoint_final_runtime.json','ADJOINT_RUNTIME.json')]:shutil.copyfile(P/src,C/dst)
for n in ['NATIVE_CONSTANTS.json','SOURCE_BINDINGS.json']:shutil.copyfile(P/'c31_math_final'/n,C/n)
shutil.copyfile(P/'c31_test_final/CONFORMANCE.json',C/'CONFORMANCE.json');shutil.copyfile(P/'c31_benchmark_results/BENCHMARK.json',C/'BENCHMARK.json');shutil.copyfile(P/'c31_integration_results/INTEGRATION.json',C/'INTEGRATION.json');(C/'INTEGRATION_OUTPUT.txt.gz').write_bytes(gzip.compress((P/'c31_integration_results/OUTPUT.txt').read_bytes(),compresslevel=9,mtime=0))
(C/'construction').mkdir()
for n in ['c31_action_initial.cpp','c31_constants_initial.json','c31_forward_runtime.json','c31_adjoint_runtime.json']:shutil.copyfile(P/n,C/'construction'/n)
(C/'review').mkdir()
for n in set(rr['capture_allowlist']+['FINAL_REVIEW.json','VERIFICATION_HASH_MANIFEST.sha256']):shutil.copyfile(review/n,C/'review'/n)
(C/'root').mkdir();shutil.copyfile(P/'c31_build.py',C/'root/build_capture.py');(C/'governance').mkdir()
for n in ['20-UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39-2-.md','21-UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md']:shutil.copyfile(P/'project_sources'/n,C/'governance'/n)
(C/'CORRECTION_REGISTRY.json').write_text(json.dumps({'new_frozen_mathematical_retractions':0,'prior_results_changed':False,'preliminary_measurement_correction':{'found_by':'root construction/self-review','problem':'First native timing helper used cumulative RUSAGE_CHILDREN; peak RSS could include a preceding compiler child.','replacement':'Final paired benchmark uses os.wait4 specific-child rusage; preliminary peak is not accepted as standalone action memory.','scope':'Initial C31 memory diagnostic only; final exact action/error results unaffected.'},'source_reader_refinement':{'found_by':'separate same-team review','change':'Initialize and validate incidence-count extraction before use; no numerical algorithm change.','validation':'Final compiled probes/rejections and full output replay pass'},'session_wide_retraction_ratio':'NOT_COMPUTABLE','physical_promotion':0},indent=2)+'\n')
(C/'CLAIM_LEDGER.json').write_text(json.dumps({'lane':'Development — no registry entry','origin':'PR316 exact source action proof plus new native104 overflow/rounding proof and actual execution','constructor':'Codex root','reviewer':'Separate same-team source/arithmetic/backend review, not external promotion authority','claims':[{'id':'NAT1','type':'DERIVED_ALGORITHM_CERTIFICATE','statement':'Native signed128 propagation at grid104 has finite safe-overflow bounds and unchanged absolute action errors<2^-68 on domains2048/2049.','dependencies':['Pinned source H/observer','Exact rational bounds','Correct audited build/runtime','NATIVE_CONSTANTS.json']},{'id':'NAT2','type':'EXECUTED_CONFORMANCE','statement':'Full native/reference action differences meet the sum of proved errors; native exact replays pass.','dependencies':['CONFORMANCE.json','Separate own compiled halfstep/rejection probes']},{'id':'NAT3','type':'EMPIRICAL_STANDALONE_PERFORMANCE','statement':'Paired observed speedups6.7408forward/6.4258adjoint; specific-child peak RSS11392/11264KiB.','dependencies':['BENCHMARK.json','wait4 perchild methodology'],'scope':'This measured environment, not worstcase or full-pipeline benchmark'},{'id':'NAT4','type':'EXECUTED_FINITE_INTEGRATION','statement':'Actual2640-state16-step decoder passes42240 arithmetic checks,15forward+16adjoint actions.','dependencies':['INTEGRATION.json','Pinned C29 decoder and C30 adapter','Native buildreceipt'],'scope':'N16 only; no8192 convergence/gain/accuracy promotion'}],'open':['Full8192 extraction and runtime','Physical/input error evidence','New compressed/preconditioned method or different floating implementation'],'hidden_space':'641 nominal dimensions unrecovered','external_promotion_review':'PENDING','physical_promotion':0},indent=2)+'\n')
(C/'README.md').write_text('''# Native actions preserve the error contract and extend real decoder execution

Development — no registry entry. External promotion review PENDING; Physical Promotion=0.

The weighted600-cell map stays unchanged. New signed128-bit propagation uses104 internal fractional bits and the same degree40 Taylor method; delivered inputs/outputs remain dyadic96. Exact source, rounding and overflow proofs preserve forward/adjoint absolute errors<2^-68 on state ball2048/data ball2049. GMP remains only for exact external norm checks. Every native term is guarded, and all admitted sparse accumulators/partial sums are proved below signed128 limits.

Full actual forward and adjoint outputs pass comparison with the audited128-grid GMP reference under the sum of their error bounds. Their bytes differ because grids differ; same-method replays are byte-identical. Separate same-team review reconstructs constants and checks eight compiled native halfstep probes/21120 final coordinates,844800 independently evaluated term divisions and nine input/reader rejection cases. Binary intermediate terms are not exported or claimed compared.

## Paired measured performance

| Action | GMP seconds | Native seconds | Observed ratio | Native child peak KiB |
|---|---:|---:|---:|---:|
| Forward |63.47|9.416|6.74|11392|
| Adjoint |52.19|8.122|6.43|11264|

The helper uses os.wait4 for the specific action child. This corrects a preliminary cumulative-child RSS diagnostic that could include earlier compiler memory. Final numbers are environment-specific standalone observations, not worstcase guarantees, independently repeated lab timings or total Python-wrapper/pipeline memory.

A real full2640-state sixteen-step C29 decoder run uses15forward+16adjoint actions and passes42240 Arb whole-coordinate checks. Its source/build/operator/input/output bindings are retained. It is an extension from N2, not an N8192 convergence or accuracy result. In particular, the<512 final decoder gain is not assigned to early iterates. The641 hidden components remain unrecovered; all physical/input premises remain HOLD.

## Replay

```bash
python /absolute/capture/c31_reproduce.py --repo /absolute/UD --out /absolute/new-workspace --integration --benchmark
```

Requires a C++17 compiler supporting signed__int128, Linux64 GMP and python-flint for integration. The explicit replay builds the new source and the pinned earlier reference for numerical conformance; archived executables are not run merely for ingestion. It regenerates source data/inputs, performs actual full action comparisons and byte replays, optionally runs16 decoder steps and a paired benchmark. Allow several minutes. Compare exact bounds and output hashes; machine/build/time provenance may differ. The replay orchestration was syntax/help checked; its constituent commands were executed in this turn, not a separate end-to-end orchestration replay.

The sourceoperator hash and trusted expected executable hash remain checked before every callback. The compiler, GMP implementation, stable files and trusted build provenance remain assumptions; no portable formal compiler or runtime verification is claimed. OPERATOR.txt.gz retains C30 bytes, including its128 metadata field; the separate native backend declares104.

No full F,F^TF or287-GiB Hankel is stored. Large action vectors are reproducible and hash-bound; the final16-step output is retained compressed. Full8192 extraction/performance is OPEN. Further certified acceleration or reusable compression is the next practical task before attempting the complete run. Separate optimized/floating estimators need their own conformance; no sixratio/Hankel/physical gate is transferred.

Ledger v0.39/CRL-2; O03 tolerances, grid104, degree40 and guards are controls, not theory constants.0 new frozen mathematical retractions; full-session ratio NOT_COMPUTABLE. External promotion review PENDING; Physical Promotion=0. Gap2_FINAL_Finite_Genesis.png unavailable/unused—please re-upload if needed. Notes/ASTER unused. No public-site/Project-board deployment or outreach asserted. CI/merge/tracking separately reported.
''')
(C/'RUN_FOOTER.md').write_text('''A. Derived: Native104 propagation is safe in signed128 and preserves action errors<2^-68 on the same source/model/domains.

B. Executed: Full native/reference conformance and exact native replays PASS; own independent compiled probes/rejections PASS; actual2640-state16-step decoder passes42240 arithmetic checks. Paired observed speedups6.74/6.43; specific-child peaks11392/11264KiB.

C. Limits: No8192 convergence/accuracy or full-pipeline benchmark. Build/runtime trust remains premise;641 hidden dimensions unrecovered; physical/input evidence HOLD. Preliminary cumulative RSS diagnostic replaced with specific-child measurement.

D. Append-only capture/event/PR; CI/merge/tracking separately reported. Next: certified reusable acceleration/compression, then complete extraction. No deployment/outreach asserted.

Governance: Ledger0.39/CRL-2; Development—no registry entry; O03 controls not constants; external promotion review PENDING; Physical Promotion=0.0 frozen mathematical retractions; sessionratio NOT_COMPUTABLE. PNG unavailable/unused—please re-upload if needed. Notes/ASTER unused.
''')
m={'capture_id':cid,'timestamp_utc':now.isoformat(),'base_commit':base,'status':'NATIVE_ACTION_CERTIFICATE_CONFORMANCE_AND_N16_PASS_FULL8192_OPEN','lane':'Development — no registry entry','physical_promotion':0,'external_review':'PENDING','supersedes':[],'extends':['2026-10-21T013801Z-codex-source-actions-9c7b87b9'],'verification_scope':'New native104 finite overflow/error proof, full-vector conformance and exact replays, observed paired standalone timing and actual N16 fullstate decoder execution. FullN8192 and physical inputs remain OPEN/HOLD.','files':[]}
for f in sorted(C.rglob('*')):
 if f.is_file():m['files'].append({'path':str(f.relative_to(R)),'sha256':H(f),'size_bytes':f.stat().st_size,'provenance':'Pinned source/reference; new native algorithm/proofs; exact conformance/replay and actual measured/finite execution; separate same-team review; supplied governance','status':'Development; full8192 OPEN; external promotion review PENDING'})
(C/'MANIFEST.json').write_text(json.dumps(m,indent=2)+'\n');(R/'events'/f'{cid}.json').write_text(json.dumps({'capture_id':cid,'timestamp_utc':now.isoformat(),'base_commit':base,'event_type':'NATIVE_SOURCE_ACTION_OPTIMIZATION_AND_N16_DECODER','manifest':str((C/'MANIFEST.json').relative_to(R)),'status':m['status'],'full8192_execution':False,'physical_promotion':0,'external_review':'PENDING'},indent=2)+'\n');s={'capture_id':cid,'capture_path':str(C),'base':base,'branch':'codex/'+cid};(P/'c31_state.json').write_text(json.dumps(s,indent=2)+'\n');print(json.dumps(s,indent=2))
