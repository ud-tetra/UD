#!/usr/bin/env python3
import json, sys, hashlib, numpy as np
from pathlib import Path

EPS=1e-10
R=np.diag([1,1,1,-1,-1,-1.0])
J=np.r_[np.c_[np.zeros((3,3)),-np.eye(3)],
        np.c_[np.eye(3),np.zeros((3,3))]]
SW=np.r_[np.c_[np.zeros((3,3)),np.eye(3)],
         np.c_[np.eye(3),np.zeros((3,3))]]

def mx(M):
    return float(np.linalg.norm(M,ord=np.inf))

def evaluate(item):
    W=np.asarray(item["W"],float)
    TH=np.asarray(item["T_H"],float)
    Q=np.asarray(item["Theta_H"],float)
    C=np.asarray(item["I_c"],float)
    c=float(item["c"])
    C_expected=np.diag([c,c,c,1/c,1/c,1/c])

    tests={}
    tests["orth"]=mx(W.T@W-np.eye(6))
    tests["th"]=mx(TH-W.T)
    tests["theta"]=mx(Q-W@R@W.T)
    tests["Ic_definition"]=mx(C-C_expected)
    tests["intertwine"]=mx(TH@Q-R@TH)
    tests["anti"]=mx(R.T@J@R+J)
    tests["commute"]=mx(R@C-C@R)
    tests["swap"]=mx(SW@R@SW.T+R)

    premise=max(tests["orth"],tests["th"],tests["theta"],
                tests["Ic_definition"],tests["commute"])<=EPS
    theorem=max(tests["intertwine"],tests["anti"],tests["swap"])<=EPS

    if premise and theorem:
        cls="IN_SCOPE_PASS"
    elif premise and not theorem:
        cls="IN_SCOPE_FAIL"
    else:
        cls="CONTROL_FAIL"
    return cls,tests

def main():
    if len(sys.argv)!=3:
        raise SystemExit("usage: replication_runner.py cases.json output.json")
    src=Path(sys.argv[1]); dst=Path(sys.argv[2])
    data=json.loads(src.read_text())
    out=[]
    for item in data["cases"]:
        cls,tests=evaluate(item)
        out.append({"case_id":item["case_id"],"classification":cls,"residuals":tests})
    payload={
        "schema":"UD_PARITY_CARRIER_CRL2D_REPLICATION_OUTPUT_v0.1",
        "input_sha256":hashlib.sha256(src.read_bytes()).hexdigest(),
        "tolerance":EPS,
        "results":out
    }
    dst.write_text(json.dumps(payload,indent=2))
    print(hashlib.sha256(dst.read_bytes()).hexdigest())

if __name__=="__main__":
    main()
