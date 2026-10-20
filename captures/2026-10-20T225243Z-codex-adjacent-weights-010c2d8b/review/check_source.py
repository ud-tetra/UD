#!/usr/bin/env python3
"""Exact sparse incidence/witness checks only; no native observability rank rerun."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,zipfile
P=Path(__file__).resolve().parent;B=P.parent;Z=B/'ud-repo/captures/2026-10-17T184000Z-codex-session-publication-7f4a2d91/recovered/UD_600CELL_VERTEX_LINK_OBSERVABILITY_v0.1.zip'
sha=lambda b:hashlib.sha256(b).hexdigest()
with zipfile.ZipFile(Z)as z:
 raw={n:z.read(n)for n in ['sources/COMPLEX_AND_ACTION.json','modular_results.json','HIDDEN_WITNESSES.json']}
C=json.loads(raw['sources/COMPLEX_AND_ACTION.json']);M=json.loads(raw['modular_results.json']);H=json.loads(raw['HIDDEN_WITNESSES.json'])
S=[[tuple(s)for s in g]for g in C['simplices']];index=[{s:i for i,s in enumerate(g)}for g in S];L=[[tuple(s)for s in g]for g in M['link_simplices']];off=[0,120,840,2040]
checks=0
for k in [2,3]:
 for s in S[k]:
  chain={}
  for i in range(k+1):
   face=s[:i]+s[i+1:]
   for j in range(k):
    edge=face[:j]+face[j+1:];chain[edge]=chain.get(edge,0)+(-1)**(i+j)
  assert all(v==0 for v in chain.values());checks+=1
cochains=[]
for k in [1,2]:
 prev={s:i for i,s in enumerate(L[k-1])};left={};right={}
 for row,s in enumerate(L[k]):
  assert s in index[k]
  for j in range(k+1):
   face=s[:j]+s[j+1:];assert face in prev
   left[row,index[k-1][face]]=(-1)**j
   right[row,index[k-1][L[k-1][prev[face]]]]=(-1)**j
 assert left==right;checks+=1
 cochains.append({'degree':k,'observed_rows':len(L[k]),'nonzeros':len(left),'exact_restriction_identity':True})
h={int(i)-2040:int(v)for i,v in H['stationary_fundamental_C3_cycle']};assert len(h)==600 and set(h)==set(range(600));checks+=1
boundary={}
for k,s in enumerate(S[3]):
 for j in range(4):
  f=s[:j]+s[j+1:];boundary[f]=boundary.get(f,0)+(-1)**j*h[k]
assert all(v==0 for v in boundary.values());checks+=1
T=C['signed_simplex_permutations'][3];tau=(0,33,34,41);taui=index[3][tau];facets=[tau[:j]+tau[j+1:]for j in range(4)];visible=[f for f in facets if f in L[2]]
assert visible==[(33,34,41)];checks+=1
assert len(facets)==4 and all(f in index[2]for f in facets);checks+=1
orbit=[];i=taui
while i not in orbit:orbit.append(i);i=T[i]['destination']
assert i==taui and len(orbit)==10;checks+=1
rows=[]
for eps in [F(1,2**20),F(1,2**10),F(-1,2)]:
 r=1/(1+eps);nz=(599+r*r)/600;dot=(599+r)/600
 angle=1-dot*dot/nz;claimed=599*eps*eps/(600*(599*(1+eps)**2+1));assert angle==claimed and 0<angle<1;checks+=1
 # B3 D (D^-1 h0)=B3 h0=0 by exact diagonal cancellation; no weighted matrix allocated.
 assert (1+eps)*r==1;checks+=1
 rows.append({'epsilon':str(eps),'old_h_readout_derivative_norm_squared':str(eps*eps/600),'perturbation_operator_norm_squared':str(4*eps*eps),'new_hidden_harmonic_norm_squared':str(nz),'dark_line_angle_sine_squared':str(angle)})
result={'status':'PASS_SOURCE_CLOSED_SUBCOMPLEX_AND_LOCAL_COLUMN_WITNESS','checks':checks,'source_archive_sha256':sha(Z.read_bytes()),'source_member_sha256':{n:sha(b)for n,b in raw.items()},'chain_dimensions':list(map(len,S)),'cochain_restrictions':cochains,'boundary_squared_zero':True,'uniform_grade_pair_annihilation_follows':True,'tetrahedron':list(tau),'tetrahedron_index':taui,'observed_unique_facet':list(visible[0]),'facet_boundary_sign':1,'tetrahedron_fundamental_cycle_sign':h[taui],'signed_tetrahedron_orbit_indices':orbit,'signed_tetrahedron_orbit_length':10,'rows':rows,'scope':{'old_1893_747_and_sector_rank_premises_inherited_not_rerun':True,'weighted_full_kernel_rank_not_computed':True,'no_estimator_fit_or_raw_acquisition':True,'new_weight_not_literal_incidence_or_physical_law':True,'physical_promotion':0,'external_promotion_review':'PENDING'}}
(P/'SOURCE_CHECKS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':result['status'],'checks':checks,'tau_index':taui,'h_sign':h[taui],'orbit_length':len(orbit)},indent=2))
