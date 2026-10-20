"""Record-only validated oscillatory factor-Gram certificate. Adapted from nominal v0.2."""
import time,json
from pathlib import Path
import numpy as np
from scipy.linalg import cholesky,svd
from flint import arb,acb,acb_mat,fmpq,fmpz_mat,ctx
ctx.prec=512

def quantize64(values,bits):
 z=np.rint(np.asarray(values,dtype=np.float64)*2.**bits)
 if not np.all(np.isfinite(z)) or np.any(z>=2.**63) or np.any(z<-(2.**63)):
  raise ArithmeticError('HOLD: dyadic proposal exceeds signed int64 range')
 return z.astype(np.int64)
def fm(a):return fmpz_mat(a.tolist())
def arr(a):return np.array(a.tolist(),dtype=object)
def nearest(n,s):
 q,r=divmod(int(n),1<<s);half=1<<(s-1);return q+int(r>half or(r==half and q%2))
def dyad(x,b=60):
 v=x.mid()*(1<<b);n=v.unique_fmpz();return int(n) if n is not None else int((v+arb('.5')).floor().unique_fmpz())
def norm_exact(a,den):return arb(sum(int(v)**2 for v in a.flat)).sqrt()/(1<<den)
def acmat(re,im):return acb_mat([[acb(arb(int(re[i,k]))/(1<<60),arb(int(im[i,k]))/(1<<60)) for k in range(re.shape[1])] for i in range(re.shape[0])])
def up(x,bits=100):
 n=(x*(1<<bits)).ceil().unique_fmpz()
 if n is None:raise ArithmeticError('HOLD: outward dyadic bound unresolved')
 return [int(n),1<<bits]
def down(x,bits=100):
 n=(x*(1<<bits)).floor().unique_fmpz()
 if n is None:raise ArithmeticError('HOLD: outward dyadic bound unresolved')
 return [int(n),1<<bits]
def verify(theta,coeff,record_error,contract,out,emit):
 """All models/factors are untrusted proposals; every accepted error is bounded here."""
 q=coeff.shape[0];K=len(theta);p=37;c=62;M=4096;freq=[arb(0)]+[arb(int(v))/(1<<60) for v in theta]
 for j in range(1,len(freq)):
  if not (freq[j]>0 and freq[j]<arb.pi()) or(j>1 and not freq[j]>freq[j-1]):raise ArithmeticError('HOLD: frequency bounds/collision')
 # Each dyadic mode block is built from fitted C,S, not a frozen spectral projector.
 # Global paired real-rank allocation is a proposal, not an acceptance assertion.
 svds=[]
 for j in range(K+1):
  bre=coeff[0].reshape(c,p) if j==0 else coeff[2*j-1].reshape(c,p)
  bim=np.zeros((c,p),np.int64) if j==0 else -coeff[2*j].reshape(c,p)
  den=60 if j==0 else 61
  bm=bre.astype(float)/2.**den+1j*bim.astype(float)/2.**den
  svds.append(svd(bm,full_matrices=False,check_finite=False))
 target=contract['spectral_rule']['target_count'];slots=sorted([(float(v*v),j,k) for j,(_,ss,_) in enumerate(svds) if j for k,v in enumerate(ss)],key=lambda z:(-z[0],z[1],z[2]))
 ps=np.cumsum([0.]+[v[0] for v in slots]);station=np.cumsum([0.]+list(svds[0][1]**2));best=None
 for r0 in range(len(svds[0][1])+1):
  if target<r0 or (target-r0)%2:continue
  pairs=(target-r0)//2
  if pairs>len(slots):continue
  score=float(station[r0]+2*ps[pairs]);key=(score,-r0)
  if best is None or key>best[0]:best=(key,r0,pairs)
 if best is None:return {'status':'HOLD','reason':'Not enough modal proposal slots for the frozen target rank'}
 allocation=[best[1]]+[0]*K
 for _,j,k in slots[:best[2]]:allocation[j]+=1
 emit('global_rank_allocation',target_real_rank=target,allocation=allocation,method='largest proposed block singular energies, with stationary/pair real-dimension costs')
 modal=[];errors=arb(0);ranks=[];minimumL=[];minimumR=[];traceL=0;traceR=0;per_mode=[]
 for j in range(K+1):
  if j==0:
   re=coeff[0].reshape(c,p);im=np.zeros((c,p),dtype=np.int64);den=60
  else:
   re=coeff[2*j-1].reshape(c,p);im=-coeff[2*j].reshape(c,p);den=61
  B=acb_mat([[acb(arb(int(re[i,a]))/(1<<den),arb(int(im[i,a]))/(1<<den)) for a in range(p)] for i in range(c)])
  u,s,vh=svds[j];r=allocation[j];ranks.append(r)
  l=u[:,:r]*s[:r];v=vh[:r,:].conj().T
  lare=quantize64(l.real,60);laim=quantize64(l.imag,60);rare=quantize64(v.real,60);raim=quantize64(v.imag,60)
  if j==0 and(np.any(laim) or np.any(raim)):raise ArithmeticError('HOLD: stationary factor must be real')
  modal.append((lare,laim,rare,raim));mult=1 if j==0 else 2
  la=acmat(lare,laim) if r else acb_mat(c,0);ra=acmat(rare,raim) if r else acb_mat(p,0)
  residual=B-la*ra.conjugate().transpose();error2=sum((abs(residual[i,a])**2 for i in range(c) for a in range(p)),arb(0));errors+=mult*error2
  if r:
   for mat,target in [(la,minimumL),(ra,minimumR)]:
    gram=mat.conjugate().transpose()*mat
    target.append(min((gram[k,k].real-sum((abs(gram[k,z]) for z in range(r) if z!=k),arb(0))).lower() for k in range(r)))
  traceL+=mult*sum(int(z)**2 for v in [lare,laim] for z in v.flat);traceR+=mult*sum(int(z)**2 for v in [rare,raim] for z in v.flat)
  per_mode.append({'mode':j,'rank':r,'modal_error_upper':up(error2.sqrt())})
 n=ranks[0]+2*sum(ranks[1:]);emit('modal_factors',rank=n,ranks=ranks,modal_residual=str(errors.sqrt().upper()))
 np.savez_compressed(out/'RECORD_FACTORS.npz',**{f'{j}_{k}':v for j,mm in enumerate(modal) for k,v in enumerate(mm)})
 if n!=contract['spectral_rule']['target_count']:return {'status':'HOLD','reason':'Proposed spatial rank differs from frozen target','proposed_rank':n,'per_mode':per_mode}
 modes=[];pair_start=0
 if ranks[0]:modes.append((arb(0),modal[0]));pair_start=1
 for j in range(1,K+1):
  if ranks[j]:
   mm=modal[j];modes.extend([(freq[j],mm),(-freq[j],(mm[0],-mm[1],mm[2],-mm[3]))])
 off=np.cumsum([0]+[m[0].shape[1] for w,m in modes]);head=ranks[0]
 lr=np.zeros((n,n),np.int64);li=lr.copy();rrr=lr.copy();ri=lr.copy();rows=[arb(0) for _ in modes];tgate=arb(1)/(1<<51)
 for a,(wa,ma) in enumerate(modes):
  ar,ai,br,bi=map(fm,ma);i=slice(off[a],off[a+1])
  for b in range(a,len(modes)):
   wb,mb=modes[b];cr,ci,dr,di=map(fm,mb);j=slice(off[b],off[b+1]);d=wb-wa
   t=acb(1) if a==b else (acb(0,M*d).exp()-1)/(acb(0,d).exp()-1)/M
   if a!=b:
    v=arb(abs(t).upper());rows[a]+=v;rows[b]+=v
   tr,ti=dyad(t.real,52),dyad(t.imag,52)
   if not abs(t.real-arb(tr)/(1<<52))+abs(t.imag-arb(ti)/(1<<52))<tgate:raise ArithmeticError('HOLD: temporal Gram enclosure')
   for which,(re,im) in enumerate([(ar.transpose()*cr+ai.transpose()*ci,ar.transpose()*ci-ai.transpose()*cr),(br.transpose()*dr+bi.transpose()*di,br.transpose()*di-bi.transpose()*dr)]):
    re,im=arr(re),arr(im);tim=ti if which==0 else -ti
    xr=np.array([nearest(v,120) for v in (tr*re-tim*im).flat],dtype=np.int64).reshape(re.shape);xi=np.array([nearest(v,120) for v in (tim*re+tr*im).flat],dtype=np.int64).reshape(re.shape)
    dr,di=(lr,li) if which==0 else(rrr,ri);dr[i,j]=xr;di[i,j]=xi;dr[j,i]=xr.T;di[j,i]=-xi.T
  if a%10==0:emit('gram_progress',mode=a,total_modes=len(modes))
 def real_transform(re,im):
  cr=re.copy();ci=im.copy()
  for a in range(pair_start,len(modes),2):
   p=slice(off[a],off[a+1]);q=slice(off[a+1],off[a+2]);cr[:,p]=re[:,p]+re[:,q];ci[:,p]=im[:,p]+im[:,q];cr[:,q]=im[:,p]-im[:,q];ci[:,q]=-re[:,p]+re[:,q]
  out=cr.copy()
  for a in range(pair_start,len(modes),2):
   p=slice(off[a],off[a+1]);q=slice(off[a+1],off[a+2]);out[p,:]=cr[p,:]+cr[q,:];out[q,:]=-ci[p,:]+ci[q,:]
  return out
 gl=real_transform(lr,li);gr=real_transform(rrr,ri);gr[:head,:head]*=4;gr[:head,head:]*=2;gr[head:,:head]*=2
 errgl=2*(tgate*arb(traceL)/(1<<120)+arb(n)/(1<<52));errgr=tgate*arb(traceR)/(1<<120)+arb(n)/(1<<52)
 a=1-arb(max(v.upper() for v in rows))
 # The truncation residual includes discarded modes too; bound the full proposed frame.
 full_freq=[arb(0)]+[v for w in freq[1:] for v in (w,-w)];full_rows=[arb(0) for _ in full_freq]
 for i in range(len(full_freq)):
  for j in range(i+1,len(full_freq)):
   dd=full_freq[j]-full_freq[i];tt=(acb(0,M*dd).exp()-1)/(acb(0,dd).exp()-1)/M;vv=arb(abs(tt).upper());full_rows[i]+=vv;full_rows[j]+=vv
 b=1+arb(max(v.upper() for v in full_rows))
 if not a>0:raise ArithmeticError('HOLD: frame Gershgorin bound inconclusive')
 minGL=a*arb(min(minimumL));minGR=a*arb(min(minimumR))/2
 total_error=record_error+b*errors.sqrt()
 np.savez_compressed(out/'FACTOR_GRAMS.npz',left=gl,right=gr)
 emit('factor_grams',left_error=up(errgl),right_error=up(errgr),frame_min=down(a),tail_error=up(total_error))
 lf=fm(quantize64(cholesky(gl.astype(float)/2.**52,lower=True,check_finite=False),60));rf=fm(quantize64(cholesky(gr.astype(float)/2.**54,lower=True,check_finite=False),60))
 resl=norm_exact(arr(lf*lf.transpose())-gl.astype(object)*(1<<68),120);emit('left_cholesky_verified',residual=up(resl))
 resr=norm_exact(arr(rf*rf.transpose())-gr.astype(object)*(1<<66),120);emit('right_cholesky_verified',residual=up(resr))
 if not (minGL>errgl+resl and minGR>errgr+resr):raise ArithmeticError('HOLD: factors not certified independent')
 etaL=(errgl+resl)/(minGL-errgl-resl);etaR=(errgr+resr)/(minGR-errgr-resr)
 if not(etaL<1 and etaR<1):raise ArithmeticError('HOLD: factor defect')
 sc=arr(lf.transpose()*rf);snum=np.array([nearest(v,68) for v in sc.flat],np.int64).reshape(n,n);emit('exact_core_product')
 u,ss,vh=svd(snum.astype(float)/2.**52,full_matrices=False,check_finite=False,lapack_driver='gesdd');un=quantize64(u,60);vn=quantize64(vh.T,60);sig=quantize64(ss,52)
 emit('untrusted_core_svd',maximum=float(ss[0]),minimum=float(ss[-1]),condition=float(ss[0]/ss[-1]))
 uf,vf=fm(un),fm(vn);identity=np.eye(n,dtype=object)*(1<<120)
 eu=norm_exact(arr(uf.transpose()*uf)-identity,120);emit('left_svd_verified',defect=up(eu))
 ev=norm_exact(arr(vf.transpose()*vf)-identity,120);emit('right_svd_verified',defect=up(ev))
 res=norm_exact(arr(fm(un.astype(object)*sig.astype(object)[None,:])*vf.transpose())-sc*(1<<52),172);emit('svd_residual_verified',residual=up(res))
 if not(eu<1 and ev<1):raise ArithmeticError('HOLD: polar correction inconclusive')
 du=eu/(1+(1-eu).sqrt());dv=ev/(1+(1-ev).sqrt());svderr=res+arb(int(sig[0]))/(1<<52)*(du*(1+ev).sqrt()+dv)
 low=((1-etaL)*(1-etaR)).sqrt()*(arb(int(sig[-1]))/(1<<52)-svderr)-total_error
 high=((1+etaL)*(1+etaR)).sqrt()*(arb(int(sig[0]))/(1<<52)+svderr)+total_error
 rule=contract['spectral_rule'];threshold=arb(fmpq(*rule['selection_threshold']));passed=low>threshold and total_error<threshold and low>0 and high/low<rule['retained_condition_number_strict_upper']
 # Full approximate singular spectra can be enclosed; stored here are the acceptance extrema.
 return {'status':'CERTIFIED_NUMERIC_RECORD_SIGNATURE' if passed else 'HOLD','physical_promotion':0,'independent_review':'pending','lane':'development — no registry entry','target_count':n,'selection_threshold':rule['selection_threshold'],'sigma_r_lower':down(low),'sigma_1_upper':up(high),'sigma_r_plus1_upper':up(total_error),'projection_tail_frobenius_upper':up(total_error),'condition_upper':up(high/low) if low>0 else None,'frame_min_lower':down(a),'frame_max_upper':up(b),'record_fit_error_upper':up(record_error),'truncation_hankel_error_upper':up(b*errors.sqrt()),'modal_residual_upper':up(errors.sqrt()),'eta_left_upper':up(etaL),'eta_right_upper':up(etaR),'core_svd_residual_upper':up(svderr),'per_mode':per_mode,'source_operator_or_nominal_modes_used':False,'empirical_provenance_validated':False,'apparatus_execution_claimed':False,'independent_blinded_execution_claimed':False}
