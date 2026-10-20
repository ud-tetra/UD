from pathlib import Path
import json,hashlib,subprocess,datetime,uuid,shutil
P=Path('/workspace/scratch/f3d1c2f040c9');R=P/'ud-repo'
J=lambda p:json.loads(p.read_text());H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
now=datetime.datetime.now(datetime.timezone.utc);base=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip()
cid=now.strftime('%Y-%m-%dT%H%M%SZ')+'-codex-source-readiness-'+uuid.uuid4().hex[:8];C=R/'captures'/cid;C.mkdir()
for src,dst in [('c23_deposit.json','DEPOSIT_METADATA.json'),('c23_source_bindings.json','SOURCE_BINDINGS.json'),('c23_metadata_compare.json','METADATA_COMPARISON.json'),('c23_access.json','SOURCE_ACCESS.json')]:shutil.copyfile(P/src,C/dst)
bindings=J(C/'SOURCE_BINDINGS.json');d=J(C/'DEPOSIT_METADATA.json');comp=J(C/'METADATA_COMPARISON.json')
assert len(d['files'])==71 and len({f['path'] for f in d['files']})==71
assert comp=={'prior_raw_count':32,'current_raw_count':32,'differences':[]}
old=J(R/'captures/2026-10-19T222108Z-codex-uniform-phase-evidence-4a6f6bda/evidence/RAW_METADATA_INVENTORY.json')['records']
current=[{'path':x['path'],'bytes':x['size_bytes'],'persistent_id':x['persistent_id'],'checksum':x['checksum']} for x in d['files'] if x['path'].endswith('.gz')]
assert {x['path']:x for x in old}=={x['path']:x for x in current}
for row,name in zip(bindings,['utility','drive1']):
 b=(P/f'c23_{name}.c').read_bytes();m=next(x for x in d['files']if x['path']==row['path']);assert H(P/f'c23_{name}.c')==row['sha256'];assert len(b)==m['size_bytes']==row['bytes'];assert hashlib.md5(b).hexdigest()==m['checksum']['value']==row['MD5'];assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==row['git_blob']
u=(P/'c23_utility.c').read_text();v=(P/'c23_drive1.c').read_text()
assert 'RP_TRIG_SRC_NOW' in u and 'RP_TRIG_SRC_EXT_NE' in v
assert 'acquire_2channels(' not in v and 'best_decimation_factor(' not in v
assert 'rp_AcqSetDecimation(RP_DEC_64)' in v and 'rp_AcqSetTriggerDelay(7992)' in v
assert all(x in v for x in ['parse_cmd_line_range(', 'lin_scale_steps(', 'ttl_arb_waveform('])
receipt={'status':'PASS_SCOPED_SOURCE_READINESS_AUDIT','release':'1.0','release_time':d['release_time'],'published_files':71,'published_gzip_metadata_records':32,'unchanged_gzip_metadata_records':32,'metadata_differences':0,'source_files_newly_byte_bound':2,'source_binding_checks_per_file':['bytecount','SHA256','Git blob identity','deposit published MD5'],'static_scope':'Textual source observations, not compiled binary/callgraph/runtime proof','raw_archives_downloaded':0,'candidate_raw_opened':0,'notebooks_or_author_code_executed':0,'estimator_calls':0,'new_calibration_evidence':0,'new_qualifying_native_records':0,'candidate_admitted':False,'numerical_tools_changed':False,'physical_promotion':0,'external_review':'PENDING'}
(C/'RESULT.json').write_text(json.dumps(receipt,indent=2)+'\n')
review=P/'c23_review';assert (review/'REVIEW.json').is_file()
(C/'review').mkdir()
for name in ['REVIEW.json','REVIEW.md']:
 shutil.copyfile(review/name,C/'review'/name)
(C/'root').mkdir();shutil.copyfile(P/'c23_build.py',C/'root/build_capture.py')
(C/'governance').mkdir()
for name in ['20-UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39-2-.md','21-UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md']:shutil.copyfile(P/'project_sources'/name,C/'governance'/name)
(C/'README.md').write_text('''# Source-readiness audit after the executable numerical handoff

Development — no registry entry. Ledger v0.39 / CRL-2. External promotion review PENDING; Physical Promotion=0.

The PR296 numerical handoff is complete. This turn checked whether the published circuit sources can supply its missing acquisition premises. No qualifying native record or calibration bundle was obtained. No extra numerical wrapper, new fit, replay of the old large records or full Hankel allocation was needed.

## Primary-source return

The live-request heiDATA API still reports release1.0, published2022-02-03. All71 file metadata entries were inspected. All32gzip metadata tuples (path, size, PID and published checksum) exactly match the earlier PR253 audit. Checksums of those32raw archives were not recomputed; no raw archive was downloaded. Filename inventories cannot exclude calibration information embedded in unopened files, and the finite source/search scope does not prove no appropriate evidence exists elsewhere.

The previously unavailable utility.c was recovered via exact-commit GitHub retrieval. Its3100bytes and drive1's8200bytes each match their published deposit size and MD5; independently calculated Git blob IDs match the returned exact-commit IDs. SHA256 bindings are in SOURCE_BINDINGS.json. This binds repository source bytes to published metadata, not to an acquisition binary or instrument. Remote deposited source contents were not separately downloaded.

| Source at author commit265b6671dde799d7c73f32247fa3ee93ae70e0f2 | Static observation | Applicability |
|---|---|---|
|utility.c|A selectable-decimation helper uses a nominal20-samples-per-cycle target; its acquisition helper uses a software trigger.|No inference that this helper acquired the selected waveform.|
|u1_drive1.c|Direct setup uses /64 and external negative-edge triggering, delay7992; it calls other utility functions.|It does not call either acquisition/decimation helper above. Including a header does not select those helper settings.|

These source observations do not establish firmware, board identity, actual clock, skew, anti-alias coverage or gain calibration. The earlier conditional drive1 recipe is unchanged. The two different trigger paths must not be merged into one purported experimental configuration. No author program was compiled or executed.

The paper's AppendixA describes empirical driven-system dissipation k=0.0045 adjusted to observations. AppendixF uses measured site amplitudes in frequency-shift predictions. A future comparison must declare these conditioning inputs and partition scored outcomes; they are not untouched predictions merely because equations are published. AppendicesB/C discuss feedback tuning and background removal. None of these paper passages supplies the required source-bound joint calibration/error certificate or native UD observation map. This is a scoped reading of that paper, not rejection of its own scientific conclusions.

## Decision and concrete next work

The uninspected05-28 candidate remains under its unchanged metadata gate. Its own source/channel map, prior exposure, calibration and reviewed physical predictor/comparator/score freeze are required before confirmatory raw inspection. The new source read supplies none of those missing records. The prior128 request blockers have not been rerun or resolved; that count is inherited from PR250/253, not a new preflight result.

For native62-channel admission, obtain one actual source-bound acquisition bundle with preparation/raw/projection and coordinate-unit receipts, independently justified calibration/timebase/aliasing coverage and the native observation-map contract. For this ten-channel circuit, use its separate component contract and explicitly retrospective model-development scope unless its own fresh-confirmation gate is satisfied. Do not pad or rename it into the37×8191×62 experiment. No native1893/747, six-ratio/SI or physical-correspondence claim advances here.

Until new source evidence arrives, further replay of the same two matrices cannot close acquisition provenance. Keep the runner ready and tasks open. No new challenge, synthetic preparation, fitted comparator, signatures, timestamps or custodian receipt was manufactured. No outreach or public-site deployment occurred.

## Evidence and reproducibility

DEPOSIT_METADATA.json retains normalized public file metadata only; SOURCE_BINDINGS.json gives source-byte identities, SOURCE_ACCESS.json records successful and failed routes and limited paper paraphrases, METADATA_COMPARISON.json binds the32record comparison. RESULT.json records finite scope. Root checks SHA256/MD5/Gitblob/size on the fetched source bytes and textual call-site distinctions; this is not a compiled-program correctness proof. The captured root script documents original execution paths; source-byte replay needs separately retrieved exact-commit files with those identities. Separate same-team review in review/ is not external nonconstructor promotion review. Primary source URLs are recorded below.

- https://heidata.uni-heidelberg.de/api/datasets/:persistentId/?persistentId=doi:10.11588/DATA/6MEKHI
- https://github.com/tychon/U1CircuitsData/blob/265b6671dde799d7c73f32247fa3ee93ae70e0f2/redpitaya-measurements/c/utility.c
- https://github.com/tychon/U1CircuitsData/blob/265b6671dde799d7c73f32247fa3ee93ae70e0f2/redpitaya-measurements/c/u1_drive1.c
- https://arxiv.org/html/2108.01086v1 (AppendicesA/B/C/F)

Web retrieval initially failed for all3pages; Firecrawl recovered paper/deposit and GitHub recovered exact source. An exact-repository calibration search returned0hits; that failure is retained without an absence inference. No instrument/error bound is filled using generic manufacturer specifications. Historical immutable sources, gates and HOLD/NO-GO conclusions are unchanged. No new mathematical retractions or frozen-source correction; full-session retraction ratio NOT_COMPUTABLE without a complete denominator. O03 controls remain protocol choices, not theory constants. PNG unavailable/unused; re-upload if needed. Notes/ASTER available but unused. Publication/CI/merge/tracking receipts are reported separately.
''')
(C/'RUN_FOOTER.md').write_text('''A. Source audit:71publishedfilemetadata,32unchangedrawmetadata;2sourcefilesnewlybytebound. Utility/helper versus drive1 applicability separated. Paper fitted/conditioned comparison identified. No fresh qualifying record.

B. Checked: exact source size/MD5/Gitblob/SHA256,32prior/currentmetadata tuples, textualcallsite distinctions and separate same-team source review. No raw or author-code execution; not compiled runtime proof.

C. Limits: calibration/source-map/freshness HOLD; prior gates and failures unchanged.128blockers inherited, not rerun. No new fit/acquisition/native result. External review PENDING.

D. Capture: append-only manifest/event and unique PR. CI/merge/tracking reported separately; no Project-board/public-site update asserted.

Governance: Ledger v0.39 / CRL-2; Development—no registry entry; O03 not theory constants.0new mathematical retractions; session ratio NOT_COMPUTABLE. Physical Promotion=0. Gap2_FINAL_Finite_Genesis.png unavailable/unused—re-upload if needed. Notes/ASTER availableunused.
''')
m={'capture_id':cid,'timestamp_utc':now.isoformat(),'base_commit':base,'status':receipt['status'],'lane':'Development — no registry entry','physical_promotion':0,'external_review':'PENDING','supersedes':[],'extends':['2026-10-20T213923Z-codex-executable-handoff-c5441caa','2026-10-19T222108Z-codex-uniform-phase-evidence-4a6f6bda'],'verification_scope':'Finite source/readiness audit, no new raw acquisition/fit/calibration or physical correspondence','files':[]}
for f in sorted(C.rglob('*')):
 if f.is_file():m['files'].append({'path':str(f.relative_to(R)),'size_bytes':f.stat().st_size,'sha256':H(f),'provenance':'New primary metadata/source audit and separate same-team review; exact supplied governance','status':'Development—no registry entry; external review PENDING'})
(C/'MANIFEST.json').write_text(json.dumps(m,indent=2)+'\n')
(R/'events'/f'{cid}.json').write_text(json.dumps({'capture_id':cid,'timestamp_utc':now.isoformat(),'base_commit':base,'event_type':'SOURCE_READINESS_AUDIT_NO_QUALIFYING_RECORD','manifest':str((C/'MANIFEST.json').relative_to(R)),'status':receipt['status'],'new_qualifying_native_records':0,'new_calibration_evidence':0,'physical_promotion':0,'external_review':'PENDING'},indent=2)+'\n')
s={'capture_id':cid,'capture_path':str(C),'base':base,'branch':'codex/'+cid,'status':receipt['status']};(P/'c23_state.json').write_text(json.dumps(s,indent=2)+'\n');print(json.dumps(s,indent=2))
