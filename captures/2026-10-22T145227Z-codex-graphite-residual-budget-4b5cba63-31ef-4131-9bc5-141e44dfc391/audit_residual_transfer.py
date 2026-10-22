"""Deterministic sensitivity audit for the held graphite first-layer stencils.

All numerical bounds refer to two archived/replayed arrays at the same named
offsets. They are not a probability model or a bound on physical friction.
"""
from pathlib import Path
import json
import numpy as np

R = Path(__file__).resolve().parent
point = json.loads((R / "point_error_budget.json").read_text())
report = {}
for case, data in point.items():
    runtime = json.loads((R / f"{case}_runtime_trace.json").read_text())
    records = np.load(R / f"{case}_runtime_middle_records.npz")
    py_records = np.load(R / f"{case}_python_middle_records.npz")
    assert np.array_equal(records["ids_1based"], py_records["ids_1based"])
    archived = np.load(R / f"{case}_projected.npz")
    keys = list(archived["point_keys"])
    ref = archived["projected_forces"][list(archived["modes"]).index("rebo1")]
    for key, sample in data["samples"].items():
        assert abs(sample["archive_eV_per_A"]-ref[keys.index(key),data["component"]])<1e-15
    rows = []
    for row in data["rows"]:
        h = row["h_A"]
        delta = np.array(row["delta_at_points_eV_per_A"])
        weights = np.array([6,-4,1,-4,1],dtype=np.float64)/(2*h)
        # Triangle bound is conditional on the maximum of these five observed
        # point differences; it is not a global solver-accuracy guarantee.
        actual = float(weights @ delta)
        epsilon = float(np.max(abs(delta)))
        triangle = epsilon*float(np.sum(abs(weights)))
        assert np.isclose(actual,row["observed_replay_minus_archive_S_eV_per_A2"],atol=1e-15,rtol=0)
        assert np.isclose(triangle,row["triangle_bound_on_abs_S_difference_eV_per_A2"],atol=1e-15,rtol=0)
        assert abs(actual)<=triangle
        rrun=next(x for x in runtime["rows"] if x["h_A"]==h)
        residual=rrun["full_minus_direct_eV_per_A2"]
        assert abs(rrun["runtime_full_S_eV_per_A2"]-row["replay_S_eV_per_A2"])<1e-9
        rows.append({
            "h_A":h,
            "observed_replay_minus_archive_S_eV_per_A2":actual,
            "observed_max_point_delta_eV_per_A":epsilon,
            "conditional_triangle_bound_eV_per_A2":triangle,
            "runtime_full_minus_direct_S_eV_per_A2":residual,
            "required_uniform_point_error_below_eV_per_A_to_resolve_runtime_remainder_by_this_bound":abs(residual)/float(np.sum(abs(weights))),
            "bound_over_runtime_remainder":triangle/abs(residual) if residual else None,
        })
    h=2e-5
    def s(terms):
        v=np.sum(terms,axis=0)
        return float(np.array([6,-4,1,-4,1])@v/(2*h))
    cpp=s(records["projected_force_eV_per_A"])
    python=s(py_records["projected_force_eV_per_A"])
    report[case]={"probe":data["probe"],"component":data["component"],
                  "rows":rows,
                  "middle_runtime_direct_angle_S_eV_per_A2_from_summed_forces":cpp,
                  "middle_python_direct_angle_S_eV_per_A2_from_summed_forces":python,
                  "middle_runtime_minus_python_direct_angle_S_eV_per_A2":cpp-python,
                  "status":"NUMERICAL_TRANSFER_NOT_A_FRICTION_OR_LOAD_BOUND"}
(R/"residual_transfer_audit.json").write_text(json.dumps(report,indent=2)+"\n")
print(json.dumps({case:{"rows":v["rows"],"runtime_minus_python":v["middle_runtime_minus_python_direct_angle_S_eV_per_A2"]} for case,v in report.items()},indent=2))
