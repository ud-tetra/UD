"""Exact admission checks, with separately marked dense numerical alias controls."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,math
from native_admission import Radical,optimize,native_generator,CLASSES
R=Path(__file__).parent;P=R/'dist/sources/native-admission-v0.1';P.mkdir(parents=True,exist_ok=True)
def mul(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def characteristic(a):
    n=len(a);b=[[F(int(i==j)) for j in range(n)] for i in range(n)];desc=[F(1)]
    for k in range(1,n+1):
        b=mul(a,b);v=-sum(b[i][i] for i in range(n))/k;desc.append(v)
        for i in range(n):b[i][i]+=v
    assert all(x==0 for row in b for x in row)
    return list(reversed(desc))
def factored(factors):
    p=[F(0),F(1)]
    for frequency_squared,count in factors:
        for _ in range(count):
            z=[F(0)]*(len(p)+2)
            for k,x in enumerate(p):z[k]+=frequency_squared*x;z[k+2]+=x
            p=z
    return p
source_cases=[]
for c,info in CLASSES.items():
    sim,b,a=native_generator(c);n=len(sim)
    assert n==info['dimension'] and all(x==0 for row in mul(b,b) for x in row)
    assert all(a[i][j]==-a[j][i] for i in range(n) for j in range(n))
    assert characteristic(a)==factored(list(zip(info['squared_positive_frequencies'],info['positive_multiplicities'])))
    source_cases.append({'carrier':c,'dimension':n,'boundary_squared_zero':True,'integer_skew_spectrum_verified':True})
checked=0;partitions=0
for n in range(2,22,2):
    for c in CLASSES:
        x=optimize(n,c);D=x['minimum_relative_spectral_floor']['radicand']
        best=Radical(F(x['minimum_relative_spectral_floor']['rational']),F(x['minimum_relative_spectral_floor']['sqrt_coefficient']),D)
        assert best.sign()>=0 and (best.sign()>0)==(n>=4)
        for row in x['partition_certificates']:
            q=row['bound'];d=Radical(F(q['rational']),F(q['sqrt_coefficient']),D);assert best<=d;partitions+=1
        intervals=x['optimal_high_centre_intervals']
        zero_only=x['partition_certificates'][-1]
        assert zero_only['zero_count']==n//2 and zero_only['high_centre_max'] is None and zero_only['high_centre_unbounded']
        for a,b in zip(intervals,intervals[1:]):assert a['max']['decimal_display']<b['min']['decimal_display']
        checked+=1
assert optimize(10,'tetra')['minimum_relative_spectral_floor']['rational']=='3'
assert optimize(10,'minus')['minimum_relative_spectral_floor']==Radical(-25,7,15).json()
assert optimize(10,'plus')['minimum_relative_spectral_floor']['rational']=='2'
assert Radical(-25,7,15)>Radical(2,0,15) and Radical(-25,7,15)<Radical(3,0,15)
# Short-clock minimizers are isolated alternatives, not their convex hull.
for c in ['minus','plus']:
    s=optimize(2,c);assert len(s['optimal_high_centre_intervals'])==2
    for r in s['optimal_high_centre_intervals']:assert r['min']==r['max']
# Enough native signed eigenspace multiplicity attains all default floors using3Q copies.
for c,info in CLASSES.items():
    demand=[4] if c=='tetra' else [2,2]
    assert all(3*m>=q for m,q in zip(info['positive_multiplicities'],demand))
    zero_capacity=3*(info['dimension']-2*sum(info['positive_multiplicities']))
    assert zero_capacity>=len([0,+2,-2])
# The compressed alias is a one-clock-component11→75 source matrix, not default dense data.
import numpy as np
from scipy.linalg import block_diag,expm
sim,b,a=native_generator('tetra');A=np.array(a,dtype=float);H=1j*A
h=np.zeros(15,complex);h[:4]=.5
v=np.zeros(15,complex);v[0]=1;v[1]=-1;u=A@v/2
pos=(v+1j*u)/2;neg=(v-1j*u)/2
assert np.linalg.norm(H@pos-2*pos)<1e-13 and np.linalg.norm(H@neg+2*neg)<1e-13
assert np.linalg.norm(H@h)<1e-13
n=10;clock=np.zeros((11,11),complex)
for j in range(n):clock[j,j+1]=clock[j+1,j]=math.sqrt((j+1)*(n-j))
vals,V=np.linalg.eigh(clock);assert np.max(np.abs(vals-np.arange(-10,11,2)))<1e-12
native=block_diag(*([H]*5));images=np.zeros((75,11),complex);zero_copy=0;pos_copy=0;neg_copy=0
for j,value in enumerate(range(-10,11,2)):
    if (value//2)%2==0:
        images[15*zero_copy:15*(zero_copy+1),j]=h;zero_copy+=1
    elif value>0:
        images[15*pos_copy:15*(pos_copy+1),j]=pos;pos_copy+=1
    else:
        images[15*neg_copy:15*(neg_copy+1),j]=neg;neg_copy+=1
E=images@V.conj().T
isometry=float(np.linalg.norm(E.conj().T@E-np.eye(11),2));residual=float(np.linalg.norm(native@E-E@clock,2))
T=math.pi/2;endpoint=float(np.linalg.norm(expm(-1j*T*native)@E-E@expm(-1j*T*clock),2))
midpoint=float(np.linalg.norm(expm(-1j*T/2*native)@E-E@expm(-1j*T/2*clock),2))
assert isometry<2e-12 and abs(residual-8)<2e-12 and endpoint<2e-12 and midpoint>1
alias={'status':'PASS','scope':'One prefix-frame clock component, Q=1; analytic full-Q extension via orthogonal copies and inverse programme dressing. No dense default matrix.','source_native_copies':5,'native_dimension':75,'clock_dimension':11,'isometry_numeric_error':isometry,'generator_residual':residual,'exact_generator_residual':'8 kappa','complete_endpoint_operator_error':endpoint,'intermediate_operator_error_at_T_over_2':midpoint,'numeric_tolerance':2e-12,'physical_promotion':0}
(P/'NATIVE_ENDPOINT_ALIAS_WITNESS_v0.1.json').write_text(json.dumps(alias,indent=2)+'\n')
receipts={'status':'PASS','version':'0.1','physical_promotion':0,'fresh_native_source_cases':source_cases,
 'exact_optimization_cases':checked,'exact_ordered_partition_certificates':partitions,'disconnected_optimizer_union_controls':2,'all_zero_unbounded_interval_controls':checked,
 'sufficient_copy_capacity_checks':3,'dense_numeric_alias_controls':1,'scope':'Exact rational/field and reconstructed incidence checks. Dense matrix alias diagnostics are numerical; general residual/minimum/sharpness/alias results have separate proofs. No source-acquired encoding, physical comparison or independent human review.',
 'source_sha256':{f:hashlib.sha256((R/f).read_bytes()).hexdigest() for f in ['native_admission.py','programmed_clock.py','joint_carrier.py']}}
(P/'NATIVE_ADMISSION_ROOT_VERIFICATION_v0.1.json').write_text(json.dumps(receipts,indent=2)+'\n');print(json.dumps(receipts));print(json.dumps(alias))
