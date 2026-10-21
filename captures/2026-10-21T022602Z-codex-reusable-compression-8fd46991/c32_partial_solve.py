from pathlib import Path
from fractions import Fraction as F
import argparse,json,gzip,hashlib,math
ap=argparse.ArgumentParser();ap.add_argument('--frame',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=False);meta=json.loads((a.frame/'PARTIAL_FRAME.json').read_text());assert meta['actual_rows_constructed']==16 and meta['full_required_rows']==1999;G=[];H=lambda b:hashlib.sha256(b).hexdigest()
for row in meta['rows']:
 packed=(a.frame/row['output_row_file']).read_bytes();assert H(packed)==row['output_row_sha256'];raw=gzip.decompress(packed);assert H(raw)==row['output_decoded_sha256'] and len(raw)==2640*16;G.append([int.from_bytes(raw[k:k+16],'little',signed=True)for k in range(0,len(raw),16)])
n=16;Gram=[[sum(x*y for x,y in zip(u,v))for v in G]for u in G];z=list(map(lambda r:int(r['rhs_dot_integer']),meta['rows']));A=[[F(v)for v in row]+[F(t)]for row,t in zip(Gram,z)];pivots=[]
for k in range(n):
 pivot=A[k][k];assert pivot>0;pivots.append(pivot)
 for i in range(k+1,n):
  t=A[i][k]/pivot
  for j in range(k,n+1):A[i][j]-=t*A[k][j]
x=[F(0)]*n
for i in range(n-1,-1,-1):x[i]=(A[i][n]-sum((A[i][j]*x[j]for j in range(i+1,n)),F(0)))/A[i][i]
assert all(sum((F(v)*t for v,t in zip(row,x)),F(0))==target for row,target in zip(Gram,z))
D=math.lcm(*(v.denominator for v in x));aa=[v.numerator*(D//v.denominator)for v in x];lift=[sum(G[j][i]*aa[j]for j in range(n))for i in range(2640)];q=[v//D for v in lift];errnum=sum((k*D-v)**2 for k,v in zip(q,lift));assert errnum<2640*D*D and F(errnum,D*D*2**192)<F(1,2**88)
raw=b''.join(v.to_bytes(16,'little',signed=True)for v in q);(a.out/'LIFT.i128.gz').write_bytes(gzip.compress(raw,compresslevel=9,mtime=0))
receipt={'status':'PASS_ACTUAL_PARTIAL16_EXACT_GRAM_SOLVE_AND_FINITE_LIFT','partial_rank':16,'full_required_rank':1999,'full_frame_or_full_decoder':'NOT_RUN_HOLD','Gram_denominator_power2':192,'Gram_integer_rows':[[str(v)for v in row]for row in Gram],'RHS_integer':list(map(str,z)),'RHS_denominator_power2':192,'coefficient_fractions':list(map(str,x)),'positive_exact_elimination_pivots':list(map(str,pivots)),'normal_equation_residual':'EXACT_ZERO','lift_error_squared':str(F(errnum,D*D*2**192)),'lift_error_gate':'<2^-44','lift_decoded_sha256':H(raw),'frame_receipt_sha256':H((a.frame/'PARTIAL_FRAME.json').read_bytes()),'scope':'Only16-row construction/solve control; no recovery of1999 observable coordinates or nominal orthogonal projection','physical_promotion':0,'external_promotion_review':'PENDING'};(a.out/'PARTIAL_SOLVE.json').write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n');print('PASS exact16rank Gram solve, residual0 and finite2640-coordinate lift')
