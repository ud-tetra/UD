from pathlib import Path
import json,hashlib,datetime,uuid,subprocess,shutil,platform,importlib.metadata
P=Path('/workspace/scratch/f3d1c2f040c9');R=P/'ud-repo';J=lambda p:json.loads(p.read_text());H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();review=P/'c27_review'
rr=J(review/'FINAL_REVIEW.json');assert rr['status'].startswith('PASS');assert rr['root_checker_sha256']==H(P/'c27_verify.py')and rr['root_theorem_sha256']==H(P/'c27_THEOREM.md')
for line in(review/'VERIFICATION_HASH_MANIFEST.sha256').read_text().splitlines():
 h,n=line.split(None,1);assert H(review/n.strip())==h
now=datetime.datetime.now(datetime.timezone.utc);base=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip();cid=now.strftime('%Y-%m-%dT%H%M%SZ')+'-codex-weighted-conditioning-'+uuid.uuid4().hex[:8];C=R/'captures'/cid;C.mkdir()
for n in ['RESULT.json','SOURCE_BINDINGS.json','ARITHMETIC_DIAGNOSTICS.json','EIGENPROPOSAL.bin.gz','TIME_KERNELS.json.gz']:shutil.copyfile(P/'c27_cert_v2'/n,C/n)
for n in ['Q_DYADIC.bin.gz','PROPOSAL_FREEZE.json','VERIFIER_V1_FREEZE.json','VERIFIER_V2_FREEZE.json']:shutil.copyfile(P/'c27_work'/n,C/n)
shutil.copyfile(P/'c27_verify.py',C/'verify.py');shutil.copyfile(P/'c27_THEOREM.md',C/'THEOREM.md');shutil.copyfile(P/'c27_plan.json',C/'STRATEGY_FREEZE.json');(C/'construction').mkdir()
for x,y in [('c27_screen.py','top_screen.py'),('c27_full_screen.py','full_screen.py'),('c27_freeze_proposal.py','freeze_proposal.py'),('c27_verify_v1.py','verify_v1.py')]:shutil.copyfile(P/x,C/'construction'/y)
shutil.copyfile(P/'c27_work/FULL_SCREEN.json',C/'construction/NUMERICAL_SCREEN.json');(C/'review').mkdir()
for n in rr['capture_allowlist']:shutil.copyfile(review/n,C/'review'/n)
shutil.copyfile(review/'FINAL_REVIEW.json',C/'review/FINAL_REVIEW.json');(C/'root').mkdir();shutil.copyfile(P/'c27_build.py',C/'root/build_capture.py');(C/'governance').mkdir()
for n in ['20-UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39-2-.md','21-UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md']:shutil.copyfile(P/'project_sources'/n,C/'governance'/n)
rows=[]
for n in ['RESULT.json','SOURCE_BINDINGS.json','ARITHMETIC_DIAGNOSTICS.json','EIGENPROPOSAL.bin.gz','TIME_KERNELS.json.gz']:
 assert (P/'c27_cert_v2'/n).read_bytes()==(P/'c27_replay'/n).read_bytes();rows.append({'path':n,'sha256':H(C/n),'byte_identical':True})
(C/'REPLAY_RECEIPT.json').write_text(json.dumps({'status':'PASS_FROZEN_INTEGER_WITNESS_REPLAY','files':rows,'scientific_JSON_files':3,'binary_and_kernel_files':2,'replay_eigensolver_calls':0,'new_acquisitions_or_estimator_calls':0,'full_Hankel_allocations':0,'python':platform.python_version(),'dependency_versions':{n:importlib.metadata.version(n)for n in ['numpy','scipy','python-flint']},'scope':'All acceptance inequalities exact integers/Arb; proposer numerical eigensolver excluded from replay','physical_promotion':0},indent=2)+'\n')
(C/'CORRECTION_REGISTRY.json').write_text(json.dumps({'new_frozen_mathematical_retractions':0,'prior_results_changed':False,'prefinal_qualifications':['Numerical screen used globally reversed generator sign; final trial upper partners were negated, and exactE uses declared source sign. Global reversal preserves complete-grid singular spectrum, but is not identical source equality.','First validated source checked a newly proposed V,d without saving it. Version2 retains the exact integer eigenproposal, adds inheritedrank source bindings and robust integer bounds; no model/budget or arithmetic-result change.','Numerical estimate near180 is not the certified condition number; the certificate proves the more conservative exact bound27648/61<512.'],'session_wide_retraction_ratio':'NOT_COMPUTABLE; complete session denominator unavailable','physical_promotion':0},indent=2)+'\n')
(C/'CLAIM_LEDGER.json').write_text(json.dumps({'lane':'Development — no registry entry','origin':'PR305 fixed weighted model and source observer, new dyadic trial columns, exact integer residuals and validated finite time sums','constructor':'Codex root','reviewer':'Separate same-team independent reconstruction; not external promotion authority','claims':[{'id':'COND1','type':'VALIDATED_DERIVED_CONDITIONAL','statement':'Frozen normalized4096 half-step map on1999-dimensional observable quotient has sigma_min>61/27648 and kappa<27648/61<512.','dependencies':['PR305 exactrank1999/kernel641 pinned hashes','Q/E exact inequalities','full1999Gram midpoint/Arb errors','saved square eigenproposal exact residual','THEOREM.md']},{'id':'COND2','type':'EXACT_SCOPE_LIMIT','statement':'Full2640-domain condition remains infinite; declared-model certificate does not transfer physical calibration, noise, source or estimator gates.','dependencies':['inherited kernel641','typed fixed map/metric/sampling contract']}],'extended_scope_only':'PR305 practical-conditioning HOLD resolved for this mathematical sampled map; old coarse bound remains valid; unrelated gates unchanged','external_promotion_review':'PENDING','physical_promotion':0},indent=2)+'\n')
(C/'README.md').write_text('''# Fresh conditioning certificate for the frozen weighted observer

Development — no registry entry. DERIVED conditional mathematics. External promotion review PENDING; Physical Promotion=0.

The PR305 model and its rank remain fixed: epsilon=1/2 on the ten-tetrahedron C10 orbit, the same62-channel readout, unit Euclidean chain coordinates,4096 half-step samples normalized by1/64. This capture establishes a fresh bound for the complete1999-dimensional observable quotient:

    sigma_min,+ > 61/27648 > 1/512
    kappa_+ < 27648/61 < 512.

All cross-channel terms are included. The full2640-domain condition remains infinite because641 dimensions are hidden. The numerical screen near180 is a proposal diagnostic; it is not the certified condition number. Weighted sector-resolved ranks remain uncomputed.

The earlier coarse bound and rank certificate remain valid. This resolves the practical-conditioning HOLD for this particular mathematical observation map. It does not validate a physical weight law, actual acquisition, the distinct nominal Hankel/preparation family, the321-column floating estimator, calibration, detector noise or shape gates. Those provenance/measurement HOLDs remain.

## How the certificate works

The saved dyadic2640×1999 trial matrix and trial frequencies need not be exact eigenvectors or belong exactly to the observable subspace. The verifier checks Q orthogonality and E=KQ−QJ exactly. Orthogonal evolution bounds the trajectory approximation error by the RMS sample time times||E||.

The true trial-output Gram is enclosed using exact62-channel dot products and validated160-bit Arb finite time sums. Every one of its3,996,001 entries is retained; its midpoint has an operator error below2^-44. A saved square eigenproposal is accepted only after arbitrary-precision integer orthogonality and residual checks. Singular-product inequalities then yield the full observable-quotient bound. No hidden-subspace projector or full Hankel allocation is needed.

## Replay without an eigensolver

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python /absolute/UD/captures/CAPTURE_ID/verify.py --repo /absolute/UD --evidence /absolute/UD/captures/CAPTURE_ID --eigenproposal /absolute/UD/captures/CAPTURE_ID/EIGENPROPOSAL.bin.gz --out /absolute/new-output
```

Replace CAPTURE_ID with this directory. Dependencies: numpy, scipy, python-flint. The required inputs are the pinned source archive and PR305 result/theorem in the repository, plus the frozen dyadic Q/frequencies and saved integer eigenproposal in this capture. The optional proposer mode, with --eigenproposal omitted, uses an eigensolver only to generate a candidate that must pass the same exact tests. Source JSON is read as data; no archived script executes.

Three scientific JSON files and the saved eigenproposal/time-kernel bytes replay identically. The reconstructed1999×1999 Gram midpoint is output for inspection but is not stored redundantly in this capture; it is regenerated from the complete saved inputs. Historical construction/review scripts retain workspace paths and need relocation; the main verifier has explicit CLI paths. Certificate inputs occupy about21MiB compressed, rather than storing the287-GiB Hankel matrix. Peak runtime memory has not been benchmarked.

## Separate review and scope

Separate same-team review reconstructs the source signed model, exact Q/E residuals, every Gram entry and saved eigenproposal residual. It validates all57600 time-kernel integers using a different192-bit complex geometric-series expression, and checks adversarial controls against dropping rank, frame norms, square-frame invertibility or cross-channel terms. Final source/theorem/witness hashes are bound. This is not external promotion authority or a blinded acquisition.

The numerical search, trial-frequency grouping and dyadic rounding are disclosed. The weighted model was already fixed; all approximation errors are included in E. The initial screen's global sign reversal is documented, and the final exact residual uses the intended source sign. The version2 change saves the previously unretained eigenproposal for direct nonconstructor replay; the mathematical model and budgets are unchanged.

Next: use this fixed-map bound only with independently specified observation, preparation, timing and encoding errors; a physical source law and qualifying acquisition remain separate requirements. No new noise tolerance or physical accuracy claim follows merely from the condition number.

Ledger v0.39 / CRL-2. O03 choices are controls, not theory constants. Zero new frozen mathematical retractions; full-session ratio NOT_COMPUTABLE. External promotion review PENDING; Physical Promotion=0. Gap2_FINAL_Finite_Genesis.png unavailable and unused—please re-upload if needed. Notes/ASTER available but unused. CI/merge/tracking receipts are reported separately; no public-site deployment or outreach is asserted.
''')
(C/'RUN_FOOTER.md').write_text('''A. Derived: Fresh full observable-quotient bound sigma_min>61/27648, kappa<27648/61<512 for the unchanged PR3054096 half-step map. Rank1999/kernel641 inherited and pinned; full-domain condition infinite.

B. Checked: Exact Q/E and saved eigenproposal identities; full3,996,001-entry cross-channel Gram;57600 validated kernel integers; three JSON and two binary/kernel files replay byte-identically with zero replay eigensolver calls. Separate independent reconstruction/review and final hashes retained.

C. Limits: Numerical estimate near180 is not certified. Mathematical fixed-map conditioning HOLD resolved only here; physical calibration/noise/source and separate floating-estimator gates remain HOLD. No acquisition or physical weight law; weighted sector ranks not computed.

D. Append-only capture/event/uniquePR, CI/merge/tracking separately reported. Next: propagate independently supplied error budgets for this exact map. No public-site deployment or outreach.

Governance: Ledger0.39/CRL-2; Development—no registry entry; O03notconstants.0 new frozen mathematical retractions; sessionratio NOT_COMPUTABLE. External promotion review PENDING; Physical Promotion=0. PNG unavailable/unused—please re-upload if needed. Notes/ASTER available unused.
''')
m={'capture_id':cid,'timestamp_utc':now.isoformat(),'base_commit':base,'status':'VALIDATED_FRESH_FULL_OBSERVABLE_QUOTIENT_KAPPA_UNDER512','lane':'Development — no registry entry','physical_promotion':0,'external_review':'PENDING','supersedes':[],'extends':['2026-10-20T232207Z-codex-weighted-history-359f283e'],'verification_scope':'Fresh fixed-map conditioning via exact integer residuals and Arb full Gram, inheritedrank1999/kernel641; no physical/calibration/acquisition/estimator gate transfer','files':[]}
for f in sorted(C.rglob('*')):
 if f.is_file():m['files'].append({'path':str(f.relative_to(R)),'sha256':H(f),'size_bytes':f.stat().st_size,'provenance':'Pinned weighted model; declared numerical trial proposals checked by exact integer and validated Arb arithmetic; separate same-team review; supplied governance','status':'Development—no registry entry; external promotion review PENDING'})
(C/'MANIFEST.json').write_text(json.dumps(m,indent=2)+'\n');(R/'events'/f'{cid}.json').write_text(json.dumps({'capture_id':cid,'timestamp_utc':now.isoformat(),'base_commit':base,'event_type':'VALIDATED_WEIGHTED_FULL_QUOTIENT_CONDITIONING','manifest':str((C/'MANIFEST.json').relative_to(R)),'inherited_rank':1999,'inherited_kernel':641,'positive_condition_upper':'27648/61<512','physical_promotion':0,'external_review':'PENDING'},indent=2)+'\n')
s={'capture_id':cid,'capture_path':str(C),'base':base,'branch':'codex/'+cid};(P/'c27_state.json').write_text(json.dumps(s,indent=2)+'\n');print(json.dumps(s,indent=2))
