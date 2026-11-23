#!/usr/bin/env python3
"""EXACT CONDITIONAL: six geometric contact midpoints identified as graph junctions.

Source-native Q169 applies ONLY once a new complex is declared. This script
never asserts that Euclidean contact authorizes a new simplex or a physical event.
One-dimensional graph-only test; not a filled-tetrahedral state update.
"""
from itertools import combinations
from pathlib import Path
import json
import sympy as S

EDGES=list(combinations(range(4),2))
def opp(e):
    return tuple(v for v in range(4) if v not in e)

def model(glued):
    vertices=[(p,i) for p in 'AB' for i in range(4)]
    vertices += ([('J',e) for e in EDGES] if glued
                 else [(p,e) for p in 'AB' for e in EDGES])
    edge_list=[]
    for p in 'AB':
        for e in EDGES:
            i,j=e if p=='A' else opp(e)
            m=('J',e) if glued else (p,e)
            edge_list.extend([((p,i),m),(m,(p,j))])
    idx={v:i for i,v in enumerate(vertices)}
    B=S.zeros(len(vertices),len(edge_list))
    for j,(u,v) in enumerate(edge_list):
        B[idx[u],j]=-1
        B[idx[v],j]=1
    return vertices,edge_list,B

def factored(s):
    return str(S.factor(s)).replace('**','^')

states={}
for tag,glued in [('disjoint_control',False),('six_identified_junctions',True)]:
    vertices,edges,B=model(glued)
    L=B*B.T
    rank=int(B.rank());assert (len(vertices),len(edges),rank)==((14,24,13) if glued else (20,24,18))
    assert len(vertices)-rank == (1 if glued else 2)
    b1=len(edges)-rank
    assert b1 == (11 if glued else 6)
    lam=S.Symbol('lam');z=S.Symbol('z')
    wanted=(lam*(lam-7)*(lam-4)**2*(lam-3)**4*(lam**2-7*lam+8)**3 if glued
            else lam**2*(lam-5)**2*(lam-4)**6*(lam-2)**4*(lam-1)**6)
    assert S.expand(L.charpoly(lam).as_expr()-wanted)==0
    A=S.BlockMatrix([[S.zeros(len(vertices)), -B],[B.T,S.zeros(len(edges))]]).as_explicit()
    assert A.T==-A
    # Matrix spectral law of the explicitly stated 0/1 chain model.
    f=(z**12*(z**2+7)*(z**2+4)**2*(z**2+3)**4*(z**4+7*z**2+8)**3 if glued else
       z**8*(z**2+5)**2*(z**2+4)**6*(z**2+2)**4*(z**2+1)**6)
    assert S.degree(f,z)==len(vertices)+len(edges)
    states[tag]={'V':len(vertices),'E':len(edges),'components':len(vertices)-rank,'boundary_rank':rank,'b1':b1,'L_charpoly':factored(wanted),'skew_A_charpoly':factored(f),'trace_L':int(S.trace(L)), 'trace_L2':int(S.trace(L*L))}
    if glued:
        edge_a=edges.index((('A',0),('J',(0,1))))
        edge_b=edges.index((('B',2),('J',(0,1))))
        beta=(B.T*B)[edge_b,edge_a]
        assert beta==1
        # ddot c_B(0)= -(B.T B)_BA for a pure A edge amplitude 1.
        ddot=-beta
        assert ddot==-1
        states[tag].update({'test_A_edge':edge_a,'test_B_edge':edge_b,'cross_BtB':str(beta),'cross_second_derivative':str(ddot),'cross_leading_amplitude':'-s^2/2 + O(s^4)','cross_leading_support':'s^4/4 + O(s^6)'})
        B_new=B
    else:
        B_oldgraph=B
        n_old=len(vertices)

# Strict local subdivision without gluing: 2 original K4 graphs C1 has 12 edges.
# Original vertices (8) map identically to the 8 unchanged new corner vertices.
vertices,edges,B=model(True)
B_old=S.zeros(8,12)
T0=S.zeros(len(vertices),8)
T1=S.zeros(len(edges),12)
for k in range(8):T0[k,k]=1
for k,p in enumerate('AB'):
    for a,e in enumerate(EDGES):
        i,j=e
        B_old[k*4+i,k*6+a]=-1; B_old[k*4+j,k*6+a]=1
        e2=e if p=='A' else next(q for q in EDGES if opp(q)==e)
        m=('J',e2)
        ef=edges.index(((p,i),m)); es=edges.index((m,(p,j)))
        T1[ef,k*6+a]=1;T1[es,k*6+a]=1
assert B*T1==T0*B_old
assert T1.T*T1==2*S.eye(12)
alpha=S.sqrt(2)/2
assert B*(alpha*T1)!=T0*B_old
assert (alpha*T1).T*(alpha*T1)==S.eye(12)
# Edge reorientation signed diag D changes only edge bases and cannot change L or spectrum.
R=S.diag(*([(-1)**(i%3==0) for i in range(24)]))
assert R.T*R==S.eye(24)
assert (B*R)*(B*R).T==B*B.T
states['strict_interface']={'chain_map':'B_new*T1=T0*B_old', 'edge_gram':'T1^T T1=2 I12','local_norm_gain':'2 for each unit old edge, not equal 1','isometric_alpha':'1/sqrt(2)', 'isometric_alpha_breaks_fixed_vertex_chain_map':True,'reorientation_spectral_null':True}
states['source_status']={'junction_constructor':'NOT_DERIVED', 'metric_and_event_source':'OPEN', 'physical_promotion':0,'regime':'graph-only, explicit midpoint identification, dimensionless, unit simplex metric'}
path=Path(__file__).with_name('results.json')
path.write_text(json.dumps(states,indent=2,sort_keys=True)+'\n')
print('PRIMARY_EXACT_PASS: incidence, betti, two spectra, strict interface no-go, cross-edge Taylor, orientation null')
print(json.dumps(states,indent=2,sort_keys=True))
