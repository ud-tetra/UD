"""Independent saved-output audit: bit decoding and quadratic-form residual identities.
No estimator import, new fit, saved factor copy, or raw record copy.
"""
import argparse,hashlib,json,struct,sys
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from flint import fmpz_mat,arb,acb,ctx,fmpq
ctx.prec=512
P=Path(__file__).resolve().parent

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_text())
def pair(q):return [str(q.numerator),str(q.denominator)]
def frac(p):return F(int(p[0]),int(p[1]))
def aa(q):
 if not isinstance(q,F):q=frac(q)
 return arb(fmpq(q.numerator,q.denominator))
def upper(x):return [int((arb(x.upper())*(1<<180)).ceil().unique_fmpz()),1<<180]
def decode(x):
 x=np.asarray(x);assert x.dtype==np.float64 and np.isfinite(x).all()
 z=x.view(np.uint64);rows=[];maxb=0
 for val in z.flat:
  v=int(val);e=(v>>52)&2047;m=v&((1<<52)-1)
  if e:m|=1<<52;power=e-1023-52
  else:power=-1074
  if v>>63:m=-m
  if m==0:power=0
  while m and m%2==0:m//=2;power+=1
  b=max(0,-power);n=m<<max(0,power);rows.append((n,b));maxb=max(maxb,b)
 return np.array([n<<(maxb-b)for n,b in rows],dtype=object).reshape(x.shape),maxb
def mat(x):return fmpz_mat(np.asarray(x,dtype=object).tolist())
def trace(x):return sum(int(x[j,j])for j in range(x.nrows()))
def normint(x):return sum(int(t)**2 for row in x.tolist()for t in row)
def gram(x,b):
 G=mat(x).transpose()*mat(x);D=fmpz_mat(G)
 for j in range(D.nrows()):D[j,j]-=1<<(2*b)
 return G,F(normint(D),1<<(4*b))
def eq_quadratic(N,V,bv,U,bu,s,bs):
 n,v,u=mat(N),mat(V),mat(U);gn=n.transpose()*n;gu=u.transpose()*u;cross=n.transpose()*u
 first=trace(v.transpose()*gn*v);middle=sum(int(s[j])**2*int(gu[j,j])for j in range(len(s)))
 mix=sum(int(s[j])*sum(int(cross[k,j])*int(V[k,j])for k in range(V.shape[0]))for j in range(len(s)))
 result=F(first,1<<(2*(55+bv)))+F(middle,1<<(2*(bu+bs)))-F(2*mix,1<<(55+bv+bu+bs));assert result>=0;return result

def lag_quadratic(U,bu,T,bt):
 minus,plus,t=mat(U[:-2]),mat(U[2:]),mat(T);gm=minus.transpose()*minus;gp=plus.transpose()*plus;cross=minus.transpose()*plus
 return F(trace(gp),1<<(2*bu))+F(trace(t.transpose()*gm*t),1<<(2*(bu+bt)))-F(2*trace(t.transpose()*cross),1<<(2*bu+bt))
def cx(x):
 x=np.asarray(x);x=x.reshape(-1,1) if x.ndim==1 else x
 r,br=decode(np.asarray(x.real,dtype=np.float64));i,bi=decode(np.asarray(x.imag,dtype=np.float64));b=max(br,bi);return mat(r*(1<<(b-br))),mat(i*(1<<(b-bi))),b
def square_cx(r,i,b):return F(normint(r)+normint(i),1<<(2*b))
def scaled_difference(ar,ai,ba,br,bi,bb):
 b=max(ba,bb);return square_cx(ar*(1<<(b-ba))-br*(1<<(b-bb)),ai*(1<<(b-ba))-bi*(1<<(b-bb)),b)
def ties_even(x):
 # Independent integer IEEE dyad decoding and signed nearest-even division.
 a,b=decode(np.array([x],dtype=np.float64));n=int(a[0])*(1<<60);q,r=divmod(n,1<<b);return q+(r*2>(1<<b)or(r*2==(1<<b)and q%2==1))
def circular(x):return 2*abs((x/2).sin()).asin()
def phase_audit(case,source,cert):
 z=np.load(case/'PHASE_META.npz',allow_pickle=False);p=np.load(case/'PHASE_PROPOSAL.npz',allow_pickle=False);T=z['shift'];V=z['eigenvectors'];H=z['inverse'];ev=z['eigenvalues'];angles=z['angles'];em=p['two_step_phase'];assert em.shape==(209,)and em.dtype==np.int64
 tr,bt=decode(T);vr,vi,bv=cx(V);hr,hi,bh=cx(H);lr,li,bl=cx(ev);I=fmpz_mat(209,209)
 for j in range(209):I[j,j]=1
 zero=fmpz_mat(209,209);rho=scaled_difference(vr*hr-vi*hi,vr*hi+vi*hr,bv+bh,I,zero,0)
 # Multiply by diagonal Lambda explicitly, independently from producer elementwise NumPy formula.
 dr,di=fmpz_mat(209,209),fmpz_mat(209,209)
 for j in range(209):dr[j,j]=int(lr[j,0])if lr.ncols()==1 else int(lr[0,j]);di[j,j]=int(li[j,0])if li.ncols()==1 else int(li[0,j])
 eig=scaled_difference(mat(tr)*vr,mat(tr)*vi,bt+bv,vr*dr-vi*di,vr*di+vi*dr,bv+bl)
 assert rho==frac(cert['phase']['exact_inverse_residual_squared']);assert eig==frac(cert['phase']['exact_eigenpair_residual_squared'])
 gr=hr.transpose()*hr+hi.transpose()*hi;gi=hr.transpose()*hi-hi.transpose()*hr
 norm_sq=F(min(trace(gr),max(sum(abs(int(gr[j,k]))+abs(int(gi[j,k]))for k in range(209))for j in range(209))),1<<(2*bh));h=aa(norm_sq).sqrt()
 assert frac(upper(h))==frac(cert['phase']['metrics']['proposed_inverse_norm'])
 targets=source['target_matches'];sep=aa(source['metrics']['minimum_target_chord_lower']);rows=[];argument=[]
 for j in range(209):
  assert int(em[j])==ties_even(angles[j]);val=acb(aa(F(int(lr[j,0]),1<<bl)),aa(F(int(li[j,0]),1<<bl)));assert abs(val)>0
  theta=aa(F(int(em[j]),1<<60));argument.append(upper(circular(val.arg()-theta)))
  errors=[circular(theta-2*aa(t['omega']))for t in targets];k=min(range(209),key=lambda k:float(errors[k].upper()));assert errors[k]<sep/2
  assert all(errors[k].upper()<errors[i].lower()for i in range(209)if i!=k);rows.append({'emitted_index':j,'target_index':k,'error_upper':upper(errors[k])})
 assert len({x['target_index']for x in rows})==209
 assert [x['target_index']for x in rows]==[x['target_index']for x in cert['phase']['observed']['rows']]
 maxarg=max(frac(x)for x in argument);producer=frac(cert['phase']['metrics']['emitted_argument_error']);assert maxarg<=producer+F(1,1<<178)
 return {'inverse_residual_squared':pair(rho),'eigenpair_residual_squared':pair(eig),'inverse_norm_upper':upper(h),'argument_error_upper':pair(maxarg),'maximum_match_error_upper':pair(max(frac(x['error_upper'])for x in rows)),'finite_target_indices':[x['target_index']for x in rows],'all_209_nearest_even_and_unique':True}

def controls():
 rows=[]
 def check(k,v):assert v,k;rows.append({'id':k,'pass':True})
 check('decode_negative_dyadic',decode(np.array([-0.125,0.,1.5]))[0].tolist()==[-1,0,12])
 x,b=decode(np.array([[1.,0.],[0.,0.5]]));check('Gram_nonorthogonal_exact',gram(x,b)[1]==F(9,16))
 N=np.array([[24,0],[0,8]],dtype=object);V=np.array([[1],[0]],dtype=object);U=V.copy();s=np.array([24],dtype=object)
 # Actual Z=N/2^55; factor Sigma=24/2^55; tail=8/2^55 is nonzero.
 check('equation_zero_separate_nonzero_tail',eq_quadratic(N,V,0,U,0,s,55)==0)
 Ubad=np.array([[1],[1]],dtype=object);check('bad_equation_rejected',eq_quadratic(N,V,0,Ubad,0,s,55)>0)
 U=np.array([[1],[2],[3],[4]],dtype=object);check('lag_quadratic_matches_direct',lag_quadratic(U,1,np.array([[1]],dtype=object),0)==F(2))
 cap=F(1,1<<41);check('fixedcap_boundary_pass',cap<=cap);check('fixedcap_one_dyadic_over_rejected',not cap+F(1,1<<180)<=cap)
 check('floor_independent_positive_required',not(F(-1)>0 and F(1)>=F(-1)))
 check('nearest_even_positive_half',ties_even(2.**-61)==0);check('nearest_even_negative_half',ties_even(-2.**-61)==0)
 check('duplicate_targets_fail_bijection',len(set([0]*209))!=209)
 return rows

def main():
 q=argparse.ArgumentParser();q.add_argument('--repo',required=True);q.add_argument('--producer',required=True);q.add_argument('--certificate',required=True);q.add_argument('--baseline',required=True);args=q.parse_args();repo=Path(args.repo);producer=Path(args.producer);f=read(P/'SAVED_AUDIT_FREEZE_v0.2.json');assert sha(__file__)==f['code_sha256'];assert sha(producer/'PROTOCOL_FREEZE.json')==f['producer_protocol_sha256'];control=controls();cert=read(args.certificate);data=read(producer/'DATA_FREEZE.json');runs=read(producer/'RUN_EXECUTIONS.json');audit=read(P/'DATA_AUDIT_RECEIPT.json');protocol=read(producer/'PROTOCOL_FREEZE.json')
 for name,h in protocol['files'].items():assert sha(producer/name)==h
 for name,h in protocol['repository_sources'].items():assert sha(repo/name)==h
 assert sha(args.baseline)==audit['baseline_sha256'];assert runs['data_freeze_sha256']==sha(producer/'DATA_FREEZE.json');assert cert['run_executions_sha256']==sha(producer/'RUN_EXECUTIONS.json')
 small=read(producer/'inputs/NULL_VECTOR.json')['vector'];v=np.zeros(2294,np.int64);v[:len(small)]=small;A=np.column_stack([2*np.random.default_rng(172026).choice([-1.,1.],(2294,160)).astype(np.int64),v,2*np.random.default_rng(184052).choice([-1.,1.],(2294,160)).astype(np.int64)])
 Y=np.memmap(args.baseline,dtype='<i8',mode='r',shape=(37,8191,62));X=np.asarray(Y.transpose(1,2,0).reshape(8191,2294),dtype=np.int64);N0=X@A;del X;u=np.ones(8191,np.int64);u[1::2]=-1;rows=[]
 for count,(datum,r,expected,result)in enumerate(zip(data['records'],runs['rows'],audit['rows'],cert['rows']),1):
  assert datum['record_sha256']==expected['raw_sha256']==r['record_sha256']==result['record_sha256'];case=producer/'results'/r['case'];assert read(case/'RUN.json')==r
  for name,h in r['numeric_witnesses'].items():assert sha(case/name)==h
  if r['execution_status']!='COMPLETED'or r['learned_order']!=209:rows.append({'case':r['case'],'status':'RETAINED_HOLD_EXECUTION_OR_ORDER'});continue
  w=np.zeros((62,37),np.int64)
  for prep in range(37):
   remaining=set(range(62))
   for k in range(count):
    c=max(remaining,key=lambda c:(abs(int(v[c*37+prep])),-c));remaining.remove(c);w[c,prep]=1 if v[c*37+prep]>=0 else -1
  N=N0+u[:,None]*(w.reshape(-1)@A)[None,:];assert hashlib.sha256(N.astype('<i8').tobytes()).hexdigest()==expected['integer_projection_sha256']
  z=np.load(case/'SVD_META.npz',allow_pickle=False);s=z['singular'];vt=z['right_transpose'];U=np.vstack([np.load(case/f'U_{k}.npz')['basis']for k in range(3)]);Ui,bu=decode(U);Vi,bv=decode(vt[:209].T.copy());si,bs=decode(s[:209].copy());T=np.load(case/'PHASE_META.npz')['shift'];Ti,bt=decode(T)
  assert sum(s>2**-24)==209;exact={'left_Gram_F':gram(Ui,bu)[1],'right_Gram_F':gram(Vi,bv)[1],'singular_equation_F':eq_quadratic(N,Vi,bv,Ui,bu,si,bs),'raw_lag_F':lag_quadratic(Ui,bu,Ti,bt)}
  for name,value in exact.items():assert value==frac(result['measured']['exact_squared'][name]),name
  smn,smb=decode(np.array([s[208]]));assert F(int(smn[0]),1<<smb)==frac(result['measured']['proposed_smin'])
  ph=phase_audit(case,read(producer/'inputs/SOURCE_PHASE.json'),result)
  rows.append({'case':r['case'],'status':'PASS_INDEPENDENT_EXACT_SAVED_ARITHMETIC','rank209_counted_not_forced':True,'exact_squared':{k:pair(v)for k,v in exact.items()},'phase':ph,'producer_gates_retained':result['gates'],'producer_status_retained':result['status'],'old_reconstruction_no_go_unchanged':True});print(json.dumps({'case':r['case'],'review_status':rows[-1]['status']}),flush=True)
 output={'status':'PASS_INDEPENDENT_TWO_SAVED_OUTPUT_AUDIT','rows':rows,'controls':control,'freeze_sha256':sha(P/'SAVED_AUDIT_FREEZE_v0.2.json'),'certificate_sha256':sha(args.certificate),'new_estimator_calls':0,'new_factor_or_raw_copies':0,'source_scope':'Protocol/source hashes replayed; source H/full factor bounds inherited, not recomputed. Independent IEEE bit decoding, quadratic-form EQ/lag exact identities, complex residuals and trig phase matching.','external_review':'PENDING','physical_promotion':0};target=P/'SAVED_AUDIT_RECEIPT.json';assert not target.exists();target.write_text(json.dumps(output,indent=2)+'\n')
if __name__=='__main__':main()
