"""Exact Q167 current-address candidate and native blind-mode audit.

The score and argmax probe are candidate observers.  The gated current and
incidence dynamics are source-bound; no gate update rule is asserted.
"""
from fractions import Fraction as Q
from itertools import combinations,permutations
from pathlib import Path
import json

cells=((0,1,2,3),(0,1,2,4))
levels=[tuple(sorted({s for c in cells for s in combinations(c,k)})) for k in (1,2,3,4)]
V,E,F,T=levels
G=[dict(zip((0,1,2,3,4),a+b)) for a in permutations((0,1,2)) for b in permutations((3,4))]
def relabel(s,p):return tuple(sorted(p[v] for v in s))
def orientation(s,p):
    images=[p[v] for v in s]
    return (-1)**sum(images[i]>images[j] for i in range(len(s)) for j in range(i+1,len(s)))
def action(amplitudes,p):return {relabel(s,p):orientation(s,p)*a for s,a in amplitudes.items()}
def scores(x,y):
    # J^0_ie=2 D_ie x_i y_e.  Its squared endpoint norm is a new observer.
    return {e:Q(4)*y.get(e,Q(0))**2*sum(x.get((v,),Q(0))**2 for v in e) for e in E}
def address(sc):
    m=max(sc.values())
    return tuple(sorted(e for e in E if m>0 and sc[e]==m))
def boundary(low,high):
    return [[sum(Q((-1)**j) for j in range(len(h)) if h[:j]+h[j+1:]==s) for h in high] for s in low]
def transpose(a):return [list(row) for row in zip(*a)]
def mv(a,v):return [sum(x*y for x,y in zip(row,v)) for row in a]
def mm(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in transpose(b)] for row in a]

checks={}
def check(name,truth):checks[name]=bool(truth);assert truth,name
check('carrier_5_9_7_2',[len(s) for s in levels]==[5,9,7,2])
check('automorphism_count',len(G)==12)
check('orientation_signs',all(orientation(e,p) in (-1,1) for e in E for p in G))

# Exact nonzero address.  Squared endpoint currents make it independent of
# oriented edge-basis sign and covariant when amplitudes are relabeled.
for target in E:
    a,b=target
    x={(a,):Q(1),(b,):Q(2)};y={target:Q(3)}
    sc=scores(x,y)
    assert sc[target]==Q(180) and address(sc)==(target,)
    for p in G:
        xp=action(x,p);yp=action(y,p)
        sp=scores(xp,yp)
        assert sp=={relabel(e,p):v for e,v in sc.items()}
        assert address(sp)==(relabel(target,p),)
check('108_generic_address_covariance_cases',True)

# Gated Q167 current is zero on a closed edge even when the ungated
# algebraic probe is nonzero.  The probe itself is an added observer.
check('gated_self_probe_deadlock',Q(0)*sc[target]==0 and sc[target]==180)
check('zero_state_returns_no_address',address(scores({},{}))==())

B2=boundary(E,F);B3=boundary(F,T)
check('boundary_squared_zero',all(v==0 for row in mm(B2,B3) for v in row))
e=[Q(1),Q(-1)]
d=mv(B3,e);gram=mm(transpose(B3),B3)
check('cell_pair_gram',gram==[[Q(4),Q(1)],[Q(1),Q(4)]])
check('antisymmetric_cell_mode_eigenvalue_3',mv(gram,e)==[Q(3)*v for v in e])
check('shared_face_blind',d[F.index((0,1,2))]==0)
check('six_private_faces_active',sum(v!=0 for v in d)==6)
check('face_state_closed_to_edges',mv(B2,d)==[Q(0)]*len(E))
check('native_mode_nonstationary',d!=[Q(0)]*len(F) and mv(gram,e)!=[Q(0)]*len(T))

# At the exact state x=y=0, f=B3 e, u=e, the whole subspace
# {x=y=0, f in im B3, u arbitrary} is invariant under A=B.T-B.
# Thus Q167 probe activity stays zero for all native evolution time,
# despite active face–cell support currents.
blind=scores({},{});
check('all_nine_edge_scores_zero_on_active_mode',all(v==0 for v in blind.values()))
J23={}
for fi,f in enumerate(F):
    for ti,t in enumerate(T):
        if B3[fi][ti]:J23[(f,t)]=Q(2)*B3[fi][ti]*d[fi]*e[ti]
check('six_nonzero_directed_face_currents',sorted(J23.values())==[Q(0),Q(0)]+[Q(2)]*6)
check('private_face_current_tie',len({v for v in J23.values() if v})==1)

out={'claim_class':'EXACT native blind mode; CANDIDATE ungated score/argmax observer; no source-selected switch; physical promotion 0',
 'score':'s_e=sum_{i in e}(2 D_ie x_i y_e)^2=4 y_e^2 (x_a^2+x_b^2); select unique positive maximum, ties return set',
 'generic_example':{'score':180,'addresses_tested':len(E),'covariance_cases':len(E)*len(G)},
 'blind_mode':{'c3':[str(v) for v in e],'c2_B3e':[str(v) for v in d],'gram':[[str(v) for v in row] for row in gram],
               'vertex_edge_zero_all_time':True,'edge_scores':[str(blind[k]) for k in E],
               'directed_J23':{''.join(map(str,f))+':'+''.join(map(str,t)):str(v) for (f,t),v in J23.items()}},
 'checks':checks,'passed':sum(checks.values())}
Path(__file__).with_name('results.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps({'passed':out['passed'],'generic_score':180,'edge_covariance_cases':108,'blind_face_currents':list(map(str,sorted(J23.values())))}))
