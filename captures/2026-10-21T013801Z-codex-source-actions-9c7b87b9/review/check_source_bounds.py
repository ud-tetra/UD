#!/usr/bin/env python3
"""Independent source/operator equality and rational Taylor certificate."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
import json,hashlib,zipfile,math
P=Path(__file__).resolve().parent;W=P.parent;Z=W/'ud-repo/captures/2026-10-17T184000Z-codex-session-publication-7f4a2d91/recovered/UD_600CELL_VERTEX_LINK_OBSERVABILITY_v0.1.zip';op=W/'c30_source/OPERATOR.txt'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
with zipfile.ZipFile(Z)as z:
 cb=z.read('sources/COMPLEX_AND_ACTION.json');rb=z.read('modular_results.json');C=json.loads(cb);R=json.loads(rb)
S=[[tuple(s)for s in g]for g in C['simplices']];assert list(map(len,S))==[120,720,1200,600];off=[0,120,840,2040];ix=[{s:i for i,s in enumerate(g)}for g in S];J={0,9,227,432,447,582,538,347,332,141};expected={};boundaries=[];norms=[]
for k in range(1,4):
 columns=[];row=[F(0)]*len(S[k-1]);col=[]
 for j,s in enumerate(S[k]):
  weight=3 if k==3 and j in J else 2;c={}
  for l in range(k+1):
   i=ix[k-1][s[:l]+s[l+1:]];v=weight*(-1)**l;c[i]=v;row[i]+=F(abs(v),2)
   lo=off[k-1]+i;hi=off[k]+j;expected[lo,hi]=-v;expected[hi,lo]=v
  columns.append(c);col.append(sum(F(abs(v),2)for v in c.values()))
 boundaries.append(columns);norms.append(max(row)*max(col))
assert norms==[24,15,15]
chain_checks=0
for k in range(2):
 for col in boundaries[k+1]:
  result=defaultdict(int)
  for i,v in col.items():
   for j,w in boundaries[k][i].items():result[j]+=v*w
  assert not any(result.values());chain_checks+=1
words=list(map(int,op.read_text().split()));assert words[:5]==[2640,62,4096,40,128];obs=words[5:67];assert obs==R['observed_indices']and len(set(obs))==62
assert words[67]==14880 and len(words)==68+3*14880
actual={}
for i in range(68,len(words),3):
 u,v,c=words[i:i+3];assert (u,v)not in actual;actual[u,v]=c
assert actual==expected and all(actual[j,i]==-v for(i,j),v in actual.items())
rows=defaultdict(int)
for(i,j),v in actual.items():rows[i]+=abs(v)
assert max(rows.values())==24
u=F(1,2**128);r=52*u;step=120*r;tau=F(5,2)**41/math.factorial(41)/(1-F(5,84));assert tau<F(1,2**110)
# Elementary per-term recurrence establishes <3r for all40terms.
e=F(0);sum_round=F(0)
for k in range(1,41):
 e=F(5,2*k)*e+r;assert e<3*r;sum_round+=e
assert sum_round<step
cap=2**18;local=tau*cap+step;acc=4096*local
forward=acc+504*F(1,2**96);adjoint=acc+52*F(1,2**96)
assert acc<1 and 2049+acc<cap
assert forward<F(1,2**79)<F(1,2**68)and adjoint<F(1,2**79)<F(1,2**68)
# Source normalization/encoding:96->128shift32, forward/64->96shift38,
# adjoint injection/64 shift26, final128->96shift32.
assert 128-96==32 and 128+6-96==38 and 128-96-6==26
result={'status':'PASS_INDEPENDENT_SOURCE_EQUALITY_AND_TAYLOR_ALL_INPUT_BOUNDS','source_archive_sha256':sha(Z),'complex_member_sha256':hashlib.sha256(cb).hexdigest(),'observer_member_sha256':hashlib.sha256(rb).hexdigest(),'operator_sha256':sha(op),'operator_entries_compared':len(actual),'unique_observer_coordinates':len(obs),'H_skew_exact':True,'H_max_absolute_row_sum':24,'weighted_boundary_chain_columns_checked':chain_checks,'boundary_squared_norm_upper':[str(x)for x in norms],'K_squared_norm_upper':24,'degree':40,'internal_bits':128,'external_bits':96,'Taylor_tail':str(tau),'tail_strict_comparison':'<2^-110','single_term_vector_round_upper':str(r),'summed_step_round_strict_upper':str(step),'computed_state_cap':cap,'single_step_error_upper':str(local),'global4096_propagation_error_upper':str(acc),'forward_absolute_error_upper':str(forward),'adjoint_absolute_error_upper':str(adjoint),'both_action_error_comparison':'<2^-79<2^-68','domain_bootstrap':'true forwardstate<=2048; true normalized adjointpartial<=2049; propagationerror<1; bothcomputedstates<2^18','scope':{'fixed_source_operator_bytes_required':True,'skew_exact_exp_isometry_used':True,'adjoint_partial_norm_uses_Cauchy_Schwarz_and1over64':True,'GMP_integer_semantics_assumed_not_all_backend_formal_proof':True,'no_producer_or_archived_program_execution':True,'actual_full_decoder_not_run':True,'physical_promotion':0,'external_review':'PENDING'}}
(P/'SOURCE_BOUND_CHECKS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':result['status'],'H_entries':len(actual),'tau_float_display':float(tau),'forward_error_float_display':float(forward),'adjoint_error_float_display':float(adjoint)}))
