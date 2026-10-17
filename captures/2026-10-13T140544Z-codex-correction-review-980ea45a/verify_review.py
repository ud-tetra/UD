#!/usr/bin/env python3
"""Exact constructor review of labels, domains and signed ray semantics."""
import argparse
import hashlib
import itertools
import json
import sys
from pathlib import Path
from fractions import Fraction as F
sys.dont_write_bytecode=True
import verify_source_corrections as v

ROOT=Path(__file__).resolve().parent
OLD_MINUS=[(0,1,2,3),(0,1,2,4)]
MINUS=[(0,2,3,4),(1,2,3,4)]
PLUS=[(0,1,2,3),(0,1,2,4),(0,1,3,4)]

def outer_faces(cells):
    counts={}
    for cell in cells:
        for face in itertools.combinations(cell,3):
            counts[face]=counts.get(face,0)+1
    return sorted(face for face,count in counts.items() if count==1)

def oriented_boundary(cells,coefficients):
    out={}
    for cell,c in zip(cells,coefficients):
        for i in range(4):
            face=cell[:i]+cell[i+1:]
            out[face]=out.get(face,0)+c*(-1)**i
    return {face:c for face,c in sorted(out.items()) if c}

def flatten(basis): return [s for grade in basis for s in grade]

def signed_relabel(source,target,permutation):
    source=flatten(source);target=flatten(target)
    index={s:i for i,s in enumerate(target)}
    p=v.z(len(target),len(source))
    for j,s in enumerate(source):
        values=[permutation[k] for k in s]
        inversions=sum(values[i]>values[k] for i in range(len(values)) for k in range(i+1,len(values)))
        p[index[tuple(sorted(values))]][j]=F((-1)**inversions)
    assert v.mul(v.tr(p),p)==v.eye(len(source))
    assert v.mul(p,v.tr(p))==v.eye(len(target))
    return p

def embed(basis,ambient):
    source=flatten(basis);target=flatten(ambient);index={s:i for i,s in enumerate(target)}
    p=v.z(len(target),len(source))
    for j,s in enumerate(source): p[index[s]][j]=F(1)
    assert v.mul(v.tr(p),p)==v.eye(len(source))
    return p

def run():
    old,oldb,olda,oldl=v.complex_from_cells(OLD_MINUS)
    minus,mb,ma,ml=v.complex_from_cells(MINUS)
    plus,pb,pa,pl=v.complex_from_cells(PLUS)
    ambient,_,_,_=v.complex_from_cells(list(itertools.combinations(range(5),4)))
    assert list(map(len,ambient))==[5,10,10,5]
    old_outer=outer_faces(OLD_MINUS);minus_outer=outer_faces(MINUS);plus_outer=outer_faces(PLUS)
    assert old_outer!=plus_outer  # negative control for the v0.1 labeling
    assert minus_outer==plus_outer and len(minus_outer)==6
    minus_oriented=oriented_boundary(MINUS,[1,-1])
    plus_oriented=oriented_boundary(PLUS,[1,-1,1])
    assert minus_oriented==plus_oriented
    # Relabel all of the old K_minus representative, including incidence signs.
    permutation={0:2,1:3,2:4,3:0,4:1}
    assert sorted(tuple(sorted(permutation[k] for k in cell)) for cell in OLD_MINUS)==MINUS
    p=signed_relabel(old,minus,permutation)
    assert v.mul(v.mul(p,olda),v.tr(p))==ma
    p1=[row[5:14] for row in p[5:14]]  # C1 block in the two-cell 23D register
    assert v.mul(v.mul(p1,oldl),v.tr(p1))==ml
    assert v.spectral_check(oldl,[3,5])==v.spectral_check(ml,[3,5])
    im=embed(minus,ambient);ip=embed(plus,ambient)
    am=v.mul(v.mul(im,ma),v.tr(im));ap=v.mul(v.mul(ip,pa),v.tr(ip))
    difference=v.sub(ap,am)
    assert v.rank(difference)==18 and 30-v.rank(difference)==12
    assert v.iszero(v.add(difference,v.tr(difference)))
    # One-edge skew fixture: oriented generator and a self-adjoint replacement
    # cannot both be passed as the same real-flow generator.
    a=[[F(0),F(-1)],[F(1),F(0)]]
    self_adjoint=[[F(0),F(1)],[F(1),F(0)]]
    assert v.iszero(v.add(a,v.tr(a)))
    assert not v.iszero(v.add(self_adjoint,v.tr(self_adjoint)))
    # A sign flip preserves a rank-one projector, but not a signed PSR root.
    x=[[F(1)],[F(0)]];negative=v.scale(x,-1)
    assert v.mul(x,v.tr(x))==v.mul(negative,v.tr(negative))
    assert x!=negative
    # At eta -> 0, a scalar device with unequal broadenings already contradicts
    # a generic unit-transmission conclusion, even at exact resonance.
    gamma_left=F(1);gamma_right=F(2)
    resonance=4*gamma_left*gamma_right/(gamma_left+gamma_right)**2
    assert resonance==F(8,9) and resonance<1
    # Revalidate copied source bindings used by the base correction replay.
    old_sources=ROOT/'sources'
    bindings={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(old_sources.iterdir()) if p.is_file()}
    out={
        'status':'PASS','review_kind':'constructor self-review; not independent',
        'physical_promotion':0,'registry_entry':False,'numerical_target_evaluated':False,
        'old_pair_boundary_match':False,'new_pair_boundary_match':True,
        'oriented_outer_boundary_match':True,'outer_faces':minus_outer,
        'pair_cells':{'K_minus':MINUS,'K_plus':PLUS},
        'shared_face_removed':[2,3,4],'interior_edge_added':[0,1],
        'K_minus_relabel_spectral_and_generator_covariance':True,
        'ambient_f_vector':[5,10,10,5],'ambient_chain_dimension':30,
        'generator_difference_rank':18,'generator_difference_kernel_dimension':12,
        'rank_one_projector_sign_ambiguity_witness':True,
        'self_adjoint_real_generator_negative_control_rejected':True,
        'unequal_lead_resonance_transmission':resonance,
        'reviewed_source_sha256':bindings,
        'limitations':['constructor-only review','finite exact algebra; no physical bridge',
                       'no state-transfer law chosen','other original passages remain unaudited']
    }
    ops={'ambient_basis':ambient,'K_minus_embedding':im,'K_plus_embedding':ip,
         'signed_K_minus_relabel':p,'old_K_minus_A':olda,
         'generator_difference':difference,
         'oriented_outer_boundary':[{'face':list(face),'coefficient':c} for face,c in minus_oriented.items()]}
    return v.encode(out),v.encode(ops)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');args=parser.parse_args()
    results,operators=run()
    if args.check:
        assert json.loads((ROOT/'REVIEW_RESULTS.json').read_text())==results
        assert json.loads((ROOT/'REVIEW_OPERATORS.json').read_text())==operators
    else:
        (ROOT/'REVIEW_RESULTS.json').write_text(json.dumps(results,indent=2)+'\n')
        (ROOT/'REVIEW_OPERATORS.json').write_text(json.dumps(operators,indent=2)+'\n')
    print(json.dumps(results,indent=2))
