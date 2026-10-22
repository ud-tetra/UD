"""Match archived first-layer projected forces to a fresh fixed-geometry replay.

Diagnostic only: coordinate construction and force summation can differ from
the frozen archive. This script compares them pointwise and propagates their
observed difference through the held signed stiffness side stencil.
"""
from pathlib import Path
import ctypes
import json
import numpy as np
from lammps import lammps

R = Path(__file__).resolve().parent
out = {}
for case, probe, comp, name in (
    ("21_dir_0", 34, 8, "dir_0"),
    ("21_dir_10024", 30, 4, "dir_10024"),
):
    cand = np.load(R / f"{case}_candidate.npz")
    x = cand["positions_A"]
    B = cand["B_extended"]
    direction = B[:, :, probe]
    flat = B.reshape(-1, 81)
    arch = np.load(R / "ud-sync/graphite-analysis" / f"{case}_projected.npz")
    ar = arch["projected_forces"][list(arch["modes"]).index("rebo1")]
    keys = list(arch["point_keys"])
    data = R / "graphite-target-replay/selected/21" / name / "struct.inp.data"
    params = R / "lammps-runtime/lammps/share/lammps/potentials/CH.rebo"
    l = lammps(cmdargs=["-screen", "none", "-log", "none"])
    try:
        for command in (
            "units metal", "boundary p p p", "atom_style full", "box tilt large",
            f"read_data {data}", "pair_style hybrid/overlay rebo",
            f"pair_coeff * * rebo {params} C NULL", "pair_coeff 1 2 none",
            "pair_coeff 2 2 none", "neighbor 3.0 nsq", "neigh_modify one 4096",
        ):
            l.command(command)
        samples = {}
        for i, key in enumerate(keys):
            t = float(key)
            xx = np.ascontiguousarray(np.asarray(
                x.astype(np.longdouble) + np.longdouble(t)*direction.astype(np.longdouble),
                dtype=np.float64))
            l.scatter_atoms("x", 1, 3, xx.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))
            l.command("run 0 pre yes post no")
            force = np.ctypeslib.as_array(l.gather_atoms("f", 1, 3), shape=(3*len(x),)).copy()
            replay = float((flat.T @ force)[comp])
            archive = float(ar[i, comp])
            samples[key] = {"archive_eV_per_A": archive,
                            "replay_eV_per_A": replay,
                            "delta_replay_minus_archive_eV_per_A": replay-archive}
        rows = []
        for h in (2e-5, 1e-5, 5e-6):
            kk = ("0", f"+{h:.12g}", f"+{2*h:.12g}", f"-{h:.12g}", f"-{2*h:.12g}")
            assert set(kk) <= set(samples)
            def stencil(field):
                f0, fp, f2p, fm, f2m = (samples[k][field] for k in kk)
                return (6*f0-4*fp+f2p-4*fm+f2m)/(2*h)
            d = [samples[k]["delta_replay_minus_archive_eV_per_A"] for k in kk]
            worst = max(abs(v) for v in d)
            actual = stencil("delta_replay_minus_archive_eV_per_A")
            bound = 8*worst/h
            archived = stencil("archive_eV_per_A")
            replay = stencil("replay_eV_per_A")
            assert abs(replay-archived-actual) < 1e-10
            assert abs(actual) <= bound*(1+1e-8)
            rows.append({"h_A":h,"point_keys":kk,"delta_at_points_eV_per_A":d,
                         "archive_S_eV_per_A2":archived,"replay_S_eV_per_A2":replay,
                         "observed_replay_minus_archive_S_eV_per_A2":actual,
                         "max_point_abs_delta_eV_per_A":worst,
                         "triangle_bound_on_abs_S_difference_eV_per_A2":bound})
        out[case] = {"probe":probe,"component":comp,"samples":samples,"rows":rows}
    finally:
        l.close()
(R/"point_error_budget.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({c:[{"h":r["h_A"],"observed":r["observed_replay_minus_archive_S_eV_per_A2"],"bound":r["triangle_bound_on_abs_S_difference_eV_per_A2"]} for r in v["rows"]] for c,v in out.items()},indent=2))
