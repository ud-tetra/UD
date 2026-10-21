"""Float64 full Gram proposal, admitted only by exact dyadic residual and lift checks."""
from pathlib import Path
from fractions import Fraction
from flint import fmpz_mat
import argparse,json,gzip,hashlib,math,time
import numpy as np
from scipy.linalg import cho_factor,cho_solve
from threadpoolctl import threadpool_limits
ap=argparse.ArgumentParser();ap.add_argument('--frame',type=Path,required=True);ap.add_argument('--frame-sha256',required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=False);H=lambda b:hashlib.sha256(b).hexdigest();fb=(a.frame/'FULL_FRAME.json').read_bytes();assert H(fb)==a.frame_sha256;meta=json.loads(fb);assert meta['status']=='PASS_FULL1999_SOURCE_FRAME_CONSTRUCTION';assert meta['actual_rows_constructed_or_authenticated']==1999 and [r['column']for r in meta['rows']]==list(range(1999));assert meta['data_scale_bits']==96
G=[];z=[];start=time.monotonic()
for row in meta['rows']:
 packed=(a.frame/row['output_row_file']).read_bytes();assert H(packed)==row['output_row_sha256'];raw=gzip.decompress(packed);assert len(raw)==2640*16 and H(raw)==row['output_decoded_sha256'];G.append([int.from_bytes(raw[k:k+16],'little',signed=True)for k in range(0,len(raw),16)]);assert row['state_integer_scale_bits']==96 and row['rhs_dot_denominator_power2']==192;z.append(int(row['rhs_dot_integer']))
p=160;S=2**96;scale=2**p;denbits=192+p;gm=fmpz_mat(G);gt=gm.transpose();zcol=fmpz_mat([[v*scale]for v in z]);GF=np.array(G,dtype=np.float64)/S;zf=np.array([math.ldexp(float(v),-192)for v in z],dtype=np.float64);quant=lambda v:(lambda t:t[0]*scale//t[1])(float(v).as_integer_ratio());history=[]
with threadpool_limits(limits=8):
 gram=GF@GF.T;factor=cho_factor(gram,lower=True,check_finite=True);proposal=cho_solve(factor,zf,check_finite=True);assert np.all(np.isfinite(proposal));aa=[quant(v)for v in proposal]
 for iteration in range(9):
  al=fmpz_mat([[v]for v in aa]);L=gt*al;r=gm*L-zcol;rr=[int(r[i,0])for i in range(1999)];r2=sum(v*v for v in rr);history.append({'iteration':iteration,'residual_squared_integer':str(r2),'residual_denominator_power2':denbits,'residual_gate_pass':r2<2**(2*denbits-128)});print(json.dumps({'iteration':iteration,'exact_residual_norm_approx':math.sqrt(math.ldexp(float(r2),-2*denbits)),'gate_pass':history[-1]['residual_gate_pass']}),flush=True)
  if history[-1]['residual_gate_pass']:break
  assert iteration<8,'Frozen residual gate not met; HOLD, no certificate'
  rf=np.array([math.ldexp(float(v),-denbits)for v in rr],dtype=np.float64);correction=cho_solve(factor,rf,check_finite=True);assert np.all(np.isfinite(correction));aa=[v-quant(d)for v,d in zip(aa,correction)]
assert r2<2**(2*denbits-128)
li=[int(L[i,0])for i in range(2640)];q=[v//scale for v in li];errnum=sum((v*scale-w)**2 for v,w in zip(q,li));assert errnum<2640*scale*scale and errnum<2**(2*(96+p)-88);raw=b''.join(v.to_bytes(16,'little',signed=True)for v in q);packed=gzip.compress(raw,compresslevel=9,mtime=0);(a.out/'LIFT.i128.gz').write_bytes(packed)
coef={'coefficient_denominator_power2':p,'coefficient_integers':list(map(str,aa)),'frame_receipt_sha256':H(fb)};cb=(json.dumps(coef,indent=2,sort_keys=True)+'\n').encode();(a.out/'COEFFICIENTS.json.gz').write_bytes(gzip.compress(cb,compresslevel=9,mtime=0))
receipt={'status':'PASS_ACTUAL_FULL1999_FLOAT_PROPOSAL_EXACT_RESIDUAL_AND_FINITE_LIFT','full_frame_rows':1999,'state_dim':2640,'coefficient_denominator_power2':p,'normal_equation_residual_squared_integer':str(r2),'normal_equation_residual_denominator_power2':denbits,'normal_equation_residual_squared':str(Fraction(r2,2**(2*denbits))),'normal_equation_residual_gate':'<2^-64','finite_lift_error_squared_integer':str(errnum),'finite_lift_error_denominator_power2':96+p,'finite_lift_error_squared':str(Fraction(errnum,2**(2*(96+p)))),'finite_lift_error_gate':'<2^-44','coefficient_decoded_sha256':H(cb),'coefficient_packed_sha256':H((a.out/'COEFFICIENTS.json.gz').read_bytes()),'lift_decoded_sha256':H(raw),'lift_packed_sha256':H(packed),'frame_receipt_sha256':H(fb),'refinement_history':history,'floating_backend':'NumPy/SciPy float64 Cholesky proposal; exact FLINT integer matvec verification','scope':'One frozen synthetic data record; finite arithmetic error relative to ideal compressed nominal decoder, not physical data or state-truth accuracy','physical_input_status':'UNSUPPLIED_HOLD','physical_promotion':0,'external_promotion_review':'PENDING'};(a.out/'FULL_SOLVE.json').write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n');print('PASS full1999 actual finite solve record; physical/state-truth accuracy remainsHOLD',flush=True)
