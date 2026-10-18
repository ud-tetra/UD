"""Seal an append-only research capture; retain local hydration leftovers outside its clean worktree."""
import hashlib,json,subprocess,shutil
from pathlib import Path
R=Path('/workspace/scratch/1544cec576c6');repo=R/'ud-audit-repo'
cap=repo/'captures/2026-10-18T141800Z-codex-measurable-audit-a7c392e1'
leftovers=[
'captures/2026-10-07T191951Z-codex-ud-bootstrap-5170f8b8/snapshots/library/.part-0031.bin.wiWmgA',
'captures/2026-10-07T191951Z-codex-ud-bootstrap-5170f8b8/snapshots/portal/.part-0008.bin.sjhcPo',
'captures/2026-10-17T181003Z-codex-noisy-proposal-6371dfe9/observer-work/codec/.LOSSLESS_RESIDUAL.npz.uXLIN3',
'captures/2026-10-18T014757Z-codex-operator-norm-c1a73e06/.WITNESS_dense_sign_float.zip.moCma8']
for rel in leftovers:
    p=repo/rel
    if not p.exists():continue
    assert subprocess.run(['git','ls-files','--error-unmatch',rel],cwd=repo,capture_output=True).returncode!=0
    dst=R/'hydration-recovery'/rel;dst.parent.mkdir(parents=True,exist_ok=True)
    assert not dst.exists();shutil.move(p,dst)
site=R/'ud-public'
patch=subprocess.check_output(['git','diff','--binary','71a506bde7360ecebf581b274ad4de12c7759916','HEAD'],cwd=site)
(cap/'SITE_SOURCE_CHANGE.patch').write_bytes(patch)
shutil.copy2(site/'dist/sources/measurable-audit-v0.1/SITE_VALIDATION_v0.1.json',cap/'SITE_VALIDATION_v0.1.json')
qa={'status':'PASS','pages':6,'all_pages_rendered_and_visually_inspected':True,'clipping_overlap_or_missing_text_observed':False,'physical_promotion':0}
(cap/'PDF_QA_v0.1.json').write_text(json.dumps(qa,indent=2)+'\n')
event={'event_id':cap.name,'capture_id':cap.name,'type':'measurable-realization-and-published-dataset-audit','status':'CANDIDATE_AND_DATASET_SCOPED','physical_promotion':0,'description':'Rank-one rotor-matter circuit candidate; one complete published waveform content audit and two atomic data comparators; no physical certification.'}
(repo/'events'/f'{cap.name}.json').write_text(json.dumps(event,indent=2)+'\n')
def seal():
    files=[{'path':p.relative_to(repo).as_posix(),'size_bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(cap.iterdir()) if p.is_file() and p.name!='MANIFEST.json']
    m={'capture_id':cap.name,'status':'CANDIDATE REALIZATION / DATASET-SCOPED CONTENT AUDIT / INDEPENDENT REVIEW PENDING','physical_promotion':0,'provenance':{'origin':'User: select a measurable realization and audit published datasets','constructor':'Codex','reviewers':[],'repo_base':'57c90583afae95fa8f91ce607194a507edbbf456','site_source_base':'71a506bde7360ecebf581b274ad4de12c7759916','site_source_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=site,text=True).strip()},'verification_scope':'One complete waveform content parser, published MD5/size match; 71+13 file metadata inventory; three CSV and one figure-table content inspections; six-page PDF visual QA and static Site checks. Constructor verification only.','scope_limits':['No all-file or all-figure replay','No apparatus or UD theorem admission','No fitted confidence interval or experiment performed','No GUT/Standard Model inference','No change to nominal action or coefficient ledger'],'supersedes':[],'files':files}
    (cap/'MANIFEST.json').write_text(json.dumps(m,indent=2)+'\n')
seal()
print(json.dumps({'capture_id':cap.name,'files':len(json.loads((cap/'MANIFEST.json').read_text())['files'])}))
