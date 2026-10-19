"""Exact endpoint comparison with pre-existing independent source receipt."""
import hashlib,json
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent;P=ROOT/'family-apparatus-work'
load=lambda p:json.loads(Path(p).read_text())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()

def run():
 fr=load(HERE/'ENDPOINT_COMPARE_FREEZE.json')
 for p,h in fr['files'].items():assert sha(ROOT/p)==h,p
 protocol=load(P/'PROTOCOL_FREEZE.json')
 for p,h in protocol['files'].items():assert sha(P/p)==h,p
 actual=load(P/'results/FAMILY_CERTIFICATE.json');independent=load(HERE/'SOURCE_BOUNDS.json');expected=independent['rows'][0]
 pairs={'rho':expected['rho'],'delta_per_62_vector':expected['delta'],'sigma209_lower':expected['sigma209_lower'],'sigma210_upper':expected['sigma210_upper'],'rho_critical_lower':expected['critical_rho_lower'],'rho_critical_upper':expected['critical_rho_upper'],'anchor_min_lower':independent['anchor_sigma209_min_lower'],'sketch_F_squared':independent['sketch_Frobenius_squared'],'baseline_F_squared':independent['raw_baseline_Frobenius_squared']}
 for key,pair in pairs.items():assert F(*map(int,actual[key]))==F(*map(int,pair)),key
 g=independent['anchor_sigma209_min_lower'];lo=expected['sigma209_lower'];assert g[1]==lo[1]
 assert actual['distance_upper']==[g[0]-lo[0],g[1]]
 assert actual['nscalar']==independent['nscalar'] and actual['nvector']==independent['nvector'] and actual['cutoff']==[1,1<<24]
 assert all(actual['controls'].values()) and actual['new_estimator_runs']==0 and actual['physical_promotion']==0 and actual['external_review']=='PENDING'
 for p,h in fr['files'].items():assert sha(ROOT/p)==h,p
 out={'status':'PASS_EXACT_ENDPOINT_IDENTITY_NO_TOLERANCES','compared_pair_fields':list(pairs)+['distance_upper'],'exact_comparison_method':'Fraction equality; common2^-180 grid identity for distance complement','no_additive_or_relative_tolerance':True,'family_certificate_sha256':sha(P/'results/FAMILY_CERTIFICATE.json'),'independent_source_receipt_sha256':sha(HERE/'SOURCE_BOUNDS.json'),'protocol_sha256':sha(P/'PROTOCOL_FREEZE.json'),'freeze_sha256':sha(HERE/'ENDPOINT_COMPARE_FREEZE.json'),'all_frozen_bytes_before_after_equal':True,'completed_utc':datetime.now(timezone.utc).isoformat(),'scope':'Same-team comparison with independently computed scalar endpoints and exact raw norm receipt. No family generation, estimator, phase or apparatus verification.','external_review':'PENDING','physical_promotion':0}
 q=HERE/'ENDPOINT_COMPARISON.json';assert not q.exists();q.write_text(json.dumps(out,indent=2))

if __name__=='__main__':run()
