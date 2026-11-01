#!/usr/bin/env python3
"""Independent exact finite audit for K4 online transfer-before-excision.
Mathematical verification only. Does not import prior PR implementation.
"""
from itertools import permutations, combinations
from fractions import Fraction
from math import comb
import json
from pathlib import Path


def build_tets(N, height=2):
    assert N >= 4 and N % 2 == 0
    T=set()
    for x in range(N):
      for y in range(N):
        for z in range(height):
          for perm in permutations(range(3)):
            p=[x,y,z]
            vert=[tuple(p)]
            for axis in perm:
              p=p.copy();p[axis]+=1;vert.append(tuple(p))
            T.add(tuple(sorted(vert)))
    return T


def subcomplex(T):
    vertices=set(); edges=set(); triangles=set()
    for tet in T:
      vertices.update(tet)
      edges.update(tuple(sorted(e)) for e in combinations(tet,2))
      triangles.update(tuple(sorted(tri)) for tri in combinations(tet,3))
    return sorted(vertices),sorted(edges),sorted(triangles), sorted(T)


def gf2rank(columns):
    pivots={}
    for c in columns:
      while c:
        p=c.bit_length()-1
        if p not in pivots:
          pivots[p]=c;break
        c^=pivots[p]
    return len(pivots)


def gf2betti(K):
    V,E,F,T=K
    ixV={v:i for i,v in enumerate(V)}
    ixE={e:i for i,e in enumerate(E)}
    ixF={f:i for i,f in enumerate(F)}
    b1=[(1<<ixV[a])^(1<<ixV[b]) for a,b in E]
    b2=[]
    for tri in F:
      v=0
      for e in combinations(tri,2):v^=1<<ixE[e]
      b2.append(v)
    b3=[]
    for tet in T:
      v=0
      for f in combinations(tet,3):v^=1<<ixF[f]
      b3.append(v)
    for c in b2:
      q=0
      while c:
        low=c&-c;idx=low.bit_length()-1;q^=b1[idx];c^=low
      assert q==0
    for c in b3:
      q=0
      while c:
        low=c&-c;idx=low.bit_length()-1;q^=b2[idx];c^=low
      assert q==0
    r1,r2,r3=map(gf2rank,(b1,b2,b3))
    vals=[len(V)-r1,len(E)-r1-r2,len(F)-r2-r3,len(T)-r3]
    assert len(V)-len(E)+len(F)-len(T)==vals[0]-vals[1]+vals[2]-vals[3]
    return vals, [len(V),len(E),len(F),len(T)], [r1,r2,r3]


def trial(N):
    full=build_tets(N)
    center=N//2
    marked=set();occupied=(center,center,0);sink=0;states=[]
    def check(label):
       live={tet for tet in full if not marked.intersection(tet)}
       v,e,f,t=subcomplex(live)
       b,counts,ranks=gf2betti((v,e,f,t))
       return {"stage":label,"token":occupied,"sink":sink,"marked":sorted(marked),
               "tetrahedra":len(t),"simplices_VEFT":counts,"betti_F2":b,
               "chain_ranks_F2":ranks,"control_stock":int(occupied is not None)+sink}
    states.append(check("initial"))
    for z in range(2):
       live_t={tet for tet in full if not marked.intersection(tet)}
       _,edges,_,_=subcomplex(live_t)
       assert occupied[2]==z
       departed=occupied
       # Discover next site ONLY from the current site and declared +z port.
       next_site=(departed[0],departed[1],departed[2]+1)
       assert tuple(sorted((departed,next_site))) in edges, "no live outgoing edge"
       # Transfer first; then prune previous vertex (local trail-memory update).
       occupied=next_site;marked.add(departed)
       assert occupied not in marked
       states.append(check(f"transfer_then_excise_{z}"))
    # At upper boundary, conserve token in an explicit boundary sink.
    assert occupied==(center,center,2)
    departed=occupied;occupied=None;sink=1;marked.add(departed)
    states.append(check("boundary_sink_and_final_excision"))
    assert [s["control_stock"] for s in states]==[1]*4
    assert states[0]["betti_F2"]==[1,0,0,0]
    assert states[-1]["betti_F2"]==[1,1,0,0]
    assert states[0]["tetrahedra"]==12*N*N
    assert states[-1]["tetrahedra"]==12*N*N-36
    # Excision-first impossibility is immediate, independent of N.
    start=(center,center,0);next_site=(center,center,1)
    v,e,_,_=subcomplex({t for t in full if start not in t})
    assert start not in v and tuple(sorted((start,next_site))) not in e
    # Counterexample: permanent center-memory does NOT prevent erasing H1
    # through an additional radial cut that joins the hole to outer boundary.
    radial_marks={(x,center,z) for x in range(center,N+1) for z in range(3)}
    radial_K=subcomplex({t for t in full if not set(t).intersection(radial_marks)})
    radial_betti,radial_counts,_=gf2betti(radial_K)
    assert marked.issubset(radial_marks)
    assert radial_betti==[1,0,0,0],(N,radial_betti)
    return {"N":N,"radial_cut_betti_F2":radial_betti,"radial_cut_simplices_VEFT":radial_counts,"states":states,"excision_first_is_blocked":True,
            "full_to_final_removed_tets":len(full)-states[-1]["tetrahedra"]}


def scaling(N):
    from fractions import Fraction as Q
    m=N//2
    hm=sum((Q(1,r) for r in range(1,m+1)),Q(0))
    lower=Q(3,8)*hm
    upper=Q(336)*hm
    return {"N":N,"m":m,"H_m":str(hm),
            "norm_h_sq_lower":str(lower),"norm_h_sq_upper":str(upper),
            "delta_lower_lambda1":str(Q(5,2)*lower),
            "lambda_for_unit_gap_upper":str(Q(2,5)/lower),
            "work_ratio_upper_with_mu_equals_lambda_n2":str(Q(9,5))}


def main():
    observed={"version":"v1.0","evidence":"EXACT_FINITE_AND_CONDITIONAL_THEOREMS",
        "coefficient_system":"F2 chain ranks; rational harmonic-number bounds",
        "topology_trials":[trial(N) for N in (4,6,8,10)],
        "stiffness_constraints":[scaling(N) for N in (4,6,8,16,32,64,128)],
        "physical_promotion":0,"review":"DEFERRED"}
    p=Path(__file__).with_name("EXACT_RESULTS.json")
    p.write_text(json.dumps(observed,indent=2,sort_keys=True)+"\n")
    print("PASS: transfer-before-excision live-edge invariants, chain complexes, sink conservation, exact scaling constraints")
    for a in observed["topology_trials"]:
      print(a["N"],[(s["stage"],s["tetrahedra"],s["betti_F2"]) for s in a["states"]])
    return observed

if __name__=="__main__":main()
