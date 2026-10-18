from pathlib import Path
import json,zipfile,hashlib,datetime,shutil
P=Path(__file__).resolve().parent;repo=P.parent/'ud-repo';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();ID=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H%M%SZ')+'-codex-record-contract-5b1e8a94';out=repo/'captures'/ID;out.mkdir(exist_ok=False);large=set(P.rglob('*.npz'));groups=[];g=[];size=0
for p in sorted(large):
 assert p.stat().st_size<9000000
 if g and size+p.stat().st_size>9000000:groups.append(g);g=[];size=0
 g.append(p);size+=p.stat().st_size
if g:groups.append(g)
arrays=[];archives=[]
for i,g in enumerate(groups,1):
 a=out/f'WITNESS_{i:02d}.zip'
 with zipfile.ZipFile(a,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
  for p in g:z.write(p,p.relative_to(P).as_posix());arrays.append({'path':p.relative_to(P).as_posix(),'size_bytes':p.stat().st_size,'sha256':sha(p),'archive':a.name})
 assert a.stat().st_size<12000000;archives.append({'filename':a.name,'size_bytes':a.stat().st_size,'sha256':sha(a)})
(P/'WITNESS_INDEX.json').write_text(json.dumps({'status':'ALL_AVAILABLE_ARCHIVED_ARRAYS_EXACT_GRAMS_AND_PROPOSALS_RETAINED','physical_promotion':0,'arrays':arrays,'archives':archives},indent=2))
files=[p for p in P.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p not in large and p.name!='PACKAGE_MANIFEST.json']
(P/'PACKAGE_MANIFEST.json').write_text(json.dumps({'artifact':'UD_RECORD_WISE_FLOATING_PHASE_CONTRACT_v0.1','physical_promotion':0,'files':[{'path':p.relative_to(P).as_posix(),'size_bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(files)]},indent=2));files.append(P/'PACKAGE_MANIFEST.json');core=out/'UD_RECORD_WISE_FLOATING_PHASE_CONTRACT_v0.1_CORE.zip'
with zipfile.ZipFile(core,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for p in sorted(files):z.write(p,p.relative_to(P).as_posix())
assert core.stat().st_size<12000000
for p in P.iterdir():
 if p.is_file() and p.suffix in ['.py','.md','.json','.txt']:shutil.copyfile(p,out/p.name)
entries=[{'path':p.relative_to(repo).as_posix(),'size_bytes':p.stat().st_size,'sha256':sha(p),'status':'Record-wise actual floating certificate on two archived eligible controls; outside-ball HOLD preserved','provenance':'New exact raw-projected sketch and archived-array verification; no new estimator runs or independent review'} for p in sorted(out.iterdir())]
(out/'MANIFEST.json').write_text(json.dumps({'capture_id':ID,'physical_promotion':0,'status':'RECORD_WISE_FLOATING_PHASE_CONTRACT_VERIFIED','supersedes':[],'extends':['2026-10-18T192301Z-codex-uniform-two-step-8a71c9d3'],'verification_scope':'Three archived raw eligibility checks and replays; two exact raw-projected sketch Gram replays; two actual saved-array phase certificate replays; four counterfactual negative controls; zero new proposer runs. Baseline/cyclic phase bounds<1.268e-8/<1.691e-8 radians per2steps. Dense-unit raw HOLD despite previous phase PASS. Uniform floating convergence, original full-Hankel/noise contracts and independent review remain open.','files':entries},indent=2))
(repo/'events'/f'{ID}.json').write_text(json.dumps({'capture_id':ID,'event':'record_wise_floating_phase_admission','timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'physical_promotion':0,'summary':'Frozen raw-noise, exact321-column sketch-fit and actual polar-alignment/shift/eigenpair/argument contract passes archived baseline and cyclic-unit; bounds<1.268e-8/<1.691e-8 circularrad/2steps. Dense-unit remains raw-ballHOLD while priorphasePASS preserved. Two exact raw Gram and two actual phase replays; four negative checks; no new proposer run or uniform convergence claim. Same-team review only; development lane.'},indent=2))
print(json.dumps({'capture':str(out),'archives':len(archives)+1,'arrays':len(arrays),'total_payload_bytes':sum(p.stat().st_size for p in out.glob('*.zip')),'core_sha256':sha(core)}))
