"""Independent selected source binding and higher-precision encoded-column audit."""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,gzip,argparse,numpy as np
from flint import arb,ctx
ctx.prec=256
ap=argparse.ArgumentParser();ap.add_argument('--workspace',type=Path,required=True);a=ap.parse_args();W=a.workspace;P=Path(__file__).resolve().parent
sha=lambda b:hashlib.sha256(b).hexdigest()
cap=W/'ud-repo/captures/2026-10-20T234200Z-codex-weighted-conditioning-d6af1d67'
pr=(cap/'PROPOSAL_FREEZE.json').read_bytes();assert sha(pr)=='7572aa3452ede3e283bd850014f443759e0ff0d181f30815d5b8be3d7a209517';proposal=json.loads(pr)
packed=(cap/'Q_DYADIC.bin.gz').read_bytes();raw=gzip.decompress(packed);assert sha(packed)==proposal['Q_gzip_sha256'] and sha(raw)==proposal['Q_decoded_sha256'];assert len(raw)==2640*1999*8
trial=np.frombuffer(raw,dtype='<i8').reshape((2640,1999))
op=(W/'c32_source_final/OPERATOR.txt').read_bytes();assert sha(op)=='cca3ed7e671b8397c3940921d9845399425fd2558cc62708941c00fc4b899950';obs=list(map(int,op.decode().splitlines()[1].split()));assert len(obs)==len(set(obs))==62
slice_bytes=(W/'c32_source_final/TRIAL_SLICE.json').read_bytes();sl=json.loads(slice_bytes);rbytes=(W/'c32_partial/PARTIAL_FRAME.json').read_bytes();report=json.loads(rbytes)
assert report['trial_slice_sha256']==sha(slice_bytes) and report['actual_rows_constructed']==16 and report['full_required_rows']==1999 and report['full_frame_status']=='NOT_CONSTRUCTED_HOLD'
assert sl['source_proposal_sha256']==sha(pr) and sl['Q_decoded_sha256']==sha(raw)
build=(W/'c31_BUILD_RECEIPT.json').read_bytes();buildj=json.loads(build);assert report['build_receipt_sha256']==sha(build) and buildj['executable_sha256']==sha((W/'c31_action').read_bytes()) and buildj['source_sha256']==sha((W/'c31_action.cpp').read_bytes())
bycol={r['column']:r for r in report['rows']};assert len(bycol)==16
cache={};phase_checks=0;results=[]
data=[3*(((13*i+7)%17)-8)*2**84 for i in range(253952)]
assert sum(v*v for v in data)==int(report['data_norm_squared_integer'])
for row in sl['columns']:
 col=row['column'];idx=col if col<1000 else col-999;mode='zero' if col==0 else 'u' if col<1000 else 'v'
 A=[int(trial[v,idx])for v in obs];B=[0]*62 if col==0 else [int(trial[v,999+idx])for v in obs]
 freq=proposal['frequency_integers'][idx];assert (A,B,freq,mode)==(row['a'],row['b'],row['frequency_integer'],row['mode'])
 assert sum(v*v for v in A)<Q(9,8)**2*2**80 and sum(v*v for v in B)<Q(9,8)**2*2**80
 if mode=='zero':values=[v*2**50 for v in A]*4096;phash=hashlib.sha256().hexdigest();logical=0
 else:
  if freq not in cache:
   phases=[];hs=hashlib.sha256()
   for j in range(4096):
    arg=arb(freq*j)/2**41;cs=[]
    for z in (arg.cos(),arg.sin()):
     p=int((z*2**128).mid().floor().unique_fmpz());assert abs(z-arb(p)/2**128)<arb(1)/2**127;phase_checks+=1;hs.update(p.to_bytes(17,'little',signed=True));cs.append(p)
    phases.append(tuple(cs))
   cache[freq]=(phases,hs.hexdigest())
  phases,phash=cache[freq];values=[]
  for c,s in phases:
   if mode=='u':values.extend((u*c-v*s)//2**78 for u,v in zip(A,B))
   else:values.extend((u*s+v*c)//2**78 for u,v in zip(A,B))
  logical=8192
 rr=bycol[col];assert rr['phase_enclosure_checks']==logical and rr['phase_table_sha256']==phash
 assert len(values)==253952 and sum(v*v for v in values)<(3*2**96)**2
 textsha=sha(''.join(str(v)+'\n' for v in values).encode());assert rr['input_text_sha256']==textsha
 rhs=sum(v*w for v,w in zip(values,data));assert rhs==int(rr['rhs_dot_integer']) and rr['rhs_dot_denominator_power2']==192
 gz=(W/'c32_partial'/rr['output_row_file']).read_bytes();out=gzip.decompress(gz);assert sha(gz)==rr['output_row_sha256'] and sha(out)==rr['output_decoded_sha256'] and len(out)==2640*16
 ints=[int.from_bytes(out[j:j+16],'little',signed=True)for j in range(0,len(out),16)];assert sum(v*v for v in ints)<(3*2**96)**2
 assert rr['native_executable_sha256']==buildj['executable_sha256']
 results.append({'column':col,'mode':mode,'frequency_integer':freq,'encoded_coordinates':len(values),'input_text_sha256':textsha,'phase_table_sha256':phash,'RHS_dot_exact_match':True,'output_packed_sha256':sha(gz),'output_decoded_sha256':sha(out),'output_shape_and_norm_match':True})
result={'status':'PASS','source_proposal_sha256':sha(pr),'slice_sha256':sha(slice_bytes),'partial_report_sha256':sha(rbytes),'native_source_sha256':buildj['source_sha256'],'native_executable_sha256':buildj['executable_sha256'],'own_Arb_precision_bits':256,'unique_frequency_phase_scalar_enclosures':phase_checks,'logical_phase_binding_checks':sum(r['phase_enclosure_checks']for r in report['rows']),'encoded_coordinates_reconstructed':sum(r['encoded_coordinates']for r in results),'rows':results,'scope':{'producer_constructor_not_executed':True,'saved_native_outputs_hash_shape_norm_checked_not_independently_recomputed':True,'all1999_frame_not_constructed_or_certified':True,'no_full_inverse_or_decoder_certified':True,'physical_promotion':0,'external_review':'PENDING'}}
(P/'PARTIAL_INPUT_CHECKS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':'PASS','rows':len(results),'encoded_coordinates':result['encoded_coordinates_reconstructed'],'unique_phase_checks':phase_checks}))
