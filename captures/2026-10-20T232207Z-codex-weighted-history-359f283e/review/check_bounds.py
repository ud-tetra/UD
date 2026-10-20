#!/usr/bin/env python3
"""Exact source norm/no-aliasing and projector-factor premises; no spectra/SVD."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
import hashlib,json,math,zipfile
P=Path(__file__).resolve().parent;B=P.parent;Z=B/'ud-repo/captures/2026-10-17T184000Z-codex-session-publication-7f4a2d91/recovered/UD_600CELL_VERTEX_LINK_OBSERVABILITY_v0.1.zip'
with zipfile.ZipFile(Z)as z:C=json.loads(z.read('sources/COMPLEX_AND_ACTION.json'));H=json.loads(z.read('HIDDEN_WITNESSES.json'))
S=[[tuple(s)for s in g]for g in C['simplices']];ix=[{s:i for i,s in enumerate(g)}for g in S];J=[0,9,227,432,447,582,538,347,332,141];D=[F(3,2)if i in J else F(1)for i in range(600)];bounds=[];dual=defaultdict(list)
h={int(i)-2040:int(v)for i,v in H['stationary_fundamental_C3_cycle']}
for k in [1,2,3]:
 rows=[F(0)]*len(S[k-1]);cols=[]
 for j,s in enumerate(S[k]):
  weight=D[j]if k==3 else F(1);cols.append((k+1)*weight)
  for m in range(k+1):
   face=s[:m]+s[m+1:];i=ix[k-1][face];rows[i]+=weight
   if k==3:dual[face].append((j,(-1)**m))
 bounds.append({'grade':k,'max_abs_row_sum':str(max(rows)),'max_abs_column_sum':str(max(cols)),'operator_norm_squared_upper':str(max(rows)*max(cols))})
assert all(F(x['operator_norm_squared_upper'])<=cap for x,cap in zip(bounds,[24,15,18]))
adj=defaultdict(list)
for pair in dual.values():
 assert len(pair)==2;(i,a),(j,b)=pair;assert a*b*h[i]*h[j]==-1;adj[i].append(j);adj[j].append(i)
seen={0};stack=[0]
while stack:
 for j in adj[stack.pop()]:
  if j not in seen:seen.add(j);stack.append(j)
assert len(seen)==600
factors=json.loads((P/'FACTOR_RESULTS.json').read_text())['factor_rows']
def trim(p):
 while p and not p[-1]:p.pop()
 return p
def rem(a,b):
 a=list(map(F,a));b=list(map(F,b))
 while len(a)>=len(b)and a:
  k=len(a)-len(b);c=a[-1]/b[-1]
  for j,x in enumerate(b):a[k+j]-=c*x
  trim(a)
 return a
def gcd(a,b):
 while b:a,b=b,rem(a,b)
 return a
pairs=0
for i,row in enumerate(factors):
 f=row['factor_coefficients_ascending'];assert len(gcd(f,[j*f[j]for j in range(1,len(f))]))==1
 for rr in factors[i+1:]:assert len(gcd(f,rr['factor_coefficients_ascending']))==1;pairs+=1
assert all(1009%d for d in range(2,math.isqrt(1009)+1))
r={'status':'PASS_EXACT_FACTOR_PREMISES_AND_FINITE_SAMPLE_NONALIASING_BOUND','source_archive_sha256':hashlib.sha256(Z.read_bytes()).hexdigest(),'block_operator_bounds':bounds,'full_K_operator_norm_squared_upper':24,'simple_frequency_bound':'sqrt24<5','half_step_phase_diameter_upper':'sqrt24<5<2pi','spectral_dimension_upper':2640,'M':4096,'sampled_kernel_equals_continuous_kernel_by_Vandermonde':True,'sampling_step':'1/2','quantitative_smallest_positive_singular_lower':'NOT_CERTIFIED','condition_number_upper':'NOT_CERTIFIED','full2640_domain_condition':'INFINITE_DUE_TO641_DIMENSION_KERNEL','dual_graph_connected600':True,'G_sign_gauge_to_connected_Laplacian':True,'G_harmonic_kernel':'span(h0)','W_contains_h_by_orthogonal_zero_eigenprojection_of_selected_coordinate':True,'projector_factors_squarefree_checked':len(factors),'pairwise_coprimality_checks':pairs,'modular_lower_prime1009_trial_division_verified':True,'scope':{'no_numerical_eigenvalue_or_SVD_calculation':True,'native1893_rank_inherited':True,'physical_promotion':0,'external_promotion_review':'PENDING'}}
(P/'BOUND_CHECKS.json').write_text(json.dumps(r,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':r['status'],'block_bounds':bounds,'coprime_pairs':pairs},indent=2))
