#!/usr/bin/env python3
"""Independent-formula exact audit of frozen cochain contrast candidate v0.1."""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import json

S = [list(combinations(range(4), k)) for k in range(1, 5)]
simplex = sum(S, [])
idx = {s:i for i,s in enumerate(simplex)}
edges = S[1]
pairs = ((0,5),(1,4),(2,3))
n = 15

def mul(a,b):
    return [[sum((x*b[k][j] for k,x in enumerate(row)), Q(0)) for j in range(n)] for row in a]

def vec(a,x):
    return [sum((t*u for t,u in zip(row,x)), Q(0)) for row in a]

def scale(a,q):
    return [[q*x for x in row] for row in a]

def add(*matrices):
    return [[sum((m[i][j] for m in matrices), Q(0)) for j in range(n)] for i in range(n)]

def contrast(x):
    e=[sum((x[idx[edges[k]]]**2 for k in pair), Q(0)) for pair in pairs]
    return [3*t-sum(e) for t in e]

def main():
    eye=[[Q(i==j) for j in range(n)] for i in range(n)]
    p0=[[Q(1,4) if i<4 and j<4 else Q(0) for j in range(n)] for i in range(n)]
    pc=add(eye,scale(p0,-1))
    a=[[Q(0) for _ in range(n)] for _ in range(n)]
    for high in simplex:
        if len(high)<2: continue
        j=idx[high]
        for t in range(len(high)):
            i=idx[high[:t]+high[t+1:]]
            a[i][j]=-Q((-1)**t)
            a[j][i]=Q((-1)**t)
    assert mul(a,a)==scale(pc,-4)
    assert mul(a,p0)==mul(p0,a)==[[Q(0) for _ in range(n)] for _ in range(n)]
    def cayley(h):
        return add(p0,scale(pc,(1-h*h)/(1+h*h)),scale(a,h/(1+h*h)))
    for h in (Q(1),Q(1,2)):
        m=cayley(h)
        left=add(eye,scale(a,-h/2))
        right=add(eye,scale(a,h/2))
        assert mul(left,m)==right
        assert mul([list(t) for t in zip(*m)],m)==eye
    q1=cayley(Q(1))
    assert q1==add(p0,scale(a,Q(1,2)))
    # A one-window same-sign, opposite-midpoint witness. At s=pi/8,
    # c1(s)=(c1(0)+(A c)_1/2)/sqrt(2); contrast scales by 1/2.
    w=[Q(t) for t in (2,-2,2,1,2,2,0,0,-2,2,0,2,1,2,1)]
    before=contrast(w)
    aw=vec(a,w)
    mid_proxy=w[:]
    for e in edges:
        i=idx[e]
        mid_proxy[i]=w[i]+aw[i]/2
    middle=[t/2 for t in contrast(mid_proxy)]
    end=contrast(vec(q1,w))
    assert before==[Q(8),Q(8),Q(-16)]
    assert middle==[Q(-5,4),Q(1),Q(1,4)]
    assert end==[Q(43,2),Q(-10),Q(-23,2)]
    assert before[0]>0 and middle[0]<0 and end[0]>0
    assert before[2]<0 and middle[2]>0 and end[2]<0
    # Frozen endpoint rule emits no flip at A,C despite >=2 continuous zeros each.
    receipt=tuple(int(x*y<0) for x,y in zip(before,end))
    assert receipt==(0,1,0)
    # A previous frozen test witness changes outcome when only the step changes.
    clock_witness=[Q(t) for t in (-2,1,2,1,-1,-2,-1,0,2,0,0,-1,-1,2,1)]
    d0=contrast(clock_witness)
    xi1=tuple(int(x*y<0) for x,y in zip(d0,contrast(vec(q1,clock_witness))))
    xihalf=tuple(int(x*y<0) for x,y in zip(d0,contrast(vec(cayley(Q(1,2)),clock_witness))))
    assert xi1==(1,0,0) and xihalf==(0,0,0)
    out={'status':'PASS','operator_identity':'A^2=-4(I-P0)',
         'cayley_identity':'Q_h=P0+((1-h^2)/(1+h^2))(I-P0)+(h/(1+h^2))A=exp(arctan(h) A) on filled K4',
         'h1_internal_s':'pi/4 (not 1)',
         'alias_witness': [int(t) for t in w],
         'contrast_at_s0':[str(t) for t in before],
         'contrast_at_s_pi_over_8':[str(t) for t in middle],
         'contrast_at_s_pi_over_4':[str(t) for t in end],
         'frozen_endpoint_receipt':receipt,
         'strict_continuous_zeros_minimum':{'A':2,'C':2},
         'clock_witness_xi_h1':xi1,'clock_witness_xi_hhalf':xihalf,
         'independent_event_target':'NOT_RUN','physical_promotion':0}
    Path(__file__).with_name('results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__': main()
