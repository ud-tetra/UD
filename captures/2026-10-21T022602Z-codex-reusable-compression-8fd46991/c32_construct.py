from pathlib import Path
from flint import arb,ctx
import argparse,json,hashlib,gzip,tempfile,subprocess,concurrent.futures
ap=argparse.ArgumentParser();ap.add_argument('--slice',type=Path,required=True);ap.add_argument('--slice-sha256',required=True);ap.add_argument('--operator',type=Path,required=True);ap.add_argument('--executable',type=Path,required=True);ap.add_argument('--build-receipt',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=False);ctx.prec=192;H=lambda b:hashlib.sha256(b).hexdigest();assert H(a.slice.read_bytes())==a.slice_sha256;sl=json.loads(a.slice.read_text());build=json.loads(a.build_receipt.read_text());expected=build['executable_sha256'];assert H(a.operator.read_bytes())==sl['operator_sha256']=='cca3ed7e671b8397c3940921d9845399425fd2558cc62708941c00fc4b899950';assert H(a.executable.read_bytes())==expected;S=2**96;data=[(((13*i+7)%17)-8)*3*S//4096 for i in range(253952)];assert sum(v*v for v in data)<(2*S)**2

def encode(row):
 A=row['a'];B=row['b'];checks=0;ph=hashlib.sha256()
 def quant(x):
  nonlocal checks
  n=(x*2**128).mid().floor().unique_fmpz();assert n is not None;n=int(n);assert abs(x-arb(n)/2**128)<arb(1)/2**127;checks+=1;ph.update(n.to_bytes(17,'little',signed=True));return n
 if row['mode']=='zero':y=[v*2**50 for v in A]*4096
 else:
  y=[]
  for j in range(4096):
   t=arb(j*row['frequency_integer'])/2**41;c=quant(t.cos());s=quant(t.sin())
   y.extend(((u*c-v*s)//2**78 if row['mode']=='u'else(u*s+v*c)//2**78)for u,v in zip(A,B))
 assert len(y)==253952 and sum(v*v for v in y)<(3*S)**2
 z=sum(v*w for v,w in zip(y,data));return y,checks,ph.hexdigest(),z

def action(row,encoded):
 y,checks,phasehash,z=encoded
 assert H(a.executable.read_bytes())==expected and H(a.operator.read_bytes())==sl['operator_sha256']
 with tempfile.TemporaryDirectory(prefix='ud-frame-')as d:
  inp=Path(d)/'input.txt';out=Path(d)/'output.txt';txt=''.join(str(v)+'\n'for v in y);inp.write_text(txt)
  p=subprocess.run([str(a.executable),str(a.operator),'adjoint',str(inp),str(out)],capture_output=True,text=True);assert p.returncode==0,p.stderr;vals=list(map(int,out.read_text().split()));assert len(vals)==2640 and sum(v*v for v in vals)<(3*S)**2
 raw=b''.join(v.to_bytes(16,'little',signed=True)for v in vals);name=f'row_{row["column"]:04d}.i128.gz';packed=gzip.compress(raw,compresslevel=9,mtime=0);(a.out/name).write_bytes(packed)
 return {'column':row['column'],'mode':row['mode'],'frequency_integer':row['frequency_integer'],'phase_enclosure_checks':checks,'phase_table_sha256':phasehash,'input_text_sha256':H(txt.encode()),'output_row_file':name,'output_row_sha256':H(packed),'output_decoded_sha256':H(raw),'rhs_dot_integer':str(z),'rhs_dot_denominator_power2':192,'state_integer_scale_bits':96,'native_executable_sha256':expected,'status':'PASS_ACTUAL_SOURCE_ADJOINT_PARTIAL_FRAME_ROW'}
rows=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=4)as pool:
 for i in range(0,len(sl['columns']),4):
  jobs=[]
  for row in sl['columns'][i:i+4]:jobs.append(pool.submit(action,row,encode(row)))
  for job in jobs:
   r=job.result();rows.append(r);print('constructed',r['column'],flush=True)
result={'status':'PASS_PARTIAL16_SOURCE_FRAME_CONSTRUCTION','rows':rows,'actual_rows_constructed':len(rows),'full_required_rows':1999,'full_frame_status':'NOT_CONSTRUCTED_HOLD','partial_inverse_status':'CHECKED_SEPARATELY','trial_slice_sha256':H(a.slice.read_bytes()),'build_receipt_sha256':H(a.build_receipt.read_bytes()),'operator_sha256':sl['operator_sha256'],'data_rule':'3*(((13i+7)mod17)-8)/4096','data_norm_squared_integer':str(sum(v*v for v in data)),'data_scale_bits':96,'precision_bits':192,'physical_promotion':0,'external_promotion_review':'PENDING'};(a.out/'PARTIAL_FRAME.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
