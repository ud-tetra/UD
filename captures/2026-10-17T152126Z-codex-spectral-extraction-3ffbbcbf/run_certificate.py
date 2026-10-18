"""Exact proof for a supplied numeric history and proposed dense right signal basis.

This is a post-processing certificate, not a candidate-vector optimizer or a metrology receipt.
Requires substantial exact arithmetic and disk; full real-data runtime is unbenchmarked.
"""
from pathlib import Path
import argparse,hashlib,json
import numpy as np
from fractions import Fraction as F
from hankel_exact import HankelRecord,disk_cores,file_sha
from spectral_certificate import certify

def run(data_path,candidate_path,workdir,contract_path):
 contract=json.loads(Path(contract_path).read_text());fmt=contract['data_format'];rule=contract['spectral_rule']
 expected=json.loads((Path(__file__).resolve().parent/'sources'/'PARENT_FREEZE_CERTIFICATE.json').read_text())['protocol_sha256']
 if file_sha(contract_path)!=expected:raise ValueError('Frozen protocol hash mismatch; no gate substitution')
 data_hash=file_sha(data_path);candidate_hash=file_sha(candidate_path)
 if Path(data_path).stat().st_size!=fmt['bytes']:raise ValueError('Incomplete normalized record')
 Y=np.memmap(data_path,dtype=fmt['dtype'],mode='r',shape=tuple(fmt['shape']))
 if fmt['scale'][0]!=1:raise ValueError('Requires fixed numerator/denominator format')
 H=HankelRecord(Y,fmt['scale'][1]);V=np.load(candidate_path,mmap_mode='r',allow_pickle=False)
 if V.shape!=(H.cols,rule['target_count']):raise ValueError('Candidate shape differs from frozen target')
 work=Path(workdir);work.mkdir(parents=True,exist_ok=True)
 cores=disk_cores(H,V,work/'exact_C_columns.i128le',2**60)
 proof=certify(H.energy(),*cores,rule['target_count'],F(*rule['selection_threshold']),rule['retained_condition_number_strict_upper'])
 if file_sha(data_path)!=data_hash or file_sha(candidate_path)!=candidate_hash:raise RuntimeError('Inputs changed during verification; no certificate')
 proof.update(protocol_sha256=expected,normalized_data_sha256=data_hash,candidate_sha256=candidate_hash,
  candidate_denominator=2**60,method='Exact integer Hankel actions + exact streamed Gram products + direct spectral enclosures',
  empirical_provenance_validated=False,apparatus_execution_claimed=False,inherited_modal_hypotheses_used_for_numeric_spectrum=False)
 target=work/'SPECTRAL_PROOF.json'
 with target.open('x') as stream:json.dump(proof,stream,indent=2);stream.write('\n')
 if proof['status']=='CERTIFIED_NUMERIC_RECORD_SIGNATURE':
  receipt={'sigma1':proof['sigma_1_interval'],'sigma1893':proof['sigma_r_interval'],
   'sigma1894':proof['sigma_r_plus1_interval'],'numerical_operator_error_upper':[0,1]}
  with (work/'FROZEN_SIGNATURE_ENCLOSURES.json').open('x') as stream:json.dump(receipt,stream,indent=2);stream.write('\n')
 return proof

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('data');p.add_argument('candidate');p.add_argument('workdir')
 p.add_argument('--contract',default=str(Path(__file__).resolve().parent/'sources'/'FROZEN_CONTRACT.json'));args=p.parse_args()
 r=run(args.data,args.candidate,args.workdir,args.contract)
 print(json.dumps({k:r[k] for k in ['status','candidate_rank','count_above_threshold_certified','condition_below_declared_cap','empirical_provenance_validated']}))
