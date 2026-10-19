"""Exact mixed flux moments; extends prior mapped RT1 audit without changing its certificate."""
import sys
sys.dont_write_bytecode=True
from patch_flux import *
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

def main(folder,generate):
 out=Path(folder);out.mkdir(parents=True,exist_ok=True)
 state_raw=(out/'STATE_WITNESS.json').read_bytes();state=json.loads(state_raw);p0,t0,_=refine(points,tets);p1,t1,P1=edgewise(p0,t0);q,ts,P2=edgewise(p1,t1);n=len(q);K,M=assemble(q,ts,[F(1,512)]*len(ts));Ks,Ms=sparse(K),sparse(M);w=spmv(Ms,[F(1)]*n);piv=max(range(n),key=lambda i:w[i]);idx=[i for i in range(n) if i!=piv];rat=[w[i]/w[piv] for i in idx]
 assert state['pivot']==piv and state['dimension']==n-1 and len(state['fixtures'])==4
 specs=[];states=[]
 for f in state['fixtures']:
  om,ga=F(f['omega']),F(f['gamma']);specs.append((om,ga));words=[decode(f[k]) for k in ['hi_real_hex','hi_imag_hex','low_real_hex','low_imag_hex']];assert all(len(x)==n-1 for x in words)
  vr=lift([a+b for a,b in zip(words[0],words[2])],idx,piv,rat,n);vi=lift([a+b for a,b in zip(words[1],words[3])],idx,piv,rat,n);assert dot(w,vr)==dot(w,vi)==0;states.extend([vr,vi])
 assert specs==[(F(0),F(1,10)),(F(4),F(1,10)),(F(9,2),F(1,10)),(F(5),F(1,10))]
 nr=len(states);assert not any(states[1]),'static state must be real'
 proj1=[];proj0=[]
 for v in states:
  fine=[]
  for cell,t in enumerate(t1):
   b=[F(0)]*4
   for child in ts[8*cell:8*cell+8]:
    values=[v[i] for i in child];s=sum(values)
    for j,a in enumerate(child):
     for i,pv in enumerate(t):b[i]+=F(1,10240)*P2[a][pv]*(s+values[j])
   c=[1280*(z-sum(b)/5) for z in b];assert all((c[i]+sum(c))/1280==b[i] for i in range(4));fine.append(c)
  coarse=[]
  for cell,t in enumerate(t0):
   b=[F(0)]*4
   for j,child in enumerate(t1[8*cell:8*cell+8]):
    values=fine[8*cell+j];s=sum(values)
    for k,a in enumerate(child):
     for i,pv in enumerate(t):b[i]+=F(1,1280)*P1[a][pv]*(s+values[k])
   c=[160*(z-sum(b)/5) for z in b];assert all((c[i]+sum(c))/160==b[i] for i in range(4));coarse.append(c)
  proj1.append(fine);proj0.append(coarse)
 log('exact fine-to-parent-to-root L2 projections complete')
 vals=[]
 for cell,t in enumerate(t0):
  local=[]
  for j,vi in enumerate(t):
   b=[]
   for k,(om,ga) in enumerate(specs):
    vr,vi_=proj0[2*k][cell][j],proj0[2*k+1][cell][j];b.extend([-om*om*vr-2*ga*om*vi_-10*sum(p0[vi][:2]),-om*om*vi_+2*ga*om*vr])
   local.append(b)
  vals.append(local)
 A,rhs=constraints(p0,t0,vals);parts,N,free=rref_many(A,rhs);G=blockmatrix(gramblocks(p0,t0,[F(1,8)]*len(t0)))
 if generate:
  assert np is not None
  proposal=minimize(N,G,parts);wit={'backend':{'numpy':np.__version__,'proposal':'complex components optimized as independent real minimum-norm flux proposals; exact reconstruction enforces constraints','coordinates':'mapped contravariant j=G j_ref, constant determinant absorbed into coefficients'},'root_free_hex':[encode(proposal[:,j]) for j in range(nr)],'patches':[]}
 else:wit=json.loads((out/'FLUX_WITNESS.json').read_text())
 assert len(wit['root_free_hex'])==nr
 root=[]
 for j in range(nr):
  x=reconstruct(parts[j],N,wit['root_free_hex'][j]);assert mv(A,x)==[b[j] for b in rhs];root.append([x[15*i:15*i+15] for i in range(16)])
 # One reference elimination, reused for every geometrical patch and RHS.
 Az,bz=constraints(RQ,RT,[[[F(0)] for _ in tet] for tet in RT]);Pr,Nr,compat,rank=operator(Az);assert rank==103 and len(Nr[0])==17
 log('reference patch operator rank103/free17 prepared')
 levels=[root];patch_index=0;patch_constraint_checks=0;map_checks=0
 for level,parents,ptets,children,ctets,P,projection,coarseproj,vol in [
  (1,p0,t0,p1,t1,P1,proj1,proj0,F(1,8)),(2,p1,t1,q,ts,P2,None,proj1,F(1,64))]:
  parentflux=levels[-1];newflux=[[None]*len(ctets) for _ in range(nr)]
  for cell,t in enumerate(ptets):
   o,Gmap,T,io,mt=geometry(parents,t);vv=[]
   for child_index,child in enumerate(ctets[8*cell:8*cell+8]):
    local=[]
    for j,vi in enumerate(child):
     diff=[]
     for r in range(nr):
      fine=projection[r][8*cell+child_index][j] if level==1 else states[r][vi]
      coarse=sum(P[vi][pv]*coarseproj[r][cell][l] for l,pv in enumerate(t));diff.append(fine-coarse)
     b=[]
     for k,(om,ga) in enumerate(specs):b.extend([-om*om*diff[2*k]-2*ga*om*diff[2*k+1],-om*om*diff[2*k+1]+2*ga*om*diff[2*k]])
     local.append(b)
    vv.append(local)
   # Trace RHS is zero; divergence rows follow reference child order.
   bs=[[F(0)]*nr for _ in range(len(Az)-32)]+[v for child in vv for v in child];assert not any(any(x for x in spmv(compat,[b[j] for b in bs])) for j in range(nr))
   pp=[spmv(Pr,[b[j] for b in bs]) for j in range(nr)];base=[transform(parentflux[j][cell],io,T,Gmap)*8 for j in range(nr)]
   objective=[[a+b for a,b in zip(base[j],pp[j])] for j in range(nr)];GG=patch_gram(tuple(x for row in mt for x in row),vol)
   if generate:
    proposals=minimize(Nr,GG,objective);record={'level':level,'cell':cell,'free_hex':[encode(proposals[:,j]) for j in range(nr)]};wit['patches'].append(record)
   else:record=wit['patches'][patch_index]
   assert record['level']==level and record['cell']==cell and len(record['free_hex'])==nr
   for j in range(nr):
    correction=reconstruct(pp[j],Nr,record['free_hex'][j]);assert mv(Az,correction)==[b[j] for b in bs];patch_constraint_checks+=len(Az)
    for k in range(8):
     cg=transform(correction[15*k:15*k+15],o,Gmap,T);newflux[j][8*cell+k]=[a+b for a,b in zip(parentflux[j][cell],cg)]
    # Exact coordinate-map roundtrip on one child polynomial.
    c=correction[:15];assert transform(transform(c,o,Gmap,T),io,T,Gmap)==c;map_checks+=1
   patch_index+=1
   if cell%16==15:log('level'+str(level)+' patches '+str(cell+1)+'/'+str(len(ptets)))
  levels.append(newflux)
 assert patch_index==144 and len(wit['patches'])==144
 if generate:(out/'FLUX_WITNESS.json').write_text(json.dumps(wit,indent=2)+'\n')
 flux=levels[-1];divchecks=0;tracechecks=0;faces={}
 for cell,t in enumerate(ts):
  for f in combinations(sorted(t),3):faces.setdefault(f,[]).append(cell)
  for vi in t:
   for k,(om,ga) in enumerate(specs):
    div=[]
    for j in [2*k,2*k+1]:
     c=flux[j][cell];div.append(c[1]+c[6]+c[11]+4*dot(c[12:],q[vi]))
    vr,vi_=states[2*k][vi],states[2*k+1][vi]
    assert div==[-om*om*vr-2*ga*om*vi_-10*sum(q[vi][:2]),-om*om*vi_+2*ga*om*vr];divchecks+=2
 log('direct final divergence checks complete')
 for f,cells in faces.items():
  assert len(cells) in [1,2];normal=cross(subvec(q[f[1]],q[f[0]]),subvec(q[f[2]],q[f[0]]))
  for vi in f:
   weights=[dot(value(b,q[vi]),normal) for b in range(15)]
   for j in range(nr):
    a=dot(weights,flux[j][cells[0]]);b=dot(weights,flux[j][cells[1]]) if len(cells)==2 else F(0);assert a==b;tracechecks+=1
 log('direct final normal-trace checks complete')
 norm=[F(0)]*nr; mixed=[F(0)]*len(specs)
 for cell,t in enumerate(ts):
  o,Gmap,T,io,mt=geometry(q,t);B=whole_gram(tuple(x for row in mt for x in row),F(1,512))
  for j in range(nr):norm[j]+=quad(B,transform(flux[j][cell],io,T,Gmap))
  for k in range(len(specs)):
   cr=transform(flux[2*k][cell],io,T,Gmap);ci=transform(flux[2*k+1][cell],io,T,Gmap)
   mixed[k]+=dot(cr,mv(B,ci))
  if cell%128==127:log('exact flux norms '+str(cell+1)+'/1024')
 solve_raw=(out/'SOLVE_RESULTS.json').read_bytes();solve=json.loads(solve_raw);assert len(solve['records'])==4;records=[];covrecords=[]
 g=spmv(Ms,[10*sum(x[:2]) for x in q]);assert sum(g)==0
 for k,((om,ga),s) in enumerate(zip(specs,solve['records'])):
  vr,vi=states[2*k],states[2*k+1];mass=dot(vr,spmv(Ms,vr))+dot(vi,spmv(Ms,vi));stiff=dot(vr,spmv(Ks,vr))+dot(vi,spmv(Ks,vi));lr=dot(g,vr);li=dot(g,vi);assert lr==F(s['raw_output_real']) and li==F(s['raw_output_imag']);assert s['omega']==str(om) and s['gamma']==str(ga)
  kR=dot(vr,spmv(Ks,vr))-dot(vi,spmv(Ks,vi));kI=2*dot(vr,spmv(Ks,vi));mR=dot(vr,spmv(Ms,vr))-dot(vi,spmv(Ms,vi));mI=2*dot(vr,spmv(Ms,vi))
  jr=2*lr-kR+om*om*mR+2*ga*om*mI;ji=2*li-kI+om*om*mI-2*ga*om*mR
  assert jr==F(s['corrected_output_real']) and ji==F(s['corrected_output_imag'])
  cr=decode(state['fixtures'][k]['reported_corrected_hex']);ev=sqrtup((cr[0]-jr)**2+(cr[1]-ji)**2);assert ev==F(s['reported_corrected_evaluation_bound'])
  eta2=norm[2*k]+norm[2*k+1]-2*lr-2*om*om*mass+stiff;assert eta2>=0
  kap2=(om*om+4*ga*ga)/(4*ga*ga) if om*om+4*ga*ga>=4 else 16/((4-om*om)**2+4*ga*ga*om*om);cont=sqrtup(kap2)*eta2;reported=cont+F(s['reported_corrected_evaluation_bound'])
  records.append({'omega':str(om),'gamma':str(ga),'flux_estimator_squared':str(eta2),'flux_norm_squared':str(norm[2*k]+norm[2*k+1]),'corrected_continuum_radius':str(cont),'reported_corrected_continuum_radius':str(reported),'precision_target':'1/10','precision_passed':reported<=F(1,10)})
  mr=dot(vr,spmv(Ms,vr));mi=dot(vi,spmv(Ms,vi));mc=dot(vr,spmv(Ms,vi));sr=dot(vr,spmv(Ks,vr));si=dot(vi,spmv(Ks,vi));sc=dot(vr,spmv(Ks,vi))
  dr=norm[2*k]+sr-2*om*om*mr-4*ga*om*mc-2*lr
  di=norm[2*k+1]+si-2*om*om*mi+4*ga*om*mc
  dc=mixed[k]+sc-2*om*om*mc-2*ga*om*(mi-mr)-li
  assert dr>=0 and di>=0 and dr*di>=dc*dc and dr+di==eta2
  covrecords.append({'omega':str(om),'gamma':str(ga),'d_real_norm_squared':str(dr),'d_imag_norm_squared':str(di),'d_cross':str(dc),'bilinear_defect_real':str(dr-di),'bilinear_defect_imag':str(2*dc),'eta_squared':str(eta2),'J_real':str(jr),'J_imag':str(ji)})
  log('omega '+str(om)+' eta²~'+str(float(eta2))+' output radius~'+str(float(reported)))
 # Structural adversarial controls: incompatible patch divergence and corrupted boundary trace.
 bad=[F(0)]*len(Az);bad[-1]=1;assert any(spmv(compat,bad)),'incompatible zero-normal divergence escaped'
 f,cells=next((f,c) for f,c in faces.items() if len(c)==1);normal=cross(subvec(q[f[1]],q[f[0]]),subvec(q[f[2]],q[f[0]]));axis=next(i for i,x in enumerate(normal) if x);c=flux[0][cells[0]][:];c[4*axis]+=1
 badtrace=sum(c[i]*dot(value(i,q[f[0]]),normal) for i in range(15));assert badtrace!=0,'corrupted boundary flux escaped'
 result={'status':'PASS','source_state_sha256':hashlib.sha256(state_raw).hexdigest(),'source_solve_sha256':hashlib.sha256(solve_raw).hexdigest(),'structural_controls':{'incompatible_patch_divergence_detected':True,'corrupted_boundary_trace_detected':True},'classification':'CONDITIONAL_1024_CELL_MAPPED_HIERARCHICAL_RT1','mesh':{'nodes':n,'tetrahedra':len(ts),'root_cells':16,'coarse_patches':16,'fine_patches':128,'reference_patch_rank':rank,'reference_patch_free':17},'checks':{'root_scalar_constraints':len(A)*nr,'mapped_patch_scalar_constraints':patch_constraint_checks,'map_roundtrips':map_checks,'final_divergence_checks':divchecks,'final_normal_trace_checks':tracechecks},'records':records,'independent_review':False,'physical_promotion':0}
 target=out/'FLUX_RESULTS.json'
 if target.exists() and not generate:assert json.loads(target.read_text())==result;log('read-only replay matches FLUX_RESULTS.json')
 else:target.write_text(json.dumps(result,indent=2)+'\n')
 cov={'status':'PASS','source_flux_witness_sha256':hashlib.sha256((out/'FLUX_WITNESS.json').read_bytes()).hexdigest(),'source_state_sha256':hashlib.sha256(state_raw).hexdigest(),'source_flux_results_sha256':hashlib.sha256((out/'FLUX_RESULTS.json').read_bytes()).hexdigest(),'records':covrecords,'independent_review':False,'physical_promotion':0}
 target=out/'COVARIANCE_RESULTS.json'
 if target.exists():assert json.loads(target.read_text())==cov;log('read-only replay matches COVARIANCE_RESULTS.json')
 else:target.write_text(json.dumps(cov,indent=2)+'\n')
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('output');a.add_argument('--generate',action='store_true');args=a.parse_args();assert not args.generate,'This extension only replays the frozen witness';main(args.output,False)
