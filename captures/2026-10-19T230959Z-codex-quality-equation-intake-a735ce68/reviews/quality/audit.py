"""Post-known independent arithmetic review, no constructor module imported."""
import os,sys
os.environ.setdefault('OPENBLAS_NUM_THREADS','1');sys.dont_write_bytecode=True
import argparse,json,hashlib,io,zipfile
from pathlib import Path
import numpy as np
from flint import fmpz_mat,arb_mat,arb,fmpq,ctx
ctx.prec=640
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def fm(a):return fmpz_mat([[int(x) for x in row] for row in a])
def decode(a):
 pairs=[float(x).as_integer_ratio() for x in a.flat];b=max(d.bit_length()-1 for n,d in pairs)
 return np.array([n*2**(b-(d.bit_length()-1)) for n,d in pairs],object).reshape(a.shape),b
def read(repo,row):
 assert sha(repo/row['archive'])==row['archive_sha256']
 with zipfile.ZipFile(repo/row['archive']) as z:blob=z.read(row['member'])
 assert hashlib.sha256(blob).hexdigest()==row['sha256']
 with np.load(io.BytesIO(blob),allow_pickle=False) as z:return {k:z[k].copy() for k in z.files}
def lower_proof(D,bits,ln,rn):
 A=arb_mat([[arb(fmpq(int(x),2**bits)) for x in row] for row in D]);J=A.inv();entries=[J[i,j].mid().man_exp() for i in range(210) for j in range(210)];kb=max(0,max(-int(e) for m,e in entries));ki=np.array([int(m)*2**(int(e)+kb) for m,e in entries],object).reshape(210,210)
 # Exact residual of a dyadic inverse proposal; interval inversion is only a proposer.
 residue=fm(D)*fm(ki)-fmpz_mat([[2**(bits+kb)*int(i==j) for j in range(210)] for i in range(210)])
 r2=sum(int(residue[i,j])**2 for i in range(210) for j in range(210));k2=sum(int(x)**2 for x in ki.flat)
 rho=arb(fmpq(r2,2**(2*(bits+kb)))).sqrt();kn=arb(fmpq(k2,2**(2*kb))).sqrt()
 assert rho<1
 lb=(1-rho)/(kn*ln*rn)
 return lb,rho,kn,r2,kb

def main():
 p=argparse.ArgumentParser();p.add_argument('--repo',required=True);p.add_argument('--producer',required=True);p.add_argument('--results',required=True);p.add_argument('--baseline',required=True);p.add_argument('--out',required=True);a=p.parse_args();repo=Path(a.repo);prod=Path(a.producer);res=Path(a.results);base=Path(a.baseline);out=Path(a.out);assert not out.exists();out.mkdir()
 fr=json.loads((prod/'FREEZE.json').read_text());assert sha(prod/'counterexample.py')==fr['code_sha256'];assert sha(base)==fr['baseline_sha256'];src={r['label']:read(repo,r) for r in fr['members']};U=np.concatenate((src['ua']['basis'],src['ub']['basis']),axis=0);ui,bu=decode(U);assert bu==77
 H=np.array(src['gram']['cross_gram_decimal'],object);H=np.array([[int(x) for x in r] for r in H],object);G=fm(ui).transpose()*fm(ui)
 v=np.pad(np.array(json.loads((repo/fr['null_path']).read_text())['vector'],np.int64),(0,1974));A=np.column_stack((2*np.random.default_rng(172026).choice([-1.,1.],size=(2294,160)).astype(np.int64),v,2*np.random.default_rng(184052).choice([-1.,1.],size=(2294,160)).astype(np.int64)));u=np.array([1-2*(t%2) for t in range(8191)],object)
 raw=np.memmap(base,dtype='<i8',mode='r',shape=(37,8191,62));uY=np.empty((62,37),object)
 for prep in range(37):uY[:,prep]=(np.array(raw[prep],object)*u[:,None]).sum(axis=0)
 direct_alt=fm(uY.reshape(1,2294))*fm(A);cu=fm(ui).transpose()*fm(u.reshape(-1,1));left=np.empty((210,210),object)
 for i in range(209):
  for j in range(209):left[i,j]=int(G[i,j])
  left[i,209]=left[209,i]=int(cu[i,0])*2**70
 left[209,209]=8191*2**140
 L=arb(fmpq(max(sum(abs(int(x)) for x in r) for r in left),2**154)).sqrt();rows=[]
 for count in (1,2):
  with np.load(res/f'TEST_FRAME_{count}.npz',allow_pickle=False) as z:W=z['w'];R=z['right'];savedD=z['compression_decimal'];savedLG=z['left_gram_decimal'];savedRG=z['right_gram_decimal']
  expected=np.zeros((62,37),np.int64)
  for prep in range(37):
   for c in sorted(range(62),key=lambda c:(-abs(int(v[c*37+prep])),c))[:count]:expected[c,prep]=1 if v[c*37+prep]>=0 else -1
  assert np.array_equal(W,expected.reshape(-1));squared=[sum(int(x)**2 for x in expected[:,p]) for p in range(37)];assert squared==[count]*37 and 4*count<=9
  ri,br=decode(R);bi=fm(expected.reshape(1,2294))*fm(A);biRi=bi*fm(ri);Hr=fm(H)*fm(ri)
  d=np.empty((210,210),object)
  # Distribute the rank-one update after multiplying test columns, unlike constructor.
  for i in range(209):
   for j in range(210):d[i,j]=int(Hr[i,j])+int(cu[i,0])*int(biRi[0,j])
  base_last=direct_alt*fm(ri)
  for j in range(210):d[209,j]=(int(base_last[0,j])+8191*int(biRi[0,j]))*2**70
  assert np.array_equal(np.array(d,dtype=str),savedD);assert np.array_equal(np.array(left,dtype=str),savedLG)
  rg=fm(ri).transpose()*fm(ri);assert all(int(savedRG[i,j])==int(rg[i,j]) for i in range(210) for j in range(210));rn=arb(fmpq(max(sum(abs(int(rg[i,j])) for j in range(210)) for i in range(210)),2**(2*br))).sqrt();lb,rho,kn,r2,kb=lower_proof(d,132+br,L,rn);assert lb>arb(fmpq(1,2**41))
  rawhash=hashlib.sha256()
  for prep in range(37):
   block=np.array(raw[prep],object)+u[:,None]*expected[:,prep][None,:];assert all(-(2**63)<=int(x)<2**63 for x in block.flat);rawhash.update(np.array(block,dtype='<i8').tobytes())
  original=json.loads((res/'CERTIFICATE.json').read_text())['rows'][count-1];assert rawhash.hexdigest()==original['raw_int64le_sha256']
  rows.append({'id':original['id'],'raw_hash':rawhash.hexdigest(),'local_squared_norm':count,'exact_alternate_compression_entries_checked':44100,'readable_independent_sigma210_lower':float(lb.lower()),'exact_inverse_proposal_residual_squared_integer':str(r2),'inverse_scale_bits':kb,'readable_exact_inverse_residual_upper':float(rho.upper()),'strict_above_2neg41':True})
 controls={'zero_or_negative_lower_refused':not(arb(0)>arb(fmpq(1,2**41))),'cap_equality_refused':not(arb(fmpq(1,2**41))>arb(fmpq(1,2**41))),'three_units_outside_local_ball':not(4*3<=9),'coordinate_two_outside_local_ball':not(4*4<=9),'wrong_source_hash_refused':hashlib.sha256(b'corrupt source').hexdigest()!=fr['baseline_sha256']};assert all(controls.values())
 receipt={'status':'PASS_SEPARATE_SAME_TEAM_EXACT_COMPRESSION_AND_INVERSE_RESIDUAL_REVIEW','producer_freeze_sha256':sha(prod/'FREEZE.json'),'producer_certificate_sha256':sha(res/'CERTIFICATE.json'),'review_code_sha256':sha(__file__),'rows':rows,'controls':controls,'source_cross_Gram':'Inherited exact source receipt retained; not recomputed all8191 rows this review','new_estimator_calls':0,'source_or_factor_copies_saved':False,'scope':'Uniform retained-rank209 approximation-cap feasibility counterexample only; no phase-failure/backendfailure/physical claim','physical_promotion':0,'external_review':'PENDING'};(out/'REVIEW_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt))
if __name__=='__main__':main()
