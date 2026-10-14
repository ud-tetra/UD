"""Fresh exact metric-family replay. Imported archive code is never executed."""
from fractions import Fraction as F
from itertools import combinations, permutations, product
from pathlib import Path
import hashlib, json

ROOT=Path(__file__).resolve().parent
BASIS=[s for k in range(1,5) for s in combinations(range(4),k)]
N=len(BASIS); INDEX={s:i for i,s in enumerate(BASIS)}
def transpose(a): return list(map(list,zip(*a)))
def multiply(a,b):
    bt=transpose(b)
    return [[sum(x*y for x,y in zip(row,col) if x and y) for col in bt] for row in a]
def identity(): return [[F(i==j) for j in range(N)] for i in range(N)]
def polynomial_product(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c
def characteristic(a):
    traces=[]; power=identity()
    for k in range(1,N+1):
        power=multiply(power,a); traces.append(sum(power[i][i] for i in range(N)))
    c=[F(1)]
    for k in range(1,N+1): c.append(-sum(c[k-j]*traces[j-1] for j in range(1,k+1))/k)
    return c
def boundary():
    b=[[F(0) for _ in BASIS] for _ in BASIS]
    for s in BASIS:
        if len(s)>1:
            for j in range(len(s)): b[INDEX[s[:j]+s[j+1:]]][INDEX[s]]=F((-1)**j)
    return b
def weighted_generator(g):
    b=boundary()
    return [[b[j][i]*g[j]/g[i]-b[i][j] for j in range(N)] for i in range(N)]
def expected_characteristic(squares,multiplicities):
    c=[F(1),F(0)]
    for square,m in zip(squares,multiplicities):
        for _ in range(m): c=polynomial_product(c,[F(1),F(0),square])
    return c
def gram(q,p):
    q=F(q); assert q>0 and p in (1,2)
    a=((1+q)/2)**p; b=((2*q+1)/3)**p; c=q**p
    squares=(4/a,2+2/a,4*a/b,2*(a+1)/b,4*b/c)
    return (a,b,c),squares
def metric_for_gram(q,p):
    (a,b,c),s=gram(q,p)
    return [F(1)]*4+[a,a,F(1),F(1),a,a]+[b]*4+[c],s
def cover_radius(m,bands=3):
    assert isinstance(m,int) and m>0
    r=0
    while m>r//2+bands*(r+1): r+=1
    return r
def verify():
    b=boundary(); assert all(not v for row in multiply(b,b) for v in row)
    gram_cases=[]
    for q,p in product([F(1,4),F(1),F(4),F(9)],[1,2]):
        g,s=metric_for_gram(q,p); a=weighted_generator(g)
        assert all(g[i]*a[i][j]+g[j]*a[j][i]==0 for i in range(N) for j in range(N))
        assert characteristic(a)==expected_characteristic(s,[1,2,1,2,1])
        assert s[0]/s[1]+s[2]/s[3]==2
        gram_cases.append({'q':str(q),'rule':'A' if p==1 else 'B','p':p,
            'squared_frequencies':list(map(str,s)),'signed_multiplicities':[1,2,1,2,1],
            'distinct_positive_bands':len(set(s)),'characteristic_coefficients':list(map(str,characteristic(a)))})
    degree_cases=[]
    for gs in [(F(1),F(1),F(1),F(1)),(F(2),F(3),F(5),F(7))]:
        g=[gs[len(s)-1] for s in BASIS]; a=weighted_generator(g)
        squares=[4*gs[k]/gs[k+1] for k in range(3)]
        assert characteristic(a)==expected_characteristic(squares,[3,3,1])
        degree_cases.append({'g':list(map(str,gs)),'squared_frequencies':list(map(str,squares))})
    assignments=[]
    for u,v,x,y in permutations([1,4,9,16,25],4):
        gap=F(u,v)+F(x,y)-2
        assert gap
        assignments.append({'U':u,'V':v,'X':x,'Y':y,'signed_relation_gap':str(gap)})
    assert len(assignments)==120
    minimum=min(abs(F(x['signed_relation_gap'])) for x in assignments)
    assert minimum==F(1,144)
    # Enumeration is a proof of exact mismatch, not a uniform operator residual bound.
    # Three-center radius witness is a relaxation, not native coefficient selection.
    witness=[3,7,10]; distances=[min(abs(x-c) for c in [0]+witness) for x in [2,4,6,8,10]]
    assert max(distances)==cover_radius(5)==1
    # Irrational pair ratios exclude two integer-grid matches in the same degree channel.
    # Squared ratios 5/3 and 5/2 are not rational squares (unique prime factorization).
    for numerator,denominator in [(5,3),(5,2)]:
        import math
        assert math.isqrt(numerator)**2!=numerator and math.isqrt(denominator)**2!=denominator
    receipt={'status':'PASS','version':'0.1','reading_edition':'0.10','physical_promotion':0,
       'constructor_team_AI':True,'independent_human_review':'PENDING',
       'scope':'Exact finite algebra and family-specific full-generator exclusion; no endpoint-error lower bound or source-selected metric.',
       'gram_cases':gram_cases,'degree_cases':degree_cases,'gram_target_assignments':assignments,
       'gram_target_assignment_count':120,'gram_target_hits':0,'minimum_relation_gap':str(minimum),
       'relation_gap_is_operator_bound':False,'three_center_default':{'radius':1,'centers':witness,'distances':distances},
       'three_center_radius_M1_to64':[cover_radius(m) for m in range(1,65)],
       'source_selected_parameters':'OPEN','glued_integer_grid_matches_max':3,
       'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    return receipt
if __name__=='__main__':
    r=verify(); out=ROOT/'dist/sources/metric-admission-v0.1/METRIC_ADMISSION_ROOT_VERIFICATION_v0.1.json'
    out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps({k:r[k] for k in ['status','gram_target_assignment_count','gram_target_hits','minimum_relation_gap','physical_promotion']}))
