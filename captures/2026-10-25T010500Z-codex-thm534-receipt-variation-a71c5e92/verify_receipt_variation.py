#!/usr/bin/env python3
"""Fresh exact receipt/refinement controls; no archived execution."""
from fractions import Fraction as Q
from itertools import product, combinations_with_replacement
from pathlib import Path
import json

D=[(-1,1),(1,0),(0,-1),(-1,0),(0,1),(1,0),(0,-1)]
CONTACTS=[(f,j,d) for f,row in enumerate(D) for j,d in enumerate(row) if d]
def currents(x,a):return [2*a[f]*d*x[f]*x[7+j] for f,j,d in CONTACTS]
def total(v,k=None):return sum(abs(x)*(k[i] if k else 1) for i,x in enumerate(v))
def stock(u):return 4*u*u/(1+u*u)**2
def variation(a,b):
    assert 0<=a<=b
    if a<=1<=b:return 2-stock(a)-stock(b)
    return abs(stock(b)-stock(a))
def pair_event(x,t):
    a,b=x;c=t/2;den=1+c*c
    return [((1-c*c)*a-t*b)/den,(t*a+(1-c*c)*b)/den]

def main():
    split_controls=0;ownership_covers=0
    states=[tuple(Q(((i+3)*(n+7))%17-8,(i+n)%3+1) for i in range(9)) for n in range(32)]
    assert len(set(states))==32
    for x in states:
        for mask in product((0,1),repeat=7):
            a=list(map(Q,mask));base=currents(x,a)
            # Original coface-neutral two-cell cover, on one fixed field state.
            pieces=[]
            for j in range(2):
                coeff=[a[f]/sum(v!=0 for v in D[f]) if D[f][j] else Q(0) for f in range(7)]
                pieces.append(currents(x,coeff))
            assert [sum(v[i] for v in pieces) for i in range(8)]==base
            assert sum(total(v) for v in pieces)==total(base);ownership_covers+=1
            for weights in ([Q(1,2)]*2,[Q(1,3)]*3,[Q(1,4)]*4,[Q(1,2),Q(1,3),Q(1,6)]):
                vs=[currents(x,[w*v for v in a]) for w in weights]
                for k in (None,[Q(i+1,3) for i in range(8)]):
                    assert sum(total(v,k) for v in vs)==total(base,k)
                split_controls+=1
    # Actual orientation changes leave native signed support currents invariant.
    reorientation_controls=0
    for x in states:
        original=currents(x,[Q(1)]*7)
        for n in range(64):
            signs=[(-1)**((n>>i)%2) for i in range(6)]+[1,(-1)**(n%2),(-1)**((n>>1)%2)]
            y=[s*v for s,v in zip(signs,x)]
            changed=[2*signs[f]*signs[7+j]*d*y[f]*y[7+j] for f,j,d in CONTACTS]
            assert changed==original;reorientation_controls+=1
    assert abs(Q(2))+abs(Q(-1))>abs(Q(2)-1) # Positive refinement hypothesis matters.
    grid=[Q(i,4) for i in range(13)];partition_controls=0
    for a,b,c in combinations_with_replacement(grid,3):
        assert variation(a,b)+variation(b,c)==variation(a,c)
        assert (stock(b)-stock(a))+(stock(c)-stock(b))==stock(c)-stock(a)
        partition_controls+=1
    assert stock(Q(0))==0 and stock(Q(1))==1 and stock(Q(2))==Q(16,25)
    assert variation(Q(0),Q(2))==Q(34,25)>abs(stock(Q(2))-stock(Q(0)))
    # The exact native private-pair Cayley event from an empty core.
    budget=[]
    for t,q in [(Q(1,2),Q(64,289)),(Q(1),Q(16,25)),(Q(3,2),Q(576,625)),(Q(2),Q(1))]:
        y=pair_event([Q(1),Q(0)],t);assert y[1]**2==q and sum(v*v for v in y)==1
        mid=[(Q(1)+y[0])/2,y[1]/2]
        J=2*t*mid[0]*mid[1];assert J==q
        budget.append({'model_step':str(t),'core_transfer':str(q)})
    assert 2*Q(1)*Q(0)==0 and budget[0]['core_transfer']!='0'
    # Exact repeated field-return cycles: four quarter turns, signed receipts cancel.
    cycle_controls=0
    for m in range(1,65):
        x=[Q(1),Q(0)];gross=Q(0);signed=Q(0)
        for _ in range(4*m):
            y=pair_event(x,Q(2));mid=[(a+b)/2 for a,b in zip(x,y)]
            J=4*mid[0]*mid[1];assert J==y[1]**2-x[1]**2
            gross+=abs(J);signed+=J;x=y
        assert x==[Q(1),Q(0)] and gross==4*m and signed==0
        cycle_controls+=1
    # Distinct positive cost weights pass the same refinement test.
    assert total([Q(1),Q(-1)],[Q(1),Q(1)])==2
    assert total([Q(1),Q(-1)],[Q(2),Q(3)])==5
    result={'status':'PASS','arithmetic':'exact fractions.Fraction','physical_promotion':0,
      'review':'CONSTRUCTOR_ONLY; INDEPENDENT_REVIEW_PENDING',
      'positive_partition_controls':split_controls,'coface_cover_controls':ownership_covers,
      'reorientation_controls':reorientation_controls,'trajectory_partition_controls':partition_controls,
      'native_field_return_cycle_controls':cycle_controls,'return_cycle_gross_receipt':'4 per cycle',
      'return_cycle_signed_receipt':'0','return_cycle_total_support':'1',
      'backflow_path_signed_receipt':'16/25','backflow_path_absolute_variation':'34/25',
      'empty_core_instantaneous_rate':'0','finite_budget_examples':budget,
      'source_scope':'Q171-Q173 currents; additive diagnostic, not derived consumable cost',
      'open':['physical event cost weights and budget','native initiation and selection','reserve coupling and renewal','action/clock and particle map']}
    Path(__file__).with_name('RESULTS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

if __name__=='__main__':main()
