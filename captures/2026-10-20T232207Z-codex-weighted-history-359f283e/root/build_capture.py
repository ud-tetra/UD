from pathlib import Path
import json,hashlib,datetime,uuid,subprocess,shutil,platform,importlib.metadata
P=Path('/workspace/scratch/f3d1c2f040c9');R=P/'ud-repo';J=lambda p:json.loads(p.read_text());H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();review=P/'c26_review'
rr=J(review/'FINAL_REVIEW.json');assert rr['status'].startswith('PASS')
assert rr['root_checker_sha256']==H(P/'c26_compute.py')and rr['root_theorem_sha256']==H(P/'c26_THEOREM.md')
now=datetime.datetime.now(datetime.timezone.utc);base=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip();cid=now.strftime('%Y-%m-%dT%H%M%SZ')+'-codex-weighted-history-'+uuid.uuid4().hex[:8];C=R/'captures'/cid;C.mkdir()
for n in ['RESULT.json','FACTOR_RESULTS.json','SOURCE_BINDINGS.json']:shutil.copyfile(P/'c26_math_v2'/n,C/n)
shutil.copyfile(P/'c26_compute.py',C/'compute.py');shutil.copyfile(P/'c26_THEOREM.md',C/'THEOREM.md')
for n in ['LOWER_WITNESSES.json','UPPER_WITNESSES.zip','FACTOR_CERTIFICATE.json']:shutil.copyfile(P/'c26_work'/n,C/n)
shutil.copyfile(P/'c26_plan.json',C/'MODEL_FREEZE.json');(C/'construction').mkdir()
for a,b in [('c26_screen.py','screen.py'),('c26_upper.py','upper.py'),('c26_package_witnesses.py','package_witnesses.py')]:shutil.copyfile(P/a,C/'construction'/b)
(C/'review').mkdir()
for n in rr['capture_allowlist']:shutil.copyfile(review/n,C/'review'/n)
shutil.copyfile(review/'FINAL_REVIEW.json',C/'review/FINAL_REVIEW.json');(C/'governance').mkdir()
for n in ['20-UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39-2-.md','21-UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md']:shutil.copyfile(P/'project_sources'/n,C/'governance'/n)
(C/'root').mkdir();shutil.copyfile(P/'c26_build.py',C/'root/build_capture.py');rows=[]
for n in ['RESULT.json','FACTOR_RESULTS.json','SOURCE_BINDINGS.json']:
 assert (P/'c26_math_v2'/n).read_bytes()==(P/'c26_replay'/n).read_bytes();rows.append({'path':n,'sha256':H(C/n),'byte_identical':True})
(C/'REPLAY_RECEIPT.json').write_text(json.dumps({'status':'PASS_THREE_SCIENTIFIC_FILES_BYTE_IDENTICAL','files':rows,'python':platform.python_version(),'dependency_versions':{n:importlib.metadata.version(n)for n in ['numpy','scipy','python-flint']},'dependencies':'numpy/scipy/python-flint; arbitrary-precision integer identities and modular determinants','new_fits_or_estimator_calls':0,'full_Hankel_allocations':0,'physical_promotion':0},indent=2)+'\n')
(C/'CORRECTION_REGISTRY.json').write_text(json.dumps({'new_frozen_mathematical_retractions':0,'prior_results_changed':False,'prefinal_execution_qualifications':['Compact witness first checker stopped on positive-denominator assertion: FLINT common denominator can be signed. Constructor normalizes row signs; final exact identities and replay use positive per-row denominators.','Review first denominator predicate similarly stopped; preserved reviewer version/failure receipts distinguish this from mathematical rank change.','Formal conditioning bound is finite but too weak for useful2029/calibration/noise certification.'],'session_wide_retraction_ratio':'NOT_COMPUTABLE; complete session denominator unavailable','physical_promotion':0},indent=2)+'\n')
(C/'CLAIM_LEDGER.json').write_text(json.dumps({'lane':'Development — no registry entry','model':'epsilon1/2 C10-orbit whole-column weights; fixed unit-coordinate observer/preparations','claims':[{'id':'WR1','type':'EXACT_CONDITIONAL','statement':'Top cyclic ranks390 nominal /443 weighted, augmented invariant space444.','evidence':['UPPER_WITNESSES.zip exact rational memberships','LOWER_WITNESSES.json nonzero prime1009 minors','compute.py']},{'id':'WR2','type':'DERIVED_CONDITIONAL','statement':'Full history rank1999/kernel641, netgain106; old/new kernelintersection640 and oldkernel restricted observationrank107.','dependencies':['WR1','inherited nominal1893 and PR303 downward-closed channel separation','THEOREM.md']},{'id':'WS1','type':'DERIVED_CONDITIONAL','statement':'Frozen4096 half-step normalized sample map has rank1999/kernel641 without constructing full Hankel.','dependencies':['source normbound24','nonaliasing and finite Vandermonde','WR2']},{'id':'WC1','type':'DERIVED_WORST_CASE_ANALYTIC','statement':'On641kernel orthogonal quotient, sigma_min>2^-10394665 and kappa<2^10394665; full-domain condition infinite. Practical2029 gate NOT_CERTIFIED/HOLD.','dependencies':['integer observable minimal polynomial and discriminant','integer jet Gram pseudodeterminant','THEOREM.md section5']}],'uncomputed':['weighted sector ranks','practically useful whole-quotient conditioning','new floating estimator accuracy','physical weight law/acquisition'],'external_review':'PENDING','physical_promotion':0},indent=2)+'\n')
(C/'README.md').write_text('''# A frozen local weighted model gains106 observable dimensions

Development—no registry entry. Exact/derived conditional mathematics; external promotion review PENDING; Physical Promotion=0.

For the PR303 ten-tetrahedron C10 orbit, freeze epsilon=1/2 and keep the same62-channel vertex-link observer, unit Euclidean chain coordinates and declared preparations. Only the top boundary columns are rescaled. This is a mathematical model selection, not an inferred physical law.

|Quantity|Nominal|Frozen weighted model|
|---|---:|---:|
|Top cyclic observation rank|390|443|
|Full history rank|1893 inherited|1999 derived|
|Full dynamical kernel|747 inherited|641 derived|
|Kernel intersection|640 shared|640 shared|

The new observer sees107 independent directions of the old kernel, while a replacement stationary direction becomes hidden. Thus the netgain106 does not mean the two hidden spaces are nested. Weighted sector-resolved ranks are NOT_COMPUTED.

The fixed normalized4096 half-step sample map also has rank1999/kernel641. Exact source norm bounds exclude aliasing; finite Vandermonde separation proves the sample-kernel equality. No dense full-history/Hankel array, eigensolver, SVD or floating estimator is run.

A full-observable-quotient analytic enclosure is finite but extremely conservative: sigma_min,+>2^-10394665 and kappa_+<2^10394665. The full2640-domain condition is infinite. This does not certify the nominal2029 condition bound or any practical calibration/noise/shape gate. Practical conditioning remains HOLD. Tighter whole-quotient Gram enclosures are the next mathematical task; cross-channel Gram terms must be retained.

## Certificate and replay

Nonzero prime1009 minors certify top-rank lower bounds390/443 and augmented lower444. An exact degree53 annihilator,30 coprime polynomial factors and60 rational row-membership witnesses prove nominal/augmented upper bounds390/444. The weighted invariant space contains an explicit invisible harmonic line, giving upper443. Lower/upper match without treating deficient modular ranks as rational upper proofs. The compact primitive-row archive contains the complete upper witnesses, not an approximate low-rank residual.

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python /absolute/UD/captures/CAPTURE_ID/compute.py --repo /absolute/UD --evidence /absolute/UD/captures/CAPTURE_ID --out /absolute/new-output
```

Replace CAPTURE_ID with this directory name. Dependencies: numpy, scipy, python-flint. The checker reads3pinned JSON members and the newly constructed witness records; no archived executable runs. RESULT.json, FACTOR_RESULTS.json and SOURCE_BINDINGS.json replay byte-identically. Source/member SHA256 and scientific claims are separately typed. The full1893 nominal rank and channel decomposition are inherited, while this run verifies the new top-channel delta, sample proof constants and exact witnesses. Construction/review scripts retain their historical workspace paths and require relocation; the main checker has explicit CLI arguments.

Separate same-team review reconstructs signed dual adjacency independently, matches all30factor dimensions, checks all60saved membership identities and3nonzero minors, the shared-kernel argument and analytic conditioning constants. Review receipts identify prefinal predicate stops and final source/theorem bindings. This is not external promotion authority. Exact constructor/witness replay is distinguished from separate review.

No raw acquisition, fresh timing record, physical preparation, fitted generator, measurement noise floor or physical weight source is introduced. No source/calibration/321-column estimator/native2029/residual gate transfers. Previous nominal results and provenance HOLDs remain unchanged. No public-site deployment or outreach is asserted.

Full A/B/C/D footer and correction registry are included. Ledger0.39/CRL-2; O03 choices are controls, not theory constants. External promotion review PENDING; Physical Promotion=0. Gap2_FINAL_Finite_Genesis.png unavailable/unused—please re-upload if needed; Notes/ASTER available unused. CI/merge/tracking receipts are reported separately.
''')
(C/'RUN_FOOTER.md').write_text('''A. Derived: Frozen epsilon1/2 C10-orbit model has fullrank1999/kernel641, netgain106; commonkernel640, oldkernel restrictionrank107.4096 half-step sample rank1999. Formal quotient condition<2^10394665.

B. Checked:3nonzero prime1009 minors;30factor exact decomposition/435coprimalities;60rational membership identities; source graph/norm facts;3byteidentical scientific JSON files; separate same-team review/final source binding. Nominal1893/105 and channel separation inherited.

C. Limits: Practical2029 conditioning and calibration/noise gates HOLD. Weighted sector ranks NOT_COMPUTED. No raw acquisition, fit, floating estimator or physical weight law. Full-domain condition infinite; hidden spaces not nested.

D. Append-only capture/event/uniquePR; CI/merge/tracking reported separately. No public-site deployment/outreach.

Governance: Ledger0.39/CRL-2; Development—no registry entry; O03notconstants.0new frozen mathematical retractions; sessionratio NOT_COMPUTABLE. External promotion review PENDING; Physical Promotion=0. PNG unavailable unused—please re-upload if needed; Notes/ASTER available unused.
''')
m={'capture_id':cid,'timestamp_utc':now.isoformat(),'base_commit':base,'status':'EXACT_WEIGHTED_RANK_AND_DERIVED_FINITE_SAMPLE_BOUND_PRACTICAL_CONDITIONING_HOLD','lane':'Development — no registry entry','physical_promotion':0,'external_review':'PENDING','supersedes':[],'extends':['2026-10-20T225243Z-codex-adjacent-weights-010c2d8b'],'verification_scope':'New weighted top-channel rational rank certificates and inherited full-rank delta; finite sampling and coarse full-quotient analytic bound; no physical/admission/estimator transfer','files':[]}
for f in sorted(C.rglob('*')):
 if f.is_file():m['files'].append({'path':str(f.relative_to(R)),'sha256':H(f),'size_bytes':f.stat().st_size,'provenance':'Declared weighted model; pinned JSON sources; new exact arithmetic certificates; separate same-team review; supplied governance','status':'Development—no registry entry; external promotion review PENDING'})
(C/'MANIFEST.json').write_text(json.dumps(m,indent=2)+'\n');(R/'events'/f'{cid}.json').write_text(json.dumps({'capture_id':cid,'timestamp_utc':now.isoformat(),'base_commit':base,'event_type':'WEIGHTED_HISTORY_RANK_AND_FINITE_SAMPLE_ANALYTIC_BOUND','manifest':str((C/'MANIFEST.json').relative_to(R)),'weighted_history_rank':1999,'weighted_kernel':641,'practical_conditioning':'HOLD_NOT_CERTIFIED','physical_promotion':0,'external_review':'PENDING'},indent=2)+'\n')
s={'capture_id':cid,'capture_path':str(C),'base':base,'branch':'codex/'+cid};(P/'c26_state.json').write_text(json.dumps(s,indent=2)+'\n');print(json.dumps(s,indent=2))
