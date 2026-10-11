#!/usr/bin/env python3
"""Deterministic add-only acquisition source audit capture."""
import base64
import hashlib
import json
import pathlib
import subprocess
import sys
import zipfile

ROOT=pathlib.Path(__file__).resolve().parent
SOURCE=ROOT.parent/'source_candidate'/'UD_OP03_KBS_PURPOSE_BUILT_BENCH_v0.2.zip'
ID='2026-10-11T020241Z-codex-op03-producer-handoff-23f7e091'
STAMP='2026-10-11T020241Z'
BASE='ce397b64ad8ddf2f4c16812db94cc803c7cd25ce'
ZIP='UD_OP03_INDEPENDENT_PRODUCER_HANDOFF_v0.1_RELEASE.zip'
FILES=('REPORT.md','PROVIDER_HANDOFF_v0.1.md','SOURCE_AUDIT.json',
       'SOURCE_MANIFEST.json','verify_archive.py','results.json','build_release.py')
def sha(b): return hashlib.sha256(b).hexdigest()
def dump(name,obj): (ROOT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
def main():
    run=subprocess.run([sys.executable,str(ROOT/'verify_archive.py'),str(SOURCE)],capture_output=True,text=True,check=True)
    dump('results.json',json.loads(run.stdout))
    dump('SOURCE_MANIFEST.json',{
      'bench':'UD_OP03_KBS_PURPOSE_BUILT_BENCH_v0.2.zip; Library libfile_ceb05c2a86308191a6244df532953d03; README.md, protocol/V0_2_STATE.json, contracts/EVENT_ENGINE_HANDOFF_CONTRACT.md, templates/ENGINE_COMMIT_TEMPLATE.json; SHA-256 e1fb3c2c53ce7caf50bcf748d1d211fee4e39a379e116d895c3d8e57d7cb9b65',
      'nested':'protocol/UD_OP03_DUAL_LANE_ACQUISITION_v0.1.zip within bench; ACQUISITION_MANIFEST.json, README.md, CUSTODY_WORKFLOW.md; SHA-256 1edce616734021ff780ab3a6a759b5b4c3ab4cbf692eec6ef05c28486b1aba17',
      'full_protocol':'UD_OP03_INDEPENDENT_EVENT_ACQUISITION_PROTOCOL_v0.2_RECEIPT_INDEX.md; Library libfile_e56ff2964c8881918c6564d57e9a6a17; Pre-event frame packet–Hidden target packet',
      'authenticated_gate':'UD_OP03_AUTHENTICATED_HELD_OUT_REPLAY_SOURCE_GATE_v0.2.md; Library libfile_32f759d285608191a746627e198f7be7; §§0–5',
      'prior_bridge':'UD capture 2026-10-11T015458Z-codex-source-bridge-8e19b473, REPORT.md and INPUT_CONTRACT_v0.1_CANDIDATE.md',
      'prior_intake':'UD capture 2026-10-10T165944Z-codex-op03-intake-ed488bce; README.md, intake.py',
      'governance_proposal':'UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md; attached; §§1–4; not adopted here'
    })
    with zipfile.ZipFile(ROOT/ZIP,'w',compression=zipfile.ZIP_DEFLATED) as z:
        for name in FILES:
            info=zipfile.ZipInfo(name,(1980,1,1,0,0,0))
            info.compress_type=zipfile.ZIP_DEFLATED
            info.external_attr=0o644<<16
            z.writestr(info,(ROOT/name).read_bytes())
    encoded=ZIP+'.base64.txt'
    (ROOT/encoded).write_text(base64.b64encode((ROOT/ZIP).read_bytes()).decode('ascii')+'\n',encoding='ascii')
    entries=[]
    for name in (*FILES,encoded):
        b=(ROOT/name).read_bytes()
        e={'path':f'captures/{ID}/{name}','size_bytes':len(b),'sha256':sha(b),
           'status':'archived-source acquisition audit; zero real events; no full OP03 target; physical promotion 0'}
        if name==encoded: e.update({'encoding':'base64 UTF-8 text, decode to ZIP',
                                  'decoded_archive_sha256':sha((ROOT/ZIP).read_bytes()),
                                  'decoded_archive_size_bytes':(ROOT/ZIP).stat().st_size})
        entries.append(e)
    m={'schema_version':1,'capture_id':ID,'captured_at':STAMP,'repository':'ud-tetra/UD','base_commit':BASE,
       'contributor':'Codex for Benjamin Walker Mayes','physical_promotion':0,
       'independent_review':'PENDING','lane':'development — no registry entry',
       'claim_status':'SOURCE_BLOCKED / NO_DATA / NOT_RUN; provider handoff prepared',
       'supersedes':[],'scope_amends':['2026-10-11T015458Z-codex-source-bridge-8e19b473'],'files':entries}
    dump('MANIFEST.json',m)
    event={'schema_version':1,'event':'op03_producer_acquisition_source_audit','capture_id':ID,
      'timestamp':STAMP,'contributor':'Codex for Benjamin Walker Mayes','repository':'ud-tetra/UD',
      'base_commit':BASE,'physical_promotion':0,'paths_added':len(entries)+2,
      'supersedes':[],'scope_amends':m['scope_amends'],
      'summary':'Inspected v0.2 bench and nested dual-lane package; both state zero real events. Full OP03 provider handoff prepared; no independent source or target scored.',
      'review':'independent producer and non-constructor adversarial review pending',
      'capture_manifest':f'captures/{ID}/MANIFEST.json','manifest_sha256':sha((ROOT/'MANIFEST.json').read_bytes())}
    dump('event.json',event)
    print(json.dumps({'capture_id':ID,'zip_sha256':sha((ROOT/ZIP).read_bytes()),
                      'manifest_sha256':event['manifest_sha256'],'files':len(entries)}))
if __name__=='__main__': main()
