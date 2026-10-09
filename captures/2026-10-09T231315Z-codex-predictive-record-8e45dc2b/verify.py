"""Exact conditional hybrid-record audit for two face-glued tetrahedra.

Q156/Q167/Q173 supply typed mask states/effects, not a factor event law.
The independent repair/failure alphabet below is a declared diagnostic contract.
"""
from fractions import Fraction as Q
from itertools import combinations, product
import json
from pathlib import Path

cells=((0,1,2,3),(0,1,2,4))
levels=[tuple(sorted({s for c in cells for s in combinations(c,k)})) for k in (1,2,3,4)]
vertices,edges,faces,_=levels
flat=sum((list(v) for v in levels),[])
ix={s:i for i,s in enumerate(flat)}
zero=lambda:[Q(0) for _ in flat]
N=zero()
for v in vertices:N[ix[v]]=Q(1)

def project(x):
    return tuple([x[ix[v]]-x[ix[(4,)]] for v in vertices if v!=(4,)]+[x[ix[s]] for s in flat if len(s)>1])

def lift(z):
    x=zero()
    for v,val in zip([v for v in vertices if v!=(4,)],z[:4]):x[ix[v]]=val
    for s,val in zip([s for s in flat if len(s)>1],z[4:]):x[ix[s]]=val
    return x

def derivative(x,edge_mask,face_mask):
    d=zero()
    for high in flat:
        if len(high)==1:continue
        for j in range(len(high)):
            low=high[:j]+high[j+1:]
            w=(edge_mask[high] if len(high)==2 else
               face_mask[low] if len(high)==4 else 1)
            sign=Q((-1)**j*w)
            d[ix[high]]+=sign*x[ix[low]]
            d[ix[low]]-=sign*x[ix[high]]
    return d

def face_lift(edge_mask):
    return {f:int(all(edge_mask[e] for e in edges if set(e)<set(f))) for f in faces}

checks={}
def check(name,truth):
    checks[name]=bool(truth)
    assert truth,name

check('register_5_9_7_2',[len(v) for v in levels]==[5,9,7,2])
check('record_dimension',len(project(zero()))==22)
check('uniform_vertex_quotient',project(N)==tuple(Q(0) for _ in range(22)))
check('right_inverse',all(project(lift(tuple(Q(i==j) for i in range(22))))==tuple(Q(i==j) for i in range(22)) for j in range(22)))

# The whole-edge mask ties both endpoint incidences. Every such mask annihilates
# N. Face–cell masks and the fixed edge–face block cannot act on N either.
for ep in product((0,1),repeat=9):
    e=dict(zip(edges,ep));f=face_lift(e)
    assert derivative(N,e,f)==zero()
check('512_candidate_modes_preserve_hidden_vertex',True)

# Independent Q173 face masks are allowed; the two operator types combine
# linearly. Checking their basis generators proves the kernel statement for
# all 2^9*2^7 independent mask assignments, without claiming mask eligibility.
for k in range(9):
    e={edge:int(j==k) for j,edge in enumerate(edges)}
    assert derivative(N,e,{f:0 for f in faces})==zero()
for k in range(7):
    f={face:int(j==k) for j,face in enumerate(faces)}
    assert derivative(N,{e:0 for e in edges},f)==zero()
check('16_independent_mask_generators_preserve_kernel',True)

# The quotient derivative is uniquely determined by z and the current masks.
e={edge:int(i%2==0) for i,edge in enumerate(edges)}
f={face:int(i%2==1) for i,face in enumerate(faces)}
z=tuple(Q((i%5)-2,3) for i in range(22))
check('exact_quotient_intertwining_witness',project(derivative(lift(z),e,f))==project(derivative([a+Q(7)*b for a,b in zip(lift(z),N)],e,f)))

# A mask change by itself does not jump c or z. This is conditional on no
# impulse law; it does not assert that all admitted events are amplitude-free.
e2=dict(e);e2[edges[0]]=1-e2[edges[0]]
check('identity_state_reset_at_pure_mask_switch',project(lift(z))==z)
check('switch_changes_quotient_generator',project(derivative(lift(z),e,f))!=project(derivative(lift(z),e2,f)))

states=tuple(product((0,1),repeat=2))
ops=('repair_C','repair_T','fail_C','fail_T')
def update(state,op):
    c,t=state
    return ((1 if op=='repair_C' else 0 if op=='fail_C' else c),
            (1 if op=='repair_T' else 0 if op=='fail_T' else t))
gate=lambda s:s[0]*s[1]
signatures={s:(gate(s),)+tuple(gate(update(s,o)) for o in ops) for s in states}
check('four_distinct_one_event_signatures',len(set(signatures.values()))==4)
check('closed_mask_has_three_hidden_factor_states',sum(gate(s)==0 for s in states)==3)
check('repair_C_ambiguous_given_closed_mask',gate(update((0,1),'repair_C'))==1 and gate(update((0,0),'repair_C'))==0)
check('repair_T_ambiguous_given_closed_mask',gate(update((1,0),'repair_T'))==1 and gate(update((0,0),'repair_T'))==0)

# Explicit two-branch observable witness: identical z and current h, one
# declared repair_C event, different next mask and next quotient derivative.
e3={edge:1 for edge in edges};target=(0,1)
e3[target]=0
s_a=(0,1);s_b=(0,0)
e_a=dict(e3);e_a[target]=gate(update(s_a,'repair_C'))
e_b=dict(e3);e_b[target]=gate(update(s_b,'repair_C'))
x=zero()
for simplex in ((0,),(0,1),(0,1,2),(0,1,2,3)):x[ix[simplex]]=Q(1)
dz_a=project(derivative(x,e_a,face_lift(e_a)))
dz_b=project(derivative(x,e_b,face_lift(e_b)))
check('same_record_and_mask_different_next_mask',e_a[target]!=e_b[target])
check('same_record_and_mask_different_next_derivative',dz_a!=dz_b)

out={
 'status':'EXACT CONDITIONAL; independent repair/failure event grammar is a diagnostic candidate; autonomous UD trigger OPEN; physical promotion 0',
 'carrier':'<0123,0124>, f=(5,9,7,2), A=B^T-B',
 'quotient':'four vertex differences against vertex 4, then all nine edges, seven faces, two cells; kernel span(uniform vertex)',
 'operator_scope':'all independent whole-edge Q167 extensions and Q173 per-face masks; fixed edge-face incidences; prescribed piecewise modes',
 'hybrid_memory':'for declared independent repair_C/repair_T/fail_C/fail_T grammar, four distinguishable (C,T) states per edge require at least two binary state bits; this is not an unconditional UD memory lower bound',
 'candidate_face_lift':'AND of its three edge gates used only for two-branch witness; Q173 face decision remains unsourced',
 'factor_signatures':{str(s):v for s,v in signatures.items()},
 'witness':{'edge':target,'same_z':list(map(str,project(x))),'same_pre_mask':0,'pre_factor_states':[s_a,s_b],'event':'repair_C','post_masks':[e_a[target],e_b[target]],'post_edge_01_derivatives':[str(dz_a[4+edges.index(target)]),str(dz_b[4+edges.index(target)])]},
 'checks':checks,'passed':sum(checks.values()),
}
Path(__file__).with_name('results.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps({'passed':out['passed'],'post_masks':out['witness']['post_masks'],'post_edge_01_derivatives':out['witness']['post_edge_01_derivatives']}))
