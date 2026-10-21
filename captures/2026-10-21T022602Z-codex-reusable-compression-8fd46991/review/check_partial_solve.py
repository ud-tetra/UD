"""Independent exact saved-row Gram, solve residual, positive pivots and finite lift audit."""
from pathlib import Path
from fractions import Fraction as Q
import json,gzip,hashlib,math,argparse
ap=argparse.ArgumentParser();ap.add_argument('--workspace',type=Path,required=True);a=ap.parse_args();W=a.workspace;P=Path(__file__).resolve().parent
sha=lambda b:hashlib.sha256(b).hexdigest()
meta_path=W/'c32_partial_final/PARTIAL_FRAME.json';meta=json.loads(meta_path.read_text());receipt_path=W/'c32_solve/PARTIAL_SOLVE.json';receipt=json.loads(receipt_path.read_text())
assert len(meta['rows'])==16 and receipt['partial_rank']==16 and receipt['full_required_rank']==1999 and receipt['frame_receipt_sha256']==sha(meta_path.read_bytes())
G=[];z=[];replayed=[]
for row in meta['rows']:
 name=row['output_row_file'];packed=(W/'c32_partial_final'/name).read_bytes();raw=gzip.decompress(packed);assert sha(packed)==row['output_row_sha256'] and sha(raw)==row['output_decoded_sha256']
 G.append([int.from_bytes(raw[i:i+16],'little',signed=True)for i in range(0,len(raw),16)]);z.append(int(row['rhs_dot_integer']))
 assert packed==(W/'c32_partial'/name).read_bytes();replayed.append(name)
assert meta_path.read_bytes()==(W/'c32_partial/PARTIAL_FRAME.json').read_bytes()
H=[[sum(u*v for u,v in zip(a,b))for b in G]for a in G];assert H==[[int(v)for v in row]for row in receipt['Gram_integer_rows']] and z==[int(v)for v in receipt['RHS_integer']]
# Independent elimination uses Schur-complement updates on symmetric square matrix.
A=[[Q(x)for x in row]for row in H];pivots=[]
for k in range(16):
 pivot=A[k][k];assert pivot>0;pivots.append(pivot)
 for i in range(k+1,16):
  for j in range(i,16):A[j][i]=A[i][j]=A[i][j]-A[i][k]*A[k][j]/pivot
assert pivots==[Q(v)for v in receipt['positive_exact_elimination_pivots']]
coeff=[Q(v)for v in receipt['coefficient_fractions']];assert len(coeff)==16
res=[sum(Q(v)*x for v,x in zip(row,coeff))-target for row,target in zip(H,z)];assert res==[0]*16
lift=[sum((Q(G[j][i])*coeff[j]for j in range(16)),Q())for i in range(2640)];delivered=[x.numerator//x.denominator for x in lift]
error2=sum((Q(q)-v)**2 for q,v in zip(delivered,lift))/2**192;assert error2==Q(receipt['lift_error_squared']) and error2<Q(1,2**88)
raw=b''.join(v.to_bytes(16,'little',signed=True)for v in delivered);actual=gzip.decompress((W/'c32_solve/LIFT.i128.gz').read_bytes());assert raw==actual and sha(raw)==receipt['lift_decoded_sha256']
# Source-authentication version changes only the explicit expected slice hash admission.
old=(W/'c32_construct_initial.py').read_text();new=(W/'c32_construct.py').read_text();assert new==old.replace("ap.add_argument('--slice',type=Path,required=True);","ap.add_argument('--slice',type=Path,required=True);ap.add_argument('--slice-sha256',required=True);").replace('sl=json.loads(a.slice.read_text());','assert H(a.slice.read_bytes())==a.slice_sha256;sl=json.loads(a.slice.read_text());')
result={'status':'PASS','partial_frame_receipt_sha256':sha(meta_path.read_bytes()),'partial_solve_receipt_sha256':sha(receipt_path.read_bytes()),'exact_Gram_entries_recomputed':256,'exact_Gram_dot_product_terms':16*16*2640,'positive_exact_pivots_compared':16,'normal_equation_residual_exact_zero':True,'lift_coordinates_independently_recomputed':2640,'finite_lift_error_squared':[error2.numerator,error2.denominator],'lift_error_lt_2^-44':True,'lift_decoded_sha256':sha(raw),'scientific_replay_files_identical':len(replayed)+1,'source_authentication_only_delta_verified':True,'source_hashes':{f:sha((W/f).read_bytes())for f in ['c32_prepare.py','c32_construct.py','c32_partial_solve.py']},'scope':{'producer_solve_driver_not_executed':True,'one16row_RHS_solved_no_full_inverse_materialized':True,'full1999_frame_and_decoder_not_certified':True,'no_recovery_of641_nominal_hidden_components':True,'physical_promotion':0,'external_review':'PENDING'}}
(P/'PARTIAL_SOLVE_CHECKS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print('PASS exact256Gram entries,16pivots,zeroresidual,2640lift coordinates,17replay files')
