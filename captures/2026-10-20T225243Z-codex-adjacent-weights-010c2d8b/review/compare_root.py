#!/usr/bin/env python3
"""Independent closed-form and directed-rounding audit of root finite cases."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
P=Path(__file__).resolve().parent;B=P.parent;file=B/'c25_math/RESULT.json';a=json.loads(file.read_text());src=json.loads((P/'SOURCE_CHECKS.json').read_text());orb=json.loads((P/'ORBIT_CHECKS.json').read_text());checks=0;rows=[];grid=F(1,2**160)
assert a['new_exact_checks']['chain_dimensions']==src['chain_dimensions'];checks+=1
assert a['new_exact_checks']['boundary_squared_columns']==1800;checks+=1
assert a['new_exact_checks']['cochain_restriction_entries']==[60,60];checks+=1
assert a['new_exact_checks']['max_abs_row_sum_A']==orb['nominal_absolute_row_bound'];checks+=1
assert a['new_exact_checks']['vanishing_cross_channel_columns']==6*2640;checks+=1
assert a['new_exact_checks']['metric_transform_triplet_checks']==8*600*4;checks+=1
for case in a['weighted_cases']:
 m=case['selected_count'];assert m in[1,10];checks+=1
 assert case['tetrahedron_indices']==([0]if m==1 else orb['orbit_indices']);checks+=1
 assert case['preserves_C10']==(m==10);checks+=1
 assert case['unnormalized_weighted_boundary_h_norm_squared']==4*m;checks+=1
 assert case['observed_derivative_coefficients']==({'1680':-1}if m==1 else{'1680':-1,'1689':-1});checks+=1
 for rr in case['rows']:
  e=F(rr['epsilon']);r=1/(1+e);nz=(600-m+m*r*r)/600;dot=(600-m+m*r)/600;ang=1-dot*dot/nz
  assert ang==F(rr['new_dark_line_sine_squared'])==m*(600-m)*e*e/(600*((600-m)*(1+e)**2+m));checks+=1
  al,au=map(F,rr['new_dark_line_sine_bracket']);assert al*al<=ang<(al+grid)**2;checks+=1
  assert (au-grid)**2<ang<=au*au;checks+=1
  lo,hi=F(rr['finite_signal_magnitude_lower']),F(rr['finite_signal_magnitude_upper']);lo2=(15*abs(e)/1024)**2/600;hi2=(17*abs(e)/1024)**2/600
  assert lo*lo<=lo2<(lo+grid)**2;checks+=1
  assert (hi-grid)**2<hi2<=hi*hi;checks+=1
  assert 2*F(rr['conditional_disjoint_scalar_error_sufficient_upper'])==lo;checks+=1
  assert rr['sample_time']=='1/64'and rr['named_face_global_index']==1680;checks+=1
  assert 0<abs(e)<=F(1,2);checks+=1
  # The reported fine decimal displays also lie outside the sharper certified remainder envelope.
  dl,du=map(F,rr['finite_signal_display_interval']);sharp_rel=F(1183,24576)
  assert dl>0 and dl*dl<((1-sharp_rel)*abs(e)/64)**2/600;checks+=1
  assert du*du>((1+sharp_rel)*abs(e)/64)**2/600;checks+=1
  rows.append({'selected_tetrahedra':m,'epsilon':str(e),'angle_fraction_matches_independent_formula':True,'160bit_square_root_endpoints_checked':True,'half_lower_error_budget_checked':True,'display_interval_covered_by_sharper_remainder_bound':True})
result={'status':'PASS_ROOT_EIGHT_LOCAL_WEIGHT_CASES_AND_ROUNDING','checks':checks,'root_compute_sha256':hashlib.sha256((B/'c25_compute.py').read_bytes()).hexdigest(),'root_result_sha256':hashlib.sha256(file.read_bytes()).hexdigest(),'independent_source_checks_sha256':hashlib.sha256((P/'SOURCE_CHECKS.json').read_bytes()).hexdigest(),'independent_orbit_checks_sha256':hashlib.sha256((P/'ORBIT_CHECKS.json').read_bytes()).hexdigest(),'rows':rows,'scope':{'metric_and_counterexample_formulas_reviewed':True,'new_full_weighted_rank_claim':False,'old_native_rank_rerun':False,'hypothesis_error_budget_requires_independent_total_error_evidence':True,'new_gate_or_acquisition_admission':False,'physical_promotion':0,'external_promotion_review':'PENDING'}}
(P/'ROOT_COMPARISON.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':result['status'],'checks':checks,'cases':len(rows)}))
