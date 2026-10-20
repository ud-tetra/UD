from pathlib import Path
import json,hashlib,datetime,uuid,subprocess,shutil,platform
P=Path('/workspace/scratch/f3d1c2f040c9');R=P/'ud-repo';J=lambda p:json.loads(p.read_text());H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();review=P/'c28_review';rr=J(review/'FINAL_REVIEW.json');assert rr['status'].startswith('PASS');assert rr['root_checker_sha256']==H(P/'c28_compute.py')and rr['root_theorem_sha256']==H(P/'c28_THEOREM.md')
for line in(review/'VERIFICATION_HASH_MANIFEST.sha256').read_text().splitlines():
 h,n=line.split(None,1);assert H(review/n.strip())==h
now=datetime.datetime.now(datetime.timezone.utc);base=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip();cid=now.strftime('%Y-%m-%dT%H%M%SZ')+'-codex-error-propagation-'+uuid.uuid4().hex[:8];C=R/'captures'/cid;C.mkdir()
for n in ['RESULT.json','SOURCE_BINDINGS.json','CONDITIONAL_ERROR_CONTRACT.json','CONTROLS.json']:shutil.copyfile(P/'c28_math_v2'/n,C/n)
shutil.copyfile(P/'c28_compute.py',C/'compute.py');shutil.copyfile(P/'c28_THEOREM.md',C/'THEOREM.md');shutil.copyfile(P/'c28_plan.json',C/'STRATEGY_FREEZE.json');shutil.copyfile(P/'c28_FREEZE.json',C/'INITIAL_FREEZE.json');shutil.copyfile(P/'c28_FINAL_FREEZE.json',C/'FINAL_SCOPE_FREEZE.json');(C/'construction').mkdir();shutil.copyfile(P/'c28_compute_initial.py',C/'construction/compute_initial.py');(C/'review').mkdir()
for n in rr['capture_allowlist']:shutil.copyfile(review/n,C/'review'/n)
shutil.copyfile(review/'FINAL_REVIEW.json',C/'review/FINAL_REVIEW.json');(C/'root').mkdir();shutil.copyfile(P/'c28_build.py',C/'root/build_capture.py');(C/'governance').mkdir()
for n in ['20-UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39-2-.md','21-UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md']:shutil.copyfile(P/'project_sources'/n,C/'governance'/n)
rows=[]
for n in ['RESULT.json','SOURCE_BINDINGS.json','CONDITIONAL_ERROR_CONTRACT.json','CONTROLS.json']:
 assert (P/'c28_math_v2'/n).read_bytes()==(P/'c28_replay'/n).read_bytes();rows.append({'path':n,'sha256':H(C/n),'byte_identical':True})
(C/'REPLAY_RECEIPT.json').write_text(json.dumps({'status':'PASS_FOUR_SCIENTIFIC_FILES_BYTE_IDENTICAL','files':rows,'python':platform.python_version(),'dependencies':'Python standard library/Fraction only','new_acquisitions_or_estimator_calls':0,'actual_error_premise_evidence':'UNSUPPLIED_HOLD','physical_promotion':0},indent=2)+'\n')
(C/'CORRECTION_REGISTRY.json').write_text(json.dumps({'new_frozen_mathematical_retractions':0,'prior_results_changed':False,'prefinal_qualifications':['Zero-error reconstruction bound is non-strict; strict0<0 is not claimed.','Whole-space singular continuity requires a fixed linear actual map; a per-record envelope alone does not imply linearity.','Final wording uses scalar-noise cap<=8u universally, includingu=0; strict version only forpositiveu.','Source weight gains use absolute weight errors, not relative ones; selected3/2 nominal weight must be included for relative uncertainty.','Initial root checker was extended with new source100-entry selectedGram calibration checks; existing conditional arithmetic unchanged.'],'session_wide_retraction_ratio':'NOT_COMPUTABLE; complete session denominator unavailable','physical_promotion':0},indent=2)+'\n')
(C/'CLAIM_LEDGER.json').write_text(json.dumps({'lane':'Development — no registry entry','origin':'PR307 conditioned observation map plus declared deterministic errors; new exact source weight gain and Fraction-only profile/controls','constructor':'Codex root','reviewer':'Separate same-team source/arithmetic/proof review, not external promotion authority','claims':[{'id':'ERR1','type':'DERIVED_CONDITIONAL','statement':'Normalized data error<=p+(X+p)b+nu+enc, b<=rho_RMS+T_RMS*xi+(5+xi)*eta_RMS; coherent errors/mixedterms retained.','dependencies':['PR307 unitary map/norm','THEOREM.md sections2-3']},{'id':'ERR2','type':'DERIVED_CONDITIONAL','statement':'Ideal observable-state error<=C*dataerror; implemented decoder error<=alphaX+beta*dataerror+algorithmerror, requiring independent full-state conformance BF≈P.','dependencies':['PR307 s61/27648','THEOREM.md section4','eight exact logical controls']},{'id':'ERR3','type':'EXACT_SOURCE_GAIN','statement':'For absolute top-weight errors supportedJ, ||DeltaK||=2 max|delta d_j| from selectedGram4I; allweighterroru givesnorm<=sqrt8*u<=3u.','dependencies':['pinned source complex','100selectedGram entries','THEOREM.md section6']},{'id':'ERR4','type':'DECLARED_CONDITIONAL_EXAMPLE','statement':'Specified unsupported input bounds imply observable-chain error<2^-40<2^-39. Actual accuracy/acquisition/decoder admission HOLD.','dependencies':['CONDITIONAL_ERROR_CONTRACT.json','Fraction checks','all errorpremises UNSUPPLIED']}],'no_gate_transfer':['sixratio q calibration','nominal Hankel2029 family','actual321column floating estimator','physical acquisition/source/noise evidence'],'external_promotion_review':'PENDING','physical_promotion':0},indent=2)+'\n')
(C/'README.md').write_text('''# Error propagation needs decoder conformance and source bounds

Development — no registry entry. DERIVED conditional mathematics. External promotion review PENDING; Physical Promotion=0.

For the unchanged PR307 weighted4096 half-step map, this capture propagates deterministic preparation, generator, readout, clock, noise, encoding and implementation errors. Rank1999/kernel641 and inverse amplification C=27648/61 are inherited and hash-pinned.

The normalized data envelope is

    D <= p + (X+p)b + nu + encoding,
    b <= rho_RMS + T_RMS*xi + (5+xi)*eta_RMS.

Here X bounds the full state amplitude, p the fixed preparation error, xi the skew generator perturbation, rho the readout operator error and eta the model-time error. T_RMS²=11180715/8. No independent or zero-mean noise is assumed. Coherent noise does not gain a1/sqrt4096 reduction. The preparation/readout and clock/generator mixed terms remain.

The ideal nominal inverse has observable-state error<=C*D. An implemented decoder instead needs independent operator bounds ||B||<=beta and ||BF−P||<=alpha over the full2640-state space, plus a numerical implementation bound. Its error is at most alphaX+betaD+algorithmerror. The good condition number alone does not establish those premises.

An exact two-coordinate counterexample has a unit trial frame, zero dynamics residual and a perfect forward right inverse, but its decoder adds a hidden component4/3 to a noiseless state. Thus the PR307 arbitrary-frame conditioning proof remains valid, while a decoder built from that frame still needs separate conformance to the orthogonal observable projection.

## Conditional arithmetic example — not admitted data

The explicitly declared control bounds in CONDITIONAL_ERROR_CONTRACT.json imply observable-chain error<2^-40<2^-39 by exact Fraction arithmetic. Every input-evidence receipt is missing and marked HOLD. No measured precision, noise tolerance, fresh acquisition or actual floating-estimator pass is claimed. The target is observable-chain Euclidean error, distinct from the older six-ratio q, port-residual and Hankel contracts.

Source calibration is made concrete: the selected ten tetrahedron boundary columns have Gram4I, so absolute weight errors supported there give exactly ||DeltaK||=2max|delta d|. Relative errors need the selected nominal weight3/2. The gain is a conditional mathematical identity; no physical weight law or measured weight uncertainty is supplied.

Small map error preserves conditioning on the nominal observable subspace when b<s. It does not preserve the entire actual kernel or full-positive condition number: tiny perturbations can expose very weak extra modes. The641 nominal hidden dimensions remain unreconstructable from nominal records.

## Checks and replay

```bash
python /absolute/UD/captures/CAPTURE_ID/compute.py --repo /absolute/UD --out /absolute/new-output
```

Replace CAPTURE_ID with this directory. The checker uses only the Python standard library, reads pinned parent files and source-complex JSON as data, checks all100 selected Gram entries, finite clock moments, a declared exact profile and eight logical countermodels. It outputs four byte-identical scientific JSON files on replay. It does not execute archived scripts or call an estimator/eigensolver/acquisition pipeline.

Separate same-team review independently derives the error lemmas, profile fractions, clock moments, source weight gains, decoder countermodel and continuity limitations. Final source/theorem hashes and replay are bound. This is not external promotion authority. Optional reviewer analysis is labeled separately from the root protocol and does not admit unsupported premises.

The next concrete implementation task is a nominal decoder with a verified full-space BF−P bound and arithmetic error, using matrix-free observation actions. Independently justified amplitude, preparation, timing, readout, generator, noise and encoding bounds remain necessary before physical use. No public-site/Project-board deployment or outreach is asserted.

Ledger v0.39/CRL-2; O03 controls are not theory constants. Zero new frozen mathematical retractions; full-session ratio NOT_COMPUTABLE. External promotion review PENDING; Physical Promotion=0. Gap2_FINAL_Finite_Genesis.png unavailable and unused—please re-upload if needed. Notes/ASTER available unused. CI/merge/tracking receipts are reported separately.
''')
(C/'RUN_FOOTER.md').write_text('''A. Derived: Deterministic normalized data/reconstruction envelopes retain amplitude and mixedterms; implemented decoder requires full-state BF−P conformance. Exact selected absolute-weight calibration gain2. Conditional control profile implies error<2^-40<2^-39, with all actual input evidence HOLD.

B. Checked:100 source Gram entries, exact finite clock moments, eight logical countermodels, four byte-identical Fraction JSON replays and separate same-team final source review. No new estimator/acquisition call.

C. Limits: Condition number does not certify a decoder or error premises. Full641-hidden state unrecovered; perturbations need not preserve actual kernel. Observable-chain target is distinct from sixratio/Hankel/calibration gates. Actual admission HOLD.

D. Append-only capture/event/uniquePR, CI/merge/tracking separately reported. Next: construct a decoder with verified full-state projection and arithmetic conformance. No public-site deployment or outreach.

Governance: Ledger0.39/CRL-2; Development—no registry entry; O03notconstants.0 new frozen mathematical retractions; sessionratio NOT_COMPUTABLE. External promotion review PENDING; Physical Promotion=0. PNG unavailable/unused—please re-upload if needed. Notes/ASTER available unused.
''')
m={'capture_id':cid,'timestamp_utc':now.isoformat(),'base_commit':base,'status':'CONDITIONAL_ERROR_PROPAGATION_PASS_ACTUAL_ADMISSION_HOLD','lane':'Development — no registry entry','physical_promotion':0,'external_review':'PENDING','supersedes':[],'extends':['2026-10-20T234200Z-codex-weighted-conditioning-d6af1d67'],'verification_scope':'New deterministic conditional error/decoder theorem, exact source calibration gain and logical controls; parent rank/conditioning inherited; all actual error/decoder evidence UNSUPPLIED_HOLD','files':[]}
for f in sorted(C.rglob('*')):
 if f.is_file():m['files'].append({'path':str(f.relative_to(R)),'sha256':H(f),'size_bytes':f.stat().st_size,'provenance':'Pinned parent/source model; declared unsupported error controls; exact Fraction/source arithmetic; separate same-team review; supplied governance','status':'Development—no registry entry; actual admission HOLD; external promotion review PENDING'})
(C/'MANIFEST.json').write_text(json.dumps(m,indent=2)+'\n');(R/'events'/f'{cid}.json').write_text(json.dumps({'capture_id':cid,'timestamp_utc':now.isoformat(),'base_commit':base,'event_type':'DETERMINISTIC_ERROR_PROPAGATION_AND_DECODER_CONFORMANCE','manifest':str((C/'MANIFEST.json').relative_to(R)),'conditional_example':'observable_chain_error<2^-40 IF unsupported premises hold','actual_admission':'HOLD','physical_promotion':0,'external_review':'PENDING'},indent=2)+'\n')
s={'capture_id':cid,'capture_path':str(C),'base':base,'branch':'codex/'+cid};(P/'c28_state.json').write_text(json.dumps(s,indent=2)+'\n');print(json.dumps(s,indent=2))
