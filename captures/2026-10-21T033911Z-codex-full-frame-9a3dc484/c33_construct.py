"""Construct the full G frame with bounded concurrency and authenticated C32 reuse."""
from pathlib import Path
from flint import arb,ctx
import argparse,json,hashlib,gzip,tempfile,subprocess,concurrent.futures,time
ap=argparse.ArgumentParser();ap.add_argument('--slice',type=Path,required=True);ap.add_argument('--slice-sha256',required=True);ap.add_argument('--operator',type=Path,required=True);ap.add_argument('--executable',type=Path,required=True);ap.add_argument('--build-receipt',type=Path,required=True);ap.add_argument('--reuse',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);ap.add_argument('--workers',type=int,default=7);a=ap.parse_args();assert 1<=a.workers<=7;a.out.mkdir(parents=True,exist_ok=False);ctx.prec=192;H=lambda b:hashlib.sha256(b).hexdigest();sb=a.slice.read_bytes();assert H(sb)==a.slice_sha256;sl=json.loads(sb);assert len(sl['columns'])==1999 and [r['column']for r in sl['columns']]==list(range(1999));build=json.loads(a.build_receipt.read_text());expected=build['executable_sha256'];assert H(a.executable.read_bytes())==expected;assert H(a.operator.read_bytes())==sl['operator_sha256']=='cca3ed7e671b8397c3940921d9845399425fd2558cc62708941c00fc4b899950'
rb=(a.reuse/'PARTIAL_FRAME.json').read_bytes();assert H(rb)=='1c8e2f214c7e832afbaff324524a12dc3dbdd9bb126e031d2a71f84c437fe015';reuse={r['column']:r for r in json.loads(rb)['rows']};assert len(reuse)==16
S=2**96;data=[(((13*i+7)%17)-8)*3*S//4096 for i in range(253952)];assert sum(v*v for v in data)<(2*S)**2;cache={};start=time.monotonic()
def phases(w):
 if w in cache:return cache[w]
 v=[];ph=hashlib.sha256()
 for j in range(4096):
  t=arb(j*w)/2**41;pair=[]
  for x in [t.cos(),t.sin()]:
   n=(x*2**128).mid().floor().unique_fmpz();assert n is not None;n=int(n);assert abs(x-arb(n)/2**128)<arb(1)/2**127;ph.update(n.to_bytes(17,'little',signed=True));pair.append(n)
  v.append(tuple(pair))
 cache[w]=(v,ph.hexdigest());return cache[w]
def encode(row):
 A=row['a'];B=row['b'];assert len(A)==len(B)==62
 if row['mode']=='zero':y=[v*2**50 for v in A]*4096;checks=0;phasehash=H(b'')
 else:
  tab,phasehash=phases(row['frequency_integer']);checks=8192
  if row['mode']=='u':y=[(u*c-v*s)//2**78 for c,s in tab for u,v in zip(A,B)]
  else:assert row['mode']=='v';y=[(u*s+v*c)//2**78 for c,s in tab for u,v in zip(A,B)]
 assert len(y)==253952 and sum(v*v for v in y)<(3*S)**2
 z=sum(v*w for v,w in zip(y,data));txt=''.join(str(v)+'\n'for v in y);return txt,checks,phasehash,z
def action(row,encoded):
 txt,checks,phasehash,z=encoded;inputhash=H(txt.encode());c=row['column'];name=f'row_{c:04d}.i128.gz'
 assert H(a.executable.read_bytes())==expected and H(a.operator.read_bytes())==sl['operator_sha256']
 if c in reuse:
  old=reuse[c];assert old['native_executable_sha256']==expected and old['mode']==row['mode'] and old['frequency_integer']==row['frequency_integer'] and old['input_text_sha256']==inputhash and old['phase_table_sha256']==phasehash and int(old['rhs_dot_integer'])==z
  packed=(a.reuse/old['output_row_file']).read_bytes();assert H(packed)==old['output_row_sha256'];raw=gzip.decompress(packed);assert H(raw)==old['output_decoded_sha256'];origin='REUSED_PINNED_C32_ROW'
 else:
  with tempfile.TemporaryDirectory(prefix='ud-fullframe-')as d:
   inp=Path(d)/'input.txt';out=Path(d)/'output.txt';inp.write_text(txt);p=subprocess.run([str(a.executable),str(a.operator),'adjoint',str(inp),str(out)],capture_output=True,text=True);assert p.returncode==0,p.stderr;vals=list(map(int,out.read_text().split()));assert len(vals)==2640;raw=b''.join(v.to_bytes(16,'little',signed=True)for v in vals)
  packed=gzip.compress(raw,compresslevel=9,mtime=0);origin='NEW_C31_NATIVE_ADJOINT'
 assert len(raw)==2640*16;vals=[int.from_bytes(raw[k:k+16],'little',signed=True)for k in range(0,len(raw),16)];assert sum(v*v for v in vals)<(3*S)**2;(a.out/name).write_bytes(packed)
 return {'column':c,'mode':row['mode'],'frequency_integer':row['frequency_integer'],'phase_enclosure_checks':checks,'phase_table_sha256':phasehash,'input_text_sha256':inputhash,'output_row_file':name,'output_row_sha256':H(packed),'output_decoded_sha256':H(raw),'rhs_dot_integer':str(z),'rhs_dot_denominator_power2':192,'state_integer_scale_bits':96,'native_executable_sha256':expected,'origin':origin,'status':'PASS_SOURCE_BOUND_FULL_FRAME_ROW'}
rows=[];pending=set()
def collect(done):
 for job in done:
  row=job.result();rows.append(row)
  with(a.out/'CHECKPOINT.jsonl').open('a')as f:f.write(json.dumps(row,sort_keys=True)+'\n')
  print(json.dumps({'completed':len(rows),'column':row['column'],'origin':row['origin'],'elapsed_seconds':round(time.monotonic()-start,2)}),flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=a.workers)as pool:
 for row in sl['columns']:
  if len(pending)>=a.workers:
   done,pending=concurrent.futures.wait(pending,return_when=concurrent.futures.FIRST_COMPLETED);collect(done)
  pending.add(pool.submit(action,row,encode(row)))
 while pending:
  done,pending=concurrent.futures.wait(pending,return_when=concurrent.futures.FIRST_COMPLETED);collect(done)
rows.sort(key=lambda r:r['column']);assert [r['column']for r in rows]==list(range(1999));assert sum(r['origin']=='REUSED_PINNED_C32_ROW'for r in rows)==16;assert sum(r['origin']=='NEW_C31_NATIVE_ADJOINT'for r in rows)==1983
result={'status':'PASS_FULL1999_SOURCE_FRAME_CONSTRUCTION','rows':rows,'actual_rows_constructed_or_authenticated':1999,'new_native_adjoint_rows':1983,'authenticated_reused_C32_rows':16,'full_required_rows':1999,'trial_slice_sha256':H(sb),'reuse_receipt_sha256':H(rb),'build_receipt_sha256':H(a.build_receipt.read_bytes()),'operator_sha256':sl['operator_sha256'],'data_rule':'3*(((13i+7)mod17)-8)/4096','data_norm_squared_integer':str(sum(v*v for v in data)),'data_scale_bits':96,'precision_bits':192,'phase_tables_constructed':len(cache),'unique_phase_scalar_checks':len(cache)*8192,'logical_phase_binding_checks':sum(r['phase_enclosure_checks']for r in rows),'solve_status':'NOT_RUN_HOLD','physical_input_status':'UNSUPPLIED_HOLD','physical_promotion':0,'external_promotion_review':'PENDING'};(a.out/'FULL_FRAME.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print('PASS all1999 rows; full solve checked separately',flush=True)
