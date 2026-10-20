#!/usr/bin/env python3
"""Independent comparison of root's exact moments and 160-bit enclosures."""
from fractions import Fraction as F
import hashlib,json
from pathlib import Path
P=Path(__file__).resolve().parent;B=P.parent;root=B/'c24_math/RESULT.json';mine=P/'EXACT_RESULTS.json'
a=json.loads(root.read_text());b=json.loads(mine.read_text());checks=0;rows=[]
for rr,mm in zip(a['rows'],b['rows']):
 assert F(rr['epsilon'])==F(*map(int,mm['epsilon']));checks+=1
 for rk,mk in [('centered_time_variance','central_variance'),('centered_fourth_moment','central_fourth_moment')]:assert F(rr[rk])==F(*map(int,b[mk]));checks+=1
 for rk,mk in [('mean_centered_sine_squared_lower','centered_S_lower'),('mean_centered_sine_squared_upper','centered_S_upper')]:assert F(rr[rk])==F(*map(int,mm[mk]));checks+=1
 L=F(*map(int,mm['centered_S_lower']));U=F(*map(int,mm['centered_S_upper']));grid=F(1,2**160)
 lo=F(rr['harmonic_plane_weak_singular_lower']);hi=F(rr['harmonic_plane_weak_singular_upper']);k=F(rr['full_map_positive_condition_lower'])
 assert lo**2<=L/10<(lo+grid)**2;checks+=1
 assert (hi-grid)**2<U/10<=hi**2;checks+=1
 assert k**2<=(1-U)/U<(k+grid)**2;checks+=1
 assert F(rr['full_map_smallest_positive_singular_upper'])==hi;checks+=1
 rows.append({'epsilon':rr['epsilon'],'raw_moments_and_S_bounds_equal':True,'160bit_lower_floor_verified':True,'160bit_upper_ceiling_minimal_verified':True,'160bit_condition_floor_verified':True})
d=a['derived'];expected={'perturbed_history_rank':1894,'perturbed_hidden_dimension':746,'nonaliased_sampling_sufficient_M':106,'m0_rank':256,'m0_hidden':8,'sum_isolated_sector_ranks':2524,'individually_dark_dimension':116,'mixed_dark_quotient_dimension':630,'unrestricted_hidden_skew_parameter_dimension':278631}
for key,v in expected.items():assert d[key]==v;checks+=1
assert a['native_identities_newly_checked']['Ru_norm_squared']=='1/10';checks+=1
result={'status':'PASS_ROOT_EXACT_MOMENTS_AND_ROUNDING_COMPARISON','check_count':checks,'root_result_sha256':hashlib.sha256(root.read_bytes()).hexdigest(),'root_compute_source_sha256':hashlib.sha256((B/'c24_compute.py').read_bytes()).hexdigest(),'independent_result_sha256':hashlib.sha256(mine.read_bytes()).hexdigest(),'rows':rows,'scope':'Moment rational equality and directed square-root endpoint review; root full native rank and sector premises remain inherited, not rerun.','physical_promotion':0,'external_promotion_review':'PENDING'}
(P/'ROOT_COMPARISON.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':result['status'],'check_count':checks}))
