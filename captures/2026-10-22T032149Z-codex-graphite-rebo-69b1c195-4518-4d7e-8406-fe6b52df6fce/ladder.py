import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from diagnose import ROOT, CASES, engine, sample, load, positions  # noqa: E402

H = [8e-5, 4e-5, 2e-5, 1e-5, 5e-6, 2.5e-6, 1.25e-6]


def angular_cosines(x, b, nei):
    # Exact same fixed-neighbor representation as the earlier geometry check.
    bb = b + (x - x0)[nei] - (x - x0)[:, None, :]
    unit = bb / np.linalg.norm(bb, axis=2)[:, :, None]
    return np.stack([np.sum(unit[:, i] * unit[:, j], axis=1) for i, j in ((0, 1), (0, 2), (1, 2))], axis=1)


result = {}
for case, (probe, comp) in CASES.items():
    a, basis, nei, b = load(case)
    x0 = a["positions_A"]
    flat = basis.reshape(3 * len(x0), basis.shape[2])
    plan = np.load(ROOT / "graphite-boundary-stencil-v02" / case / "PLAN.npz")
    direction = np.einsum("nam,m->na", basis, plan["vectors"][probe])
    lmp = engine(case, "rebo")
    try:
        f0 = sample(lmp, x0, flat)
        cos0 = angular_cosines(x0, b, nei)
        details = []
        raw = []
        for h in H:
            xp = positions(x0, direction, h)
            x2p = positions(x0, direction, 2*h)
            xm = positions(x0, direction, -h)
            x2m = positions(x0, direction, -2*h)
            fp = sample(lmp, xp, flat)
            f2p = sample(lmp, x2p, flat)
            fm = sample(lmp, xm, flat)
            f2m = sample(lmp, x2m, flat)
            raw.append(np.stack((fp, f2p, fm, f2m)))
            qp = -(-3*f0+4*fp-f2p)/(2*h)
            qm = -(3*f0-4*fm+f2m)/(2*h)
            cp = angular_cosines(xp, b, nei)
            cm = angular_cosines(xm, b, nei)
            input_plus = np.linalg.norm((-3*x0.astype(np.longdouble)+4*xp.astype(np.longdouble)-x2p.astype(np.longdouble))/(2*np.longdouble(h))-direction)
            input_minus = np.linalg.norm((3*x0.astype(np.longdouble)-4*xm.astype(np.longdouble)+x2m.astype(np.longdouble))/(2*np.longdouble(h))-direction)
            details.append({"h_A":h,"side_fixed_eV_per_A2":float((qp-qm)[comp]),
                            "Qplus_fixed":float(qp[comp]),"Qminus_fixed":float(qm[comp]),
                            "max_input_direction_error":float(max(input_plus,input_minus)),
                            "C2_knot_baseline_count_abs_1e-12":int(np.sum(abs(cos0+0.5)<1e-12)),
                            "C2_knot_plus_vs_minus_branch_count":int(np.sum((cp >= -.5)!=(cm >= -.5))),
                            "C2_knot_near_samples_1e-8":int(np.sum(abs(cp+0.5)<1e-8)+np.sum(abs(cm+0.5)<1e-8))})
    finally:
        lmp.close()
    np.savez_compressed(HERE / f"{case}_ladder_raw.npz", baseline=f0,
                        steps_A=np.asarray(H), projected_forces=np.stack(raw))
    result[case] = {"probe":probe,"component":comp,"step_ladder":details}
    print(case, json.dumps(details),flush=True)
(HERE/"LADDER.json").write_text(json.dumps(result,indent=2)+"\n")
