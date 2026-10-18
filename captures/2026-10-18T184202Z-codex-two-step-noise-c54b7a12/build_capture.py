from pathlib import Path
import json,hashlib,zipfile,datetime,shutil
P=Path(__file__).resolve().parent;repo=P.parent/'ud-repo';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ID=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H%M%SZ')+'-codex-two-step-noise-c54b7a12';out=repo/'captures'/ID;out.mkdir(parents=True,exist_ok=False)
large=set((P/'results').rglob('*.npz'));groups=[];current=[];size=0
for p in sorted(large):
 assert p.stat().st_size<9000000
 if current and size+p.stat().st_size>9000000:groups.append(current);current=[];size=0
 current.append(p);size+=p.stat().st_size
if current:groups.append(current)
arrays=[];archives=[]
for i,group in enumerate(groups,1):
 a=out/f'WITNESS_{i:02d}.zip'
 with zipfile.ZipFile(a,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
  for p in group:z.write(p,p.relative_to(P).as_posix());arrays.append({'path':p.relative_to(P).as_posix(),'size_bytes':p.stat().st_size,'sha256':sha(p),'archive':a.name})
 assert a.stat().st_size<12000000;archives.append({'filename':a.name,'size_bytes':a.stat().st_size,'sha256':sha(a)})
(P/'WITNESS_INDEX.json').write_text(json.dumps({'status':'ALL_AVAILABLE_ACTUAL_ARRAYS_AND_EXACT_GRAMS_RETAINED','physical_promotion':0,'arrays':arrays,'archives':archives,'instructions':'Extract core and all witness ZIPs into one folder, then run replay_package_v2.py'},indent=2))
files=[p for p in P.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p not in large and p.name!='PACKAGE_MANIFEST.json' and 'records' not in p.relative_to(P).parts]
(P/'PACKAGE_MANIFEST.json').write_text(json.dumps({'artifact':'UD_TWO_STEP_NOISE_TOLERANCE_v0.1','physical_promotion':0,'independent_review':'pending','files':[{'path':p.relative_to(P).as_posix(),'size_bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(files)]},indent=2));files.append(P/'PACKAGE_MANIFEST.json')
core=out/'UD_TWO_STEP_NOISE_TOLERANCE_v0.1_CORE.zip'
with zipfile.ZipFile(core,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for p in sorted(files):z.write(p,p.relative_to(P).as_posix())
assert core.stat().st_size<12000000
for p in P.iterdir():
 if p.is_file() and p.suffix in ['.py','.md','.json','.txt']:shutil.copyfile(p,out/p.name)
entries=[{'path':p.relative_to(repo).as_posix(),'size_bytes':p.stat().st_size,'sha256':sha(p),'status':'Conditional uniform noise/order bound and six-case actual two-step noise campaign; all HOLDs preserved','provenance':'Known PR195 synthetic records, frozen new source-precision rule/adapter, exact binary residuals and normal-model similarity certificate; same-team review only'} for p in sorted(out.iterdir())]
(out/'MANIFEST.json').write_text(json.dumps({'capture_id':ID,'physical_promotion':0,'status':'TWO_STEP_NOISE_TOLERANCE_BOUNDED','supersedes':[],'extends':['2026-10-18T181950Z-codex-two-step-adapter-39ce61a8'],'verification_scope':'Arbitrary per62-vector order budget2^-37; six frozen noisy raw records checked and separately regenerated;12 original/instrumented estimator runs, six order replays, five actual saved-array phase replays, six tests. Dense noise amplitude65536 passes phase certificate; dense33554432 changes learned order to321 and HOLD; DC33554432 passes. Uniform phase sufficient bound HOLD even atzero. No SI, full-Hankel, independent-review or physical-promotion claim.','files':entries},indent=2))
(repo/'events'/f'{ID}.json').write_text(json.dumps({'capture_id':ID,'event':'two_step_noise_tolerance_campaign','timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'physical_promotion':0,'summary':'Quantified uniform order209 tolerance: arbitrary per62-vector noise≤2^-37. Six frozen cases, all raw gates checked and hashes regenerated;12 actual runs, five phase replays and six tests. Largest tested dense pass amplitude65536; dense33554432 learns321 and remains HOLD. Coherent DC33554432 passes. All uniform ideal-phase rows HOLD; not a failure proof. Postexecution supplemental rounding correction disclosed; original code/failure retained. Physical promotion0; independent review pending.'},indent=2))
print(json.dumps({'capture':str(out),'core_sha256':sha(core),'core_bytes':core.stat().st_size,'total_payload_bytes':sum(p.stat().st_size for p in out.glob('*.zip')),'archives':len(archives)+1,'arrays':len(arrays),'core_files':len(files)}))
