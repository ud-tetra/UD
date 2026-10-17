#!/usr/bin/env python3
"""Frozen nominal benchmark. No dense Hankel allocation; exact source moments and dyadic actions."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import time,json,gzip,hashlib,resource,sys
from pathlib import Path
from fractions import Fraction
import numpy as np
from scipy.linalg import svd,cholesky
from flint import ctx,arb,acb,arb_mat,acb_mat,fmpz_mat,fmpq,fmpq_poly
ctx.prec=512
P=Path(__file__).resolve().parent; S=P/'sources'; O=P/'output';O.mkdir(exist_ok=True)
START=time.monotonic(); metrics={}
def emit(stage,**kw):
 metrics[stage]={'elapsed_seconds':time.monotonic()-START,**kw};(O/'PROGRESS.json').write_text(json.dumps(metrics,indent=2));print(stage,kw,flush=True)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(name,d): (O/name).write_text(json.dumps(d,indent=2))
def arq(x):return arb(fmpq(int(x[0]),int(x[1])))
def interval(x):
 a,b=arq(x['a']),arq(x['b']); return (a+b)/2+arb(0,((b-a)/2).upper())
def upper(x): return str(x.upper())
def dyad(x,b=60):return int((x.mid()*(1<<b)).unique_fmpz()) if (x.mid()*(1<<b)).unique_fmpz() is not None else int((x.mid()*(1<<b)+arb('0.5')).floor().unique_fmpz())
def nearest(n,s):
 q,r=divmod(int(n),1<<s);half=1<<(s-1)
 return q+(r>half or (r==half and q%2!=0))
def fm(a):return fmpz_mat(a.tolist())
def arr(a):return np.array(a.tolist(),dtype=object)
def norm_exact(a,den):return arb(sum(int(v)**2 for v in a.flat)).sqrt()/(1<<den)
def maxerr(vals, nums,b):return sum((abs(v-arb(int(n))/(1<<b)) for v,n in zip(vals,nums)),arb(0))
A=np.load(S/'OPERATORS.npz'); X=np.load(S/'BASE_PREPARATIONS.npz'); obs=A['obs'];inds=A['A_indices'];ptr=A['A_indptr'];data=A['A_data'];sn=X['numerator'].astype(object)
with gzip.open(S/'CROSS_MOMENTS.json.gz','rt') as f: mom=json.load(f)
roots=json.loads((S/'REFINED_ROOT_INTERVALS.json').read_text()); co=json.loads((S/'ANNIHILATOR_COEFFICIENTS.json').read_text())['qL_coefficients_descending']; cert=json.loads((S/'PREPARATION_CERTIFICATE.json').read_text())
assert X['denominator']==52 and np.all((sn==1)|(sn==-1));assert len(roots)==53
qpoly=fmpq_poly(list(reversed(co)))
for j,r in enumerate(roots):
 a,b=fmpq(*r['a']),fmpq(*r['b']);assert a<=b
 assert qpoly(a)==0 if a==b else qpoly(a)*qpoly(b)<0
 if j: assert fmpq(*roots[j-1]['b'])<a
emit('inputs',source_hashes={p.name:sha(p) for p in S.iterdir()},roots_isolated=53)
def apply(m):
 out=np.zeros_like(m)
 for i in range(2640):
  for k in range(ptr[i],ptr[i+1]):out[i]+=int(data[k])*m[inds[k]]
 return out
if not (O/'MOMENTS_VERIFIED.json').exists():
 m=sn.copy(); annih=np.zeros_like(m)
 for k in range(54):
  annih+=int(co[53-k])*m
  if k<53:
   assert np.array_equal(m[obs],np.array(mom['G'][k],dtype=object))
   am=apply(m);assert np.array_equal(am[obs],np.array(mom['J'][k],dtype=object))
   m=-apply(am)
  if k%10==0:print('moment',k,flush=True)
 assert not np.any(annih)
 save('MOMENTS_VERIFIED.json',{'exact':True,'powers_checked':53,'annihilator_on_all_preparations':True})
emit('moments_verified')
# Interval projector coefficients, coefficient dyadics, and numerical low rank factors.
Cs=[]; Ss=[]; W=[]; Bs=[]; ranks=[]; cerrors=[]; modal=[]; modal_error2=arb(0); etaR=arb(0)
Gs=[arb_mat(g) for g in mom['G']];Js=[arb_mat(g) for g in mom['J']]
dco=[(53-i)*co[i] for i in range(53)]
for j,rr in enumerate(roots):
 mu=interval(rr);cc=[arb(1)]
 for c in co[1:-1]:cc.append(arb(c)+mu*cc[-1])
 dd=arb(0)
 for c in dco:dd=dd*mu+c
 gg=arb_mat(62,37);jj=arb_mat(62,37)
 for k in range(53):gg+=Gs[52-k]*cc[k];jj+=Js[52-k]*cc[k]
 gg/=dd*52
 if j==0:
  B=acb_mat(gg);cs=[gg[i,a] for i in range(62) for a in range(37)];ss=None;W.append(arb(0))
 else:
  w=mu.sqrt();W.append(w);jj/=dd*52*w
  B=acb_mat(gg)/2-acb(0,1)*acb_mat(jj)/2
  cs=[gg[i,a] for i in range(62) for a in range(37)];ss=[jj[i,a] for i in range(62) for a in range(37)]
 cn=[dyad(v) for v in cs]; Cs.append(cn);cerrors.append(arb(max(abs(v-arb(n)/(1<<60)).upper() for v,n in zip(cs,cn))))
 if ss is not None:
  ssn=[dyad(v) for v in ss];Ss.append(ssn);cerrors.append(arb(max(abs(v-arb(n)/(1<<60)).upper() for v,n in zip(ss,ssn))))
 bm=np.array([[complex(float(B[i,a].real.mid()),float(B[i,a].imag.mid())) for a in range(37)] for i in range(62)])
 u,s,vh=svd(bm,full_matrices=False,check_finite=False);r=cert['components'][j]['rank_per_signed_frequency'];ranks.append(r)
 l=u[:,:r]*s[:r];v=vh[:r,:].conj().T
 lnre=np.rint(l.real*2.**60).astype(np.int64);lnim=np.rint(l.imag*2.**60).astype(np.int64);rnre=np.rint(v.real*2.**60).astype(np.int64);rnim=np.rint(v.imag*2.**60).astype(np.int64)
 if j==0:assert np.max(abs(lnim))==0 and np.max(abs(rnim))==0
 la=acb_mat([[acb(arb(int(lnre[i,k]))/(1<<60),arb(int(lnim[i,k]))/(1<<60)) for k in range(r)] for i in range(62)])
 ra=acb_mat([[acb(arb(int(rnre[i,k]))/(1<<60),arb(int(rnim[i,k]))/(1<<60)) for k in range(r)] for i in range(37)])
 diff=B-la*ra.conjugate().transpose();ee=sum((abs(diff[i,a])**2 for i in range(62) for a in range(37)),arb(0));modal_error2+=ee*(1 if j==0 else 2)
 rd=ra.conjugate().transpose()*ra-acb_mat(np.eye(r,dtype=int).tolist()); eta=sum((abs(rd[i,k])**2 for i in range(r) for k in range(r)),arb(0)).sqrt();etaR=arb(max(etaR.upper(),eta.upper()))
 modal.append((lnre,lnim,rnre,rnim)); Bs.append({'factor':rr['factor'],'rank':r,'residual_frobenius_upper':upper(ee.sqrt()),'right_isometry_defect_upper':upper(eta)})
 if j%10==0:print('modal',j,flush=True)
coeff=np.array([Cs[0]]+[v for j in range(52) for v in (Cs[j+1],Ss[j])],dtype=np.int64)
np.savez_compressed(O/'MODAL_FACTORS.npz',**{f'{j}_{k}':v for j,mm in enumerate(modal) for k,v in enumerate(mm)},coeff=coeff)
save('MODAL_VERIFICATION.json',{'components':Bs,'modal_error_frobenius_upper':upper(modal_error2.sqrt()),'right_defect_upper':upper(etaR),'coefficient_error_sum_upper':upper(sum(cerrors,arb(0)))})
emit('modal_factorization',real_rank=sum(ranks)*2-1,modal_error=upper(modal_error2.sqrt()))
# Canonical 150MB integer record generated with exact products of interval-rounded dyadics.
if not (O/'PHASES.npy').exists():
 phase=np.zeros((8191,105),dtype=np.int64);phase[:,0]=1<<60;phase_error=arb(0)
 for j in range(1,53):
  step=acb(0,W[j]/2).exp();z=acb(1);err=arb(0)
  for k in range(8191):
   z=acb(0,W[j]*k/2).exp()
   nn=[dyad(z.real),dyad(z.imag)];phase[k,2*j-1:2*j+1]=nn
   err=arb(max(err.upper(),abs(z.real-arb(nn[0])/(1<<60)).upper(),abs(z.imag-arb(nn[1])/(1<<60)).upper()))
  phase_error=arb(max(phase_error.upper(),err.upper()))
  if j%10==0:print('phase',j,flush=True)
 np.save(O/'PHASES.npy',phase);save('PHASE_ERROR.json',{'upper':upper(phase_error)})
else:phase=np.load(O/'PHASES.npy');phase_error=arb(json.loads((O/'PHASE_ERROR.json').read_text())['upper'])
phase_error=arb(phase_error.upper()); scalar_error=sum(cerrors,arb(0))+phase_error*arb(sum(np.max(np.abs(coeff),axis=1).astype(object)))/(1<<60)+arb(1)/(1<<49)
trajectory_h_error=arb(37*62).sqrt()*scalar_error
if not (O/'FROZEN_RECORD.npy').exists():
 record=np.lib.format.open_memmap(O/'FROZEN_RECORD.npy',mode='w+',dtype='<i8',shape=(37,8191,62)); cf=fm(coeff)
 for k in range(0,8191,128):
  yy=fm(phase[k:k+128])*cf;yy=np.array([[nearest(x,72) for x in row] for row in yy.tolist()],dtype=np.int64)
  record[:,k:k+len(yy),:]=yy.reshape(-1,62,37).transpose(2,0,1)
  if k%1024==0:print('record',k,flush=True)
 record.flush()
else:record=np.load(O/'FROZEN_RECORD.npy',mmap_mode='r')
# payload hash excludes NPY header
h=hashlib.sha256();
for a in range(37):h.update(record[a].tobytes())
save('FROZEN_RECORD_MANIFEST.json',{'shape':[37,8191,62],'dtype':'<i8','payload_sha256':h.hexdigest(),'payload_bytes':record.nbytes,'scale_bits':48,'scalar_error_upper':upper(scalar_error),'hankel_frobenius_error_upper':upper(trajectory_h_error),'recipe':'PHASES.npy @ MODAL_FACTORS.npz[coeff], exact integer dot products, divide 2^72 nearest ties-even, columns c*37+a.'})
emit('record_generated',payload_sha256=h.hexdigest(),hankel_error=upper(trajectory_h_error))
# Signed modes and actual factor Gram matrices.
if (O/'FACTOR_GRAMS.npz').exists():
 z=np.load(O/'FACTOR_GRAMS.npz');gl=z['left'];gr=z['right'];ee=json.loads((O/'GRAM_ERRORS.json').read_text());errgl=arb(ee['left']);errgr=arb(ee['right'])
else:
 modes=[(arb(0),modal[0])]
 for j in range(1,53):
  mm=modal[j];modes.extend([(W[j],mm),(-W[j],(mm[0],-mm[1],mm[2],-mm[3]))])
 sizes=[mm[0].shape[1] for w,mm in modes];off=np.cumsum([0]+sizes);n=int(off[-1]);assert n==1893
 lr=np.zeros((n,n),dtype=np.int64);li=lr.copy();rrr=lr.copy();ri=lr.copy();crossnormL=0;crossnormR=0;maxterr=arb(0)
 for a,(wa,ma) in enumerate(modes):
  ar,ai,br,bi=map(fm,ma);i=slice(off[a],off[a+1])
  for b in range(a,len(modes)):
   wb,mb=modes[b];cr,ci,dr,di=map(fm,mb);j=slice(off[b],off[b+1]);delta=(wb-wa)/2
   t=acb(1) if a==b else (acb(0,4096*delta).exp()-1)/(acb(0,delta).exp()-1)/4096
   tr,ti=dyad(t.real,52),dyad(t.imag,52);maxterr=arb(max(maxterr.upper(),(abs(t.real-arb(tr)/(1<<52))+abs(t.imag-arb(ti)/(1<<52))).upper()))
   for which,(re,im) in enumerate([(ar.transpose()*cr+ai.transpose()*ci,ar.transpose()*ci-ai.transpose()*cr),(br.transpose()*dr+bi.transpose()*di,br.transpose()*di-bi.transpose()*dr)]):
    re,im=arr(re),arr(im);cn=sum(int(v)**2 for v in re.flat)+sum(int(v)**2 for v in im.flat)
    if which==0:crossnormL+=cn*(1 if a==b else 2)
    else:crossnormR+=cn*(1 if a==b else 2)
    tim=ti if which==0 else -ti
    xr=np.array([nearest(v,120) for v in (tr*re-tim*im).flat],dtype=np.int64).reshape(re.shape);xi=np.array([nearest(v,120) for v in (tim*re+tr*im).flat],dtype=np.int64).reshape(re.shape)
    destR,destI=(lr,li) if which==0 else (rrr,ri);destR[i,j]=xr;destI[i,j]=xi;destR[j,i]=xr.T;destI[j,i]=-xi.T
  if a%10==0:print('Gram mode',a,flush=True)
 # Congruence A*G A; pair transform gives real columns [2Re,2Im].
 def real_transform(re,im):
  cr=re.copy();ci=im.copy()
  for a in range(1,len(modes),2):
   p=slice(off[a],off[a+1]);q=slice(off[a+1],off[a+2]);cr[:,p]=re[:,p]+re[:,q];ci[:,p]=im[:,p]+im[:,q];cr[:,q]=im[:,p]-im[:,q];ci[:,q]=-re[:,p]+re[:,q]
  out=cr.copy()
  for a in range(1,len(modes),2):
   p=slice(off[a],off[a+1]);q=slice(off[a+1],off[a+2]);out[p,:]=cr[p,:]+cr[q,:];out[q,:]=-ci[p,:]+ci[q,:]
  return out
 gl=real_transform(lr,li);gr=real_transform(rrr,ri)
 # right B=A/2 on each paired block; store denominator 2^54, stationary untouched.
 gr[0,0]*=4;gr[0,1:]*=2;gr[1:,0]*=2
 errgl=2*(maxterr*arb(crossnormL).sqrt()/(1<<120)+arb(n)/(1<<52))
 errgr=maxterr*arb(crossnormR).sqrt()/(1<<120)+arb(n)/(1<<52)
 np.savez_compressed(O/'FACTOR_GRAMS.npz',left=gl,right=gr)
 save('GRAM_ERRORS.json',{'left':upper(errgl),'right':upper(errgr),'left_scale_bits':52,'right_scale_bits':54,'temporal_error':upper(maxterr)})
emit('factor_grams',left_error=upper(errgl),right_error=upper(errgr),shape=list(gl.shape))
# Verified nominal singular spectrum. Floating factorizations are only proposals.
n=1893; glf=gl.astype(float)/2.**52;grf=gr.astype(float)/2.**54
ll=cholesky(glf,lower=True,check_finite=False);rl=cholesky(grf,lower=True,check_finite=False)
ln=np.rint(ll*2.**60).astype(np.int64);rn=np.rint(rl*2.**60).astype(np.int64)
lf,rf=fm(ln),fm(rn)
emit('cholesky_proposed')
resl=norm_exact(arr(lf*lf.transpose())-gl.astype(object)*(1<<68),120);emit('left_cholesky_verified',residual=upper(resl))
resr=norm_exact(arr(rf*rf.transpose())-gr.astype(object)*(1<<66),120);emit('right_cholesky_verified',residual=upper(resr))
# Conservative lower bounds from rechecked source projector certificate.
a=arb(fmpq(1149,2042));b=arb(fmpq(2935,2042));alphaB=arb(1)/(1<<27);betaB=arb(1)/128
em=modal_error2.sqrt();minGL=a*(alphaB.sqrt()-em)**2/(1+etaR);minGR=a*(1-etaR)/2
etaL=(errgl+resl)/(minGL-errgl-resl);etaRight=(errgr+resr)/(minGR-errgr-resr)
assert etaL<1 and etaRight<1
sc=fm(ln).transpose()*rf; scarr=arr(sc); snum=np.array([nearest(v,68) for v in scarr.flat],dtype=np.int64).reshape(n,n)
emit('exact_core_product')
u,ss,vh=svd(snum.astype(float)/2.**52,full_matrices=False,check_finite=False,lapack_driver='gesdd')
un=np.rint(u*2.**60).astype(np.int64);vn=np.rint(vh.T*2.**60).astype(np.int64);sig=np.rint(ss*2.**52).astype(np.int64)
np.savez_compressed(O/'SPECTRAL_PROPOSAL.npz',left_cholesky=ln,right_cholesky=rn,U=un,V=vn,sigma=sig)
emit('core_svd_proposed',sigma_max=float(ss[0]),sigma_min=float(ss[-1]),condition=float(ss[0]/ss[-1]))
uf,vf=fm(un),fm(vn);identity=np.eye(n,dtype=object)*(1<<120)
eu=norm_exact(arr(uf.transpose()*uf)-identity,120);emit('svd_left_verified',defect=upper(eu))
ev=norm_exact(arr(vf.transpose()*vf)-identity,120);emit('svd_right_verified',defect=upper(ev))
us=fm(un.astype(object)*sig.astype(object)[None,:]);approx=us*vf.transpose();res=norm_exact(arr(approx)-scarr*(1<<52),172)
emit('svd_residual_verified',residual=upper(res))
assert eu<1 and ev<1
du=eu/(1+(1-eu).sqrt());dv=ev/(1+(1-ev).sqrt());svderr=res+arb(int(sig[0]))/(1<<52)*(du*(1+ev).sqrt()+dv)
faclo=((1-etaL)*(1-etaRight)).sqrt();fachi=((1+etaL)*(1+etaRight)).sqrt()
model_error=b*modal_error2.sqrt();total_error=model_error+trajectory_h_error
smin=faclo*(arb(int(sig[-1]))/(1<<52)-svderr)-total_error;smax=fachi*(arb(int(sig[0]))/(1<<52)+svderr)+total_error
contract=json.loads((S/'FROZEN_CONTRACT.json').read_text())
threshold=arq(contract['spectral_rule']['selection_threshold'])
# Store all proof quantities; exact B source threshold is inherited and pinned by hash.
spectrum={'status':'CERTIFIED_INTERVAL_CONSTRUCTOR','physical_promotion':0,'independent_review':'pending','implementation':'structured frozen-nominal factor-Gram reduction','rank_retained':1893,'hidden_dimension_source':747,'sigma_min_lower':str(smin.lower()),'sigma_max_upper':upper(smax),'condition_upper':upper(smax/smin),'tail_spectral_upper':upper(total_error),'eta_left_upper':upper(etaL),'eta_right_upper':upper(etaRight),'svd_error_upper':upper(svderr),'modal_hankel_error_upper':upper(model_error),'trajectory_hankel_error_upper':upper(trajectory_h_error),'threshold_display':str(threshold),'rank_count_at_threshold_pass':bool(smin>threshold and total_error<threshold),'condition_below_2029':bool(smax/smin<2029),'condition_below_2028_403':bool(smax/smin<arb('2028.403'))}
save('SPECTRAL_CERTIFICATE.json',spectrum);emit('spectral_certified',**spectrum)
# Exact data energy and both full-size Hankel actions on deterministic probes.
sys.path.insert(0,str(P.parent/'spectral-work'));from hankel_exact import HankelRecord
print('HankelRecord API',flush=True)
import inspect
save('RESOURCE_RESULT.json',{'wall_seconds':time.monotonic()-START,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'dense_hankel_allocated':False,'dense_hankel_bytes_avoided':307895468032,'record_payload_bytes':record.nbytes,'factor_gram_bytes':gl.nbytes+gr.nbytes,'threads':os.environ.get('OPENBLAS_NUM_THREADS')})
print(inspect.signature(HankelRecord),flush=True)
emit('complete_spectral_stage')
