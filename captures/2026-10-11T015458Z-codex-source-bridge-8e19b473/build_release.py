#!/usr/bin/env python3
"""Build a deterministic, add-only UD capture and evidence receipt."""
import base64
import hashlib
import json
import pathlib
import subprocess
import sys
import zipfile

ROOT=pathlib.Path(__file__).resolve().parent
ID="2026-10-11T015458Z-codex-source-bridge-8e19b473"
STAMP="2026-10-11T015458Z"
BASE="944c65b785f6c03c692c6068ad5a265c10288834"
FILES=("REPORT.md","INPUT_CONTRACT_v0.1_CANDIDATE.md","SOURCE_MANIFEST.json",
       "ACQUISITION_STATUS.json","verify.py","results.json","build_release.py")
ZIP="UD_OBSERVED_FRAME_AND_SEAT_SOURCE_AUDIT_v0.1_RELEASE.zip"

def sha(data): return hashlib.sha256(data).hexdigest()
def write_json(path,obj):
    (ROOT/path).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

def main():
    run=subprocess.run([sys.executable,str(ROOT/"verify.py")],capture_output=True,text=True,check=True)
    write_json("results.json",json.loads(run.stdout))
    src={
      "native_generator":"UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md; attached Q165/Q169; SHA-256 1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63",
      "native_memory":"UD C1 native memory lift capture 2026-10-11T014149Z-codex-memory-seat-b7043e45, REPORT.md §§Exact 12-dimensional native memory lift–Independent finite guard reproduction",
      "frame":"UD_RELATIVE_FRAME_FROM_C1_EXECUTION_v0.7.md; Library libfile_197ff0fbc504819185ef21e9e3ed083f; §§0–5",
      "co_moving":"UD_PREEVENT_RELATIVE_FRAME_SOURCE_LAW_v0.1.md; Library libfile_f5cc9aef39fc819180ce90b67b7ec4b5; §§2,4–6",
      "receipt_index":"UD_OPEN_SYSTEM_HAMMING_BUDGET_RECEIPT_INDEX_LAW_v0.2; Library libfile_8ea519b7af8881918c2d009ce74fe8d8; §§1,3–8",
      "acquisition":"UD_OP03_INDEPENDENT_EVENT_ACQUISITION_PROTOCOL_v0.2_RECEIPT_INDEX.md; Library libfile_e56ff2964c8881918c6564d57e9a6a17; frame through hidden target",
      "source_gate":"UD_OP03_AUTHENTICATED_HELD_OUT_REPLAY_SOURCE_GATE_v0.2.md; Library libfile_32f759d285608191a746627e198f7be7; §§0–5",
      "governance_proposal":"UD_GOVERNANCE_CRL2_SUBDIVISION_v1.0.md; attached; §§1–4; not adopted here",
      "site":"https://tetrahedral-packet-complexes.ben-w-mayes.chatgpt.site/; fetched 2026-10-11, Papers I–III 1.1.1/IV 0.1, physical promotion 0"
    }
    write_json("SOURCE_MANIFEST.json",src)
    with zipfile.ZipFile(ROOT/ZIP,"w",compression=zipfile.ZIP_DEFLATED) as archive:
        for name in FILES:
            info=zipfile.ZipInfo(name,(1980,1,1,0,0,0))
            info.compress_type=zipfile.ZIP_DEFLATED
            info.external_attr=0o644<<16
            archive.writestr(info,(ROOT/name).read_bytes())
    encoded=ZIP+".base64.txt"
    (ROOT/encoded).write_text(base64.b64encode((ROOT/ZIP).read_bytes()).decode("ascii")+"\n",encoding="ascii")
    entries=[]
    for name in (*FILES,encoded):
        blob=(ROOT/name).read_bytes()
        entry={"path":f"captures/{ID}/{name}","size_bytes":len(blob),"sha256":sha(blob),
               "status":"exact conditional algebra and finite implementation; candidate input contract; independent target NOT_RUN; physical promotion 0"}
        if name==encoded:
            entry.update({"encoding":"base64 UTF-8 text, decode to ZIP","decoded_archive_sha256":sha((ROOT/ZIP).read_bytes()),"decoded_archive_size_bytes":(ROOT/ZIP).stat().st_size})
        entries.append(entry)
    manifest={"schema_version":1,"capture_id":ID,"captured_at":STAMP,"repository":"ud-tetra/UD",
      "base_commit":BASE,"contributor":"Codex for Benjamin Walker Mayes","physical_promotion":0,
      "independent_review":"PENDING","lane":"development — no registry entry","supersedes":[],
      "scope_amends":["2026-10-11T014149Z-codex-memory-seat-b7043e45"],
      "claim_status":"EXACT conditional frame/seat certificates; producer and independent target OPEN", "files":entries}
    write_json("MANIFEST.json",manifest)
    event={"schema_version":1,"event":"observed_frame_and_lineage_seat_source_boundary",
      "capture_id":ID,"timestamp":STAMP,"contributor":"Codex for Benjamin Walker Mayes",
      "repository":"ud-tetra/UD","base_commit":BASE,"physical_promotion":0,
      "paths_added":len(entries)+2,"supersedes":[],"scope_amends":manifest["scope_amends"],
      "summary":"Conditional 12D-to-C1 frame certificate and exact coordinate-span seat test; no independent producer or target acquired.",
      "review":"non-constructor review pending; no predictive switch or physical claim",
      "capture_manifest":f"captures/{ID}/MANIFEST.json","manifest_sha256":sha((ROOT/"MANIFEST.json").read_bytes())}
    write_json("event.json",event)
    print(json.dumps({"capture_id":ID,"zip_sha256":sha((ROOT/ZIP).read_bytes()),
                      "manifest_sha256":event["manifest_sha256"],"files":len(entries)}))

if __name__=="__main__": main()
