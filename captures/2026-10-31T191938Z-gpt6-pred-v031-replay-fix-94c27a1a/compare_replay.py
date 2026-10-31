#!/usr/bin/env python3
"""Typed JSON replay comparator for PRED01/PRED02.

Exact structure and all non-relaxation fields are required to agree byte-value
semantically (dict keys, scalar values, ordered arrays). Only finite numeric
floats inside the declared 'relaxation' subtree permit bounded comparison.
This is cross-platform numerical reproducibility, NOT scientific acceptance.
"""
import argparse
import json
import math
from pathlib import Path

REL_TOL=1e-9
ABS_TOL=1e-10


def compare(saved,produced,path=(),numeric_relaxation=False,stats=None):
    if stats is None: stats={'exact_fields':0,'numerical_fields':0,'max_abs_error':0.0,'max_relative_error':0.0}
    loc='/'.join(map(str,path))
    if isinstance(saved,dict):
        assert isinstance(produced,dict) and set(saved)==set(produced),f'key mismatch at {loc}'
        for key in sorted(saved):
            compare(saved[key],produced[key],path+(key,),numeric_relaxation or (len(path)==0 and key=='relaxation'),stats)
    elif isinstance(saved,list):
        assert isinstance(produced,list) and len(saved)==len(produced),f'list mismatch at {loc}'
        for i,(left,right) in enumerate(zip(saved,produced)):
            compare(left,right,path+(i,),numeric_relaxation,stats)
    elif numeric_relaxation and type(saved) is float:
        assert type(produced) is float,f'floating type mismatch at {loc}'
        assert math.isfinite(saved) and math.isfinite(produced),f'nonfinite value at {loc}'
        delta=abs(saved-produced)
        scale=max(abs(saved),abs(produced),1e-30)
        stats['max_abs_error']=max(stats['max_abs_error'],delta)
        stats['max_relative_error']=max(stats['max_relative_error'],delta/scale)
        assert math.isclose(saved,produced,rel_tol=REL_TOL,abs_tol=ABS_TOL), f'floating drift exceeds tolerance at {loc}'
        stats['numerical_fields']+=1
    else:
        assert type(saved) is type(produced) and saved==produced, f'exact structural mismatch at {loc}: {saved!r} vs {produced!r}'
        stats['exact_fields']+=1
    return stats


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('saved_json')
    ap.add_argument('replay_json')
    args=ap.parse_args()
    a=json.loads(Path(args.saved_json).read_text())
    b=json.loads(Path(args.replay_json).read_text())
    stats=compare(a,b)
    assert a['physics_promotion']==0 and b['physics_promotion']==0
    print(json.dumps({'status':'PASS_SCOPED','comparison':'EXACT_STRUCTURAL_PLUS_BOUNDED_RELAXATION',
                      'relative_tolerance':REL_TOL,'absolute_tolerance':ABS_TOL,
                      'stats':stats,'physical_promotion':0},indent=2,sort_keys=True))

if __name__=='__main__':main()
