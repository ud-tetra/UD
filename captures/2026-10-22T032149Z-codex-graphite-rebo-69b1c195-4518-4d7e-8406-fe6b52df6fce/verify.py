import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
report = json.loads((HERE / "RESULTS.json").read_text())
ladder = json.loads((HERE / "LADDER.json").read_text())
original = {"21_dir_0": 7.265001257117376e-5,
            "21_dir_10024": 7.78066277096201e-5}
out = {}
for case in original:
    data = np.load(HERE / f"{case}_projected.npz")
    keys = list(data["point_keys"])
    modes = list(data["modes"])
    arr = data["projected_forces"]
    assert modes == ["total", "rebo", "rebo1", "rebo2", "kc"]
    assert arr.shape == (5, 9, 81)
    error = float(np.max(abs(arr[0] - arr[1] - arr[4])))
    layer_error = float(np.max(abs(arr[1] - arr[2] - arr[3])))
    assert error < 2e-15
    assert layer_error < 2e-15
    assert abs(error-report[case]["max_absolute_projected_force_decomposition_error_eV_per_A"]) < 1e-16
    assert abs(layer_error-report[case]["max_absolute_rebo_layer_decomposition_error_eV_per_A"]) < 1e-16
    component = report[case]["component"]
    def get(mode, label):
        return arr[modes.index(mode),keys.index(label)]
    def side(mode,h):
        f0=get(mode,"0");fp=get(mode,f"+{h:.12g}");f2p=get(mode,f"+{2*h:.12g}")
        fm=get(mode,f"-{h:.12g}");f2m=get(mode,f"-{2*h:.12g}")
        return -(-3*f0+4*fp-f2p)/(2*h)+(3*f0-4*fm+f2m)/(2*h)
    for m in modes:
        for i,h in enumerate((2e-5,1e-5,5e-6)):
            assert abs(side(m,h)[component]-report[case]["modes"][m]["side_fixed"][i])<1e-12
    assert abs(abs(side("total",2e-5)[component])-original[case])<2e-12
    trace = np.load(HERE / f"{case}_ladder_raw.npz")
    assert len(trace["steps_A"])==7 and trace["projected_forces"].shape==(7,4,81)
    for i,(h, samples) in enumerate(zip(trace["steps_A"],trace["projected_forces"])):
        f0=trace["baseline"];fp,f2p,fm,f2m=samples
        qp=-(-3*f0+4*fp-f2p)/(2*h)
        qm=-(3*f0-4*fm+f2m)/(2*h)
        assert abs(float((qp-qm)[component])-ladder[case]["step_ladder"][i]["side_fixed_eV_per_A2"])<1e-12
    out[case]={"raw_decomposition_error_eV_per_A":error,
               "raw_rebo_layer_decomposition_error_eV_per_A":layer_error,
               "original_worst_probe_replayed":True,
               "ladder_rows_replayed":7}
print(json.dumps({"status":"PASS_CONSTRUCTOR_RAW_REPLAY","cases":out},indent=2))
