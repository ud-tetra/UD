"""Exact saved-T spectral extension; no eigenvalue solver or estimator calls."""
import argparse,hashlib,json
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
from flint import arb,fmpq,ctx
ctx.prec=512
P=Path(__file__).resolve().parent
pair=lambda q:[str(q.numerator),str(q.denominator)]
def q(x):return Q(int(x[0]),int(x[1]))
def a(x):
    x=Q(x);return arb(fmpq(x.numerator,x.denominator))
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def up(x):
    n=(arb(x.upper())*(1<<180)).ceil().unique_fmpz();assert n is not None
    return Q(int(n),1<<180)
def below(x):
    n=(arb(x.lower())*(1<<180)).floor().unique_fmpz();assert n is not None
    return Q(int(n),1<<180)
def predicates(rho,e,h,s2,m2):
    assert rho>=0 and e>=0 and h>0 and s2>=0 and m2>=0
    if rho>=1:return 'HOLD_INVERSE_PREMISE',None
    R=e*h/(1-rho)
    if s2<=4*R*R:return 'HOLD_CENTER_DISKS_NOT_DISJOINT',R
    if m2<=R*R:return 'HOLD_ORIGIN_NOT_EXCLUDED',R
    return 'CERTIFIED_EXACT_T_DISK_BIJECTION',R
def phase_predicate(total,sep):
    return "CERTIFIED_EXACT_T_SOURCE_PHASE_BIJECTION" if total<sep/2 else "HOLD_EXACT_T_SOURCE_PHASE"
def controls():
    cases=[('zero_residual',Q(0),Q(0),Q(1),Q(4),Q(1),'CERTIFIED_EXACT_T_DISK_BIJECTION'),('inverse_equality',Q(1),Q(0),Q(1),Q(4),Q(1),'HOLD_INVERSE_PREMISE'),('disk_touch_equality',Q(0),Q(1),Q(1),Q(4),Q(4),'HOLD_CENTER_DISKS_NOT_DISJOINT'),('origin_touch_equality',Q(0),Q(1),Q(1),Q(16),Q(1),'HOLD_ORIGIN_NOT_EXCLUDED'),('small_positive_residual',Q(1,8),Q(1,100),Q(2),Q(4),Q(1),'CERTIFIED_EXACT_T_DISK_BIJECTION')]
    out=[]
    for name,r,e,h,s,m,expected in cases:
        actual,R=predicates(r,e,h,s,m);assert actual==expected;out.append({'id':name,'expected':expected,'actual':actual})
    actual=phase_predicate(Q(1,2),Q(1));assert actual=='HOLD_EXACT_T_SOURCE_PHASE'
    out.append({'id':'source_half_radius_equality','expected':'HOLD_EXACT_T_SOURCE_PHASE','actual':actual})
    return {'status':'PASS_SIX_EXACT_BOUNDARY_CONTROLS','rows':out,'new_fits':0,'physical_promotion':0}
def exact_centers(z):
    assert z.dtype==np.complex128 and z.shape==(209,) and np.isfinite(z).all()
    rr=[float(x.real).as_integer_ratio() for x in z];ii=[float(x.imag).as_integer_ratio() for x in z]
    b=max(d.bit_length()-1 for n,d in rr+ii)
    re=[n<<(b-(d.bit_length()-1)) for n,d in rr];im=[n<<(b-(d.bit_length()-1)) for n,d in ii]
    s2=min((re[j]-re[k])**2+(im[j]-im[k])**2 for j in range(209) for k in range(j))
    m2=min(x*x+y*y for x,y in zip(re,im));return Q(s2,1<<(2*b)),Q(m2,1<<(2*b))
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--phase-dir',required=True);ap.add_argument('--repo',required=True);ap.add_argument('--out',required=True);args=ap.parse_args()
    phase=Path(args.phase_dir).resolve();repo=Path(args.repo).resolve();out=Path(args.out).resolve()
    assert P not in out.parents and phase not in out.parents and out not in [P,phase];out.mkdir(parents=True,exist_ok=False)
    freeze=json.loads((P/'EXACT_T_FREEZE.json').read_text())
    for n,h in freeze['files'].items():assert sha(P/n)==h,n
    for n,h in freeze['phase_inputs'].items():assert sha(phase/n)==h,n
    protocol=json.loads((phase/'PROTOCOL_FREEZE.json').read_text())
    for n,h in protocol['files'].items():assert sha(phase/n)==h,n
    for n,h in protocol['source_files'].items():
        rel=Path(n);assert rel.parts[0]=='ud-repo' and '..' not in rel.parts
        assert sha(repo/Path(*rel.parts[1:]))==h,n
    proof=json.loads((phase/'CERTIFICATE.json').read_text());index=json.loads((phase/'SOURCE_INDEX.json').read_text())
    assert len(proof['rows'])==len(index['cases'])==4 and proof['amplitudes']==[0,1,2,4]
    (out/'CONTROLS.json').write_text(json.dumps(controls(),indent=2)+'\n');rows=[]
    for old,source in zip(proof['rows'],index['cases']):
        assert old['case']==source['case'] and old['status']=='CERTIFIED_FINITE_EMITTED_MATCH_AND_SAVED_NUMERICAL_QUALITY' and old['learned_order']==209
        assert set(old['gates'])=={'inverse_residual','proposed_inverse_norm','eigenpair_residual','emitted_argument_error','emission_ties_even_consistency','finite_observed_bijection'} and all(v is True for v in old['gates'].values())
        assert old['observed']['bijective'] is True and len(old['observed']['rows'])==209
        p=repo/source['repository_sources']['PHASE_META.npz']['source_path'];assert sha(p)==source['repository_sources']['PHASE_META.npz']['sha256']
        with np.load(p,allow_pickle=False) as z:s2,m2=exact_centers(z['eigenvalues'])
        mt=old['metrics'];rho,e,h=q(mt['inverse_residual']),q(mt['eigenpair_residual']),q(mt['proposed_inverse_norm'])
        status,R=predicates(rho,e,h,s2,m2);row={'case':old['case'],'prior_frame':old['prior_frame_verdict_unchanged'],'disk_status':status,'minimum_center_separation_squared':pair(s2),'minimum_center_modulus_squared':pair(m2),'radius':None if R is None else pair(R),'physical_promotion':0}
        if status=='CERTIFIED_EXACT_T_DISK_BIJECTION':
            displacement=up((a(R)/a(m2).sqrt()).asin());total=displacement+q(mt['emitted_argument_error'])+q(old['observed']['maximum_circular_error_upper']);sep=q(protocol['minimum_target_chord_lower']);phase_status=phase_predicate(total,sep)
            row.update(status=phase_status,phase_displacement_upper=pair(displacement),exact_T_to_source_angular_upper=pair(total),fixed_source_half_chord=pair(sep/2),center_separation_lower=pair(below(a(s2).sqrt())),center_modulus_lower=pair(below(a(m2).sqrt())),readable_radius_upper=float(a(R).upper()),readable_exact_T_phase_upper=float(a(total).upper()),algebraic_eigenvalue_count_per_disk=1)
        else:row['status']=status
        rows.append(row)
    result={'status':'COMPLETE_FOUR_SAVED_EXACT_T_SPECTRAL_ENCLOSURES','rows':rows,'phase_certificate_sha256':sha(phase/'CERTIFICATE.json'),'extension_freeze_sha256':sha(P/'EXACT_T_FREEZE.json'),'center_pair_distances_checked':4*209*208//2,'new_estimator_SVD_eigenvalue_inverse_alignment_calls':0,'scope':'Post-known-outcome finite exact dyadic T eigenvalue/phase enclosure conditional on independently replayed saved residual/inverse premises; no uniform noise-ball, SI/unaliased frequency, idealSVD or physical claim','external_review':'PENDING','physical_promotion':0}
    for n,h in freeze['files'].items():assert sha(P/n)==h,n
    (out/'EXACT_T_CERTIFICATE.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'statuses':[r['status'] for r in rows],'phase_upper_max':max(r.get('readable_exact_T_phase_upper',0) for r in rows),'new_fits':0}))
if __name__=='__main__':main()
