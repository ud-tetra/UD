from pathlib import Path
import json,hashlib,zipfile,datetime,shutil
P=Path(__file__).resolve().parent;repo=P.parent/'ud-repo';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ID=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H%M%SZ')+'-codex-timing-preparation-6c93e12a';out=repo/'captures'/ID;out.mkdir(parents=True,exist_ok=False)
files=[p for p in P.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.name!='PACKAGE_MANIFEST.json']
(P/'PACKAGE_MANIFEST.json').write_text(json.dumps({'artifact':'UD_PREPARATION_CLOCK_BUDGET_v0.1','physical_promotion':0,'independent_review':'pending','files':[{'path':p.relative_to(P).as_posix(),'size_bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(files)]},indent=2));files.append(P/'PACKAGE_MANIFEST.json')
core=out/'UD_PREPARATION_CLOCK_BUDGET_v0.1.zip'
with zipfile.ZipFile(core,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for p in sorted(files):z.write(p,p.relative_to(P).as_posix())
assert core.stat().st_size<12000000
for p in P.iterdir():
 if p.is_file() and p.suffix in ['.py','.md','.json','.txt']:shutil.copyfile(p,out/p.name)
entries=[{'path':p.relative_to(repo).as_posix(),'size_bytes':p.stat().st_size,'sha256':sha(p),'status':'EXACT conditional theorem/no-go; constructor validated source margins/grids and replay, as typed in CLAIM_LEDGER.json','provenance':'Frozen known-reference ideal-estimator budget grids, exact right-inverse/Gram residuals and same-team mathematical review; independent review pending'} for p in sorted(out.iterdir())]
(out/'MANIFEST.json').write_text(json.dumps({'capture_id':ID,'physical_promotion':0,'status':'CONDITIONAL_PREPARATION_CLOCK_BUDGET_CERTIFICATE','supersedes':[],'extends':['2026-10-18T020014Z-codex-frame-span-7b29c641','2026-10-18T154341Z-codex-new-seeds-f2a8d310'],'verification_scope':'Learned temporal excitation margin and74 conditional exact-estimator budget rows plus joint example; six exact/validated control families and eight tests; same-team parallel review only. No new raw acquisition, actual floating convergence, full-Hankel proof, SI clock or physical promotion.','files':entries},indent=2))
(repo/'events'/f'{ID}.json').write_text(json.dumps({'capture_id':ID,'event':'conditional_preparation_clock_budget_and_identifiability_limits','timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'physical_promotion':0,'summary':'Validated learned temporal excitation gamma>0.0012130785174; preparation p<gamma and declared common-clock jitter/rate bounds transport to exact-SVD phase gates.74 frozen rows and a joint example replay; joint error<1.791e-5 radians/sample. Alias jitter and clock-scale no-go, preparation-specific rank-loss controls retained. Two same-team reviews, six control families and eight tests; independent review and metrology inputs remain open.'},indent=2))
print(json.dumps({'capture':str(out),'archive_sha256':sha(core),'archive_bytes':core.stat().st_size,'core_files':len(files)}))
