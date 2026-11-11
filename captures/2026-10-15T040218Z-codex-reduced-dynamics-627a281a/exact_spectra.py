from pathlib import Path
import json,time
import numpy as np
from flint import fmpz_mat
import sympy as s
R=Path(__file__).resolve().parent
raw=np.load(R/'polynomial_arrays.npz')
def red(v):
 v=list(v)+[0]*max(0,7-len(v))
 for k in range(len(v)-1,3,-1):
  c=v[k];v[k]=0
  for j,sg in enumerate([-1,1,-1,1]):v[k-4+j]+=sg*c
 return tuple(v[:4])
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def mul(a,b):
 v=[0]*7
 for i,x in enumerate(a):
  for j,y in enumerate(b):v[i+j]+=x*y
 return red(v)
unit=(1,0,0,0);z=(0,1,0,0)
pows=[unit]
for _ in range(10):pows.append(mul(pows[-1],z))
assert pows[5]==(-1,0,0,0) and pows[10]==unit
def eval_coeff(c,m):
 out=[np.zeros(c.shape[1:],dtype=np.int64) for _ in range(4)]
 for k in range(10):
  for j,v in enumerate(pows[(m*k)%10]):out[j]+=int(v)*c[k]
 return out
def transpose_conj(a):
 n,r=a[0].shape;out=[np.zeros((r,n),dtype=np.int64) for _ in range(4)]
 for k in range(4):
  for j,v in enumerate(pows[(-k)%10]):out[j]+=int(v)*a[k].T
 return out
def fm(a):return [fmpz_mat(x.tolist()) for x in a]
def matmul(a,b):
 v=[fmpz_mat(a[0].nrows(),b[0].ncols()) for _ in range(7)]
 for i in range(4):
  for j in range(4):v[i+j]+=a[i]*b[j]
 for k in range(6,3,-1):
  for j,sg in enumerate([-1,1,-1,1]):v[k-4+j]+=sg*v[k]
 return v[:4]
def trace(a):return tuple(sum(int(M[i,i]) for i in range(M.nrows())) for M in a)
def charpoly(G):
 n=G[0].nrows()
 if all(G[j]==fmpz_mat(n,n) for j in range(1,4)):
  co=list(G[0].charpoly());return [(int(c),0,0,0) for c in reversed(co)]
 power=[fmpz_mat(n,n) for _ in range(4)]
 for i in range(n):power[0][i,i]=1
 moments=[]
 for k in range(1,n+1):
  power=matmul(power,G);moments.append(trace(power))
 coeff=[unit]
 for k in range(1,n+1):
  v=(0,0,0,0)
  for j in range(1,k+1):v=add(v,mul(coeff[k-j],moments[j-1]))
  assert all(t%k==0 for t in v)
  coeff.append(tuple(-t//k for t in v))
 return coeff
x=s.symbols('x');root=s.sqrt(5)
def run():
 records=[];allblocks=[]
 for m in range(10):
  bs=[eval_coeff(raw[f'B{k}'],m) for k in [1,2,3]]
  blocks=[]
  for B in bs:
   nz=np.nonzero(sum(abs(a) for a in B))
   blocks.append({'shape':list(B[0].shape),'entries':[[int(i),int(j),*[int(a[i,j]) for a in B]] for i,j in zip(*nz)]})
  allblocks.append({'m':m,'B1_B2_B3':blocks})
  if m>5:continue
  for k,B in enumerate(bs,1):
   start=time.time();H=transpose_conj(B)
   G=matmul(fm(B),fm(H)) if k<3 else matmul(fm(H),fm(B))
   co=charpoly(G)
   # Hermitian characteristic coefficients belong to the real subfield Q(sqrt5).
   assert all(t[1]==0 and t[3]==-t[2] for t in co)
   expr=sum((t[0]+t[2]*(root-1)/2)*x**(len(co)-1-j) for j,t in enumerate(co))
   factors=s.factor_list(expr,x,extension=root)[1]
   fac=[{'polynomial':str(s.expand(f)),'multiplicity':int(e),'coefficients_descending':[str(c) for c in s.Poly(f,x).all_coeffs()]} for f,e in factors]
   rec={'m':m,'channel':k,'gram_dimension':len(co)-1,'exact_characteristic_coefficients_cyclotomic':[list(t) for t in co],'factors_over_Qsqrt5':fac}
   records.append(rec);print(m,k,'seconds',round(time.time()-start,2),fac,flush=True)
   (R/'EXACT_SPECTRA_PARTIAL.json').write_text(json.dumps(records,indent=2)+'\n')
 (R/'ALL_REDUCED_BLOCKS.json').write_text(json.dumps({'field':'Q(zeta10); coefficient [c0,c1,c2,c3] represents sum c_j zeta10^j; zeta10^4-zeta10^3+zeta10^2-zeta10+1=0','dimensions':[12,72,120,60],'symbolic_generator':'A_m has upper blocks -a B1, -b B2, -c B3 and lower adjoint blocks a B1dagger, b B2dagger, c B3dagger','blocks':allblocks},separators=(',',':'))+'\n')
 (R/'EXACT_SPECTRA.json').write_text(json.dumps({'m_0_through_5':records,'m_6_through_9':'Identical Gram characteristic polynomials to m=4,3,2,1 respectively, by complex conjugation; exact matrices for all ten supplied.','weighted_spectrum':'Each positive Gram eigenvalue mu in channel k contributes +/- i a_k sqrt(mu) with its multiplicity. Include only two zero eigenvalues in m=0 when a,b,c nonzero.','proof':'Boundary-square zero splits adjacent exchanges into orthogonal singular-vector two-planes. Characteristic polynomials computed by exact cyclotomic-field Newton identities, or direct integer charpoly for m0,m5.'},indent=2)+'\n')
 print('DONE',flush=True)

if __name__=='__main__':run()
