#!/usr/bin/env python3
from pathlib import Path
import itertools, importlib.util, sys

BASE=Path(__file__).resolve().parent

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec)
    sys.modules[name]=mod
    spec.loader.exec_module(mod)
    return mod

te=load("theta_evt_v01",BASE/"theta_flip_event_quarantine_contract_v0_1.py")
states=list(itertools.product((0,1),repeat=3))
masks=list(itertools.product((0,1),repeat=3))
perms=list(itertools.permutations(range(3)))
def perm(x,p): return tuple(x[p[i]] for i in range(3))
def xor(a,b): return tuple(x^y for x,y in zip(a,b))
count=0
for th in states:
    for xi in masks:
        for p in perms:
            y=perm(th,p); nxt=xor(y,xi)
            C=sum((1-y[i])*xi[i] for i in range(3))
            O=sum(y[i]*xi[i] for i in range(3))
            assert sum(nxt)-sum(th)==C-O
            assert C+O==sum(xi)
            r=te.make_receipt(provider_id="test",event_id=str(count),theta_prev=th,
                              flip_mask=xi,pair_permutation=p,context_note="phase23")
            out=te.apply_receipt(r,theta_prev=th,pair_permutation=p,context_note="phase23")
            assert out.theta_next==nxt
            assert (out.pair_closures,out.pair_reopenings)==(C,O)
            count+=1
assert count==384

for h in perms:
    for th in states:
        for xi in masks:
            assert perm(xor(th,xi),h)==xor(perm(th,h),perm(xi,h))

assert te.apply_optional_receipt(None,theta_prev=(1,0,1)).status=="THETA_UPDATE_DEFERRED"

print("PASS: source Theta-only block; direct event cases =", count)
