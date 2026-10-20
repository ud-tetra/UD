"""Seal this immutable clock/plant capture and preserve clone temporaries."""
import hashlib,json,shutil,subprocess,uuid
from pathlib import Path
R=Path('/workspace/scratch/1544cec576c6');REPO=R/'ud-repo';SITE=R/'ud-public'
C=REPO/'captures/2026-10-20T180500Z-codex-clock-plant-c4d128b7'
for rel in subprocess.check_output(['git','ls-files','-o','--exclude-standard','-z'],cwd=REPO).decode().split('\0'):
    if not rel or rel.startswith('captures/'+C.name+'/') or rel=='events/'+C.name+'.json':continue
    p=REPO/rel
    assert p.name.startswith('.') and any(t in p.name for t in ('.part-','.part00.','.zip.','.npz.')),rel
    assert subprocess.run(['git','ls-files','--error-unmatch',rel],cwd=REPO,capture_output=True).returncode!=0
    out=R/'clone-download-recovery'/rel;out.parent.mkdir(parents=True,exist_ok=True)
    if out.exists():out=out.with_name(out.name+'.copy-'+uuid.uuid4().hex[:8])
    shutil.move(p,out)
(C/'SITE_SOURCE_CHANGE.patch').write_bytes(subprocess.check_output(['git','diff','--binary','f9368b468e8dc78f3c07fa0cbf91b5020fc3b356','HEAD'],cwd=SITE))
shutil.copy2(SITE/'dist/sources/clock-plant-v0.1/SITE_VALIDATION_v0.1.json',C/'SITE_VALIDATION_v0.1.json')
for name in ['prepare_clock_capture.py','publish_clock.py','check_clock_site.py','seal_clock.py']:shutil.copy2(R/name,C/name)
event={'event_id':C.name,'capture_id':C.name,'type':'clock-plant-compatibility-and-component-screen','status':'DERIVED_CONDITIONAL_HARDWARE_HOLD','physical_promotion':0,'description':'Clock/plant compatibility and filtered-readout theorems, alternate error allocation, supplier audit and identification plan; ten exact controls plus inherited SAC/FCAL replay. No hardware admission or experiment.'}
(REPO/'events'/f'{C.name}.json').write_text(json.dumps(event,indent=2)+'\n')
files=[{'path':p.relative_to(REPO).as_posix(),'size_bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(C.iterdir()) if p.is_file() and p.name!='MANIFEST.json']
manifest={'capture_id':C.name,'status':'DERIVED CONDITIONAL / CANDIDATE COMPONENT ROUTE / HARDWARE HOLD / INDEPENDENT REVIEW PENDING','physical_promotion':0,'provenance':{'origin':'User: continue next steps after sampled-actuator theorem','constructor':'Codex','reviewers':[],'repo_derivation_base':'d01945104084db51877ff15df8fff890120771be','publication_base':subprocess.check_output(['git','rev-parse','HEAD'],cwd=REPO,text=True).strip(),'site_source_base':'f9368b468e8dc78f3c07fa0cbf91b5020fc3b356','site_source_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=SITE,text=True).strip(),'lane':'development; no registry entry'},'verification_scope':'Analytic clock-product and filtered-history proofs, conservative budget obstruction, ten exact rational controls, inherited SAC/FCAL replay, four-page visual PDF QA and static Site checks. Manufacturer screen uses primary data sheets; constructor verification only.','scope_limits':['No actual hardware observations or component admission','Manufacturer limits retain their operating conditions','Certificate obstruction is not physical impossibility','No full campaign or SDW endpoint admission','No experiment or independent review','No physical/GUT promotion'],'supersedes':[],'extends':['captures/2026-10-20T163500Z-codex-sampled-actuator-9c71de42'],'files':files}
(C/'MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'capture_id':C.name,'manifest_files':len(files)}))
