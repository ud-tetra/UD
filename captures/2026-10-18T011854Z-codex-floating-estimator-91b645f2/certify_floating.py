"""All-rounding-accounted verification of captured floating estimator outputs."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import argparse,json,time,hashlib,resource
from pathlib import Path
import numpy as np
from flint import ctx,arb,acb
from proof_math import fm,arr,dyad,up
from numeric_math import encode,encode_complex,norm2_receipt,diffnorm,cmul,complex_residual,assemble
ctx.prec=512
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def model():
 with np.load(P/'inputs/REFERENCE_PROPOSAL.npz',allow_pickle=False) as z:theta=z['theta'];coeff=z['coeff']
 W=np.random.default_rng(172026).choice([-1.,1.],size=(2294,160)).astype(np.int64);v=np.pad(np.array(json.loads((P/'inputs/NULL_VECTOR.json').read_text())['vector'],np.int64),(0,1974));A=np.column_stack((2*W,v));C=fm(coeff)*fm(A)
 pp=np.zeros((8191,105),np.int64);pp[:,0]=1<<60;gate=arb(1)/(1<<60)
 for j,t in enumerate(theta):
  for k in range(8191):
   z=acb(0,arb(int(t))*k/(1<<60)).exp();r,i=dyad(z.real),dyad(z.imag)
   assert abs(z.real-arb(r)/(1<<60))<gate and abs(z.imag-arb(i)/(1<<60))<gate
   pp[k,2*j+1]=r;pp[k,2*j+2]=i
 ca=arr(C);cmax=sum(max(abs(int(x)) for x in row) for row in ca[1:]);phase=arb(8191*161).sqrt()*arb(cmax)/(1<<127)
 return pp,C,phase,A

def run(case,portable=False):
 start=time.monotonic();freeze=json.loads((P/'CAMPAIGN_FREEZE.json').read_text());entry=next(c for c in freeze['cases'] if c['case']==case);out=P/f'results/{case}';wpath=out/'FLOAT_WITNESS.npz';prop=out/'PROPOSAL.npz';hashes={'witness':sha(wpath),'proposal':sha(prop)}
 with np.load(wpath,allow_pickle=False) as z:w={n:z[n] for n in z.files}
 assert set(w)=={'basis','shift','eigenvalues','eigenvectors','inverse','reduction','angles'}
 assert w['basis'].shape==(8191,105) and w['shift'].shape==(105,105) and w['reduction'].shape==(105,161)
 with np.load(prop,allow_pickle=False) as z:theta=z['theta']
 assert theta.shape==(52,) and sha(prop)==entry['parent_proposal_sha256'],'Original proposal changed'
 pp,C,phase,A=model()
 if portable:
  with np.load(out/'EXACT_RECORD_SKETCH.npz',allow_pickle=False) as z:Z=z['integer_sketch']
  assert Z.dtype==np.int64 and Z.shape==(8191,161)
 else:
  path=P/entry['record_path'];before=sha(path);assert before==entry['record_sha256']
  Y=np.memmap(path,dtype='<i8',mode='r',shape=(37,8191,62));X=np.array(Y.transpose(1,2,0).reshape(8191,2294),dtype=np.int64)
  assert max(abs(int(X.min())),abs(int(X.max())))*max(sum(abs(int(x)) for x in A[:,j]) for j in range(161))<2**63
  Z=X@A;del X
  np.savez_compressed(out/'EXACT_RECORD_SKETCH.npz',integer_sketch=Z)
  assert sha(path)==before
 # Exact reference-model residual against exact raw-record sketch, not floating Z.
 sq=0
 for k in range(0,8191,128):
  values=arr(fm(pp[k:k+128])*C);diff=values-Z[k:k+len(values)].astype(object)*(1<<72);sq+=sum(int(x)**2 for x in diff.flat)
 fit=arb(sq).sqrt()/(1<<127)+phase
 un,bu=encode(w['basis']);bn,bb=encode(w['reduction']);tn,bt=encode(w['shift']);uf=fm(un);bf=fm(bn);tf=fm(tn)
 eta,eta2=diffnorm(uf.transpose()*uf,2*bu,fm(np.eye(105,dtype=object)),0)
 proj,proj2=diffnorm(fm(Z),55,uf*bf,bu+bb)
 bnorm,bnorm2=norm2_receipt(bn,bb)
 shift,shift2=diffnorm(fm(un[1:]),bu,fm(un[:-1])*tf,bu+bt)
 vr,vi,bv=encode_complex(w['eigenvectors']);ir,ii,bi=encode_complex(w['inverse']);lr,li,bl=encode_complex(w['eigenvalues'])
 vf=(fm(vr),fm(vi));iv=(fm(ir),fm(ii));identity=(fm(np.eye(105,dtype=object)),fm(np.zeros((105,105),dtype=object)))
 inverse,inverse2=complex_residual(cmul(*vf,*iv),bv+bi,identity,0)
 invnorm,invnorm2=norm2_receipt(np.r_[ir.flat[:],ii.flat[:]],bi)
 left=(tf*vf[0],tf*vf[1]);right=(fm(vr*lr[None,:]-vi*li[None,:]),fm(vr*li[None,:]+vi*lr[None,:]))
 eigen,eigen2=complex_residual(left,bt+bv,right,bv+bl)
 angles=w['angles'];assert angles.shape==(105,)
 positive=np.where(angles>1e-10)[0];positive=positive[np.argsort(angles[positive])]
 assert len(positive)==52 and np.count_nonzero(angles<-1e-10)==52 and np.count_nonzero(abs(angles)<=1e-10)==1
 errors=[]
 for j,index in enumerate(positive):
  # Verify exact ties-to-even grid rounding of the captured angle bit pattern.
  n,d=float(angles[index]).as_integer_ratio();q,r=divmod(n*(1<<60),d);expected=q+int(2*r>d or (2*r==d and q%2))
  assert int(theta[j])==expected,'HOLD: emitted phase is not captured rounding result'
  z=acb(arb(int(lr[index]))/(1<<bl),arb(int(li[index]))/(1<<bl));arg=z.arg();assert arg>0 and arg<arb.pi()
  errors.append(up(abs(arg-arb(int(theta[j]))/(1<<60))))
 argerror=[max(x[0] for x in errors),1<<100]
 constants=json.loads((P/'inputs/PHASE_STABILITY_CERTIFICATE.json').read_text())['constants'];constants['discovery_cutoff']=json.loads((P/'inputs/SKETCH_RULE.json').read_text())['cutoff']
 metrics={'basis_orthogonality_upper':up(eta),'projection_residual_upper':up(proj),'reduction_norm_upper':up(bnorm),'reference_model_residual_upper':up(fit),'shift_residual_upper':up(shift),'inverse_residual_upper':up(inverse),'inverse_norm_upper':up(invnorm),'eigenpair_residual_upper':up(eigen),'argument_output_error_upper':argerror}
 result=assemble(metrics,constants)
 result.update(case=case,record_sha256=entry['record_sha256'],witness_sha256=hashes['witness'],proposal_sha256=hashes['proposal'],exact_sketch_sha256=sha(out/'EXACT_RECORD_SKETCH.npz'),metrics=metrics,exact_squared_norms={'basis_orthogonality':eta2,'projection':proj2,'reduction':bnorm2,'reference_dyadic_phase':[sq,1<<254],'shift':shift2,'inverse':inverse2,'inverse_norm':invnorm2,'eigenpair':eigen2},exact_binary_scale_bits={'basis':bu,'reduction':bb,'shift':bt,'eigenvectors':bv,'inverse':bi,'eigenvalues':bl},original_proposal_byte_identical=True,all_18790154_readings_projected=not portable,portable_sketch_witness_replay=portable,independent_review='pending',nominal_operator_or_modes_used=False,wall_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 assert sha(wpath)==hashes['witness'] and sha(prop)==hashes['proposal']
 dest=out/('REPLAY_CERTIFICATE.json' if portable else 'FLOAT_CERTIFICATE.json');assert not dest.exists();dest.write_text(json.dumps(result,indent=2));print(json.dumps({'case':case,'bounds':result['readable'],'metrics':metrics,'seconds':result['wall_seconds']},indent=2),flush=True)
 return result
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('case');p.add_argument('--portable',action='store_true');a=p.parse_args();run(a.case,a.portable)
