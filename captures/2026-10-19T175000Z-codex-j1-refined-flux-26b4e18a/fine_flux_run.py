"""Refined RT1 H(div) and exact audit of stored NumPy complex128 witnesses."""
import sys
sys.dont_write_bytecode=True
from fine_flux_core import *
import argparse,hashlib,platform
from pathlib import Path
def log(s):print(s,flush=True)
def value(b,x):
 if b<12:
  i,k=divmod(b,4);v=F(1) if not k else x[k-1];return [v if j==i else F(0) for j in range(3)]
 return [v*x[b-12] for v in x]
def divvalue(b,x):
 if b<12:
  i,k=divmod(b,4);return F(k==i+1)
 return 4*x[b-12]
def subvec(a,b):return tuple(x-y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def poly(b,k):
 e=[0]*3
 if b<12:
  i,j=divmod(b,4)
  if i!=k:return {}
  if j:e[j-1]=1
 else:e[k]+=1;e[b-12]+=1
 return {tuple(e):F(1)}
def rref_many(A,B):
 n=len(A[0]);nr=len(B[0]);w=[r[:]+b[:] for r,b in zip(A,B)];piv=[];r=0
 for j in range(n):
  ids=[i for i in range(r,len(w)) if w[i][j]]
  if not ids:continue
  i=ids[0];w[r],w[i]=w[i],w[r];v=w[r][j];w[r]=[x/v for x in w[r]]
  for i in range(len(w)):
   if i!=r and w[i][j]:
    v=w[i][j];w[i]=[x-v*y for x,y in zip(w[i],w[r])]
  piv.append(j);r+=1
 for row in w[r:]:assert not any(row[n:]),'divergence compatibility failed'
 free=[j for j in range(n) if j not in piv];N=zeros(n,len(free))
 for k,j in enumerate(free):
  N[j][k]=1
  for i,l in enumerate(piv):N[l][k]=-w[i][j]
 parts=[]
 for k in range(nr):
  x=[F(0)]*n
  for i,j in enumerate(piv):x[j]=w[i][n+k]
  parts.append(x)
 return parts,N,free
def farray(a):return np.array([[float(x) for x in r] for r in a],dtype=np.float64)
def decode(xs):return [F.from_float(float.fromhex(x)) for x in xs]
def encode(xs):return [float(x).hex() for x in xs]
def main(out,generate):
 out=Path(out);out.mkdir(parents=True,exist_ok=True)
 q,ts,P=refine(points,tets);n=len(q);K,M=assemble(q,ts,[F(1,8)]*len(ts));p=[F(x) for x in [0,1,0,-1,0]];g=[10*x for x in mv(M,mv(P,p))]
 w=mv(M,[F(1)]*n);Z=[[F(i==j)-F(i==0)*w[j]/w[0] for j in range(1,n)] for i in range(n)]
 Kr=mm(tr(Z),mm(K,Z));Mr=mm(tr(Z),mm(M,Z));gr=mv(tr(Z),g);Kri=inv(Kr)
 specs=[(F(0),F(1,10)),(F(4),F(1,10)),(F(9,2),F(1,10)),(F(5),F(1,10))]
 if generate:
  assert np is not None,'NumPy required only for witness generation'
  witness={'backend':{'python':platform.python_version(),'numpy':np.__version__,'dtype':'complex128','solver':'numpy.linalg.solve','target_arithmetic':'exact Fraction; gamma=1/10 rational','representation':'Stored reduced coefficient floats decoded by exact hex; exact mean-free lift Z. Free flux coefficients likewise decoded, constraints then imposed exactly.'},'fixtures':[]}
  for om,ga in specs:
   ar=farray(add(Kr,Mr,-om*om))+1j*float(2*ga*om)*farray(Mr);xf=np.linalg.solve(ar,np.array(list(map(float,gr)),dtype=np.complex128))
   qfloat=farray(Z)@xf;gfloat=np.array(list(map(float,g)));fullA=farray(add(K,M,-om*om))+1j*float(2*ga*om)*farray(M);hout=gfloat@qfloat;jout=2*hout-qfloat@(fullA@qfloat)
   witness['fixtures'].append({'omega':str(om),'gamma':str(ga),'x_real_hex':encode(xf.real),'x_imag_hex':encode(xf.imag),'reported_raw_hex':encode([hout.real,hout.imag]),'reported_corrected_hex':encode([jout.real,jout.imag])})
 else:witness=json.loads((out/'WITNESS.json').read_text())
 states=[]
 for f,(om,ga) in zip(witness['fixtures'],specs):
  assert f['omega']==str(om) and f['gamma']==str(ga)
  xr,xi=decode(f['x_real_hex']),decode(f['x_imag_hex']);states.append((mv(Z,xr),mv(Z,xi),xr,xi))
 log('assembled exact14-node state matrices and binary64 witnesses')
 faces={}
 for i,t in enumerate(ts):
  for face in combinations(sorted(t),3):faces.setdefault(face,[]).append(i)
 A=[];rhs=[];nflux=15*len(ts);nrhs=2*len(specs)
 for face,cells in faces.items():
  normal=cross(subvec(q[face[1]],q[face[0]]),subvec(q[face[2]],q[face[0]]))
  for vi in face:
   row=[F(0)]*nflux
   for k,cell in enumerate(cells):
    for j in range(15):row[15*cell+j]=(-1)**k*dot(value(j,q[vi]),normal)
   A.append(row);rhs.append([F(0)]*nrhs)
 for cell,t in enumerate(ts):
  for vi in t:
   row=[F(0)]*nflux
   for j in range(15):row[15*cell+j]=divvalue(j,q[vi])
   b=[]
   for (om,ga),(vr,vi_,xr,xi) in zip(specs,states):
    b.extend([-om*om*vr[vi]-2*ga*om*vi_[vi]-10*sum(q[vi][:2]),-om*om*vi_[vi]+2*ga*om*vr[vi]])
   A.append(row);rhs.append(b)
 log('exact RT1 constraint elimination')
 parts,N,free=rref_many(A,rhs)
 log('constraint rank '+str(nflux-len(free))+'; free flux dimension '+str(len(free)))
 @lru_cache(None)
 def integral(cell,e):
  p={(0,0,0,0):F(1)}
  for axis,deg in enumerate(e):
   for _ in range(deg):
    nxt={}
    for ex,c in p.items():
     for j,vi in enumerate(ts[cell]):
      ee=list(ex);ee[j]+=1;ee=tuple(ee);nxt[ee]=nxt.get(ee,F(0))+c*q[vi][axis]
    p=nxt
  return sum(c*F(6,8*factorial(sum(ex)+3))*factorial(ex[0])*factorial(ex[1])*factorial(ex[2])*factorial(ex[3]) for ex,c in p.items())
 blocks=[];G=zeros(nflux,nflux)
 for cell in range(len(ts)):
  block=zeros(15,15)
  for i in range(15):
   for j in range(15):
    for k,weight in enumerate([F(1),F(1),F(1,2)]):
     for e,c in poly(i,k).items():
      for ee,cc in poly(j,k).items():block[i][j]+=weight*c*cc*integral(cell,tuple(a+b for a,b in zip(e,ee)))
    G[cell*15+i][cell*15+j]=block[i][j]
  blocks.append(block)
 def fluxquad(x):return sum(quad(b,x[15*i:15*i+15]) for i,b in enumerate(blocks))
 if generate:
  nf,gf=farray(N),farray(G);gram=nf.T@gf@nf
  for k,f in enumerate(witness['fixtures']):
   proposals=np.linalg.solve(gram,-nf.T@gf@np.array([list(map(float,parts[2*k])),list(map(float,parts[2*k+1]))]).T)
   f['free_real_hex']=encode(proposals[:,0]);f['free_imag_hex']=encode(proposals[:,1])
  (out/'WITNESS.json').write_text(json.dumps(witness,indent=2)+'\n')
 checks=[];records=[]
 def check(name,condition):
  assert condition,name
  checks.append(name)
 check('14 nodes16 tetrahedra',n==14 and len(ts)==16)
 check('fixed volume source zero mean',sum(g)==0)
 for k,(f,(om,ga),(vr,vi,xr,xi)) in enumerate(zip(witness['fixtures'],specs,states)):
  jr=[a+b for a,b in zip(parts[2*k],mv(N,decode(f['free_real_hex'])))];ji=[a+b for a,b in zip(parts[2*k+1],mv(N,decode(f['free_imag_hex'])))]
  for r,(row,b) in enumerate(zip(A,rhs)):
   sparse=[(j,v) for j,v in enumerate(row) if v]
   check('real exact flux constraint '+str((k,r)),sum(v*jr[j] for j,v in sparse)==b[2*k])
   check('imag exact flux constraint '+str((k,r)),sum(v*ji[j] for j,v in sparse)==b[2*k+1])
  check('exact mean-free state '+str(k),dot(w,vr)==dot(w,vi)==0)
  mass=quad(M,vr)+quad(M,vi);stiff=quad(K,vr)+quad(K,vi);lr,li=dot(g,vr),dot(g,vi)
  eta2=fluxquad(jr)+fluxquad(ji)-2*lr-2*om*om*mass+stiff
  check('nonnegative exact flux error '+str(k),eta2>=0)
  a=add(Kr,Mr,-om*om);b=[[2*ga*om*x for x in row] for row in Mr]
  rhoR=[x-y+z for x,y,z in zip(gr,mv(a,xr),mv(b,xi))];rhoI=[-x-y for x,y in zip(mv(a,xi),mv(b,xr))]
  eps2=quad(Kri,rhoR)+quad(Kri,rhoI);beta2=max(4*ga*ga/(om*om+4*ga*ga),max(F(0),1-om*om/4)**2);B=1+(om*om+2*ga*om)/4
  algout2=5*eps2/beta2;budget=F(1,10**10)
  check('certified raw algebraic output budget '+str(k),algout2<=budget*budget)
  # Bilinear output correction: ordinary transpose, no conjugation.
  kR=quad(K,vr)-quad(K,vi);kI=2*dot(vr,mv(K,vi));mR=quad(M,vr)-quad(M,vi);mI=2*dot(vr,mv(M,vi))
  azR=kR-om*om*mR-2*ga*om*mI;azI=kI-om*om*mI+2*ga*om*mR
  corrR,corrI=2*lr-azR,2*li-azI;rbR,rbI=lr-azR,li-azI
  # Rational upper on sqrt(norm²) rounded upward to a fixed decimal grid.
  def sqrtup(x,digits=18):
   from math import isqrt
   scale=10**digits;n=isqrt(x.numerator*scale*scale//x.denominator)
   if F(n*n,scale*scale)<x:n+=1
   return F(n,scale)
  residual_correction=sqrtup(rbR*rbR+rbI*rbI);cont=B*eta2/beta2
  raw_report=decode(f['reported_raw_hex']);corr_report=decode(f['reported_corrected_hex']);raw_eval=sqrtup((raw_report[0]-lr)**2+(raw_report[1]-li)**2);corr_eval=sqrtup((corr_report[0]-corrR)**2+(corr_report[1]-corrI)**2)
  total_alg=sqrtup(algout2)+raw_eval;check('end-to-end reported raw output budget '+str(k),total_alg<=budget)
  coarse_eta=F(47,42)*100/((20-om*om)**2+4*ga*ga*om*om);check('sampled refined flux improvement '+str(k),eta2<coarse_eta)
  static_bracket=None
  if om==0:
   scale=10**6;lo=F((corrR*scale).numerator//(corrR*scale).denominator,scale);bound=corrR+cont;hi=F(-((-bound*scale).numerator//(-bound*scale).denominator),scale)
   check('static outward bracket',lo<=corrR and hi>=bound and corrI==0);static_bracket={'lower':str(lo),'upper':str(hi)}
  records.append({'static_continuum_bracket':static_bracket,'omega':str(om),'gamma':str(ga),'raw_output_real':str(lr),'raw_output_imag':str(li),'corrected_output_real':str(corrR),'corrected_output_imag':str(corrI),'algebraic_dual_residual_squared':str(eps2),'raw_algebraic_output_error_bound':str(sqrtup(algout2)),'raw_algebraic_budget':str(budget),'reported_output_evaluation_error_bound':str(raw_eval),'reported_corrected_evaluation_error_bound':str(corr_eval),'reported_raw_total_algebraic_error_bound':str(total_alg),'coarse_flux_estimator_squared':str(coarse_eta),'flux_estimator_squared':str(eta2),'corrected_continuum_error_bound':str(cont),'raw_continuum_error_bound':str(cont+residual_correction+raw_eval),'reported_corrected_continuum_error_bound':str(cont+corr_eval),'rounding_scope':'Exact audit of stored binary64 reduced coefficients and reported raw/corrected outputs; exact mean-free reference lift. Evaluation bounds include the recorded floating lift/dot/correction. No all-input IEEE error theorem.'})
  log('certified omega='+str(om)+' eta²~'+str(float(eta2))+' continuum bound~'+str(float(cont)))
 result={'status':'PASS','classification':'CONDITIONAL_REFINED_RT1_AND_AUDITED_BINARY64_WITNESSES','checks':checks,'check_count':len(checks),'mesh':{'vertices':n,'tetrahedra':len(ts),'rt1_coefficients':nflux,'constraint_equations':len(A),'constraint_rank':nflux-len(free),'free_flux_coefficients':len(free)},'backend':witness['backend'],'records':records,'independent_review':False,'physical_promotion':0}
 if not generate and (out/'RESULTS.json').exists():
  assert json.loads((out/'RESULTS.json').read_text())==result,'captured results mismatch';log('read-only replay matches RESULTS.json')
 else:(out/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
 log('PASS '+str(len(checks))+' checks')
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('output');a.add_argument('--generate',action='store_true');args=a.parse_args();main(args.output,args.generate)
