"""Read-only replay of frozen cover exhaustion and exact local formula diagnostic."""
import sys
sys.dont_write_bytecode=True
import json,hashlib
from fractions import Fraction as F
from pathlib import Path
import planner as P
import kernel as K
HERE=Path(__file__).resolve().parent

def main():
 contract=json.loads((HERE/'CONTRACT.json').read_text());repo=HERE.parents[1]
 for d in contract['source_dependencies']:
  p=repo/d['path'];assert p.stat().st_size==d['size_bytes'] and hashlib.sha256(p.read_bytes()).hexdigest()==d['sha256']
 original=K.certificate;lastbox=None;lastcerts=[];calls=0;accepted=0
 def observed(sid,box):
  nonlocal lastbox,lastcerts,calls,accepted
  if lastbox!=box:lastbox=box;lastcerts=[]
  cert=original(sid,box);lastcerts.append(cert);calls+=1
  if len(lastcerts)==len(K.BANK) and min(F(x['total_radius']) for x in lastcerts)<=F(contract['target']):accepted+=1
  return cert
 K.certificate=observed
 try:P.create_cover(contract)
 except AssertionError as ex:
  assert str(ex)=='unresolved cell at depth budget';reason=str(ex)
 else:raise AssertionError('Expected frozen-budget exhaustion did not recur')
 finally:K.certificate=original
 assert len(lastcerts)==20 and all(F(x['total_radius'])>F(contract['target']) for x in lastcerts)
 wl,wu,gl,gu=lastbox;w=(wl+wu)/2;g=(gl+gu)/2;points={sid:K.point_formula_bounds(sid,w,g) for sid in sorted(K.BANK)};lo=min(v[0] for v in points.values());hi=min(v[1] for v in points.values());cert=min(lastcerts,key=lambda x:(F(x['total_radius']),x['state']))
 result={'status':'UNRESOLVED_FROZEN_BUDGET','classification':'EXACT_CONDITIONAL_FORMULA_AND_ALGORITHM_DIAGNOSTIC','reason':reason,'goal':contract['complete_cover_domain'],'finite_algorithm_budget':contract['finite_algorithm_budget'],'certificate_calls_before_stop':calls,'accepted_leaf_visits_before_stop':accepted,'partial_leaves_published_as_coverage':False,'first_unresolved_box':list(map(str,lastbox)),'box_best_state':cert['state'],'box_minimum_total_upper':cert['total_radius'],'box_certificates':lastcerts,'midpoint':{'omega':str(w),'gamma':str(g),'formula_bounds_by_state':{s:list(map(str,v)) for s,v in points.items()},'minimum_formula_lower':str(lo),'minimum_model_upper':str(hi),'all_twenty_formulas_above_target':lo>F(contract['target'])},'prior_certified_upper_gamma':'17/100','scope':'The frozen algorithm failed to certify the proposed extension. A positive lower here applies only to the twenty particular transported-upper formulas, never to actual approximation error or every possible certificate. No new runtime guard or uniform extension claim.','scientific_status':'OPEN','independent_review':False,'physical_promotion':0}
 P.save_or_compare('REFINEMENT_DIAGNOSTIC_RESULTS.json',result);print('PASS reproduced expected unresolved depth budget; midpoint=('+str(w)+','+str(g)+'); minimum formula lower='+str(float(lo))+'; all twenty above target='+str(lo>F(contract['target'])),flush=True)
if __name__=='__main__':main()
