from pathlib import Path
import json,hashlib,datetime,uuid,subprocess,shutil,platform
P=Path('/workspace/scratch/f3d1c2f040c9');R=P/'ud-repo';J=lambda p:json.loads(p.read_text());H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
review=P/'c25_review';rr=J(review/'REVIEW.json');final=J(review/'FINAL_BINDING.json');assert rr['status'].startswith('PASS')and final['status'].startswith('PASS')
for line in(review/'VERIFICATION_HASH_MANIFEST.sha256').read_text().splitlines():
 h,n=line.split(None,1);assert H(review/n.strip())==h
now=datetime.datetime.now(datetime.timezone.utc);base=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip();cid=now.strftime('%Y-%m-%dT%H%M%SZ')+'-codex-adjacent-weights-'+uuid.uuid4().hex[:8];C=R/'captures'/cid;C.mkdir()
for f in(P/'c25_math').iterdir():shutil.copyfile(f,C/f.name)
shutil.copyfile(P/'c25_compute.py',C/'compute.py');(C/'review').mkdir()
for n in rr['capture_allowlist']+['VERIFICATION_HASH_MANIFEST.sha256','FINAL_BINDING.json']:shutil.copyfile(review/n,C/'review'/n)
(C/'root').mkdir();shutil.copyfile(P/'c25_build.py',C/'root/build_capture.py');(C/'governance').mkdir()
for n in['20-UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39-2-.md','21-UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md']:shutil.copyfile(P/'project_sources'/n,C/'governance'/n)
rows=[]
for n in['RESULT.json','WITNESS.json','SOURCE_BINDINGS.json']:
 assert (P/'c25_math'/n).read_bytes()==(P/'c25_replay'/n).read_bytes()==(P/'c25_final_replay'/n).read_bytes();rows.append({'file':n,'sha256':H(C/n),'byte_identical':True})
(C/'REPLAY_RECEIPT.json').write_text(json.dumps({'status':'PASS_THREE_SCIENTIFIC_FILES_BYTE_IDENTICAL','files':rows,'python':platform.python_version(),'dependencies':'Python standard library only','scope':'Final checker replays new exact source/weight/angle/finite-response arithmetic; old rank proofs inherited','new_fits_or_estimator_calls':0,'physical_promotion':0},indent=2)+'\n')
(C/'CORRECTION_REGISTRY.json').write_text(json.dumps({'new_frozen_mathematical_retractions':0,'prior_results_changed':False,'prefinal_qualifications':['Pairwise Ai commutation/annihilation alone is not the N-invariance proof; downward-closed grade-resolved readout is essential','Local weighted witness moves the kernel but proves no rank increase','ker(H^-1 A)=kerA is stationary-kernel equality, not dynamic-observer-kernel equality; preparation transport is mandatory'],'execution_note':'After first checks, one exact reciprocal-witness assertion was added. Scientific JSON files remained byte-identical under final-source replay; final review binding names source/theorem. No fit or solver retry.','session_wide_retraction_ratio':'NOT_COMPUTABLE; complete session denominator unavailable','physical_promotion':0},indent=2)+'\n')
(C/'CLAIM_LEDGER.json').write_text(json.dumps({'lane':'Development — no registry entry','origin':'Inherited unit-chain62channel observer and declared grade rates/weighted-boundary operators; new exact sparse source identities','constructor':'Codex root','reviewer':'Separate same-team mathematical source/arithmetic reviewer, not external promotion authority','claims':[{'id':'GR1','type':'DERIVED_CONDITIONAL','statement':'Every constant nonzero grade-rate triple has exactly the nominal N747, even at weighted frequency collisions.','dependencies':['THEOREM.md section2','source cochain restrictions and cross-channel annihilation','inherited nominal N747']},{'id':'GR2','type':'DERIVED_CONDITIONAL','statement':'Arbitrary locally integrable grade rates cannot reveal oldN; equality for zero/time-varying rates is not claimed.','dependencies':['GR1 direct-channel decomposition','THEOREM.md section2']},{'id':'LW1','type':'EXACT_DECLARED_MODEL_VARIANT','statement':'Local whole-column weights, including a C10 orbit, expose oldh while retaining new stationary darkz; both kernel set differences witnessed. Total weighted rank NOT_COMPUTED.','dependencies':['WITNESS.json','RESULT.json','THEOREM.md section3']},{'id':'LW2','type':'DERIVED_FINITE_RESPONSE','statement':'For exactoldh,0<|epsilon|<=1/2, namedface atmodeltime1/64 has magnitude strictly between15|epsilon|/(1024sqrt600) and17|epsilon|/(1024sqrt600).','dependencies':['source rowbound12 and selectedGram4I','odd skew Taylor remainder','THEOREM.md section4']},{'id':'LW3','type':'DERIVED_COORDINATE_RELATION','statement':'Weighted-unit-metric and H^-1A coordinate descriptions require transporting preparations; same numeric h is not the same input in both conventions.','dependencies':['THEOREM.md section5','exact metric triplet checks']}],'external_review':'PENDING','physical_promotion':0},indent=2)+'\n')
(C/'README.md').write_text('''# Adjacent-grade rates preserve darkness; local weights move it

Development — no registry entry. DERIVED conditional mathematics; external promotion review PENDING; Physical Promotion=0.

The next question after PR300 was whether its nonlocal0↔3 example could be replaced by a declared adjacent-grade construction. The answer depends on the perturbation class. None of the results below selects a physical constitutive law or supplies acquisition evidence.

|Declared change|New exact/derived return|Scope|
|---|---|---|
|Constant nonzero rates on the three original grade couplings|Same continuous-history kernel747 and rank1893, even at weighted-frequency collisions|No finite-sampling/conditioning or unknown-rate identification claim|
|Arbitrary locally integrable grade rates|All old747hidden dimensions remain invisible|Additional blindness can arise; equality not asserted|
|Whole-tetrahedron boundary-column weights|Old hidden3-cycle becomes visible; a replacement3-cycle remains hidden|Kernel changes as a set; total weighted rank NOT_COMPUTED|
|Weight one10tetrahedron rightC10orbit|Same old/new dark-state distinction, preserving C10, adjacent grades and weightedchain nilpotency|Declared local weighted model, not native/physical weight selection|

THEOREM.md provides the proofs. The rate result uses the downward-closed, grade-resolved link readout: cochain restriction identities separate each image channel even when its frequencies collide with another channel. Pairwise commutation alone would not suffice. All isolated character kernels/ranks consequently remain unchanged under constant nonzero grade rates. Old1893/747and sector ranks are inherited, not rerun.

## Constructive local witness

The selected tetrahedron is(0,33,34,41), index0. Its ten-element orbit is[0,9,227,432,447,582,538,347,332,141]. D=I+epsilon P_J rescales those C3columns in B3D, with transposed lower block DB3^T. This retains incidence support, chain-square zero, skewness, odd chain parity and adjacent-grade locality. The orbit choice also commutes with the actual signedC10action. It is a weighted boundary, not unchanged integer incidences.

For old normalized fundamental cycle h, the named face(33,34,41), globalport1680, has derivative−epsilon/sqrt600. The new dark state z=D^-1h satisfies K_Dz=0 but is visible under the old A; thus both kernel set differences have explicit witnesses. This supplies no dimension reduction or rank1894claim for the weighted model. That PR300 rank belongs to its distinct nonlocal harmonic variant.

For0<|epsilon|<=1/2, a single noiseless response at internalmodeltime1/64 obeys

    15|epsilon|/(1024 sqrt600) < |y_face| < 17|epsilon|/(1024 sqrt600).

The bound follows from a newly checked rownorm12, perturbationnorm2|epsilon| and an odd-skew Taylor remainder. This is a mathematical finite-response enclosure. The optional half-lower scalar-error separation condition is conditional on independently supplied total error under each hypothesis, including preparation/time/readout/encoding; no actual tolerance/gate is adopted. No SI/six-ratio/residual/Hankel/321column estimator bound is transferred.

The metric description y=diag(I,I,I,D)x yields K_y=H^-1A, H=diag(I,I,I,D^-2), and unchanged readout values. It also transforms the preparation: oldx=h maps to y=Dh, whereas fixednumeric y=h remains stationary. Stationary-kernel equality in this representation is not a claim about the full dynamical observer kernel. Typed coordinates/preparations must stay explicit.

## Checks and reproduction

Run the standard-library checker from any directory, supplying a complete repository and NEW output outside it:

```bash
python /absolute/UD/captures/CAPTURE_ID/compute.py --repo /absolute/UD --out /absolute/new-adjacent-check
```

Replace CAPTURE_ID with this directory name. It reads3JSONmembers of the immutable observer archive; no archived script is executed. It checks1800boundary-product columns,15840vanishing cross-channel columns,60+60cochain restriction entries, the oriented cycle, signed action/orbit, selected Gram4I, rowbound12,19200metric triplets and exact angle/response root brackets. Final-source replay gives3byte-identical scientific JSON files; no dense fullhistory/Hankel, SVD or estimator fit occurs. Source hashes and witness signs/indices are preserved.

Separate same-team review independently checks1813source facts, the orbit/support/metric/finite-remainder argument, eight exact cases and96root-result comparisons. It checks rational dark-line angles, directed160-bit signal/angle bounds and the conditional half-lower budget. Final source/theorem and unchanged replay are bound separately; original review receipts remain. Reviewer scripts retain historical workspace paths and need relocation; the root checker has explicit CLI arguments. This is not external nonconstructor/custodian promotion review.

The next mathematical task is complete weighted-model history rank and conditioning for an explicitly frozen member. Source-supported physical weights, state preparation, time/gain/aliasing/error receipts and independent acquisition remain separate OPEN requirements. Previous nominal results, gates, failures and HOLD/NO-GO are preserved. No public-site/Project-board update or outreach is asserted.

Ledger v0.39 / CRL-2; Development—no registry entry. O03 controls/modeltime choices are not theory constants.0new frozen mathematical retractions; prefinal proof/coordinate qualifications are recorded. Full-session ratio NOT_COMPUTABLE. External promotion review PENDING; Physical Promotion=0. Gap2_FINAL_Finite_Genesis.png unavailable/unused—please re-upload if needed. Notes/ASTER availableunused. CI/merge/tracking receipts are reported separately.
''')
(C/'RUN_FOOTER.md').write_text('''A. Derived: Constantnonzerograderates keepN747/rank1893, evenfrequencycollisions; arbitraryintegrablerates retainoldNinclusion. Localwholecolumn/orbitweights movehiddenstates, with finiteface-responseenclosure; weightedrankNOT_COMPUTED.

B. Checked:1800boundary/15840crosschannelcolumns,60+60restrictions,Gram4I/row12/19200metrictriplets,3byteidenticalJSONreplays; separate1813sourcefacts/8cases/96comparisons/finalbinding. Oldrankpremisesinherited.

C. Limits: Declaredweight/metriccoordinatechoices, no nativephysicalsource or acquisition. Preparationtransportmandatory; no weightedrankshrink/inheritedsampling/estimator/gateclaim. ExistingHOLDs unchanged.

D. Append-onlycapture/event/uniquePR; CI/merge/tracking reportedseparately. No public-site/Project-boarddeployment.

Governance: Ledger0.39/CRL-2; Development—noregistryentry; O03notconstants.0frozenmathretractions; sessionratioNOT_COMPUTABLE. ExternalreviewPENDING;PhysicalPromotion=0. PNGunavailableunused—re-uploadifneeded;Notes/ASTERavailableunused.
''')
m={'capture_id':cid,'timestamp_utc':now.isoformat(),'base_commit':base,'status':'DERIVED_GRADE_RATE_INVARIANCE_AND_WEIGHTED_KERNEL_MOTION','lane':'Development — no registry entry','physical_promotion':0,'external_review':'PENDING','supersedes':[],'extends':['2026-10-20T222457Z-codex-hidden-coupling-a329b704'],'verification_scope':'New conditional rate-invariance proof and local weighted witness/finite response; nominal ranks inherited and full weighted rank not computed; no physicalsource/admission','files':[]}
for f in sorted(C.rglob('*')):
 if f.is_file():m['files'].append({'path':str(f.relative_to(R)),'sha256':H(f),'size_bytes':f.stat().st_size,'provenance':'Declared rate/weighted-chain classes; new exact source arithmetic and separate same-team review; inherited nominal ranks; supplied governance','status':'Development—no registry entry; external review PENDING'})
(C/'MANIFEST.json').write_text(json.dumps(m,indent=2)+'\n');(R/'events'/f'{cid}.json').write_text(json.dumps({'capture_id':cid,'timestamp_utc':now.isoformat(),'base_commit':base,'event_type':'GRADE_RATE_INVARIANCE_AND_LOCAL_KERNEL_MOTION','manifest':str((C/'MANIFEST.json').relative_to(R)),'nominal_rate_class_kernel':747,'weighted_model_rank':'NOT_COMPUTED','physical_promotion':0,'external_review':'PENDING'},indent=2)+'\n')
s={'capture_id':cid,'capture_path':str(C),'base':base,'branch':'codex/'+cid};(P/'c25_state.json').write_text(json.dumps(s,indent=2)+'\n');print(json.dumps(s,indent=2))
