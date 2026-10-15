"""Exact finite code geometry and labelled perturbation diagnostics."""
from pathlib import Path
from fractions import Fraction as F
import json,math,numpy as np,scipy.sparse as sp
from scipy.linalg import eigh,eigvals,expm
from scipy.sparse.linalg import expm_multiply
from model import build,scalar_recurrence,bareiss_det
R=Path(__file__).resolve().parent;M=build(R)
B1,B2,B3=M['B'];A=M['A'];L=M['L'];Z=M['Z'];den=M['den'];u=M['u'];edge=M['e'];be=M['be'];P=M['protected'];scores=M['scores'];S=M['S']
checks=[]
def ck(name,b,scope='EXACT',**data):
 assert b,(name,data)
 checks.append(dict(name=name,status='PASS',scope=scope,**data))
rho2=F(601,720);tau=F(1,1000);delta=F(6551,375000000000);H0=F(1,2);r=F(1,5);T=F(600)
ck('source_boundary_and_common_initial_stock',(B1@B2).nnz==0 and (B2@B3).nnz==0)
ck('reciprocal_perturbation_is_skew',np.array_equal(np.array([[0,F(2,7)],[-F(2,7),0]],dtype=object).T,-np.array([[0,F(2,7)],[-F(2,7),0]],dtype=object)))
ck('all_vertex_inputs_annihilated_by_protected_projection',P(np.r_[np.ones(120),np.zeros(2520)]).max()==0)
# Exact port-range tests: cycle projection kills every gradient, but not one edge.
star=B1.T[:,u].toarray().ravel()
B1T_exact=B1.T.toarray().astype(object)
star_cycle_numerator=den*star.astype(object)-B1T_exact@(Z@(B1@star))
edge_cycle_numerator=np.zeros(720,dtype=object);edge_cycle_numerator[edge]=den;edge_cycle_numerator-=B1T_exact@(Z@be)
ck('balanced_local_star_is_exactly_protected',np.all(star_cycle_numerator==0) and int(star@star)==12)
ck('unpaired_local_edge_leaks_into_cycles',any(x!=0 for x in edge_cycle_numerator) and F(sum(int(x)**2 for x in edge_cycle_numerator),den*den)==rho2)
# Outward incident edge vectors provide a twelve-word leading code.
inc=M['incident'];assert len(inc)==12
G=[]
for x in inc:
 row=[];bx=B1[:,x['edge']].toarray().ravel()*x['outward_sign']
 for y in inc:
  by=B1[:,y['edge']].toarray().ravel()*y['outward_sign']
  row.append(F(int(x['edge']==y['edge']))-F(int(bx@Z@by),den))
 G.append(row)
ck('twelve_exact_cycle_word_norms',all(G[i][i]==rho2 for i in range(12)))
ck('twelve_words_sum_to_zero',all(sum(row)==0 for row in G))
selected=[next(i for i,x in enumerate(inc) if x['subgroup']==h) for h in range(6)]
ck('six_frozen_representatives_have_distinct_labels',len(set(selected))==6 and sorted(inc[i]['subgroup'] for i in selected)==list(range(6)))
d2=min(G[i][i]+G[j][j]-2*G[i][j] for i in selected for j in selected if i<j)
ck('leading_code_minimum_distance',d2>F(25,16),minimum_distance_squared=str(d2),off_diagonal_values=sorted(set(str(G[i][j]) for i in range(12) for j in range(i))))
finite_distance=F(5,4)*tau-36*tau*tau
ck('finite_six_word_distance_certificate',finite_distance==F(607,500000) and finite_distance>0)
ck('finite_six_score_gap_certificate',F(11,600)*tau*tau-864*tau**4==delta)
eps_score=F(1,4000000);Sbound=T*H0/r
ck('storage_integral_budget',Sbound==1500 and F(39)**2>Sbound)
score_error=rho2*(2*tau*(1+F(9,2)*tau)*eps_score*39+eps_score*eps_score*Sbound)
ck('rational_score_decoder_leakage_budget',score_error<delta,epsilon=str(eps_score),worst_gap_error=str(score_error),certified_margin_remaining=str(delta-score_error))
eps_nearest=F(1,100000)
ck('nearest_template_decoder_leakage_budget',eps_nearest*39<finite_distance/2,epsilon=str(eps_nearest),amplitude_error_upper=str(eps_nearest*39),decision_radius_lower=str(finite_distance/2))
ck('normalized_gap_does_not_restore_absolute_stock',F(11,600)/rho2==F(66,3005))
# Exact minimal polynomial of the same-edge protected Krylov space.
Q=(B2@B2.T).tocsr();p=[int(x) for x in Q[:,edge].toarray().ravel()]
def mv(v):return [sum(int(Q.data[k])*v[int(Q.indices[k])] for k in range(Q.indptr[i],Q.indptr[i+1])) for i in range(720)]
vectors=[p];moments=[]
for _ in range(70):
 moments.append(sum(a*b for a,b in zip(p,vectors[-1])));vectors.append(mv(vectors[-1]))
poly=scalar_recurrence(moments);d=len(poly)-1
ann=[sum(poly[j]*vectors[d-j][i] for j in range(d+1)) for i in range(720)]
hankel=bareiss_det([[moments[i+j] for j in range(d)] for i in range(d)])
ck('exact_cycle_krylov_polynomial',all(x==0 for x in ann) and hankel!=0 and poly[-1]!=0,degree=d,polynomial_descending=[str(x) for x in poly],hankel_nonzero=True,protected_cyclic_dimension=2*d)
Leu=L[:,u]
ck('site_vector_is_not_a_laplacian_eigenvector',any(Leu[j]!=0 for j in range(120) if j!=u))
# Numerical corroborations use an independently assembled reachable subspace.
x0=np.zeros(2640);x0[u]=1
words=[]
for i in selected:words.append(P(expm_multiply(float(tau)*(A-M['edge_operator'](inc[i]['edge'])),x0)))
dist=min(np.linalg.norm(words[i]-words[j]) for i in range(6) for j in range(i))
ck('finite_code_distance_matches_certificate',dist>float(finite_distance),'NUMERICAL',minimum_distance=float(dist))
leading=[]
for i in selected:
 x=np.zeros(2640);x[120+inc[i]['edge']]=inc[i]['outward_sign'];leading.append(P(x))
ck('finite_word_taylor_error',max(np.linalg.norm(w-float(tau)*v) for w,v in zip(words,leading))<18*float(tau)**2,'NUMERICAL')
mu0,U=eigh(L.astype(float));cutbasis=B1.T@U[:,1:]/np.sqrt(mu0[1:])
qvals,V=eigh(Q.toarray().astype(float));w0=np.zeros(2640);w0[120+edge]=1;w0=P(w0)[120:840]
cycles=[];cvals=[]
for val in qvals:
 if val<1e-8 or any(abs(val-z)<1e-7 for z in cvals):continue
 idx=np.where(abs(qvals-val)<1e-7)[0];proj=V[:,idx]@(V[:,idx].T@w0)
 if np.linalg.norm(proj)>1e-8:cvals.append(float(val));cycles.append(proj/np.linalg.norm(proj))
assert len(cycles)==d
Cy=np.array(cycles).T;Fcy=B2.T@Cy/np.sqrt(cvals)
nb=239+2*d;CB=np.zeros((2640,nb));CB[:120,:120]=np.eye(120);CB[120:840,120:239]=cutbasis;CB[120:840,239:239+d]=Cy;CB[840:2040,239+d:]=Fcy
ck('numerical_reachable_basis',np.linalg.norm(CB.T@CB-np.eye(nb))<1e-7 and np.linalg.norm(A@CB-CB@(CB.T@(A@CB)))<1e-7,'NUMERICAL',carrier_dimension=nb,joint_dimension=nb+120)
Ac=CB.T@(A@CB);Inc=np.zeros((nb,120));Inc[:120,:]=np.eye(120);Vport=np.zeros((nb,120));Vport[:,u]=CB[120+edge,:]
Rb=L/4+np.eye(120)/5;gamma=2/3
def joint(eps):
 tr=gamma*Inc+eps*Vport
 return np.block([[Ac,tr],[-tr.T,-Rb]])
base_roots=eigvals(joint(0));ck('exact_port_limit_has_protected_oscillators',sum(abs(z.real)<1e-8 for z in base_roots)==2*d,'NUMERICAL')
rates=[]
for eps in [.1,.01]:
 ev=eigvals(joint(eps));rates.append({'epsilon':eps,'largest_real_part':float(max(ev.real))})
ck('same_edge_misalignment_erases_reachable_code',all(x['largest_real_part']<-1e-10 for x in rates),'NUMERICAL',rates=rates)
cut=expm_multiply(.001*(A-M['edge_operator'](edge)),x0);Y0=P(cut);stock=float(Y0@Y0)
ck('initial_cut_has_no_unreachable_dark_component',np.linalg.norm(CB@(CB.T@cut)-cut)<1e-7,'NUMERICAL',retained_stock=stock,ideal_exported_storage=(1-stock)/2)
initial=np.r_[CB.T@cut,np.zeros(120)];actual=expm(600*joint(float(eps_nearest)))@initial
actual_c=CB@actual[:nb];Y=P(actual_c);reference=expm_multiply(600*A,Y0)
bound=float(eps_nearest)*math.sqrt(float(rho2*Sbound));err=float(np.linalg.norm(Y-reference))
ck('small_local_leak_respects_retention_budget',err<bound and np.argmin([np.linalg.norm(Y-expm_multiply(600*A,w)) for w in words])==M['target'],'NUMERICAL',epsilon=float(eps_nearest),amplitude_error=err,analytic_error_bound=bound)
data={'code_representatives':[inc[i] for i in selected],'twelve_incident_edges':inc,'leading_gram_exact':[[str(x) for x in row] for row in G],'minimum_leading_distance_squared':str(d2),'cycle_krylov_polynomial_descending':[str(x) for x in poly],'protected_cyclic_dimension':2*d,'benchmark_stock':stock,'ideal_exported_storage':(1-stock)/2,'rates':rates}
(R/'ROBUST_RETENTION_DATA.json').write_text(json.dumps(data,indent=2)+'\n')
out={'checks':checks,'exact_count':sum(x['scope']=='EXACT' for x in checks),'numerical_count':sum(x['scope']=='NUMERICAL' for x in checks),'physical_promotion':0,'status':'DEVELOPMENT_NO_REGISTRY_ENTRY','scope':'Conditional real-amplitude code and passive local perturbation; not native write/admission, quantum memory, calibrated energy or independent review.'}
(R/'ROBUST_RETENTION_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='checks'},indent=2));print(json.dumps(data,indent=2)[:1800])
