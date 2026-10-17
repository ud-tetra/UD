"""Exact fixed-sketch blindness and impulse-Hankel rank lower bound.

The baseline rank-1893 approximation/tail certificate is inherited explicitly.
This script does not execute the spectral constructor or prove apparatus admission.
"""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,math
import numpy as np
from flint import fmpz_mat
P=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def pair(x):return [x.numerator,x.denominator]
spec=json.loads((P/'CAMPAIGN_FREEZE.json').read_text());witness=json.loads((P/'NULL_VECTOR.json').read_text())
assert sha(P/'NULL_VECTOR.json')==spec['null_vector_sha256']
v=np.zeros(2294,np.int64);v[:320]=witness['vector']
W=np.random.default_rng(172026).choice([-1.,1.],size=(2294,160)).astype(np.int64)
products=[sum(int(v[i])*int(W[i,j]) for i in range(2294)) for j in range(160)]
assert products==[0]*160 and np.count_nonzero(v)==250
sketch_minor=int(fmpz_mat(W[:160].tolist()).det());assert sketch_minor!=0
B=v.reshape(62,37);active=[i for i in range(62) if np.any(B[i])];assert active==list(range(8))
G=B[:8]@B[:8].T;test=G-4*np.eye(8,dtype=np.int64)
minors=[int(fmpz_mat(test[:k,:k].tolist()).det()) for k in range(1,9)]
assert all(x>0 for x in minors);rank=fmpz_mat(B.tolist()).rank();assert rank==8
# Sylvester positivity proves B B^T > 4 I on its eight nonzero rows.
assert sum(int(x)**2 for x in v)==16228
bounded=spec['cases'][0]['scale'];assert bounded==spec['cases'][1]['scale']
coordinate=bounded*max(abs(int(x)) for x in v)
vector2=max(sum((bounded*int(B[c,a]))**2 for c in range(62)) for a in range(37))
assert coordinate<2**25 and vector2<2**56
baseline=json.loads((P/'inputs/BASELINE_CERTIFICATE.json').read_text())
assert baseline['status']=='CERTIFIED_NUMERIC_RECORD_SIGNATURE' and baseline['target_count']==1893
assert baseline['input_sha256']['record']==spec['baseline_sha256']
assert baseline['input_sha256']['contract']==sha(P/'inputs/FROZEN_CONTRACT.json')
tau=F(*baseline['projection_tail_frobenius_upper']);ell=F(2*bounded,4096*2**48);gap=ell-tau
assert gap>0
threshold=F(*baseline['selection_threshold']);assert ell<threshold
out={'status':'EXACT_FIXED_SKETCH_BLIND_FAMILY_AND_IMPULSE_RANK_BOUND','physical_promotion':0,'independent_review':'not established','source_baseline_certificate_sha256':sha(P/'inputs/BASELINE_CERTIFICATE.json'),'baseline_tail_is_inherited_not_rerun':True,'null_witness_sha256':sha(P/'NULL_VECTOR.json'),'freeze_sha256':sha(P/'CAMPAIGN_FREEZE.json'),'sketch_shape':[2294,160],'sketch_rank':160,'sketch_kernel_dimension':2134,'first_160_row_minor_determinant':sketch_minor,'exact_products_vT_W':products,'null_support':250,'null_max_coefficient':23,'null_squared_norm':16228,'spatial_active_channels':active,'spatial_rank':rank,'gram':G.tolist(),'sylvester_minors_G_minus_4I':minors,'strict_spatial_nonzero_singular_lower':2,'bounded_integer_scale':bounded,'max_coordinate_integer_error':coordinate,'max_vector_integer_squared_error':vector2,'coordinate_ceiling_met':coordinate<=2**25,'global_vector_ceiling_met':vector2<=2**56,'full_acquisition_contract_admission':False,'uniform_blindness':'For any temporal sequence f and scale s, E=(s/2^48) f v^T obeys E(W/64)=0 exactly. Applies to the mathematical sketch; floating evaluations may differ by roundoff.','impulse_hankel_factorization':'H(E)=(s/(4096*2^48)) J_4096 tensor B; row index (i,c), column index (j,a).','alternating_hankel_factorization':'H(E)=(s/2^48) (u u^T/4096) tensor B, u_i=(-1)^i.','impulse_perturbation_rank':4096*rank,'impulse_nonzero_singular_lower':pair(ell),'baseline_rank_approximation':1893,'baseline_tail_upper':pair(tau),'noisy_rank_lower':4096*rank-1893,'noisy_positive_singular_lower':pair(gap),'proof':'sigma_(rankE-r)(E+A_r)>=sigma_rankE(E) for rank(A_r)<=r; Weyl subtraction of inherited baseline tail tau yields the positive gap. No baseline exact-rank claim.','frozen_threshold':pair(threshold),'rank_is_not_threshold_count':True,'strong_control_scope':'Out of budget. A verifier HOLD is not by itself proof of a true signature violation or its physical cause.','readable':{'max_coordinate_error':float(F(coordinate,2**48)),'max_vector_error_upper':math.sqrt(vector2)/2**48,'impulse_nonzero_singular_lower':float(ell),'baseline_tail_upper':float(tau),'noisy_positive_singular_lower':float(gap)}}
(P/'EXACT_BLIND_FAMILY_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['status','spatial_rank','impulse_perturbation_rank','noisy_rank_lower','readable']},indent=2))
