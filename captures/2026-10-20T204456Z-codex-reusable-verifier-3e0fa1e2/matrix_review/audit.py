"""Independent generic exact statistic audit: bounded all-entry CRT plus scalar identities."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,ast,gzip,hashlib,json,math,re,resource,time,zipfile
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from flint import fmpz_mat
P=Path(__file__).resolve().parent
STAT=('M','K','A','B','E','H')

def need(ok,why):
 if not ok:raise ValueError(why)
def sha(path):
 h=hashlib.sha256()
 with Path(path).open('rb')as stream:
  for b in iter(lambda:stream.read(1048576),b''):h.update(b)
 return h.hexdigest()
def pair(x):return[str(x.numerator),str(x.denominator)]
def fraction(x):
 need(type(x)is list and len(x)==2,'rational pair');need(all(type(v)is str and re.fullmatch('-?[0-9]+',v)for v in x),'string rational integers');n,d=map(int,x);need(d>0,'positive rational denominator');return F(n,d)
def unique(pairs):
 d={}
 for k,v in pairs:need(k not in d,'duplicate JSON key');d[k]=v
 return d
def parse_json(data):return json.loads(data,object_pairs_hook=unique,parse_constant=lambda x:(_ for _ in()).throw(ValueError('nonfinite JSON')))
def json_file(path,limit):need(Path(path).stat().st_size<=limit,'JSON size limit');return parse_json(Path(path).read_bytes())
def keys(d,want):need(type(d)is dict and set(d)==set(want),'exact schema keys')
def integer(x,low,high):need(type(x)is int and low<=x<=high,'integer/profile range');return x
def digest(x):need(type(x)is str and re.fullmatch('[0-9a-f]{64}',x),'SHA256 syntax');return x

def clean(path):
 p=Path(os.path.abspath(path))
 for q in(p,*p.parents):need(not q.is_symlink(),'symlink component')
 return p

def input_path(root,value):
 need(type(value)is str and value and '\\'not in value and '\x00'not in value,'relative path syntax');r=Path(value);need(not r.is_absolute()and'..'not in r.parts,'input path escape');p=clean(root/r);need(p.is_relative_to(root)and p.is_file(),'missing/escaped input');return p

def read_header(stream,total,dtype,profile):
 need(stream.read(6)==b'\x93NUMPY','NPY magic');v=stream.read(2);need(v in[b'\x01\x00',b'\x02\x00',b'\x03\x00'],'NPY version');width=2 if v==b'\x01\x00'else 4;raw=stream.read(width);need(len(raw)==width,'NPY header length');size=int.from_bytes(raw,'little');need(size<=profile['max_header_bytes'],'NPY header resource');raw=stream.read(size);need(len(raw)==size,'NPY truncated header');meta=ast.literal_eval(raw.decode('utf8'if v==b'\x03\x00'else'latin1'));keys(meta,['descr','shape','fortran_order']);need(meta['descr']==dtype and type(meta['fortran_order'])is bool,'NPY dtype/order');shape=meta['shape'];need(type(shape)is tuple and 1<=len(shape)<=2 and all(type(x)is int and 1<=x<=profile['max_m']for x in shape),'NPY shape');payload=math.prod(shape)*8;need(payload<=profile['max_entry_bytes']and stream.tell()+payload==total,'NPY payload/trailing bytes');return shape

def npz_headers(path,expected,profile):
 with zipfile.ZipFile(path)as z:
  infos=z.infolist();need(len(infos)==len(expected)and{e.filename for e in infos}==set(expected),'NPZ exact nonduplicate entries');need(sum(e.file_size for e in infos)<=profile['max_file_bytes'],'NPZ expanded total');out={}
  for e in infos:
   need(e.file_size<=profile['max_entry_bytes']and not(e.flag_bits&1)and e.compress_type in[0,8],'NPZ encoding/resource')
   with z.open(e)as stream:out[e.filename]=read_header(stream,e.file_size,expected[e.filename],profile)
  return out

def encode(x,profile):
 x=np.asarray(x);need(x.dtype==np.float64 and np.isfinite(x).all(),'finite binary64 factor');ratios=[float(v).as_integer_ratio()for v in x.flat];b=max(d.bit_length()-1 for _,d in ratios);need(b<=profile['max_denominator_bits'],'factor denominator resource');values=[(n*(1<<b))//d for n,d in ratios];need(all(abs(z).bit_length()<=profile['max_encoded_integer_bits']for z in values),'factor integer resource');return np.array(values,dtype=object).reshape(x.shape),b

def intake(manifest,contract):
 profile=contract['profile'];manifest=clean(manifest);need(manifest.is_file(),'manifest missing');spec=json_file(manifest,65536);mh=sha(manifest);keys(spec,['schema_version','record','svd','left_chunks']);need(spec['schema_version']=='1.0','manifest version');keys(spec['record'],['path','sha256','payload_sha256','dyadic_exponent']);keys(spec['svd'],['path','sha256']);bN=integer(spec['record']['dyadic_exponent'],0,profile['max_denominator_bits']);digest(spec['record']['payload_sha256']);chunks=spec['left_chunks'];need(type(chunks)is list and 1<=len(chunks)<=profile['max_m'],'left chunk count')
 for c in chunks:keys(c,['path','sha256','start','stop']);integer(c['start'],0,profile['max_m']);integer(c['stop'],1,profile['max_m'])
 entries=[spec['record'],spec['svd'],*chunks];paths=[];total=0
 for e in entries:
  path=input_path(manifest.parent,e['path']);digest(e['sha256']);size=path.stat().st_size;total+=size;need(size<=profile['max_file_bytes']and total<=profile['max_total_bytes'],'input bytes resource');need(sha(path)==e['sha256'],'input SHA mismatch');paths.append(path)
 need(len(set(paths))==len(paths)and manifest not in paths,'duplicate input paths')
 with paths[0].open('rb')as stream:shape=read_header(stream,paths[0].stat().st_size,'<i8',profile)
 need(len(shape)==2,'projected record matrix');m,n=shape;need(2<=n<=min(m,profile['max_n']),'record dimension resource');h=npz_headers(paths[1],{'singular.npy':'<f8','right_transpose.npy':'<f8'},profile);need(h=={'singular.npy':(n,),'right_transpose.npy':(n,n)},'SVD shapes')
 shapes=[];previous=0
 for c,path in zip(chunks,paths[2:]):
  need(c['start']==previous and c['start']<c['stop']<=m,'ordered complete left intervals');shape=npz_headers(path,{'basis.npy':'<f8'},profile)['basis.npy'];need(len(shape)==2 and shape[0]==c['stop']-c['start']and shape[1]<n,'left chunk shapes');shapes.append(shape);previous=c['stop']
 need(previous==m,'left coverage');N=np.load(paths[0],mmap_mode='r',allow_pickle=False);need(N.dtype==np.dtype('<i8')and N.shape==(m,n),'loaded record shape/type');ph=hashlib.sha256(np.asarray(N,dtype='<i8').tobytes(order='C')).hexdigest();need(ph==spec['record']['payload_sha256'],'record payload hash')
 with np.load(paths[1],allow_pickle=False)as z:s=z['singular'].copy();vt=z['right_transpose'].copy()
 need(s.dtype==vt.dtype==np.float64 and np.isfinite(s).all()and np.isfinite(vt).all()and np.all(s>=0)and np.all(s[:-1]>=s[1:]),'SVD numeric values');singular=[F(*float(v).as_integer_ratio())for v in s];cut=F(1,1<<contract['cutoff_denominator_bits']);need(cut not in singular,'strict cutoff equality');q=sum(x>cut for x in singular);need(1<=q<n and all(c[1]==q for c in shapes),'independent strict saved rank/chunk width')
 U=np.empty((m,q),dtype=np.float64)
 for c,path in zip(chunks,paths[2:]):
  with np.load(path,allow_pickle=False)as z:block=z['basis'];need(block.dtype==np.float64 and np.isfinite(block).all(),'left values');U[c['start']:c['stop']]=block
 Ui,bU=encode(U,profile);Vi,bV=encode(vt[:q].T.copy(),profile);Di,bD=encode(vt[q:].T.copy(),profile);si,bS=encode(s[:q].copy(),profile)
 return {'manifest':manifest,'manifest_sha256':mh,'entries':entries,'paths':paths,'N':N,'Ui':Ui,'Vi':Vi,'Di':Di,'si':si,'s':singular,'m':m,'n':n,'q':q,'bN':bN,'bU':bU,'bV':bV,'bD':bD,'bS':bS,'payload_sha256':ph,'total_input_bytes':total}

def unchanged(data):return sha(data['manifest'])==data['manifest_sha256']and all(sha(p)==e['sha256']for p,e in zip(data['paths'],data['entries']))
def numeric_string(value):need(type(value)is str and re.fullmatch('-?[0-9]+',value)and len(value)<=1300,'bounded decimal integer');v=int(value);need(abs(v).bit_length()<=4096,'witness integer resource');return v

def decode_matrix(row,shape,symmetric):
 keys(row,['shape','storage','values']);r,c=shape;need(type(row['shape'])is list and len(row['shape'])==2 and all(type(z)is int for z in row['shape'])and row['shape']==[r,c]and row['storage']==('upper'if symmetric else'full'),'matrix codec shape/storage');values=row['values'];need(type(values)is list and len(values)==(r*(r+1)//2 if symmetric else r*c),'packed entry count');out=np.empty((r,c),dtype=object);k=0
 for i in range(r):
  for j in range(i if symmetric else 0,c):
   v=numeric_string(values[k]);k+=1;out[i,j]=v
   if symmetric:out[j,i]=v
 return out

def witness(path,data):
 need(path.stat().st_size<=67108864,'compressed witness resource')
 with gzip.open(path,'rb')as stream:raw=stream.read(134217729)
 need(len(raw)<=134217728,'expanded witness resource');w=parse_json(raw);keys(w,['schema_version','dimensions','exponents','singular_integers','matrices','trace_terms','exact','metrics']);need(all(type(z)is int for z in w['dimensions'].values())and all(type(z)is int for z in w['exponents'].values()),'typed witness dimensions/exponents');need(w['schema_version']=='1.0'and w['dimensions']=={k:data[k]for k in['m','n','q']}and w['exponents']=={k:data[k]for k in['bN','bU','bV','bD','bS']},'witness independent dimensions/encodings');need([numeric_string(v)for v in w['singular_integers']]==list(map(int,data['si'])),'independent encoded singular values');keys(w['matrices'],STAT);n,q=data['n'],data['q'];d=n-q;shapes={'M':(n,n),'K':(n,q),'A':(q,q),'B':(q,q),'E':(d,d),'H':(d,d)};mat={name:decode_matrix(w['matrices'][name],shapes[name],name!='K')for name in STAT};return w,mat

def maxabs(a):return max(abs(int(x))for x in np.asarray(a).flat)
def prime(p):return p>=2 and(p==2 or(p%2==1 and all(p%d for d in range(3,math.isqrt(p)+1,2))))
def primes_for(B):
 result=[];product=1;p=(1<<24)-1
 while not result or product<=2*B:
  while p>=3 and not prime(p):p-=2
  need(p>=3,'prime supply');result.append(p);product*=p;p-=2
 return result,product

def dot_bound(inner,p):
 bound=inner*(p-1)**2;need(0<inner<=8191 and 2<=p<(1<<24)and bound<(1<<63),'int64 modular dot overflow/profile');return bound

def mod(a,p):return np.fromiter((int(v)%p for v in np.asarray(a).flat),dtype=np.int64,count=np.asarray(a).size).reshape(np.asarray(a).shape)
def plans(data,mat):
 m,n=data['m'],data['n'];x=maxabs(data['N']);u=maxabs(data['Ui']);v=maxabs(data['Vi']);d=maxabs(data['Di']);M=maxabs(mat['M']);true={'M':m*x*x,'K':m*x*u,'A':m*u*u,'B':n*v*v,'E':n*d*d+(1<<(2*data['bD'])),'H':n*n*M*d*d};out={}
 for key in STAT:
  saved=maxabs(mat[key]);B=true[key]+saved;ps,P=primes_for(B);out[key]={'true_entry_absolute_bound':str(true[key]),'saved_entry_max_abs':str(saved),'difference_bound':str(B),'primes':ps,'CRT_product':str(P),'magnitude_possible':saved<=true[key],'bound_dependency':'M exact CRT identity required'if key=='H'else'original integer/independent dyadic inputs','checks':[]}
 return out

def check_residue(actual,saved,p,inner):
 expected=mod(saved,p);same=actual==expected;where=np.argwhere(~same);count=int(np.count_nonzero(same));return {'prime':p,'trial_division_prime_proved':prime(p),'dot_inner_lengths':inner,'maximum_int64_dot_sums':[str(dot_bound(z,p))for z in inner],'int64_limit_exclusive':str(1<<63),'entries':actual.size,'matching_entries':count,'all_entries_match':count==actual.size,'computed_residue_sha256':hashlib.sha256(actual.astype('<i8').tobytes()).hexdigest(),'supplied_residue_sha256':hashlib.sha256(expected.astype('<i8').tobytes()).hexdigest(),'first_mismatch':None if len(where)==0 else list(map(int,where[0]))}

def finalize_plan(plan):
 ps=plan['primes'];P=int(plan['CRT_product']);B=int(plan['difference_bound']);need(len(ps)==len(set(ps))and all(prime(p)for p in ps)and P==math.prod(ps)and P>2*B,'sufficient distinct-prime product');need([x['prime']for x in plan['checks']]==ps,'all selected primes checked');need(plan['magnitude_possible']and all(x['all_entries_match']for x in plan['checks']),'matrix magnitude/residue mismatch');plan['status']='PASS_EXACT_ALL_ENTRY_CRT'

def matrices(data,mat):
 out=plans(data,mat);N,U,V,D=data['N'],data['Ui'],data['Vi'],data['Di'];m,n=data['m'],data['n'];initial=STAT[:-1];union=sorted(set(p for k in initial for p in out[k]['primes']if out[k]['magnitude_possible']),reverse=True)
 for p in union:
  active=[k for k in initial if out[k]['magnitude_possible']and p in out[k]['primes']];Nm=np.remainder(N,p).astype(np.int64,copy=False)if any(k in active for k in['M','K'])else None;Um=mod(U,p)if any(k in active for k in['K','A'])else None;Vm=mod(V,p)if'B'in active else None;Dm=mod(D,p)if'E'in active else None
  for k in active:
   inner=m if k in['M','K','A']else n;dot_bound(inner,p)
   if k=='M':actual=np.remainder(Nm.T@Nm,p)
   elif k=='K':actual=np.remainder(Nm.T@Um,p)
   elif k=='A':actual=np.remainder(Um.T@Um,p)
   elif k=='B':actual=np.remainder(Vm.T@Vm,p)
   else:
    actual=np.remainder(Dm.T@Dm,p)
    for j in range(n-data['q']):actual[j,j]-=pow(2,2*data['bD'],p)
    actual=np.remainder(actual,p)
   out[k]['checks'].append(check_residue(actual,mat[k],p,[inner]))
 for k in initial:
  try:finalize_plan(out[k])
  except Exception as exc:out[k].update(status='HOLD_MATRIX_CRT',reason=str(exc))
 if out['M']['status']!='PASS_EXACT_ALL_ENTRY_CRT':out['H'].update(status='HOLD_UNVERIFIED_M_DEPENDENCY')
 elif not out['H']['magnitude_possible']:out['H'].update(status='HOLD_MATRIX_MAGNITUDE')
 else:
  for p in out['H']['primes']:
   dot_bound(n,p);Mm=mod(mat['M'],p);Dm=mod(D,p);product=np.remainder(Mm@Dm,p);actual=np.remainder(Dm.T@product,p);out['H']['checks'].append(check_residue(actual,mat['H'],p,[n,n]))
  try:finalize_plan(out['H'])
  except Exception as exc:out['H'].update(status='HOLD_MATRIX_CRT',reason=str(exc))
 return out

def norm_square(M,b):return F(sum(int(v)**2 for v in M.flat),1<<(2*b))
def scalar_statistics(data,mat):
 A=mat['A'].copy();B=mat['B'].copy();q=data['q']
 for j in range(q):A[j,j]-=1<<(2*data['bU']);B[j,j]-=1<<(2*data['bV'])
 exact={'a_squared':norm_square(A,2*data['bU']),'b_squared':norm_square(B,2*data['bV']),'eta_squared':norm_square(mat['E'],2*data['bD']),'r_fourth':norm_square(mat['H'],2*(data['bN']+data['bD']))}
 V=data['Vi'];s=list(map(int,data['si']));n=data['n'];cross=sum(int(mat['K'][i,j])*int(V[i,j])*s[j]for i in range(n)for j in range(q))
 # Different exact association from producer: build VV^T, then symmetric contraction with M.
 vm=fmpz_mat(V.tolist());C=vm*vm.transpose();trace=sum(int(mat['M'][i,i])*int(C[i,i])for i in range(n))+2*sum(int(mat['M'][i,j])*int(C[i,j])for i in range(n)for j in range(i+1,n))
 udiag=sum(s[j]*s[j]*int(mat['A'][j,j])for j in range(q));vdiag=sum(s[j]*s[j]*int(mat['B'][j,j])for j in range(q));ksquare=sum(int(v)**2 for v in mat['K'].flat)
 kF=max(data['bN']+data['bV'],data['bU']+data['bS']);af=1<<(kF-data['bN']-data['bV']);bf=1<<(kF-data['bU']-data['bS']);kG=max(data['bN']+data['bU'],data['bV']+data['bS']);ag=1<<(kG-data['bN']-data['bU']);bg=1<<(kG-data['bV']-data['bS']);exact.update(f_squared=F(af*af*trace-2*af*bf*cross+bf*bf*udiag,1<<(2*kF)),g_squared=F(ag*ag*ksquare-2*ag*bg*cross+bg*bg*vdiag,1<<(2*kG)))
 need(all(x>=0 for x in exact.values()),'negative quadratic norm identity');return exact,{'cross':cross,'trace':trace,'udiag':udiag,'vdiag':vdiag,'ksquare':ksquare}

def verify_ceil(value,square,power,bits):
 need(value>=0 and square>=0 and(value*(1<<bits)).denominator==1,'nonnegative dyadic grid bound');need(value**power>=square and(value==0 or(value-F(1,1<<bits))**power<square),'minimal exact root grid enclosure')

def derive(metric,s,q,contract):
 a,b,e,r,f,g=[metric[k]for k in['a','b','eta','r','f','g']];gates={'left_Gram_full_rank':a<1,'retained_right_Gram_full_rank':b<1,'discarded_right_Gram_full_rank':e<1};bounds={}
 if all(gates.values()):
  tail=r/(1-e);comp=(s[0]*(a/(2-a)+b/(2-b))+f)/(1-b);off=max(f/(1-b),g/(1-a));eps=comp+off;low=s[q-1]-eps;bounds={'direct_tail_upper':tail,'compression_upper':comp,'offdiagonal_upper':off,'retained_abs_error_upper':eps,'discarded_abs_error_upper':max(tail,s[q]),'full_abs_error_upper':max(eps,tail,s[q]),'matching_gap':s[q-1]-comp-tail-off,'ambient_sigma_q_lower':low}
  if low>0:bounds['ambient_leading_condition_upper']=(s[0]+eps)/low
  cut=F(1,1<<contract['cutoff_denominator_bits']);gates.update(strict_leading_block_matching=bounds['matching_gap']>0,tail_below_cutoff=tail<cut,retained_lower_above_cutoff=low>cut,full_abs_error_below_gate=bounds['full_abs_error_upper']<F(1,1<<contract['accuracy_denominator_bits']))
 return gates,bounds

def scalar_audit(data,mat,w,cert,contract):
 exact,terms=scalar_statistics(data,mat);keys(w['exact'],exact);need(all(fraction(w['exact'][k])==v for k,v in exact.items()),'exact norm identities differ');keys(w['trace_terms'],terms);need(all(numeric_string(w['trace_terms'][k])==v for k,v in terms.items()),'independent trace contractions differ');keys(w['metrics'],['a','b','eta','r','f','g']);metric={k:fraction(v)for k,v in w['metrics'].items()}
 for k,name,power in[('a','a_squared',2),('b','b_squared',2),('eta','eta_squared',2),('r','r_fourth',4),('f','f_squared',2),('g','g_squared',2)]:verify_ceil(metric[k],exact[name],power,contract['root_ceiling_bits'])
 need({k:fraction(v)for k,v in cert['metrics'].items()}==metric,'certificate metrics differ');gates,bounds=derive(metric,data['s'],data['q'],contract);gates['input_bytes_unchanged']=unchanged(data);need(cert['gates']==gates and all(type(x)is bool for x in cert['gates'].values()),'fresh gates differ');need({k:fraction(v)for k,v in cert['bounds'].items()}==bounds,'derived bounds differ');status='CERTIFIED_FINITE_SUPPLIED_RECORD'if all(gates.values())else'HOLD_NUMERICAL';need(cert['status']==status,'reported acceptance differs');return {'exact':{k:pair(v)for k,v in exact.items()},'trace_terms':{k:str(v)for k,v in terms.items()},'metrics':{k:pair(v)for k,v in metric.items()},'bounds':{k:pair(v)for k,v in bounds.items()},'gates':gates,'independently_derived_status':status,'minimal180bit_root_bounds_verified':True}

def guard(arg,inputs=()):
 lex=clean(arg);out=lex.resolve();protected={P.absolute(),P.resolve()}
 for z in(P,*P.parents):
  if(z/'MANIFEST.json').is_file():protected.update((z.absolute(),z.resolve()))
 for q in(lex,out):need(all(q!=z and z not in q.parents and q not in z.parents for z in protected),'protected output');need(all(q!=z and q not in z.parents for z in inputs),'output overlaps source')
 need(not out.exists(),'new output required');return out

def sealed():
 f=json_file(P/'FREEZE.json',1048576)
 for name,h in f['files'].items():need(sha(P/name)==h,'audit source changed '+name)
 return json_file(P/'PROFILE.json',65536)

def run(manifest,wfile,cfile,out):
 start=time.perf_counter();contract=sealed();data=intake(manifest,contract);need(not out.exists(),'new output');out=guard(out,[data['manifest'],*data['paths'],wfile,cfile]);out.mkdir(parents=True,exist_ok=False);wh,ch=sha(wfile),sha(cfile);report={'status':'HOLD_MATRIX_OR_SCALAR_AUDIT','manifest_sha256':data['manifest_sha256'],'witness_sha256':wh,'producer_certificate_sha256':ch,'dimensions':{k:data[k]for k in['m','n','q']},'exponents':{k:data[k]for k in['bN','bU','bV','bD','bS']},'record_payload_sha256':data['payload_sha256']}
 try:
  w,mat=witness(wfile,data);cert=json_file(cfile,1048576);need(cert['new_estimator_calls']==0 and cert['prior_certificate_inputs']==0 and cert['physical_promotion']==0 and cert['algebraic_rank_q_claimed']is False and cert['full_matrix_condition_claimed']is False and cert['all_input_backend_conformance']=='OPEN','certificate scope flags');need(cert['manifest_sha256']==data['manifest_sha256']and cert['record_payload_sha256']==data['payload_sha256']and cert['witness_sha256']==wh and cert['protocol_sha256']==sha(P/'PROFILE.json')and cert['dimensions']==report['dimensions'],'certificate input/contract identity');stats=matrices(data,mat);report['matrix_checks']=stats;need(all(x['status']=='PASS_EXACT_ALL_ENTRY_CRT'for x in stats.values()),'one matrix identity failed');scalars=scalar_audit(data,mat,w,cert,contract);need(unchanged(data)and sha(wfile)==wh and sha(cfile)==ch,'input/witness mutation');report.update(status='PASS_ALL_SIX_EXACT_CRT_AND_FRESH_SCALAR_CERTIFICATE',scalar_checks=scalars)
 except Exception as exc:report['error']={'type':type(exc).__name__,'message':str(exc)}
 sealed();report.update(audit_freeze_sha256=sha(P/'FREEZE.json'),input_scope='Explicit supplied manifest bytes only; acquisition/projection lineage not established',prior_certificate_mathematical_premises=0,new_estimator_calls=0,new_raw_records=0,new_factor_or_matrix_copies=0,same_team_review=True,external_review='PENDING',physical_promotion=0)
 with(out/'CERTIFICATE.json').open('x')as f:json.dump(report,f,indent=2);f.write('\n')
 with(out/'RESOURCE.json').open('x')as f:json.dump({'elapsed_seconds':time.perf_counter()-start,'process_peak_RSS_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},f,indent=2);f.write('\n')
 print(json.dumps({'status':report['status'],'dimensions':report['dimensions'],'primes':{k:len(v['primes'])for k,v in report.get('matrix_checks',{}).items()},'error':report.get('error')}),flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--manifest',required=True);p.add_argument('--witness',required=True);p.add_argument('--certificate',required=True);p.add_argument('--out',required=True);a=p.parse_args();run(clean(a.manifest),clean(a.witness),clean(a.certificate),guard(a.out))
