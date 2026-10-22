#!/usr/bin/env python3
"""Test a LAMMPS KC/z-style pair cutoff shift, without claiming archive provenance."""
import contextlib, hashlib, io, json, runpy, sys
from pathlib import Path
import numpy as np

archive_path=Path(sys.argv[1])
expected="b1ccf62a3e75928e1382cbdd6c669b99675fef9ad5f077e79057a142a0a07875"
with archive_path.open("rb") as f:
    assert hashlib.file_digest(f,"sha256").hexdigest()==expected
repo=Path(__file__).resolve().parents[2]
old=repo/"captures/2026-10-22T224639Z-codex-graphite-material-projection-fcd6e90e-4531aa0e-8487-4d43-b0dd-cfe246d1b6b4/derive_graphite_source_projection.py"
sys.argv=[str(old),str(archive_path)]
with contextlib.redirect_stdout(io.StringIO()):
    d=runpy.run_path(str(old))  # trusted repository-owned derivation; archive programs never executed
rc=16.0
original=d["pair_fields"](3.46,rc)[:,0]
counts=np.array([np.sum((rho+3.46**2)<rc**2)/len(d["top"]) for rho in d["rho2"]])
shift_mev=d["A"]*(d["z0"]/rc)**6
source=d["Z"]
def comparison(field):
    return {"mean_difference_mev_per_atom":float(np.mean(field-source)),
            "centered_rms_difference_microev_per_atom":float(1000*np.std(field-source))}
result={"source_archive_sha256":expected,"cutoff_angstrom":rc,"pair_shift_mev":shift_mev,
        "pair_count_per_atom_min_max_mean":[float(counts.min()),float(counts.max()),float(counts.mean())],
        "unshifted":comparison(original),"shifted":comparison(original+shift_mev*counts),
        "status":"conditional convention check; does not identify source simulation"}
print(json.dumps(result,indent=2))
