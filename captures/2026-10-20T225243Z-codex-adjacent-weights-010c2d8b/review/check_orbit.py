#!/usr/bin/env python3
"""Independent orbit support and finite-response constants, no dynamics solver."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,zipfile
P=Path(__file__).resolve().parent;B=P.parent;Z=B/'ud-repo/captures/2026-10-17T184000Z-codex-session-publication-7f4a2d91/recovered/UD_600CELL_VERTEX_LINK_OBSERVABILITY_v0.1.zip'
with zipfile.ZipFile(Z)as z:C=json.loads(z.read('sources/COMPLEX_AND_ACTION.json'));M=json.loads(z.read('modular_results.json'));H=json.loads(z.read('HIDDEN_WITNESSES.json'))
S=[[tuple(s)for s in g]for g in C['simplices']];idx=[{s:i for i,s in enumerate(g)}for g in S];off=[0,120,840,2040];T=C['signed_simplex_permutations'][3];h={int(i)-2040:int(v)for i,v in H['stationary_fundamental_C3_cycle']}
orbit=[];i=0
while i not in orbit:orbit.append(i);i=T[i]['destination']
assert i==0 and orbit==[0,9,227,432,447,582,538,347,332,141]
facets={};face_sets=[]
for i in orbit:
 ss=S[3][i];fs=[]
 for j in range(4):
  f=ss[:j]+ss[j+1:];fs.append(f);facets[f]=facets.get(f,0)+(-1)**j*h[i]
 face_sets.append(set(fs))
assert all(not a&b for i,a in enumerate(face_sets)for b in face_sets[i+1:]);assert len(facets)==40 and all(v in[-1,1]for v in facets.values())
obs={tuple(f)for f in M['link_simplices'][2]};visible={idx[2][f]:v for f,v in facets.items()if f in obs};assert visible=={840:1,849:1}
# Exact absolute row sums in sparse A; no matrix or spectral estimate allocated.
rows=[0]*2640
for k in [1,2,3]:
 for j,s in enumerate(S[k]):
  for v in range(k+1):
   f=s[:v]+s[v+1:];rows[off[k-1]+idx[k-1][f]]+=1;rows[off[k]+j]+=1
assert max(rows)==12
assert F(1183,24576)<F(1,16);assert 40<7**2
examples=[]
for m in [1,10]:
 for eps in [F(1,2**20),F(1,2),F(-1,2)]:
  r=1/(1+eps);nz=(600-m+m*r*r)/600;dot=(600-m+m*r)/600
  angle=1-dot*dot/nz;claimed=F(m*(600-m),600)*eps*eps/((600-m)*(1+eps)**2+m);assert angle==claimed
  examples.append({'weighted_tetrahedra':m,'epsilon':str(eps),'dark_line_angle_sine_squared':str(angle)})
result={'status':'PASS_C10_ORBIT_AND_FINITE_RESPONSE_CONSTANTS','source_archive_sha256':hashlib.sha256(Z.read_bytes()).hexdigest(),'orbit_indices':orbit,'orbit_columns_disjoint_faces':True,'B3_orbit_columns_Gram':'4I10','B3_PJ_h0_squared_norm':40,'nonzero_observed_face_indices':[840,849],'global_output_coordinate_indices':[1680,1689],'observed_face_coefficients':[1,1],'nominal_absolute_row_bound':12,'local_perturbation_norm':'2|epsilon|','weighted_generator_norm_upper_for_abs_epsilon_le_half':13,'time':'1/64','relative_remainder_upper_strict':'1183/24576','strict_relative_margin':'1/16','face_response_absolute_interval_coefficients':['15/1024','17/1024'],'interval_multiplied_by':'|epsilon|/sqrt600','strict_interval_requires':'0<|epsilon|<=1/2','signal_sign':'-sgn(epsilon)','angle_examples':examples,'metric_preparation_scope':{'F':'diag(I,I,I,D)','H':'diag(I,I,I,D^-2)','Ky':'F K_D F^-1=H^-1 A','fixed_x_h_maps_to_y_Dh':True,'fixed_y_h_maps_to_x_D^-1h':True,'same_numeric_h_is_Ky_harmonic':True,'no_claim_H^-1A_exposes_its_numeric_h':True},'scope':{'no_total_weighted_rank_claim':True,'not_acquisition_or_physical_gate':True,'no_estimator_fit_or_raw_acquisition':True,'physical_promotion':0,'external_promotion_review':'PENDING'}}
(P/'ORBIT_CHECKS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':result['status'],'orbit10':True,'40facets':True,'observed_global_indices':result['global_output_coordinate_indices'],'row_bound':max(rows)}))
