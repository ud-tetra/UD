from pathlib import Path
import json,hashlib,zipfile,datetime,shutil
P=Path(__file__).resolve().parent;repo=P.parent/'ud-repo';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ID=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H%M%SZ')+'-codex-two-step-adapter-39ce61a8';out=repo/'captures'/ID;out.mkdir(parents=True,exist_ok=False)
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
(P/'WITNESS_INDEX.json').write_text(json.dumps({'status':'ALL_AVAILABLE_ACTUAL_ARRAYS_AND_EXACT_GRAMS_RETAINED','physical_promotion':0,'arrays':arrays,'archives':archives,'instructions':'Extract core and all witness ZIPs into one folder, then verify_structure.py and replay_package.py'},indent=2))
files=[p for p in P.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p not in large and p.name!='PACKAGE_MANIFEST.json']
(P/'PACKAGE_MANIFEST.json').write_text(json.dumps({'artifact':'UD_ACTUAL_TWO_STEP_SOURCE_PRECISION_v0.1','physical_promotion':0,'independent_review':'pending','files':[{'path':p.relative_to(P).as_posix(),'size_bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(files)]},indent=2));files.append(P/'PACKAGE_MANIFEST.json')
core=out/'UD_ACTUAL_TWO_STEP_SOURCE_PRECISION_v0.1_CORE.zip'
with zipfile.ZipFile(core,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for p in sorted(files):z.write(p,p.relative_to(P).as_posix())
assert core.stat().st_size<12000000
for p in P.iterdir():
 if p.is_file() and p.suffix in ['.py','.md','.json','.txt']:shutil.copyfile(p,out/p.name)
entries=[{'path':p.relative_to(repo).as_posix(),'size_bytes':p.stat().st_size,'sha256':sha(p),'status':'Conditional actual two-step source-precision phase/output and rank certificate; previous noise HOLD preserved','provenance':'Known PR195 synthetic records, frozen new source-precision rule/adapter, exact binary residuals and normal-model similarity certificate; same-team review only'} for p in sorted(out.iterdir())]
(out/'MANIFEST.json').write_text(json.dumps({'capture_id':ID,'physical_promotion':0,'status':'ACTUAL_TWO_STEP_SOURCE_PRECISION_AUDIT_CERTIFIED','supersedes':[],'extends':['2026-10-18T172041Z-codex-floating-timing-2f6a91ce','2026-10-18T180347Z-codex-wide-timing-81a7d5c2'],'verification_scope':'Two exact source-precision orders105/209, four actual original/instrumented runs, two full saved-array phase replays, six tests and two actual-array corruption refusals. Source-model rank209 closes previous interval; original204/205 noise-cutoff HOLD unchanged. No SI, independent review, original-contract admission or new full-Hankel proof.','files':entries},indent=2))
(repo/'events'/f'{ID}.json').write_text(json.dumps({'capture_id':ID,'event':'actual_two_step_source_precision_phase_certificates','timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'physical_promotion':0,'summary':'New source-precision cutoff2^-24: actual record-only counts105/209 agree with exact source-order proof. Baseline circular2step phase error<1.373e-13, stress<8.961e-10, unique209targetmatching. Four actual runs, two source-order and two saved-array phase replays, six tests, two corrupted-array refusals. Source comparisonrank209; encoded exact algebraicrank separate. Original noisecutoff204/205HOLD and modulo-pi ambiguity preserved; no physical/CRL promotion.'},indent=2))
print(json.dumps({'capture':str(out),'core_sha256':sha(core),'core_bytes':core.stat().st_size,'total_payload_bytes':sum(p.stat().st_size for p in out.glob('*.zip')),'archives':len(archives)+1,'arrays':len(arrays),'core_files':len(files)}))
