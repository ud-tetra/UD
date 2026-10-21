from pathlib import Path
import json,hashlib,datetime,uuid,subprocess,shutil
P=Path('/workspace/scratch/f3d1c2f040c9');R=P/'ud-repo';H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();J=lambda p:json.loads(p.read_text())
review=P/'c32_review';rr=J(review/'FINAL_REVIEW.json');assert rr['status']=='PASS'
for n,h in rr['source_hashes'].items():assert H(P/n)==h
for line in(review/'VERIFICATION_HASH_MANIFEST.sha256').read_text().splitlines():
 h,n=line.split(None,1);assert H(review/n.strip())==h
assert J(P/'c32_math_final/RESULT.json')['full_frame_construction_status']=='NOT_RUN_HOLD'
assert J(P/'c32_solve_final/PARTIAL_SOLVE.json')['status'].startswith('PASS')
now=datetime.datetime.now(datetime.timezone.utc);base=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip();cid=now.strftime('%Y-%m-%dT%H%M%SZ')+'-codex-reusable-compression-'+uuid.uuid4().hex[:8];C=R/'captures'/cid;C.mkdir()
def copy(src,dst):
 d=C/dst;d.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,d)
for n in ['c32_certify.py','c32_construct.py','c32_partial_solve.py','c32_reproduce.py']:copy(P/n,n)
copy(P/'c32_THEOREM.md','THEOREM.md')
for n in ['RESULT.json','CONTROLS.json','SOURCE_BINDINGS.json','TRIAL_SLICE.json']:copy(P/'c32_math_final'/n,n)
copy(R/'captures/2026-10-21T013801Z-codex-source-actions-9c7b87b9/OPERATOR.txt.gz','OPERATOR.txt.gz')
for n in ['CONSTRUCTION_FREEZE','SOURCE_AUTH_FREEZE','FINAL_FREEZE','REPLAY_RECEIPT']:copy(P/f'c32_{n}.json',f'{n}.json')
copy(P/'c31_BUILD_RECEIPT.json','BUILD_RECEIPT.json');copy(P/'c32_workflow_replay/BUILD_RECEIPT.json','fresh_workflow/BUILD_RECEIPT.json')
for f in (P/'c32_partial_final').iterdir():copy(f,'frame/'+f.name)
for f in (P/'c32_solve_final').iterdir():copy(f,'solve/'+f.name)
for n in rr['capture_allowlist']:copy(review/n,'review/'+n)
for n in ['20-UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39-2-.md','21-UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md']:copy(P/'project_sources'/n,'governance/'+n)
copy(P/'c32_build.py','root/build_capture.py')
def write(n,o):
 (C/n).write_text(json.dumps(o,indent=2)+'\n')
write('CORRECTION_REGISTRY.json',{'new_frozen_mathematical_retractions':0,'prior_results_changed':False,'development_refinements':['Trusted expected slice hash added before authenticated construction replay; all17 frame files byte-identical.','Encoded RHS error included separately; partial16 projection explicitly distinguished from full1999 projection.'],'session_wide_retraction_ratio':'NOT_COMPUTABLE','physical_promotion':0})
write('CLAIM_LEDGER.json',{'lane':'Development — no registry entry','claims':[{'id':'CMP1','type':'DERIVED_CONDITIONAL_THEOREM','statement':'C=Y^T F is a minimal1999-dimensional real linear nominal observable reconstruction statistic, kerC=kerF (641), B0F=P_V, gain<454.','dependencies':['Pinned PR307 real model/rank/conditioning/trial bounds']},{'id':'CMP2','type':'CONDITIONAL_FINITE_ALGORITHM_PROFILE','statement':'If all1999 rows G satisfy constructed per-row bounds, full projection defect<2^-55 and gain<455; certified per-record RHS/normal/lift residual gates give implementation error<2^-43.','status':'FULL1999_CONSTRUCTION_AND_SOLVE_NOT_RUN_HOLD'},{'id':'CMP3','type':'EXECUTED_PARTIAL_CONSTRUCTION','statement':'16 source-bound rows,122880 logical phase checks, exact16x16 Gram solve with16 positive pivots/residual0 and2640-coordinate finite lift verified; fresh rebuilt workflow and byte replays PASS.'},{'id':'CMP4','type':'NO_GO','statement':'Any rank<=16 decoder has full rank1999 projection operator defect>=1; partial prototype cannot certify complete reconstruction.'}],'review':'Separate same-team non-constructor proof/input/Gram/lift/replay audit; not external promotion authority; native adjoint outputs not independently reexecuted by reviewer','open':['Remaining1983 rows','Full1999 solve and per-record residuals','Physical/input evidence','Complete extraction/performance'],'external_promotion_review':'PENDING','physical_promotion':0})
(C/'README.md').write_text('''# Reusable observation compression: theorem and actual16-row prototype

Development — no registry entry. External promotion review PENDING; Physical Promotion=0.

For the pinned real253952-by2640 weighted observation map F, C=Y^T F has1999 independent rows and exactly the same641-dimensional kernel. The decoder B0=C^+Y^T satisfies B0F=P_V and has gain<454. This is minimal dimension among real linear statistics that reconstruct the nominal observable quotient. It is a post-acquisition feature dimension, not a claim of fewer physical readings or statistical sufficiency.

The full approximate-frame construction profile yields projection defect<2^-55 and gain<455, conditional on all1999 source-bound rows being constructed and validated. A separate per-record RHS, normal-equation and lift residual protocol bounds implementation error<2^-43. With additional supplied X<=1,D<2^-50 premises this would imply observable-state error<2^-40. Full-frame construction, full solve and physical/input premises remain NOT_RUN/UNSUPPLIED_HOLD.

## What actually ran

Sixteen distributed rows were built with the certified C31 native adjoint, Arb192 phase encoding and dyadic96 delivery.122880 logical phase checks passed. The exact16-by16 Gram solve has16 positive elimination pivots and zero normal-equation residual. All2640 coordinates of the finite lift passed the rounding-error check. The authenticated replay reproduced17 frame files and2 solve files exactly. A fresh end-to-end workspace rebuilt the pinned native source and repeated construction, solve and17-file internal replay; numerical row/lift bytes match. Fresh build/parent-receipt metadata differs as documented.

Separate same-team review independently rebuilt4063232 encoded input coordinates at Arb256, checked65536 unique phase enclosures, all256 exact Gram entries,16 pivots and2640 lift coordinates, and audited the proof and exact fixtures. The reviewer checked saved native outputs and their bindings; it did not independently execute the adjoints. Source/build/compiler/GMP/Arb and inherited model bounds remain explicit assumptions.

The16-row decoder approximates only its own16-dimensional subprojection. Its error against the complete rank1999 state projection is at least1. The remaining1983 observable directions and nominal641 hidden dimensions are not reconstructed. These rows are not identified with character sectors or eigenmodes.

## Reproduce

```bash
python /absolute/capture/c32_reproduce.py --repo /absolute/UD --out /absolute/new-workspace --replay
```

Requires Python with python-flint, C++17 signed128 support and Linux64 GMP. This explicit construction builds pinned C31 source and performs actual16 adjoints. Archive ingestion alone does not execute scripts. The root executed this fresh workflow successfully. Compare numerical bytes and exact bounds; fresh trusted build provenance may differ.

Prospective storage consists of a1999-by2640 frame and1999-by1999 Gram matrix with streamed RHS generation; neither full Y nor the287-GiB Hankel is needed. This turn stores only16 row witnesses and their solve. It does not benchmark the full matrix pipeline or transfer earlier six-ratio/Hankel gates. The general projected-F residual is<3/64, not1/8192 and not a2^-68 action replacement.

Ledger0.39/CRL-2; O03 tolerances/precisions/sample choices are controls, not theory constants.0 new frozen mathematical retractions; session ratio NOT_COMPUTABLE. Gap2_FINAL_Finite_Genesis.png unavailable/unused—please re-upload if needed. Notes/ASTER unused. No public-site/Project-board deployment or outreach asserted. CI/merge/tracking separately reported.
''')
(C/'RUN_FOOTER.md').write_text('''A. Derived: minimal1999-coordinate real linear observation statistic, same nominal641 kernel; exact decoder gain<454. Conditional full approximate-frame defect<2^-55/gain<455 and finite residual protocol error<2^-43.

B. Executed:16 source-bound rows,122880 logical phase checks, exact rank16 Gram solve/residual0,2640-coordinate finite lift, authenticated replay and fresh rebuilt workflow PASS. Separate same-team review PASS with explicit native-runtime assumptions.

C. Captured: append-only evidence, proof, sources,16 row witnesses, exact solve, replay and independent review. CI/merge/tracking separately reported. No full1999 or physical accuracy claim.

D. Next: construct remaining1983 rows and certify full1999 solve. Fullframe/solve and physical inputs HOLD; partial16 error against full projection>=1. Nominal641 hidden dimensions unrecovered.

Governance: Ledger0.39/CRL-2; Development—no registry entry; external promotion review PENDING; Physical Promotion=0; O03 controls not constants.0 new frozen mathematical retractions; sessionratio NOT_COMPUTABLE. PNG unavailable/unused—please re-upload if needed. Notes/ASTER unused.
''')
m={'capture_id':cid,'timestamp_utc':now.isoformat(),'base_commit':base,'status':'COMPRESSION_THEOREM_AND_PARTIAL16_EXECUTION_PASS_FULL1999_HOLD','physical_promotion':0,'lane':'Development — no registry entry','external_promotion_review':'PENDING','extends':['2026-10-21T015546Z-codex-native-actions-6a0c79b1','2026-10-20T234200Z-codex-weighted-conditioning-d6af1d67'],'supersedes':[],'verification_scope':'Conditional full compression proof and actual16-row construction/exact solve/replay; full1999 construction/solve and physical premises HOLD','files':[]}
for f in sorted(C.rglob('*')):
 if f.is_file():m['files'].append({'path':str(f.relative_to(R)),'sha256':H(f),'size_bytes':f.stat().st_size,'provenance':'Pinned real model/source; new proof and actual partial execution; same-team review; supplied governance','status':'Development; full1999/physical HOLD'})
write('MANIFEST.json',m)
(R/'events'/f'{cid}.json').write_text(json.dumps({'capture_id':cid,'timestamp_utc':now.isoformat(),'base_commit':base,'event_type':'REUSABLE_COMPRESSION_THEOREM_AND_PARTIAL16_FRAME','manifest':str((C/'MANIFEST.json').relative_to(R)),'status':m['status'],'actual_rows':16,'full_frame_rows_required':1999,'full_frame_status':'NOT_RUN_HOLD','physical_promotion':0},indent=2)+'\n')
s={'capture_id':cid,'capture_path':str(C),'base':base,'branch':'codex/'+cid};(P/'c32_state.json').write_text(json.dumps(s,indent=2)+'\n');print(json.dumps(s))
