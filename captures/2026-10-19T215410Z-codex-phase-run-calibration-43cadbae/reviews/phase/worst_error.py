"""Post-known descriptive two-sided global emitted-error witness; no new gate."""
import argparse,json,hashlib
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from decimal import Decimal,getcontext
import numpy as np
from flint import arb,fmpq,ctx
ctx.prec=512;getcontext().prec=250
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();load=lambda p:json.loads(Path(p).read_text())
q=lambda x:F(int(x[0]),int(x[1]));a=lambda x:arb(fmpq(x.numerator,x.denominator));pair=lambda x:[str(x.numerator),str(x.denominator)]
def endpoint(x,upper):
    v=x.upper() if upper else x.lower();n=((v*(1<<180)).ceil() if upper else (v*(1<<180)).floor()).unique_fmpz();assert n is not None;return F(int(n),1<<180)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--source',required=True);args=ap.parse_args();S=Path(args.source).resolve();f=load(P/'WORST_ERROR_FREEZE.json');assert sha(Path(__file__))==f['script_sha256']
    for n,h in f['producer_files'].items():assert sha(S/n)==h,n
    phase=load(S/'PHASE_CERTIFICATE.json');targets=load(S/'inputs/SOURCE_PHASE.json')['target_matches'];rows=[]
    for case in phase['rows']:
        assert case['status']=='CERTIFIED_FINITE_EMITTED_MATCH_AND_SAVED_NUMERICAL_QUALITY'
        path=S/'results'/case['case']/'PHASE_PROPOSAL.npz';assert sha(path)==f['phase_proposal_hashes'][case['case']];em=np.load(path,allow_pickle=False)['two_step_phase']
        for m in case['observed']['rows']:
            i,j=m['emitted_index'],m['target_index'];d=F(int(em[i]),1<<60)-2*q(targets[j]['omega']);exact=None
            if abs(a(d))<arb.pi():lo=hi=abs(d);exact=abs(d)
            else:
                vals=[abs(a(d)+2*k*arb.pi()) for k in range(-3,4)];pick=min(range(7),key=lambda k:float(vals[k].upper()));assert all(vals[pick].upper()<vals[k].lower() for k in range(7) if k!=pick)
                lo=endpoint(vals[pick],False);hi=endpoint(vals[pick],True)
            assert 0<=lo<=hi<=q(m['circular_error_upper'])
            rows.append({'case':case['case'],'emitted_index':i,'target_index':j,'target_label':targets[j]['label'],'lower':lo,'upper':hi,'exact':exact,'emitted_integer':int(em[i]),'target_omega':targets[j]['omega']})
    assert len(rows)==836;L=max(r['lower'] for r in rows);U=max(r['upper'] for r in rows);candidates=[r for r in rows if r['upper']>=L]
    exact=all(r['exact'] is not None and r['exact']==L for r in candidates) and all(r['upper']<=L for r in rows)
    if exact:U=L
    quantum=F(1,10**22);dl=(L//quantum)*quantum
    # Safe fixed-decimal outward enclosure; use one grid step above floor(U)
    # unless U itself is exactly on the decimal grid.
    du=(U//quantum)*quantum
    if du<U:du+=quantum
    assert dl<=L<=U<=du
    case_bounds=[]
    for name in [c['case'] for c in phase['rows']]:
        rr=[r for r in rows if r['case']==name];case_bounds.append({'case':name,'maximum_error_lower':pair(max(r['lower'] for r in rr)),'maximum_error_upper':pair(max(r['upper'] for r in rr))})
    out={'status':'RIGOROUS_POST_KNOWN_GLOBAL_WORST_EMITTED_ERROR_INTERVAL','utc':datetime.now(timezone.utc).isoformat(),'freeze_sha256':sha(P/'WORST_ERROR_FREEZE.json'),'emissions_checked':836,'global_maximum_error_lower':pair(L),'global_maximum_error_upper':pair(U),'global_maximum_exactly_rational':exact,'safe_decimal_bracket':[str(Decimal(dl.numerator)/Decimal(dl.denominator)),str(Decimal(du.numerator)/Decimal(du.denominator))],'worst_candidates':[{k:(pair(v) if isinstance(v,F) else v) for k,v in r.items()} for r in candidates],'case_maxima':case_bounds,'unit':'radians per TWO-step sample, circular modulo2pi','scope':'Post-known descriptive achieved-error quantification only. No new campaign admission gate, no retuning of fixed identity cap, and no equation to six-ratio calibration error or SI accuracy.','new_estimator_SVD_eigenvalue_inverse_alignment_calls':0,'external_review':'PENDING','physical_promotion':0}
    path=P/'WORST_ERROR_RECEIPT.json';assert not path.exists();path.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':out['status'],'exact':exact,'decimal_bracket':out['safe_decimal_bracket'],'receipt_sha256':sha(path)}))
if __name__=='__main__':main()
