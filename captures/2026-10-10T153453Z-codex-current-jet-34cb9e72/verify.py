"""Exact first-jet activity audit for Q166 native incidence currents."""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import json

cells=((0,1,2,3),(0,1,2,4))
levels=[tuple(sorted({s for c in cells for s in combinations(c,k)})) for k in (1,2,3,4)]
flat=sum((list(level) for level in levels),[]);idx={s:i for i,s in enumerate(flat)}
links=[]
for high in flat:
    if len(high)<2:continue
    for j in range(len(high)):
        low=high[:j]+high[j+1:]
        links.append((idx[low],idx[high],Q((-1)**j),low,high))
n=len(flat)
A=[[Q(0) for _ in range(n)] for _ in range(n)]
for i,j,b,_,_ in links:A[j][i]+=b;A[i][j]-=b
def derivative(c):return [sum(a*x for a,x in zip(row,c)) for row in A]
def currents(c):return [Q(2)*b*c[i]*c[j] for i,j,b,_,_ in links]
def current_slope(c):
    v=derivative(c)
    return [Q(2)*b*(v[i]*c[j]+c[i]*v[j]) for i,j,b,_,_ in links]
def rank(a):
    b=[row[:] for row in a];r=0
    for col in range(len(b[0])):
        pivot=next((k for k in range(r,len(b)) if b[k][col]),None)
        if pivot is None:continue
        b[r],b[pivot]=b[pivot],b[r];v=b[r][col];b[r]=[x/v for x in b[r]]
        for k in range(r+1,len(b)):
            q=b[k][col]
            if q:b[k]=[x-q*y for x,y in zip(b[k],b[r])]
        r+=1
        if r==len(b):break
    return r
checks={}
def check(name,value):checks[name]=bool(value);assert value,name

check('carrier_5_9_7_2',[len(level) for level in levels]==[5,9,7,2])
check('incidence_links_18_21_8',[
 sum(len(low)==k for _,_,_,low,_ in links) for k in (1,2,3)]==[18,21,8])
check('skew_generator',all(A[i][j]==-A[j][i] for i in range(n) for j in range(n)))
check('native_rank_22',rank(A)==22)
uniform=[Q(1) if len(s)==1 else Q(0) for s in flat]
check('uniform_vertex_null',derivative(uniform)==[Q(0)]*n)
check('null_current_and_slope_on_stationary_mode',not any(currents(uniform)) and not any(current_slope(uniform)))

# Exact active state that defeats every instantaneous native current.  Only
# the two cells initially carry amplitude e=(1,-1); their six private faces
# acquire nonzero slopes immediately.  No time-grid sampling is used.
c=[Q(0)]*n;c[idx[(0,1,2,3)]]=Q(1);c[idx[(0,1,2,4)]]=Q(-1)
dc=derivative(c);J=currents(c);dJ=current_slope(c)
check('cell_pair_active',any(dc))
check('all_47_currents_zero_at_initial_instant',not any(J))
check('six_private_face_cell_slopes_minus_two',sorted(v for v in dJ if v)==[Q(-2)]*6)
check('shared_face_both_slopes_zero',all(dJ[k]==0 for k,(_,_,_,low,high) in enumerate(links) if low==(0,1,2) and len(high)==4))
check('all_other_current_slopes_zero',all(dJ[k]==0 for k,(_,_,_,low,high) in enumerate(links) if not(len(low)==3 and low!=(0,1,2))))

# A one-coordinate active state must have zero current but nonzero first jet.
for k in range(n):
    singleton=[Q(int(i==k)) for i in range(n)]
    assert not any(currents(singleton))
    assert any(derivative(singleton)) and any(current_slope(singleton))
check('23_singletons_first_jet_detection',True)

# The general proof is in REPORT.md: J=0 makes the nonzero support an
# independent set of the incidence graph.  If A c is nonzero at vertex j,
# then c_j=0 and a neighboring nonzero c_i gives J'_ij !=0.
out={'claim_class':'EXACT native fixed-generator activity first-jet theorem; observer admission and gate decision OPEN; physical promotion 0',
     'carrier':'<0123,0124>','chain_register':[len(level) for level in levels],
     'incidence_links_by_degree':[18,21,8], 'generator_rank':rank(A),
     'activity_equivalence':'on this carrier A c != 0 iff some native directed current J or first derivative Jprime is nonzero',
     'witness':{'state':'c3=(1,-1), all lower coordinates zero','instantaneous_nonzero_currents':sum(v!=0 for v in J),
                'nonzero_current_slopes':sum(v!=0 for v in dJ),'private_face_cell_slopes':sorted(str(v) for v in dJ if v)},
     'checks':checks,'passed':sum(checks.values())}
Path(__file__).with_name('results.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps({'passed':out['passed'],'incidence_links':len(links),'rank':out['generator_rank'],'witness_currents':sum(v!=0 for v in J),'witness_slopes':sum(v!=0 for v in dJ)}))
