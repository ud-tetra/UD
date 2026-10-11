#!/usr/bin/env python3
"""Exact OP03 v0.2 typed-seat and first-admissibility counterexample audit."""
import itertools
import json
from fractions import Fraction as F

VERTICES=tuple(range(4))
S=[list(itertools.combinations(VERTICES,k)) for k in (1,2,3,4)]

def z(n,m): return [[F(0) for _ in range(m)] for _ in range(n)]
def eye(n):
    a=z(n,n)
    for i in range(n): a[i][i]=F(1)
    return a
def tr(a): return [list(row) for row in zip(*a)]
def mm(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))),F(0))
             for j in range(len(b[0]))] for i in range(len(a))]
def lin(a,b,ca=F(1),cb=F(1)):
    return [[ca*x+cb*y for x,y in zip(ra,rb)] for ra,rb in zip(a,b)]
def boundary(lower,upper):
    a=z(len(lower),len(upper)); lookup={s:i for i,s in enumerate(lower)}
    for j,t in enumerate(upper):
        for p in range(len(t)): a[lookup[t[:p]+t[p+1:]]][j]=F((-1)**p)
    return a
def frozen_endpoint(theta,mu,pair,w):
    shell=sum(theta)+mu
    candidates=[x for x in itertools.product((0,1),repeat=3)
                if sum(x)==shell and all(x[p] or pair[p] for p in range(3))]
    if not candidates: return (),"INTEGRITY_HOLD"
    scores={x:sum((x[p]*w[p] for p in range(3)),F(0)) for x in candidates}
    best=min(scores.values()); winners=tuple(x for x in candidates if scores[x]==best)
    return winners,"PASS" if len(winners)==1 else "TIE_HOLD"
def coordinate_support(theta): return tuple(p for p in range(3) if theta[p]==0)
def frame_gate_identity(b1):
    j4=[[F(1)]*4 for _ in range(4)]
    phat=lin(mm(mm(b1,eye(6)),tr(b1)),j4,F(1,4),F(1,4))
    return phat==eye(4) and mm(b1,eye(6))==mm(phat,b1)

def main():
    b1,b2,b3=[boundary(S[k],S[k+1]) for k in range(3)]
    assert mm(b1,b2)==z(4,4) and mm(b2,b3)==z(6,1)
    assert lin(mm(tr(b1),b1),mm(b2,tr(b2)))==[[F(4 if i==j else 0) for j in range(6)] for i in range(6)]
    assert frame_gate_identity(b1)
    # Native skew Hodge-Dirac maps every nonzero C1 vector into C0+C2;
    # no nonzero C1 vector lies in an A-invariant subspace contained in C1.
    assert all(mm(tr(b1),b1)[i][j]+mm(b2,tr(b2))[i][j]==F(4 if i==j else 0)
               for i in range(6) for j in range(6))
    a=z(15,15); offs=(0,4,10,14)
    for k,b in enumerate((b1,b2,b3)):
        for i in range(len(b)):
            for j in range(len(b[0])):
                a[offs[k]+i][offs[k+1]+j]=-b[i][j]
                a[offs[k+1]+j][offs[k]+i]=b[i][j]
    a2=mm(a,a)
    assert mm(a2,a)==lin(z(15,15),a,cb=F(-4))
    oq=lin(lin(eye(15),a,cb=F(1,2)),a2,cb=F(1,4))
    oh=lin(eye(15),a2,cb=F(1,2))
    assert mm(oq,oq)==oh
    tq=[row[4:10] for row in oq[4:10]]
    th=[row[4:10] for row in oh[4:10]]
    assert tq==z(6,6) and th==lin(z(6,6),eye(6),cb=F(-1))
    assert mm(tq,tq)!=th # edge compression is not a composed C1 step transport

    pair=(1,1,1)
    # A concrete nonnegative K4 quadratic burden receipt, not fitted to an
    # endpoint: b=(0,2,1,3), W_p=sum_{e in opposite pair p}(B1^T b)_e^2.
    burden=[F(x) for x in (0,2,1,3)]
    gradients=[sum((b1[v][e]*burden[v] for v in range(4)),F(0)) for e in range(6)]
    matching=((0,5),(1,4),(2,3))
    w_native=tuple(sum((gradients[e]**2 for e in pair_edges),F(0)) for pair_edges in matching)
    assert w_native==(F(8),F(2),F(10))
    # Exact all-open fixed lineage: L-=L+=Q^3, F=I3, A_src=A_ren=0.
    # The v0.2 first-admissibility gates pass, but affine receipt is identity.
    static=(0,0,0); lplus_static=(0,1,2); mu_static=3-3
    winners,status=frozen_endpoint(static,mu_static,pair,w_native)
    assert status=="PASS" and winners==(static,)
    a_static=tuple(x^y for x,y in zip(static,winners[0]))
    assert a_static==(0,0,0)
    assert coordinate_support(winners[0])==lplus_static
    # Exact no-turnover two-seat lineage: B,C survive, F=I2, no additions.
    # The original shell optimizer can place the open seats at A,C.
    prior=(1,0,0); lplus=(1,2); mu=2-2
    endpoint,status=frozen_endpoint(prior,mu,pair,w_native)
    assert status=="PASS" and endpoint==((0,1,0),)
    assert coordinate_support(endpoint[0])==(0,2)!=lplus
    a_swap=tuple(x^y for x,y in zip(prior,endpoint[0]))
    assert a_swap==(1,1,0) and mu==0
    # All six strict burden rankings: 4 violate source-typed seat support.
    ranked=[]
    for w in itertools.permutations((F(1),F(2),F(3))):
        opt,state=frozen_endpoint(prior,mu,pair,w)
        assert state=="PASS"
        ranked.append(coordinate_support(opt[0])==lplus)
    assert ranked.count(True)==2 and ranked.count(False)==4
    # Source-complete seat equality admits only the coordinate complement.
    repaired=[x for x in itertools.product((0,1),repeat=3)
              if sum(x)==1 and coordinate_support(x)==lplus]
    assert repaired==[prior]
    # Zero budget is not a valid null-event veto: a typed sink plus addition
    # can exchange seats with q+=q-=2, with a!=0.
    swapped_plus=(0,2)
    swapped=[x for x in itertools.product((0,1),repeat=3)
             if coordinate_support(x)==swapped_plus]
    # In bases (B,C)->(A,C), a terminal B and novel A yield this exact map.
    f_swap=[[F(0),F(0)],[F(0),F(1)]]
    assert f_swap==tr(f_swap) and f_swap[0]==[F(0),F(0)] and f_swap[1]==[F(0),F(1)]
    n_sink=1; n_add=1
    assert n_sink-n_add==0
    assert swapped==[(0,1,0)] and sum(prior)==sum(swapped[0])
    assert tuple(x^y for x,y in zip(prior,swapped[0]))==(1,1,0)

    print(json.dumps({
      "status":"EXACT conditional counterexamples / source promotion unchanged",
      "native_C1":{"L1":"4 I6","C1_invariant_nonzero_subspace":False,
                   "compression_at_pi_over_4":"0","two_compressed_steps":"0",
                   "compressed_full_step":"-I6"},
      "all_open_static":{"frame":"identity pass","index":0,"endpoint":"000",
                         "affine_toggle":"000","v0_2_first_admissibility":"PASS_NOOP",
                         "proposed_theta_switch":"HOLD_NO_CHANGE"},
      "two_seat_counterexample":{"source_open_seats":["B","C"],"index":0,
        "source_typed_endpoint":"100","v0_2_optimizer_endpoint":"010",
        "v0_2_toggle":"110","support_mismatch":True,
        "burden_source":{"vertex_b":[0,2,1,3],"W_B2":[8,2,10]},
        "mismatched_strict_burden_rankings":"4/6"},
      "zero_budget_real_swap":{"source_open_seats_after":["A","C"],
        "source_typed_endpoint":"010","index":0,"toggle":"110"},
      "independent_OP03_target_scored":False,"physical_promotion":0
    },indent=2))

if __name__=="__main__": main()
