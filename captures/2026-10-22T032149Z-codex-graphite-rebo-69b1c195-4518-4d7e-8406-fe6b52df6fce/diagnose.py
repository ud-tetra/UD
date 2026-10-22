from __future__ import annotations

import ctypes
import hashlib
import json
import os
import sys
from pathlib import Path

import numpy as np
from lammps import lammps

ROOT = Path(os.environ.get("UD_GRAPHITE_ROOT", Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(ROOT / "graphite-boundary-stencil-v02"))
from common import load, positions  # noqa: E402

CASES = {"21_dir_0": (34, 8), "21_dir_10024": (30, 4)}
MODES = ("total", "rebo", "rebo1", "rebo2", "kc")
PLAN = (ROOT / "graphite-boundary-stencil-v02/FREEZE.json")
SOURCE = ROOT / "graphite-boundary-stencil-v02/calculate.py"
OUT = Path(__file__).resolve().parent


def engine(case: str, mode: str) -> lammps:
    pattern, name = case.split("_", 1)
    params = ROOT / "lammps-runtime/lammps/share/lammps/potentials"
    plugin = ROOT / "graphite-width/plugin/kcz_width2.so"
    data = ROOT / "graphite-target-replay/selected" / pattern / name / "struct.inp.data"
    lmp = lammps(cmdargs=["-screen", "none", "-log", str(OUT / f"{case}_{mode}.log")])
    cmds = ["units metal", "boundary p p p", "atom_style full", "box tilt large", f"read_data {data}"]
    if mode in {"total", "kc"}:
        cmds.insert(0, f"plugin load {plugin}")
    if mode == "total":
        cmds += [
            "pair_style hybrid/overlay rebo rebo kolmogorov/crespi/z/smooth 24",
            f"pair_coeff * * rebo 1 {params}/CH.rebo C NULL",
            f"pair_coeff * * rebo 2 {params}/CH.rebo NULL C",
            f"pair_coeff 1 2 kolmogorov/crespi/z/smooth {params}/CC.KC C C",
        ]
    elif mode == "rebo":
        cmds += [
            "pair_style hybrid/overlay rebo rebo",
            f"pair_coeff * * rebo 1 {params}/CH.rebo C NULL",
            f"pair_coeff * * rebo 2 {params}/CH.rebo NULL C",
            "pair_coeff 1 2 none",
        ]
    elif mode in {"rebo1", "rebo2"}:
        cmds += [
            "pair_style hybrid/overlay rebo",
            f"pair_coeff * * rebo {params}/CH.rebo " + ("C NULL" if mode == "rebo1" else "NULL C"),
            "pair_coeff 1 2 none",
            "pair_coeff 2 2 none" if mode == "rebo1" else "pair_coeff 1 1 none",
        ]
    elif mode == "kc":
        cmds += [
            "pair_style hybrid/overlay kolmogorov/crespi/z/smooth 24",
            "pair_coeff 1 1 none",
            "pair_coeff 2 2 none",
            f"pair_coeff 1 2 kolmogorov/crespi/z/smooth {params}/CC.KC C C",
        ]
    else:
        raise ValueError(mode)
    cmds += ["neighbor 3.0 nsq", "neigh_modify one 4096"]
    for command in cmds:
        lmp.command(command)
    return lmp


def sample(lmp: lammps, xx: np.ndarray, flat: np.ndarray) -> np.ndarray:
    xx = np.ascontiguousarray(xx)
    lmp.scatter_atoms("x", 1, 3, xx.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))
    lmp.command("run 0 pre yes post no")
    return flat.T @ np.ctypeslib.as_array(lmp.gather_atoms("f", 1, 3), shape=(3 * len(xx),)).copy()


def main() -> None:
    freeze = json.loads(PLAN.read_text())
    for path, sha in freeze["inputs"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == sha, path
    records = {}
    for case, (j, component) in CASES.items():
        a, basis, _, _ = load(case)
        baseline = a["positions_A"]
        flat = basis.reshape(3 * len(baseline), basis.shape[2])
        plan = np.load(ROOT / "graphite-boundary-stencil-v02" / case / "PLAN.npz")
        disp = np.einsum("nam,m->na", basis, plan["vectors"][j])
        radii = [float(r) for r in plan["radii_A"]]
        points = [("0", baseline)] + [(f"{sign}{h:.12g}", positions(baseline, disp, h if sign == "+" else -h))
                                         for h in radii for sign in ("+", "-")]
        by_mode = {}
        for mode in MODES:
            lmp = engine(case, mode)
            try:
                by_mode[mode] = {key: sample(lmp, pos, flat) for key, pos in points}
            finally:
                lmp.close()
        np.savez_compressed(OUT / f"{case}_projected.npz",
                            modes=np.asarray(MODES),
                            point_keys=np.asarray([key for key, _ in points]),
                            projected_forces=np.stack([[by_mode[mode][key] for key, _ in points]
                                                       for mode in MODES]))
        decomposition = max(float(np.max(abs(by_mode["total"][key] - by_mode["rebo"][key] - by_mode["kc"][key])))
                            for key, _ in points)
        intralayer = max(float(np.max(abs(by_mode["rebo"][key] - by_mode["rebo1"][key] - by_mode["rebo2"][key])))
                         for key, _ in points)
        slopes = {}
        for mode in MODES:
            f = by_mode[mode]
            plus, minus, mean = [], [], []
            for h in (2e-5, 1e-5, 5e-6):
                f0 = f["0"]
                fp = f[f"+{h:.12g}"]
                f2p = f[f"+{2*h:.12g}"]
                fm = f[f"-{h:.12g}"]
                f2m = f[f"-{2*h:.12g}"]
                qp = -(-3 * f0 + 4 * fp - f2p) / (2 * h)
                qm = -(3 * f0 - 4 * fm + f2m) / (2 * h)
                plus.append(qp)
                minus.append(qm)
                mean.append((qp + qm) / 2)
            slopes[mode] = {
                "Qplus_fixed": [float(x[component]) for x in plus],
                "Qminus_fixed": [float(x[component]) for x in minus],
                "side_fixed": [float((x - y)[component]) for x, y in zip(plus, minus)],
                "side_max": [float(np.max(abs(x - y))) for x, y in zip(plus, minus)],
                "middle_average_fixed": float(mean[1][component]),
                "baseline_force_norm": float(np.linalg.norm(f["0"])),
            }
        records[case] = {
            "probe": j,
            "component": component,
            "radii_A": radii,
            "max_absolute_projected_force_decomposition_error_eV_per_A": decomposition,
            "max_absolute_rebo_layer_decomposition_error_eV_per_A": intralayer,
            "modes": slopes,
        }
        print(case, json.dumps(records[case]), flush=True)
    (OUT / "RESULTS.json").write_text(json.dumps(records, indent=2) + "\n")


if __name__ == "__main__":
    main()
