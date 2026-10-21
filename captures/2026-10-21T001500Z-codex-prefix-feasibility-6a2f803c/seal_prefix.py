"""Seal the append-only prefix-feasibility capture."""
import hashlib,json,shutil,subprocess,uuid
from pathlib import Path
R=Path('/workspace/scratch/1544cec576c6');REPO=R/'ud-repo';SITE=R/'ud-public'
C=REPO/'captures/2026-10-21T001500Z-codex-prefix-feasibility-6a2f803c'
for rel in subprocess.check_output(['git','ls-files','-o','--exclude-standard','-z'],cwd=REPO).decode().split('\0'):
    if not rel or rel.startswith('captures/'+C.name+'/') or rel=='events/'+C.name+'.json':continue
    p=REPO/rel
    assert p.name.startswith('.') and any(t in p.name for t in ('.part-','.part00.','.zip.','.npz.')),rel
    assert subprocess.run(['git','ls-files','--error-unmatch',rel],cwd=REPO,capture_output=True).returncode!=0
    out=R/'clone-download-recovery'/rel;out.parent.mkdir(parents=True,exist_ok=True)
    if out.exists():out=out.with_name(out.name+'.copy-'+uuid.uuid4().hex[:8])
    shutil.move(p,out)
(C/'SITE_SOURCE_CHANGE.patch').write_bytes(subprocess.check_output(['git','diff','--binary','ebdf1ab2447a86a8b0225758214b2b7119abe6d9','HEAD'],cwd=SITE))
shutil.copy2(SITE/'dist/sources/prefix-feasibility-v0.1/SITE_VALIDATION_v0.1.json',C/'SITE_VALIDATION_v0.1.json')
for n in ['prepare_prefix_capture.py','publish_prefix.py','check_prefix_site.py','seal_prefix.py']:shutil.copy2(R/n,C/n)
event={'event_id':C.name,'capture_id':C.name,'type':'local-prefix-certificate-and-clock-compatible-component-route','status':'DERIVED_CONDITIONAL_HARDWARE_HOLD','physical_promotion':0,'description':'Exact local Hamiltonian majorants and closed prefix barrier; clock overlap8/575<t0<=1/48 sec with series-loss plant; example residual0.00962; screened component route with calibration/identification gates. No experiment.'}
(REPO/'events'/f'{C.name}.json').write_text(json.dumps(event,indent=2)+'\n')
files=[{'path':p.relative_to(REPO).as_posix(),'size_bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(C.iterdir()) if p.is_file() and p.name!='MANIFEST.json']
manifest={'capture_id':C.name,'status':'DERIVED CONDITIONAL / CANDIDATE CLOCK-COMPATIBLE ROUTE / HARDWARE HOLD / INDEPENDENT REVIEW PENDING','physical_promotion':0,'provenance':{'origin':'User: continue next steps after clock-plant theorem','constructor':'Codex','reviewers':[],'repo_derivation_base':'fa8176d24e45f2d30bca2b0f2bc9e669988e1892','publication_base':subprocess.check_output(['git','rev-parse','HEAD'],cwd=REPO,text=True).strip(),'site_source_base':'ebdf1ab2447a86a8b0225758214b2b7119abe6d9','site_source_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=SITE,text=True).strip(),'lane':'development; no registry entry'},'verification_scope':'Exact symbolic preparation-box majorants; analytic state/tracking barrier; twelve exact arithmetic controls including negative clocks and conditional noise union bound; five-page visual PDF QA; static Site checks. Primary supplier screen only, constructor verification only.','scope_limits':['Short preparation prefix only','Actual operating-band parameters and residuals OPEN','Supplier limits do not establish noise tails or low-voltage leakage','No complete firmware/driver implementation admitted','No experiment or independent review','No full campaign, SDW or physical/GUT promotion'],'supersedes':[],'extends':['captures/2026-10-20T180500Z-codex-clock-plant-c4d128b7'],'files':files}
(C/'MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'capture_id':C.name,'manifest_files':len(files)}))
