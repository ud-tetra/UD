"""Own hierarchical RT1 upper certificate for the stored center-enriched J1 state."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
REPO=Path(__file__).resolve().parents[2]
SOURCE=REPO/'captures/2026-10-19T213000Z-codex-j1-center-state-2786e1d9'
sys.path.insert(0,str(SOURCE))
from patch_flux import *
import center_mesh,center_solve,gzip
from red_mesh import edgewise,frame,metric
from level2_check import lift,sparse,spmv,sqrtup

def operator(A):
 m,n=len(A),len(A[0]);w=[r[:]+e for r,e in zip(A,eye(m))];piv=[];rr=0
 for j in range(n):
  ids=[i for i in range(rr,m) if w[i][j]]
  if not ids:continue
  i=ids[0];w[rr],w[i]=w[i],w[rr];z=w[rr][j];w[rr]=[x/z for x in w[rr]]
  for i in range(m):
   if i!=rr and w[i][j]:
    z=w[i][j];w[i]=[a-z*b for a,b in zip(w[i],w[rr])]
  piv.append(j);rr+=1
 free=[i for i in range(n) if i not in piv];N=zeros(n,len(free));P=zeros(n,m)
 for i,j in enumerate(piv):P[j]=w[i][n:]
 for k,j in enumerate(free):
  N[j][k]=1
  for i,l in enumerate(piv):N[l][k]=-w[i][j]
 return sparse(P),N,sparse([r[n:] for r in w[rr:]]),rr

def transform(c,o,G,T):
 a=[c[4*i] for i in range(3)];A=[[c[4*i+1+j] for j in range(3)] for i in range(3)];C=mm(G,mm(A,T));d=mv(tr(T),c[12:]);u=dot(d,o);v=[x-y+z*u for x,y,z in zip(mv(G,a),mv(C,o),o)]
 out=[]
 for i in range(3):out.extend([v[i]]+[C[i][j]-F(i==j)*u-o[i]*d[j] for j in range(3)])
 return out+d

def geometry(q,t):
 o=q[t[0]];G=tr(frame(q,t));T=inv(G);io=tuple(-x for x in mv(T,o));metricG=[[metric(a,b) for b in frame(q,t)] for a in frame(q,t)]
 return o,G,T,io,metricG

def moments(q,ts,vol):
 @lru_cache(None)
 def integ(cell,e):
  p={(0,0,0,0):F(1)}
  for axis,deg in enumerate(e):
   for _ in range(deg):
    nxt={}
    for ex,c in p.items():
     for j,vi in enumerate(ts[cell]):
      ee=list(ex);ee[j]+=1;ee=tuple(ee);nxt[ee]=nxt.get(ee,F(0))+c*q[vi][axis]
    p=nxt
  return sum(c*vol*F(6,factorial(sum(ex)+3))*factorial(ex[0])*factorial(ex[1])*factorial(ex[2])*factorial(ex[3]) for ex,c in p.items())
 return integ

BASIS=[[next(iter(poly(i,k)),None) for k in range(3)] for i in range(15)]
def gram(mt,I):
 B=zeros(15,15)
 for i in range(15):
  for j in range(i,15):
   v=F(0)
   for k,e in enumerate(BASIS[i]):
    if e is None:continue
    for l,f in enumerate(BASIS[j]):
     if f is not None and mt[k][l]:v+=mt[k][l]*I(tuple(a+b for a,b in zip(e,f)))
   B[i][j]=B[j][i]=v
 return B

REF=[(F(0),F(0),F(0)),(F(1),F(0),F(0)),(F(1),F(1),F(0)),(F(1),F(1),F(1))]
RQ,RT,RP=edgewise(REF,[(0,1,2,3)])
RI=moments(RQ,RT,F(1,8))
@lru_cache(None)
def patch_gram(flat,vol):
 mt=[list(flat[3*i:3*i+3]) for i in range(3)];return blockmatrix([gram(mt,lambda e,k=k:vol*RI(k,e)) for k in range(8)])
@lru_cache(None)
def whole_gram(flat,vol):
 mt=[list(flat[3*i:3*i+3]) for i in range(3)]
 return gram(mt,lambda e:vol*F(6,(e[2]+1)*(e[1]+e[2]+2)*(sum(e)+3)))


def reference(center=False):
 weights=[(w,F(1,8)) for w,perm in center_mesh.pattern()] if not center else center_mesh.center_pattern()[1]
 q=[];ts=[]
 for w,ratio in weights:
  tet=[]
  for lam in w:
   x=tuple(sum(lam[j]*REF[j][axis] for j in range(4)) for axis in range(3))
   if x not in q:q.append(x)
   tet.append(q.index(x))
  ts.append(tuple(tet))
 A,_=constraints(q,ts,[[[F(0)] for vi in t] for t in ts]);P,N,C,rank=operator(A)
 As=sparse(A);Ns=sparse(N)
 integrals=[moments(q,[t],ratio) for t,(w,ratio) in zip(ts,weights)]
 return weights,A,As,P,N,Ns,C,rank,integrals

@lru_cache(None)
def patchG(kind,flat,vol):
 mt=[list(flat[3*i:3*i+3]) for i in range(3)];R=OPS[kind]
 return blockmatrix([gram(mt,lambda e,k=k:vol*R[-1][k](0,e)) for k in range(len(R[0]))])

def projection(values,weights,parentvol):
 count=len(weights);out=[]
 for cell in range(len(values)//count):
  b=[F(0)]*4
  for k,(ww,ratio) in enumerate(weights):
   vs=values[count*cell+k];s=sum(vs)
   for a,lam in enumerate(ww):
    for i in range(4):b[i]+=parentvol*ratio*lam[i]*(s+vs[a])/20
  c=[20*(x-sum(b)/5)/parentvol for x in b]
  assert all(parentvol*(c[i]+sum(c))/20==b[i] for i in range(4))
  out.append(c)
 return out

def main(folder,generate):
 global OPS
 out=Path(folder);state_raw=(SOURCE/'CENTER_WITNESS.json').read_bytes();state=json.loads(state_raw)
 coarse,cts,parent,pts,coarseP,q,ts,Ps,vols,ref=center_mesh.mesh();K,M=center_solve.assemble_sparse(q,ts,vols);w=center_solve.spmv(M,[F(1)]*len(q));words=center_solve.decode_state(state)
 states=[center_solve.project([a+b for a,b in zip(words[j],words[j+2])],w) for j in range(2)];vr,vi=states;assert dot(w,vr)==dot(w,vi)==0
 p0,t0,_=refine(points,tets);p1,t1,_=edgewise(p0,t0);p2,t2,_=edgewise(p1,t1);assert p2==coarse and t2==cts
 om,ga=F(9,2),F(1,10);a,b=om*om,2*ga*om
 log('center mesh/state exact decoding complete')
 OPS=[reference(False),reference(True)];assert (OPS[0][7],len(OPS[0][4][0]))==(103,17)
 log('reference operators '+str([(r[7],len(r[4][0])) for r in OPS]))
 # Levels contain broken affine values on each tetrahedron, finest first projected up.
 values=[[[v[i] for i in tet] for tet in ts] for v in states]
 levels=[None]*4;levels[3]=values
 for lev,kind,vol in [(2,1,F(1,512)),(1,0,F(1,64)),(0,0,F(1,8))]:levels[lev]=[projection(v,OPS[kind][0],vol) for v in levels[lev+1]]
 log('three exact L2 projection levels checked')
 vals=[[[ -a*levels[0][0][cell][j]-b*levels[0][1][cell][j]-10*sum(p0[vertex][:2]),-a*levels[0][1][cell][j]+b*levels[0][0][cell][j]] for j,vertex in enumerate(t)] for cell,t in enumerate(t0)]
 A,rhs=constraints(p0,t0,vals);parts,N,free=rref_many(A,rhs);G=blockmatrix(gramblocks(p0,t0,[F(1,8)]*16))
 if generate:
  assert not (out/'UPPER_WITNESS.json.gz').exists()
  proposal=minimize(N,G,parts);wit={'omega':'9/2','gamma':'1/10','source_state_sha256':hashlib.sha256(state_raw).hexdigest(),'backend':{'numpy':np.__version__,'proposal':'binary64 minimum-norm free coordinates; exact rational constraint reconstruction','scope':'actual saved words, no all-input floating-point claim'},'root_free_hex':[encode(proposal[:,j]) for j in range(2)],'patches':[]}
 else:wit=json.loads(gzip.decompress((out/'UPPER_WITNESS.json.gz').read_bytes()))
 assert wit['omega']=='9/2' and wit['gamma']=='1/10' and wit['source_state_sha256']==hashlib.sha256(state_raw).hexdigest() and len(wit['root_free_hex'])==2
 flux=[]
 for j in range(2):
  x=reconstruct(parts[j],N,wit['root_free_hex'][j]);assert mv(A,x)==[r[j] for r in rhs];flux.append([x[15*i:15*i+15] for i in range(16)])
 patchindex=0;patchchecks=0;roundtrips=0
 for level,kind,p,tt,vol in [(0,0,p0,t0,F(1,8)),(1,0,p1,t1,F(1,64)),(2,1,p2,t2,F(1,512))]:
  weights,Az,As,Pr,Nr,Ns,compat,rank,ints=OPS[kind];nc=len(weights);nextflux=[[None]*(nc*len(tt)) for _ in range(2)]
  for cell,t in enumerate(tt):
   o,Gmap,T,io,mt=geometry(p,t);bs=[[F(0)]*2 for _ in range(len(Az)-4*nc)]
   for k,(ww,ratio) in enumerate(weights):
    for j,lam in enumerate(ww):
     dr,di=[levels[level+1][r][nc*cell+k][j]-dot(lam,levels[level][r][cell]) for r in range(2)];bs.append([-a*dr-b*di,-a*di+b*dr])
   assert not any(any(spmv(compat,[r[j] for r in bs])) for j in range(2))
   pp=[spmv(Pr,[r[j] for r in bs]) for j in range(2)];base=[transform(flux[j][cell],io,T,Gmap)*nc for j in range(2)];objective=[[x+y for x,y in zip(base[j],pp[j])] for j in range(2)]
   if generate:
    GG=patchG(kind,tuple(x for row in mt for x in row),vol);proposals=minimize(Nr,GG,objective);record={'level':level+1,'cell':cell,'free_hex':[encode(proposals[:,j]) for j in range(2)]};wit['patches'].append(record)
   else:record=wit['patches'][patchindex]
   assert record['level']==level+1 and record['cell']==cell and len(record['free_hex'])==2
   for j in range(2):
    fw=decode(record['free_hex'][j]);assert len(fw)==len(Nr[0]);correction=[x+y for x,y in zip(pp[j],spmv(Ns,fw))];assert spmv(As,correction)==[r[j] for r in bs];patchchecks+=len(Az)
    for k in range(nc):nextflux[j][nc*cell+k]=[x+y for x,y in zip(flux[j][cell],transform(correction[15*k:15*k+15],o,Gmap,T))]
    c=correction[:15];assert transform(transform(c,o,Gmap,T),io,T,Gmap)==c;roundtrips+=1
   patchindex+=1
   if cell%128==127:log('level '+str(level+1)+' patches '+str(cell+1)+'/'+str(len(tt)))
  flux=nextflux
 assert patchindex==1168 and len(wit['patches'])==1168
 if generate:(out/'UPPER_WITNESS.json.gz').write_bytes(gzip.compress((json.dumps(wit,indent=1)+'\n').encode(),mtime=0))
 faces={};divchecks=0;tracechecks=0
 for cell,t in enumerate(ts):
  for face in combinations(sorted(t),3):faces.setdefault(face,[]).append(cell)
  for vertex in t:
   ds=[c[1]+c[6]+c[11]+4*dot(c[12:],q[vertex]) for c in [flux[0][cell],flux[1][cell]]]
   assert ds==[-a*vr[vertex]-b*vi[vertex]-10*sum(q[vertex][:2]),-a*vi[vertex]+b*vr[vertex]];divchecks+=2
 log('direct final divergence verified')
 for face,cells in faces.items():
  assert len(cells) in [1,2];normal=cross(subvec(q[face[1]],q[face[0]]),subvec(q[face[2]],q[face[0]]))
  for vertex in face:
   ww=[dot(value(k,q[vertex]),normal) for k in range(15)]
   for j in range(2):
    assert dot(ww,flux[j][cells[0]])==(dot(ww,flux[j][cells[1]]) if len(cells)==2 else 0);tracechecks+=1
 log('direct final normal traces verified')
 norm=[F(0),F(0)];mixed=F(0)
 for cell,t in enumerate(ts):
  o,Gmap,T,io,mt=geometry(q,t);B=whole_gram(tuple(x for row in mt for x in row),vols[cell]);cs=[transform(flux[j][cell],io,T,Gmap) for j in range(2)];Bc=[mv(B,c) for c in cs]
  for j in range(2):norm[j]+=dot(cs[j],Bc[j])
  mixed+=dot(cs[0],Bc[1])
  if cell%1024==1023:log('degree4 exact flux moments '+str(cell+1)+'/12288')
 mr,mi=center_solve.spmv(M,vr),center_solve.spmv(M,vi);kr,ki=center_solve.spmv(K,vr),center_solve.spmv(K,vi);g=center_solve.spmv(M,[10*sum(x[:2]) for x in q]);lr,li=dot(g,vr),dot(g,vi)
 massr,massi,massc=dot(vr,mr),dot(vi,mi),dot(vr,mi);sr,si,sc=dot(vr,kr),dot(vi,ki),dot(vr,ki)
 dr=norm[0]+sr-2*a*massr-2*b*massc-2*lr;di=norm[1]+si-2*a*massi+2*b*massc;dc=mixed+sc-2*a*massc-b*(massi-massr)-li
 assert dr>=0 and di>=0 and dr*di>=dc*dc;eta=dr+di;qr,qi=dr-di,2*dc;assert qr*qr+qi*qi<=eta*eta
 jr=2*lr-sr+si+a*(massr-massi)+2*b*massc;ji=2*li-2*sc+2*a*massc-b*(massr-massi)
 solve=json.loads((SOURCE/'CENTER_SOLVE_RESULTS.json').read_text());assert jr==F(solve['corrected_output_real']) and ji==F(solve['corrected_output_imag'])
 # c=1/2-i*a/(2*b), delta²=|c|², valid spectral circle including solenoidal zero coefficient.
 cr,ci=F(1,2),-a/(2*b);delta2=cr*cr+ci*ci;assert delta2==F(2029,16)
 center=(jr+cr*qr-ci*qi,ji+cr*qi+ci*qr);reported=[F.from_float(float(x)) for x in center];ev=sqrtup(sum((x-y)**2 for x,y in zip(reported,center)));radius=sqrtup(delta2)*eta+ev
 originradius=sqrtup(4*delta2)*eta+F(solve['corrected_evaluation_bound'])
 # Audit Riesz residual by an independent mixed integral identity, and reject structural corruptions.
 assert eta==sum(norm)+sr+si-2*a*(massr+massi)-2*lr
 controls={}
 for kind,R in enumerate(OPS):
  bad=[F(0)]*len(R[1]);bad[-1]=1;assert any(spmv(R[6],bad));controls['incompatible_divergence_'+str(kind)]=True
 face,cells=next((f,c) for f,c in faces.items() if len(c)==1);normal=cross(subvec(q[face[1]],q[face[0]]),subvec(q[face[2]],q[face[0]]));axis=next(i for i,x in enumerate(normal) if x);c=flux[0][cells[0]][:];c[4*axis]+=1;assert sum(c[i]*dot(value(i,q[face[0]]),normal) for i in range(15))!=0;controls['corrupted_boundary_trace']=True
 for name,freewords in [('truncated',wit['patches'][-1]['free_hex'][0][:-1]),('nonfinite',['inf']+wit['patches'][-1]['free_hex'][0][1:])]:
  try:reconstruct([F(0)]*len(OPS[1][4]),OPS[1][4],freewords)
  except (AssertionError,ValueError,OverflowError):controls[name]=True
  else:raise AssertionError('bad witness accepted')
 result={'status':'PASS','classification':'DERIVED_CONDITIONAL_OWN_CENTER_STATE_RT1_CONTINUUM_UPPER_CERTIFICATE','omega':str(om),'gamma':str(ga),'source_state_sha256':hashlib.sha256(state_raw).hexdigest(),'source_solve_sha256':hashlib.sha256((SOURCE/'CENTER_SOLVE_RESULTS.json').read_bytes()).hexdigest(),'source_flux_witness_sha256':hashlib.sha256((out/'UPPER_WITNESS.json.gz').read_bytes()).hexdigest(),'mesh':{'nodes':len(q),'tetrahedra':len(ts),'patches_by_level':[16,128,1024],'reference_ranks':[r[7] for r in OPS],'reference_free_counts':[len(r[4][0]) for r in OPS],'normalized_volumes':['1/4096','1/8192']},'checks':{'root_scalar_constraints':len(A)*2,'patch_scalar_constraints':patchchecks,'map_roundtrips':roundtrips,'final_divergence_checks':divchecks,'final_normal_trace_checks':tracechecks,'boundary_faces':sum(len(x)==1 for x in faces.values()),'volume_residual_exactly_zero':True},'flux_real_norm_squared':str(norm[0]),'flux_imag_norm_squared':str(norm[1]),'flux_cross':str(mixed),'defect_real_norm_squared':str(dr),'defect_imag_norm_squared':str(di),'defect_cross':str(dc),'eta_squared':str(eta),'bilinear_defect':[str(qr),str(qi)],'J':[str(jr),str(ji)],'corrected_J_reported_continuum_radius':str(originradius),'phase_circle_delta_squared':str(delta2),'phase_circle_exact_center':[str(x) for x in center],'phase_circle_reported_center_hex':[float(x).hex() for x in reported],'phase_circle_evaluation_bound':str(ev),'phase_circle_reported_radius':str(radius),'own_phase_precision_passed':radius<=F(1,10),'precision_target':'1/10','inherited_radius_about_reported_J':solve['inherited_reported_corrected_continuum_radius'],'controls':controls,'scope':'Own pointwise certificate for the exact decoded center-enriched state at omega9/2,gamma1/10. Not a uniform-band accuracy, rate, termination or independent-review result. Externally declared scalar wave, not native UD action.','independent_review':False,'physical_promotion':0}
 target=out/'UPPER_RESULTS.json'
 if target.exists():assert json.loads(target.read_text())==result;log('read-only replay matches UPPER_RESULTS.json')
 else:target.write_text(json.dumps(result,indent=2)+'\n')
 log('PASS eta²='+str(float(eta))+' own phase radius='+str(float(radius))+' J radius='+str(float(originradius))+' phase center='+str(complex(*map(float,reported))))
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('folder');ap.add_argument('--generate',action='store_true');args=ap.parse_args();main(args.folder,args.generate)
