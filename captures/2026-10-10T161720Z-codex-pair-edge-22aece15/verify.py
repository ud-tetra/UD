"""Exhaustive symmetry/capacity audit for pair-indexed to edge-indexed masks."""
from itertools import permutations, product
from pathlib import Path
import json

verts=range(4)
edges=tuple((i,j) for i in verts for j in verts if i<j)
pairs=(((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2)))
perms=tuple(permutations(verts))
def edge_image(g,e):return tuple(sorted((g[e[0]],g[e[1]])))
def pair_image(g,p):return next(i for i,P in enumerate(pairs) if {edge_image(g,e) for e in pairs[p]}==set(P))
def act_pair(g,bits):
    out=[None]*3
    for i,b in enumerate(bits):out[pair_image(g,i)]=b
    return tuple(out)
def act_edge(g,bits):return {edge_image(g,e):bits[e] for e in edges}
def lift(bits):return {e:bits[p] for p,P in enumerate(pairs) for e in P}
def admissible(T,L,q):return all(q[p]<=T[p] and T[p]*L[p]<=q[p] for p in range(3))
def hard(q,T):return lift(tuple(q[p]*T[p] for p in range(3)))

checks={}
def check(name,value):
    checks[name]=bool(value)
    assert value,name

kernel=tuple(g for g in perms if all(pair_image(g,p)==p for p in range(3)))
check('six_edges_three_opposite_pairs',len(edges)==6 and len(pairs)==3)
check('full_S4_action_24',len(perms)==24)
check('matching_action_kernel_V4_order_four',len(kernel)==4)
check('kernel_orbits_are_opposite_edge_pairs',
      all({edge_image(g,P[0]) for g in kernel}==set(P) for P in pairs))
check('kernel_fixes_all_pair_state_triples',all(
      act_pair(g,bits)==bits for g in kernel for bits in product((0,1),repeat=3)))
check('canonical_copy_lift_S4_equivariant',all(
      lift(act_pair(g,bits))==act_edge(g,lift(bits))
      for g in perms for bits in product((0,1),repeat=3)))

triples=tuple(product((0,1),repeat=3))
states=[(T,L,q) for T in triples for L in triples for q in triples if admissible(T,L,q)]
check('idle_mask_three_pair_admissible_states_125',len(states)==125)
check('all_admissible_triplets_stable_under_S4',all(
      admissible(act_pair(g,T),act_pair(g,L),act_pair(g,q))
      for g in perms for T,L,q in states))
check('candidate_hard_lift_equivariant_on_125_states',all(
      hard(act_pair(g,q),act_pair(g,T))==act_edge(g,hard(q,T))
      for g in perms for T,L,q in states))

def mask_tuple(m):return tuple(m[e] for e in edges)
image={mask_tuple(hard(q,T)) for T,L,q in states}
all_masks=set(product((0,1),repeat=6))
check('pair_only_candidate_image_exactly_eight_masks',len(image)==8)
check('56_Q167_algebraic_masks_outside_pair_constant_image',len(all_masks-image)==56)
check('all_image_masks_opposite_edge_constant',all(
      m[edges.index(P[0])]==m[edges.index(P[1])] for m in image for P in pairs))
check('asymmetric_single_edge_mask_excluded',tuple(int(e==(0,1)) for e in edges) not in image)

# A fixed pair-integrity/support receipt leaves the site's response bit free.
T=(1,0,0);L=(0,0,0)
q0=(0,0,0);q1=(1,0,0)
check('intact_null_two_admissible_responses',admissible(T,L,q0) and admissible(T,L,q1))
check('intact_null_hard_masks_diverge_under_candidate_bridge',hard(q0,T)!=hard(q1,T))

out={'claim_class':'EXACT S4 representation obstruction under pair-only state; edge/pair bridge CANDIDATE; predictive source OPEN',
     'carrier':'K4 six edges; three opposite-edge matching classes',
     'kernel_size':len(kernel),'kernel_orbits':[[list(e) for e in P] for P in pairs],
     'site_idle_mask_admissible_triples':len(states),
     'conditional_copy_bridge_mask_image_size':len(image),
     'full_six_edge_binary_mask_count':len(all_masks),
     'outside_copy_bridge':len(all_masks-image),
     'theorem':'every S4-equivariant map from any pair-indexed state with trivial V4 action to six edge bits is opposite-edge constant',
     'bridge_status':'copying pair q/T to edges is mathematical candidate only; no UD source identity',
     'checks':checks,'passed':sum(checks.values()),'physical_promotion':0,'independent_review':'PENDING'}
Path(__file__).with_name('results.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps({'passed':out['passed'],'admissible_states':len(states),'image_masks':len(image),'excluded_masks':len(all_masks-image)}))
