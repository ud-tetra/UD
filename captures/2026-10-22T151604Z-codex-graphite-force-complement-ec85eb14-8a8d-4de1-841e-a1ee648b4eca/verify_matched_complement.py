"""Constructor checks for force-level REBO complement and one-ULP control."""
from pathlib import Path
import json
import math

R=Path(__file__).resolve().parent
out={}
for case in ("21_dir_0","21_dir_10024"):
    j=json.loads((R/f"{case}_matched_complement.json").read_text())
    prior=json.loads((R/f"{case}_runtime_trace.json").read_text())
    methods=j["coordinate_methods"]
    assert methods==["extended_then_cast","binary64_multiply_add","alternating_one_ulp"]
    assert j["unique_points_per_method"]==17
    assert len(j["rows"])==7
    max_closure=0.0
    max_projection_identity=0.0
    for style in methods:
        assert len(j["point_values"][style])==17
        for point in j["point_values"][style].values():
            max_closure=max(max_closure,point["force_closure_max_abs_eV_per_A"])
            max_projection_identity=max(max_projection_identity,abs(point["full"]-point["angle"]-point["rest"]))
    assert max_closure==0.0 and max_projection_identity<5e-16
    max_vs_prior=0.0
    for row,old in zip(j["rows"],prior["rows"]):
        assert row["h_A"]==old["h_A"]
        a,b,c=(row[style] for style in methods)
        assert row["max_coordinate_delta_A"]==0.0
        assert row["complement_stencil_delta_eV_per_A2"]==0.0
        assert a==b
        assert 0.0<row["one_ulp_max_coordinate_delta_A"]<=8e-15
        assert math.isclose(c["rest"]-a["rest"],row["one_ulp_complement_stencil_delta_eV_per_A2"],abs_tol=1e-18)
        assert abs(a["full"]-a["angle"]-a["rest"])<3e-10
        max_vs_prior=max(max_vs_prior,abs(a["rest"]-old["full_minus_direct_eV_per_A2"]))
    middle=next(r for r in j["rows"] if r["h_A"]==2e-5)
    out[case]={"force_level_closure_max_abs_eV_per_A":max_closure,
               "point_projection_identity_max_abs_eV_per_A":max_projection_identity,
               "max_complement_stencil_difference_vs_PR394_eV_per_A2":max_vs_prior,
               "middle_complement_eV_per_A2":middle[methods[0]]["rest"],
               "middle_one_ulp_complement_eV_per_A2":middle[methods[2]]["rest"],
               "middle_one_ulp_shift_eV_per_A2":middle["one_ulp_complement_stencil_delta_eV_per_A2"],
               "middle_one_ulp_max_coordinate_delta_A":middle["one_ulp_max_coordinate_delta_A"]}
(R/"matched_complement_verification.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
