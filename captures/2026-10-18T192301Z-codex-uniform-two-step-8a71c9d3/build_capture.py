from pathlib import Path
import json,hashlib,zipfile,datetime,shutil
P=Path(__file__).resolve().parent;repo=P.parent/'ud-repo';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();ID=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H%M%SZ')+'-codex-uniform-two-step-8a71c9d3';out=repo/'captures'/ID;out.mkdir(exist_ok=False)
large=set(P.rglob('*.npz'));groups=[];current=[];size=0
for p in sorted(large):
 assert p.stat().st_size<9000000
 if current and size+p.stat().st_size>9000000:groups.append(current);current=[];size=0
 current.append(p);size+=p.stat().st_size
if current:groups.append(current)
arrays=[];archives=[]
for i,g in enumerate(groups,1):
 a=out/f'WITNESS_{i:02d}.zip'
 with zipfile.ZipFile(a,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
  for p in g:z.write(p,p.relative_to(P).as_posix());arrays.append({'path':p.relative_to(P).as_posix(),'size_bytes':p.stat().st_size,'sha256':sha(p),'archive':a.name})
 assert a.stat().st_size<12000000;archives.append({'filename':a.name,'size_bytes':a.stat().st_size,'sha256':sha(a)})
(P/'WITNESS_INDEX.json').write_text(json.dumps({'arrays':arrays,'archives':archives,'status':'ALL_ACTUAL_AND_BASELINE_ARRAYS_AND_EXACT_GRAMS_RETAINED','physical_promotion':0},indent=2))
files=[p for p in P.rglob('*') if p.is_file() and '__pycache__' not in p.parts and 'records' not in p.relative_to(P).parts and p not in large and p.name!='PACKAGE_MANIFEST.json']
(P/'PACKAGE_MANIFEST.json').write_text(json.dumps({'files':[{'path':p.relative_to(P).as_posix(),'size_bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(files)],'physical_promotion':0,'artifact':'UD_UNIFORM_IDEAL_TWO_STEP_PHASE_v0.1'},indent=2));files.append(P/'PACKAGE_MANIFEST.json');core=out/'UD_UNIFORM_IDEAL_TWO_STEP_PHASE_v0.1_CORE.zip'
with zipfile.ZipFile(core,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for p in sorted(files):z.write(p,p.relative_to(P).as_posix())
assert core.stat().st_size<12000000
for p in P.iterdir():
 if p.is_file() and p.suffix in ['.py','.json','.md','.txt']:shutil.copyfile(p,out/p.name)
entries=[{'path':p.relative_to(repo).as_posix(),'size_bytes':p.stat().st_size,'sha256':sha(p),'status':'Conditional uniform ideal phase theorem and finite actual floating control; all HOLDs preserved','provenance':'Exact encoded-baseline cross-Grams, separate raw replay/regeneration, pinned parent source witnesses and same-team proof review; not independent data/review'} for p in sorted(out.iterdir())]
(out/'MANIFEST.json').write_text(json.dumps({'capture_id':ID,'physical_promotion':0,'status':'UNIFORM_IDEAL_TWO_STEP_PHASE_TOLERANCE_CERTIFIED','supersedes':[],'extends':['2026-10-18T184202Z-codex-two-step-noise-c54b7a12'],'verification_scope':'Two64-row grids in total:32rows perversion; v2 certifies uniform ideal209-target matching at2^-48 per62-vector, phase error<2.618e-7 radians/2steps;2^-47HOLD. Exact baseline cross-Gram raw replay, fresh cyclic-unit raw regeneration, two actual original/instrumented runs, primary saved-array phase replay and two zero-coefficient all-HOLD controls pass. No uniform actual-floating convergence, apparatus, full-Hankel or physical/CRL promotion.','files':entries},indent=2))
(repo/'events'/f'{ID}.json').write_text(json.dumps({'capture_id':ID,'event':'uniform_ideal_two_step_phase_tolerance','timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'physical_promotion':0,'summary':'Exact encoded-baseline low-rank residual<6.960e-13 and exact sketch Gram powers certify a nonzero encoding-scale ideal phase ball:δ≤2^-48 per62-vector, unique209matching, circular2step error<2.618e-7. Frozen2^-47HOLD retained; not a failure proof. Fresh cyclic-unit actual floating certificate<9.323e-10rad; separate raw/source replays. v1subquantum2^-49 result and disclosed post-v1 norm refinement retained; savedT0 not assumedexactLS. Uniform floating convergence and independent review remain open; physical promotion0.'},indent=2))
print(json.dumps({'capture':str(out),'total_payload_bytes':sum(p.stat().st_size for p in out.glob('*.zip')),'archives':len(archives)+1,'arrays':len(arrays),'core_sha256':sha(core)}))
