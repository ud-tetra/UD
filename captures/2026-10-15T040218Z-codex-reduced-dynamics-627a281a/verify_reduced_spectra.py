from pathlib import Path
import json
import numpy as np
import scipy.linalg as la
from flint import fmpz_mat,nmod_mat
import sympy as s
from exact_spectra import eval_coeff,transpose_conj,fm,matmul,raw,pows
R=Path(__file__).resolve().parent
records=json.load(open(R/'EXACT_SPECTRA.json'))['m_0_through_5']
checks=[]
def check(name,b,scope='EXACT',**data):
 assert b,name
 checks.append({'name':name,'status':'PASS','scope':scope,**data})
def polyco(expr):
 cs=[]
 for c in s.Poly(expr,s.Symbol('x')).all_coeffs():
  a=s.expand(c).coeff(s.sqrt(5),0);b=s.expand(c).coeff(s.sqrt(5),1)
  t=(a+b,0,2*b,-2*b);assert all(s.denom(v)==1 for v in t);cs.append(tuple(int(v) for v in t))
 return cs
def add_scalar_identity(M,c):
 for k in range(4):
  for i in range(M[k].nrows()):M[k][i,i]+=c[k]
 return M
def evaluate(poly,G):
 n=G[0].nrows();out=[fmpz_mat(n,n) for _ in range(4)]
 for c in poly:out=add_scalar_identity(matmul(out,G),c)
 return out
def eval_mod(a,z,p):return sum(int(t)*pow(z,j,p) for j,t in enumerate(a))%p
x=s.Symbol('x');root=s.sqrt(5)
# The group-ring boundary identities certify all ten sectors simultaneously.
for d in [1,2]:
 a=raw[f'B{d}'];b=raw[f'B{d+1}'];co=np.zeros((10,a.shape[1],b.shape[2]),dtype=np.int64)
 for i in range(10):
  for j in range(10):co[(i+j)%10]+=a[i]@b[j]
 check(f'group_ring_boundary_{d}',not np.any(co))
summary=[]
for rec in records:
 m=rec['m'];k=rec['channel'];B=eval_coeff(raw[f'B{k}'],m);H=transpose_conj(B)
 G=matmul(fm(B),fm(H)) if k<3 else matmul(fm(H),fm(B))
 cp=rec['exact_characteristic_coefficients_cyclotomic'];n=G[0].nrows()
 ff=[(s.sympify(t['polynomial']),t['multiplicity']) for t in rec['factors_over_Qsqrt5']]
 expanded=s.Poly(s.prod(f**e for f,e in ff),x,extension=root)
 check(f'factorization_reconstruction_m{m}_k{k}',polyco(expanded.as_expr())==[tuple(c) for c in cp])
 annihilator=s.prod(f for f,_ in ff)
 check(f'squarefree_annihilator_m{m}_k{k}',all(a==fmpz_mat(n,n) for a in evaluate(polyco(annihilator),G)),degree=int(s.degree(annihilator,x)))
 check(f'coprime_factors_m{m}_k{k}',s.degree(s.gcd(annihilator,s.diff(annihilator,x),extension=root),x)==0)
 # Independent finite-field determinant check at two roots/character embeddings.
 for p,z0 in [(101,6),(211,23)]:
  # Find a root with exact order ten; seeded value is only an optimization.
  z0=next(z for z in range(2,p) if pow(z,10,p)==1 and pow(z,5,p)!=1 and pow(z,2,p)!=1)
  gm=[[sum(int(G[j][a,b])*pow(z0,j,p) for j in range(4))%p for b in range(n)] for a in range(n)]
  actual=[int(c) for c in nmod_mat(gm,p).charpoly()]
  expected=list(reversed([eval_mod(c,z0,p) for c in cp]))
  check(f'modular_determinant_m{m}_k{k}_p{p}',actual==expected,scope='EXACT_FINITE_FIELD')
 zero=next((e for f,e in ff if f==x),0)
 summary.append({'m':m,'channel':k,'rank':n-zero,'zero_in_gram':zero})
 # Discovery data and exact factors must agree, with multiplicities.
 numeric=[]
 for f,e in ff:
  for v in s.nroots(f,maxsteps=100):
   assert abs(float(s.im(v)))<1e-9
   numeric += [float(s.re(v))]*e
 Gnum=sum(np.array(G[j].tolist(),dtype=float)*np.exp(2j*np.pi*j/10) for j in range(4))
 ev=la.eigvalsh(Gnum)
 check(f'factor_roots_vs_Hermitian_m{m}_k{k}',np.max(np.abs(ev-np.sort(numeric)))<1e-9,scope='NUMERICAL_CORROBORATION',max_error=float(np.max(np.abs(ev-np.sort(numeric)))))
for m in range(6):
 rr=[r['rank'] for r in summary if r['m']==m]
 check(f'exchange_rank_and_zero_count_m{m}',rr==([11,61,59] if m==0 else [12,60,60]),ranks=rr,harmonic=264-2*sum(rr))
 # Direct numerical spectrum of weighted 264-dimensional generator.
 bs=[sum(raw[f'B{k}'][l]*np.exp(2j*np.pi*m*l/10) for l in range(10)) for k in [1,2,3]]
 cuts=[0,12,84,204,264];A=np.zeros((264,264),complex)
 predicted=[0.]*(264-2*sum(rr))
 for d,(b,w) in enumerate(zip(bs,[2,3,5])):
  i=slice(cuts[d],cuts[d+1]);j=slice(cuts[d+1],cuts[d+2]);A[i,j]=-w*b;A[j,i]=w*b.conj().T
  sv=la.svdvals(b)
  for v in sv[sv>1e-8]:predicted.extend([-w*v,w*v])
 error=float(np.max(np.abs(la.eigvalsh(1j*A)-np.sort(predicted))))
 check(f'weighted_generator_m{m}',error<1e-9,scope='NUMERICAL_CORROBORATION',max_error=error)
for m in range(6,10):
 for k in [1,2,3]:
  a=eval_coeff(raw[f'B{k}'],m);b=transpose_conj(eval_coeff(raw[f'B{k}'],10-m))
  check(f'exact_conjugation_m{m}_k{k}',all(np.array_equal(a[j],b[j].T) for j in range(4)))
result={'status':'PASS','physical_promotion':0,'independent_review':False,'check_families':len(checks),'checks':checks,'rank_summary':summary,'scope':'Exact number-field factorizations and squarefree annihilation, exact finite-field determinant checks, symbolic weighted-spectrum proof in report, labelled numerical corroboration.'}
(R/'REDUCED_SPECTRAL_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','check_families':len(checks),'rank_summary':summary}))
