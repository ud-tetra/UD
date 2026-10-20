"""Seal only this append-only capture; preserve any hydration leftovers."""
import hashlib,json,shutil,subprocess,uuid
from pathlib import Path
R=Path('/workspace/scratch/1544cec576c6');REPO=R/'ud-repo';SITE=R/'ud-public'
C=REPO/'captures/2026-10-20T140000Z-codex-finite-calibration-f4b96720'
for rel in subprocess.check_output(['git','ls-files','-o','--exclude-standard','-z'],cwd=REPO).decode().split('\0'):
    if not rel or rel.startswith('captures/'+C.name+'/') or rel=='events/'+C.name+'.json':continue
    p=REPO/rel
    assert p.name.startswith('.') and any(t in p.name for t in ('.part-','.part00.','.zip.','.npz.')),rel
    assert subprocess.run(['git','ls-files','--error-unmatch',rel],cwd=REPO,capture_output=True).returncode!=0
    out=R/'clone-download-recovery'/rel;out.parent.mkdir(parents=True,exist_ok=True)
    if out.exists():out=out.with_name(out.name+'.copy-'+uuid.uuid4().hex[:8])
    shutil.move(p,out)
(C/'SITE_SOURCE_CHANGE.patch').write_bytes(subprocess.check_output(['git','diff','--binary','78db53a4e47d296e0d604fba164a28a0b0bbcc09','HEAD'],cwd=SITE))
shutil.copy2(SITE/'dist/sources/finite-calibration-v0.1/SITE_VALIDATION_v0.1.json',C/'SITE_VALIDATION_v0.1.json')
for name in ['prepare_finite_capture.py','publish_finite.py','check_finite_site.py','seal_finite.py']:shutil.copy2(R/name,C/name)
event={'event_id':C.name,'capture_id':C.name,'type':'finite-calibration-and-short-window-fault-certificate','status':'DERIVED_CONDITIONAL_APPARATUS_OPEN','physical_promotion':0,'description':'Finite-cover residual theorem and obstruction, active-port commands, controller-age budget, exact Gauss fault gaps; six-page manuscript, symbolic verification and seven arithmetic controls. No experiment.'}
(REPO/'events'/f'{C.name}.json').write_text(json.dumps(event,indent=2)+'\n')
files=[{'path':p.relative_to(REPO).as_posix(),'size_bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(C.iterdir()) if p.is_file() and p.name!='MANIFEST.json']
manifest={'capture_id':C.name,'status':'DERIVED CONDITIONAL / APPARATUS BOUNDS OPEN / INDEPENDENT REVIEW PENDING','physical_promotion':0,'provenance':{'origin':'User: continue next steps after CAM/CD-1','constructor':'Codex','reviewers':[],'repo_derivation_base':'8bfcbd64848212cc12833df4b3f9a6e143474a96','publication_base':subprocess.check_output(['git','rev-parse','HEAD'],cwd=REPO,text=True).strip(),'site_source_base':'78db53a4e47d296e0d604fba164a28a0b0bbcc09','site_source_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=SITE,text=True).strip(),'lane':'development; no registry entry'},'verification_scope':'Exact symbolic Hamiltonian/source/propagator identities and conservative norm majorants; seven exact rational controls; six-page visual PDF QA; static Site checks. Constructor verification only.','scope_limits':['All apparatus inputs are illustrative supplied bounds, not measurements','Only short-window Gauss discriminator certified conditionally','No full CD-1 horizon or SDW endpoint admission','No apparatus execution or independent review','No physical or GUT promotion'],'supersedes':[],'extends':['captures/2026-10-20T133000Z-codex-canonical-diamond-6d82a19f'],'files':files}
(C/'MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'capture_id':C.name,'manifest_files':len(files)}))
