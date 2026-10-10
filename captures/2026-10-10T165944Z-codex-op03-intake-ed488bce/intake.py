#!/usr/bin/env python3
"""Two-stage, exact OP03 capacity-polarity intake; no native switch generator."""
import argparse
import hashlib
import json
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path

if not __debug__:
    raise RuntimeError("Run without Python -O; validation assertions must remain enabled")

SCHEMA = "UD-OP03-POLARITY-INTAKE-v0.1"
CARRIER = "K4/C1/opposite-pair/Theta"


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read_json(path):
    return json.loads(Path(path).read_text())


def read_rows(path):
    rows = [json.loads(line) for line in Path(path).read_text().splitlines() if line.strip()]
    ids = [r["event_id"] for r in rows]
    assert ids and all(isinstance(i, str) and i for i in ids) and len(ids) == len(set(ids))
    return rows


def exact(x):
    assert isinstance(x, str) and x and all(c in "-0123456789/" for c in x)
    q = Fraction(x)
    assert str(q) == x, "use canonical exact fraction strings"
    return q


def bits(x):
    assert type(x) is list and len(x) == 3 and all(type(z) is int and z in (0, 1) for z in x)
    return x


def sha(x):
    return isinstance(x, str) and len(x) == 64 and all(c in "0123456789abcdef" for c in x)


def metadata(m):
    assert m["schema"] == SCHEMA and m["carrier"] == CARRIER
    assert isinstance(m["source_version"], str) and m["source_version"]
    assert all(sha(m[k]) for k in ("source_computation_sha256","pre_event_generator_sha256",
                                  "eligibility_rule_sha256"))
    assert m["outcome_acquisition_mode"] in ("precommitted_file", "future_acquisition")
    if m["outcome_acquisition_mode"] == "precommitted_file":
        assert sha(m["independent_outcome_sha256"])
    else:
        assert m["independent_outcome_sha256"] is None
    p = m["outcome_producer"]
    assert p["kind"] in ("independent_model", "measurement")
    assert sha(p["artifact_sha256"]) and p["independence_evidence"]
    assert m["time_parameter"] == "native dimensionless s"
    assert m["claim_scope"] == "conditional one-pair capacity polarity; no physical promotion"


def prepare(args):
    m = read_json(args.manifest)
    metadata(m)
    rows = read_rows(args.pre_event)
    predictions = []
    for r in rows:
        theta, integrity = bits(r["theta_minus"]), bits(r["pair_integrity"])
        G = [exact(x) for x in r["signed_G_by_pair"]]
        assert len(G) == 3
        assert exact(r["s_start"]) < exact(r["s_end"])
        assert sha(r["state_receipt_sha256"]) and r["prior_event_boundary"]
        assert type(r["eligible_before_outcome"]) is bool
        g = (sum(G) > 0) - (sum(G) < 0)
        both_directions_feasible = any(not theta[i] and integrity[i] for i in range(3)) and any(theta[i] and integrity[i] for i in range(3))
        eligible = r["eligible_before_outcome"] and g != 0 and 0 < sum(theta) < 3 and both_directions_feasible
        predictions.append({"event_id": r["event_id"], "theta_minus":theta,
                            "signed_G_sum":str(sum(G)), "sign":g,
                            "primary_eligible":eligible,
                            "predicted_D_cl_delta_aligned":2*g if eligible else None,
                            "predicted_D_cl_delta_anti_aligned":-2*g if eligible else None,
                            "predicted_D_cl_delta_persistence":0 if eligible else None})
    Path(args.predictions).write_text("".join(json.dumps(p,sort_keys=True)+"\n" for p in predictions))
    frozen={"schema":SCHEMA,"created_utc":datetime.now(timezone.utc).isoformat(),
            "manifest_sha256":digest(args.manifest),"pre_event_sha256":digest(args.pre_event),
            "predictions_sha256":digest(args.predictions),
            "outcome_acquisition_mode":m["outcome_acquisition_mode"],
            "committed_independent_outcome_sha256":m["independent_outcome_sha256"],
            "row_count":len(rows),"primary_eligible_count":sum(p["primary_eligible"] for p in predictions),
            "interpretation":"mechanical freeze only; independence, chronological custody and domain eligibility require non-constructor review",
            "physical_promotion":0}
    Path(args.freeze).write_text(json.dumps(frozen,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"status":"FROZEN_PREDICTIONS_TARGET_UNOPENED",**frozen},indent=2))


def score(args):
    f,m=read_json(args.freeze),read_json(args.manifest)
    metadata(m)
    assert f["schema"] == SCHEMA
    assert digest(args.manifest) == f["manifest_sha256"]
    assert digest(args.pre_event) == f["pre_event_sha256"]
    assert digest(args.predictions) == f["predictions_sha256"]
    if m["outcome_acquisition_mode"] == "precommitted_file":
        assert digest(args.outcomes) == f["committed_independent_outcome_sha256"] == m["independent_outcome_sha256"]
    else:
        assert f["committed_independent_outcome_sha256"] is None
    pred=read_rows(args.predictions);target=read_rows(args.outcomes)
    assert [p["event_id"] for p in pred] == [t["event_id"] for t in target]
    count={"eligible":0,"aligned_match":0,"anti_aligned_match":0,"persistence_match":0,
           "non_event_or_swap":0,"invalid_multi_pair":0,"excluded_precommitted":0}
    for p,t in zip(pred,target):
        before,after=bits(p["theta_minus"]),bits(t["theta_plus"])
        assert sha(t["target_receipt_sha256"]) and t["producer_artifact_sha256"] == m["outcome_producer"]["artifact_sha256"]
        if not p["primary_eligible"]:
            count["excluded_precommitted"]+=1;continue
        count["eligible"]+=1
        distance=sum(x!=y for x,y in zip(before,after))
        delta_D=-2*(sum(after)-sum(before))
        if distance == 0 or (distance == 2 and delta_D == 0):
            count["non_event_or_swap"]+=1
        elif distance != 1:
            count["invalid_multi_pair"]+=1
        if distance == 1:
            count["aligned_match"]+=delta_D==p["predicted_D_cl_delta_aligned"]
            count["anti_aligned_match"]+=delta_D==p["predicted_D_cl_delta_anti_aligned"]
        count["persistence_match"]+=delta_D==0
    verdict="NO_DISCRIMINATING_EVENT" if count["eligible"] == count["non_event_or_swap"]+count["invalid_multi_pair"] else "RETROSPECTIVE_COUNTS_PENDING_INDEPENDENT_REVIEW"
    print(json.dumps({"status":verdict,"counts":count,"target_sha256":digest(args.outcomes),
                      "outcome_acquisition_mode":m["outcome_acquisition_mode"],
                      "conditional_rule_validated":False,"physical_promotion":0},indent=2))


def main():
    a=argparse.ArgumentParser()
    sub=a.add_subparsers(dest="command",required=True)
    p=sub.add_parser("prepare")
    for flag in ("manifest","pre_event","predictions","freeze"):p.add_argument(flag)
    q=sub.add_parser("score")
    for flag in ("manifest","pre_event","predictions","freeze","outcomes"):q.add_argument(flag)
    args=a.parse_args()
    (prepare if args.command=="prepare" else score)(args)


if __name__ == "__main__":main()
