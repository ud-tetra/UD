#!/usr/bin/env python3
"""Fresh exact controls; no imported historical code or empirical inputs."""
from fractions import Fraction as Q
from itertools import permutations, product, combinations
from pathlib import Path
import json
from random import Random

D = [(-1,1),(1,0),(0,-1),(-1,0),(0,1),(1,0),(0,-1)]
FACES = [(0,1,2),(0,1,3),(0,1,4),(0,2,3),(0,2,4),(1,2,3),(1,2,4)]
SIMPLICES = FACES + [(0,1,2,3),(0,1,2,4)]
ORIENT = [1]*8+[-1]
CONTACTS = [(f,7+j,d) for f,row in enumerate(D) for j,d in enumerate(row) if d]
W = [{f}|{t for g,t,d in CONTACTS if g==f} for f in range(7)]
N = [{g for g in range(7) if g!=f and W[f]&W[g]} for f in range(7)]
R = [set().union(*(W[g] for g in N[f]|{f})) for f in range(7)]
PRIVATE = [[(f,d) for f,row in enumerate(D) if sum(v!=0 for v in row)==1
            for t,d in enumerate(row) if t==j and d] for j in range(2)]

def norm(x): return sum(v*v for v in x)
def score(x,f):
    k=len(W[f])-1; B=sum(d*x[t] for g,t,d in CONTACTS if g==f)
    return (B*B+k*x[f]*x[f])/(1+Q(k,4))
def weights(x):
    s=[score(x,f) for f in range(7)]
    return [max(Q(0),s[f]-max([Q(0)]+[s[g] for g in N[f]]))/((len(W[f])-1)*sum(x[i]**2 for i in R[f]))
            if any(x[i] for i in R[f]) else Q(0) for f in range(7)]
def original_event(x,f,t):
    y=list(x); c=t/2; k=len(W[f])-1
    B=sum(d*x[j] for g,j,d in CONTACTS if g==f); den=1+k*c*c
    y[f]=((1-k*c*c)*x[f]-2*c*B)/den
    for g,j,d in CONTACTS:
        if g==f:y[j]+=2*c*d*(x[f]-c*B)/den
    return y
def margin_event(x,h):
    y=list(x)
    for f,w in enumerate(weights(x)):
        if h[f] and w:y=original_event(y,f,w)
    return y
def collective(x,h,t=Q(1)):
    y=list(x); c=t/2
    for j,block in enumerate(PRIVATE):
        active=[(f,d) for f,d in block if h[f]]; m=len(active)
        if not m:continue
        b=x[7+j]; z=sum(d*x[f] for f,d in active); den=1+m*c*c
        y[7+j]=((1-m*c*c)*b+2*c*z)/den
        for f,d in active:y[f]=x[f]-2*c*d*(b+c*z)/den
    return y
def receipts(x,y,h):
    mid=[(a+b)/2 for a,b in zip(x,y)]; J={}
    for j,block in enumerate(PRIVATE):
        for f,d in block:J[f,7+j]=2*h[f]*d*mid[f]*mid[7+j]
    for f in range(7):
        assert y[f]**2-x[f]**2 == -sum(v for (g,t),v in J.items() if g==f)
    for j in range(2):
        assert y[7+j]**2-x[7+j]**2 == sum(v for (g,t),v in J.items() if t==7+j)
        owned=lambda v: v[7+j]**2+sum(v[f]**2/(len(W[f])-1) for f in range(7) if D[f][j])
        assert owned(x)==owned(y)
    return J
def parity(seq):return (-1)**sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))
def symmetries():
    out=[]
    for p in permutations(range(3)):
        for swap in (False,True):
            perm=list(p)+([4,3] if swap else [3,4]); mapping=[]
            for i,s in enumerate(SIMPLICES):
                v=tuple(perm[k] for k in s); dst=SIMPLICES.index(tuple(sorted(v)))
                mapping.append((dst,parity(v)*ORIENT[i]*ORIENT[dst]))
            out.append(mapping)
    return out
def transform(x,T):
    y=[Q(0)]*9
    for i,(dst,s) in enumerate(T):y[dst]=s*x[i]
    return y
def mask_transform(h,T):
    out=[0]*7
    for f in range(7):out[T[f][0]]=h[f]
    return out
def independent(bits):return all(not(bits[f] and bits[g]) for f in range(7) for g in N[f])

def main():
    rng=Random(534211)
    states=[]
    while len(states)<64:
        x=tuple(Q(rng.randrange(-4,5),rng.randrange(1,5)) for _ in range(9))
        if x not in states:states.append(x)
    zero=[Q(0)]*9
    witness=list(map(Q,[0,1,-1,-1,1,1,-1,0,0])); allon=[1]*7
    assert norm(witness)==6
    assert [score(witness,f) for f in range(7)]==[Q(0)]+[Q(4,5)]*6
    assert margin_event(witness,allon)==witness
    assert all(original_event(witness,f,Q(1))!=witness for f in range(1,7))
    perms=symmetries(); assert len(perms)==12
    # The actual even vertex cycle (0 1 2), fixing both apex vertices.
    cycle=perms[list(permutations(range(3))).index((1,2,0))*2]
    assert transform(witness,cycle)==witness
    admissible=[]
    for bits in product((0,1),repeat=7):
        if independent(bits) and mask_transform(bits,cycle)==list(bits):admissible.append(list(bits))
    assert admissible==[[0]*7,[1]+[0]*6]
    out=collective(witness,allon)
    assert out==[Q(0),Q(1,7),Q(-1,7),Q(-1,7),Q(1,7),Q(1,7),Q(-1,7),Q(12,7),Q(12,7)]
    J=receipts(witness,out,allon); assert set(J.values())=={Q(48,49)}
    assert out[7]**2+out[8]**2==Q(288,49)
    assert collective(witness,[0]*7)==witness
    repeated=collective(out,allon)
    assert repeated[7]==repeated[8]==Q(24,49)
    assert repeated[7]**2+repeated[8]**2<out[7]**2+out[8]**2
    dark=zero.copy();dark[1]=dark[3]=Q(1)
    assert collective(dark,allon)==dark and norm(dark)==2
    # Closed 4-simplex boundary: five tetrahedra, ten triangles, each valence two.
    closed_cells=list(combinations(range(5),4))
    closed_faces=list(combinations(range(5),3))
    assert len(closed_cells)==5 and len(closed_faces)==10
    assert all(sum(set(f)<=set(tau) for tau in closed_cells)==2 for f in closed_faces)
    assert not [f for f in closed_faces if sum(set(f)<=set(tau) for tau in closed_cells)==1]
    # Nonzero core-only stall: scores tie within each private K3.
    coreonly=zero.copy(); coreonly[7]=coreonly[8]=Q(1)
    assert margin_event(coreonly,allon)==coreonly
    assert all(original_event(coreonly,f,Q(1))!=coreonly for f in range(1,7))
    masks=list(product((0,1),repeat=7)); count=0
    for x in states:
        for h in masks:
            y=collective(x,h); assert norm(x)==norm(y); receipts(x,y,h)
            assert collective(y,h,Q(-1))==list(x)
            assert collective([-v for v in x],h)==[-v for v in y]
            assert y[0]==x[0]
            count+=1
    covariance=0
    for idx,x in enumerate(states):
        h=masks[(idx*37)%128]; y=collective(x,h)
        for T in perms:
            assert collective(transform(x,T),mask_transform(h,T))==transform(y,T)
            covariance+=1
    # Local read dependence: each cell event sees only its private faces and core.
    locality=0
    for x in states:
        y=collective(x,allon)
        for j,block in enumerate(PRIVATE):
            reads={7+j}|{f for f,d in block}
            for i in set(range(9))-reads:
                z=list(x);z[i]+=Q(17,13);v=collective(z,allon)
                assert all(v[k]==y[k] for k in reads);locality+=1
    criterion=0
    for x in states+[tuple(witness),tuple(coreonly),tuple(zero)]:
        s=[score(x,f) for f in range(7)]
        no_strict_max=all(s[f]==0 or any(s[g]>=s[f] for g in N[f]) for f in range(7))
        assert (margin_event(x,allon)==list(x))==no_strict_max;criterion+=1
    # Small asymmetric perturbations: continuity, not a uniform throughput bound.
    tie_controls=[]
    for n in (4,16,64,256):
        z=witness.copy();z[1]+=Q(1,n)
        delta=norm([a-b for a,b in zip(margin_event(z,allon),z)])
        assert delta>0 and delta<=Q(112*112,n*n)
        tie_controls.append({'perturbation':str(Q(1,n)),'squared_increment':str(delta)})
    result={'status':'PASS','arithmetic':'fractions.Fraction exact rational',
      'norm_receipt_ownership_mask_controls':count,'fixed_mask_inverse_controls':count,
      'odd_map_controls':count,'signed_covariance_controls':covariance,
      'bounded_read_controls':locality,'stall_criterion_controls':criterion,
      'independent_batch_masks_enumerated':128,'cycle_invariant_independent_batches':admissible,
      'symmetric_witness':list(map(str,witness)),'collective_output':list(map(str,out)),
      'each_private_contact_receipt':'48/49','aggregate_core_gain':'288/49',
      'repeated_event_core_amplitude':'24/49',
      'additional_countercontrols':['all hard off identity','nonzero collective cancellation',
          'repeated collective event backflow','closed 4-simplex boundary has no private faces'],
      'near_tie_controls':tie_controls,'review':'CONSTRUCTOR_ONLY; INDEPENDENT_REVIEW_PENDING',
      'physical_promotion':0}
    Path(__file__).with_name('RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
