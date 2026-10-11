#!/usr/bin/env python3
"""Create the source-hashed connected-seam development release."""
import hashlib
import json
import zipfile
from pathlib import Path

root = Path(__file__).resolve().parent
names = ("REPORT.md", "verify.py", "results.json", "ACQUISITION_STATUS.json")
manifest = {
    "schema": "UD-CONNECTED-SEAM-BOUNDARY-RELEASE-v0.1",
    "date_utc": "2026-10-11",
    "provenance": {
        "attached_ledger_sha256": "1281aa8454013fbbdbcf8ada07af0aefe81014003f25a27f3929ad43afffae63",
        "attached_governance_proposal_sha256": "8e9e8159fe2e5c4bdc234712e02db0151fc77f4a92c140372279a1e9717689a4",
        "hard_gate": "UD_EDGE_CLOSURE_AND_TRANSPORT_INTEGRITY_HARD_GATE_DERIVATION_v0.1.md §§I–IV, 2026-08-21",
        "isometry_gate": "UD_JOP_WORKING_MANUSCRIPT_THROUGH_SECTION11_v1.2_JOINT_REPLAY_GOVERNED.md §6.2, 2026-08-30",
        "newborn_seam": "UD_COFACE_NEWBORN_PACKET_TRANSPORT_INHERITANCE_AND_FORMATION_DEBIT_RECEIPT_TESTBED_v0.1.md §§1–5, 2026-10-03",
        "theta_lift": "UD_THETA_TRANSPORT_LIFT_v0.1.md §§2,4,6,11–12, 2026-08-30",
        "op03": "UD_OP03_INDEPENDENT_EVENT_ACQUISITION_PROTOCOL_v0.1.md, 2026-08-30",
    },
    "claim": "EXACT conditional phase integrity and connected-to-discrete obstruction; no native seam generator",
    "independent_event_history_scored": False,
    "physical_promotion": 0,
    "files": [{
        "name": name,
        "size_bytes": (root / name).stat().st_size,
        "sha256": hashlib.sha256((root / name).read_bytes()).hexdigest(),
    } for name in names],
}
path = root / "SOURCE_MANIFEST.json"
path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
archive = root / "UD_CONNECTED_SEAM_EVENT_BOUNDARY_v0.1_RELEASE.zip"
with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as z:
    for name in (*names, path.name):
        info = zipfile.ZipInfo(name, date_time=(2026, 10, 11, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o644 << 16
        z.writestr(info, (root / name).read_bytes())
print(json.dumps({
    "release": archive.name,
    "size_bytes": archive.stat().st_size,
    "sha256": hashlib.sha256(archive.read_bytes()).hexdigest(),
}))
