#!/usr/bin/env python3
"""Build a deterministic add-only UD capture and verify its SHA manifest."""
import base64
import hashlib
import json
import pathlib
import subprocess
import sys
import zipfile

ROOT=pathlib.Path(__file__).resolve().parent
CAPTURE_ID="2026-10-11T012338Z-codex-frame-boundary-fc4d4c2a"
FILES=("REPORT.md","ACQUISITION_STATUS.json","SOURCE_MANIFEST.json","verify.py","results.json","build_release.py")

def sha(data):
    return hashlib.sha256(data).hexdigest()

def write_json(name,obj):
    (ROOT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

def main():
    run=subprocess.run([sys.executable,str(ROOT/"verify.py")],capture_output=True,text=True,check=True)
    write_json("results.json",json.loads(run.stdout))
    sources={
      "primary_frame":"UD_RELATIVE_FRAME_FROM_C1_EXECUTION_v0.7.md; Library libfile_197ff0fbc504819185ef21e9e3ed083f; §§0–5,7–10",
      "manuscript_reconciliation":"UD_JOP_WORKING_MANUSCRIPT_THROUGH_SECTION11_v1.2_JOINT_REPLAY_GOVERNED.md; Library libfile_8b9461fba6248191bb6d58dcf977a977; §7.R6",
      "conditional_alternative":"UD_PREEVENT_RELATIVE_FRAME_SOURCE_LAW_v0.1.md; Library libfile_f5cc9aef39fc819180ce90b67b7ec4b5; §§2,4–6,9–13",
      "independent_protocol":"UD_OP03_INDEPENDENT_EVENT_ACQUISITION_PROTOCOL_v0.1.md; Library libfile_30fb9c2688f08191acb9119bfdb6a2f4",
      "synthetic_control":"UD_OP03_JOINT_REPLAY_EXECUTION_v0.9.md; Library libfile_de1a3ebc085c8191a78c966bd723cd7a; §§1,4–9",
      "local_ledger":{"name":"UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md","sections":"Q169","sha256":"1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63"},
      "prior_capture_ids":["2026-10-10T164734Z-codex-native-static-null-b71cb9e8","2026-10-11T010749Z-codex-native-projection-c9c95ae7","2026-10-11T011622Z-codex-connected-seam-84c4d102","2026-10-10T165944Z-codex-op03-intake-ed488bce"]
    }
    write_json("SOURCE_MANIFEST.json",sources)
    zipname="UD_C1_FRAME_BOUNDARY_AND_OP03_INTAKE_v0.1_RELEASE.zip"
    zp=ROOT/zipname
    with zipfile.ZipFile(zp,"w",compression=zipfile.ZIP_DEFLATED) as z:
        for name in FILES:
            info=zipfile.ZipInfo(name,(1980,1,1,0,0,0))
            info.compress_type=zipfile.ZIP_DEFLATED
            info.external_attr=0o644<<16
            z.writestr(info,(ROOT/name).read_bytes())
    encoded=ROOT/(zipname+".base64.txt")
    encoded.write_text(base64.b64encode(zp.read_bytes()).decode("ascii")+"\n",encoding="ascii")
    entries=[]
    for name in (*FILES,encoded.name):
        blob=(ROOT/name).read_bytes()
        record={"path":f"captures/{CAPTURE_ID}/{name}","size_bytes":len(blob),"sha256":sha(blob),
                "status":"EXACT conditional diagnostic / OP03 NO_DATA / physical promotion 0"}
        if name==encoded.name:
            record.update({"encoding":"base64 UTF-8 text, decode to ZIP","decoded_archive_sha256":sha(zp.read_bytes()),"decoded_archive_size_bytes":zp.stat().st_size})
        entries.append(record)
    manifest={"schema_version":1,"capture_id":CAPTURE_ID,"captured_at":"2026-10-11T012338Z",
      "repository":"ud-tetra/UD","base_commit":"5103dc67697d0ea8399d2bed5f76c29e5f964b66",
      "contributor":"Codex for Benjamin Walker Mayes","physical_promotion":0,
      "independent_review":"PENDING","claim_status":"EXACT conditional frame boundary; source bridge OPEN; OP03 NO_DATA",
      "lane":"development — no registry promotion","supersedes":[],
      "scope_amends":["2026-10-11T011622Z-codex-connected-seam-84c4d102"],"files":entries}
    write_json("MANIFEST.json",manifest)
    event={"schema_version":1,"event":"pre_event_c1_frame_boundary_scope_amendment",
       "capture_id":CAPTURE_ID,"timestamp":"2026-10-11T012338Z",
       "contributor":"Codex for Benjamin Walker Mayes","repository":"ud-tetra/UD",
       "base_commit":manifest["base_commit"],"physical_promotion":0,"paths_added":len(entries)+2,
       "summary":"Existing v0.7 exact frame gate and v0.1 conditional alternative diverge on a native chain-compression diagnostic; neither supplies a Theta event. Independent OP03 target absent.",
       "review":"exact algebraic replay only; no held-out history or physical promotion",
       "supersedes":[],"scope_amends":manifest["scope_amends"],
       "capture_manifest":f"captures/{CAPTURE_ID}/MANIFEST.json", "manifest_sha256":sha((ROOT/"MANIFEST.json").read_bytes())}
    write_json("event.json",event)
    print(json.dumps({"capture_id":CAPTURE_ID,"manifest_sha256":event["manifest_sha256"],"zip_sha256":sha(zp.read_bytes()),"files":len(entries)}))

if __name__=="__main__":
    main()
