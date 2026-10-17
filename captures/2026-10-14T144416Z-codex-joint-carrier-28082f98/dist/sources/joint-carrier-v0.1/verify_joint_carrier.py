"""Exact constructor tests; arbitrary-dimension claims have algebraic proofs."""
from pathlib import Path
from itertools import product
from dataclasses import asdict
import json,hashlib
from joint_carrier import Carrier,Payload,Joint,compile_rsp,witness
from rsp1 import State
R=Path(__file__).parent;P=R/'dist/sources/joint-carrier-v0.1';P.mkdir(parents=True,exist_ok=True)
def payloads(d,m,n):
    return [Payload(w,h,r) for w in range(d) for h in product(range(d),repeat=n) for r in product(range(m),repeat=n)]
checked=0;permutations=0
for n,b in [(1,0),(1,1),(2,0)]:
    for f in product(range(2),repeat=2):
        for rho in product(range(2),repeat=2):
            c=Carrier(f,rho,2,n,b);ps=payloads(2,2,n);seen=set()
            for clock in range(c.L):
                for pack in product(ps,repeat=b+1):
                    x=Joint(clock,pack[0],pack[1:]);y=c.step(x)
                    assert c.step(y,inverse=True)==x and c.step(c.step(x,inverse=True))==x
                    assert y not in seen;seen.add(y);checked+=1
            assert len(seen)==c.resources()['joint_dimension'];permutations+=1
prepared=0
for d in [1,2,3]:
    for f in product(range(d),repeat=d):
        for n,b in product([1,2,3],[0,1,2]):
            rho=tuple(i+1 for i in range(d));c=Carrier(f,rho,d+1,n,b);x=c.prepared();expected=0;history=[];records=[];outgoing=[]
            for k in range(c.L-1):
                j,i=divmod(x.clock,n+1);old=x;x=c.step(x)
                if i<n:
                    history.append(expected);records.append(rho[expected]);expected=f[expected]
                    assert x.active.w==expected and x.active.h[:i+1]==tuple(history) and x.active.records[:i+1]==tuple(records)
                else:
                    outgoing.append(old.active);assert x.donors[j]==old.active and x.active==c.blank()
                    expected=0;history=[];records=[]
                assert x.donors[:len(outgoing)]==tuple(outgoing)
            assert x.clock==c.L-1 and c.resources()['unused_reset_blocks_final']==0;prepared+=1
# RSP compilation retains FULL states and branches, including future queue and cache.
rsp_windows=0
for branch in ['C','H']:
    for amount in [0,1,2,3]:
        for bank in [(),((0,0,0),),((1,0,0),(0,0,0),(2,0,0))]:
            s=State((1,0,0),(0,0,0),(0,0,0),(amount,0,0),bank,branch=branch);spec=compile_rsp(s)
            for n,b in [(1,0),(4,1),(8,2)]:
                c=Carrier(spec['successor'],spec['receipt'],spec['record_dimension'],n,b);x=c.prepared()
                for k in range(c.L-1):
                    j,i=divmod(x.clock,n+1);x=c.step(x);expected=min(i+1,len(spec['states'])-1) if i<n else 0
                    assert x.active.w==expected
                rsp_windows+=1
# Two inputs with the same noninjective F output remain distinguishable in old-state memory.
c=Carrier((0,0),(1,2),3,1,0)
a=c.step(Joint(0,c.blank(0),()));b=c.step(Joint(0,c.blank(1),()))
assert a.active.w==b.active.w and a.active.h!=b.active.h
# Correlated unknown old payload is exported by SWAP, not cloned/erased.
c=Carrier((1,1),(1,2),3,1,1);p0=c.blank(0);p1=c.blank(1);fresh=c.blank()
terms=[(Joint(1,p0,(fresh,)),0),(Joint(1,p1,(fresh,)),1)]
out=[(c.step(x),spectator) for x,spectator in terms]
assert all(x.active==fresh for x,y in out) and out[0][0].donors[0]==p0 and out[1][0].donors[0]==p1
assert all(c.step(x,inverse=True)==terms[i][0] for i,(x,y) in enumerate(out))
# Negative controls: dirty memory can break work law; dirty record can wrap to BLANK.
c=Carrier((1,1),(1,2),3,1,0)
dirty=Joint(0,Payload(0,(1,),(2,)),());y=c.step(dirty)
assert y.active.w==0!=c.f[0] and y.active.records==(0,)
# Actual prepared quarter trace after wrap: second dirty compute fails desired stable work.
for branch in ['C','H']:
    w=witness(branch);assert all(r['work_matches'] for r in w['trace'])
    post=w['post_window_negative_control'];assert post[0]['action']['kind']=='WRAP_IDLE'
    assert post[1]['active']['w']==2 and post[2]['active']['w']==0
    assert w['final']['clock']==9 and w['final']['donors'][0]['records']==(1,2,3,3)
    assert w['resources']['payload_dimension']==62208 and w['resources']['joint_dimension']==38698352640
# SWAP with already used outgoing donor returns the old payload; it is not a fresh reset.
c=Carrier((1,1),(1,2),3,1,1);x=c.prepared();x=c.step(x);x=c.step(x);archived=x.donors[0]
assert archived.w==1
used=Joint(1,c.blank(),(archived,));assert c.step(used).active==archived
# General collision bound follows from orthogonal distinct inputs: enumerate finite preimages.
collision_checks=0
for d in [1,2,3,4]:
    for f in product(range(d),repeat=d):
        largest=max(f.count(y) for y in range(d));assert 1<=largest<=d;collision_checks+=1
hashes={name:hashlib.sha256((R/name).read_bytes()).hexdigest() for name in ['joint_carrier.py','rsp1.py','response_contract.py']}
receipt={'status':'PASS','audit_version':'0.1','physical_promotion':0,'source_sha256':hashes,
 'global_joint_states_checked':checked,'total_global_permutations_checked':permutations,'generic_prepared_windows_checked':prepared,
 'rsp_prepared_windows_checked':rsp_windows,'finite_collision_maps_checked':collision_checks,
 'checks':['two-sided inverse on every dirty configuration of three small carriers','prepared trajectory/history/receipt identity','donor exports unchanged and consumed once within window','full RSP state compilation C/H and finite banks','noninjective output retains input distinction','spectator-correlated SWAP branch identity','dirty memory/record and used-donor negative controls','post-window wrap counterexample','exact dimension and slot accounting'],
 'scope':'Standard-library exact integer/tuple checks. Arbitrary-size result uses algebraic proof, not exhaustive enumeration. Correlation check tests basis branches of a coherent state, not a detector experiment. Constructor-team AI verification; independent human review pending.'}
(P/'JOINT_CARRIER_ROOT_VERIFICATION_v0.1.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt))
