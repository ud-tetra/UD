"""Exact dyadic coefficient weights, baseline residual, and encoded-ball row norms."""
import argparse,json
from pathlib import Path
import numpy as np
from flint import arb,fmpq
from common import P,freeze,sha,check_evidence,a,up,down
from numeric_math import encode
from proof_math import fm,arr,norm_exact
def sketch(evidence):
 old=np.random.default_rng(172026).choice([-1.,1.],size=(2294,160)).astype(np.int64)
 v=np.pad(np.array(json.loads((evidence/'NULL_VECTOR.json').read_text())['vector'],np.int64),(0,1974))
 new=np.random.default_rng(184052).choice([-1.,1.],size=(2294,160)).astype(np.int64)
 assert int(v@v)==16228 and np.all(v@old==0)
 return np.column_stack((2*old,v,2*new))
def square_sum(m):return sum(int(x)**2 for row in m.tolist() for x in row)
def verify(evidence):
 freeze();evidence=Path(evidence);check_evidence(evidence);pf=json.loads((P/'PROPOSAL_FREEZE.json').read_text());assert sha(P/'INVERSE_PROPOSAL.npz')==pf['sha256']
 with np.load(evidence/'C.npz',allow_pickle=False) as z:cn,bc=encode(z['coefficient'])
 with np.load(P/'INVERSE_PROPOSAL.npz',allow_pickle=False) as z:mn,bm=encode(z['inverse'])
 Cf,Mf=fm(cn),fm(mn);K=Cf.transpose()*Mf;bk=bc+bm;CK=Cf*K
 rho=norm_exact(arr(CK)-np.eye(209,dtype=object)*(1<<(bc+bk)),bc+bk);assert rho<1
 A=sketch(evidence);AK=fm(A)*K;rows=[sum(int(v)**2 for v in row) for row in AK.tolist()]
 maxima=[max(rows[37*c+j] for c in range(62)) for j in range(37)]
 row_bound=sum(arb(x).sqrt() for x in maxima)/(arb(2)**(bk+7));noise_constant=arb(8191).sqrt()*row_bound
 with np.load(evidence/'U_A.npz',allow_pickle=False) as z:ua=z['basis']
 with np.load(evidence/'U_B.npz',allow_pickle=False) as z:ub=z['basis']
 un,bu=encode(np.r_[ua,ub]);Uf=fm(un);G=Uf.transpose()*Uf
 eta0=norm_exact(arr(G)-np.eye(209,dtype=object)*(1<<(2*bu)),2*bu)
 parent=json.loads((P/'inputs/PARENT_UNIFORM.json').read_text());assert eta0<=a(parent['basis_orthogonality_upper'])
 chunks=[]
 for k in range(3):
  with np.load(evidence/f'ANCHOR_{k}.npz',allow_pickle=False) as z:chunks.append(z['numerator'])
 N=np.vstack(chunks);assert N.shape==(8191,321) and N.dtype==np.int64
 # Anchors are the CYCLIC record, not the baseline. Subtract its pinned one-quantum projection exactly.
 protocol=json.loads((evidence/'BASE_PROTOCOL.json').read_text());assert protocol['baseline_sha256']=='25a0888972c8fb961774ef69430070e07e1cf6bd02ca05fd1bb0a5552c6e9f59'
 assert protocol['noise_recipe']=='At preparation a, time k add integer (-1)^(a+floor(k/62)) at channel(a+k)%62; zero elsewhere; quantum2^-48.'
 t=np.arange(8191,dtype=np.int64)
 for j in range(37):N-=np.where((j+t//62)%2==0,1,-1)[:,None]*A[37*((j+t)%62)+j,:]
 receipt=json.loads((evidence/'BASE_PROJECTION.json').read_text());n2=sum(int(v)**2 for v in N.flat)
 assert n2==int(receipt['raw_sketch_norm_squared_integer']) and bu==receipt['basis_scale_bits'] and receipt['raw_sketch_scale_bits']==55
 Nf=fm(N);H=Uf.transpose()*Nf
 # Independently recompute the source's exact unweighted residual as a baseline identity control.
 GC=G*Cf;L=max(110,2*bu+2*bc,bu+55+bc)
 rnum=(n2<<(L-110))+(sum(int(c)*int(gc) for cr,gr in zip(Cf.tolist(),GC.tolist()) for c,gc in zip(cr,gr))<<(L-2*bu-2*bc))-(2*sum(int(c)*int(h) for cr,hr in zip(Cf.tolist(),H.tolist()) for c,h in zip(cr,hr))<<(L-bu-55-bc))
 assert fmpq(rnum,1<<L)==fmpq(*parent['baseline_exact_low_rank_residual_squared'])
 # Direct differences avoid cancellation of floating products. Every product is an integer FLINT product.
 Nk=Nf*K;Uck=Uf*CK;scale=max(55+bk,bu+bc+bk)
 R=Nk*(1<<(scale-55-bk))-Uck*(1<<(scale-bu-bc-bk));weighted_rnum=square_sum(R)
 rk=arb(weighted_rnum).sqrt()/(arb(2)**scale)
 Cnorm=arb(square_sum(Cf)).sqrt()/(arb(2)**bc)
 result={'status':'CERTIFIED_EXACT_SOURCE_WEIGHTED_CONSTANTS','proposal_sha256':pf['sha256'],'right_inverse_residual_F_upper':up(rho),'baseline_weighted_squared':[weighted_rnum,1<<(2*scale)],'baseline_weighted_F_upper':up(rk),'weighted_noise_multiplier_upper':up(noise_constant),'source_coefficient_F_upper':up(Cnorm),'source_Gram_defect_F_upper':up(eta0),'row_square_maxima_decimal':[str(v) for v in maxima],'row_square_scale_bits':2*(bk+7),'baseline_unweighted_squared_control':[rnum,1<<L],'baseline_integer_bytes_sha256':__import__('hashlib').sha256(N.astype('<i8').tobytes()).hexdigest(),'exact_K_scale_bits':bk,'scope':'Encoded quantum onehot ball, exact K=C^T M, corrected CYCLIC anchor; source/parent proof dependencies explicit','readable':{'rho_F':float(rho.upper()),'baseline_weighted_F':float(rk.upper()),'noise_multiplier':float(noise_constant.upper()),'C_F':float(Cnorm.upper()),'eta0_F':float(eta0.upper())},'physical_promotion':0}
 return result
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--evidence',required=True);p.add_argument('--replay',action='store_true');args=p.parse_args();r=verify(args.evidence);q=P/'WEIGHTS_CERTIFICATE.json'
 if args.replay:assert json.loads(q.read_text())==r
 else:assert not q.exists();q.write_text(json.dumps(r,indent=2))
 print(json.dumps({'status':r['status'],'readable':r['readable']}),flush=True)
