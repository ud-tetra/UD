#!/usr/bin/env python3
"""Read-only audit replay. No network, raw archives, model fits or hardware."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
HERE=Path(__file__).resolve().parent
def read(name): return json.loads((HERE/name).read_text())
def main():
    inv=read("RAW_METADATA_INVENTORY.json")
    rows=inv["records"]
    assert len(rows)==32 and len({x["persistent_id"] for x in rows})==32
    assert all(x["bytes"]>0 and x["checksum"]["type"]=="MD5"
               and len(x["checksum"]["value"])==32 for x in rows)
    ten=[x for x in rows if "CH10-" in x["path"]]
    assert len(ten)==2
    freeze=read("CANDIDATE_INTAKE_FREEZE.json")
    assert freeze["already_exposed"] in ten and freeze["candidate"] in ten
    assert freeze["already_exposed"]!=freeze["candidate"]
    assert freeze["candidate"]["persistent_id"]=="doi:10.11588/DATA/6MEKHI/NH8JC2"
    assert freeze["candidate"]["bytes"]==81386005
    assert freeze["candidate"]["checksum"]["value"]=="3fc592443a1c117ab4a9503e01d5a92c"
    assert freeze["raw_records_opened_this_audit"]==0
    inp=read("INPUT_BINDINGS.json")
    for x in inp["inputs"]:
        p=Path(x["path"])
        if not p.is_file():
            raise AssertionError("Declared original input unavailable; no invented PASS")
        b=p.read_bytes()
        assert len(b)==x["bytes"] and hashlib.sha256(b).hexdigest()==x["sha256"]
    original=next(x for x in inp["inputs"] if x["path"].endswith("TEMPLATE_PREFLIGHT_HOLD.json"))
    pre=json.loads(Path(original["path"]).read_text())
    mapped=read("BLOCKER_MAP.json")
    assert len(mapped["entries"])==128
    assert [x["original_blocker"] for x in mapped["entries"]]==pre["blocking_metadata"]
    assert all(x["status"]=="UNRESOLVED_QUALIFICATION_EVIDENCE"
               and x["request_modified"] is False for x in mapped["entries"])
    f0=F(125000000,64)
    assert f0==1953125 and 1/f0==F(512,10**9)
    exact_times={16384:F(8388608,10**9),16383:F(8388096,10**9),
                 16184:F(8286208,10**9),16183:F(8285696,10**9)}
    assert all(F(n)/f0==t for n,t in exact_times.items())
    # Independent rational edge checks of both signs; algebraic proof is in note.
    clock_checks=0
    for rho in [F(0),F(1,10**6),F(1,100),F(9,10)]:
        for e in [-rho,F(0),rho]:
            assert abs(1/(1+e)-1)<=rho/(1-rho)
            clock_checks+=1
    result={"status":"PASS","raw_metadata_rows":32,"ten_channel_labels":2,
            "unchanged_qualification_blockers":128,
            "exact_nominal_sample_rate_Hz":str(f0),
            "exact_duration_identities_checked":4,
            "rational_clock_edge_checks":clock_checks,
            "timing_lemma_status":"DERIVED_CONDITIONAL_NOT_CALIBRATION",
            "new_raw_downloads":0,"raw_records_opened":0,"new_fits":0,
            "physical_promotion":0}
    print(json.dumps(result,indent=2))
if __name__=="__main__": main()

