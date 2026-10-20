"""Seal this append-only capture with hashes and publication provenance."""
import hashlib,json,shutil,subprocess,uuid
from pathlib import Path
R=Path('/workspace/scratch/1544cec576c6');REPO=R/'ud-repo';SITE=R/'ud-public'
C=REPO/'captures/2026-10-20T163500Z-codex-sampled-actuator-9c71de42'
for rel in subprocess.check_output(['git','ls-files','-o','--exclude-standard','-z'],cwd=REPO).decode().split('\0'):
    if not rel or rel.startswith('captures/'+C.name+'/') or rel=='events/'+C.name+'.json':continue
    p=REPO/rel
    assert p.name.startswith('.') and any(t in p.name for t in ('.part-','.part00.','.zip.','.npz.')),rel
    assert subprocess.run(['git','ls-files','--error-unmatch',rel],cwd=REPO,capture_output=True).returncode!=0
    out=R/'clone-download-recovery'/rel;out.parent.mkdir(parents=True,exist_ok=True)
    if out.exists():out=out.with_name(out.name+'.copy-'+uuid.uuid4().hex[:8])
    shutil.move(p,out)
(C/'SITE_SOURCE_CHANGE.patch').write_bytes(subprocess.check_output(['git','diff','--binary','a8847b287e6648a9a3e84c4fe29eba611fdbcfb0','HEAD'],cwd=SITE))
shutil.copy2(SITE/'dist/sources/sampled-actuator-v0.1/SITE_VALIDATION_v0.1.json',C/'SITE_VALIDATION_v0.1.json')
for name in ['prepare_sampled_capture.py','publish_sampled.py','check_sampled_site.py','seal_sampled.py']:shutil.copy2(R/name,C/name)
event={'event_id':C.name,'capture_id':C.name,'type':'sampled-controller-finite-bandwidth-actuator-certificate','status':'DERIVED_CONDITIONAL_APPARATUS_OPEN','physical_promotion':0,'description':'Sampled controller/actuator theorem, explicit residual allocation, preload and saturation bounds, component/instrument contract; nine exact controls and inherited Gauss replay. No experiment.'}
(REPO/'events'/f'{C.name}.json').write_text(json.dumps(event,indent=2)+'\n')
files=[{'path':p.relative_to(REPO).as_posix(),'size_bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(C.iterdir()) if p.is_file() and p.name!='MANIFEST.json']
manifest={'capture_id':C.name,'status':'DERIVED CONDITIONAL / CANDIDATE IMPLEMENTATION / APPARATUS OPEN / INDEPENDENT REVIEW PENDING','physical_promotion':0,'provenance':{'origin':'User: continue next steps after finite calibration','constructor':'Codex','reviewers':[],'repo_derivation_base':'73d23f983f54a0dc5a5c986f5410513e5f3fe937','publication_base':subprocess.check_output(['git','rev-parse','HEAD'],cwd=REPO,text=True).strip(),'site_source_base':'a8847b287e6648a9a3e84c4fe29eba611fdbcfb0','site_source_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=SITE,text=True).strip(),'lane':'development; no registry entry'},'verification_scope':'Analytic first-order tracking and barrier arguments; nine exact rational controls with Taylor startup bound; source-bound Gauss-budget replay; four-page PDF visual QA; static Site checks. Constructor verification only.','scope_limits':['All hardware numbers are supplied design bounds, not measured capabilities','Actual model identification and calibration OPEN','No physical component selection or experiment','Only short Gauss-discriminator prefix, not full campaign or SDW admission','No physical/GUT promotion'],'supersedes':[],'extends':['captures/2026-10-20T140000Z-codex-finite-calibration-f4b96720'],'files':files}
(C/'MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'capture_id':C.name,'manifest_files':len(files)}))
