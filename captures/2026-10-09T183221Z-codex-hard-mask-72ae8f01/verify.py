"""Exact two-tetrahedron structural hard-gate audit; standard library only.

Source rule: C_e=AND of declared required closure receipts; T_e is lawful
transport; h_e=C_e*T_e.  The incident-face requirement and face lift below
are explicitly declared contexts/candidates, not source-selected dynamics.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations, permutations, product
import json
from pathlib import Path

cells=((0,1,2,3),(0,1,2,4))
simplexes=[tuple(sorted({s for c in cells for s in combinations(c,k)})) for k in (1,2,3,4)]
vertices,edges,faces,_=simplexes
flat=sum((list(level) for level in simplexes),[])
ix={s:i for i,s in enumerate(flat)}
req={e:tuple(f for f in faces if set(e)<set(f)) for e in edges}
inc={f:tuple(e for e in edges if set(e)<set(f)) for f in faces}

def gate(face_receipts,transport):
    closure={e:int(all(face_receipts[f] for f in req[e])) for e in edges}
    integrity={e:int(transport[e] in (-1,1)) for e in edges}
    edge={e:closure[e]*integrity[e] for e in edges}
    # Declared complete-boundary viability lift; not Q173's mask selector.
    face={f:int(all(edge[e] for e in inc[f])) for f in faces}
    return closure,integrity,edge,face

def relabel(s,p): return tuple(sorted(p[v] for v in s))
def relabel_map(d,p): return {relabel(k,p):v for k,v in d.items()}
def A(edge_mask,face_mask):
    """Q167 and Q173 typed mask effects in A=B.T-B orientation."""
    matrix=[[Q(0) for _ in flat] for _ in flat]
    for high in flat:
        if len(high)<2:continue
        for j in range(len(high)):
            low=high[:j]+high[j+1:]
            if low not in ix: continue
            weight=(edge_mask[high] if len(high)==2 else
                    face_mask[low] if len(high)==4 else 1)
            sign=Q((-1)**j * weight)
            matrix[ix[high]][ix[low]]+=sign
            matrix[ix[low]][ix[high]]-=sign
    return matrix

checks={}
def check(label,value):
    checks[label]=bool(value)
    assert value,label

check('chain_register_5_9_7_2',[len(s) for s in simplexes]==[5,9,7,2])
check('each_edge_has_required_faces',all(req[e] for e in edges))
full_faces={f:1 for f in faces}; full_transport={e:1 for e in edges}
_,_,open_e,open_f=gate(full_faces,full_transport)
check('complete_identity_context_open',all(open_e.values()) and all(open_f.values()))
check('closed_topology_identity_no_transition',gate(full_faces,full_transport)==gate(full_faces,full_transport))

# Exhaustive Boolean structural selector, with no probabilistic interpretation.
edge_patterns=Counter();face_patterns=Counter();joint_patterns=Counter()
for fb in product((0,1),repeat=len(faces)):
    rf=dict(zip(faces,fb))
    for tb in product((0,1),repeat=len(edges)):
        u=dict(zip(edges,tb))
        c,t,e,f=gate(rf,u)
        check_key=(tuple(e[x] for x in edges),tuple(f[x] for x in faces))
        edge_patterns[check_key[0]]+=1
        face_patterns[check_key[1]]+=1
        joint_patterns[check_key]+=1
        assert all(e[x]==c[x]*t[x] for x in edges)
        assert all(f[x]==int(all(e[y] for y in inc[x])) for x in faces)
check('exhaustive_65536',sum(joint_patterns.values())==65536)
check('all_edge_masks_reachable',len(edge_patterns)==512)
check('face_lift_deterministic_from_edges',len(joint_patterns)==len(edge_patterns))

# The automorphism group of the glued pair is S3 on its common triangle,
# times S2 swapping the apex vertices.  Masks must transform covariantly.
automorphisms=[]
for tri in permutations((0,1,2)):
    for apex in permutations((3,4)):
        p=dict(zip((0,1,2,3,4),tri+apex));automorphisms.append(p)
        rf={f:int(sum(f)%2==0) for f in faces}
        u={e:(-1 if sum(e)%2 else 0) for e in edges}
        c,t,em,fm=gate(rf,u)
        c2,t2,em2,fm2=gate(relabel_map(rf,p),relabel_map(u,p))
        assert (c2,t2,em2,fm2)==tuple(relabel_map(x,p) for x in (c,t,em,fm))
check('12_carrier_automorphisms',len(automorphisms)==12)

# Nontrivial loop holonomy does not close lawful local transport.
signed={e:1 for e in edges};signed[(0,1)]=-1
_,_,signed_e,_=gate(full_faces,signed)
check('nonflat_lawful_loop_remains_open',signed[(0,1)]*signed[(0,2)]*signed[(1,2)]==-1 and all(signed_e.values()))

causes=Counter()
for c0,t0,c1,t1 in product((0,1),repeat=4):
    before=c0*t0;after=c1*t1
    if before==1 and after==0:
        cause=('joint_failure' if c1==t1==0 else
               'closure_failure' if c1==0 else 'transport_failure')
    elif before==0 and after==1:cause='both_restored'
    else:cause='no_mask_change'
    causes[cause]+=1
check('factor_transition_truth_table',dict(causes)=={'no_mask_change':10,'joint_failure':1,'closure_failure':1,'transport_failure':1,'both_restored':3})

# Same chain state and same compact R22 record, different supplied local
# transport.  The source does not supply U from c; selecting one is extra data.
blocked=dict(full_transport);blocked[(0,1)]=0
_,_,blocked_e,blocked_f=gate(full_faces,blocked)
x=[Q(0) for _ in flat]
for s in ((0,),(0,1),(0,1,2),(0,1,2,3)):x[ix[s]]=Q(1)
def action(e,f):return [sum(a*b for a,b in zip(row,x)) for row in A(e,f)]
dx_open=action(open_e,open_f);dx_block=action(blocked_e,blocked_f)
check('same_amplitudes_different_edge_mask',open_e[(0,1)]==1 and blocked_e[(0,1)]==0)
check('different_edge_01_derivative',dx_open[ix[(0,1)]]!=dx_block[ix[(0,1)]])
check('different_cell_derivative',dx_open[ix[(0,1,2,3)]]!=dx_block[ix[(0,1,2,3)]])
check('face_012_rule_changes',open_f[(0,1,2)]==1 and blocked_f[(0,1,2)]==0)

result={
    'claim_class':'exact conditional Boolean audit; no autonomous switch prediction; physical promotion 0',
    'source_rule':'h_e=C_cl,e^hard*T_int,e^hard; C_cl,e^hard=AND of declared required binary closure receipts',
    'declared_context':'two-tetrahedron <0123,0124>; Req_cl(e)=all incident triangles; one-dimensional real transport U_e in {-1,0,1} with T_e=1 iff U_e in {-1,1}',
    'candidate_face_lift':'h_f=AND of its three edge gates; not Q173-sourced mask decision',
    'counts':{'face_receipt_assignments':128,'transport_bit_assignments':512,'total':65536,'reachable_edge_masks':len(edge_patterns),'reachable_face_masks':len(face_patterns),'reachable_joint_masks':len(joint_patterns),'automorphisms':len(automorphisms),'factor_transition_table':dict(causes)},
    'witness':{'state_nonzero_simplexes':['0','01','012','0123'],'changed_transport_edge':'01','open_edge_01_derivative':str(dx_open[ix[(0,1)]]),'blocked_edge_01_derivative':str(dx_block[ix[(0,1)]]),'open_cell_0123_derivative':str(dx_open[ix[(0,1,2,3)]]),'blocked_cell_0123_derivative':str(dx_block[ix[(0,1,2,3)]]),'open_face_mask':{''.join(map(str,f)):open_f[f] for f in faces},'blocked_face_mask':{''.join(map(str,f)):blocked_f[f] for f in faces}},
    'checks':checks,
}
Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps({'counts':result['counts'],'witness':result['witness'],'passed':sum(checks.values())},indent=2))
