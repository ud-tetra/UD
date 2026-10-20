"""Independent six-matrix scalar/trace proof review; no prior certificates."""
from pathlib import Path
from fractions import Fraction as F
import argparse,gzip,hashlib,json
import numpy as np
P=Path(__file__).resolve().parent;W=P.parent;PKG=W/'c20_verifier'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def f(x):return F(int(x[0]),int(x[1]))
def pair(x):return[str(x.numerator),str(x.denominator)]
def unpack(j):
 m,n=j['shape'];sym=j['storage']=='upper';v=list(map(int,j['values']));A=[[0]*n for _ in range(m)];p=0
 assert j['storage']in('upper','full') and (not sym or m==n)
 for i in range(m):
  for k in range(i if sym else 0,n):
   x=v[p];p+=1;A[i][k]=x
   if sym:A[k][i]=x
 assert p==len(v)
 return A

def norm2(A):return sum(x*x for row in A for x in row)
def symmetric_sq(j,shift):
 assert j['storage']=='upper';m,n=j['shape'];assert m==n;v=iter(map(int,j['values']));total=0
 for i in range(m):
  for k in range(i,n):
   x=next(v)-(shift if i==k else 0);total+=(1 if i==k else 2)*x*x
 return total

def encode_exact(x):
 ratios=[float(v).as_integer_ratio()for v in x.flat];b=max(d.bit_length()-1 for _,d in ratios);values=[(n*2**b)//d for n,d in ratios];return np.array(values,dtype=object).reshape(x.shape).tolist(),b

def run(case,manifest,out):
 checks=[]
 def ck(n,b):
  assert b,n
  checks.append({'id':n,'pass':True})
 seal=read(PKG/'SEAL.json');protocol=read(PKG/'PROTOCOL.json')
 for n,h in seal['files'].items():ck('sealed_package_'+n,sha(PKG/n)==h)
 d=W/'c20_primary'/case;cert=read(d/'CERTIFICATE.json');body=gzip.decompress((d/'WITNESS.json.gz').read_bytes());wit=json.loads(body)
 ck('canonical_witness_payload',json.dumps(wit,sort_keys=True,separators=(',',':')).encode()==body)
 ck('compressed_witness_hash',sha(d/'WITNESS.json.gz')==cert['witness_sha256'])
 spec=read(manifest);base=manifest.parent;ck('explicit_manifest_hash',sha(manifest)==cert['manifest_sha256'])
 for row in [spec['record'],spec['svd'],*spec['left_chunks']]:ck('explicit_input_hash_'+row['path'],sha(base/row['path'])==row['sha256'])
 N=np.load(base/spec['record']['path'],allow_pickle=False,mmap_mode='r');m,n=N.shape
 h=hashlib.sha256()
 for begin in range(0,m,512):h.update(np.asarray(N[begin:begin+512],dtype='<i8').tobytes())
 ck('supplied_record_payload_identity',h.hexdigest()==cert['record_payload_sha256']==spec['record']['payload_sha256'])
 with np.load(base/spec['svd']['path'],allow_pickle=False)as data:s=data['singular'];vt=data['right_transpose']
 sf=[F.from_float(float(x))for x in s];tau=F(1,2**protocol['cutoff_denominator_bits']);accuracy=F(1,2**protocol['accuracy_denominator_bits']);q=sum(x>tau for x in sf)
 ck('complete_saved_singular_shape_and_domain',s.shape==(n,) and np.isfinite(s).all() and sf==sorted(sf,reverse=True) and min(sf)>=0 and tau not in sf and 1<=q<n<=m)
 ck('dimensions_bound_to_supplied_record',wit['dimensions']==cert['dimensions']=={'m':m,'n':n,'q':q})
 Vi,bV=encode_exact(vt[:q].T);si,bS=encode_exact(s[:q]);si=list(map(int,si));ex=wit['exponents'];bN=ex['bN'];bU=ex['bU'];bD=ex['bD']
 ck('independent_V_and_s_integer_encodings',bV==ex['bV'] and bS==ex['bS'] and si==list(map(int,wit['singular_integers'])))
 ck('record_exponent_from_manifest',bN==spec['record']['dyadic_exponent'])
 mats={k:unpack(v)for k,v in wit['matrices'].items()};M,K,A,B,E,H=[mats[k]for k in ['M','K','A','B','E','H']]
 ck('all6_matrix_shapes',len(M)==n and all(len(x)==n for x in M) and len(K)==n and all(len(x)==q for x in K) and len(A)==len(B)==q and all(len(x)==q for x in A+B) and len(E)==len(H)==n-q and all(len(x)==n-q for x in E+H))
 ad=[row[:]for row in A];bd=[row[:]for row in B]
 for j in range(q):ad[j][j]-=2**(2*bU);bd[j][j]-=2**(2*bV)
 rawsq={'a_squared':symmetric_sq(wit['matrices']['A'],2**(2*bU)),'b_squared':symmetric_sq(wit['matrices']['B'],2**(2*bV)),'eta_squared':symmetric_sq(wit['matrices']['E'],0),'r_fourth':symmetric_sq(wit['matrices']['H'],0)}
 for key,mat in [('a_squared',ad),('b_squared',bd),('eta_squared',E),('r_fourth',H)]:ck('packed_offdiagonals_twice_'+key,rawsq[key]==norm2(mat))
 # Independent symmetric quadratic contraction, avoiding the producer's M*Vi route.
 trace=sum(M[i][i]*sum(x*x for x in Vi[i])for i in range(n))
 trace+=2*sum(M[i][k]*sum(x*y for x,y in zip(Vi[i],Vi[k]))for i in range(n)for k in range(i+1,n))
 cross=sum(K[i][j]*Vi[i][j]*si[j]for i in range(n)for j in range(q))
 udiag=sum(si[j]**2*A[j][j]for j in range(q));vdiag=sum(si[j]**2*B[j][j]for j in range(q));ksquare=norm2(K)
 for key,x in [('trace',trace),('cross',cross),('udiag',udiag),('vdiag',vdiag),('ksquare',ksquare)]:ck('independent_trace_term_'+key,int(wit['trace_terms'][key])==x)
 kF=max(bN+bV,bU+bS);alphaF=2**(kF-bN-bV);betaF=2**(kF-bU-bS)
 kG=max(bN+bU,bV+bS);alphaG=2**(kG-bN-bU);betaG=2**(kG-bV-bS)
 fnum=alphaF**2*trace-2*alphaF*betaF*cross+betaF**2*udiag;gnum=alphaG**2*ksquare-2*alphaG*betaG*cross+betaG**2*vdiag
 ck('exact_residual_square_numerators_nonnegative',fnum>=0 and gnum>=0)
 exact={'a_squared':F(rawsq['a_squared'],2**(4*bU)),'b_squared':F(rawsq['b_squared'],2**(4*bV)),'eta_squared':F(rawsq['eta_squared'],2**(4*bD)),'r_fourth':F(rawsq['r_fourth'],2**(4*(bN+bD))),'f_squared':F(fnum,2**(2*kF)),'g_squared':F(gnum,2**(2*kG))}
 for key,value in exact.items():ck('exact_scalar_norm_identity_'+key,f(wit['exact'][key])==value)
 metrics={k:f(v)for k,v in cert['metrics'].items()};step=F(1,2**protocol['root_ceiling_bits'])
 for key,eq,power in [('a','a_squared',2),('b','b_squared',2),('eta','eta_squared',2),('r','r_fourth',4),('f','f_squared',2),('g','g_squared',2)]:
  upper=metrics[key];v=exact[eq];ck('minimal180_dyadic_wrapper_'+key,upper==f(wit['metrics'][key]) and upper>=0 and (upper/step).denominator==1 and upper**power>=v and(upper==0 and v==0 or upper>0 and(upper-step)**power<v))
 a,b,eta,r,forward,adjoint=[metrics[k]for k in ['a','b','eta','r','f','g']]
 ck('Gram_fullrank_domains',0<=a<1 and 0<=b<1 and 0<=eta<1)
 tail=r/(1-eta);c=(sf[0]*(a/(2-a)+b/(2-b))+forward)/(1-b);e=max(forward/(1-b),adjoint/(1-a));eps=c+e;lower=sf[q-1]-eps;gap=lower-tail
 expected={'direct_tail_upper':tail,'compression_upper':c,'offdiagonal_upper':e,'retained_abs_error_upper':eps,'discarded_abs_error_upper':max(tail,sf[q]),'full_abs_error_upper':max(eps,tail,sf[q]),'matching_gap':gap,'ambient_sigma_q_lower':lower,'ambient_leading_condition_upper':(sf[0]+eps)/lower}
 ck('all9_bound_fields',set(expected)==set(cert['bounds']))
 for key,value in expected.items():ck('independent_rational_bound_'+key,f(cert['bounds'][key])==value)
 gates={'left_Gram_full_rank':a<1,'retained_right_Gram_full_rank':b<1,'discarded_right_Gram_full_rank':eta<1,'strict_leading_block_matching':gap>0,'tail_below_cutoff':tail<tau,'retained_lower_above_cutoff':lower>tau,'full_abs_error_below_gate':expected['full_abs_error_upper']<accuracy,'input_bytes_unchanged':True}
 ck('all8_gates_true_and_equal',gates==cert['gates'] and all(gates.values()))
 ck('finite_supplied_record_scope',cert['prior_certificate_inputs']==cert['new_estimator_calls']==cert['physical_promotion']==0 and cert['status']=='CERTIFIED_FINITE_SUPPLIED_RECORD' and cert['all_input_backend_conformance']=='OPEN' and not cert['algebraic_rank_q_claimed'] and not cert['full_matrix_condition_claimed'] and cert['external_promotion_review']=='PENDING')
 ck('package_identity_bound',cert['seal_sha256']==sha(PKG/'SEAL.json') and cert['protocol_sha256']==sha(PKG/'PROTOCOL.json'))
 report={'case':case,'status':'PASS_INDEPENDENT_ACTUAL_SIX_MATRIX_SCALAR_TRACE_AND_BOUND_REVIEW','checks':checks,'check_count':len(checks),'dimensions':{'m':m,'n':n,'q':q},'independent_exact_norms':{k:pair(v)for k,v in exact.items()},'independent_metrics':{k:pair(v)for k,v in metrics.items()},'independent_bounds':{k:pair(v)for k,v in expected.items()},'source_sha256':{str(p.relative_to(W)):sha(p)for p in [d/'CERTIFICATE.json',d/'WITNESS.json.gz',manifest,PKG/'verifier.py',PKG/'PROTOCOL.json',PKG/'SEAL.json']},'matrix_product_identity_independently_rederived_here':False,'matrix_identity_scope':'Distinct all-entry exact CRT audit needed; these are independently checked scalar consequences of supplied sufficient-statistic matrices','prior_certificates_loaded':0,'new_fits':0,'input_stability_scope':'Own observed bytes plus producer before/after hashes, not a universal concurrent-mutation guarantee','physical_promotion':0}
 with out.open('x')as z:json.dump(report,z,indent=2);z.write('\n')
 print(json.dumps({'status':report['status'],'case':case,'checks':len(checks),'full_bound':float(expected['full_abs_error_upper']),'condition':float(expected['ambient_leading_condition_upper'])}),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--case',required=True);p.add_argument('--manifest',type=Path,required=True);p.add_argument('--out',type=Path,required=True);args=p.parse_args();run(args.case,args.manifest.resolve(),args.out)
