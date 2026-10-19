"""1024-cell fixed-port solve: exact posterior audit of two-word complex128 coefficients."""
import sys
sys.dont_write_bytecode=True
from red_mesh import *
from pathlib import Path
from math import isqrt
import argparse,platform,hashlib

def sqrtup(x):
 assert x>=0
 scale=10**18;n=isqrt(x.numerator*scale*scale//x.denominator)
 if F(n*n,scale*scale)<x:n+=1
 return F(n,scale)
def sparse(A):return [[(j,x) for j,x in enumerate(row) if x] for row in A]
def spmv(A,x):return [sum(v*x[j] for j,v in row) for row in A]
def sparse_pull(A,P):
 ps=sparse(P);n=len(P[0]);B=zeros(n,n)
 for i,row in enumerate(A):
  for j,a in row:
   for ii,b in ps[i]:
    for jj,c in ps[j]:B[ii][jj]+=a*b*c
 return B

def encode(x):return [float(v).hex() for v in x]
def decode(x):return [F.from_float(float.fromhex(v)) for v in x]
def reduced(A,idx,piv,r):return [[A[i][j]-r[k]*A[piv][j]-r[l]*A[i][piv]+r[k]*r[l]*A[piv][piv] for l,j in enumerate(idx)] for k,i in enumerate(idx)]
def farray(A):return np.array([[float(x) for x in row] for row in A])
def lift(x,idx,piv,r,n):
 q=[F(0)]*n
 for i,a in zip(idx,x):q[i]=a
 q[piv]=-dot(r,x)
 return q

def main(folder,generate):
 out=Path(folder);out.mkdir(parents=True,exist_ok=True)
 p,t,_=refine(points,tets);p,t,_=edgewise(p,t);q,ts,P=edgewise(p,t);n=len(q)
 assert n==285 and len(ts)==1024
 for tet in ts:assert abs(determinant(frame(q,tet)))==F(1,512)
 h2=max(distance(q,i,j) for tet in ts for i,j in combinations(tet,2));assert h2==F(5,64)
 K,M=assemble(q,ts,[F(1,512)]*len(ts));Ks,Ms=sparse(K),sparse(M);Kp,Mp=assemble(p,t,[F(1,64)]*len(t))
 assert sparse_pull(Ks,P)==Kp and sparse_pull(Ms,P)==Mp
 g=spmv(Ms,[10*sum(v[:2]) for v in q]);w=spmv(Ms,[F(1)]*n);assert sum(g)==0 and sum(w)==2
 piv=max(range(n),key=lambda i:w[i]);idx=[i for i in range(n) if i!=piv];r=[w[i]/w[piv] for i in idx]
 Kr,Mr=reduced(K,idx,piv,r),reduced(M,idx,piv,r);gr=[g[i]-r[k]*g[piv] for k,i in enumerate(idx)]
 specs=[(F(0),F(1,10)),(F(4),F(1,10)),(F(9,2),F(1,10)),(F(5),F(1,10))]
 def residual(vr,vi,om,ga):
  kvR,kvI=spmv(Ks,vr),spmv(Ks,vi);mvR,mvI=spmv(Ms,vr),spmv(Ms,vi)
  rr=[a-b+om*om*c+2*ga*om*d for a,b,c,d in zip(g,kvR,mvR,mvI)];ri=[-a+om*om*b-2*ga*om*c for a,b,c in zip(kvI,mvI,mvR)]
  return rr,ri
 if generate:
  assert np is not None
  wit={'backend':{'python':platform.python_version(),'numpy':np.__version__,'dtype':'complex128','solver':'numpy.linalg.solve','representation':'Two-word expansion per real/imag reduced coefficient: initial complex128 solve plus one complex128 solve of its exact rational residual; coefficients are exact sums of decoded hex words. No all-input IEEE claim.'},'pivot':piv,'dimension':n-1,'fixtures':[]}
  kf,mf=farray(Kr),farray(Mr);gf=np.array(list(map(float,gr)))
  Z=np.zeros((n,n-1));Z[idx,range(n-1)]=1;Z[piv,:]=-np.array(list(map(float,r)));fullg=np.array(list(map(float,g)))
  for om,ga in specs:
   a=kf-float(om*om)*mf+1j*float(2*ga*om)*mf;hi=np.linalg.solve(a,gf);hr,hi_=decode(encode(hi.real)),decode(encode(hi.imag));vr,vi=lift(hr,idx,piv,r,n),lift(hi_,idx,piv,r,n)
   rr,ri=residual(vr,vi,om,ga);redr=np.array([complex(float(rr[i]-r[k]*rr[piv]),float(ri[i]-r[k]*ri[piv])) for k,i in enumerate(idx)])
   low=np.linalg.solve(a,redr);xf=hi+low;qf=Z@xf;af=farray(K)-float(om*om)*farray(M)+1j*float(2*ga*om)*farray(M);H=fullg@qf;J=2*H-qf@(af@qf)
   wit['fixtures'].append({'omega':str(om),'gamma':str(ga),'hi_real_hex':encode(hi.real),'hi_imag_hex':encode(hi.imag),'low_real_hex':encode(low.real),'low_imag_hex':encode(low.imag),'reported_raw_hex':encode([H.real,H.imag]),'reported_corrected_hex':encode([J.real,J.imag])})
   print('generated omega',om,flush=True)
  (out/'WITNESS.json').write_text(json.dumps(wit,indent=2)+'\n')
 else:wit=json.loads((out/'WITNESS.json').read_text())
 assert wit['pivot']==piv and wit['dimension']==n-1 and len(wit['fixtures'])==4
 records=[]
 for f,(om,ga) in zip(wit['fixtures'],specs):
  assert f['omega']==str(om) and f['gamma']==str(ga)
  words=[decode(f[k]) for k in ['hi_real_hex','hi_imag_hex','low_real_hex','low_imag_hex']];assert all(len(x)==n-1 for x in words)
  xr=[a+b for a,b in zip(words[0],words[2])];xi=[a+b for a,b in zip(words[1],words[3])];vr,vi=lift(xr,idx,piv,r,n),lift(xi,idx,piv,r,n)
  assert dot(w,vr)==dot(w,vi)==0
  if om==0:assert not any(xi),'static state must be real'
  rr,ri=residual(vr,vi,om,ga);assert sum(rr)==sum(ri)==0
  eps2=F(5,4)*sum((a*a+b*b)/wi for a,b,wi in zip(rr,ri,w))
  beta2=max(4*ga*ga/(om*om+4*ga*ga),max(F(0),1-om*om/4)**2)
  lr,li=dot(g,vr),dot(g,vi);kvR,kvI=spmv(Ks,vr),spmv(Ks,vi);mvR,mvI=spmv(Ms,vr),spmv(Ms,vi)
  ar=dot(vr,kvR)-dot(vi,kvI)-om*om*(dot(vr,mvR)-dot(vi,mvI))-4*ga*om*dot(vr,mvI)
  ai=2*dot(vr,kvI)-2*om*om*dot(vr,mvI)+2*ga*om*(dot(vr,mvR)-dot(vi,mvI))
  jr,ji=2*lr-ar,2*li-ai;raw=decode(f['reported_raw_hex']);cor=decode(f['reported_corrected_hex'])
  rawev=sqrtup((raw[0]-lr)**2+(raw[1]-li)**2);corev=sqrtup((cor[0]-jr)**2+(cor[1]-ji)**2);alg=sqrtup(5*eps2/beta2)+rawev
  assert alg<=F(1,10**10),'raw algebraic1e-10 budget'
  kap2=(om*om+4*ga*ga)/(4*ga*ga) if om*om+4*ga*ga>=4 else 16/((4-om*om)**2+4*ga*ga*om*om)
  records.append({'omega':str(om),'gamma':str(ga),'static_real_state_verified':bool(om==0),'raw_output_real':str(lr),'raw_output_imag':str(li),'corrected_output_real':str(jr),'corrected_output_imag':str(ji),'algebraic_dual_residual_squared_upper':str(eps2),'raw_total_algebraic_output_bound':str(alg),'reported_raw_evaluation_bound':str(rawev),'reported_corrected_evaluation_bound':str(corev),'corrected_algebraic_output_bound':str(sqrtup(kap2)*eps2+corev)})
  print('audited omega',om,'raw algebraic bound',float(alg),flush=True)
 result={'status':'PASS','classification':'CONDITIONAL_1024_CELL_TWO_WORD_SOLVER_WITNESSES','mesh':{'vertices':n,'tetrahedra':len(ts),'maximum_diameter_squared':'5/64','meanfree_pivot':piv,'reduced_dimension':n-1},'records':records,'backend':wit['backend'],'physical_promotion':0,'independent_review':False}
 target=out/'SOLVE_RESULTS.json'
 if target.exists() and not generate:assert json.loads(target.read_text())==result;print('read-only replay matches SOLVE_RESULTS.json')
 else:target.write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('output');a.add_argument('--generate',action='store_true');args=a.parse_args();main(args.output,args.generate)
