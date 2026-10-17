#!/usr/bin/env python3
"""Exact full-size record perturbations, using certified base bounds and Weyl inequalities."""
import argparse,json,hashlib,shutil,time
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from flint import arb,ctx,fmpq
from proof_math import up,down
ctx.prec=512
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def run(base_path,certificate_path,contract_path,destination):
 t=time.monotonic();out=Path(destination);out.mkdir(exist_ok=False,parents=True);base=json.loads(Path(certificate_path).read_text());contract=json.loads(Path(contract_path).read_text());fmt=contract['data_format'];shape=tuple(fmt['shape']);b=np.memmap(base_path,dtype=fmt['dtype'],mode='r',shape=shape)
 assert sha(base_path)==base['input_sha256']['record'] and base['status']=='CERTIFIED_NUMERIC_RECORD_SIGNATURE'
 lo,hi,tail=[F(*base[k]) for k in ['sigma_r_lower','sigma_1_upper','projection_tail_frobenius_upper']];T=F(*base['selection_threshold']);M=4096;r=base['target_count'];results=[]
 for label,raw_delta in [('bounded_vector_impulse',2**28),('strong_rank_breach_impulse',2**48)]:
  path=out/(label+'.i64le');shutil.copyfile(base_path,path);z=np.memmap(path,dtype=fmt['dtype'],mode='r+',shape=shape);z[0,M-1,0]+=raw_delta;z.flush();del z;z=np.memmap(path,dtype=fmt['dtype'],mode='r',shape=shape)
  total=0;changes=0;where=[]
  for k in range(8191):
   d=z[:,k,:].astype(object)-b[:,k,:].astype(object);nz=np.nonzero(d)
   if len(nz[0]):
    changes+=len(nz[0]);where.extend([[int(a),k,int(c),int(d[a,c])] for a,c in zip(*nz)])
    total+=min(k+1,8191-k,M)*sum(int(v)**2 for v in d.flat)
  assert changes==1 and where==[[0,M-1,0,raw_delta]]
  # Central-time impulse has M disjoint anti-diagonal entries: singular values amp/M,
  # each repeated M times. Its Frobenius norm is amp/sqrt(M).
  amplitude=F(raw_delta,2**48);delta=amplitude/64;assert F(total,M*M*2**96)==delta**2
  nl,nh,nt=lo-delta,hi+delta,tail+delta;accept=nl>T and nt<T and nh/nl<2029
  row={'control':label,'recipe':{'base_sha256':base['input_sha256']['record'],'coordinate':[0,M-1,0],'raw_int64_increment':raw_delta},'modified_record_sha256':sha(path),'changed_entries_verified':1,'hankel_difference_frobenius':[delta.numerator,delta.denominator],'hankel_difference_singular_value':[amplitude.numerator,amplitude.denominator*M],'difference_rank':M,'numeric_signature_certified':bool(accept),'sigma_r_lower':[nl.numerator,nl.denominator],'sigma_1_upper':[nh.numerator,nh.denominator],'tail_upper':[nt.numerator,nt.denominator],'condition_upper':[ (nh/nl).numerator,(nh/nl).denominator] if nl>0 else None}
  if label.startswith('strong'):
   # rank-r perturbation can erase at most r of the M flat singular values.
   lower=amplitude/M-tail;assert M-r>r and lower>T and not accept
   row.update(guaranteed_count_above_threshold_at_least=M-r,sigma_r_plus1_lower=[lower.numerator,lower.denominator],actual_signature_breach_proved=True,status='CERTIFIED_FROZEN_RANK_BREACH')
  else:
   assert accept;row.update(status='CERTIFIED_NUMERIC_RECORD_SIGNATURE',vector_impulse_amplitude=[amplitude.numerator,amplitude.denominator])
  results.append(row)
 report={'status':'PASS','scope':'Full-size encoded-record perturbation certificates from base rank-r approximation; proposer not rerun; no metrology or hidden-dynamics claim.','physical_promotion':0,'independent_review':'pending','exact_full_record_difference_scans':2,'controls':results,'seconds':time.monotonic()-t}
 (out/'CONTROL_CERTIFICATES.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2));return report
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('base');p.add_argument('certificate');p.add_argument('contract');p.add_argument('output');a=p.parse_args();run(a.base,a.certificate,a.contract,a.output)
