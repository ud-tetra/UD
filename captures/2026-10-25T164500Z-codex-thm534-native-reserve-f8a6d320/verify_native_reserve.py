#!/usr/bin/env python3
"""Fresh full-tetrahedron exact controls; no added field or archived execution."""
from fractions import Fraction as Q
from itertools import combinations, permutations, product
from pathlib import Path
import json

SIMPLICES=[s for k in range(1,5) for s in combinations(range(4),k)]
def zeros(n,m):return [[Q(0)]*m for _ in range(n)]
def norm(x):return sum(v*v for v in x)
def mv(A,x):return [sum(a*b for a,b in zip(row,x)) for row in A]
def mm(A,B):return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]
def transpose(A):return list(map(list,zip(*A)))
def sign(v):return (-1)**sum(v[i]>v[j] for i in range(len(v)) for j in range(i+1,len(v)))
def boundary(k):
    lo=list(combinations(range(4),k));hi=list(combinations(range(4),k+1));B=zeros(len(lo),len(hi))
    for j,s in enumerate(hi):
        for i in range(k+1):B[lo.index(s[:i]+s[i+1:])][j]=Q((-1)**i)
    return B
B1=boundary(1);B2=boundary(2);B3=boundary(3);b=[v[0] for v in B3]
def generator(h):
    A=zeros(15,15)
    for B,lo,hi in [(B1,0,4),(B2,4,10),(B3,10,14)]:
        for i,row in enumerate(B):
            for j,v in enumerate(row):
                a=v*(h[i] if lo==10 else 1);A[lo+i][hi+j]=-a;A[hi+j][lo+i]=a
    return A
def solve(A,b):
    rows=[list(row)+[v] for row,v in zip(A,b)]
    for k in range(len(b)):
        p=next(i for i in range(k,len(b)) if rows[i][k]);rows[k],rows[p]=rows[p],rows[k]
        d=rows[k][k];rows[k]=[v/d for v in rows[k]]
        for i in range(len(b)):
            if i!=k and rows[i][k]:
                d=rows[i][k];rows[i]=[a-d*v for a,v in zip(rows[i],rows[k])]
    return [row[-1] for row in rows]
def event(x,A,t):
    L=[[Q(i==j)-t*A[i][j]/2 for j in range(15)] for i in range(15)]
    rhs=[x[i]+t*sum(A[i][j]*x[j] for j in range(15))/2 for i in range(15)]
    return solve(L,rhs)
def receipts(x,y,A,t):
    mid=[(a+b)/2 for a,b in zip(x,y)];delta=[Q(0)]*15;j12=Q(0);j23=Q(0)
    for i in range(15):
        for j in range(i+1,15):
            if A[j][i]:
                J=2*t*A[j][i]*mid[i]*mid[j];delta[i]-=J;delta[j]+=J
                if 4<=i<10 and 10<=j<14:j12+=J
                if 10<=i<14 and j==14:j23+=J
    assert delta==[v*v-u*u for u,v in zip(x,y)]
    assert norm(y[4:10])-norm(x[4:10])==-j12
    assert norm(y[10:14])-norm(x[10:14])==j12-j23
    assert y[14]**2-x[14]**2==j23
    return j12,j23
def action(p):
    T=[]
    for s in SIMPLICES:
        v=tuple(p[i] for i in s);T.append((SIMPLICES.index(tuple(sorted(v))),sign(v)))
    return T
def transform(x,T):
    y=[Q(0)]*15
    for i,(j,s) in enumerate(T):y[j]=s*x[i]
    return y

def main():
    assert mm(B1,B2)==zeros(4,4) and mm(B2,B3)==zeros(6,1)
    assert norm(b)==4 and mm(transpose(B2),B2)==[[4*Q(i==j)-b[i]*b[j] for j in range(4)] for i in range(4)]
    controls=0;covariance=0;matched=[];masks=list(product((0,1),repeat=4))
    for h in masks:
        k=sum(h);u=mv(B2,[h[i]*b[i] for i in range(4)]);q=norm(u)
        assert q==k*(4-k) and mv(B1,u)==[0]*4
        A=generator(h);assert all(A[i][j]==-A[j][i] for i in range(15) for j in range(15))
        assert mm(A,A)[14][4:10]==u
        inputs=[u]+[[B2[i][j] for i in range(6)] for j in range(4)]
        for e in inputs:
            x=[Q(0)]*4+e+[Q(0)]*5;gamma=sum(a*c for a,c in zip(u,e))
            for t in (Q(1,4),Q(1,2),Q(1),Q(2)):
                y=event(x,A,t);den=16+(16+4*k)*t*t+k*k*t**4
                assert y[14]==8*gamma*t*t/den
                assert y[:4]==[0]*4 and norm(y)==norm(x)
                receipts(x,y,A,t);assert event(y,A,-t)==x;controls+=1
        x=[Q(0)]*4+u+[Q(0)]*5;y=event(x,A,Q(1))
        if q:
            assert y[14]!=0 and y[14]==Q(8*q,k*k+4*k+32)
            j12,j23=receipts(x,y,A,Q(1))
            assert j12>0 and j23>0
            matched.append({'mask':list(h),'open_faces':k,'edge_stock':str(q),'core_amplitude':str(y[14]),
                            'edge_to_face_receipt':str(j12),'face_to_core_receipt':str(j23)})
        # Actual signed S4 covariance, including prepared reserve vector.
        for p in permutations(range(4)):
            T=action(p);hp=[0]*4
            for i,v in enumerate(h):hp[T[10+i][0]-10]=v
            Ap=generator(hp)
            assert all(Ap[T[i][0]][T[j][0]]==T[i][1]*T[j][1]*A[i][j] for i in range(15) for j in range(15))
            assert mv(Ap,transform(x,T))==transform(mv(A,x),T);covariance+=1
    assert len(matched)==14
    assert {m['open_faces']:m['core_amplitude'] for m in matched}=={1:'24/37',2:'8/11',3:'24/53'}
    # Robustness in the native edge-cycle subspace; projection signal is linear.
    h=(1,0,0,0);u=mv(B2,[h[i]*b[i] for i in range(4)]);q=norm(u)
    perturbed=0
    for j in range(4):
        e=[u[i]+Q(1,10)*B2[i][j] for i in range(6)]
        gamma=sum(a*c for a,c in zip(u,e));assert gamma>0
        x=[Q(0)]*4+e+[Q(0)]*5;y=event(x,generator(h),Q(1))
        assert y[14]>0 and norm(y)==norm(x);perturbed+=1
    report={'status':'PASS','arithmetic':'exact fractions.Fraction','physical_promotion':0,
       'review':'CONSTRUCTOR_ONLY; INDEPENDENT_REVIEW_PENDING','full_native_event_controls':controls,
       'signed_S4_generator_controls':covariance,'nonuniform_conversion_masks':14,
       'uniform_masks_block_edge_to_core':[[0,0,0,0],[1,1,1,1]],'edge_cycle_perturbations':perturbed,
       'conversion_strength':'k(4-k)','exact_core_output':'8 gamma t^2 / (16+(16+4k)t^2+k^2 t^4)',
       'matched_preparations':matched,'new_real_coordinates':0,
       'source_limits':['Masks are supplied mathematical permissions, not derived native gate readiness',
        'Edge support is a donor stock, not identified physical consumable event cost',
        'One tetrahedron only; shared-face bulk extension not claimed',
        'No open-system reserve/record renewal, action unit or particle correspondence']}
    Path(__file__).with_name('RESULTS.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='matched_preparations'},indent=2))

if __name__=='__main__':main()
