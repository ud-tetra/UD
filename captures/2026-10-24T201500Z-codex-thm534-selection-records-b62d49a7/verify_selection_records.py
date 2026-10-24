#!/usr/bin/env python3
"""New exact record-selection controls; enumerated kernels, no random source."""
from fractions import Fraction as Q
from itertools import combinations, permutations, product
from pathlib import Path
import json

def sign(v):return (-1)**sum(v[i]>v[j] for i in range(len(v)) for j in range(i+1,len(v)))
def norm(v):return sum(a*a for a in v)
def solve(A,b):
    rows=[list(a)+[v] for a,v in zip(A,b)];n=len(b)
    for col in range(n):
        p=next(i for i in range(col,n) if rows[i][col]);rows[col],rows[p]=rows[p],rows[col]
        d=rows[col][col];rows[col]=[v/d for v in rows[col]]
        for i in range(n):
            if i!=col:
                d=rows[i][col]
                if d:rows[i]=[a-d*b for a,b in zip(rows[i],rows[col])]
    return [row[-1] for row in rows]

class Model:
    def __init__(self,cells,orient):
        self.cells=cells;self.orient=orient;self.faces=sorted({f for c in cells for f in combinations(c,3)})
        self.F=len(self.faces);self.C=len(cells);self.n=self.F+self.C
        self.d=[[0]*self.C for _ in self.faces]
        for j,c in enumerate(cells):
            for i in range(4):self.d[self.faces.index(c[:i]+c[i+1:])][j]=(-1)**i*orient[j]
        self.k=[sum(d!=0 for d in row) for row in self.d];assert max(self.k)<=2
        self.fs=[{f for f in range(self.F) if self.d[f][j]} for j in range(self.C)]
        dual=[{l for l in range(self.C) if l!=j and self.fs[j]&self.fs[l]} for j in range(self.C)]
        self.conflict=[]
        for j in range(self.C):
            s=dual[j]|{v for l in dual[j] for v in dual[l]};s.discard(j);self.conflict.append(s)
        self.W=[fs|{self.F+l for f in fs for l,d in enumerate(self.d[f]) if d} for fs in self.fs]
        assert all(len(W)<=9 for W in self.W) and all(len(s)<=16 for s in self.conflict)
    def eligible(self,q):return [j for j in range(self.C) if q[j] and all(not q[l] for l in self.conflict[j])]
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
    def receipts(self,x,y,j,h):
        mid=[(a+b)/2 for a,b in zip(x,y)]
        J=[[2*Q(h[f]*self.d[f][l],self.k[f])*mid[f]*mid[self.F+l]
            if f in self.fs[j] else Q(0) for l in range(self.C)] for f in range(self.F)]
        for f in range(self.F):assert y[f]**2-x[f]**2==-sum(J[f])
        for l in range(self.C):assert y[self.F+l]**2-x[self.F+l]**2==sum(row[l] for row in J)
        owned=lambda v,e:v[self.F+e]**2+sum(v[f]**2/self.k[f] for f in self.fs[e])
        for e in range(self.C):
            assert owned(y,e)-owned(x,e)==sum((Q(l==e)-Q(f in self.fs[e],self.k[f]))*J[f][l]
              for f in range(self.F) for l in range(self.C))
    def lift(self,x,q,h,t=Q(1),check=False):
        y=list(x);selected=self.eligible(q)
        assert all(not(self.W[j]&self.W[l]) for j in selected for l in selected if l<j)
        for j in selected:
            z=self.event(y,j,h,t)
            if check:self.receipts(y,z,j,h)
            y=z
        return y,tuple(q)
    def action(self,p):
        T=[]
        for f in self.faces:
            v=tuple(p[i] for i in f);T.append((self.faces.index(tuple(sorted(v))),sign(v)))
        for j,c in enumerate(self.cells):
            v=tuple(p[i] for i in c);l=self.cells.index(tuple(sorted(v)))
            T.append((self.F+l,sign(v)*self.orient[j]*self.orient[l]))
        return T

def field_action(x,T):
    out=[Q(0)]*len(x)
    for i,(j,s) in enumerate(T):out[j]=s*x[i]
    return out
def record_action(q,T,F):
    out=[0]*len(q)
    for j,v in enumerate(q):out[T[F+j][0]-F]=v
    return tuple(out)
def mask_action(h,T):
    out=[0]*len(h)
    for f,v in enumerate(h):out[T[f][0]]=v
    return out

def main():
    K=Model(list(combinations(range(5),4)),[1,-1,1,-1,1])
    strip=Model([tuple(range(i,i+4)) for i in range(7)],[1]*7)
    qs=list(product((0,1),repeat=5));masks=list(product((0,1),repeat=10))
    states=[tuple(Q(((i+3)*(s+7))%17-8,(i+s)%3+1) for i in range(15)) for s in range(16)]
    assert len(set(states))==16
    controls=0
    for s,x in enumerate(states):
        h=masks[(s*61)%1024]
        for q in qs:
            y,qr=K.lift(x,q,h,check=True);assert qr==q and norm(y)==norm(x)
            assert K.lift(y,q,h,Q(-1))[0]==list(x)
            assert K.lift([-v for v in x],q,h)[0]==[-v for v in y];controls+=1
    onehots=[tuple(int(i==j) for i in range(5)) for j in range(5)]
    for h in masks:
        y,q=K.lift(states[0],onehots[0],h,check=True)
        assert norm(y)==norm(states[0]);controls+=1
    covariance=0
    x=states[1];h=masks[617]
    for p in permutations(range(5)):
        T=K.action(p)
        for q in onehots:
            y,qr=K.lift(x,q,h)
            zp,rp=K.lift(field_action(x,T),record_action(q,T,K.F),mask_action(h,T))
            assert zp==field_action(y,T) and rp==record_action(qr,T,K.F);covariance+=1
    strip_x=[Q((i*7)%11-5,3) for i in range(strip.n)];strip_controls=0;local_controls=0
    for q in product((0,1),repeat=7):
        y,qr=strip.lift(strip_x,q,[1]*strip.F,check=True)
        assert norm(y)==norm(strip_x) and qr==q
        assert strip.lift(y,q,[1]*strip.F,Q(-1))[0]==strip_x;strip_controls+=1
        for j in range(7):
            for l in set(range(7))-(strip.conflict[j]|{j}):
                r=list(q);r[l]=1-r[l]
                assert (j in strip.eligible(q))==(j in strip.eligible(r));local_controls+=1
    # The source-fixed preparation, and all five distinctly marked outcomes.
    witness=list(map(Q,[1,0,1,0,0,1,1,0,0,1]+[0]*5));h=[1]*10
    T=K.action((1,2,3,4,0));assert field_action(witness,T)==witness
    outputs=[K.lift(witness,q,h,check=True)[0] for q in onehots]
    assert all(y!=witness and norm(y)==5 for y in outputs)
    assert all(norm([a-b for a,b in zip(y,witness)])==Q(8,17) for y in outputs)
    assert all(sum(v*v for v in y[10:])==Q(128,289) for y in outputs)
    orbit=[];q=onehots[0]
    for _ in range(5):orbit.append(q);q=record_action(q,T,K.F)
    assert len(set(orbit))==5 and q==onehots[0]
    invariant=[q for q in qs if record_action(q,T,K.F)==q]
    assert invariant==[(0,)*5,(1,)*5]
    assert all(K.lift(witness,q,h)[0]==witness for q in invariant)
    assert K.lift(witness,onehots[0],[0]*10)[0]==witness
    dark=list(map(Q,[0]*10+[1]*5))
    assert norm(dark)==5 and K.lift(dark,onehots[0],h)[0]==dark
    assert K.lift(witness,(1,1,0,0,0),h)[0]==witness
    mean=[sum(y[i] for y in outputs)/5 for i in range(15)]
    assert mean==[Q(81,85)*v for v in witness]
    assert norm(mean)==Q(6561,1445)
    variance=sum(norm([a-b for a,b in zip(y,mean)]) for y in outputs)/5
    assert variance==Q(664,1445) and norm(mean)+variance==5
    assert all(sum(y[i] for y in outputs)==0 for i in range(10,15))
    report={'status':'PASS','arithmetic':'exact fractions.Fraction; all outcomes enumerated',
      'physical_promotion':0,'review':'CONSTRUCTOR_ONLY; INDEPENDENT_REVIEW_PENDING',
      'closed_norm_receipt_cases':controls,'closed_inverse_and_odd_cases':512,
      'signed_covariance_cases':covariance,'strip_mark_configurations':strip_controls,
      'record_eligibility_locality_cases':local_controls,'record_orbit_size_required':5,
      'binary_fixed_length_minimum_bits':3,'C5_fixed_binary_records':invariant,
      'per_selected_outcome_squared_displacement':'8/17','per_selected_outcome_core_gain':'128/289',
      'uniform_kernel_mean_factor':'81/85','uniform_kernel_mean_squared_norm':'6561/1445',
      'uniform_kernel_variance':'664/1445','pathwise_squared_norm':'5',
      'record_preservation':'STATIC_MARKS_UNCHANGED; NO_RESET_OR_RENEWAL_CLAIM',
      'unique_mark_dark_control':'NONZERO_CORE_CYCLE_FIXED_WITH_ALL_PERMISSIONS_ON',
      'colliding_mark_control':'TWO_MARKS_STALL_ON_COMPLETE_CONFLICT_GRAPH',
      'randomness':'NO_RANDOMNESS_GENERATED; UNIFORM_KERNEL_CONDITIONAL_ONLY',
      'all_hard_off':'IDENTITY'}
    Path(__file__).with_name('RESULTS.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()
