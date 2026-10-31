#!/usr/bin/env python3
"""Independent standard-library replay of UD PRED-01 and PRED-02 conditional math.
Assumed carriers C0..C4; simulation only, no physical correspondence.
"""
from fractions import Fraction as F
from itertools import product
from collections import Counter
from math import comb, sqrt
from random import Random
import json, argparse

def increments(A,C,kappa,n=4):
    assert A>0
    out=[]; f=F(0)
    for k in range(n):
        e=A+C*k+kappa*f
        out.append(e)
        f+=e
    return out

def d2(e): return e[2]-2*e[1]+e[0]
def h4(e): return (e[1]-e[0])*(e[3]-e[2])-(e[2]-e[1])**2

def infer(e):
    A, e1, e2=e[:3]
    d0=e1-A
    if d0==0:
        return {"status":"NONIDENTIFIABLE" if e2==A else "REJECT_WBX1"}
    kappa=(e2-2*e1+A)/d0
    C=d0-kappa*A
    return {"status":"IDENTIFIED_CONDITIONAL","kappa":kappa,"C":C}

def plb1(eps,lam):
    if len(eps)!=len(lam): raise ValueError("event mismatch")
    factors=[e/l for e,l in zip(eps,lam) if l]
    if any(e and not l for e,l in zip(eps,lam)):return "REJECTED"
    return "COMPATIBLE" if factors and min(factors)>=0 and len(set(factors))==1 else "UNIDENTIFIABLE_OR_REJECTED"

def simulate(draws=10000,seed=20261031,cv=0.1,n=12):
    threshold=3*cv/sqrt(n)*sqrt(62)
    rng=Random(seed)
    models=[("affine",F(2),F(0)),("WBX1_k_half",F(3,2),F(1,2)),
            ("WBX1_k_one",F(1),F(1)),("WBX1_k_two",F(0),F(2))]
    out={}
    for name,C,k in models:
        es=increments(F(1),C,k,4)
        count=0
        for j in range(draws):
            noisy=[rng.gauss(float(x),cv*abs(float(x))/sqrt(n)) for x in es[:3]]
            count+=abs(noisy[2]-2*noisy[1]+noisy[0])>threshold
        out[name]={"increments":[str(x) for x in es],"D2":str(d2(es)),
                   "detections":count,"fraction":count/draws}
    return {"draws":draws,"seed":seed,"CV":cv,"means_n":n,
            "fixed_null_3sigma_threshold":threshold,"rates":out}

def audit():
    # First-order recurrence / exact fourth-event identity, including the singular line.
    for C in [F(-2),F(-1,2),F(0),F(1,2),F(1),F(3,2),F(2)]:
        for k in [F(-1,2),F(0),F(1,2),F(1),F(3,2),F(2)]:
            e=increments(F(1),C,k,5)
            assert all(e[j+1]==(1+k)*e[j]+C for j in range(4))
            assert h4(e)==0
            fitted=infer(e)
            if C+k!=0:
                assert fitted["C"]==C and fitted["kappa"]==k
    constant=increments(F(1),F(-2),F(2),8)
    assert constant==[F(1)]*8 and infer(constant)["status"]=="NONIDENTIFIABLE"
    assert h4([F(1),F(1),F(1),F(9)])==0  # invariant necessary, not sufficient
    grid=[F(0),F(1,2),F(1),F(3,2),F(2)]
    aliases=[(C,k) for C in grid for k in grid if increments(F(1),C,k,2)==[F(1),F(3)]]
    assert len(aliases)==5 and sum(k!=0 for C,k in aliases)==4
    nonlinear=increments(F(1),F(0),F(2),4)
    assert plb1(nonlinear,nonlinear)=="COMPATIBLE"
    assert plb1(nonlinear,[F(1),F(3),F(5),F(7)])=="UNIDENTIFIABLE_OR_REJECTED"

    # Formal PRED-02 27-state class set, not an experimentally realizable claim.
    classes=list(product(((0,0),(0,1),(1,1)),repeat=3))
    assert len(classes)==27
    shell=Counter(sum(x[0] for x in c) for c in classes)
    assert shell=={0:8,1:12,2:6,3:1}
    uniform_exp=F(comb(24,2),27)
    skew=[F(9,10)]+[F(1,260)]*26
    skew_exp=F(comb(24,2))*sum(p*p for p in skew)
    assert skew_exp>=uniform_exp
    def pairs(s):
        return sum(comb(n,2) for n in Counter(s).values())
    assert pairs(classes[:24])==0 and pairs(classes+classes)==27
    return {"two_event_aliases":len(aliases),"nonlinear_aliases":sum(k!=0 for C,k in aliases),
            "constant_positive_cone_no_go":list(map(str,constant[:4])),
            "iid_24_minimum_expected_replays":str(uniform_exp),
            "skew_iid_expected_replays":str(skew_exp),
            "deliberate_distinct_24_replays":pairs(classes[:24]),
            "two_pass_27_class_replays":pairs(classes+classes),
            "formal_shell_counts":dict(sorted(shell.items()))}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--out",default="pred_results.json")
    p.add_argument("--draws",type=int,default=10000)
    p.add_argument("--seed",type=int,default=20261031)
    a=p.parse_args()
    r={"metadata":{"version":"UD_PRED01_PRED02_REPLAY_v0.2",
                   "evidence":"EXACT_CONDITIONAL_AND_SYNTHETIC_NUMERICAL",
                   "physical_promotion":0,"external_review":"DEFERRED",
                   "carrier_n3":"ASSUMED_NOT_CONSTRUCTED"},
       "exact_audit":audit(),"monte_carlo":simulate(a.draws,a.seed)}
    with open(a.out,"w",encoding="utf-8") as f:json.dump(r,f,indent=2,sort_keys=True)
    print(json.dumps(r,indent=2,sort_keys=True))
if __name__=="__main__":main()
