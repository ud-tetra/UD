"""Finite nonzero signed full-shape fixture for the independent residual auditor, not source admission."""
from pathlib import Path
from fractions import Fraction as Q
import json,gzip,hashlib,subprocess,shutil
P=Path(__file__).resolve().parent;work=P/'work_fixture';work.mkdir(exist_ok=False);frame=work/'frame';solve=work/'solve';frame.mkdir();solve.mkdir();sha=lambda b:hashlib.sha256(b).hexdigest();n=2640;r=1999;p=160;S=2**96;scale=2**p
rows=[];aa=[];z=[];L=[0]*n
for i in range(r):
 sign=1 if i%2==0 else-1;base=(i%3)-1;small=(17*i+5)%31;coef=base*2**(p-6)+small;aa.append(coef);z.append(base*2**186);L[i]=sign*S*coef
 raw=bytearray(n*16);raw[i*16:(i+1)*16]=(sign*S).to_bytes(16,'little',signed=True);raw=bytes(raw);packed=gzip.compress(raw,mtime=0);name=f'row_{i:04d}.gz';(frame/name).write_bytes(packed)
 rows.append({'column':i,'state_integer_scale_bits':96,'rhs_dot_denominator_power2':192,'rhs_dot_integer':str(z[-1]),'output_row_file':name,'output_row_sha256':sha(packed),'output_decoded_sha256':sha(raw)})
fb=(json.dumps({'rows':rows})+'\n').encode();(frame/'FULL_FRAME.json').write_bytes(fb);(work/'ROWS_CHECKS.json').write_text(json.dumps({'status':'PASS_FULL1999_ROWS_AND_TRUE_RHS','frame_or_checkpoint_prefix_sha256':sha(fb),'RHS_error_squared_upper':[0,1]}))
cb=(json.dumps({'coefficient_denominator_power2':p,'coefficient_integers':list(map(str,aa)),'frame_receipt_sha256':sha(fb)})+'\n').encode();cp=gzip.compress(cb,mtime=0);(solve/'COEFFICIENTS.json.gz').write_bytes(cp)
r2=2**384*sum(((17*i+5)%31)**2 for i in range(r));q=[x//scale for x in L];err=sum((v*scale-x)**2 for v,x in zip(q,L));raw=b''.join(x.to_bytes(16,'little',signed=True)for x in q);packed=gzip.compress(raw,mtime=0);(solve/'LIFT.i128.gz').write_bytes(packed);den=192+p
receipt={'status':'PASS_ACTUAL_FULL1999_FLOAT_PROPOSAL_EXACT_RESIDUAL_AND_FINITE_LIFT','frame_receipt_sha256':sha(fb),'coefficient_packed_sha256':sha(cp),'coefficient_decoded_sha256':sha(cb),'coefficient_denominator_power2':p,'normal_equation_residual_denominator_power2':den,'normal_equation_residual_squared_integer':str(r2),'normal_equation_residual_squared':str(Q(r2,2**(2*den))),'finite_lift_error_squared_integer':str(err),'finite_lift_error_denominator_power2':96+p,'finite_lift_error_squared':str(Q(err,2**(2*(96+p)))),'lift_decoded_sha256':sha(raw),'lift_packed_sha256':sha(packed),'refinement_history':[{'iteration':0,'residual_denominator_power2':den,'residual_squared_integer':str(r2),'residual_gate_pass':True}]}
rb=(json.dumps(receipt)+'\n').encode();(solve/'FULL_SOLVE.json').write_bytes(rb)
source=(P/'audit_solve.py').read_bytes();(work/'audit_solve.py').write_bytes(source)
cmd=['python',str(work/'audit_solve.py'),'--workspace',str(work),'--frame',str(frame),'--solve',str(solve)]
run=subprocess.run(cmd,capture_output=True,text=True);assert run.returncode==0,(run.stdout,run.stderr);positive=json.loads((work/'SOLVE_CHECKS.json').read_text());assert int(positive['residual_squared_integer'])==r2 and int(positive['finite_lift_error_squared_integer'])==err
neg=[]
for name in ['residual_square_tamper','coefficient_payload_tamper','lift_payload_tamper','frame_admission_hash_tamper']:
 (work/'SOLVE_CHECKS.json').unlink(missing_ok=True)
 if name=='residual_square_tamper':
  bad=receipt.copy();bad['normal_equation_residual_squared_integer']=str(r2+1);(solve/'FULL_SOLVE.json').write_text(json.dumps(bad))
 elif name=='coefficient_payload_tamper':(solve/'COEFFICIENTS.json.gz').write_bytes(gzip.compress(cb+b' ',mtime=0))
 elif name=='lift_payload_tamper':(solve/'LIFT.i128.gz').write_bytes(gzip.compress(b'\x01'+raw[1:],mtime=0))
 else:(work/'ROWS_CHECKS.json').write_text(json.dumps({'status':'PASS_FULL1999_ROWS_AND_TRUE_RHS','frame_or_checkpoint_prefix_sha256':'0'*64,'RHS_error_squared_upper':[0,1]}))
 out=subprocess.run(cmd,capture_output=True,text=True);assert out.returncode!=0 and not(work/'SOLVE_CHECKS.json').exists();neg.append({'name':name,'nonzero_exit':True,'no_acceptance_receipt':True})
 (solve/'FULL_SOLVE.json').write_bytes(rb);(solve/'COEFFICIENTS.json.gz').write_bytes(cp);(solve/'LIFT.i128.gz').write_bytes(packed);(work/'ROWS_CHECKS.json').write_text(json.dumps({'status':'PASS_FULL1999_ROWS_AND_TRUE_RHS','frame_or_checkpoint_prefix_sha256':sha(fb),'RHS_error_squared_upper':[0,1]}))
(P/'AUDITOR_FIXTURE_CHECKS.json').write_text(json.dumps({'status':'PASS','auditor_source_sha256':sha(source),'positive_nonzero_signed_fullshape_fixture':{'rows':r,'columns':n,'residual_squared_integer':str(r2),'finite_lift_error_squared_integer':str(err),'all10554720_matvec_products_replayed':True},'negative_cases':neg,'scope':'synthetic audit-logic fixture only; fake source-admission precondition intentionally supplied, not a600cell frame or physical certificate','physical_promotion':0},indent=2,sort_keys=True)+'\n');print('PASS nonzero signed fullshape auditor fixture and4 failclosed tamper controls')
