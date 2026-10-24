#!/usr/bin/env python3
"""Fresh exact bulk-cover controls; no historical code execution."""
from fractions import Fraction as Q
from itertools import combinations, permutations, product
from random import Random
from pathlib import Path
import json

def parity(v):return (-1)**sum(v[i]>v[j] for i in range(len(v)) for j in range(i+1,len(v)))
def norm(x):return sum(v*v for v in x)
def matvec(A,x):return [sum(a*b for a,b in zip(row,x)) for row in A]
def solve(A,b):
    a=[list(row)+[v] for row,v in zip(A,b)];n=len(b)
    for k in range(n):
        pivot=next(i for i in range(k,n) if a[i][k]);a[k],a[pivot]=a[pivot],a[k]
        z=a[k][k];a[k]=[v/z for v in a[k]]
        for i in range(n):
            if i!=k and a[i][k]:
                z=a[i][k];a[i]=[u-z*v for u,v in zip(a[i],a[k])]
    return [row[-1] for row in a]

class Carrier:
    def __init__(self,cells,orient=None):
        self.cells=list(cells);self.orient=orient or [1]*len(cells)
        self.faces=sorted(set(f for c in cells for f in combinations(c,3)))
        self.F=len(self.faces);self.C=len(cells);self.n=self.F+self.C
        self.D=[[Q(0)]*self.C for _ in self.faces]
        for j,c in enumerate(cells):
            for i in range(4):self.D[self.faces.index(c[:i]+c[i+1:])][j]=Q((-1)**i*self.orient[j])
        self.k=[sum(d!=0 for d in row) for row in self.D]
        assert all(1<=k<=2 for k in self.k)
        self.inc=[{f for f in range(self.F) if self.D[f][j]} for j in range(self.C)]
        self.dual=[{l for l in range(self.C) if l!=j and self.inc[j]&self.inc[l]} for j in range(self.C)]
        self.W=[set(fs)|{self.F+l for f in fs for l,d in enumerate(self.D[f]) if d} for fs in self.inc]
    def H(self,j,h):
        H=[[Q(0)]*self.n for _ in range(self.n)]
        for f in self.inc[j]:
            for l,d in enumerate(self.D[f]):
                v=Q(h[f],self.k[f])*d
                H[self.F+l][f]+=v;H[f][self.F+l]-=v
        return H
    def event(self,x,j,h,t=Q(1)):
        H=self.H(j,h);ids=sorted(self.W[j]);n=len(ids);c=t/2
        A=[[Q(a==b)-c*H[a][b] for b in ids] for a in ids]
        rhs=[x[a]+c*sum(H[a][b]*x[b] for b in ids) for a in ids]
        values=solve(A,rhs);y=list(x)
        for a,v in zip(ids,values):y[a]=v
        return y
    def check_receipts(self,x,y,j,h,t=Q(1)):
        mid=[(a+b)/2 for a,b in zip(x,y)]
        J=[[2*t*Q(h[f],self.k[f])*self.D[f][l]*mid[f]*mid[self.F+l]
            if f in self.inc[j] else Q(0) for l in range(self.C)] for f in range(self.F)]
        for f in range(self.F):assert y[f]**2-x[f]**2==-sum(J[f])
        for l in range(self.C):assert y[self.F+l]**2-x[self.F+l]**2==sum(row[l] for row in J)
        deltas=[]
        for eta in range(self.C):
            owned=lambda v:v[self.F+eta]**2+sum(v[f]**2/self.k[f] for f in self.inc[eta])
            actual=owned(y)-owned(x)
            expected=sum((Q(l==eta)-Q(f in self.inc[eta],self.k[f]))*J[f][l]
                         for f in range(self.F) for l in range(self.C))
            assert actual==expected;deltas.append(actual)
        assert sum(deltas)==0
        return deltas
    def transformation(self,p):
        out=[]
        for s in self.faces:
            v=tuple(p[i] for i in s);out.append((self.faces.index(tuple(sorted(v))),parity(v)))
        for j,s in enumerate(self.cells):
            v=tuple(p[i] for i in s);l=self.cells.index(tuple(sorted(v)))
            out.append((self.F+l,parity(v)*self.orient[j]*self.orient[l]))
        return out

def transform(x,T):
    y=[Q(0)]*len(x)
    for i,(j,s) in enumerate(T):y[j]=s*x[i]
    return y
def mask_transform(h,T):
    y=[0]*len(h)
    for f,v in enumerate(h):y[T[f][0]]=v
    return y
def graph_checks(K):
    n=0
    for j in range(K.C):
        square=K.dual[j]|set().union(*(K.dual[l] for l in K.dual[j]))
        square.discard(j)
        for l in range(K.C):
            if l!=j:assert bool(K.W[j]&K.W[l])==(l in square);n+=1
        assert len(K.W[j])<=9 and len(K.dual[j])<=4 and len(square)<=16
    return n

def main():
    closed=Carrier(list(combinations(range(5),4)),[(-1)**i for i in reversed(range(5))])
    # Lexicographic tetrahedra omit vertices 4,3,2,1,0 respectively.
    assert closed.F==10 and closed.C==5 and closed.k==[2]*10
    assert all(len(W)==9 for W in closed.W)
    pair=Carrier([(0,1,2,3),(0,1,2,4)],[1,-1])
    strip=Carrier([tuple(range(i,i+4)) for i in range(7)])
    star=Carrier([(0,1,2,3),(0,1,2,4),(0,1,3,5),(0,2,3,6),(1,2,3,7)])
    graph_count=sum(graph_checks(K) for K in (closed,pair,strip,star))
    assert len(star.W[0])==9
    # Fresh disjoint commits commute on the strip, including their local solves.
    strip_x=[Q((i*7)%11-5,3) for i in range(strip.n)]
    strip_h=[1]*strip.F;commuting=0
    for j in range(strip.C):
        for l in range(j):
            if not strip.W[j]&strip.W[l]:
                a=strip.event(strip.event(strip_x,j,strip_h,Q(1,3)),l,strip_h,Q(1,3))
                b=strip.event(strip.event(strip_x,l,strip_h,Q(1,3)),j,strip_h,Q(1,3))
                assert a==b;commuting+=1
    # Exact partition of the original hard-gated native generator, not its finite flow.
    for bits in product((0,1),repeat=closed.F):
        Hs=[closed.H(j,bits) for j in range(closed.C)]
        for f in range(closed.F):
            for l,d in enumerate(closed.D[f]):
                assert sum(H[closed.F+l][f] for H in Hs)==bits[f]*d
                assert sum(H[f][closed.F+l] for H in Hs)==-bits[f]*d
    rng=Random(534212)
    x=[Q(rng.randrange(-3,4),rng.randrange(1,4)) for _ in range(closed.n)]
    masks=list(product((0,1),repeat=closed.F));norm_controls=0
    for h in masks:
        y=closed.event(x,0,h);assert norm(y)==norm(x)
        closed.check_receipts(x,y,0,h)
        assert closed.event(y,0,h,Q(-1))==x;norm_controls+=1
    states=[]
    while len(states)<16:
        z=tuple(Q(rng.randrange(-3,4),rng.randrange(1,4)) for _ in range(closed.n))
        if z not in states:states.append(z)
    for idx,z in enumerate(states):
        h=masks[idx*61%1024]
        for j in range(5):
            y=closed.event(z,j,h);assert norm(y)==norm(z);closed.check_receipts(z,y,j,h)
            assert closed.event([-a for a in z],j,h)==[-a for a in y];norm_controls+=1
    covariance=0
    x2=states[0];h=masks[617]
    base=[closed.event(x2,j,h) for j in range(5)]
    for p in permutations(range(5)):
        T=closed.transformation(p);z=transform(x2,T);hp=mask_transform(h,T)
        for j in range(5):
            jp=T[closed.F+j][0]-closed.F
            assert closed.event(z,jp,hp)==transform(base[j],T);covariance+=1
    locality=0
    for j in range(5):
        y=closed.event(x2,j,[1]*10)
        for i in set(range(closed.n))-closed.W[j]:
            z=list(x2);z[i]+=Q(13,7);v=closed.event(z,j,[1]*10)
            assert all(v[a]==y[a] for a in closed.W[j]);locality+=1
    # C5-invariant signed face preparation: sum the orbit of one oriented face.
    cycle=closed.transformation((1,2,3,4,0))
    e=[Q(0)]*closed.n;e[closed.faces.index((0,1,2))]=Q(1)
    witness=[Q(0)]*closed.n
    for _ in range(5):witness=[a+b for a,b in zip(witness,e)];e=transform(e,cycle)
    assert transform(witness,cycle)==witness and norm(witness)==5
    assert all(a==0 for a in witness[closed.F:])
    h=[1]*10;events=[closed.event(witness,j,h) for j in range(5)]
    assert all(y!=witness for y in events)
    assert all(norm(y)==5 for y in events)
    deltas=closed.check_receipts(witness,events[0],0,h)
    assert any(deltas) # Shared-face execution redistributes native owned stock.
    Hs=[closed.H(j,h) for j in range(5)]
    total=[[sum(H[a][b] for H in Hs) for b in range(closed.n)] for a in range(closed.n)]
    assert matvec(total,witness)==[0]*closed.n
    invariant=[]
    for bits in product((0,1),repeat=5):
        valid=all(not(bits[j] and bits[l]) for j in range(5) for l in range(j) if closed.W[j]&closed.W[l])
        moved=[0]*5
        for j,v in enumerate(bits):moved[cycle[closed.F+j][0]-closed.F]=v
        if valid and moved==list(bits):invariant.append(list(bits))
    assert invariant==[[0]*5]
    # Fixed-mask serial order is a genuine extra input.
    a=closed.event(closed.event(x2,0,h),1,h)
    b=closed.event(closed.event(x2,1,h),0,h)
    assert a!=b
    assert closed.event(witness,0,[0]*10)==witness
    report={'status':'PASS','arithmetic':'exact fractions.Fraction','physical_promotion':0,
      'review':'CONSTRUCTOR_ONLY; INDEPENDENT_REVIEW_PENDING','closed_face_valence':closed.k,
      'closed_block_sizes':list(map(len,closed.W)),'generator_partition_masks':1024,
      'norm_receipt_ownership_controls':norm_controls,'inverse_controls':1024,'odd_controls':80,
      'signed_covariance_controls':covariance,'locality_controls':locality,'graph_pair_controls':graph_count,
      'disjoint_strip_commutation_controls':commuting,
      'C5_witness':list(map(str,witness)),'witness_norm':'5',
      'center0_output':list(map(str,events[0])),'center0_owned_deltas':list(map(str,deltas)),
      'C5_invariant_independent_batches':invariant,
      'total_generator_on_witness':'ZERO_DESPITE_EACH_BLOCK_ACTIVE',
      'serial_order_squared_difference':str(norm([u-v for u,v in zip(a,b)])),
      'all_hard_off':'IDENTITY','complexes':['closed four-simplex boundary','two-cell pair','seven-cell strip','four-neighbor star']}
    Path(__file__).with_name('RESULTS.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()
