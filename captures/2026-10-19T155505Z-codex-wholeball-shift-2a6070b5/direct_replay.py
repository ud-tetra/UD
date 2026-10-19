"""Portable exact-data replay of the separately frozen same-team direct-Gram check."""
import sys
sys.dont_write_bytecode=True
import json,argparse
from fractions import Fraction as F
from pathlib import Path
import numpy as np
from flint import fmpz_mat
from bounds import P,sha
from numeric_math import encode
def verify(evidence):
 f=json.loads((P/'DIRECT_REPLAY_FREEZE.json').read_text());assert sha(__file__)==f['code_sha256'] and sha(P/'DIRECT_GRAM_CERTIFICATE.json')==f['certificate_sha256']
 cert=json.loads((P/'DIRECT_GRAM_CERTIFICATE.json').read_text());d=evidence/'results/directed_period4/results/integer_projection'
 for name,h in cert['input_sha256_before_after_equal'].items():
  if Path(name).name in ('FACTOR_0.npz','FACTOR_1.npz','FACTOR_2.npz','PHASE_META.npz'):assert sha(d/Path(name).name)==h
 U=np.vstack([np.load(d/f'FACTOR_{k}.npz',allow_pickle=False)['left'] for k in range(3)])[:,:209]
 with np.load(d/'PHASE_META.npz',allow_pickle=False) as z:T=z['shift']
 un,bu=encode(U);tn,bt=encode(T);A=fmpz_mat(un[:-2].tolist());B=fmpz_mat(un[2:].tolist());tm=fmpz_mat(tn.tolist());G=A.transpose()*A;gn=np.array(G.tolist(),object);D=gn-np.eye(209,dtype=object)*(1<<(2*bu));eta2=F(sum(int(x)**2 for x in D.flat),1<<(4*bu))
 pair=lambda p:F(*map(int,p))
 assert eta2==pair(cert['actual_deleted_basis_gram_defect_squared_exact'])
 ell=pair(cert['deleted_basis_sigma_min_squared_lower_exact']);assert 0<ell<=1 and (1-ell)**2>=eta2
 E=B*(1<<bt)-A*tm;N=A.transpose()*E
 s2=F(sum(int(v)**2 for row in E.tolist() for v in row),1<<(2*bu+2*bt));n2=F(sum(int(v)**2 for row in N.tolist() for v in row),1<<(4*bu+2*bt))
 assert s2==pair(cert['direct_shift_residual_squared_exact']) and n2==pair(cert['direct_normal_residual_squared_exact'])
 lower=s2-n2/ell;assert lower==pair(cert['LS_minimum_residual_squared_lower_before_max0_exact']) and lower>F(1,1<<68)
 result={'status':'PASS_DATA_ONLY_FIXED_BASIS_OBSTRUCTION_REPLAY','strict_rational_lower_exceeds_v1_gate_squared':True,'source_frame_SVD_quality_or_noise_model_needed':False,'new_SVD_or_fits':0,'external_review':'PENDING','physical_promotion':0};print(json.dumps(result),flush=True);return result
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--evidence',type=Path,required=True);a=p.parse_args();verify(a.evidence.resolve())
