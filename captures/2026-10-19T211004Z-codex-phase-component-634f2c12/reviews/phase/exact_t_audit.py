"""Independent finite exact-T extension audit; Fraction centers and atan geometry."""
import json,hashlib
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import numpy as np
from flint import arb,fmpq,ctx
ctx.prec=512
ROOT=Path('/workspace/scratch/f3d1c2f040c9');P=ROOT/'directional-phase-audit-20261019';EXT=ROOT/'phase-component-work-20261019';PHASE=ROOT/'directional-phase-work-20261019';RESULT=Path('/tmp/ud-exact-T-run1-20261019/EXACT_T_CERTIFICATE.json')
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
q=lambda x:F(int(x[0]),int(x[1]));a=lambda x:arb(fmpq(x.numerator,x.denominator));pair=lambda x:[str(x.numerator),str(x.denominator)]

def main():
    f=load(P/'EXACT_T_AUDIT_FREEZE.json');assert sha(Path(__file__))==f['script_sha256']
    for path,h in f['inputs'].items():assert sha(path)==h,path
    extfreeze=load(EXT/'EXACT_T_FREEZE.json')
    for n,h in extfreeze['files'].items():assert sha(EXT/n)==h,n
    for n,h in extfreeze['phase_inputs'].items():assert sha(PHASE/n)==h,n
    own=load(P/'AUDIT_V2_RECEIPT.json');comparison=load(P/'COMPARE_RECEIPT.json');assert comparison['status']=='INDEPENDENT_ASSIGNMENT_FRACTION_AND_DIRECTED_ENDPOINT_COMPARISON_PASS'
    phase=load(PHASE/'CERTIFICATE.json');index=load(PHASE/'SOURCE_INDEX.json');cert=load(RESULT)
    assert len(own['rows'])==len(phase['rows'])==len(index['cases'])==len(cert['rows'])==4
    source_half=q(own['fixed_source_chord_lower'])/2;rows=[]
    for independent,old,source,row in zip(own['rows'],phase['rows'],index['cases'],cert['rows']):
        assert independent['case']==old['case']==source['case']==row['case']
        p=ROOT/'ud-repo'/source['repository_sources']['PHASE_META.npz']['source_path'];assert sha(p)==source['repository_sources']['PHASE_META.npz']['sha256']
        z=np.load(p,allow_pickle=False)['eigenvalues'];assert z.dtype==np.complex128 and z.shape==(209,) and np.isfinite(z).all()
        # Different representation from producer: per-entry exact Fraction pairs,
        # with no common denominator integer-vector construction.
        centers=[(F(*float(x.real).as_integer_ratio()),F(*float(x.imag).as_integer_ratio())) for x in z]
        distances=[((x-u)**2+(y-v)**2,j,k) for j,(x,y) in enumerate(centers) for k,(u,v) in enumerate(centers[:j])]
        s2,ji,ki=min(distances);m2=min(x*x+y*y for x,y in centers)
        assert s2==q(row['minimum_center_separation_squared']) and m2==q(row['minimum_center_modulus_squared'])
        metrics=old['metrics'];rho=q(metrics['inverse_residual']);e=q(metrics['eigenpair_residual']);h=q(metrics['proposed_inverse_norm'])
        inverse2=q(independent['exact_inverse_residual_squared']);eigen2=q(independent['exact_eigenpair_residual_squared']);hn2=q(independent['proposed_inverse_norm_bound_squared'])
        assert rho>=0 and rho<1 and e>=0 and h>0
        assert rho*rho>=inverse2 and e*e>=eigen2 and h*h>=hn2
        R=e*h/(1-rho);assert R==q(row['radius']) and s2>4*R*R and m2>R*R
        # An independently tighter radius from exact squared residuals must fit
        # within the producer's rational upper-premise radius.
        R_alt=a(eigen2).sqrt()*a(hn2).sqrt()/(1-a(inverse2).sqrt());assert R_alt.upper()<=a(R)
        # asin(R/sqrt(m2)) = atan(R/sqrt(m2-R²)), using a different function/path.
        displacement=(a(R)/a(m2-R*R).sqrt()).atan();published=q(row['phase_displacement_upper'])
        assert displacement.upper()<=a(published)
        total=published+q(metrics['emitted_argument_error'])+q(old['observed']['maximum_circular_error_upper'])
        assert total==q(row['exact_T_to_source_angular_upper']) and total<source_half==q(row['fixed_source_half_chord'])
        for name,square in [('center_separation_lower',s2),('center_modulus_lower',m2)]:
            lower=q(row[name]);assert 0<=lower and lower*lower<=square and (lower+F(1,1<<180))**2>square
        assert row['disk_status']=='CERTIFIED_EXACT_T_DISK_BIJECTION' and row['status']=='CERTIFIED_EXACT_T_SOURCE_PHASE_BIJECTION' and row['algebraic_eigenvalue_count_per_disk']==1
        assert row['prior_frame']==old['prior_frame_verdict_unchanged']
        rows.append({'case':row['case'],'independent_exact_center_minimum_squared':pair(s2),'minimum_center_pair':[ji,ki],'independent_exact_minimum_modulus_squared':pair(m2),'validated_rational_radius':pair(R),'strict_disk_separation':True,'strict_origin_exclusion':True,'independent_atan_phase_upper_validates_published_arcsine':True,'validated_total_phase_upper':pair(total),'strict_half_fixed_source_separation':True,'prior_frame_unchanged':row['prior_frame']})
    maximum=max(q(r['validated_total_phase_upper']) for r in rows);assert maximum<F(9413,10**15)
    receipt={'status':'SAME_TEAM_EXACT_T_DISK_AND_SOURCE_PHASE_AUDIT_PASS','utc':datetime.now(timezone.utc).isoformat(),'freeze_sha256':sha(P/'EXACT_T_AUDIT_FREEZE.json'),'rows':rows,'exact_center_pair_distances_checked':4*209*208//2,'center_moduli_checked':4*209,'maximum_phase_upper':pair(maximum),'safe_decimal_upper':'9.413e-12 radians per TWO-step sample','theorem_review':'Normality applies to diagonal Lambda in the similarity basis; disjoint-disk counts follow by homotopy with enlarged boundary-free radius; no V norm factor is omitted.','new_estimator_SVD_eigenvalue_inverse_alignment_calls':0,'scope':'Four exact saved dyadic T matrices with replayed complex residual/inverse premises. No uniform noise-ball, SI or unaliased primitive-frequency claim; old frame refusals unchanged.','external_review':'PENDING','physical_promotion':0}
    out=P/'EXACT_T_AUDIT_RECEIPT.json';assert not out.exists();out.write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({'status':receipt['status'],'receipt_sha256':sha(out),'center_pair_checks':receipt['exact_center_pair_distances_checked']}))
if __name__=='__main__':main()
