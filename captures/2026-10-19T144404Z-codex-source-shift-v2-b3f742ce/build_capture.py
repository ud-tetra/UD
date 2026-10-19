"""Append-only text/code capture; large parent witnesses remain hash-pinned dependencies."""
import datetime,hashlib,json,shutil
from pathlib import Path
P=Path(__file__).resolve().parent
repo=P.parent/'ud-repo'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H%M%SZ')
ID=stamp+'-codex-source-shift-v2-b3f742ce'
out=repo/'captures'/ID
out.mkdir(exist_ok=False)
files=[p for p in P.rglob('*') if p.is_file() and '__pycache__' not in p.parts]
assert all(p.suffix in {'.py','.md','.json','.log','.txt'} for p in files)
for p in sorted(files):
    q=out/p.relative_to(P);q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
readme=out/'README.md';readme.write_text(readme.read_text().replace('CAPTURE_ID',ID))
assert json.loads((out/'executions/clean/REPLAY_RECEIPT.json').read_text())['status']=='PASS_COMPLETE_SAVED_FACTOR_AND_V2_REPLAY'
doc={'capture_id':ID,'status':'THREE_SAVED_OUTPUTS_V2_CERTIFIED_V1_HOLD_PRESERVED_EXTERNAL_PENDING',
     'physical_promotion':0,'extends':['2026-10-19T141834Z-codex-adversarial-admission-ec42d9a1','2026-10-19T134625Z-codex-uniform-output-73b6e18a'],
     'supersedes':[],'verification_scope':'Source-conditioned affine allowance; three known saved outputs; complete new and clean factor replays;13syntheticboundarycontrols; same-team review only. No newSVD/raw/physicalrun or externalreceipt.',
     'files':[{'path':p.relative_to(repo).as_posix(),'size_bytes':p.stat().st_size,'sha256':sha(p),
               'provenance':'Frozen source/maxima, pinned PR212 witnesses, new exact-Arb derivation/replay and sourced unsent reviewer handoff',
               'status':'Development — no registry entry; external review PENDING'}
              for p in sorted(out.rglob('*')) if p.is_file()]}
(out/'MANIFEST.json').write_text(json.dumps(doc,indent=2))
event={'capture_id':ID,'event':'source_conditioned_shift_allowance_v2','timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
       'physical_promotion':0,'summary':'Three known saved PR212 outputs certify under source allowance>5.56320640913e-10; directed phase<3.285772e-7radians/TWOsteps. V1 fixedgateHOLD retained.13controls/cleanfactorreplay pass. Rump proposedprimaryreviewer, unsentrequest, externalreceiptPENDING.'}
(repo/'events'/f'{ID}.json').write_text(json.dumps(event,indent=2))
(P.parent/'SOURCE_SHIFT_CAPTURE_PATH.txt').write_text(str(out))
print(json.dumps({'capture':str(out),'files':len(doc['files']),'bytes':sum(e['size_bytes'] for e in doc['files'])}))
