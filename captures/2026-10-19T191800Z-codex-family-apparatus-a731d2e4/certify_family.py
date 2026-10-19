"""Directed scalar theorem replay; no estimator, full Hankel, or physical fit."""
import json, hashlib
from pathlib import Path
from fractions import Fraction as F
from flint import arb, fmpq, ctx
ctx.prec = 512
P = Path(__file__).resolve().parent
def load(n): return json.loads((P/n).read_text())
def a(x):
    if isinstance(x, (list,tuple)): return arb(fmpq(int(x[0]),int(x[1])))
    return arb(x)
def edge(x, lower=False):
    y=x*(1<<180)
    z=(y.floor() if lower else y.ceil()).unique_fmpz()
    assert z is not None
    return [int(z),1<<180]
def certify(raw=None):
    n,v=37*8191*62,37*8191
    h=a([1,1<<48]); c=a([1,1<<24])
    src=load('inputs/SOURCE_BOUNDS.json')
    f2=F(*map(int,src['raw_baseline_Frobenius_squared']))
    if raw is not None:
        import numpy as np
        raw=Path(raw)
        assert raw.stat().st_size==n*8
        digest=hashlib.sha256()
        with raw.open('rb') as f:
            while b:=f.read(1<<20): digest.update(b)
        assert digest.hexdigest()==load('INPUT_PROVENANCE.json')['baseline_raw_sha256']
        y=np.memmap(raw,dtype='<i8',mode='r')
        total=0
        for k in range(0,n,65536):
            block=y[k:k+65536].astype(object); total+=int(block@block)
        assert F(total,1<<96)==f2
    null=load('inputs/NULL_VECTOR.json')['vector']
    null2=sum(x*x for x in null); assert null2==16228
    k2=F(320*4*2294+null2,128**2); assert k2==F(738137,4096)
    k=a([k2.numerator,k2.denominator]).sqrt(); f0=a([f2.numerator,f2.denominator]).sqrt()
    generation=load('inputs/BASE_GENERATION.json')['row']
    assert generation['case']=='ramp_clock_stress'
    assert generation['record_sha256']==load('INPUT_PROVENANCE.json')['baseline_raw_sha256']
    d0=a(generation['evaluation_bounds']['scalar_waveform_error_upper'])
    assert F(*generation['evaluation_bounds']['scalar_waveform_error_upper'])==F(278304534082539066,1<<120)+F(1,1<<49)
    anchors=load('inputs/ANCHORS.json')['rows']; data=load('inputs/ANCHOR_DATA.json')['records']
    assert len(anchors)==len(data)==6
    gs=[]
    for cert,record in zip(anchors,data):
        assert cert['case']==record['case'] and cert['record_sha256']==record['record_sha256']
        assert record['raw_quantum']==[1,1<<48]
        assert cert['cutoff']['status']=='CERTIFIED_EXACT_SKETCH_CUTOFF_209'
        assert cert['cutoff']['learned_order']==209 and cert['cutoff']['cutoff']==[1,1<<24]
        assert record['per_new_nominal_vector_integer_squared_error_max']<=1
        m=record['transform_integer_matrix']; den=record['transform_denominator']
        assert len(m)==37 and all(len(row)==37 for row in m)
        for i in range(37):
            for j in range(37):
                assert sum(m[i][t]*m[j][t] for t in range(37))==(den*den if i==j else 0)
                if i%2!=j%2: assert m[i][j]==0
        gs.append(a(cert['cutoff']['sigma209_lower']))
    g=min(gs)
    tail=lambda delta:k*((d0+h/2)*a(n).sqrt()+delta*a(v).sqrt())
    delta=1127*h; rho=a([1,1<<20])
    assert tail(delta)<c/2 and tail(delta+h)>=c/2
    base=k*(h*a(n).sqrt()+(delta+h)*a(v).sqrt())
    rhocrit=(g-c-base)/(2*k*f0)
    assert rho<rhocrit and 2*rho>=rhocrit
    distance=k*f0*rho+base
    lo=g-distance; hi=tail(delta)
    assert lo>c and hi<c
    # Budget success/failure are proof-contour decisions, not actual failure limits.
    controls={'1127_half_tail':bool(tail(delta)<c/2),
              '1128_half_tail_refused':bool(tail(delta+h)>=c/2),
              'radius_half_gap':bool(rho<rhocrit),
              'doubled_radius_half_gap_refused':bool(2*rho>=rhocrit),
              'strict_lower_cutoff':bool(lo>c),'strict_upper_cutoff':bool(hi<c)}
    return {'status':'DERIVED_UNIFORM_EXACT_SKETCH_CUTOFF_209',
        'anchor_cases':[r['case'] for r in anchors], 'anchor_count':6,
        'nscalar':n,'nvector':v,'sketch_shape':[8191,321],
        'rho':[1,1<<20],'delta_per_62_vector':[1127,1<<48],
        'cutoff':[1,1<<24], 'sigma209_lower':edge(lo,True),
        'sigma210_upper':edge(hi),'anchor_min_lower':edge(g,True),
        'distance_upper':edge(distance),'rho_critical_lower':edge(rhocrit,True),
        'rho_critical_upper':edge(rhocrit),'sketch_F_squared':[k2.numerator,k2.denominator],
        'baseline_F_squared':[str(f2.numerator),str(f2.denominator)],
        'controls':controls,'new_estimator_runs':0,
        'scope':'Exact projected cutoff for the declared orthogonal same-parity tube and encoded per-vector noise ball. Future solver/frame/phase checks and apparatus qualification separate.',
        'readable':{'sigma209_lower':float(a(edge(lo,True))), 'sigma210_upper':float(a(edge(hi))), 'delta':float(delta),'rho':float(rho)},
        'physical_promotion':0,'external_review':'PENDING'}
