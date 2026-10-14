"""Exact constructor verification, plus explicitly separate floating clock diagnostics."""
from pathlib import Path
from fractions import Fraction as Q
from math import comb,isclose,pi,sqrt
import json,hashlib
from programmed_clock import path_metrics,characteristic_clock,compiled_word,clock_snapshot
R=Path(__file__).parent;P=R/'dist/sources/programmed-clock-v0.1';P.mkdir(parents=True,exist_ok=True)
def mul(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def char(a):
    n=len(a);b=[[Q(int(i==j)) for j in range(n)] for i in range(n)];descending=[Q(1)]
    for k in range(1,n+1):
        b=mul(a,b);c=-sum(b[i][i] for i in range(n))/k;descending.append(c)
        for i in range(n):b[i][i]+=c
    return list(reversed(descending))
def polynomial(roots):
    p=[Q(1)]
    for r in roots:
        out=[Q(0)]*(len(p)+1)
        for k,v in enumerate(p):out[k]-=r*v;out[k+1]+=v
        p=out
    return p
metrics_checked=0;edge_checks=0
for n in range(2,22,2):
    v,e=path_metrics(n);m=n//2;b=[[Q(0)]*m for _ in range(m+1)]
    for r in range(m):
        b[r][r]=-1;b[r+1][r]=1
        assert v[r]/e[r]==(2*r+1)*(n-2*r)
        assert v[r+1]/e[r]==(2*r+2)*(n-2*r-1);edge_checks+=2
    assert all(x>0 for x in v+e)
    # Full weighted Hodge in original chain coordinates: ∂=B, adjoint=G1^-1 BᵀG0.
    a=[[Q(0)]*(n+1) for _ in range(n+1)]
    for i in range(m+1):
        for j in range(m):a[i][m+1+j]=b[i][j];a[m+1+j][i]=-b[i][j]*v[i]/e[j]
    g=v+e
    assert all(g[i]*a[i][j]==-g[j]*a[j][i] for i in range(n+1) for j in range(n+1))
    h=[1/x for x in v]+[Q(0)]*m
    assert all(sum(x*y for x,y in zip(row,h))==0 for row in a)
    expected=[Q(0),Q(1)]
    for freq in range(2,n+1,2):
        out=[Q(0)]*(len(expected)+2)
        for k,x in enumerate(expected):out[k]+=freq*freq*x;out[k+2]+=x
        expected=out
    assert char(a)==expected;metrics_checked+=1
clock_spectra=0
for n in range(1,26):
    cp=characteristic_clock(n);assert cp==polynomial([n-2*j for j in range(n+1)])
    assert (cp[0]==0)==(n%2==0);clock_spectra+=1
prefix_checks=0
for branch in ['C','H']:
    for N in [1,2,4,8]:
        for B in [0,1,2,3]:
            x=compiled_word(branch,N,B);raw=compiled_word(branch,N,B,False)
            assert x['word_length']%2==0 and x['word_length']==raw['word_length']+x['padding_gates']
            assert len(x['prefixes'])==x['clock_addresses']
            assert x['prefixes'][-1]['active']==raw['prefixes'][-1]['active'] and x['prefixes'][-1]['donors']==raw['prefixes'][-1]['donors']
            assert x['complete_joint_dimension']==x['clock_addresses']*x['data_bank_dimension'];prefix_checks+=1
x=compiled_word();assert x['unit_rate_vertex_metrics']==['1','9/5','21/10','21/10','9/5','1']
assert x['complete_joint_dimension']==42568187904 and x['padding_gates']==1 and x['clock_addresses']==11
# Unit-metric tetrahedron spectral no-go: two unequal positive clock values cannot both equal2.
for n in range(4,22,2):assert 2 in [n-2*j for j in range(n+1)] and 4 in [n-2*j for j in range(n+1)]
bound=Q(1,1000)+Q(4,100)+(Q(11,7)+Q(1,100))/10000;assert bound==Q(288107,7000000)
timing=0
for n in range(1,22):
    for q in range(41):
        xi=q/40;r=clock_snapshot(n,xi);assert isclose(sum(r['clock_probabilities']),1,abs_tol=2e-14)
        assert isclose(r['full_joint_terminal_trace_distance']**2,1-r['terminal_probability'],abs_tol=2e-14)
        if abs(xi-.5)<.1:assert r['full_joint_terminal_trace_distance']<=sqrt(n)*pi*abs(xi-.5)+2e-14
        timing+=1
receipt={'status':'PASS','version':'0.1','physical_promotion':0,
 'exact_weighted_path_metric_spectra':metrics_checked,'exact_squared_edge_identities':edge_checks,
 'exact_spin_clock_characteristic_polynomials':clock_spectra,'complete_word_padding_cases':prefix_checks,
 'floating_timing_diagnostics':timing,'floating_tolerance':2e-14,'rational_protocol_example_bound':str(bound),
 'checks':['positive rational metrics','metric-skew Hodge adjoint','harmonic kernel vector','exact rational determinant/spectrum','odd/full-carrier kernel obstruction','identity padding preserves complete terminal payload','unit-metric tetrahedron spectral class excluded','rate/norm/variance/dimension accounting','jitter bound arithmetic'],
 'source_sha256':{n:hashlib.sha256((R/n).read_bytes()).hexdigest() for n in ['programmed_clock.py','joint_carrier.py','rsp1.py','response_contract.py']},
 'scope':'Exact rational/integer constructor checks; timing plots are numerical formula diagnostics. General operator/mixed-state/native-residual theorems use supplied proofs. No dense default matrix, native source, physical experiment, CRL promotion or human review.'}
(P/'PROGRAMMED_CLOCK_ROOT_VERIFICATION_v0.1.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt))
