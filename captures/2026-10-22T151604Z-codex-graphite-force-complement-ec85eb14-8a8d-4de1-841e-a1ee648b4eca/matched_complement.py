"""Compute the first-layer REBO complement of the logged direct angular force.

Two binary64 coordinate preparation orders are a numerical sensitivity control.
The complement is an algebraic force partition, not an independent physical
potential or a decomposition of all REBO bond-order paths.
"""
from pathlib import Path
import ctypes
import hashlib
import json
import sys
import numpy as np
from lammps import lammps

R=Path(__file__).resolve().parent
case=sys.argv[1]
assert case in ("21_dir_0","21_dir_10024")
probe,comp,name=(34,8,"dir_0") if case=="21_dir_0" else (30,4,"dir_10024")
a=np.load(R/f"{case}_candidate.npz")
x=a["positions_A"]
B=a["B_extended"]
d=B[:,:,probe]
direction=B.reshape(-1,81)[:,comp]
plugin=R/"graphite-trace/rebo_udtrace.so"
assert hashlib.sha256(plugin.read_bytes()).hexdigest()=="80b511dd88cfa6db9d15705709f36d6b37a40892a6d703248a3b86ab098402bf"
lib=ctypes.CDLL(str(plugin))
lib.ud_trace_count.restype=ctypes.c_size_t
lib.ud_trace_copy.argtypes=[ctypes.POINTER(ctypes.c_double),ctypes.c_size_t]
lib.ud_trace_copy.restype=ctypes.c_size_t
params=R/"lammps-runtime/lammps/share/lammps/potentials/CH.rebo"
data=R/"graphite-target-replay/selected/21"/name/"struct.inp.data"
l=lammps(cmdargs=["-screen","none","-log","none"])
for command in (f"plugin load {plugin}","units metal","boundary p p p","atom_style full","box tilt large",
                f"read_data {data}","pair_style hybrid/overlay rebo/udtrace",
                f"pair_coeff * * rebo/udtrace {params} C NULL","pair_coeff 1 2 none","pair_coeff 2 2 none",
                "neighbor 3.0 nsq","neigh_modify one 4096"):
    l.command(command)

def coords(t,style):
    precise=np.ascontiguousarray(np.asarray(x.astype(np.longdouble)+np.longdouble(t)*d.astype(np.longdouble),dtype=np.float64))
    if style=="extended_then_cast":
        return precise
    if style=="binary64_multiply_add":
        return np.ascontiguousarray(x+np.float64(t)*d)
    assert style=="alternating_one_ulp"
    # Frozen parity pattern, independent of forces and of the stencil sign.
    parity=(np.arange(len(x))[:,None]+np.arange(3)[None,:])%2==0
    return np.ascontiguousarray(np.nextafter(precise,np.where(parity,np.inf,-np.inf)))

def sample(t,style):
    xx=coords(t,style)
    l.scatter_atoms("x",1,3,xx.ctypes.data_as(ctypes.POINTER(ctypes.c_double)))
    l.command("run 0 pre yes post no")
    full=np.ctypeslib.as_array(l.gather_atoms("f",1,3),shape=(3*len(x),)).copy().reshape(-1,3)
    n=lib.ud_trace_count()
    logged=np.empty((n,17),dtype=np.float64)
    assert lib.ud_trace_copy(logged.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),n)==n
    assert n==3024
    ids=logged[:,:3].astype(np.int64)-1
    angle=np.zeros_like(full)
    for col,atom_col in ((8,0),(11,1),(14,2)):
        np.add.at(angle,ids[:,atom_col],logged[:,col:col+3])
    rest=full-angle
    closure=float(np.max(abs(full-(angle+rest))))
    return {"full":float(full.ravel()@direction),
            "angle":float(angle.ravel()@direction),
            "rest":float(rest.ravel()@direction),
            "force_closure_max_abs_eV_per_A":closure,
            "coords":xx}

steps=[8e-5,4e-5,2e-5,1e-5,5e-6,2.5e-6,1.25e-6]
offsets=sorted(set([0.0]+[sign*mult*h for h in steps for sign in (-1,1) for mult in (1,2)]))
methods=("extended_then_cast","binary64_multiply_add","alternating_one_ulp")
values={}
try:
    for style in methods:
        values[style]={float(t):sample(t,style) for t in offsets}
finally:
    l.close()

def stencil(v,h,key):
    return (6*v[0.0][key]-4*v[float(h)][key]+v[float(2*h)][key]-4*v[float(-h)][key]+v[float(-2*h)][key])/(2*h)

rows=[]
for h in steps:
    v0=values[methods[0]]
    v1=values[methods[1]]
    terms={style:{key:stencil(values[style],h,key) for key in ("full","angle","rest")} for style in methods}
    used=(0.0,float(h),float(2*h),float(-h),float(-2*h))
    max_coord=max(float(np.max(abs(v0[t]["coords"]-v1[t]["coords"]))) for t in used)
    max_point_rest=max(abs(v0[t]["rest"]-v1[t]["rest"]) for t in used)
    perturbed=values[methods[2]]
    terms["max_coordinate_delta_A"]=max_coord
    terms["max_point_complement_delta_eV_per_A"]=max_point_rest
    terms["complement_stencil_delta_eV_per_A2"]=terms[methods[1]]["rest"]-terms[methods[0]]["rest"]
    terms["one_ulp_max_coordinate_delta_A"]=max(float(np.max(abs(v0[t]["coords"]-perturbed[t]["coords"]))) for t in used)
    terms["one_ulp_max_point_complement_delta_eV_per_A"]=max(abs(v0[t]["rest"]-perturbed[t]["rest"]) for t in used)
    terms["one_ulp_complement_stencil_delta_eV_per_A2"]=terms[methods[2]]["rest"]-terms[methods[0]]["rest"]
    terms["h_A"]=h
    rows.append(terms)
point_values={style:{f"{t:+.12g}":{k:float(v) for k,v in record.items() if k!="coords"} for t,record in values[style].items()} for style in methods}
output={"case":case,"probe":probe,"component":comp,"plugin_sha256":hashlib.sha256(plugin.read_bytes()).hexdigest(),
        "coordinate_methods":methods,"unique_points_per_method":len(offsets),"point_values":point_values,"rows":rows,
        "status":"MATCHED_PREPARATION_FORCE_COMPLEMENT_NUMERICAL_ONLY"}
(R/f"{case}_matched_complement.json").write_text(json.dumps(output,indent=2)+"\n")
print(json.dumps({"case":case,"points":len(offsets),"rows":[{"h":r["h_A"],"rest_extended":r[methods[0]]["rest"],"rest_binary64":r[methods[1]]["rest"],"rest_one_ulp":r[methods[2]]["rest"],"one_ulp_delta":r["one_ulp_complement_stencil_delta_eV_per_A2"],"max_dx":r["one_ulp_max_coordinate_delta_A"]} for r in rows]},indent=2))
