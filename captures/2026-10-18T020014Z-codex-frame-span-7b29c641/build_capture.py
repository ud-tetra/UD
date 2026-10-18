from pathlib import Path
import json,hashlib,zipfile,datetime,shutil
P=Path(__file__).resolve().parent;repo=P.parent/'ud-repo';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ID=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H%M%SZ')+'-codex-frame-span-7b29c641';out=repo/'captures'/ID;out.mkdir(parents=True,exist_ok=False)
f=json.loads((P/'CAMPAIGN_FREEZE.json').read_text());arrays=[];archives=[];large=set()
for e in f['cases']:
 n=e['case'];p=P/f'results/{n}/FLOAT_WITNESS.npz';assert sha(p)==e['witness_sha256'];large.add(p);a=out/f'WITNESS_{n}_float.zip'
 with zipfile.ZipFile(a,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:z.write(p,p.relative_to(P).as_posix())
 arrays.append({'path':p.relative_to(P).as_posix(),'size_bytes':p.stat().st_size,'sha256':sha(p),'archive':a.name});archives.append({'filename':a.name,'size_bytes':a.stat().st_size,'sha256':sha(a)})
(P/'WITNESS_INDEX.json').write_text(json.dumps({'status':'ALL_FLOAT_ARRAYS_REQUIRED_FOR_FRAME_SPAN_PROOF_RETAINED','physical_promotion':0,'arrays':arrays,'archives':archives,'new_frame_reductions':'Inside core results/CASE/FRAME_REDUCTION.npz','instructions':'Extract core and all three witness archives into one folder, then run replay_package.py'},indent=2))
files=[p for p in P.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p not in large and p.name!='PACKAGE_MANIFEST.json']
(P/'PACKAGE_MANIFEST.json').write_text(json.dumps({'artifact':'UD_FIXED_REFERENCE_FRAME_SPAN_v0.1','physical_promotion':0,'independent_review':'pending','witness_arrays_index':'WITNESS_INDEX.json','files':[{'path':p.relative_to(P).as_posix(),'size_bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(files)]},indent=2));files.append(P/'PACKAGE_MANIFEST.json')
core=out/'UD_FIXED_REFERENCE_FRAME_SPAN_v0.1_CORE.zip'
with zipfile.ZipFile(core,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for p in sorted(files):z.write(p,p.relative_to(P).as_posix())
for p in P.iterdir():
 if p.is_file() and p.suffix in ['.py','.md','.json','.txt'] and p.name!='requirements.txt':shutil.copyfile(p,out/p.name)
entries=[{'path':p.relative_to(repo).as_posix(),'size_bytes':p.stat().st_size,'sha256':sha(p),'status':'EXACT conditional theorem / constructor validated saved outputs and replays, as typed in CLAIM_LEDGER.json','provenance':'Frozen direct reference-frame proof; hash-identical PR186/187 captured outputs; no new raw-source or estimator execution; independent review pending'} for p in sorted(out.iterdir())]
(out/'MANIFEST.json').write_text(json.dumps({'capture_id':ID,'physical_promotion':0,'status':'CONSTRUCTOR_FIXED_REFERENCE_FRAME_SPAN_CERTIFICATE','supersedes':[],'extends':['2026-10-18T014757Z-codex-operator-norm-c1a73e06','2026-10-18T011854Z-codex-floating-estimator-91b645f2'],'verification_scope':'Three saved floating-output certificates/replays; fixed fitted-reference phases, recomputed frame constants, eight tests and two actual-array corruption refusals. Old HOLDs preserved. No new raw data/estimator/full-Hankel execution, uniform all-input, physical identity or independent review.','files':entries},indent=2))
(repo/'events'/f'{ID}.json').write_text(json.dumps({'capture_id':ID,'event':'amplitude_independent_fixed_reference_span_certificate','timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'physical_promotion':0,'summary':'Direct reference-frame span proof certifies saved coherent_dc phase output<1.256e-11 radians/sample, dense_sign<0.000502361 and phase_2neg20<3.802e-7. Estimator/proposal bytes unchanged; prior HOLDs preserved. Three array replays, eight checks and two corrupted-array HOLD controls pass. No new raw source or estimator execution; independent review and uniform guarantees remain open.'},indent=2))
print(json.dumps({'capture':str(out),'core_sha256':sha(core),'core_bytes':core.stat().st_size,'total_payload_bytes':sum(p.stat().st_size for p in out.glob('*.zip')),'archives':len(archives)+1,'core_files':len(files)}))
