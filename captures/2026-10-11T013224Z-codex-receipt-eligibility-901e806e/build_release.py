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
CAPTURE_ID="2026-10-11T013224Z-codex-receipt-eligibility-901e806e"
FILES=("REPORT.md","ACQUISITION_STATUS.json","SOURCE_MANIFEST.json","verify.py","results.json","build_release.py")

def sha(data):
    return hashlib.sha256(data).hexdigest()

def write_json(name,obj):
    (ROOT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

def main():
    run=subprocess.run([sys.executable,str(ROOT/"verify.py")],capture_output=True,text=True,check=True)
    write_json("results.json",json.loads(run.stdout))
    sources={
      "primary_receipt_index":"UD_OPEN_SYSTEM_HAMMING_BUDGET_RECEIPT_INDEX_LAW_v0.2 (1).md; Library libfile_8ea519b7af8881918c2d009ce74fe8d8; §§1,3–8,12–13",
      "independent_arithmetic_audit":"UD_HAMMING_BUDGET_RECEIPT_INDEX_INDEPENDENT_AUDIT_v0.1.json; Library libfile_f8791a67b2a8819185cd7dd98d28504d",
      "frame_input":"UD_RELATIVE_FRAME_FROM_C1_EXECUTION_v0.7.md; Library libfile_197ff0fbc504819185ef21e9e3ed083f; §§0–5",
      "independent_protocol":"UD_OP03_INDEPENDENT_EVENT_ACQUISITION_PROTOCOL_v0.2_RECEIPT_INDEX.md; Library libfile_e56ff2964c8881918c6564d57e9a6a17",
      "independent_schema":"UD_OP03_INDEPENDENT_EVENT_ACQUISITION_SCHEMA_v0.2_RECEIPT_INDEX.json; Library libfile_65d6302675688191baefd0a7d73d6e20",
      "authenticated_source_gate":"UD_OP03_AUTHENTICATED_HELD_OUT_REPLAY_SOURCE_GATE_v0.2.md; Library libfile_32f759d285608191a746627e198f7be7",
      "synthetic_control":"UD_OP03_JOINT_REPLAY_EXECUTION_v0.9.md; Library libfile_de1a3ebc085c8191a78c966bd723cd7a; §2.3",
      "local_ledger":{"name":"UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md","sections":"Q169","sha256":"1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63"},
      "prior_capture_ids":["2026-10-11T012338Z-codex-frame-boundary-fc4d4c2a","2026-10-11T010749Z-codex-native-projection-c9c95ae7","2026-10-10T165944Z-codex-op03-intake-ed488bce"]
    }
    write_json("SOURCE_MANIFEST.json",sources)
    zipname="UD_OP03_RECEIPT_ELIGIBILITY_AND_TYPED_SEATS_v0.1_RELEASE.zip"
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
                "status":"EXACT scoped counterexamples / amendment CANDIDATE / OP03 NO_DATA / physical promotion 0"}
        if name==encoded.name:
            record.update({"encoding":"base64 UTF-8 text, decode to ZIP","decoded_archive_sha256":sha(zp.read_bytes()),"decoded_archive_size_bytes":zp.stat().st_size})
        entries.append(record)
    manifest={"schema_version":1,"capture_id":CAPTURE_ID,"captured_at":"2026-10-11T013224Z",
      "repository":"ud-tetra/UD","base_commit":"25d5cc8348bbda11ba57f9d7f5af30a65108f77e",
      "contributor":"Codex for Benjamin Walker Mayes","physical_promotion":0,
      "independent_review":"PENDING","claim_status":"EXACT scoped receipt-index counterexamples; v0.2.1 repair CANDIDATE; OP03 NO_DATA",
      "lane":"development — no registry promotion","supersedes":[],
      "scope_amends":["2026-10-11T012338Z-codex-frame-boundary-fc4d4c2a"],"files":entries}
    write_json("MANIFEST.json",manifest)
    event={"schema_version":1,"event":"op03_receipt_index_eligibility_scope_amendment",
       "capture_id":CAPTURE_ID,"timestamp":"2026-10-11T013224Z",
       "contributor":"Codex for Benjamin Walker Mayes","repository":"ud-tetra/UD",
       "base_commit":manifest["base_commit"],"physical_promotion":0,"paths_added":len(entries)+2,
       "summary":"Exact v0.2 first-admissibility no-op and typed-seat endpoint counterexamples; native C1 restriction obstruction; v0.2.1 repair candidate; independent OP03 target absent.",
       "review":"exact algebraic replay only; no held-out history or physical promotion",
       "supersedes":[],"scope_amends":manifest["scope_amends"],
       "capture_manifest":f"captures/{CAPTURE_ID}/MANIFEST.json", "manifest_sha256":sha((ROOT/"MANIFEST.json").read_bytes())}
    write_json("event.json",event)
    print(json.dumps({"capture_id":CAPTURE_ID,"manifest_sha256":event["manifest_sha256"],"zip_sha256":sha(zp.read_bytes()),"files":len(entries)}))

if __name__=="__main__":
    main()
