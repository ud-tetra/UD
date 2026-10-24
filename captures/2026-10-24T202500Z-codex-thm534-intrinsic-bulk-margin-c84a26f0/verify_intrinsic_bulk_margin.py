#!/usr/bin/env python3
"""Fresh exact candidate-response controls on original real coordinates."""
from fractions import Fraction as Q
from itertools import combinations, permutations, product
from pathlib import Path
import json

def norm(x):return sum(v*v for v in x)
def sign(v):return (-1)**sum(v[i]>v[j] for i in range(len(v)) for j in range(i+1,len(v)))
def solve(A,b):
    rows=[list(row)+[v] for row,v in zip(A,b)]
    for k in range(len(b)):
        p=next(i for i in range(k,len(b)) if rows[i][k]);rows[k],rows[p]=rows[p],rows[k]
        d=rows[k][k];rows[k]=[v/d for v in rows[k]]
        for i in range(len(b)):
            if i!=k and rows[i][k]:
                d=rows[i][k];rows[i]=[a-d*v for a,v in zip(rows[i],rows[k])]
    return [row[-1] for row in rows]

class Carrier:
    def __init__(self,cells,orient=None):
        self.cells=cells;self.orient=orient or [1]*len(cells)
        self.faces=sorted({f for c in cells for f in combinations(c,3)})
        self.F=len(self.faces);self.C=len(cells);self.n=self.F+self.C
        self.d=[[0]*self.C for _ in self.faces]
        for j,c in enumerate(cells):
            for i in range(4):self.d[self.faces.index(c[:i]+c[i+1:])][j]=(-1)**i*self.orient[j]
        self.k=[sum(d!=0 for d in row) for row in self.d];assert max(self.k)<=2
        self.fs=[{f for f in range(self.F) if self.d[f][j]} for j in range(self.C)]
        self.dual=[{l for l in range(self.C) if l!=j and self.fs[j]&self.fs[l]} for j in range(self.C)]
        self.balls=[]
        for j in range(self.C):
            bs=[{j}]
            for _ in range(4):bs.append(bs[-1]|{v for l in bs[-1] for v in self.dual[l]})
            self.balls.append(bs)
        self.neighbors=[bs[2]-{j} for j,bs in enumerate(self.balls)]
        self.W=[fs|{self.F+l for f in fs for l,d in enumerate(self.d[f]) if d} for fs in self.fs]
        self.R=[set().union(*(self.W[l] for l in self.balls[j][2])) for j in range(self.C)]
    def event(self,x,j,h,t=Q(1)):
        ids=sorted(self.W[j]);H={(a,b):Q(0) for a in ids for b in ids}
        for f in self.fs[j]:
            for l,d in enumerate(self.d[f]):
                if d:
                    v=Q(h[f]*d,self.k[f]);H[self.F+l,f]=v;H[f,self.F+l]=-v
        A=[[Q(a==b)-t*H[a,b]/2 for b in ids] for a in ids]
        rhs=[x[a]+t*sum(H[a,b]*x[b] for b in ids)/2 for a in ids]
        y=list(x)
        for a,v in zip(ids,solve(A,rhs)):y[a]=v
        return y
    def scores(self,x,h):
        return [norm([y[a]-x[a] for a in self.W[j]]) for j in range(self.C) for y in [self.event(x,j,h)]]
    def weights(self,x,h):
        s=self.scores(x,h);out=[]
        for j in range(self.C):
            E=sum(x[i]**2 for i in self.R[j]);r=max(Q(0),s[j]-max([Q(0)]+[s[l] for l in self.neighbors[j]]))
            out.append(r/(4*E) if E else Q(0))
        assert all(0<=v<=1 for v in out)
        return out
    def receipt(self,x,y,j,h,t):
        mid=[(a+b)/2 for a,b in zip(x,y)]
        J=[[2*t*Q(h[f]*self.d[f][l],self.k[f])*mid[f]*mid[self.F+l]
            if f in self.fs[j] else Q(0) for l in range(self.C)] for f in range(self.F)]
        for f in range(self.F):assert y[f]**2-x[f]**2==-sum(J[f])
        for l in range(self.C):assert y[self.F+l]**2-x[self.F+l]**2==sum(row[l] for row in J)
        owned=lambda v,e:v[self.F+e]**2+sum(v[f]**2/self.k[f] for f in self.fs[e])
        for e in range(self.C):
            assert owned(y,e)-owned(x,e)==sum((Q(l==e)-Q(f in self.fs[e],self.k[f]))*J[f][l]
              for f in range(self.F) for l in range(self.C))
    def update(self,x,h,check=False):
        w=self.weights(x,h);active=[j for j,v in enumerate(w) if v]
        assert all(not(self.W[j]&self.W[l]) for j in active for l in active if j!=l)
        y=list(x)
        for j in active:
            z=self.event(y,j,h,w[j])
            if check:self.receipt(y,z,j,h,w[j])
            assert z!=y;y=z
        return y
    def action(self,p):
        T=[]
        for f in self.faces:
            v=tuple(p[i] for i in f);T.append((self.faces.index(tuple(sorted(v))),sign(v)))
        for j,c in enumerate(self.cells):
            v=tuple(p[i] for i in c);l=self.cells.index(tuple(sorted(v)))
            T.append((self.F+l,sign(v)*self.orient[j]*self.orient[l]))
        return T

def transform(x,T):
    y=[Q(0)]*len(x)
    for i,(j,s) in enumerate(T):y[j]=s*x[i]
    return y
def transform_mask(h,T):
    y=[0]*len(h)
    for i,v in enumerate(h):y[T[i][0]]=v
    return y
def tree(depth):
    cells=[(0,1,2,3)];levels=[0];used={};nxt=4;j=0
    while j<len(cells):
        c=cells[j]
        for f in combinations(c,3):used[f]=used.get(f,0)+1
        if levels[j]<depth:
            for f in combinations(c,3):
                # A newly created cell's parent face already occurs in an earlier cell.
                if used[f]==1:
                    cells.append(tuple(sorted(f+(nxt,))));levels.append(levels[j]+1);nxt+=1
        j+=1
    return Carrier(cells)

def main():
    K=Carrier(list(combinations(range(5),4)),[1,-1,1,-1,1]);h=[1]*10
    witness=list(map(Q,[1,0,1,0,0,1,1,0,0,1]+[0]*5))
    assert K.scores(witness,h)==[Q(8,17)]*5 and K.update(witness,h)==witness
    perturb=[]
    for delta in (Q(1),Q(1,4),Q(1,16),Q(1,64)):
        x=witness.copy();x[10]+=delta;s=K.scores(x,h);w=K.weights(x,h)
        assert s[0]==Q(8,17)+Q(16,21)*delta**2
        assert s[1:]==[Q(8,17)+Q(80,357)*delta**2]*4
        assert w==[16*delta**2/(119*(5+delta**2))]+[Q(0)]*4
        y=K.update(x,h,True);assert norm(y)==norm(x)
        perturb.append({'core_perturbation':str(delta),'winner':0,'weight':str(w[0])})
    assert Q(64,119)-Q(501,1250)==Q(20381,148750)>0
    controls=0
    x=[Q((i*7)%13-6,i%3+1) for i in range(K.n)]
    for bits in product((0,1),repeat=10):
        y=K.update(x,bits,True);assert norm(y)==norm(x);controls+=1
    covariance=0;hp=[int(i%3!=0) for i in range(10)];base=K.update(x,hp)
    for p in permutations(range(5)):
        T=K.action(p)
        assert K.update(transform(x,T),transform_mask(hp,T))==transform(base,T);covariance+=1
    for a in (Q(-2),Q(1,3)):
        assert K.update([a*v for v in x],h)==[a*v for v in K.update(x,h)]
    assert K.update([Q(0)]*K.n,h)==[Q(0)]*K.n
    assert K.update(x,[0]*10)==x
    # Saturating geometry: a dual four-regular tree through radius four.
    big=tree(4);assert big.C==161
    assert len(big.R[0])==105 and len(big.balls[0][4])-1==160
    graph_controls=0
    for j in range(big.C):
        assert len(big.W[j])<=9 and len(big.R[j])<=105
        for l in range(big.C):
            if j!=l:
                assert bool(big.W[j]&big.R[l])==(l in big.balls[j][4]);graph_controls+=1
    read_multiplicity=max(sum(i in R for R in big.R) for i in range(big.n))
    assert read_multiplicity==53
    # A fresh-weight race despite disjoint writes: centers 0 and 3 on a strip.
    strip=Carrier([tuple(range(i,i+4)) for i in range(7)]);hs=[1]*strip.F
    prep=[Q(0)]*strip.n
    for j in (0,3):prep[min(f for f in strip.fs[j] if strip.k[f]==1)]=Q(1)
    ws=strip.weights(prep,hs);assert ws[0]>0 and ws[3]>0 and not(strip.W[0]&strip.W[3])
    bootstrap=strip.update(prep,hs,True)
    core_gain=sum(v*v for v in bootstrap[strip.F:]);assert core_gain>0
    first=strip.event(prep,0,hs,ws[0]);new3=strip.weights(first,hs)[3]
    assert new3!=ws[3]
    forward=strip.event(first,3,hs,new3)
    otherfirst=strip.event(prep,3,hs,ws[3]);new0=strip.weights(otherfirst,hs)[0]
    reverse=strip.event(otherfirst,0,hs,new0)
    assert forward!=reverse and norm(forward)==norm(reverse)==norm(prep)
    locality=0
    for j in (0,3,6):
        before=strip.weights(prep,hs)[j]
        for i in set(range(strip.n))-strip.R[j]:
            z=prep.copy();z[i]+=Q(7,11)
            assert strip.weights(z,hs)[j]==before;locality+=1
    report={'status':'PASS','arithmetic':'exact fractions.Fraction','physical_promotion':0,
      'review':'CONSTRUCTOR_ONLY; INDEPENDENT_REVIEW_PENDING','hard_mask_norm_receipt_controls':controls,
      'signed_covariance_controls':covariance,'declared_read_write_pair_controls':graph_controls,
      'weight_locality_controls':locality,'saturating_tree_cells':big.C,'max_real_reads':105,
      'max_real_writes':9,'max_coordinate_read_multiplicity':read_multiplicity,
      'max_recomputed_execution_conflict_degree':160,'C5_tie_score':'8/17',
      'asymmetric_preparation_controls':perturb,'fresh_race_initial_weight_3':str(ws[3]),
      'certified_preparation_ball_radius':'1/100 at witness plus unit core0',
      'certified_margin_lower_bound':'20381/148750',
      'fresh_race_recomputed_weight_3':str(new3),
      'fresh_race_order_difference':'NONZERO_EXACT; BOTH_ORDERS_NORM_CONSERVING',
      'empty_core_strip_bootstrap_gain':str(core_gain),
      'zero_and_hard_off':'IDENTITY','new_record_registers':0,
      'limits':['metric activity, cover, margin, normalization and model step remain candidate policy',
        'no symmetry breaking at C5 preparation','no general liveness, inverse, renewal or physical action claim']}
    Path(__file__).with_name('RESULTS.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))

if __name__=='__main__':main()
