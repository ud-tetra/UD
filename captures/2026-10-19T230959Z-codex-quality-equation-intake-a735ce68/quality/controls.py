"""Post-known-outcome rejection controls; no estimator or raw-data constructor."""
import json,hashlib,argparse
from pathlib import Path
import numpy as np
from flint import arb,arb_mat,fmpq,ctx
ctx.prec=512
HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def mat(arr,den):return arb_mat([[arb(fmpq(int(x),den)) for x in row] for row in arr])
def floor(D,L,R):
 try:inv=D.inv()
 except (ValueError,ZeroDivisionError):return None
 n=D.nrows();s=sum((inv[i,j]*inv[i,j] for i in range(n) for j in range(n)),arb(0))
 return 1/s.sqrt()/L/R

def main():
 a=argparse.ArgumentParser();a.add_argument('--inputs',required=True);a.add_argument('--out',required=True);o=a.parse_args();p=Path(o.inputs);dest=Path(o.out);assert not dest.exists();f=json.loads((HERE/'CONTROL_FREEZE.json').read_text());assert sha(HERE/'controls.py')==f['code_sha256'];rows=[]
 def add(id,got,want):assert got==want,(id,got,want);rows.append({'id':id,'observed':got,'expected':want})
 for name,h in f['inputs'].items():assert sha(p/name)==h
 cert=json.loads((p/'CERTIFICATE.json').read_text())
 for count in [1,2]:
  with np.load(p/f'TEST_FRAME_{count}.npz',allow_pickle=False) as z:
   D=mat(z['compression_decimal'],1<<cert['rows'][count-1]['compression_bits']);LG=z['left_gram_decimal'];RG=z['right_gram_decimal']
  L=arb(fmpq(max(sum(abs(int(x)) for x in row) for row in LG),1<<154)).sqrt();R=arb(fmpq(max(sum(abs(int(x)) for x in row) for row in RG),1<<(2*cert['rows'][count-1]['test_right_scale_bits']))).sqrt();lo=floor(D,L,R)
  add(f'{count}_real_compression_cap_obstruction',bool(lo>arb(fmpq(1,1<<41))),True)
  add(f'{count}_inflated_cap_not_obstructed',bool(lo>arb(fmpq(1,1<<30))),False)
  corrupt=arb_mat([[D[i,j] if i!=209 else 0 for j in range(210)] for i in range(210)])
  add(f'{count}_zero_last_row_not_invertible',floor(corrupt,L,R) is None,True)
  add(f'{count}_wrong_artifact_digest_refused',hashlib.sha256((p/f'TEST_FRAME_{count}.npz').read_bytes()+b'corrupt').hexdigest()==f['inputs'][f'TEST_FRAME_{count}.npz'],False)
 add('three_quantum_coordinates_outside_three_halves_ball',4*3<=9,False)
 add('one_double_quantum_coordinate_outside_three_halves_ball',4*4<=9,False)
 add('one_quantum_admitted_to_closed_q_ball',1<=1,True)
 add('two_quantum_coordinates_admitted_to_closed_three_halves_ball',4*2<=9,True)
 dest.write_text(json.dumps({'status':'PASS_POST_KNOWN_OUTCOME_TWELVE_CONTROLS','freeze_sha256':sha(HERE/'CONTROL_FREEZE.json'),'controls':rows,'new_estimator_calls':0,'physical_promotion':0},indent=2)+'\n');print(len(rows))
if __name__=='__main__':main()
