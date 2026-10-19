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

def constraints(q,ts,values):
 faces={}
 for i,t in enumerate(ts):
  for face in combinations(sorted(t),3):faces.setdefault(face,[]).append(i)
 nflux=15*len(ts);nr=len(values[0][0]);A=[];rhs=[]
 for face,cells in faces.items():
  assert len(cells)<=2
  normal=cross(subvec(q[face[1]],q[face[0]]),subvec(q[face[2]],q[face[0]]))
  for vi in face:
   row=[F(0)]*nflux
   for k,cell in enumerate(cells):
    for j in range(15):row[15*cell+j]=(-1)**k*dot(value(j,q[vi]),normal)
   A.append(row);rhs.append([F(0)]*nr)
 for cell,t in enumerate(ts):
  for k,vi in enumerate(t):
   row=[F(0)]*nflux
   for j in range(15):row[15*cell+j]=divvalue(j,q[vi])
   A.append(row);rhs.append(values[cell][k])
 return A,rhs

def gramblocks(q,ts,vol):
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
  return sum(c*vol[cell]*F(6,factorial(sum(ex)+3))*factorial(ex[0])*factorial(ex[1])*factorial(ex[2])*factorial(ex[3]) for ex,c in p.items())
 blocks=[]
 for cell in range(len(ts)):
  block=zeros(15,15)
  for i in range(15):
   for j in range(15):
    for k,weight in enumerate([F(1),F(1),F(1,2)]):
     for e,c in poly(i,k).items():
      for ee,cc in poly(j,k).items():block[i][j]+=weight*c*cc*integral(cell,tuple(a+b for a,b in zip(e,ee)))
  blocks.append(block)
 return blocks

def blockmatrix(blocks):
 G=zeros(15*len(blocks),15*len(blocks))
 for k,b in enumerate(blocks):
  for i in range(15):
   for j in range(15):G[15*k+i][15*k+j]=b[i][j]
 return G

def reconstruct(part,N,free):
 assert len(free)==len(N[0]) and len(part)==len(N)
 return [a+b for a,b in zip(part,mv(N,decode(free)))]
def minimize(N,G,parts):
 nf,gf=farray(N),farray(G)
 return np.linalg.solve(nf.T@gf@nf,-nf.T@gf@np.array([list(map(float,p)) for p in parts]).T)

def main(out,generate):
 out=Path(out);out.mkdir(parents=True,exist_ok=True)
 parent,pts,P0=refine(points,tets);q=parent[:];ts=[];P=eye(len(parent))
 for t in pts:
  c=len(q);q.append(tuple(sum(parent[i][j] for i in t)/4 for j in range(3)))
  P.append([F(i in t,4) for i in range(len(parent))])
  for k in range(4):ts.append(tuple(c if j==k else vi for j,vi in enumerate(t)))
 for tet in ts:
  d=[subvec(q[i],q[tet[0]]) for i in tet[1:]]
  assert abs(dot(d[0],cross(d[1],d[2])))==F(1,32),'child volume'
 # Parent barycentric basis equals P at new nodes. Exact orthogonality of w-1/4.
 for k,t in enumerate(pts):
  mc=[F(0)]*len(q);c=len(parent)+k
  for tet in ts[4*k:4*k+4]:
   for vi in tet:mc[vi]+=F(1+int(vi==c),640)
  assert sum(mc)==F(1,32)
  for vi in t:assert sum(mc[j]*P[j][vi] for j in range(len(q)))==F(1,128)
 n=len(q);K,M=assemble(q,ts,[F(1,32)]*len(ts));Kp,Mp=assemble(parent,pts,[F(1,8)]*len(pts))
 assert mm(tr(P),mm(K,P))==Kp and mm(tr(P),mm(M,P))==Mp
 g=mv(M,[10*sum(x[:2]) for x in q]);gp=mv(Mp,[10*sum(x[:2]) for x in parent]);assert mv(tr(P),g)==gp
 w=mv(M,[F(1)]*n);Z=[[F(i==j)-F(i==0)*w[j]/w[0] for j in range(1,n)] for i in range(n)]
 Kr=mm(tr(Z),mm(K,Z));Mr=mm(tr(Z),mm(M,Z));gr=mv(tr(Z),g);Kri=inv(Kr)
 specs=[(F(0),F(1,10)),(F(4),F(1,10)),(F(9,2),F(1,10)),(F(5),F(1,10))]
 if generate:
  assert np is not None
  witness={'backend':{'python':platform.python_version(),'numpy':np.__version__,'dtype':'complex128','solver':'numpy.linalg.solve','target_arithmetic':'Fraction; exact rational gamma=1/10','representation':'Exact hex decoding of state, parent free flux and patch free flux proposals; exact reconstruction imposes constraints.'},'fixtures':[]}
  for om,ga in specs:
   ar=farray(add(Kr,Mr,-om*om))+1j*float(2*ga*om)*farray(Mr);xf=np.linalg.solve(ar,np.array(list(map(float,gr)),dtype=np.complex128))
   qfloat=farray(Z)@xf;gf=np.array(list(map(float,g)));fullA=farray(add(K,M,-om*om))+1j*float(2*ga*om)*farray(M);hout=gf@qfloat;jout=2*hout-qfloat@(fullA@qfloat)
   witness['fixtures'].append({'omega':str(om),'gamma':str(ga),'x_real_hex':encode(xf.real),'x_imag_hex':encode(xf.imag),'reported_raw_hex':encode([hout.real,hout.imag]),'reported_corrected_hex':encode([jout.real,jout.imag]),'patch_free':[]})
 else:witness=json.loads((out/'WITNESS.json').read_text())
 states=[];deltas=[]
 assert len(witness['fixtures'])==len(specs)
 for f,(om,ga) in zip(witness['fixtures'],specs):
  assert f['omega']==str(om) and f['gamma']==str(ga)
  xr,xi=decode(f['x_real_hex']),decode(f['x_imag_hex']);assert len(xr)==len(xi)==n-1
  vr,vi=mv(Z,xr),mv(Z,xi);states.append((vr,vi,xr,xi));deltas.append([(v[len(parent)+k]-sum(v[i] for i in t)/4) for v in (vr,vi) for k,t in enumerate(pts)])
 log('30-node/64-cell exact matrices, nested forms and source checked')
 # Parent divergence is z times the cellwise L2 affine projection of v, minus F.
 vals=[]
 for k,t in enumerate(pts):
  cell=[]
  for vi in t:
   row=[]
   for f,((om,ga),(vr,vi_,xr,xi)) in enumerate(zip(specs,states)):
    dr,di=deltas[f][k],deltas[f][len(pts)+k];pr,pi=vr[vi]+dr/4,vi_[vi]+di/4
    row.extend([-om*om*pr-2*ga*om*pi-10*sum(parent[vi][:2]),-om*om*pi+2*ga*om*pr])
   cell.append(row)
  vals.append(cell)
 A,rhs=constraints(parent,pts,vals);parts,N,free=rref_many(A,rhs);G=blockmatrix(gramblocks(parent,pts,[F(1,8)]*len(pts)))
 if generate:
  proposals=minimize(N,G,parts)
  for k,f in enumerate(witness['fixtures']):f['free_real_hex']=encode(proposals[:,2*k]);f['free_imag_hex']=encode(proposals[:,2*k+1])
 parentflux=[]
 for k,f in enumerate(witness['fixtures']):parentflux.append([reconstruct(parts[2*k+j],N,f['free_real_hex' if j==0 else 'free_imag_hex']) for j in range(2)])
 blocks=gramblocks(q,ts,[F(1,32)]*len(ts));flux=[[[F(0)]*(15*len(ts)) for _ in range(2)] for f in specs];patchdata=[]
 for k,t in enumerate(pts):
  child=ts[4*k:4*k+4];center=len(parent)+k
  vv=[[[F(3,4) if vi==center else F(-1,4)] for vi in tet] for tet in child]
  Ap,bp=constraints(q,child,vv);ps,Np,fp=rref_many(Ap,bp);Gp=blockmatrix(blocks[4*k:4*k+4]);patchdata.append((Ap,bp,Np,fp))
  pp=[]
  for f,((om,ga),(drs,dis)) in enumerate(zip(specs,[(d[:len(pts)],d[len(pts):]) for d in deltas])):
   dr,di=drs[k],dis[k];zr,zi=-om*om*dr-2*ga*om*di,-om*om*di+2*ga*om*dr
   for j,zdelta in enumerate((zr,zi)):
    base=parentflux[f][j][15*k:15*k+15]*4
    pp.append([a+zdelta*b for a,b in zip(base,ps[0])])
  if generate:
   proposals=minimize(Np,Gp,pp)
   for f in range(len(specs)):witness['fixtures'][f]['patch_free'].append({'real_hex':encode(proposals[:,2*f]),'imag_hex':encode(proposals[:,2*f+1])})
  for f,wit in enumerate(witness['fixtures']):
   for j in range(2):flux[f][j][60*k:60*k+60]=reconstruct(pp[2*f+j],Np,wit['patch_free'][k]['real_hex' if j==0 else 'imag_hex'])
  log('local patch '+str(k+1)+'/16 rank '+str(60-len(fp)))
 if generate:(out/'WITNESS.json').write_text(json.dumps(witness,indent=2)+'\n')
 # Audit final assembled flux directly, independently of the hierarchical constraint construction.
 vals=[]
 for t in ts:
  cell=[]
  for vi in t:
   row=[]
   for (om,ga),(vr,vi_,xr,xi) in zip(specs,states):row.extend([-om*om*vr[vi]-2*ga*om*vi_[vi]-10*sum(q[vi][:2]),-om*om*vi_[vi]+2*ga*om*vr[vi]])
   cell.append(row)
  vals.append(cell)
 Af,bf=constraints(q,ts,vals);checks=[];records=[]
 def check(name,cond):
  assert cond,name
  checks.append(name)
 check('30 vertices and64 tetrahedra',n==30 and len(ts)==64)
 check('exact nested stiffness mass and source',mm(tr(P),mm(K,P))==Kp and mm(tr(P),mm(M,P))==Mp and mv(tr(P),g)==gp)
 check('source zero mean',sum(g)==0)
 check('exact child determinant volumes and local affine L2 projection',True)
 for k,(f,(om,ga),(vr,vi,xr,xi)) in enumerate(zip(witness['fixtures'],specs,states)):
  jr,ji=flux[k]
  for r,(row,b) in enumerate(zip(Af,bf)):
   sparse=[(j,v) for j,v in enumerate(row) if v]
   check('assembled real flux constraint '+str((k,r)),sum(v*jr[j] for j,v in sparse)==b[2*k])
   check('assembled imag flux constraint '+str((k,r)),sum(v*ji[j] for j,v in sparse)==b[2*k+1])
  check('exact meanfree '+str(k),dot(w,vr)==dot(w,vi)==0)
  def fluxquad(x):return sum(quad(b,x[15*i:15*i+15]) for i,b in enumerate(blocks))
  mass=quad(M,vr)+quad(M,vi);stiff=quad(K,vr)+quad(K,vi);lr,li=dot(g,vr),dot(g,vi)
  eta2=fluxquad(jr)+fluxquad(ji)-2*lr-2*om*om*mass+stiff
  check('nonnegative flux norm '+str(k),eta2>=0)
  a=add(Kr,Mr,-om*om);b=[[2*ga*om*x for x in row] for row in Mr]
  rhoR=[x-y+z for x,y,z in zip(gr,mv(a,xr),mv(b,xi))];rhoI=[-x-y for x,y in zip(mv(a,xi),mv(b,xr))]
  eps2=quad(Kri,rhoR)+quad(Kri,rhoI);beta2=max(4*ga*ga/(om*om+4*ga*ga),max(F(0),1-om*om/4)**2);B=1+(om*om+2*ga*om)/4
  algout2=5*eps2/beta2;budget=F(1,10**10)
  check('raw algebraic budget '+str(k),algout2<=budget*budget)
  kR=quad(K,vr)-quad(K,vi);kI=2*dot(vr,mv(K,vi));mR=quad(M,vr)-quad(M,vi);mI=2*dot(vr,mv(M,vi))
  azR=kR-om*om*mR-2*ga*om*mI;azI=kI-om*om*mI+2*ga*om*mR
  corrR,corrI=2*lr-azR,2*li-azI;rbR,rbI=lr-azR,li-azI
  def sqrtup(x,digits=18):
   from math import isqrt
   scale=10**digits;v=isqrt(x.numerator*scale*scale//x.denominator)
   if F(v*v,scale*scale)<x:v+=1
   return F(v,scale)
  residual_correction=sqrtup(rbR*rbR+rbI*rbI)
  kap2=(om*om+4*ga*ga)/(4*ga*ga) if om*om+4*ga*ga>=4 else 16/((4-om*om)**2+4*ga*ga*om*om)
  kap=sqrtup(kap2);check('outward spectral factor '+str(k),kap*kap>=kap2)
  cont=kap*eta2;oldcont=B*eta2/beta2
  check('spectral factor no worse than prior bound '+str(k),kap<=B/beta2)
  raw_report=decode(f['reported_raw_hex']);corr_report=decode(f['reported_corrected_hex']);raw_eval=sqrtup((raw_report[0]-lr)**2+(raw_report[1]-li)**2);corr_eval=sqrtup((corr_report[0]-corrR)**2+(corr_report[1]-corrI)**2)
  total_alg=sqrtup(algout2)+raw_eval;check('end to end raw algebraic budget '+str(k),total_alg<=budget)
  static_bracket=None
  if om==0:
   scale=10**6;lo=F((corrR*scale).numerator//(corrR*scale).denominator,scale);bound=corrR+cont;hi=F(-((-bound*scale).numerator//(-bound*scale).denominator),scale)
   check('static outward bracket',lo<=corrR and hi>=bound and corrI==0);static_bracket={'lower':str(lo),'upper':str(hi)}
  records.append({'omega':str(om),'gamma':str(ga),'static_continuum_bracket':static_bracket,'raw_output_real':str(lr),'raw_output_imag':str(li),'corrected_output_real':str(corrR),'corrected_output_imag':str(corrI),'flux_estimator_squared':str(eta2),'spectral_factor_squared':str(kap2),'spectral_factor_upper':str(kap),'corrected_continuum_error_bound':str(cont),'prior_factor_same_flux_bound':str(oldcont),'reported_corrected_continuum_error_bound':str(cont+corr_eval),'raw_continuum_error_bound':str(cont+residual_correction+raw_eval),'raw_algebraic_dual_residual_squared':str(eps2),'reported_raw_total_algebraic_error_bound':str(total_alg),'reported_raw_evaluation_error_bound':str(raw_eval),'reported_corrected_evaluation_error_bound':str(corr_eval),'raw_algebraic_budget':str(budget)})
  log('omega='+str(om)+' eta2~'+str(float(eta2))+' corrected continuum bound~'+str(float(cont)))
 result={'status':'PASS','classification':'CONDITIONAL_LOCAL_HIERARCHICAL_RT1_AND_SPECTRAL_OUTPUT_BOUND','check_count':len(checks),'checks':[c for c in checks if not c.startswith('assembled ')],'mesh':{'vertices':n,'tetrahedra':len(ts),'parent_max_diameter_squared':str(max(distance(parent,i,j) for tet in pts for i,j in combinations(tet,2))),'child_max_diameter_squared':str(max(distance(q,i,j) for tet in ts for i,j in combinations(tet,2))),'parent_constraint_equations':len(A),'parent_constraint_rank':240-len(free),'parent_free':len(free),'patches':len(pts),'patch_constraint_equations':len(patchdata[0][0]),'patch_constraint_rank':60-len(patchdata[0][3]),'patch_free':len(patchdata[0][3]),'assembled_constraint_equations':len(Af),'scalar_flux_checks':len(Af)*2*len(specs)},'records':records,'backend':witness['backend'],'independent_review':False,'physical_promotion':0}
 if not generate and (out/'RESULTS.json').exists():assert json.loads((out/'RESULTS.json').read_text())==result;log('read-only exact replay matches RESULTS.json')
 else:(out/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
 log('PASS '+str(len(checks))+' checks')
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('output');a.add_argument('--generate',action='store_true');args=a.parse_args();main(args.output,args.generate)
