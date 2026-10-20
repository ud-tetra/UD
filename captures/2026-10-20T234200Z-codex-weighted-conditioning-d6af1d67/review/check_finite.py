#!/usr/bin/env python3
"""Independent fixed-frame residual and full temporal Gram reconstruction.
Source is rebuilt grade-by-grade. Time balls use a complex geometric series,
not the producer sine quotient. No producer checker or archived program runs.
"""
from pathlib import Path
import json,gzip,hashlib,zipfile,gc
import numpy as np
from scipy.sparse import csr_matrix
from flint import fmpz_mat,acb,arb,ctx
P=Path(__file__).resolve().parent;W=P.parent;ctx.prec=192
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
F=json.loads((W/'c27_work/PROPOSAL_FREEZE.json').read_text());Qpath=W/'c27_work/Q_DYADIC.bin.gz';Qhash=sha(Qpath)
raw=gzip.decompress(Qpath.read_bytes());assert Qhash==F['Q_gzip_sha256'] and hashlib.sha256(raw).hexdigest()==F['Q_decoded_sha256'];Q=np.frombuffer(raw,dtype='<i8').reshape(2640,1999);assert np.max(np.abs(Q))<=2**40
source=W/'ud-repo/captures/2026-10-17T184000Z-codex-session-publication-7f4a2d91/recovered/UD_600CELL_VERTEX_LINK_OBSERVABILITY_v0.1.zip'
with zipfile.ZipFile(source)as z:
 S=json.loads(z.read('sources/COMPLEX_AND_ACTION.json'))['simplices'];obs=json.loads(z.read('modular_results.json'))['observed_indices']
S=[[tuple(t)for t in g]for g in S];sizes=list(map(len,S));assert sizes==[120,720,1200,600];off=[0,120,840,2040,2640];ix=[{t:i for i,t in enumerate(g)}for g in S];J=set([0,9,227,432,447,582,538,347,332,141]);SQ=np.zeros(Q.shape,dtype=np.int64)
for k in range(1,4):
 rows=[];cols=[];vals=[]
 for j,t in enumerate(S[k]):
  for l in range(k+1):
   rows.append(ix[k-1][t[:l]+t[l+1:]]);cols.append(j);vals.append((-1)**l*(3 if k==3 and j in J else 2))
 B=csr_matrix((vals,(rows,cols)),shape=(sizes[k-1],sizes[k]),dtype=np.int64)
 SQ[off[k-1]:off[k]]-=B@Q[off[k]:off[k+1]]
 SQ[off[k]:off[k+1]]+=B.T@Q[off[k-1]:off[k]]
assert int(np.max(np.abs(SQ)))<=24*2**40
omega=F['frequency_integers'];assert len(omega)==1000 and omega[0]==0
# E integer numerator uses common denominator2^80.
e2=0
for st in range(0,2640,32):
 x=SQ[st:st+32].astype(object)*2**39;q=Q[st:st+32].astype(object)
 x[:,1:1000]+=q[:,1000:]*np.array(omega[1:],dtype=object)
 x[:,1000:]-=q[:,1:1000]*np.array(omega[1:],dtype=object)
 e2+=sum(int(v)**2 for v in x.flat)
assert e2<2**112
print('exact model residual PASS',flush=True)
QM=fmpz_mat(Q.tolist());QtQ=QM.transpose()*QM
q2=sum((int(QtQ[i,j])-(2**80 if i==j else 0))**2 for i in range(1999)for j in range(1999));assert q2*256<2**160
del QM,QtQ,SQ;gc.collect();print('exact frame Gram PASS',flush=True)
# Validate saved time-kernel integers using another algebraic formula.
kpath=W/'c27_cert/TIME_KERNELS.json.gz';khash=sha(kpath);kr=json.loads(gzip.decompress(kpath.read_bytes()));centers=F['distinct_frequency_integers'];ng=len(centers);assert ng==120 and len(kr)==ng*ng
phase_cache={}
def geom(d):
 if d not in phase_cache:
  if d==0:phase_cache[d]=acb(1)
  else:
   z=acb(0,arb(int(d))/2**41).exp()
   phase_cache[d]=(1-z**4096)/(4096*(1-z))
 return phase_cache[d]
kernels={};kernel_checks=0
for row in kr:
 i,j,*v=row;assert 0<=i<ng and 0<=j<ng and (i,j)not in kernels
 a=geom(centers[i]-centers[j]);b=geom(centers[i]+centers[j])
 balls=[(a.real+b.real)/2,(a.real-b.real)/2,(b.imag-a.imag)/2,(b.imag+a.imag)/2]
 for ball,t in zip(balls,v):
  assert abs(ball-arb(t)/2**60)<arb(1)/2**59;kernel_checks+=1
 kernels[i,j]=v
print('independent geometric-series ball checks PASS',flush=True)
# Literal cosine/sine coefficients for each of the1999 state columns:
# u columns: A*cos-B*sin; v columns: B*cos+A*sin.
RQ=Q[obs];A=RQ[:,:1000];B=np.zeros((62,1000),dtype=np.int64);B[:,1:]=RQ[:,1000:]
ca=np.hstack([A,B[:,1:]]);sa=np.hstack([-B,A[:,1:]]);mode=list(range(1000))+list(range(1,1000));groups=F['frequency_group_indices'];AM=fmpz_mat(ca.tolist());BM=fmpz_mat(sa.tolist())
with np.load(W/'c27_cert/GRAM_MIDPOINT.npz',allow_pickle=False)as z:G0=z['matrix']
assert G0.shape==(1999,1999) and G0.dtype==np.dtype('int64') and np.array_equal(G0,G0.T)
checks=0;coeffmax=0
for st in range(0,1999,64):
 en=min(st+64,1999);a=fmpz_mat(ca[:,st:en].T.tolist());b=fmpz_mat(sa[:,st:en].T.tolist())
 aa=a*AM;ab=a*BM;ba=b*AM;bb=b*BM
 for ii in range(en-st):
  i=st+ii;gi=groups[mode[i]]
  for j in range(1999):
   cc,ss,cs,sc=kernels[gi,groups[mode[j]]];co=[int(aa[ii,j]),int(ab[ii,j]),int(ba[ii,j]),int(bb[ii,j])];coeffmax=max(coeffmax,*map(abs,co))
   val=(co[0]*cc+co[1]*cs+co[2]*sc+co[3]*ss)//2**80
   assert val==int(G0[i,j]);checks+=1
assert coeffmax<=2*2**80 and 1999*17<2**16
original=json.loads((W/'c27_cert/ARITHMETIC_DIAGNOSTICS.json').read_text())
assert q2==int(original['Q_orthogonality_squared_numerator']) and e2==int(original['intertwining_residual_squared_numerator']) and coeffmax==int(original['Gram_coefficient_max_numerator'])
assert sha(Qpath)==Qhash and sha(kpath)==khash
r={'status':'PASS_INDEPENDENT_FIXED_FRAME_RESIDUAL_AND_FULL_GRAM','Q_orthogonality_squared_numerator':str(q2),'Q_orthogonality_squared_denominator_power2':160,'equation_residual_squared_numerator':str(e2),'equation_residual_squared_denominator_power2':160,'coefficient_max_numerator':str(coeffmax),'coefficient_denominator_power2':80,'all_Gram_entries_reconstructed':checks,'time_kernel_individual_ball_checks':kernel_checks,'phase_formula':'(1-exp(i theta)^M)/(M*(1-exp(i theta))) at192bits; theta=delta/2^41; zero special-cased','stable_input_endpoint_hashes_match':True,'inputs':{'Q_gzip_sha256':Qhash,'proposal_freeze_sha256':sha(W/'c27_work/PROPOSAL_FREEZE.json'),'time_kernel_gzip_sha256':khash,'Gram_midpoint_npz_sha256':sha(W/'c27_cert/GRAM_MIDPOINT.npz'),'source_archive_sha256':sha(source)},'scope':{'no_producer_checker_or_archived_code_execution':True,'model_source_rebuilt_grade_by_grade':True,'cross_channel_terms_all_included':True,'Gram_eigenproposal_identity':'NOT_CHECKED_IN_THIS_STAGE','physical_promotion':0,'external_review':'PENDING'}}
(P/'FINITE_CHECKS.json').write_text(json.dumps(r,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':r['status'],'Gram_entries':checks,'kernel_checks':kernel_checks}))
