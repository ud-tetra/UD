"""Independent Python-bigint residual/lift replay; no SciPy, FLINT, native actions or exact Gram."""
from pathlib import Path
from fractions import Fraction as Q
from math import isqrt,factorial
import argparse,json,gzip,hashlib,time
ap=argparse.ArgumentParser();ap.add_argument('--workspace',type=Path,required=True);ap.add_argument('--frame',type=Path,required=True);ap.add_argument('--solve',type=Path,required=True);a=ap.parse_args();W=a.workspace;P=Path(__file__).resolve().parent
sha=lambda b:hashlib.sha256(b).hexdigest();fb=(a.frame/'FULL_FRAME.json').read_bytes();meta=json.loads(fb);rows_audit=json.loads((P/'ROWS_CHECKS.json').read_text());assert rows_audit['status']=='PASS_FULL1999_ROWS_AND_TRUE_RHS' and rows_audit['frame_or_checkpoint_prefix_sha256']==sha(fb)
solveb=(a.solve/'FULL_SOLVE.json').read_bytes();result=json.loads(solveb);assert result['status']=='PASS_ACTUAL_FULL1999_FLOAT_PROPOSAL_EXACT_RESIDUAL_AND_FINITE_LIFT' and result['frame_receipt_sha256']==sha(fb)
packed=(a.solve/'COEFFICIENTS.json.gz').read_bytes();raw=gzip.decompress(packed);coeff=json.loads(raw);assert sha(packed)==result['coefficient_packed_sha256'] and sha(raw)==result['coefficient_decoded_sha256'] and coeff['frame_receipt_sha256']==sha(fb)
p=coeff['coefficient_denominator_power2'];assert type(p)is int and p==160 and result['coefficient_denominator_power2']==p;aa=[int(v)for v in coeff['coefficient_integers']];assert len(aa)==1999;scale=2**p;G=[];L=[0]*2640;z=[]
start=time.monotonic()
for ix,row in enumerate(meta['rows']):
 assert row['column']==ix and row['state_integer_scale_bits']==96 and row['rhs_dot_denominator_power2']==192
 packed=(a.frame/row['output_row_file']).read_bytes();raw=gzip.decompress(packed);assert sha(packed)==row['output_row_sha256'] and sha(raw)==row['output_decoded_sha256'] and len(raw)==2640*16
 values=[int.from_bytes(raw[k:k+16],'little',signed=True)for k in range(0,len(raw),16)];G.append(values);z.append(int(row['rhs_dot_integer']))
 for k,x in enumerate(values):L[k]+=aa[ix]*x
rnum=[sum(x*y for x,y in zip(g,L))-zi*scale for g,zi in zip(G,z)];r2=sum(x*x for x in rnum);denbits=192+p
assert result['normal_equation_residual_denominator_power2']==denbits and int(result['normal_equation_residual_squared_integer'])==r2 and Q(result['normal_equation_residual_squared'])==Q(r2,2**(2*denbits)) and r2<2**(2*denbits-128)
history=result['refinement_history'];assert 1<=len(history)<=9
for i,row in enumerate(history):
 assert row['iteration']==i and row['residual_denominator_power2']==denbits
 actual=int(row['residual_squared_integer'])<2**(2*denbits-128);assert row['residual_gate_pass']is actual and actual is(i==len(history)-1)
assert int(history[-1]['residual_squared_integer'])==r2
q=[x//scale for x in L];errnum=sum((v*scale-x)**2 for v,x in zip(q,L));assert errnum==int(result['finite_lift_error_squared_integer']) and result['finite_lift_error_denominator_power2']==96+p and Q(result['finite_lift_error_squared'])==Q(errnum,2**(2*(96+p))) and errnum<2**(2*(96+p)-88)
expected=b''.join(x.to_bytes(16,'little',signed=True)for x in q);packed=(a.solve/'LIFT.i128.gz').read_bytes();raw=gzip.decompress(packed);assert expected==raw and sha(raw)==result['lift_decoded_sha256'] and sha(packed)==result['lift_packed_sha256'];assert sum(x*x for x in q)<(1024*2**96)**2
# Exact minimal192-grid square-root upper wrappers for scientific error composition.
def upper_sqrt(v):
 target=v.numerator*2**384;k=isqrt(target//v.denominator)
 if k*k*v.denominator<target:k+=1
 assert k*k*v.denominator>=target and(k==0 or(k-1)**2*v.denominator<target)
 return Q(k,2**192)
EZ2=Q(*rows_audit['RHS_error_squared_upper']);ER2=Q(r2,2**(2*denbits));EL2=Q(errnum,2**(2*(96+p)));ez=upper_sqrt(EZ2);er=upper_sqrt(ER2);el=upper_sqrt(EL2)
s=Q(61,27648);h=s*(Q(1,384)-Q(1,8192));tau=Q(5,2)**41/factorial(41)/(1-Q(5,84));ad=4096*(4096*tau+Q(6240,2**104))+Q(52,2**96);EY=Q(3,2**127)+Q(504,2**96);delta=45*(ad+EY)
implementation=(ez+er)/(h-delta)+el;assert ez<Q(1,2**64) and er<Q(1,2**64) and el<Q(1,2**44) and implementation<Q(1,2**43)
out={'status':'PASS_INDEPENDENT_BIGINT_RESIDUAL_AND_FINITE_LIFT','frame_sha256':sha(fb),'solve_sha256':sha(solveb),'coefficient_decoded_sha256':result['coefficient_decoded_sha256'],'coefficient_grid_bits':p,'integer_matvec_product_terms_recomputed':2*1999*2640,'residual_components_recomputed':1999,'residual_squared_integer':str(r2),'residual_norm_denominator_power2':denbits,'finite_lift_coordinates_recomputed':2640,'finite_lift_error_squared_integer':str(errnum),'lift_decoded_sha256':sha(expected),'actual_composed_implementation_error_upper':[implementation.numerator,implementation.denominator],'actual_error_display_only':float(implementation),'sqrt_upper_grid_bits':192,'RHS_error_upper':[ez.numerator,ez.denominator],'residual_error_upper':[er.numerator,er.denominator],'lift_error_upper':[el.numerator,el.denominator],'all_fixed_gates_pass':True,'refinement_final_record_replayed_intermediate_records_only_gate_consistency_checked':True,'elapsed_seconds_observed':time.monotonic()-start,'scope':{'own_Python_bigint_backend_not_producer_FLINT_or_SciPy':True,'no_exact_full_Gram_materialized':True,'no_native_adjoint_calls_rerun':True,'one_frozen_synthetic_record_only':True,'arithmetic_error_relative_to_exact_compressed_decoder_not_state_truth':True,'full_physical_preparation_and_state_truth':'UNSUPPLIED_HOLD','floating_backend_universal_completeness':'OPEN','physical_promotion':0,'external_review':'PENDING'}}
(P/'SOLVE_CHECKS.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'integer_products':2*1999*2640,'actual_implementation_error_upper':float(implementation)}))
