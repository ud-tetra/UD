#!/usr/bin/env python3
"""UD-PRED01/PRED02 D0 candidate: local K4 star excision, bounded staged source,
12-bit microstate lift, and source-blind readout contracts.

No physical carrier, laboratory observation, or independent review is asserted.
"""
from __future__ import annotations
import argparse
import itertools
import json
import math
from collections import Counter, deque
from fractions import Fraction
from pathlib import Path
import numpy as np
from scipy.sparse import coo_matrix, csr_matrix
from scipy.sparse.linalg import spsolve


def planar_faces(grid: int):
    assert grid >= 4 and grid % 2 == 0
    for x in range(grid):
        for y in range(grid):
            a=(x,y); b=(x+1,y); c=(x+1,y+1); d=(x,y+1)
            yield tuple(sorted((a,b,c)))
            yield tuple(sorted((a,c,d)))


def source_prop(grid: int, height: int, seed: tuple[int,int,int] | None=None):
    """Conserved unit token travels along stipulated +z port; marks a trail.
    Local rule at each update: one occupied vertex to its adjacent +z neighbor.
    The seed, direction port, token, and occupancy-to-excision law are assumed.
    """
    seed=seed or (grid//2,grid//2,0)
    assert 0 < seed[0] < grid and 0 < seed[1] < grid and seed[2]==0
    token=seed; trail=[token]; ledger=[]
    for tick in range(height):
        next_token=(token[0],token[1],token[2]+1)
        assert 0 <= next_token[2] <= height
        ledger.append({"event_index":tick,"stock_before":1,"source":token,"sink":next_token,"stock_after":1})
        token=next_token; trail.append(token)
    assert len(trail)==height+1
    return trail,ledger


def build_complex(grid:int=4,height:int=2,defect:bool=False,seed=None):
    """Triangulates a 3-ball by K4 tetrahedra, then optionally applies only
    the local 'remove every K4 packet incident to the marked trail' rule.
    """
    trail,ledger=source_prop(grid,height,seed)
    active_planar=(trail[0][0],trail[0][1])
    base_full=list(planar_faces(grid))
    faces=[f for f in base_full if not defect or active_planar not in f]
    tets=set()
    for k in range(height):
        for f in faces:
            a,b,c=sorted(f)
            a0=(*a,k);b0=(*b,k);c0=(*c,k)
            a1=(*a,k+1);b1=(*b,k+1);c1=(*c,k+1)
            for tet in ((a0,b0,c0,c1),(a0,b0,b1,c1),(a0,a1,b1,c1)):
                tets.add(tuple(sorted(tet)))
    tris=set();edges=set();vertices=set()
    for tet in tets:
        vertices.update(tet)
        tris.update(tuple(sorted(f)) for f in itertools.combinations(tet,3))
        edges.update(tuple(sorted(e)) for e in itertools.combinations(tet,2))
    complex_={"vertices":sorted(vertices),"edges":sorted(edges),"triangles":sorted(tris),"tetrahedra":sorted(tets),"trail":trail,"ledger":ledger,"grid":grid,"height":height,"defect":defect}
    if defect:
        assert all(set(tet).isdisjoint(trail) for tet in tets)
        assert all(active_planar not in f for f in faces)
    return complex_


def gf2_rank_vectors(columns):
    pivots={}
    for v in columns:
        while v:
            p=v.bit_length()-1
            if p not in pivots:
                pivots[p]=v;break
            v^=pivots[p]
    return len(pivots)


def boundaries(c):
    maps=[{s:i for i,s in enumerate(c[name])} for name in ('vertices','edges','triangles')]
    b1=[];b2=[];b3=[]
    for e in c['edges']:
        b1.append((1<<maps[0][e[0]])^(1<<maps[0][e[1]]))
    for tri in c['triangles']:
        v=0
        for e in itertools.combinations(tri,2):v^=1<<maps[1][tuple(sorted(e))]
        b2.append(v)
    for tet in c['tetrahedra']:
        v=0
        for face in itertools.combinations(tet,3):v^=1<<maps[2][tuple(sorted(face))]
        b3.append(v)
    return b1,b2,b3


def audit_topology(c):
    b1,b2,b3=boundaries(c)
    def compose(cols,lower):
        for v in cols:
            acc=0
            while v:
                z=v & -v
                acc ^= lower[z.bit_length()-1]
                v-=z
            assert acc==0
    compose(b2,b1);compose(b3,b2)
    r1,r2,r3=map(gf2_rank_vectors,(b1,b2,b3))
    v,e,f,t=map(lambda name:len(c[name]),('vertices','edges','triangles','tetrahedra'))
    betti=[v-r1,e-r1-r2,f-r2-r3,t-r3]
    assert v-e+f-t==betti[0]-betti[1]+betti[2]-betti[3]
    return {"simplices":{"V":v,"E":e,"F":f,"T":t},"ranks_F2":[r1,r2,r3],"betti_F2":betti,"euler":v-e+f-t,"boundary_of_boundary_zero":True}


def directed_edge_index(c):
    return {v:i for i,v in enumerate(c['edges'])}


def integer_cocycle(c):
    """Integer seam cochain from angular cut, not fitted from a target.
    Angular order selects a discrete branch; all subsequent checks exact.
    """
    assert c['defect']
    grid=c['grid']; cx=cy=grid//2
    rays=sorted({(int((v[0]-cx)//math.gcd(abs(v[0]-cx),abs(v[1]-cy))),
                  int((v[1]-cy)//math.gcd(abs(v[0]-cx),abs(v[1]-cy))))
                 for v in c['vertices']},key=lambda t:math.atan2(t[1],t[0]))
    assert (0,0) not in rays
    tmap={ray:Fraction(i,len(rays)) for i,ray in enumerate(rays)}
    def angle(v):
        dx=v[0]-cx; dy=v[1]-cy;g=math.gcd(abs(dx),abs(dy))
        assert g
        return tmap[(dx//g,dy//g)]
    angles={v:angle(v) for v in c['vertices']}
    z=[]
    for a,b in c['edges']:
        dt=angles[b]-angles[a]
        z.append(1 if dt < -Fraction(1,2) else (-1 if dt > Fraction(1,2) else 0))
    # Each oriented triangle has zero discrete curvature.
    lookup=directed_edge_index(c)
    def value(a,b):
        e=tuple(sorted((a,b))); idx=lookup[e]
        return z[idx] if (a,b)==e else -z[idx]
    for a,b,d in c['triangles']:
        assert value(a,b)+value(b,d)+value(d,a)==0
    assert sum(x*x for x in z)>0
    # Inner boundary cycle: vertices in link of removed center in planar source.
    incident=[f for f in planar_faces(grid) if (cx,cy) in f]
    link_edges=[]
    for face in incident:
        pair=tuple(sorted([q for q in face if q!=(cx,cy)]))
        link_edges.append(pair)
    link_edges=set(link_edges)
    neigh=set(itertools.chain.from_iterable(link_edges))
    links=sorted(neigh,key=lambda v:math.atan2(v[1]-cy,v[0]-cx))
    assert len(link_edges)==len(links)
    assert all(tuple(sorted((links[i],links[(i+1)%len(links)]))) in link_edges for i in range(len(links)))
    loop=[(*v,0) for v in links]
    period=sum(value(loop[i],loop[(i+1)%len(loop)]) for i in range(len(loop)))
    assert abs(period)==1
    if period<0:z=[-x for x in z]
    return np.array(z,dtype=float), {"integer_seam_support":int(np.count_nonzero(z)),"integral_period":1,"inner_link_length":len(loop),"angular_ray_count":len(rays)}


def graph_incidence(c):
    vindex={v:i for i,v in enumerate(c['vertices'])}
    rows=[];cols=[];data=[]
    for j,(a,b) in enumerate(c['edges']):
        rows.extend([vindex[a],vindex[b]]); cols.extend([j,j]);data.extend([-1.,1.])
    return coo_matrix((data,(rows,cols)),shape=(len(vindex),len(c['edges']))).tocsr()


def sparse_tri_incidence(c):
    eindex=directed_edge_index(c)
    rows=[];cols=[];data=[]
    for j,tri in enumerate(c['triangles']):
        for k in range(3):
            edge=tuple(sorted((tri[:k]+tri[k+1:])))
            rows.append(eindex[edge]);cols.append(j);data.append(float((-1)**k))
    return coo_matrix((data,(rows,cols)),shape=(len(c['edges']),len(c['triangles']))).tocsr()


def harmonic(c,z):
    b1=graph_incidence(c); l=(b1@b1.T).tocsr()
    rhs=b1@z
    phi=np.zeros(len(c['vertices']))
    phi[1:]=spsolve(l[1:,1:],rhs[1:])
    h=z-np.asarray(b1.T@phi).ravel()
    b2=sparse_tri_incidence(c)
    flat=np.max(np.abs(b2.T@h))
    coflat=np.max(np.abs(b1@h))
    assert flat<1.e-10 and coflat<1.e-9,(flat,coflat)
    return h,{"norm_h_sq":float(h@h),"norm_cut_sq":float(z@z),"flat_residual_max":float(flat),"coflat_residual_max":float(coflat)}



def local_hodge_relaxation(c,z,steps=2500):
    """Local graph-neighbor Jacobi/gradient update computes harmonic projection.
    This is algorithmic time, not physical time. Source z remains global data,
    but each update reads only neighbor phi and incident edge z.
    """
    b1=graph_incidence(c);lap=(b1@b1.T).tocsr()
    max_degree=float(lap.diagonal().max())
    eta=1/(2*max_degree)
    rhs=np.asarray(b1@z).ravel()
    phi=np.zeros(len(c['vertices']))
    initial=float(np.max(np.abs(rhs)))
    for t in range(steps):
        phi += eta*(rhs-lap@phi)
    h=z-np.asarray(b1.T@phi).ravel()
    b2=sparse_tri_incidence(c)
    return h,{"iterations":steps,"eta":eta,"initial_divergence_max":initial,
              "final_divergence_max":float(np.max(np.abs(b1@h))),
              "exact_flatness_residual":float(np.max(np.abs(b2.T@h))),
              "updated_from_vertex_neighbors_only":True}


def local_staged_work(c,h,n=2,mu_ratio=1.0):
    """One edge update per event, with temporary nonflat states. Action:
    lambda ||a||^2/2 + mu ||d a||^2/2; normalized retained gap = 1.
    Tracks positive work separately from signed net action difference.
    """
    b2=sparse_tri_incidence(c)
    norm=float(h@h)
    lam=1/((n+0.5)*norm); mu=mu_ratio*lam
    # A queued local front, not a global distance sort: visit only adjacent
    # edges from previously visited vertices. Vertex memory and queue are
    # assumed algorithmic control, not derived physical propagation.
    adj={v:[] for v in c['vertices']}
    for j,(u,v) in enumerate(c['edges']):
        adj[u].append((j,v)); adj[v].append((j,u))
    center=c['grid']//2
    anchors=[v for v in c['vertices'] if
             max(abs(v[0]-center),abs(v[1]-center))==1 and v[2]==0]
    assert anchors
    todo=deque([min(anchors)]);seen_v=set(todo);seen_e=set();order=[]
    while todo:
        v=todo.popleft()
        for idx,w in sorted(adj[v]):
            if idx not in seen_e:
                seen_e.add(idx);order.append(idx)
            if w not in seen_v:
                seen_v.add(w);todo.append(w)
    assert len(order)==len(c['edges'])
    dmax=max(np.diff(b2.tocsr().indptr))
    curv=np.zeros(len(c['triangles']))
    a=n*h.copy()
    oldE=.5*lam*(a@a)
    positive=0.;peak=oldE;curvpeak=0.;num_nonflat=0
    b2csr=b2.tocsr()
    for j in order:
        dq=h[j];a[j]+=dq
        arow=b2csr.getrow(j)
        curv[arow.indices]+=arow.data*dq
        E=.5*lam*(a@a)+.5*mu*(curv@curv)
        positive+=max(E-oldE,0.)
        peak=max(peak,E)
        curvpeak=max(curvpeak,float(curv@curv))
        num_nonflat+=int(np.max(np.abs(curv))>1e-10)
        oldE=E
    net=lam*(n+.5)*norm
    assert abs(oldE-.5*lam*(n+1)**2*norm)<1e-8
    assert abs(net-1.)<1e-10
    upper=net+3*mu*dmax*norm
    assert positive<=upper+1e-7,(positive,upper)
    return {"edge_updates":len(order),"lambda_for_unit_gap":lam,"mu_over_lambda":mu_ratio,
            "net_retained_action":net,"sum_positive_injected_work":positive,"safe_upper_bound":upper,
            "peak_action":peak,"peak_curvature_sq":curvpeak,"nonflat_intermediate_steps":num_nonflat,
            "triangle_incidence_max":int(dmax),"source_fraction_nonzero":float(np.mean(abs(h)>1e-12))}


def fixed_cut_work(h,z,n=2):
    nh=float(h@h);nz=float(z@z)
    lam=1/((n+.5)*nh)
    return {"retained_gap":1.,"input_work_at_fixed_cut":float(lam*(n*nh+nz/2)),
            "relaxation_remainder":float(lam*(nz-nh)/2),
            "fixed_cut_over_retained":float((n*nh+nz/2)/((n+.5)*nh))}


def pair_class(state):
    Ta,Tb,La,Lb=state
    g=(Ta and La) or (Tb and Lb)
    omega=(Ta and Tb) and (La or Lb)
    return (int(omega),int(g))


def microstate_audit():
    states=list(itertools.product((0,1),repeat=4))
    counts=Counter(pair_class(s) for s in states)
    assert counts=={(0,0):9,(0,1):4,(1,1):3}
    options={label:sorted((s for s in states if pair_class(s)==label),key=lambda x:(sum(x),x)) for label in counts}
    reps={label:opts[0] for label,opts in options.items()}
    assert all(pair_class(s)==label for label,s in reps.items())
    triple_labels=list(itertools.product(((0,0),(0,1),(1,1)),repeat=3))
    micro_counts={"".join("0" if p==(0,0) else "1" if p==(0,1) else "2" for p in q):math.prod(counts[p] for p in q) for q in triple_labels}
    assert sum(micro_counts.values())==16**3
    probabilities=[Fraction(9,16),Fraction(4,16),Fraction(3,16)]
    p_match=sum(p*p for p in probabilities)**3
    E=math.comb(24,2)*p_match
    shell=Counter(sum(pair[0] for pair in q) for q in triple_labels)
    assert shell=={0:8,1:12,2:6,3:1}
    def label_key(q):
        return "".join("0" if pair==(0,0) else "1" if pair==(0,1) else "2" for pair in q)
    schedule=[]
    # A and B are matched full microstates; C changes raw inputs but preserves the 27-class label.
    for pass_name in ("A_baseline", "B_exact_replay", "C_within_class_challenge"):
        for q in triple_labels:
            k=0 if pass_name!="C_within_class_challenge" else 1
            schedule.append({"pass":pass_name,"class":label_key(q),
                             "raw_12bits":[list(options[p][k]) for p in q]})
    assert len(schedule)==81
    assert all(options[p][1]!=options[p][0] for p in counts)
    sample=54
    p_prepar=Fraction(1,10**5)
    p_any=1-(1-float(p_prepar))**(12*sample)
    return {"pair_class_multiplicity":{str(k):v for k,v in sorted(counts.items())},
            "representative_raw_states":{str(k):list(v) for k,v in sorted(reps.items())},
            "raw_triple_microstate_count":sum(micro_counts.values()),"formal_class_count":len(triple_labels),
            "raw_class_multiplicity_min":min(micro_counts.values()),"raw_class_multiplicity_max":max(micro_counts.values()),
            "natural_iid_match_probability":str(p_match),"expected_iid_replays_N24":str(E),
            "shell_counts_formal":dict(sorted(shell.items())),
            "input_channel_count":12,"output_channels_needed":{"q":3,"theta_plus":3,"leakage":4},
            "p_flip_per_input":str(p_prepar),"union_failure_probability_54_preparations_approx":p_any,
            "union_failure_probability_exact":"1-(1-1/100000)^648",
            "union_bound_54x12_input_flips":str(sample*12*p_prepar),
            "class_representatives":micro_counts,
            "schedule_81_observations":schedule,
            "full_raw_match_vs_within_class_challenge":"A/B identical raw 12-bit preparations; C alternate raw state in same 27-class",
            "class_sufficiency_counterexample":{"raw_a":[0,0,0,0],"raw_b":[0,0,1,0],
                "class":"(0,0) for both","memoryless_raw_output":"L_a gives 0 versus 1"}}


def main():
    p=argparse.ArgumentParser();p.add_argument("--out",default="RESULTS.json")
    a=p.parse_args()
    results={"metadata":{"status":"D0_DEVELOPMENT_ASSUMPTION_SCOPED","physical_promotion":0,
                          "external_review":"DEFERRED","physical_time":"NOT_CALIBRATED",
                          "source_rules":"STIPULATED_NOT_RECOVERED_NATIVE_UD"},
             "pred01":{},"pred02":microstate_audit()}
    for size in (4,6,8):
        full=build_complex(size,2,defect=False)
        hole=build_complex(size,2,defect=True)
        full_b=audit_topology(full);hole_b=audit_topology(hole)
        assert full_b['betti_F2']==[1,0,0,0],full_b
        assert hole_b['betti_F2']==[1,1,0,0],hole_b
        z,seam=integer_cocycle(hole)
        h,har=harmonic(hole,z)
        st=local_staged_work(hole,h)
        loc_h,local_solver=local_hodge_relaxation(hole,z,steps=2500)
        local_solver["error_to_direct_harmonic_norm"]=float(np.linalg.norm(loc_h-h))
        fixed=fixed_cut_work(h,z)
        results['pred01'][size]={"original":full_b,"selected":hole_b,"seam":seam,
                                "harmonic":har,"distributed_staged_source":st,"fixed_cut_source":fixed,"local_hodge_solver":local_solver}
    Path(a.out).write_text(json.dumps(results,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps({"sizes":list(results['pred01']),"pred02_pair_counts":results['pred02']['pair_class_multiplicity'],
                      "results":a.out,"physical_promotion":0},indent=2))
if __name__=="__main__": main()
