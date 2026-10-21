from pathlib import Path
import json,hashlib,datetime,uuid,subprocess,shutil,gzip
P=Path('/workspace/scratch/f3d1c2f040c9');R=P/'ud-repo';H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();J=lambda p:json.loads(p.read_text());review=P/'c30_review';rr=J(review/'FINAL_REVIEW.json');assert rr['status'].startswith('PASS')
for n,h in rr['source_hashes'].items():assert H(P/n)==h
assert rr['root_theorem_sha256']==H(P/'c30_THEOREM.md')
for line in(review/'VERIFICATION_HASH_MANIFEST.sha256').read_text().splitlines():
 h,n=line.split(None,1);assert H(review/n.strip())==h
integ=J(P/'c30_integration_final/INTEGRATION.json');assert integ['status'].startswith('PASS_ACTUAL2640') and integ['steps']==2 and not integ['full8192_accuracy_claim'];assert(P/'c30_integration_final/OUTPUT.txt').read_bytes()==(P/'c30_integration_results/OUTPUT.txt').read_bytes()
assert(P/'c30_test_build/ACTION_TESTS.json').read_bytes()==(P/'c30_test_build_replay/ACTION_TESTS.json').read_bytes()
now=datetime.datetime.now(datetime.timezone.utc);base=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip();cid=now.strftime('%Y-%m-%dT%H%M%SZ')+'-codex-source-actions-'+uuid.uuid4().hex[:8];C=R/'captures'/cid;C.mkdir()
for n in ['c30_action.cpp','c30_certify.py','c30_oracles.py','c30_tests.py','c30_integration.py','c30_reproduce.py','c30_run_timed.py']:shutil.copyfile(P/n,C/n)
for src,dst in [('c30_THEOREM.md','THEOREM.md'),('c30_FREEZE.json','INITIAL_FREEZE.json'),('c30_BACKEND_FREEZE.json','BACKEND_FREEZE.json'),('c30_FINAL_ACTION_FREEZE.json','ACTION_FREEZE.json'),('c30_INTEGRATION_FREEZE.json','INITIAL_INTEGRATION_FREEZE.json'),('c30_BUILD_BINDING_FREEZE.json','BUILD_BINDING_FREEZE.json'),('c30_FINAL_FREEZE.json','FINAL_FREEZE.json'),('c30_BUILD_RECEIPT.json','BUILD_RECEIPT.json'),('c30_REPLAY_RECEIPT.json','REPLAY_RECEIPT.json'),('c30_forward_runtime.json','FORWARD_RUNTIME.json'),('c30_adjoint_runtime.json','ADJOINT_RUNTIME.json')]:shutil.copyfile(P/src,C/dst)
for n in ['ACTION_CONSTANTS.json','SOURCE_BINDINGS.json']:shutil.copyfile(P/'c30_math'/n,C/n)
shutil.copyfile(P/'c30_test_build/ACTION_TESTS.json',C/'ACTION_TESTS.json');shutil.copyfile(P/'c30_integration_final/INTEGRATION.json',C/'INTEGRATION.json')
(C/'OPERATOR.txt.gz').write_bytes(gzip.compress((P/'c30_math/OPERATOR.txt').read_bytes(),compresslevel=9,mtime=0));(C/'INTEGRATION_OUTPUT.txt.gz').write_bytes(gzip.compress((P/'c30_integration_final/OUTPUT.txt').read_bytes(),compresslevel=9,mtime=0))
(C/'construction').mkdir()
for n in ['c30_prepare.py','c30_action_boost_unbuilt.cpp','c30_oracles_initial.py','c30_integration_initial.py','c30_tests_initial.py']:shutil.copyfile(P/n,C/'construction'/n)
shutil.copyfile(P/'c30_integration_results/INTEGRATION.json',C/'construction/INITIAL_INTEGRATION.json')
(C/'review').mkdir()
for n in set(rr['capture_allowlist']+['FINAL_REVIEW.json','VERIFICATION_HASH_MANIFEST.sha256']):shutil.copyfile(review/n,C/'review'/n)
(C/'root').mkdir();shutil.copyfile(P/'c30_build.py',C/'root/build_capture.py');(C/'governance').mkdir()
for n in ['20-UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39-2-.md','21-UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md']:shutil.copyfile(P/'project_sources'/n,C/'governance'/n)
replay=J(C/'REPLAY_RECEIPT.json');replay['integration_output_replay']={'byte_identical':True,'sha256':H(P/'c30_integration_final/OUTPUT.txt'),'scope':'Initial and final source/build-bound integrations use unchanged numerical algorithm; provenance fields intentionally differ'};(C/'REPLAY_RECEIPT.json').write_text(json.dumps(replay,indent=2)+'\n')
(C/'CORRECTION_REGISTRY.json').write_text(json.dumps({'new_frozen_mathematical_retractions':0,'prior_results_changed':False,'prerelease_implementation_correction':{'found_by':'separate same-team reviewer','problem':'Initial adapter enforced operator hash but accepted an unbound executable path.','replacement':'Expected executable SHA required from trusted build receipt, verified before every call; actual final integration rerun, identical output; build/runtime trust explicitly remains a premise.'},'construction_changes':['Boost headers unavailable: initial build did not run; replaced with recorded platform-bound GMP ABI backend.','Reference term-coordinate evaluations are distinguished from compiled final output comparisons; no intermediate compiled trace claimed.','Elementary120u rounding bound replaces earlier looser520u construction bound.'],'session_wide_retraction_ratio':'NOT_COMPUTABLE','physical_promotion':0},indent=2)+'\n')
(C/'CLAIM_LEDGER.json').write_text(json.dumps({'lane':'Development — no registry entry','origin':'Pinned actual600-cell JSON source, new finite integer Taylor method, executed source actions and same-team independent audit','constructor':'Codex root','reviewer':'Separate same-team adversarial/source/arithmetic review, not external promotion authority','claims':[{'id':'ACT1','type':'DERIVED_NUMERICAL_METHOD_CERTIFICATE','statement':'Actual source-bound forward/adjoint reference algorithms have absolute error<2^-68 on state ball2048/data ball2049, respectively.','dependencies':['Exact source incidence/observer reconstruction','Boundary norm and chain identities','Degree40 Taylor tail and128bit division proof','Correct audited build and integer runtime']},{'id':'ACT2','type':'EXECUTED_REFERENCE','statement':'Three full4096 actual source-action cases pass consistency controls; timed forward/adjoint replays are byte-identical.','dependencies':['ACTION_TESTS.json','REPLAY_RECEIPT.json','RUNTIME receipts']},{'id':'ACT3','type':'EXECUTED_INTEGRATION','statement':'Actual2640-state two-step C29 decoder run passes5280 arithmetic checks with one forward/two adjoint actions.','dependencies':['INTEGRATION.json','BUILD_RECEIPT.json','Expected executable/sourceoperator hash enforcement'],'scope':'N=2 only; no8192 convergence/accuracy test'}],'open':['Full8192 decoder execution and performance','Different optimized/floating implementation','Physical/input error evidence and experimental correspondence'],'hidden_space':'641 nominal dimensions remain unrecovered','external_promotion_review':'PENDING','physical_promotion':0},indent=2)+'\n')
(C/'README.md').write_text('''# Actual source actions now implement the decoder oracle contracts

Development — no registry entry. External promotion review PENDING; Physical Promotion=0.

This capture supplies new finite forward and adjoint reference implementations for the unchanged weighted600-cell map F from PR307/PR313. The generator is reconstructed from pinned simplicial JSON, with the frozen ten top-cell weights3/2 and unchanged62-channel ordered readout. All14880 signed generator entries, chain annihilations and boundary norm caps24/15/15 are checked.

Degree40 Taylor halfsteps, exact GMP integer products/sums and128bit fixed-grid division deliver dyadic96 outputs. Exact rational inequalities prove absolute forward and adjoint errors<2^-68 on the required state ball2048 and data ball2049. The composed normal action therefore satisfies the2^-67 slot in PR313. This is a source-bound mathematical reference certificate under the recorded build/runtime arithmetic assumptions.

Three full4096 actual source-action cases execute at dimensions2640→253952 and253952→2640. Forward/adjoint replay outputs are byte-identical. Root controls independently evaluate211200 Python reference term coordinates and compare5280 compiled final halfstep coordinates; separate review supplies its own source/bound/backend checks. Actual full-size duality and scaling residuals satisfy the analytic budgets. Timed replay peaks were14600KiB and14216KiB, with walltimes about65s and57s in this environment. These are empirical standalone measurements, not worst-case or full-decoder benchmarks.

A source/build-bound two-step execution connects the actual actions to the unchanged PR313 decoder, checking5280 whole-update coordinates at full2640-state size. It passes and reproduces the earlier integration output exactly after the executable-binding correction. It is N=2, not a completed8192-step extraction. The641 nominal hidden components remain unrecovered. No physical/input premise, sixratio calibration or old Hankel gate is admitted.

## Source/build identity and scope

The adapter requires the pinned sourceoperator hash AND an expected executable SHA from a trusted build receipt; both are checked before each call. The integration receipt binds that build, executable and adapter. This corrects an initial implementation gap identified in separate review. Trust in the compiler, GMP arithmetic/runtime and build provenance remains explicit. The current backend uses minimal Linux64 GMP ABI declarations because development headers were unavailable; this is not a portable or formally verified compiler/library claim. Initial unbuilt Boost code and pre-correction source/results are preserved as construction history.

## Replay

```bash
python /absolute/capture/c30_reproduce.py --repo /absolute/UD --out /absolute/new-workspace --integration
```

Requires Python, a C++17 compiler, Linux64 libgmp.so.10 and python-flint for decoder integration. The replay builds the new source, reconstructs source data without running archived executables, generates exact input rules, runs the three full source-action cases and consistency controls, and optionally the actual two-step decoder integration. Allow several minutes. Compare scientific JSON and output hashes; empirical runtime/build-provenance fields may differ by machine. The trusted expected executable hash must come from the build being audited, not an arbitrary untrusted replacement.

OPERATOR.txt.gz and the final small integration output are retained. Full253952-coordinate action vectors are reproducibly generated and hash-bound rather than stored in the capture; their exact input rules and output hashes are in ACTION_TESTS.json. The source uses vector memory and no F,F^TF or full287-GiB Hankel matrix.

Next: improve the reference action throughput under the same error certificate, then execute the entire8192-step decoder.16383 forward/adjoint calls make full reference runtime a material limitation. Optimized code requires fresh conformance checks; no unexecuted performance benefit is claimed.

Ledger v0.39/CRL-2; O03 controls, Taylor degree and dyadic grids are not theory constants. Zero new frozen mathematical retractions; full-session ratio NOT_COMPUTABLE. External promotion review PENDING; Physical Promotion=0. Gap2_FINAL_Finite_Genesis.png unavailable/unused—please re-upload if needed. Notes/ASTER available unused. No public-site/Project-board deployment or outreach asserted. CI/merge/tracking separately reported.
''')
(C/'RUN_FOOTER.md').write_text('''A. Derived: Source-bound actual600-cell F/Fᵀ reference actions satisfy absolute error<2^-68 on domains2048/2049; composed normal error<=2^-67.

B. Executed: Three full4096 source-action cases, two byte-identical timed action replays, source/control replay, independent same-team source/backend audit and actual2640-state two-step decoder integration PASS. No full8192 run.

C. Limits: Platform/build/runtime arithmetic premises explicit; actual full8192 execution/performance, optimized/floating implementations and all physical/input evidence remain OPEN/HOLD.641 hidden dimensions unrecovered. No gate transfer.

D. Append-only capture/event/PR, CI/merge/tracking separately reported. Next: improve certified action throughput, then complete8192-step extraction.

Governance: Ledger0.39/CRL-2; Development—no registry entry; O03 controls not constants; external promotion review PENDING; Physical Promotion=0.0 new frozen mathematical retractions; sessionratio NOT_COMPUTABLE. PNG unavailable/unused—please re-upload if needed. Notes/ASTER unused.
''')
m={'capture_id':cid,'timestamp_utc':now.isoformat(),'base_commit':base,'status':'SOURCE_ACTION_CERTIFICATES_AND_FULLSIZE_TWO_STEP_INTEGRATION_PASS_FULL8192_OPEN','lane':'Development — no registry entry','physical_promotion':0,'external_review':'PENDING','supersedes':[],'extends':['2026-10-21T011432Z-codex-finite-decoder-cde7ea74'],'verification_scope':'Pinned source-bound forward/adjoint finite reference error proofs, actual fullsize source-action executions/replays and N2 decoder integration; fullN8192 and physical/input evidence remain OPEN/HOLD.','files':[]}
for f in sorted(C.rglob('*')):
 if f.is_file():m['files'].append({'path':str(f.relative_to(R)),'sha256':H(f),'size_bytes':f.stat().st_size,'provenance':'Pinned source JSON; new exact Taylor/fixed-grid source and checks; actual source-action execution; separate same-team review; supplied governance','status':'Development; full8192 OPEN; external promotion review PENDING'})
(C/'MANIFEST.json').write_text(json.dumps(m,indent=2)+'\n');(R/'events'/f'{cid}.json').write_text(json.dumps({'capture_id':cid,'timestamp_utc':now.isoformat(),'base_commit':base,'event_type':'SOURCE_BOUND_FORWARD_ADJOINT_ACTIONS_AND_TWO_STEP_INTEGRATION','manifest':str((C/'MANIFEST.json').relative_to(R)),'status':m['status'],'full8192_execution':False,'physical_promotion':0,'external_review':'PENDING'},indent=2)+'\n')
s={'capture_id':cid,'capture_path':str(C),'base':base,'branch':'codex/'+cid};(P/'c30_state.json').write_text(json.dumps(s,indent=2)+'\n');print(json.dumps(s,indent=2))
