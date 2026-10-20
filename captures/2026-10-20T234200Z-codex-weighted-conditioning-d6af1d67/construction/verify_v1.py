#!/usr/bin/env python3
"""Exact residual/Arb time-sum conditioning certificate for PR305.
Eigensolver supplies only a trial V,d. All acceptance inequalities use exact
integer products and validated Arb balls. No full sampled history or Hankel.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,zipfile,gzip,hashlib,math,gc
import numpy as np
from scipy.sparse import csr_matrix
from scipy.linalg import eigh
from flint import fmpz_mat,arb,ctx

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--repo',required=True,type=Path);ap.add_argument('--evidence',required=True,type=Path);ap.add_argument('--out',required=True,type=Path);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=False);ctx.prec=160
 H=lambda b:hashlib.sha256(b).hexdigest();n=2640;r=1999;m=1000;M=4096;qbits=40;kb=60;vb=40
 p=json.loads((a.evidence/'PROPOSAL_FREEZE.json').read_text());packed=(a.evidence/'Q_DYADIC.bin.gz').read_bytes();assert H(packed)==p['Q_gzip_sha256'];raw=gzip.decompress(packed);assert len(raw)==n*r*8 and H(raw)==p['Q_decoded_sha256'];Q=np.frombuffer(raw,dtype='<i8').reshape(n,r);assert np.max(np.abs(Q))<=2**40
 assert p['shape']==[n,r]and p['coordinate_scale_denominator_power2']==qbits and p['frequency_scale_denominator_power2']==40
 w=np.array(p['frequency_integers'],dtype=np.int64);groups=p['frequency_group_indices'];centers=p['distinct_frequency_integers'];assert len(w)==len(groups)==1000 and w[0]==0 and all(w[i]==centers[groups[i]]for i in range(m));assert all(0<=x<5*2**40 for x in w)
 Z=a.repo/'captures/2026-10-17T184000Z-codex-session-publication-7f4a2d91/recovered/UD_600CELL_VERTEX_LINK_OBSERVABILITY_v0.1.zip';assert H(Z.read_bytes())=='d80fc253a77b59b72a387a0db63eb5a60563c2d1f7563e12f9570172d69e087b'
 members={'sources/COMPLEX_AND_ACTION.json':'1e8a15425fa80e5d500370a51a1b7c8605dfab5befe61824d47c07ec8fb35575','modular_results.json':'e7955b36d396b77ab35a97d02af8e1badac6ac031181653dfac682b248647ee5'}
 with zipfile.ZipFile(Z)as z:
  data={k:z.read(k)for k in members};assert all(H(data[k])==v for k,v in members.items())
 C=json.loads(data['sources/COMPLEX_AND_ACTION.json']);obs=json.loads(data['modular_results.json'])['observed_indices'];assert len(obs)==62 and len(set(obs))==62
 S=[[tuple(s)for s in g]for g in C['simplices']];assert list(map(len,S))==[120,720,1200,600];ix=[{s:i for i,s in enumerate(g)}for g in S];off=[0,120,840,2040];J={0,9,227,432,447,582,538,347,332,141};rr=[];cc=[];dd=[]
 for k in [1,2,3]:
  for j,s in enumerate(S[k]):
   weight=3 if k==3 and j in J else 2
   for b in range(k+1):
    i=ix[k-1][s[:b]+s[b+1:]];u=off[k-1]+i;v=off[k]+j;c=weight*(-1)**b;rr.extend([u,v]);cc.extend([v,u]);dd.extend([-c,c])
 # S_int=2K, actual source sign upper−B/lower+Btranspose.
 Sint=csr_matrix((np.array(dd,dtype=np.int64),(rr,cc)),shape=(n,n));assert np.max(np.asarray(abs(Sint).sum(axis=1)))<=24
 # Exact Q norm certificate. All products below use arbitrary-precision integers.
 print('exact Q orthogonality',flush=True);QI=fmpz_mat(Q.tolist());Qg=QI.transpose()*QI
 q2=sum((int(Qg[i,j])-(2**80 if i==j else 0))**2 for i in range(r)for j in range(r));assert q2*256<2**160
 del Qg,QI;gc.collect();print('exact intertwining residual',flush=True)
 # S Q uses int64 safely: row1norm<=24, each|Q|<=2^40. No overflow.
 # E=KQ−QJ has common denominator2^80, with J upper+omega.
 e2=0
 for start in range(0,n,32):
  sq=(Sint[start:start+32]@Q).astype(object)*(2**39);qq=Q[start:start+32].astype(object);qj=np.zeros(qq.shape,dtype=object);qj[:,1:m]=-qq[:,m:]*w[1:];qj[:,m:]=qq[:,1:m]*w[1:];E=sq-qj;e2+=sum(int(x)**2 for x in E.flat)
 assert e2<2**112 # ||E||F<2^-24
 print('exact readout coefficients',flush=True)
 RQ=Q[obs];AAi=fmpz_mat(RQ[:,:m].tolist());BB=np.zeros((62,m),dtype=np.int64);BB[:,1:]=RQ[:,m:];BBi=fmpz_mat(BB.tolist());AA=AAi.transpose()*AAi;AB=AAi.transpose()*BBi;BBm=BBi.transpose()*BBi
 coeffmax=max(abs(int(A[i,j]))for A in [AA,AB,BBm]for i in range(m)for j in range(m));assert coeffmax<=2*2**80
 print('validated time kernels',len(centers),flush=True)
 def meanphase(delta):
  if delta==0:return arb(1),arb(0)
  t=arb(int(delta))/(2**42);quot=(M*t).sin()/(M*t.sin());ang=(M-1)*t;return quot*ang.cos(),quot*ang.sin()
 def quant(x):
  k=int((x*(2**60)).mid().floor().unique_fmpz());assert abs(x-arb(k)/(2**60))<arb(1)/(2**59);assert abs(k)<=2**60+2;return k
 kernels={};kernel_rows=[]
 for gi,x in enumerate(centers):
  for gj,y in enumerate(centers):
   dr,di=meanphase(x-y);pr,pi=meanphase(x+y);vals=[quant((dr+pr)/2),quant((dr-pr)/2),quant((pi-di)/2),quant((pi+di)/2)];kernels[gi,gj]=vals;kernel_rows.append([gi,gj,*vals])
 kernel_blob=(json.dumps(kernel_rows,separators=(',',':'))+'\n').encode();print('exact full Gram midpoint',flush=True)
 G0=np.empty((r,r),dtype=np.int64)
 def dot(i,j,typ):
  c,s,cs,sc=kernels[groups[i],groups[j]];aa=int(AA[i,j]);ab=int(AB[i,j]);ba=int(AB[j,i]);bb=int(BBm[i,j])
  if typ==0:v=aa*c-ab*cs-ba*sc+bb*s
  elif typ==1:v=aa*cs+ab*c-ba*s-bb*sc
  else:v=aa*s+ab*sc+ba*cs+bb*c
  return v//(2**80)
 for i in range(r):
  ii=i if i<m else i-m+1
  for j in range(i,r):
   jj=j if j<m else j-m+1;typ=0 if j<m else(1 if i<m else 2);v=dot(ii,jj,typ);assert abs(v)<2**61;G0[i,j]=G0[j,i]=v
 # Each kernelerror<2^-59, each of4coeffs<=2. Entry rounding<2^-60;
 # hence entryerror<17*2^-60; fullFrob<r*17*2^-60<2^-44.
 assert r*17<2**16
 print('numerical eigenproposal only',flush=True);Gf=G0.astype(float)/(2**60);d,V=eigh(Gf,check_finite=True,driver='evd');VI=np.rint(V*2**40).astype(np.int64);di=np.rint(d*2**60).astype(np.int64);assert np.max(np.abs(VI))<=2**40 and np.max(np.abs(di))<=2**60
 dmin=int(np.min(di));assert dmin>9*2**40 # min(di/2^60)>9*2^-20
 print('exact eigenproposal orthogonality',flush=True);VM=fmpz_mat(VI.tolist());Vg=VM.transpose()*VM;v2=sum((int(Vg[i,j])-(2**80 if i==j else 0))**2 for i in range(r)for j in range(r));assert v2*256<2**160;del Vg;gc.collect()
 print('exact full Gram eigen-residual',flush=True);GI=fmpz_mat(G0.tolist());B=GI*VM;b2=sum((int(B[i,j])-int(VI[i,j])*int(di[j]))**2 for i in range(r)for j in range(r));assert b2<2**156 # denominator2^100; ||B||F<2^-22
 # Full-spectrum bound applies first to symmetric G0, then Weyl to true G.
 assert F(9,2**20)-F(1,2**21)-F(1,2**44)>F(1,2**17)
 assert F((M-1)*(2*M-1),24)<2**22
 assert (F(1,384)-F(1,8192))/F(9,8)==F(61,27648)>F(1,512)
 # Eigh proposals affect no model coefficients and are accepted only after exact tests.
 exact={'Q_orthogonality_squared_numerator':str(q2),'Q_orthogonality_squared_denominator_power2':160,'intertwining_residual_squared_numerator':str(e2),'intertwining_residual_squared_denominator_power2':160,'Gram_coefficient_max_numerator':str(coeffmax),'Gram_coefficient_denominator_power2':80,'Gram_eigenproposal_min_diagonal_numerator':str(dmin),'Gram_eigenproposal_diagonal_denominator_power2':60,'V_orthogonality_squared_numerator':str(v2),'V_orthogonality_squared_denominator_power2':160,'Gram_eigen_residual_squared_numerator':str(b2),'Gram_eigen_residual_squared_denominator_power2':200}
 # Exact numerical residual values depend on the proposal solver. The scientific
 # certificate records fixed conservative inequalities; diagnostics are separate.
 result={'status':'PASS_VALIDATED_FULL_OBSERVABLE_QUOTIENT_CONDITIONING','model':'PR305 epsilon1/2 C10 orbit; unchanged62 observer; unit Euclidean coordinates','map':'4096^-1/2 stack_j R exp(jK_D/2), j0..4095','inherited_history_and_sample_rank':1999,'inherited_kernel':641,'positive_sigma_lower':'>61/27648>1/512','positive_condition_upper':'<27648/61<512','full_domain_condition':'INFINITE','validated_bounds':{'Q_orthogonality_Frobenius':'<1/16','Q_operator_norm':'<9/8','E_Frobenius':'<2^-24','time_rms':'<2048','trajectory_operator_error':'<1/8192','Gram_entry_error':'<17*2^-60','Gram_operator_error':'<2^-44','V_orthogonality_Frobenius':'<1/16','G0_V_minus_V_d_Frobenius':'<2^-22','min_d':'>9*2^-20','true_Gram_min_eigenvalue':'>2^-17'},'scope':{'numerical_eigensolver_role':'PROPOSAL_ONLY_THEN_EXACT_INTEGER_VERIFICATION','Arb_bits':160,'full_cross_channel_terms_retained':True,'full_Hankel_allocations':0,'new_acquisitions':0,'estimator_calls':0,'old_nominal2029_certificate_transfer':False,'accuracy_noise_calibration_gate_transfer':False,'physical_promotion':0,'external_promotion_review':'PENDING'}}
 bindings={'source_archive_sha256':H(Z.read_bytes()),'source_members':members,'proposal_freeze_sha256':H((a.evidence/'PROPOSAL_FREEZE.json').read_bytes()),'Q_gzip_sha256':H(packed),'time_kernel_midpoints_sha256':H(kernel_blob),'time_kernel_count':len(kernel_rows),'cross_Gram_shape':[r,r]}
 for name,obj in [('RESULT.json',result),('SOURCE_BINDINGS.json',bindings),('ARITHMETIC_DIAGNOSTICS.json',exact)]: (a.out/name).write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')
 (a.out/'TIME_KERNELS.json.gz').write_bytes(gzip.compress(kernel_blob,mtime=0));np.savez_compressed(a.out/'GRAM_MIDPOINT.npz',matrix=G0);print(json.dumps({'status':result['status'],'kappa_upper':'27648/61<512','sigma_lower':'61/27648>1/512'}),flush=True)
if __name__=='__main__':main()
