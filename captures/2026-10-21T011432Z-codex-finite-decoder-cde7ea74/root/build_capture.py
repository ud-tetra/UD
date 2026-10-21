from pathlib import Path
import json,hashlib,datetime,uuid,subprocess,shutil,platform
P=Path('/workspace/scratch/f3d1c2f040c9');R=P/'ud-repo';H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();J=lambda p:json.loads(p.read_text());review=P/'c29_review';rr=J(review/'FINAL_REVIEW.json')
assert rr['status'].startswith('PASS')
for key,n in [('root_checker_sha256','c29_certify.py'),('root_decoder_sha256','c29_decoder.py'),('root_reference_sha256','c29_reference_tests.py'),('root_theorem_sha256','c29_THEOREM.md')]:assert rr[key]==H(P/n)
for line in(review/'VERIFICATION_HASH_MANIFEST.sha256').read_text().splitlines():
 h,n=line.split(None,1);assert H(review/n.strip())==h
now=datetime.datetime.now(datetime.timezone.utc);base=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip();cid=now.strftime('%Y-%m-%dT%H%M%SZ')+'-codex-finite-decoder-'+uuid.uuid4().hex[:8];C=R/'captures'/cid;C.mkdir()
for n in ['RESULT.json','POLYNOMIAL_WITNESS.json','SOURCE_BINDINGS.json']:shutil.copyfile(P/'c29_math'/n,C/n)
for n in ['REFERENCE_RESULTS.json','SMALL_OPERATOR.json']:shutil.copyfile(P/'c29_ref_final'/n,C/n)
for src,dst in [('c29_decoder.py','decoder.py'),('c29_certify.py','certify.py'),('c29_reference_tests.py','reference_tests.py'),('c29_THEOREM.md','THEOREM.md'),('c29_plan.json','STRATEGY_FREEZE.json'),('c29_FREEZE.json','INITIAL_FREEZE.json'),('c29_INTERFACE_FREEZE.json','INTERFACE_FREEZE.json')]:shutil.copyfile(P/src,C/dst)
(C/'construction').mkdir()
for src,dst in [('c29_decoder_initial.py','decoder_initial.py'),('c29_reference_initial.py','reference_initial.py')]:shutil.copyfile(P/src,C/'construction'/dst)
(C/'review').mkdir()
for n in set(rr['capture_allowlist']+['FINAL_REVIEW.json','VERIFICATION_HASH_MANIFEST.sha256']):shutil.copyfile(review/n,C/'review'/n)
(C/'root').mkdir();shutil.copyfile(P/'c29_build.py',C/'root/build_capture.py');(C/'governance').mkdir()
for n in ['20-UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39-2-.md','21-UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md']:shutil.copyfile(P/'project_sources'/n,C/'governance'/n)
rows=[]
for a,b,names in [('c29_math','c29_math_replay',['RESULT.json','POLYNOMIAL_WITNESS.json','SOURCE_BINDINGS.json']),('c29_ref_final','c29_ref_replay',['REFERENCE_RESULTS.json','SMALL_OPERATOR.json'])]:
 for n in names:
  assert(P/a/n).read_bytes()==(P/b/n).read_bytes();rows.append({'path':n,'sha256':H(C/n),'byte_identical':True})
(C/'REPLAY_RECEIPT.json').write_text(json.dumps({'status':'PASS_FIVE_SCIENTIFIC_FILES_BYTE_IDENTICAL','files':rows,'python':platform.python_version(),'reference_dependencies':'python-flint Arb192, exact Fraction audits, dyadic96 states','actual_600cell_action_calls':0,'actual_600cell_decoder_run':False,'physical_promotion':0},indent=2)+'\n')
(C/'CORRECTION_REGISTRY.json').write_text(json.dumps({'new_frozen_mathematical_retractions':0,'prior_results_changed':False,'construction_refinements':['The full data wrapper was added after the first from-adjoint proxy run; initial source bytes retained against initial freeze hashes.','Generic data-ball2 proxy validation is distinct from illustrative state-X<=1 profile.','Three iterate vectors plus fixed g and action results, not three total vectors.','h(0) is nonzero; hidden action and arithmetic errors require full-space Green bound.'],'session_wide_retraction_ratio':'NOT_COMPUTABLE','physical_promotion':0},indent=2)+'\n')
(C/'CLAIM_LEDGER.json').write_text(json.dumps({'lane':'Development — no registry entry','origin':'Pinned PR307/PR309 model certificates plus new exact Chebyshev construction','claims':[{'id':'DEC1','type':'DERIVED_CONDITIONAL','statement':'N8192 polynomial B=h(F^TF)F^T has full-state projection defect<2^-51 and gain<512.','dependencies':['PR307 spectral interval','exact integer power witness','THEOREM sections2-3']},{'id':'DEC2','type':'DERIVED_CONDITIONAL','statement':'Full-space Green gain<256 controls hidden and visible additive errors; specified absolute action and aggregate arithmetic budgets imply implementation error<11*2^-46<2^-42.','dependencies':['THEOREM sections4-6','oracle truths UNSUPPLIED_HOLD for actual600cell']},{'id':'DEC3','type':'EXECUTED_PROXY_REFERENCE','statement':'Three full8192-step rotated rational controls, exact action audits and per-coordinate Arb update checks pass; separate implementation reproduces outputs.','dependencies':['REFERENCE_RESULTS.json','review receipts'],'scope':'Small rational proxies, not600cell execution'},{'id':'DEC4','type':'CONDITIONAL_PROFILE','statement':'Prior declared X<=1 and D<2^-50 plus new certified action/update obligations imply observable-chain error<2^-40.','scope':'Actual input evidence and actual600cell actions HOLD'}],'hidden_space':'641 nominal components not reconstructed','no_gate_transfer':['sixratio calibration','old Hankel native family','actual floating estimator','physical acquisition'],'external_promotion_review':'PENDING','physical_promotion':0},indent=2)+'\n')
(C/'README.md').write_text('''# Finite matrix-free decoding with verified projection and error bounds

Development — no registry entry. External promotion review PENDING; Physical Promotion=0.

For the unchanged PR307 weighted4096 half-step observation map F, the inherited singular interval is [61/27648,1], with rank1999/kernel641. This capture constructs B=h(F^T F)F^T using a finite8192-degree Chebyshev residual polynomial. It proves the whole-state bound ||BF−P||<2^-51 and ||B||<512, where P is the nominal orthogonal observable projection. The earlier arbitrary-frame inverse counterexample remains valid; this construction uses the exact adjoint range instead.

The recurrence requires one adjoint and8191 normal actions, or16383 forward/adjoint calls when normal actions are composed. It stores vectors and coefficient enclosures rather than F, F^TF, P or a full Hankel matrix. Actual600-cell runtime has not been benchmarked.

The full-space error proof includes hidden-direction arithmetic and action errors. Under the declared absolute action contracts and whole-update error budget2^-67, the implementation error is below11*2^-46<2^-42. Sufficient factored forward/adjoint errors are2^-68 absolute on state ball2048 and data ball2049 respectively. These are explicit obligations, not certified facts about an actual600-cell implementation.

## Executed checks

The standard-library checker verifies30 exact scalar identities, zero-mode limits, constants and the8192-degree integer-power inequality. The executable reference uses Arb192 coefficient balls, exact dyadic96 vectors and certified whole-coordinate rounding. Three full8192-step rational four-state proxy cases pass, including a rotated hidden subspace, inconsistent data and coherent hidden oracle errors. Independent exact action audits and adversarial rejection controls pass. Separate same-team review independently reproduces all three outputs with an algebraically regrouped recurrence. Five scientific JSON files replay byte-identically.

The generic weak-mode proxy has state amplitude about453; it validates the declared data-ball2 domain. It is distinct from the earlier illustrative X<=1 profile. Substituting that profile's D<2^-50 and the new obligations implies observable-chain error<2^-40. All physical/input premises and actual600-cell action contracts remain UNSUPPLIED/HOLD. The641 hidden components are not recovered.

## Replay

```bash
python /absolute/capture/certify.py --repo /absolute/UD --out /absolute/new-math-output
python /absolute/capture/reference_tests.py --decoder /absolute/capture/decoder.py --out /absolute/new-reference-output
```

The first command uses the Python standard library and reads pinned parent JSON/theorem bytes as data. The second explicitly runs the new reference module and requires python-flint. Neither command runs the actual600-cell decoder or executes archived acquisition scripts. Reference output binds decoder bytes, so use the captured decoder unchanged.

Next: implement and certify true weighted600-cell F/F^T actions on the required domains, then run this decoder on the frozen full problem. An opaque callback or successful small proxy cannot establish that certificate. No physical experiment, fresh preparation, calibration gate, public-site deployment or Project-board update is asserted here.

Ledger v0.39/CRL-2; O03 controls are not theory constants. Zero new frozen mathematical retractions; full-session ratio NOT_COMPUTABLE. Gap2_FINAL_Finite_Genesis.png unavailable and unused—please re-upload if needed. Notes/ASTER available unused. CI/merge/tracking receipts reported separately.
''')
(C/'RUN_FOOTER.md').write_text('''A. Derived: N8192 finite matrix-free decoder; full-state projection defect<2^-51, gain<512. Full-space Green gain<256; conditional implementation error<2^-42.

B. Checked:30 exact root controls, five byte-identical scientific replays, three full8192-step proxy runs with exact action audits, Arb arithmetic checks and separate same-team output reproduction. No actual600-cell decoder execution.

C. Open: Actual600-cell F/F^T actions and their domain-wide absolute error certificates, full runtime and physical/input evidence remain HOLD.641 hidden components unrecovered. No sixratio/Hankel/physical gate transfer.

D. Append-only capture/event/PR; CI/merge/tracking separately reported. Next: certify actual weighted600-cell action oracles, then full decoder execution.

Governance: Ledger0.39/CRL-2; Development—no registry entry; external promotion review PENDING; Physical Promotion=0.0 new frozen mathematical retractions; sessionratio NOT_COMPUTABLE. PNG unavailable/unused—please re-upload if needed. Notes/ASTER available unused.
''')
m={'capture_id':cid,'timestamp_utc':now.isoformat(),'base_commit':base,'status':'FINITE_DECODER_THEOREM_AND_PROXY_ARITHMETIC_PASS_ACTUAL600_ACTIONS_HOLD','lane':'Development — no registry entry','physical_promotion':0,'external_review':'PENDING','supersedes':[],'extends':['2026-10-20T235659Z-codex-error-propagation-550c9eb1','2026-10-20T234200Z-codex-weighted-conditioning-d6af1d67'],'verification_scope':'Finite nominal polynomial decoder and full-space conditional arithmetic bounds; three full small-proxy reference runs and independent review. Parent conditioning inherited; actual600-cell actions/execution and physical inputs HOLD.','files':[]}
for f in sorted(C.rglob('*')):
 if f.is_file():m['files'].append({'path':str(f.relative_to(R)),'sha256':H(f),'size_bytes':f.stat().st_size,'provenance':'Pinned parent certificates; new exact Chebyshev proofs; newly executed proxy reference and separate same-team review; supplied governance','status':'Development; actual600-cell admission HOLD; external promotion review PENDING'})
(C/'MANIFEST.json').write_text(json.dumps(m,indent=2)+'\n')
(R/'events'/f'{cid}.json').write_text(json.dumps({'capture_id':cid,'timestamp_utc':now.isoformat(),'base_commit':base,'event_type':'FINITE_MATRIX_FREE_DECODER_PROJECTION_AND_ARITHMETIC','manifest':str((C/'MANIFEST.json').relative_to(R)),'status':m['status'],'actual_600cell_execution':'NOT_RUN_HOLD','physical_promotion':0,'external_review':'PENDING'},indent=2)+'\n')
s={'capture_id':cid,'capture_path':str(C),'base':base,'branch':'codex/'+cid};(P/'c29_state.json').write_text(json.dumps(s,indent=2)+'\n');print(json.dumps(s,indent=2))
