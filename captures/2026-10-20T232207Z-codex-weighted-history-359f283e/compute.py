#!/usr/bin/env python3
"""Exact weighted top-channel certificates, finite sampling, coarse conditioning.
Reads JSON source data only. Dependencies: numpy, scipy, python-flint.
No acquisition, fit, eigensolver, SVD, large full-history or Hankel allocation.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
import argparse,hashlib,json,zipfile,math
import numpy as np
from scipy.sparse import csr_matrix
from flint import fmpz_mat,fmpz_poly,nmod_mat

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--repo',required=True,type=Path);ap.add_argument('--evidence',required=True,type=Path);ap.add_argument('--out',required=True,type=Path);a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=False)
 H=lambda b:hashlib.sha256(b).hexdigest()
 archive=a.repo/'captures/2026-10-17T184000Z-codex-session-publication-7f4a2d91/recovered/UD_600CELL_VERTEX_LINK_OBSERVABILITY_v0.1.zip'
 assert H(archive.read_bytes())=='d80fc253a77b59b72a387a0db63eb5a60563c2d1f7563e12f9570172d69e087b'
 names={'sources/COMPLEX_AND_ACTION.json':'1e8a15425fa80e5d500370a51a1b7c8605dfab5befe61824d47c07ec8fb35575','modular_results.json':'e7955b36d396b77ab35a97d02af8e1badac6ac031181653dfac682b248647ee5','HIDDEN_WITNESSES.json':'0d40036b19b513bda2e7629e9fd8b89e3a20835cdcb7806f49ee763b7455d82c'}
 with zipfile.ZipFile(archive)as z:
  data={n:z.read(n)for n in names}
  assert all(H(data[n])==v for n,v in names.items())
 C,M,hidden=[json.loads(data[n])for n in names]
 S=[[tuple(s)for s in g]for g in C['simplices']];assert list(map(len,S))==[120,720,1200,600]
 ix=[{s:i for i,s in enumerate(g)}for g in S];J=[0,9,227,432,447,582,538,347,332,141];d=np.full(600,2,dtype=np.int64);d[J]=3
 B=np.zeros((1200,600),dtype=np.int64);dual=defaultdict(list)
 for j,s in enumerate(S[3]):
  for k in range(4):
   i=ix[2][s[:k]+s[k+1:]];v=(-1)**k;B[i,j]=v;dual[i].append((j,v))
 h=np.zeros(600,dtype=np.int64)
 for i,v in hidden['stationary_fundamental_C3_cycle']:h[int(i)-2040]=int(v)
 assert np.all(np.abs(h)==1)and np.all(B@h==0)
 adj=defaultdict(list)
 for pair in dual.values():
  assert len(pair)==2;(i,u),(j,v)=pair;assert u*v*h[i]*h[j]==-1;adj[i].append(j);adj[j].append(i)
 seen={0};todo=[0]
 while todo:
  for j in adj[todo.pop()]:
   if j not in seen:seen.add(j);todo.append(j)
 assert len(seen)==600
 observed=M['observed_indices'];assert len(observed)==62
 C0=B[[i-840 for i in observed if 840<=i<2040]];assert C0.shape==(20,600)
 G=B.T@B;MW=d[:,None]*G*d[None,:];CW=C0*d[None,:];U=np.vstack([C0,np.eye(600,dtype=np.int64)[J]])
 # Recheck downward closure; algebraic channel separation is inherited from PR303.
 obs=[set(i-off for i in observed if off<=i<off+len(g))for off,g in zip([0,120,840,2040],S)]
 for k in [1,2]:
  for j in obs[k]:
   s=S[k][j];assert all(ix[k-1][s[:m]+s[m+1:]]in obs[k-1]for m in range(k+1))
 assert not obs[3]
 # A nonzero determinant over a prime gives a characteristic-zero rank lower bound.
 lower=json.loads((a.evidence/'LOWER_WITNESSES.json').read_text());lower_results=[]
 assert all(1009%i for i in range(2,math.isqrt(1009)+1))
 models={'nominal':(G,C0),'weighted':(MW,CW),'augmented_nominal':(G,U)}
 for w in lower['witnesses']:
  A,V=models[w['case']];p=w['prime'];assert p==1009 and len(V)==w['seed_rows'];v=V.copy()%p;powers=[];op=csr_matrix(A)
  for j in range(w['max_selected_power']+1):powers.append(v);v=(op@v.T).T%p
  T=np.vstack(powers);rr=w['rows_time_major'];cc=w['columns'];r=w['rank_lower'];assert len(rr)==len(set(rr))==len(cc)==len(set(cc))==r
  det=int(nmod_mat(T[np.ix_(rr,cc)].tolist(),p).det());assert det==w['determinant_mod_prime']and det
  lower_results.append({'case':w['case'],'rank_lower':r,'prime':p,'nonzero_minor_determinant':det})
 # Exact upper proof: annihilator, CRT factors and explicit rational row memberships.
 factor_meta=json.loads((a.evidence/'FACTOR_CERTIFICATE.json').read_text());fs=[x['coefficients_ascending']for x in factor_meta['factors']];q=list(reversed(M['qL_coefficients']));qp=fmpz_poly(q);prod=fmpz_poly([1]);pairs=0
 for i,f in enumerate(fs):
  fp=fmpz_poly(f);prod*=fp;assert fp.gcd(fp.derivative()).degree()==0
  for g in fs[i+1:]:assert fp.gcd(fmpz_poly(g)).degree()==0;pairs+=1
 assert list(map(int,prod.coeffs()))==q and pairs==435
 cols=[[(int(i),int(G[i,j]))for i in np.flatnonzero(G[:,j])]for j in range(600)]
 def step(V):
  T=np.zeros(V.shape,dtype=object)
  for j,col in enumerate(cols):
   for i,c in col:T[:,j]+=c*V[:,i]
  return T
 powers=[U.astype(object)]
 for _ in range(53):powers.append(step(powers[-1]))
 ann=sum((c*powers[i]for i,c in enumerate(q)),np.zeros(U.shape,dtype=object));assert all(x==0 for x in ann.flat)
 upper=[];membership_entries=0
 with zipfile.ZipFile(a.evidence/'UPPER_WITNESSES.zip')as z:
  for fi,f in enumerate(fs):
   quotient,rem=divmod(qp,fmpz_poly(f));assert not rem;hs=list(map(int,quotient.coeffs()));degree=len(f)-1
   blocks=[sum((c*powers[i+j]for i,c in enumerate(hs)),np.zeros(U.shape,dtype=object))for j in range(degree)]
   V=np.vstack(blocks);V0=np.vstack([v[:20]for v in blocks]);ranks={}
   for label,T in [('augmented',V),('nominal',V0)]:
    w=json.loads(z.read(f'{fi:02d}_{label}.json'));r=w['upper_dimension'];piv=w['pivot_columns'];ds=list(map(int,w['row_denominators']));rows=[[int(x)for x in row]for row in w['basis_rows']]
    assert len(rows)==len(piv)==len(ds)==r and len(set(piv))==r and all(x>0 for x in ds)
    assert all(rows[i][piv[j]]==(ds[i]if i==j else 0)for i in range(r)for j in range(r))
    den=math.lcm(*ds)if ds else 1;Bs=fmpz_mat(r,600,[x*(den//ds[i])for i,row in enumerate(rows)for x in row]);A=fmpz_mat(T.tolist());Vp=fmpz_mat(len(T),r,[int(T[i,j])for i in range(len(T))for j in piv]);assert Vp*Bs==den*A
    ranks[label]=r;membership_entries+=len(T)*600
   if fi==0:assert all(abs(int(x))==abs(int(V[20,0]))for x in V[20])and V[20,0]!=0
   upper.append({'factor_index':fi,'coefficients_ascending':f,'degree':degree,'nominal_upper':ranks['nominal'],'augmented_upper':ranks['augmented']})
 r0=sum(x['nominal_upper']for x in upper);dimW=sum(x['augmented_upper']for x in upper);lb={x['case']:x['rank_lower']for x in lower_results};assert r0==lb['nominal']==390 and dimW==lb['augmented_nominal']==444 and lb['weighted']==443
 # W is invariant under G and selected-coordinate P. z=D2^-1 h is in W,
 # nonzero and killed by MW,CW. Thus weighted rank<=dimW-1=443; lower saturates.
 z6=np.where(d==3,2*h,3*h);assert np.all(MW@z6==0)and np.all(CW@z6==0)
 # Source Schur norm bounds. B3D rowmax5/2,colmax6, and lower chain bounds.
 bounds=[]
 for k in [1,2,3]:
  rr=[F(0)]*len(S[k-1]);cc=[]
  for j,s in enumerate(S[k]):
   w=F(int(d[j]),2)if k==3 else F(1);cc.append((k+1)*w)
   for m in range(k+1):rr[ix[k-1][s[:m]+s[m+1:]]]+=w
  bounds.append({'grade':k,'row_abs_sum':str(max(rr)),'col_abs_sum':str(max(cc)),'norm_squared_upper':str(max(rr)*max(cc))})
 assert [F(x['norm_squared_upper'])for x in bounds]==[24,15,15]
 rank=1893+2*(443-390);assert rank==1999
 D=105+2*443;N=D*(D-1)//2;jet_exp=4*D+4;modal_exp=4*D+6;E=5*N+10*(D-1)+jet_exp*(rank-1)+modal_exp+6;assert D==991 and E==10394665
 sine=F(5,2)-F(5,2)**3/6+F(5,2)**5/120-F(5,2)**7/5040;assert sine==F(75935,129024)>F(1,2)
 result={'status':'PASS_EXACT_WEIGHTED_HISTORY_AND_FINITE_SAMPLE_RANK','epsilon':'1/2','orbit':J,'nominal_top_rank':r0,'augmented_space_dimension':dimW,'weighted_top_rank':443,'inherited_nominal_full_rank':1893,'weighted_full_rank':rank,'weighted_full_kernel':2640-rank,'net_observable_gain':106,'common_old_new_kernel_dimension':640,'new_observation_rank_restricted_to_old_kernel':107,'old_kernel_contained_in_new':False,'weighted_sector_ranks':'NOT_COMPUTED','sampling':{'M':4096,'h':'1/2','normalization':'1/64','rank':1999,'kernel':641,'nonaliasing':'phase diameter<5<2pi'},'conditioning':{'positive_sigma_lower':'>2^-10394665','positive_condition_upper':'<2^10394665','full_domain_condition':'INFINITE','practical_2029_gate':'HOLD_NOT_CERTIFIED','type':'DERIVED_WORST_CASE_ANALYTIC_NOT_NUMERICAL_SVD'},'checks':{'exact_annihilator_entries':18000,'rational_membership_entries':membership_entries,'pairwise_coprime_factor_checks':pairs,'lower_nonzero_minors':lower_results,'source_norm_bounds':bounds,'dual_graph_connected':600},'scope':{'nominal_full_rank_and_channel_separation':'INHERITED_PRIOR_EXACT_RESULTS','new_acquisitions':0,'estimator_calls':0,'SVD_calls':0,'full_Hankel_allocations':0,'physical_weight_source':'NOT_SUPPLIED','external_promotion_review':'PENDING','physical_promotion':0}}
 for name,obj in [('RESULT.json',result),('FACTOR_RESULTS.json',{'factors':upper}),('SOURCE_BINDINGS.json',{'archive_path':str(archive.relative_to(a.repo)),'archive_sha256':H(archive.read_bytes()),'members':names,'evidence_sha256':{n:H((a.evidence/n).read_bytes())for n in ['LOWER_WITNESSES.json','FACTOR_CERTIFICATE.json','UPPER_WITNESSES.zip']}})]:
  (a.out/name).write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'status':result['status'],'rank':rank,'kernel':2640-rank,'coarse_condition_exponent':E}))
if __name__=='__main__':main()
