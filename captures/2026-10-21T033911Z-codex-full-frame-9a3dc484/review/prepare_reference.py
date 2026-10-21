"""Independent full source, phase and true-RHS reference; no native actions."""
from pathlib import Path
import json,gzip,hashlib,struct,argparse
from fractions import Fraction as Q
from flint import arb,ctx
ctx.prec=256
ap=argparse.ArgumentParser();ap.add_argument('--workspace',type=Path,required=True);a=ap.parse_args();W=a.workspace;P=Path(__file__).resolve().parent
sha=lambda b:hashlib.sha256(b).hexdigest();source=W/'c33_source/FULL_SLICE.json';sb=source.read_bytes();sl=json.loads(sb)
cap=W/'ud-repo/captures/2026-10-20T234200Z-codex-weighted-conditioning-d6af1d67';pb=(cap/'PROPOSAL_FREEZE.json').read_bytes();assert sha(pb)=='7572aa3452ede3e283bd850014f443759e0ff0d181f30815d5b8be3d7a209517';proposal=json.loads(pb);packed=(cap/'Q_DYADIC.bin.gz').read_bytes();qraw=gzip.decompress(packed);assert sha(packed)==proposal['Q_gzip_sha256'] and sha(qraw)==proposal['Q_decoded_sha256'] and len(qraw)==2640*1999*8
op=(W/'c33_source/OPERATOR.txt').read_bytes();assert sha(op)=='cca3ed7e671b8397c3940921d9845399425fd2558cc62708941c00fc4b899950';obs=list(map(int,op.decode().splitlines()[1].split()));assert len(obs)==len(set(obs))==62
assert len(sl['columns'])==1999 and [r['column']for r in sl['columns']]==list(range(1999));assert sl['source_proposal_sha256']==sha(pb) and sl['Q_decoded_sha256']==sha(qraw)
rows=[];group={}
get=lambda r,c:struct.unpack_from('<q',qraw,(r*1999+c)*8)[0]
for col,row in enumerate(sl['columns']):
 idx=col if col<1000 else col-999;mode='zero'if col==0 else'u'if col<1000 else'v';aa=[get(r,idx)for r in obs];bb=[0]*62 if col==0 else[get(r,999+idx)for r in obs];freq=proposal['frequency_integers'][idx]
 assert (row['a'],row['b'],row['mode'],row['frequency_integer'])==(aa,bb,mode,freq)
 assert sum(x*x for x in aa)<Q(9,8)**2*2**80 and sum(x*x for x in bb)<Q(9,8)**2*2**80
 # Exact reduction of k_(j,c)=((13*(62j+c)+7) mod17)-8.
 At=[sum(x*(((7*t+13*c+7)%17)-8)for c,x in enumerate(aa))for t in range(17)]
 Bt=[sum(x*(((7*t+13*c+7)%17)-8)for c,x in enumerate(bb))for t in range(17)]
 rows.append((col,mode,freq,At,Bt));group.setdefault(freq,[]).append(len(rows)-1)
assert len(group)-1==119 and 0 in group
phase=[];intervals=[None]*1999;checks=0
for freq,indices in sorted(group.items()):
 C=[arb(0)for _ in range(17)];S=[arb(0)for _ in range(17)];hs=hashlib.sha256()
 if freq==0:
  C=[arb(sum(j%17==t for j in range(4096)))for t in range(17)]
 else:
  for j in range(4096):
   arg=arb(j*freq)/2**41;c=arg.cos();s=arg.sin();C[j%17]+=c;S[j%17]+=s
   for x in(c,s):
    value=int((x*2**128).mid().floor().unique_fmpz());assert abs(x-arb(value)/2**128)<arb(1)/2**127;checks+=1;hs.update(value.to_bytes(17,'little',signed=True))
 phase.append({'frequency_integer':freq,'phase_table_sha256':hs.hexdigest(),'scalar_enclosures':0 if freq==0 else8192,'columns':len(indices)})
 for ix in indices:
  col,mode,_,A,B=rows[ix];z=arb(0)
  for t in range(17):
   if mode in('zero','u'):z+=A[t]*C[t]-B[t]*S[t]
   else:z+=A[t]*S[t]+B[t]*C[t]
  z*=arb(3)/2**58
  lo=int((z*2**160).lower().floor().unique_fmpz())-1;hi=int((z*2**160).upper().ceil().unique_fmpz())+1
  assert z>arb(lo)/2**160 and z<arb(hi)/2**160
  intervals[col]={'column':col,'lower_integer':str(lo),'upper_integer':str(hi),'denominator_power2':160,'mode':mode,'frequency_integer':freq}
 print(json.dumps({'frequency_done':freq,'groups':len(phase),'of':len(group)}),flush=True)
reference={'status':'PASS_INDEPENDENT_SOURCE_PHASE_AND_TRUE_RHS_REFERENCE','source_slice_sha256':sha(sb),'proposal_sha256':sha(pb),'Q_decoded_sha256':sha(qraw),'operator_sha256':sha(op),'precision_bits':256,'source_rows_reconstructed':1999,'unique_nonzero_frequencies':119,'unique_phase_scalar_enclosures':checks,'phase_tables':phase,'true_RHS_intervals':intervals,'data_rule':'y_(j,c)=3*(((7j+13c+7)mod17)-8)/4096','RHS_formula':'3*2^-58 sum_t(A_t*C_t-B_t*S_t) or3*2^-58 sum_t(A_t*S_t+B_t*C_t)','scope':'independent high-precision trueY RHS reference; no507million encoded coordinate dots or native adjoints executed','physical_promotion':0}
raw=(json.dumps(reference,indent=2,sort_keys=True)+'\n').encode();out=P/'REFERENCE_RHS.json.gz';out.write_bytes(gzip.compress(raw,compresslevel=9,mtime=0))
(P/'REFERENCE_CHECKS.json').write_text(json.dumps({'status':'PASS','reference_packed_sha256':sha(out.read_bytes()),'reference_decoded_sha256':sha(raw),'source_slice_sha256':sha(sb),'source_rows_reconstructed':1999,'unique_nonzero_frequencies':119,'unique_phase_scalar_enclosures':checks,'true_RHS_intervals':1999,'precision_bits':256,'native_actions_executed':0,'physical_promotion':0},indent=2,sort_keys=True)+'\n');print('PASS1999source rows,119phase tables,1999 trueRHS intervals')
