#!/usr/bin/env python3
"""Deterministic UD native-memory/seat-source capture package."""
import base64
import hashlib
import json
import pathlib
import subprocess
import sys
import zipfile

ROOT=pathlib.Path(__file__).resolve().parent
CAPTURE_ID="2026-10-11T014149Z-codex-memory-seat-b7043e45"
STAMP="2026-10-11T014149Z"
BASE="0007c38fb6169d69b9444ebbfe84a31a3c0d8248"
FILES=("REPORT.md","PROTOCOL_v0.2.1_CANDIDATE.md","SOURCE_MANIFEST.json",
       "memory_lift.py","guard_replay.py","memory_results.json","guard_results.json","build_release.py")

def sha(data): return hashlib.sha256(data).hexdigest()
def write_json(name,obj):
    (ROOT/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")

def main():
    for program,out in (("memory_lift.py","memory_results.json"),("guard_replay.py","guard_results.json")):
        s=subprocess.run([sys.executable,str(ROOT/program)],capture_output=True,text=True,check=True)
        write_json(out,json.loads(s.stdout))
    sources={
      "native_generator":"UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md; attached Q165/Q169; local SHA-256 1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63",
      "frame_extractor":"UD_RELATIVE_FRAME_FROM_C1_EXECUTION_v0.7.md; Library libfile_197ff0fbc504819185ef21e9e3ed083f; §§0–5",
      "conditional_co_moving":"UD_PREEVENT_RELATIVE_FRAME_SOURCE_LAW_v0.1.md; Library libfile_f5cc9aef39fc819180ce90b67b7ec4b5; §§2,4–6",
      "receipt_index":"UD_OPEN_SYSTEM_HAMMING_BUDGET_RECEIPT_INDEX_LAW_v0.2 (1).md; Library libfile_8ea519b7af8881918c2d009ce74fe8d8; §§1,3–8",
      "independent_protocol":"UD_OP03_INDEPENDENT_EVENT_ACQUISITION_PROTOCOL_v0.2_RECEIPT_INDEX.md; Library libfile_e56ff2964c8881918c6564d57e9a6a17",
      "authenticated_gate":"UD_OP03_AUTHENTICATED_HELD_OUT_REPLAY_SOURCE_GATE_v0.2.md; Library libfile_32f759d285608191a746627e198f7be7",
      "prior_capture_id":"2026-10-11T013224Z-codex-receipt-eligibility-901e806e",
      "live_site":"https://tetrahedral-packet-complexes.ben-w-mayes.chatgpt.site/; 2026-10-11 current edition Papers I–III 1.1.1, IV 0.1, physical promotion 0"
    }
    write_json("SOURCE_MANIFEST.json",sources)
    zipname="UD_C1_MEMORY_AND_OP03_SEAT_GUARD_v0.1_RELEASE.zip"
    zp=ROOT/zipname
    with zipfile.ZipFile(zp,"w",compression=zipfile.ZIP_DEFLATED) as archive:
        for name in FILES:
            info=zipfile.ZipInfo(name,(1980,1,1,0,0,0))
            info.compress_type=zipfile.ZIP_DEFLATED
            info.external_attr=0o644<<16
            archive.writestr(info,(ROOT/name).read_bytes())
    encoded=ROOT/(zipname+".base64.txt")
    encoded.write_text(base64.b64encode(zp.read_bytes()).decode("ascii")+"\n",encoding="ascii")
    entries=[]
    for name in (*FILES,encoded.name):
        blob=(ROOT/name).read_bytes()
        item={"path":f"captures/{CAPTURE_ID}/{name}","size_bytes":len(blob),"sha256":sha(blob),
              "status":"EXACT scoped memory/seat mathematics; candidate test protocol; independent target OPEN; physical promotion 0"}
        if name==encoded.name:
            item.update({"encoding":"base64 UTF-8 text, decode to ZIP",
                         "decoded_archive_sha256":sha(zp.read_bytes()),
                         "decoded_archive_size_bytes":zp.stat().st_size})
        entries.append(item)
    manifest={"schema_version":1,"capture_id":CAPTURE_ID,"captured_at":STAMP,
      "repository":"ud-tetra/UD","base_commit":BASE,
      "contributor":"Codex for Benjamin Walker Mayes","physical_promotion":0,
      "independent_review":"PENDING","claim_status":"EXACT native memory lift and coordinate-seat audit; candidate protocol; independent event source OPEN",
      "lane":"development — no registry promotion","supersedes":[],
      "scope_amends":["2026-10-11T013224Z-codex-receipt-eligibility-901e806e"],"files":entries}
    write_json("MANIFEST.json",manifest)
    event={"schema_version":1,"event":"native_c1_memory_and_coordinate_seat_guard",
      "capture_id":CAPTURE_ID,"timestamp":STAMP,"contributor":"Codex for Benjamin Walker Mayes",
      "repository":"ud-tetra/UD","base_commit":BASE,"physical_promotion":0,
      "paths_added":len(entries)+2,"supersedes":[],"scope_amends":manifest["scope_amends"],
      "summary":"Exact 12D native memory lift and quarter-step recovery, independent 13,824-case coordinate-seat guard census, candidate v0.2.1 freeze; no independent endpoint scored.",
      "review":"exact internal calculations only; frame occurrence and physical correspondence OPEN",
      "capture_manifest":f"captures/{CAPTURE_ID}/MANIFEST.json",
      "manifest_sha256":sha((ROOT/"MANIFEST.json").read_bytes())}
    write_json("event.json",event)
    print(json.dumps({"capture_id":CAPTURE_ID,"manifest_sha256":event["manifest_sha256"],
                      "zip_sha256":sha(zp.read_bytes()),"files":len(entries)}))

if __name__=="__main__": main()
