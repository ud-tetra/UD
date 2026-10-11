#!/usr/bin/env python3
"""Independent bit-mask census of proposed OP03 v0.2.1 null/seat guards."""
import itertools
import json

BITS=range(8)
PAIRS=range(3)
WEIGHTS=list(itertools.product(range(3),repeat=3))
PERMS=list(itertools.permutations(PAIRS))

def bit(x,p): return (x>>p)&1
def pop(x): return x.bit_count()
def opens(theta): return (~theta)&7
def transform(x,perm):
    return sum(bit(x,i)<<perm[i] for i in PAIRS)
def transform_w(w,perm):
    out=[0]*3
    for i in PAIRS: out[perm[i]]=w[i]
    return tuple(out)
def original(theta,seat,integrity,w):
    # Independent reimplementation of v0.2 §7: address optimizer sees only
    # the Hamming shell q+=|seat| and pair integrity, not the typed seat map.
    candidates=[x for x in BITS if pop(opens(x))==pop(seat)
                and not (opens(x)&~integrity&7)]
    if not candidates: return None,"INFEASIBLE"
    scores=[sum(bit(x,p)*w[p] for p in PAIRS) for x in candidates]
    best=min(scores); winners=[x for x,s in zip(candidates,scores) if s==best]
    return (winners[0],"PASS") if len(winners)==1 else (None,"TIE")
def typed_guard(theta,seat,integrity):
    # Source-complete coordinate-seat reading: a θ endpoint is possible only
    # when its open-seat support equals the frozen viable-output support.
    if seat&~integrity&7: return None,"SEAT_INTEGRITY_HOLD"
    endpoint=(~seat)&7
    toggle=theta^endpoint
    return endpoint,"NO_CHANGE" if toggle==0 else "THETA_SWITCH"

def main():
    counts={"total":0,"seat_integrity_hold":0,"no_change":0,"theta_switch":0,
            "zero_index_switch":0,"legacy_unique":0,"legacy_typed_mismatch":0,
            "legacy_tie":0,"legacy_infeasible":0}
    equivariance_checks=0
    for theta in BITS:
        for seat in BITS:
            mu=pop(opens(theta))-pop(seat)
            for integrity in BITS:
                expected,status=typed_guard(theta,seat,integrity)
                for w in WEIGHTS:
                    counts["total"]+=1
                    candidate,legacy=original(theta,seat,integrity,w)
                    if legacy=="PASS":
                        counts["legacy_unique"]+=1
                        if status!="SEAT_INTEGRITY_HOLD" and candidate!=expected:
                            counts["legacy_typed_mismatch"]+=1
                    else:
                        counts["legacy_tie" if legacy=="TIE" else "legacy_infeasible"]+=1
                    if status=="SEAT_INTEGRITY_HOLD": counts["seat_integrity_hold"]+=1
                    elif status=="NO_CHANGE": counts["no_change"]+=1
                    else:
                        counts["theta_switch"]+=1
                        if mu==0: counts["zero_index_switch"]+=1
                    assert (status=="NO_CHANGE")==(expected==theta) if expected is not None else True
                    assert expected is None or pop(expected)-pop(theta)==mu
                    for perm in PERMS:
                        thp=transform(theta,perm); sp=transform(seat,perm)
                        ip=transform(integrity,perm); wp=transform_w(w,perm)
                        check,state=typed_guard(thp,sp,ip)
                        assert state==status
                        assert check==(None if expected is None else transform(expected,perm))
                        # For strict unique optimizer cases its original
                        # coordinate permutation must also commute with S3.
                        if legacy=="PASS":
                            pc,ps=original(thp,sp,ip,wp)
                            assert ps==legacy and pc==transform(candidate,perm)
                        equivariance_checks+=1
    assert counts["total"]==8*8*8*27
    assert sum(counts[k] for k in ("seat_integrity_hold","no_change","theta_switch"))==counts["total"]
    assert counts["legacy_typed_mismatch"]>0 and counts["zero_index_switch"]>0
    assert typed_guard(0,7,7)==(0,"NO_CHANGE")
    assert original(1,6,7,(8,2,10))==(2,"PASS")
    assert typed_guard(1,6,7)==(1,"NO_CHANGE")
    assert typed_guard(1,5,7)==(2,"THETA_SWITCH")
    # The non-coordinate line span(1,1,1) is S3-fixed, whereas no singleton
    # coordinate seat is S3-fixed. Hence no universal equivariant rank-one
    # seat selector exists without additional typed address information.
    invariant_line=(1,1,1)
    assert all(transform_w(invariant_line,p)==invariant_line for p in PERMS)
    assert not any(all(transform(1<<i,p)==1<<i for p in PERMS) for i in PAIRS)
    print(json.dumps({"status":"EXACT finite guard census, conditional coordinate-seat semantics",
                      "counts":counts,"S3_equivariance_cases":equivariance_checks,
                      "generic_noncoordinate_rank_one_equivariant_selector":"NO_GO",
                      "independent_endpoints_scored":0,"physical_promotion":0},indent=2))

if __name__=="__main__": main()
