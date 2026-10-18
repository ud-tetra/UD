#!/usr/bin/env python3
import json, sys, hashlib
import numpy as np
from pathlib import Path

TOL = 1e-10
CONTROL_TOL = 1e-8

R = np.diag([1,1,1,-1,-1,-1]).astype(float)
J = np.block([[np.zeros((3,3)), -np.eye(3)],
              [np.eye(3), np.zeros((3,3))]])
S = np.block([[np.zeros((3,3)), np.eye(3)],
              [np.eye(3), np.zeros((3,3))]])

def infnorm(M):
    return float(np.max(np.abs(M)))

def classify(case):
    W = np.array(case["W"], dtype=float)
    T = np.array(case["T_H"], dtype=float)
    Theta = np.array(case["Theta_H"], dtype=float)
    Ic = np.array(case["I_c"], dtype=float)

    residuals = {
        "W_orthogonality": infnorm(W.T @ W - np.eye(6)),
        "TH_definition": infnorm(T - W.T),
        "Theta_definition": infnorm(Theta - W @ R @ W.T),
        "parity_intertwining": infnorm(T @ Theta - R @ T),
        "event_antisymplectic": infnorm(R.T @ J @ R + J),
        "Q121_commutation": infnorm(R @ Ic - Ic @ R),
        "copy_swap_sign": infnorm(S @ R @ S.T + R),
    }

    premise_ok = (
        residuals["W_orthogonality"] <= TOL and
        residuals["TH_definition"] <= TOL and
        residuals["Theta_definition"] <= TOL and
        residuals["Q121_commutation"] <= TOL
    )

    if premise_ok:
        result = "IN_SCOPE_PASS" if (
            residuals["parity_intertwining"] <= TOL and
            residuals["event_antisymplectic"] <= TOL and
            residuals["copy_swap_sign"] <= TOL
        ) else "IN_SCOPE_FAIL"
    else:
        result = "CONTROL_FAIL"

    return result, residuals

def main():
    if len(sys.argv) != 3:
        raise SystemExit("usage: runner.py CASES.json OUTPUT.json")
    cases_path = Path(sys.argv[1])
    out_path = Path(sys.argv[2])
    doc = json.loads(cases_path.read_text())
    results = []
    for case in doc["cases"]:
        cls, residuals = classify(case)
        results.append({
            "case_id":case["case_id"],
            "classification":cls,
            "residuals":residuals
        })

    payload = {
        "schema":"UD_PARITY_CARRIER_CRL2C_RUN_OUTPUT_v0.1",
        "input_sha256":hashlib.sha256(cases_path.read_bytes()).hexdigest(),
        "tolerance":TOL,
        "results":results
    }
    out_path.write_text(json.dumps(payload, indent=2))
    print(hashlib.sha256(out_path.read_bytes()).hexdigest())

if __name__ == "__main__":
    main()
