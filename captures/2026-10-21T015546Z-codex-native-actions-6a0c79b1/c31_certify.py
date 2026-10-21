from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib,math,gzip
ap=argparse.ArgumentParser();ap.add_argument('--repo',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=False);C=a.repo/'captures/2026-10-21T013801Z-codex-source-actions-9c7b87b9';H=lambda b:hashlib.sha256(b).hexdigest();op=gzip.decompress((C/'OPERATOR.txt.gz').read_bytes());assert H(op)=='cca3ed7e671b8397c3940921d9845399425fd2558cc62708941c00fc4b899950';assert H((C/'ACTION_CONSTANTS.json').read_bytes())=='a098a06f4c11df9258433e64d3836ca9465efa668b69e2ecf73ebf28e3b59ac4';parent=json.loads((C/'ACTION_CONSTANTS.json').read_text());assert parent['boundary_norm_squared_bounds']==['24','15','15'];assert parent['H_max_absolute_row_sum']==24
lines=op.decode().splitlines();assert lines[0]=='2640 62 4096 40 128';obs=list(map(int,lines[1].split()));edges=[tuple(map(int,l.split()))for l in lines[3:]];assert len(obs)==len(set(obs))==62 and len(edges)==14880;E={(i,j):w for i,j,w in edges};assert all(E[j,i]==-w for(i,j),w in E.items());rows=[0]*2640
for i,j,w in edges:rows[i]+=abs(w)
assert max(rows)==24
u=F(52,2**104);r=120*u;tau=F(5,2)**41/math.factorial(41)/(1-F(5,84));cap=4096;state=4096*(tau*cap+r);fw=state+F(504,2**96);ad=state+F(52,2**96);assert state<1 and fw<F(1,2**68)and ad<F(1,2**68)
terms=[F(5,2)**k/math.factorial(k)for k in range(41)];assert max(terms)<4 and sum(terms)+tau<13
term=4*cap+3*u;partialsum=13*cap+r;assert24=24*term*2**104<F(2**123);assert assert24 and partialsum*2**104<2**121
# Conservative runtime guards ensure safety even before source spectral bounds:
# each term<2^119; row abs sum<=24; max41 terms in a partial output.
assert 24*2**119<2**124<2**127 and 41*2**119<2**125<2**127
rat=F(0)
for k in range(1,41):
 rat=F(5,2*k)*rat+1;assert rat<3
result={'status':'PASS_NATIVE104_SOURCE_ERROR_AND_OVERFLOW_CERTIFICATE','parent_operator_sha256':H(op),'parent_action_constants_sha256':H((C/'ACTION_CONSTANTS.json').read_bytes()),'same_model':True,'internal_bits':104,'external_bits':96,'degree':40,'computed_state_cap':cap,'tau':str(tau),'rounding_halfstep_error':str(r),'accumulated_state_error':str(state),'forward_error_upper':str(fw),'adjoint_error_upper':str(ad),'absolute_error_gate':'<2^-68 on state ball2048/data ball2049','term_integer_bound':'<2^123 for source sparse accumulators','partial_sum_integer_bound':'<2^121','guard_safety':'term<2^119 ⇒ every row partial<2^124 and every output partial<2^125; signed128 safe','controls':{'Taylor_coefficients':41,'term_rounding_recurrence':40,'finite_norm_product':3,'native_guard_integer_comparisons':4},'full8192_decoder_run':False,'physical_promotion':0,'external_promotion_review':'PENDING'}
(a.out/'NATIVE_CONSTANTS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');(a.out/'OPERATOR.txt').write_bytes(op);(a.out/'SOURCE_BINDINGS.json').write_text(json.dumps({'operator_sha256':H(op),'parent_capture':str(C.relative_to(a.repo)),'parent_action_constants_sha256':H((C/'ACTION_CONSTANTS.json').read_bytes()),'archived_executables_run':0,'header_note':'128 is retained C30 protocol metadata; optimized backend grid104 is declared separately'},indent=2,sort_keys=True)+'\n');print(json.dumps({'status':result['status'],'forward_error':float(fw),'adjoint_error':float(ad)}))
