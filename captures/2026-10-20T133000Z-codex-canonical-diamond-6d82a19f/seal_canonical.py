"""Append-only capture inventory and recovery of this checkout's download leftovers."""
import hashlib,json,shutil,subprocess,uuid
from pathlib import Path
R=Path('/workspace/scratch/1544cec576c6');REPO=R/'ud-repo';SITE=R/'ud-public'
C=REPO/'captures/2026-10-20T133000Z-codex-canonical-diamond-6d82a19f'
untracked=subprocess.check_output(['git','ls-files','-o','--exclude-standard','-z'],cwd=REPO).decode().split('\0')
for rel in untracked:
    if not rel or rel.startswith('captures/'+C.name+'/') or rel=='events/'+C.name+'.json':continue
    p=REPO/rel
    # These are download/hydration temporaries created by the current fresh clone.
    # Preserve every byte outside the repository; never include them as source evidence.
    assert p.name.startswith('.') and any(t in p.name for t in ('.part-','.part00.','.zip.','.npz.')),rel
    assert subprocess.run(['git','ls-files','--error-unmatch',rel],cwd=REPO,capture_output=True).returncode!=0
    out=R/'clone-download-recovery'/rel;out.parent.mkdir(parents=True,exist_ok=True)
    if out.exists():
        out=out.with_name(out.name+'.copy-'+uuid.uuid4().hex[:8])
    shutil.move(p,out)
patch=subprocess.check_output(['git','diff','--binary','61b58f7e4fc8bd9b59cdf64acc37c135a90448dd','HEAD'],cwd=SITE)
(C/'SITE_SOURCE_CHANGE.patch').write_bytes(patch)
shutil.copy2(SITE/'dist/sources/canonical-map-v0.1/SITE_VALIDATION_v0.1.json',C/'SITE_VALIDATION_v0.1.json')
event={'event_id':C.name,'capture_id':C.name,'type':'canonical-apparatus-map-and-closed-diamond-test','status':'DERIVED_CONDITIONAL_AND_PROPOSED_COMPONENT','physical_promotion':0,'description':'Common-action canonical map, Gauss/source identities and CD-1 proposed protocol; 64 exact constructor checks. Dataset release watch configured. No experiment executed.'}
(REPO/'events'/f'{C.name}.json').write_text(json.dumps(event,indent=2)+'\n')
files=[{'path':p.relative_to(REPO).as_posix(),'size_bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(C.iterdir()) if p.is_file() and p.name!='MANIFEST.json']
manifest={'capture_id':C.name,'status':'DERIVED CONDITIONAL / CANDIDATE APPARATUS / PROPOSED CD-1 / INDEPENDENT REVIEW PENDING','physical_promotion':0,'provenance':{'origin':'User requested dataset watch, canonical apparatus-to-model map and one instrumented closed-diamond test','constructor':'Codex','reviewers':[],'repo_base':'0dc7dd79f565063ff198f3cade3e0548b8577c52','site_source_base':'61b58f7e4fc8bd9b59cdf64acc37c135a90448dd','site_source_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=SITE,text=True).strip(),'lane':'development; no registry entry'},'verification_scope':'64 exact symbolic checks of Hamiltonian/map/current/Gauss/source/control identities; analytic proof; eight-page PDF visual QA and Site static link/source checks. Constructor verification only.','scope_limits':['Actual physical canonical variables and Hamiltonian matching require calibration','No apparatus execution or independent review','Diamond component does not inherit tetrahedral trapping constants','Engineering thresholds do not replace endpoint precision gates','No physical/GUT promotion'],'supersedes':[],'files':files}
(C/'MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'capture_id':C.name,'manifest_files':len(files)}))
