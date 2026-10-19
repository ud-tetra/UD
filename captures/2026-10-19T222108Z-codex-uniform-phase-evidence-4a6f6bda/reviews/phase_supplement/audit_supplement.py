"""Independent retained-quality, operator identity, and lattice-lineage audit."""
import ast,hashlib,io,itertools,json
from pathlib import Path
from fractions import Fraction as Q
from zipfile import ZipFile
import numpy as np
from flint import arb,fmpq,ctx
ctx.prec=512
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent;REPO=ROOT/'ud-repo';PROD=ROOT/'phase-uniform-20261019'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def a(x):
 if isinstance(x,(list,tuple)):x=Q(int(x[0]),int(x[1]))
 x=Q(x);return arb(fmpq(x.numerator,x.denominator))
def main():
 f=json.loads((HERE/'FREEZE.json').read_text())
 for rel,h in f['files'].items():assert sha(ROOT/rel)==h,rel
 def generate(source):
  tree=ast.parse(source.read_text());fun=next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='sketch')
  namespace=dict(np=np,json=json,P=PROD);exec(compile(ast.Module(body=[fun],type_ignores=[]),str(source),'exec'),namespace)
  return namespace['sketch']()
 old=REPO/'captures/2026-10-19T132221Z-codex-rounding-replay-82e4a9b7'
 freeze=json.loads((old/'FREEZE.json').read_text());assert sha(old/'sketch.py')==freeze['code_sha256']['sketch.py']
 assert sha(PROD/'inputs/NULL_VECTOR.json')==freeze['code_sha256']['inputs/NULL_VECTOR.json']
 A0=generate(old/'sketch.py');A1=generate(REPO/'captures/2026-10-19T215410Z-codex-phase-run-calibration-43cadbae/phase/estimator.py')
 assert A0.shape==A1.shape==(2294,321) and np.array_equal(A0,A1)
 # A third construction independently matches the source matrices.
 middle=np.zeros(2294,dtype=np.int64);v=json.loads((PROD/'inputs/NULL_VECTOR.json').read_text())['vector'];middle[:len(v)]=v
 A2=np.hstack([2*np.random.default_rng(172026).choice([-1.,1.],(2294,160)).astype(np.int64),middle[:,None],2*np.random.default_rng(184052).choice([-1.,1.],(2294,160)).astype(np.int64)])
 assert np.array_equal(A0,A2)
 archive=old/'WITNESS_03.zip';member='results/legacy_gemm/SVD_META.npz'
 base=REPO/'captures/2026-10-19T134625Z-codex-uniform-output-73b6e18a/admission'
 fc=json.loads((base/'inputs/ACTUAL_SVD.json').read_text());ad=json.loads((base/'ACTUAL_ADMISSION.json').read_text());af=json.loads((base/'FREEZE.json').read_text())
 assert sha(base/'inputs/ACTUAL_SVD.json')==af['input_sha256']['ACTUAL_SVD.json']
 with ZipFile(archive) as z:data=z.read(member)
 assert hashlib.sha256(data).hexdigest()==af['actual_arrays_sha256'][member]==ad['bindings'][member]
 with np.load(io.BytesIO(data),allow_pickle=False) as z:s=z['singular']
 assert s.shape==(321,) and np.all(np.isfinite(s)) and np.all(s[:-1]>=s[1:]) and np.all(s>=0) and s[208]>0
 eL=a(fc['eta_left_upper']);eR=a(fc['eta_right_upper']);smax=a(float(s[0]).as_integer_ratio());s210=a(float(s[209]).as_integer_ratio())
 # Different square-root form for the polar correction, no producer import.
 pL=1-(1-eL).sqrt();pR=1-(1-eR).sqrt()
 tail=s210*((1+eL)*(1+eR)).sqrt();polar=smax*(pL*(1+eR).sqrt()+pR)
 total=a(fc['projection_error_upper'])+a(fc['reconstruction_residual_upper'])+tail+polar
 assert total < a([1,1<<41])
 sf=json.loads((PROD/'SUPPLEMENT_FREEZE_v2.json').read_text())
 for rel,h in sf['files'].items():assert sha(PROD/rel)==h
 for row in sf['repository_sources']:assert sha(REPO/row['path'])==row['sha256']
 current=json.loads((ROOT/'phase-uniform-supplement-v2-primary-20261019/SUPPLEMENT_CERTIFICATE.json').read_text())
 assert abs(total-a(current['retained_operator_error_upper']))<a([1,1<<170])
 assert all(current['conditional_quality_gates'].values()) and current['record_membership_scope'].startswith('Inherited complete raw replay of oneq/vector cyclicunit')
 replay=json.loads((old/'RAW_PROJECTION_REPLAY.json').read_text())
 assert replay['raw_sha256']==freeze['record_sha256']==current['record_sha256']
 assert replay['vector_integer_squared_error_max']==1 and replay['readings_checked']==18790154
 assert replay['baseline_sha256']==current['original_baseline_sha256']=='25a0888972c8fb961774ef69430070e07e1cf6bd02ca05fd1bb0a5552c6e9f59'
 assert current['raw_record_noise_relative_original_baseline_upper']==[1,1<<48]
 bad_total=total+2*s210;assert bad_total>a([1,1<<41])
 lattice=json.loads((ROOT/'phase-lattice-corollary-20261019/LATTICE_COROLLARY.json').read_text())
 assert lattice['primary_certificate_sha256']==sha(ROOT/'phase-uniform-primary-20261019/CERTIFICATE.json')
 # Independent support/sign enumeration; not a full-record campaign.
 patterns={((),())}
 for size in [1,2]:
  patterns.update((positions,signs) for positions in itertools.combinations(range(62),size) for signs in itertools.product([-1,1],repeat=size))
 assert len(patterns)==lattice['patterns_per_62_vector']==7689
 v1=json.loads((ROOT/'phase-uniform-supplement-primary-20261019/SUPPLEMENT_CERTIFICATE.json').read_text());assert v1['raw_record_noise_relative_original_baseline']==[0,1]
 result=dict(status='PASS_CORRECTED_CYCLIC_TUPLE_AND_SAME_OPERATOR_SUPPLEMENT',retained_error_upper_readable=float(total.upper()),conditional_retained_cap=2.0**-41,source_matrices_exactly_equal=True,original_sketch_source_sha256=sha(old/'sketch.py'),same_operator_shape=[2294,321],operator_scale_divisor=128,record_is_nonzero_one_quantum_cyclic_not_zero_noise_nominal=True,record_sha256=current['record_sha256'],original_baseline_sha256=current['original_baseline_sha256'],inherited_raw_receipt_only_not_reread=True,archived_full_factor_proof_inherited_not_rerun=True,tail_inflation_control='REFUSED',lattice_patterns=len(patterns),v1_zero_noise_provenance_error_preserved=True,corrected_v2_certificate_sha256=sha(ROOT/'phase-uniform-supplement-v2-primary-20261019/SUPPLEMENT_CERTIFICATE.json'),external_review='PENDING',physical_promotion=0,new_fits=0)
 (HERE/'REVIEW_RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
if __name__=='__main__':main()
