#!/usr/bin/env python3
"""Build source-hashed reproducible release, without touching earlier captures."""
import hashlib
import json
import zipfile
from pathlib import Path

root = Path(__file__).resolve().parent
names = ("REPORT.md", "verify.py", "results.json", "ACQUISITION_STATUS.json")
manifest = {
    "schema": "UD-NATIVE-PROJECTION-BOUNDARY-RELEASE-v0.1",
    "date_utc": "2026-10-11",
    "provenance": {
        "ledger": "UD_COEFFICIENT_PROVENANCE_LEDGER_v0.39(2).md Q156/Q167/Q169/Q173",
        "hard_gate": "UD_EDGE_CLOSURE_AND_TRANSPORT_INTEGRITY_HARD_GATE_DERIVATION_v0.1.md §§II–IV, 2026-08-21",
        "specialization": "UD_JOP_WORKING_MANUSCRIPT_THROUGH_SECTION11_v1.2_JOINT_REPLAY_GOVERNED.md §6.2, 2026-08-30",
        "frozen_null": "ud-tetra/UD capture 2026-10-10T164734Z-codex-native-static-null-b71cb9e8",
        "op03": "UD_OP03_INDEPENDENT_EVENT_ACQUISITION_PROTOCOL_v0.1.md, 2026-08-30",
    },
    "claim": "EXACT conditional native edge projection, NO-GO universal transport identification",
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
archive = root / "UD_NATIVE_PROJECTION_BOUNDARY_v0.1_RELEASE.zip"
with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as z:
    for name in (*names, path.name):
        zi = zipfile.ZipInfo(name, date_time=(2026, 10, 11, 0, 0, 0))
        zi.compress_type = zipfile.ZIP_DEFLATED
        zi.external_attr = 0o644 << 16
        z.writestr(zi, (root / name).read_bytes())
print(json.dumps({
    "release": archive.name,
    "size_bytes": archive.stat().st_size,
    "sha256": hashlib.sha256(archive.read_bytes()).hexdigest(),
}))
