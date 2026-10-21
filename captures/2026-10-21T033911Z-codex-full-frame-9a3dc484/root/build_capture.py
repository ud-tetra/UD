from pathlib import Path
import json,hashlib,datetime,uuid,subprocess,shutil,zipfile
P=Path('/workspace/scratch/f3d1c2f040c9');R=P/'ud-repo';H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();J=lambda p:json.loads(p.read_text());rr=J(P/'c33_review/FINAL_REVIEW.json');assert rr['status'].startswith('PASS')
for n,h in rr['source_hashes'].items():assert H(P/n)==h
assert H(P/'c33_THEOREM.md')==rr['root_theorem_sha256']
for n,h in J(P/'c33_FINAL_FREEZE.json')['files'].items():assert H(P/n)==h
for line in(P/'c33_review/VERIFICATION_HASH_MANIFEST.sha256').read_text().splitlines():
 h,n=line.split(None,1);assert H(P/'c33_review'/n.strip())==h
cert=J(P/'c33_cert_final/FULL_CERTIFICATE.json');assert cert['status']=='PASS_FULL1999_CONSTRUCTION_AND_ONE_ACTUAL_FLOAT_RECORD_CERTIFIED';assert J(P/'c33_full_frame/FULL_FRAME.json')['actual_rows_constructed_or_authenticated']==1999;assert J(P/'c33_row_replay/ROW_REPLAY.json')['actual_new_adjoint_replays']==8;assert J(P/'c33_FRESH_RECEIPT.json')['status'].startswith('PASS')
assert J(P/'c33_gap_row_replay/ROW_REPLAY.json')['actual_new_adjoint_replays']==10
now=datetime.datetime.now(datetime.timezone.utc);base=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip();cid=now.strftime('%Y-%m-%dT%H%M%SZ')+'-codex-full-frame-'+uuid.uuid4().hex[:8];C=R/'captures'/cid;C.mkdir()
def copy(src,dst):
 d=C/dst;d.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,d)
def write(n,o):(C/n).write_text(json.dumps(o,indent=2)+'\n')
for n in ['prepare','construct','preflight','solve','certify','pack','unpack','replay_rows','reproduce','run_solve']:copy(P/f'c33_{n}.py',f'c33_{n}.py')
copy(P/'c33_gap_replay_rows.py','c33_gap_replay_rows.py');copy(P/'c33_THEOREM_pre_gap.md','construction/c33_THEOREM_pre_gap.md')
copy(P/'c33_THEOREM.md','THEOREM.md');copy(P/'c33_source/SOURCE_PLAN.json','SOURCE_PLAN.json');copy(P/'c33_full_frame/FULL_FRAME.json','FULL_FRAME.json');copy(P/'c33_cert_final/FULL_CERTIFICATE.json','FULL_CERTIFICATE.json');copy(P/'c33_PREFLIGHT.json','PREFLIGHT.json')
for f in (P/'c33_parts').iterdir():copy(f,'frame-parts/'+f.name)
for f in (P/'c33_first_solve/record').iterdir():copy(f,'solve/'+f.name)
for f in (P/'c33_fresh_verification/solve').iterdir():copy(f,'fresh-verification/solve/'+f.name)
copy(P/'c33_fresh_verification/certificate/FULL_CERTIFICATE.json','fresh-verification/FULL_CERTIFICATE.json')
for n in ['PROCESS_RECEIPT.json','STDOUT.log','STDERR.log']:copy(P/'c33_first_solve'/n,'solve-process/'+n)
for src,dst in [('c33_row_replay/ROW_REPLAY.json','ROW_REPLAY.json'),('c33_FRESH_RECEIPT.json','FRESH_RECEIPT.json'),('c31_BUILD_RECEIPT.json','BUILD_RECEIPT.json')]:copy(P/src,dst)
for src,dst in [('c33_gap_row_replay/ROW_REPLAY.json','GAP_ROW_REPLAY.json'),('c33_PROGRESS_GAP_FREEZE.json','PROGRESS_GAP_FREEZE.json'),('c33_PROGRESS_JOURNAL.jsonl.gz','PROGRESS_JOURNAL.jsonl.gz'),('c33_CONSTRUCTION_RUNTIME.json','CONSTRUCTION_RUNTIME.json')]:copy(P/src,dst)
for n in ['INITIAL_FREEZE','SOLVE_AUTH_FREEZE','CERTIFICATE_FREEZE','TOOLING_FREEZE','SOLVE_INPUT_FREEZE','FINAL_FREEZE']:copy(P/f'c33_{n}.json',f'{n}.json')
for n in ['c33_solve_initial.py','c33_certify_initial.py','c33_certify_v2.py','c33_pack_initial.py','c33_unpack_initial.py']:copy(P/n,'construction/'+n)
for n in rr['capture_allowlist']:copy(P/'c33_review'/n,'review/'+n)
er=P/'c33_estimator_review';assert J(er/'REVIEW_RECEIPT.json')['status'].startswith('PASS');assert J(er/'REVIEW_RECEIPT.json')['solver_sha256']==H(P/'c33_solve.py')
def verify_review(d,expected):
 assert H(d/'FINAL_MANIFEST.json')==expected
 inv=J(d/'FINAL_MANIFEST.json');assert all(H(d/n)==h for n,h in inv.items());assert{f.relative_to(d).as_posix()for f in d.rglob('*')if f.is_file()and f.name!='FINAL_MANIFEST.json'}==set(inv)
verify_review(er,'258d4e29a4d53a6ff5b1f8de21f9a961ce8c86d6f48140114570c7a624a156b2')
for n in ['README.md','REVIEW_RECEIPT.json','FINAL_MANIFEST.json','FREEZE.json','PLAN.json','test_solver.py']:copy(er/n,'synthetic-review/'+n)
(C/'synthetic-review/FULL_SYNTHETIC_PACKAGE.zip').parent.mkdir(parents=True,exist_ok=True)
with zipfile.ZipFile(C/'synthetic-review/FULL_SYNTHETIC_PACKAGE.zip','w',compression=zipfile.ZIP_DEFLATED,compresslevel=9)as z:
 for f in sorted(er.rglob('*')):
  if f.is_file():assert not f.is_symlink();info=zipfile.ZipInfo(f.relative_to(er).as_posix(),date_time=(1980,1,1,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;z.writestr(info,f.read_bytes(),compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
copy(P/'c33_build.py','root/build_capture.py')
sr=P/'c33_storage_review';assert J(sr/'REVIEW_RECEIPT.json')['status'].startswith('PASS')
verify_review(sr,'558410899fa43f5f3e407a7159cc7b7dd744c4d8fd4bf47abe14696a01ad67f0')
for n in ['README.md','REVIEW_RECEIPT.json','FINAL_MANIFEST.json','FREEZE.json']:copy(sr/n,'storage-review/'+n)
with zipfile.ZipFile(C/'storage-review/FULL_STORAGE_PACKAGE.zip','w',compression=zipfile.ZIP_DEFLATED,compresslevel=9)as z:
 for f in sorted(sr.rglob('*')):
  if f.is_file():assert not f.is_symlink();info=zipfile.ZipInfo(f.relative_to(sr).as_posix(),date_time=(1980,1,1,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;z.writestr(info,f.read_bytes(),compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
for n in ['20-UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39-2-.md','21-UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md']:copy(P/'project_sources'/n,'governance/'+n)
write('CORRECTION_REGISTRY.json',{'new_frozen_mathematical_retractions':0,'prior_mathematical_results_changed':False,'development_refinements':[{'found_by':'Separate same-team review','change':'Trusted expected full-frame hash required before any floating solve; source arithmetic/gates unchanged; initial source preserved.'},{'found_by':'Construction syntax precheck','change':'Missing whitespace in initial certifier was caught by py_compile before execution; initial bytes preserved; no computed claim.'},{'found_by':'Construction transport planning','change':'Witness part size reduced200 to64 rows before packing; all original compressed row bytes preserved.'},{'found_by':'Separate same-team proof review','change':'Added exact nominal decoder comparison<2^-44; no physical state-truth assumption introduced.'}],'execution_evidence_qualification':{'found_by':'Separate same-team review; root confirmed','finding':'Progress journal has1989 of1999 rows; ten entries absent; cause UNDETERMINED.','remedy':'Journal preserved; all1989 retained entries match finalmetadata; ten additionalnative replays match allaffected rowdata. Complete final1999payloads and fresh restoration independentlychecked.','scope':'Does not reconstructoriginalchronology or explainfailurecause; no missingfinalpayload or mathematicalboundretraction'},'session_wide_retraction_ratio':'NOT_COMPUTABLE','physical_promotion':0})
write('CLAIM_LEDGER.json',{'lane':'Development — no registry entry','claims':[{'id':'FULL1','type':'EXECUTED_FULL_FRAME_CONSTRUCTION','statement':'All1999 source-bound rows admitted:1983 new native adjoints and16 authenticated prior rows;974848 unique phase scalar checks,16367616 logical bindings.','dependencies':['Pinned Q/operator/C32 theorem/C31 action contract','Frozen constructor and trusted runtime','All saved row hashes and domain checks']},{'id':'FULL2','type':'DERIVED_EXECUTION_ADMISSION','statement':'Actual full frame has rank1999, projection defect<2^-55 and ideal compressed decoder gain<455 under inherited source/runtime premises.','dependencies':['FULL1','C32 full-frame perturbation proof']},{'id':'FULL3','type':'EXECUTED_ONE_SYNTHETIC_RECORD','statement':'Actual float64 proposal admitted by exact residual<2^-64 and finite lift checks; implementation error<2^-46 relative to BGy; error<2^-44 relative to exact nominal B0y.','dependencies':['FULL2','Exact synthetic datum norm<2','Saved coefficient and lift witnesses','FULL_CERTIFICATE.json'],'scope':'One record, not a universal floating convergence or physical accuracy result'},{'id':'FULL4','type':'EXECUTED_REPRODUCIBILITY_AND_SAME_TEAM_AUDIT','statement':'Eight planned plus ten progress-gap new row actions replayed exactly; fresh packed-data restoration/solve/verification passed; independent source/phase/RHS and Python-integer residual/lift audit passed.','scope':'Reviewer did not independently rerun1983 native actions; fresh workflow is restoration/solve, not a second full construction'}],'open':['Fresh nominal known-state preparations and data-specific RHS','Physical/input correspondence','Spectral extraction and old Hankel/sixratio gates'],'external_promotion_review':'PENDING','physical_promotion':0,'nominal_hidden_dimensions_unrecovered':641})
(C/'README.md').write_text('''# Full observation frame and an actual certified floating record

Development — no registry entry. External promotion review PENDING. Physical Promotion=0.

All1999 rows of the C32 reusable observation frame are now constructed and admitted:1983 new C31 native adjoint calls plus16 authenticated earlier rows. The constructor regenerated all source-bound inputs and exact RHS dots;119 shared phase tables used974848 unique scalar enclosure checks and16367616 logical row bindings. A source/phase/output contract and trusted runtime remain premises. This does not independently attest the compiler or hardware.

The full-frame theorem now applies to the actual saved frame: rank1999, operator defect<2^-55 relative to the nominal observable-state projector, and ideal compressed decoder gain<455. The641 nominal hidden dimensions remain unrecovered. These are real weighted-model results, not finite-field character or physical identifications.

An actual full-size float64 Gram/Cholesky proposal was executed on one frozen253952-scalar synthetic datum. Every accepted coefficient is saved as an exact dyadic160 integer. Exact two-matvec normal residual checks and the finite2640-coordinate lift prove implementation error<2^-46 relative to BGy and error<2^-44 relative to the exact nominal decoder B0y. Ordinary floating residuals did not decide admission. This is one-record arithmetic validation, not a guarantee that all floating solves converge or that the datum is a measured/source state. X<=1,D<2^-50 remains a conditional truth profile; physical/input evidence is UNSUPPLIED_HOLD.

Separate same-team review reconstructed the full source coefficients, all phase tables, enclosed every true RHS and independently recomputed the saved record residual/lift with Python integers. It did not independently rerun1983 native adjoints. Eight selected new native actions were reexecuted by the producer and matched original bytes. Review found the original progress journal has1989 of1999 entries; the cause is UNDETERMINED. The journal is preserved without repair. All retained entries match finalmetadata; ten additionalnative replays match the affected row inputs, metadata and outputbytes. Complete final1999row witnesses are present and audited. The replays establish those values, not the missing original chronology or its cause. A fresh workflow restored every packed witness, reran the full solve and verified its certificate. This is a fresh restoration/solve replay, not a second full native construction.

## Data and replay

The32 parts in frame-parts retain all1999 original compressed row witnesses verbatim. FULL_FRAME.json retains every input/output/phase/RHS binding. The saved frame has1999×2640 signed128 coordinates; the floating Gram is1999×1999. The program does not allocate Y, F, F^TF or the287-GiB Hankel matrix. No unmeasured process peak or complete spectral-pipeline timing is claimed.

```bash
python /absolute/capture/c33_reproduce.py --repo /absolute/UD --capture /absolute/capture --out /absolute/new-workspace
```

Trust the capture manifest/Git commit before using its expected hashes. Unpacking proves integrity and coverage; source admission also depends on the finite constructor execution and inherited mathematical/runtime contracts. The fresh workflow above recomputes source data, restores rows, proposes coefficients and verifies exact residuals. NumPy/SciPy, python-flint and a compatible Python are required. Different numerical backends may yield different valid finite coefficients; compare certificates and exact gates rather than assuming byte identity.

To repeat the entire expensive construction, add --construct instead of --capture. This explicitly compiles pinned C31 C++17 source and requires the rebuilt binary to match the inherited approved executable hash before use; a changed build requires its own admission. Correct Linux64 GMP/compiler/Arb execution and stable intended files remain assumptions. Archived source is never executed merely for ingestion.

The separate synthetic solver package contains a source-excluded1999×2640 diagonal fixture, an actual refinement, four rejecting CLI controls and two exact oracle mutation controls. Its successful residual test is not UD source admission. Frozen plans, receipts and exact oracle errors are retained separately from actual-frame evidence.

Next: fresh nominal known-state preparations and data-specific RHS validation, then any separately specified spectral extraction. Old six-ratio/Hankel thresholds and physical gates are not transferred.

Ledger0.39/CRL-2. O03 tolerances, grids, sample counts, concurrency and iteration budgets are controls, not theory constants.0 new frozen mathematical retractions; session ratio NOT_COMPUTABLE. Gap2_FINAL_Finite_Genesis.png and Notes Backup17-04-2026 unavailable/unused—please re-upload if needed. ASTER unused. No public-site/Project-board deployment or outreach asserted. CI/merge/tracking separately reported.
''')
(C/'RUN_FOOTER.md').write_text('''A. Constructed: Full1999-row source frame:1983 new native actions plus16 authenticated reused rows; inherited full-frame defect<2^-55/gain<455 now applies to the saved data.

B. Executed/checked: One actual full float proposal, exact residual<2^-64 and finite lift; implementation error<2^-46, exact nominal decoder record error<2^-44. Separate same-team audit, eight planned plus ten progress-gap native row replays and fresh packed restoration/solve PASS. The original1989-entry progress journal is preserved; ten missing entries remain unexplained, with allfinal1999row witnesses verified. Synthetic-only CLI controls are separately labeled.

C. Captured: Full row witnesses in32 bounded parts, source, proof, coefficients, lift, process/replay/review receipts and governance. CI/merge/tracking separately reported; no physical or spectral gate transferred.

D. Next: fresh nominal known-state preparation records and RHS validation. Unknown physical truth/input correspondence remains HOLD;641 nominal hidden dimensions unrecovered. No universal floating convergence claim.

Governance: Ledger0.39/CRL-2; Development—no registry entry; external promotion review PENDING; Physical Promotion=0; O03 controls not theory constants.0 new frozen mathematical retractions; session ratio NOT_COMPUTABLE. PNG and Notes Backup attachments unavailable/unused—please re-upload if needed. ASTER unused. No public-site/Project-board deployment or outreach asserted.
''')
m={'capture_id':cid,'timestamp_utc':now.isoformat(),'base_commit':base,'status':'FULL1999_FRAME_AND_ONE_ACTUAL_FLOAT_RECORD_CERTIFIED','physical_promotion':0,'lane':'Development — no registry entry','external_promotion_review':'PENDING','extends':['2026-10-21T022602Z-codex-reusable-compression-8fd46991'],'supersedes':[],'verification_scope':'Actual fullframe construction, one frozen synthetic record with exact residual/lift and nominal decoder reference bounds, selected native replays and fresh packed restoration/solve; physical/input truth and spectral extraction HOLD','files':[]}
for f in sorted(C.rglob('*')):
 if f.is_file():m['files'].append({'path':str(f.relative_to(R)),'sha256':H(f),'size_bytes':f.stat().st_size,'provenance':'Pinned source/theorem; actual full-frame construction and one finite solve; same-team independent audits; supplied governance','status':'Development; physical/input truth and spectral extraction HOLD'})
write('MANIFEST.json',m);(R/'events'/f'{cid}.json').write_text(json.dumps({'capture_id':cid,'timestamp_utc':now.isoformat(),'base_commit':base,'event_type':'FULL1999_SOURCE_FRAME_AND_ACTUAL_FLOAT_RECORD_CERTIFICATE','manifest':str((C/'MANIFEST.json').relative_to(R)),'status':m['status'],'full_frame_rows':1999,'new_native_rows':1983,'reused_rows':16,'actual_synthetic_records':1,'physical_promotion':0},indent=2)+'\n');s={'capture_id':cid,'capture_path':str(C),'base':base,'branch':'codex/'+cid};(P/'c33_state.json').write_text(json.dumps(s,indent=2)+'\n');print(json.dumps(s))
