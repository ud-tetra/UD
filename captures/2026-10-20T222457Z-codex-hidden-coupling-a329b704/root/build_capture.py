from pathlib import Path
import json,hashlib,datetime,uuid,subprocess,shutil,platform
P=Path('/workspace/scratch/f3d1c2f040c9');R=P/'ud-repo';J=lambda p:json.loads(p.read_text());H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
now=datetime.datetime.now(datetime.timezone.utc);base=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip();cid=now.strftime('%Y-%m-%dT%H%M%SZ')+'-codex-hidden-coupling-'+uuid.uuid4().hex[:8];C=R/'captures'/cid;C.mkdir()
review=P/'c24_review';rr=J(review/'REVIEW.json');assert rr['status'].startswith('PASS')
for line in (review/'VERIFICATION_HASH_MANIFEST.sha256').read_text().splitlines():
 h,n=line.split(None,1);assert H(review/n.strip())==h
final=J(review/'FINAL_SOURCE_BINDING.json');assert final['status'].startswith('PASS')
for f in (P/'c24_math').iterdir():shutil.copyfile(f,C/f.name)
shutil.copyfile(P/'c24_compute.py',C/'compute.py')
(C/'review').mkdir()
for n in rr['capture_allowlist']+['VERIFICATION_HASH_MANIFEST.sha256','FINAL_SOURCE_BINDING.json']:shutil.copyfile(review/n,C/'review'/n)
(C/'root').mkdir();shutil.copyfile(P/'c24_build.py',C/'root/build_capture.py')
(C/'governance').mkdir()
for n in ['20-UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39-2-.md','21-UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md']:shutil.copyfile(P/'project_sources'/n,C/'governance'/n)
replay=[]
for n in ['RESULT.json','HARMONIC_WITNESS.json','SOURCE_BINDINGS.json']:
 assert (P/'c24_math'/n).read_bytes()==(P/'c24_replay'/n).read_bytes();replay.append({'file':n,'sha256':H(C/n),'byte_identical':True})
(C/'REPLAY_RECEIPT.json').write_text(json.dumps({'status':'PASS_EXACT_THREE_FILE_REPLAY','files':replay,'python':platform.python_version(),'dependencies':'Python standard library only','new_SVD_or_estimator_calls':0,'scope':'New source harmonic/action/polynomial/moment checks; inherited native rank not rerun','physical_promotion':0},indent=2)+'\n')
(C/'CORRECTION_REGISTRY.json').write_text(json.dumps({'new_frozen_mathematical_retractions':0,'prior_nominal_results_modified':False,'pre_publication_clarifications':['Distinguished S_c (mean sine squared) from B=S_c/10 (output energy); no1-B numerator claim','Odd chain-parity anticommutation does not preserve even/odd state subspaces separately','Explicit sampled-nullspace/nonaliasing proof is required for positive singular-value upper bound'],'operational_note':'Initial invocation stopped at missing sympy import before arithmetic; final checker uses own standard-library rational Sturm implementation. Added explicit CLI/out guard and monic assertion after first arithmetic review; unchanged3scientific JSON files replay byte-identically. Final source/theorem separately bound in review/FINAL_SOURCE_BINDING.json. No estimator retry/fit occurred.','session_wide_retraction_ratio':'NOT_COMPUTABLE; complete session denominator unavailable','physical_promotion':0},indent=2)+'\n')
(C/'CLAIM_LEDGER.json').write_text(json.dumps({'lane':'Development — no registry entry','origin':'Declared nominal unit-metric observer plus explicit general-skew perturbation; source-bound harmonic/character checks and rational arithmetic','constructor':'Codex root','reviewer':'Separate same-team mathematical reviewer; not external promotion authority','claims':[{'id':'HC1','type':'DERIVED_CONDITIONAL','statement':'Any skew change supported entirely on nominalN leaves every output history unchanged; unrestricted hidden-skew family dimension278631.','dependencies':['THEOREM.md sections1-2','inherited nominal invariantN']},{'id':'HC2','type':'DERIVED_CONDITIONAL','statement':'Hidden initial state transfer at most sin(min(epsilon|t|,pi/2)) under skew evolution with offdiagonal norm<=epsilon; readout error adds eta.','dependencies':['THEOREM.md section2']},{'id':'HC3','type':'DERIVED_EXACT_MODEL_VARIANT','statement':'Declared harmonic coupling raises historyrank1893to1894, reduceskernel747to746, changesonlym0rank255to256; no native coupling law claimed.','dependencies':['inherited nominal/sector ranks','HARMONIC_WITNESS.json','SOURCE_BINDINGS.json','THEOREM.md section3']},{'id':'HC4','type':'DERIVED_FINITE_SAMPLE','statement':'NonaliasedM>=106 half-step samples have kernel746. M4096 centeredharmonicplane gives exact positive-singular/condition bounds, not fullstate/Hankel/estimator guarantee.','dependencies':['THEOREM.md section4','RESULT.json','review/EXACT_RESULTS.json','review/ROOT_COMPARISON.json']}],'external_review':'PENDING','physical_promotion':0},indent=2)+'\n')
(C/'README.md').write_text('''# Hidden-mode coupling: exact rank activation can be ill-conditioned

Development — no registry entry. DERIVED conditional finite-model results; external promotion review PENDING; Physical Promotion=0.

The nominal62-channel 600-cell observer still has its certified747-dimensional dynamical kernel. This addendum explicitly changes the mathematical generator and asks which forms of change can reveal a hidden mode. It neither replaces nominal A nor supplies physical acquisition evidence.

## New return

- Hidden-only skew changes leave all nominal output histories exactly unchanged, even if their operator norm is large. Their unrestricted real skew parameter space has dimension278631.
- For a skew actual generator with hidden-to-visible coupling norm at mostε, a hidden unit state transfers at most sin(min(ε|t|,π/2)) into the visible space. A readout operator errorη adds at mostη to the output bound. Internal hidden/visible frequencies need no norm ceiling for this result.
- A concrete coupling between the visible uniform-vertex harmonic and the hidden fundamental3-cycle raises history rank1893→1894 and lowers the kernel747→746 for every ε=2^-k, k≥20. It preserves norm, declaredC10 symmetry and odd chain-parity anticommutation; its direct0↔3 coupling is outside the native adjacent-degree/local Hodge–Dirac class.
- Only isolated characterm=0 changes, rank255→256. The additional mixed-sector hidden quotient remains630. Source ranks are inherited, not newly recalculated.

THEOREM.md contains proofs, exact domains, the106-sample nonaliasing argument and a reproducible harmonic witness. New exact checks reconstruct boundary cancellations, closed fundamental-cycle orientation, link indices, signedC10 action and its10th power. A rational Sturm calculation bounds the52nonzero squared-frequency roots in(0,16). No archived scripts were run.

## Finite-window conditioning

For normalized62-channel state observations at M=4096 half-step times, exact centered moments and directed rational square-root bounds give:

|Coupling ε|Upper bound on smallest positive singular value|Lower bound on positive-spectrum condition number κ+|
|---|---:|---:|
|2^-20|<1.7830e-4|>1773.61|
|2^-30|<1.7412e-7|>1.8161e6|
|2^-40|<1.7004e-10|>1.8597e9|

Exact rank can increase while stable recovery of that extra mode becomes arbitrarily poor. κ+ is restricted to the observable subspace; the full2640column condition number is infinite because746directions remain hidden. These bounds concern a state-observation map. They do not certify or modify the37-preparation Hankel condition, the321column floating-estimator sketch, κ<2029, the six-ratio gate or any acquisition tolerance. Plane singular lower bounds are not full-map lower bounds.

## Reproduction and audit

From any directory, with a complete repository and a NEW output directory outside it:

```bash
python /absolute/UD/captures/CAPTURE_ID/compute.py --repo /absolute/UD --out /absolute/new-harmonic-check
```

Replace CAPTURE_ID by this directory name. The script uses only Python's standard library and reads3JSON members from the immutable pinned observer archive. It reconstructs the new structural checks and3JSON outputs, reproduced byte-identically in a separate invocation. Source archive/member hashes are in SOURCE_BINDINGS.json. The old1893/747/isolatedsector ranks and observer annihilator identity remain explicit inherited proof premises, not a full native-observer replay. No dense perturbation, SVD or fullHankel is needed.

Separate same-team review independently checks the harmonic cycle/action, rebuilds q from its low-degree factors, certifies root counts, directly sums centered moments and verifies37root-result comparisons including directed160-bit square-root endpoints. Its original source/comparison receipts remain, and a separate final binding checks the finished source/theorem after CLI/monic assertion refinements. Review scripts retain historical workspace layout and need relocation for replay; compute.py has explicit path arguments. Review is not an external nonconstructor/custodian promotion ruling.

No raw acquisition, new physical preparation, estimator fit or calibration evidence was supplied. Previous numerical tools, gates, nominal rank results and HOLD/NO-GO findings are unchanged. The next substantive boundary is a justified native perturbation class or independently measured cross-coupling/readout bounds; the declared nonlocal harmonic example is not that source law. The ready PR296 numerical handoff still requires source-bound inputs, as documented in PR298. No public-site/Project-board deployment or outreach occurred.

Ledger v0.39 / CRL-2; O03 protocol controls are not theory constants. Prepublication notation/parity refinements and the initial dependency import failure are disclosed in CORRECTION_REGISTRY.json.0new frozen mathematical retractions; session-wide ratio NOT_COMPUTABLE. External promotion review PENDING; Physical Promotion=0. Gap2_FINAL_Finite_Genesis.png unavailable/unused—re-upload if needed. Notes/ASTER availableunused. Publication/CI/merge/tracking is reported separately.
''')
(C/'RUN_FOOTER.md').write_text('''A. Derived: coupling-only sine transfer ceiling;278631hidden-skew freedoms; declared harmonic couplingrank1894/kernel746, m0rank256; normalizedM4096positiveconditionlower>1.8597e9forε2^-40.

B. Checked: exact sourceharmonics/signedaction/polynomialrootband/centeredmoments;3scientificJSONbyteidenticalreplay;37separatereviewercomparisons and finalsource/theorembinding. Oldrankpremisesinherited, notrerun.

C. Limits: general-skew nonlocal0↔3variant, notnativeconstitutivelaw;κ+notfullstate/Hankel/estimatorcondition.746hidden remain. No fresh acquisition, fit or calibration; allpriorHOLD/gates unchanged.

D. Append-onlycapture/event/uniquePR; CI/merge/tracking reportedseparately. No public-site/Project-boarddeployment.

Governance: Ledger0.39/CRL-2; Development—noregistryentry; O03notconstants.0frozenmathretractions; sessionratioNOT_COMPUTABLE. ExternalpromotionreviewPENDING;PhysicalPromotion=0. PNGunavailableunused—re-uploadifneeded;Notes/ASTERavailableunused.
''')
m={'capture_id':cid,'timestamp_utc':now.isoformat(),'base_commit':base,'status':'EXACT_CONDITIONAL_HIDDEN_COUPLING_THEOREM','lane':'Development — no registry entry','physical_promotion':0,'external_review':'PENDING','supersedes':[],'verification_scope':'New conditional hidden-coupling proofs and exact harmonic/polynomial/moment checks; prior native ranks inherited; no new fit/acquisition/physicalsource','files':[]}
for f in sorted(C.rglob('*')):
 if f.is_file():m['files'].append({'path':str(f.relative_to(R)),'sha256':H(f),'size_bytes':f.stat().st_size,'provenance':'Declared skew mathematical variant and newly checked integer/rational identities; inherited nominal source ranks; separate same-team review; supplied governance','status':'Development—no registry entry; external review PENDING'})
(C/'MANIFEST.json').write_text(json.dumps(m,indent=2)+'\n');(R/'events'/f'{cid}.json').write_text(json.dumps({'capture_id':cid,'timestamp_utc':now.isoformat(),'base_commit':base,'event_type':'HIDDEN_COUPLING_RANK_AND_CONDITION_THEOREM','manifest':str((C/'MANIFEST.json').relative_to(R)),'nominal_rank_unchanged':1893,'declared_variant_rank':1894,'declared_variant_hidden':746,'physical_promotion':0,'external_review':'PENDING'},indent=2)+'\n')
s={'capture_id':cid,'capture_path':str(C),'base':base,'branch':'codex/'+cid};(P/'c24_state.json').write_text(json.dumps(s,indent=2)+'\n');print(json.dumps(s,indent=2))
