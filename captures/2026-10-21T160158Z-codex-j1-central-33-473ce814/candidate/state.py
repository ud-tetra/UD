"""Neighboring two-word P2 wave state and exact algebraic/residual audit."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
REPO=Path(__file__).resolve().parents[3]
RROOT=REPO/'captures/2026-10-19T214921Z-codex-j1-p2-riesz-44ebda6e'
sys.path.insert(0,str(RROOT))
from riesz_lower import *
OMEGA=F(461339,102400)
GAMMA=F(33,100)
COUPLED=REPO/'captures/2026-10-19T213658Z-codex-j1-coupled-curl-86434624'

@lru_cache(None)
def moment(e):return F(6*math.prod(math.factorial(x) for x in e),math.factorial(sum(e)+3))
def pmul(p,q):
 out={}
 for e,c in p.items():
  for f,d in q.items():
   g=tuple(x+y for x,y in zip(e,f));out[g]=out.get(g,F(0))+c*d
 return {e:c for e,c in out.items() if c}
def pint(p):return sum(c*moment(e) for e,c in p.items())
def mass_reference():
 basis=[]
 for i in range(4):
  e=[0]*4;e[i]=2;f=[0]*4;f[i]=1;basis.append({tuple(e):F(2),tuple(f):F(-1)})
 for i,j in EDGES:
  e=[0]*4;e[i]=e[j]=1;basis.append({tuple(e):F(4)})
 M=[[pint(pmul(a,b)) for b in basis] for a in basis];assert [sum(row) for row in M]==MEANS
 assert mm(tr(P),mm(M,P))==[[F(1+int(i==j),20) for j in range(4)] for i in range(4)]
 alpha=F(1,1000);A=[[x-alpha*int(i==j) for j,x in enumerate(row)] for i,row in enumerate(M)];pivots=[]
 for j in range(10):
  pivot=A[j][j];assert pivot>0,'P2 reference mass lower failed';pivots.append(pivot)
  for i in range(j+1,10):
   for k in range(j+1,10):A[i][k]-=A[i][j]*A[j][k]/pivot
 return M,alpha,pivots

def decode_state2(blob,n):
 raw=gzip.decompress(blob);assert len(raw)==32*n,'P2 two-word state payload length';words=struct.unpack('<'+str(4*n)+'d',raw);assert all(math.isfinite(x) for x in words),'nonfinite P2 state word'
 return [[F.from_float(x) for x in words[r*n:(r+1)*n]] for r in range(4)]
def energy_pair(K,u,v):return dot(u,spmv(K,v))

def main(folder,generate):
 out=Path(folder);_,_,_,_,_,q,ts,_,vols,_=mesh();nv=len(q);edges=sorted({e for tet in ts for e in combinations(sorted(tet),2)});ei={e:nv+i for i,e in enumerate(edges)};n=nv+len(edges);assert n==18673
 topo=hashlib.sha256(json.dumps({'edges':edges,'cells':ts},separators=(',',':')).encode()).hexdigest();Mr,alpha,pivots=mass_reference();K=[{} for _ in range(n)];M=[{} for _ in range(n)];w=[F(0)]*n;W=[F(0)]*n;cells=[]
 for cell,t in enumerate(ts):
  frame=tuple(tuple(q[t[i]][axis]-q[t[0]][axis] for axis in range(3)) for i in range(1,4));gs,Kl,means=local(frame);ids=list(t)+[ei[tuple(sorted((t[i],t[j])))] for i,j in EDGES];mu=vols[cell];cells.append((ids,gs,Kl,mu))
  for i,node in enumerate(ids):
   w[node]+=mu*MEANS[i];W[node]+=mu
   for j,other in enumerate(ids):
    kk=mu*Kl[i][j];mm_=mu*Mr[i][j]
    if kk:K[node][other]=K[node].get(other,F(0))+kk
    if mm_:M[node][other]=M[node].get(other,F(0))+mm_
  if cell%2048==2047:log('exact P2 stiffness/mass assembly '+str(cell+1)+'/12288')
 K=[{j:x for j,x in row.items() if x} for row in K];M=[{j:x for j,x in row.items() if x} for row in M];assert spmv(M,[F(1)]*n)==w and sum(w)==2 and sum(W)==20 and min(W)>0 and not any(sum(row.values()) for row in K)
 f=[10*sum(v[:2]) for v in q]+[5*sum(q[i][axis]+q[j][axis] for axis in range(2)) for i,j in edges];g=spmv(M,f);assert sum(g)==0 and dot(f,g)==20
 om,ga=OMEGA,GAMMA;a,b=om*om,2*ga*om;beta2=4*ga*ga/(om*om+4*ga*ga);kappa=sqrtup(1/beta2)
 log('P2 nested mass, source and positive mass lower certificate PASS')
 if generate:
  assert not (out/'P2_WITNESS.json').exists(),'generation requires unpublished directory'
  import scipy
  from scipy.sparse import coo_matrix
  from scipy.sparse.linalg import splu
  rows=[];cols=[];data=[]
  for i in range(n):
   for j in K[i].keys()|M[i].keys():rows.append(i);cols.append(j);data.append(complex(float(K[i].get(j,F(0))-a*M[i].get(j,F(0))),float(b*M[i].get(j,F(0)))))
  A=coo_matrix((data,(rows,cols)),shape=(n,n)).tocsc();log('P2 complex sparse factorization starts; nnz='+str(A.nnz));lu=splu(A);gf=np.array(list(map(float,g)));wf=np.array(list(map(float,w)));hi=lu.solve(gf.astype(np.complex128));hr,hi_=decode(encode(hi.real)),decode(encode(hi.imag));vr0,vi0=project(hr,w),project(hi_,w);rr,ri=residual(K,M,g,vr0,vi0,om,ga);assert sum(rr)==sum(ri)==0;low=lu.solve(np.array([complex(float(x),float(y)) for x,y in zip(rr,ri)]));qf=hi+low;qf-=wf@qf/2;H=gf@qf;J=2*H-qf@(A@qf);raw=np.array([hi.real,hi.imag,low.real,low.imag],dtype='<f8').tobytes(order='C');payload=gzip.compress(raw,mtime=0);out.joinpath('P2_STATE.bin.gz').write_bytes(payload)
  wit={'omega':str(om),'gamma':str(ga),'nodes_P2':n,'topology_sha256':topo,'state_payload_sha256':hashlib.sha256(payload).hexdigest(),'coefficient_format':'gzip of four n-word little-endian binary64 arrays: hi real,hi imag,low real,low imag; vertices then all sorted edges; sum words exactly and subtract exact weighted mean/2','reported_raw_hex':encode([H.real,H.imag]),'reported_corrected_hex':encode([J.real,J.imag]),'backend':{'numpy':np.__version__,'scipy':scipy.__version__,'solver':'splu on full complex Neumann matrix; one exact-residual correction solve','scope':'Actual saved two-word state and actual floating output posterior audit, not an all-input IEEE guarantee.'}};out.joinpath('P2_WITNESS.json').write_text(json.dumps(wit,indent=2)+'\n');log('P2 two-word wave state proposal stored')
 else:wit=json.loads((out/'P2_WITNESS.json').read_text());payload=(out/'P2_STATE.bin.gz').read_bytes()
 assert wit['omega']==str(om) and wit['gamma']==str(ga) and wit['nodes_P2']==n and wit['topology_sha256']==topo and wit['state_payload_sha256']==hashlib.sha256(payload).hexdigest()
 words=decode_state2(payload,n);states=[project([x+y for x,y in zip(words[r],words[r+2])],w) for r in range(2)];vr,vi=states;assert dot(w,vr)==dot(w,vi)==0
 rr,ri=residual(K,M,g,vr,vi,om,ga);assert sum(rr)==sum(ri)==0;eps2=sum((x*x+y*y)/weight for x,y,weight in zip(rr,ri,W))/(4*alpha)
 kr,ki,mr,mi=spmv(K,vr),spmv(K,vi),spmv(M,vr),spmv(M,vi);lr,li=dot(g,vr),dot(g,vi);ar=dot(vr,kr)-dot(vi,ki)-a*(dot(vr,mr)-dot(vi,mi))-2*b*dot(vr,mi);ai=2*dot(vr,ki)-2*a*dot(vr,mi)+b*(dot(vr,mr)-dot(vi,mi));jr,ji=2*lr-ar,2*li-ai;rf,cf=decode(wit['reported_raw_hex']),decode(wit['reported_corrected_hex']);rev=sqrtup((rf[0]-lr)**2+(rf[1]-li)**2);cev=sqrtup((cf[0]-jr)**2+(cf[1]-ji)**2);rawalg=sqrtup(5*eps2/beta2)+rev;coralg=kappa*eps2+cev
 projected_residual2=F(0);projected_weighted2=F(0)
 for cell,(ids,gs,Kl,mu) in enumerate(cells):
  localR=F(0)
  for v in states:
   x=[v[i] for i in ids];bb=mv(tr(Q),x);pc=[20*(y-sum(bb)/5) for y in bb];assert all((pc[i]+sum(pc))/20==bb[i] for i in range(4));defect=quad(Mr,x)-(sum(y*y for y in pc)+sum(pc)**2)/20;assert defect>=0;localR+=mu*(a*a+b*b)*defect
  h2=max(distance(q,i,j) for i,j in combinations(ids[:4],2));projected_residual2+=localR;projected_weighted2+=h2*localR/9
  if cell%2048==2047:log('neighbor projected-source volume residual '+str(cell+1)+'/12288')
 controls=[];raw=gzip.decompress(payload)
 for name,bad in [('truncated state',gzip.compress(raw[:-8],mtime=0)),('nonfinite state',gzip.compress(struct.pack('<d',float('nan'))+raw[8:],mtime=0))]:
  try:decode_state2(bad,n)
  except (AssertionError,ValueError,OverflowError):controls.append(name)
  else:raise AssertionError(name+' accepted')
 assert any(x<0 for x in MEANS);controls.append('signed P2 means are not positive norm weights')
 ancestor=REPO/'captures/2026-10-19T220433Z-codex-j1-p2-state-8d4041af/P2_WITNESS.json';assert wit['topology_sha256']==json.loads(ancestor.read_text())['topology_sha256']
 result={'status':'PASS','classification':'DERIVED_CONDITIONAL_ADAPTIVE_CANDIDATE_P2_STATE','omega':str(om),'gamma':str(ga),'source_witness_sha256':hashlib.sha256((out/'P2_WITNESS.json').read_bytes()).hexdigest(),'mesh':{'nodes_P1':nv,'edges_total':len(edges),'nodes_P2':n,'tetrahedra':len(ts),'stiffness_nonzeros':sum(map(len,K)),'mass_nonzeros':sum(map(len,M)),'all_boundary_nodes_included':True},'topology_matches_original_P2':True,'exact_source_L2_squared':20,'mass_lower_alpha':str(alpha),'mass_lower_LDL_pivots':[str(x) for x in pivots],'beta_squared':str(beta2),'kappa_squared':str(1/beta2),'raw_output':[str(lr),str(li)],'corrected_output':[str(jr),str(ji)],'algebraic_dual_residual_squared_upper':str(eps2),'raw_evaluation_bound':str(rev),'corrected_evaluation_bound':str(cev),'raw_total_algebraic_output_bound':str(rawalg),'corrected_total_algebraic_output_bound':str(coralg),'algebraic_precision_target':'1/10000000000','raw_algebraic_precision_passed':rawalg<=F(1,10**10),'corrected_algebraic_precision_passed':coralg<=F(1,10**10),'projected_source_volume_residual_squared':str(projected_residual2),'projected_source_cell_Poincare_budget_squared':str(projected_weighted2),'controls':controls,'scope':'Actual neighboring two-word P2 state; algebraic bounds only here. Continuum upper requires its own new flux certificate; no inherited old-frequency output disk used.','independent_review':False,'physical_promotion':0}
 assert result['corrected_algebraic_precision_passed']
 p=out/'P2_RESULTS.json'
 if p.exists():assert json.loads(p.read_text())==result;log('read-only neighbor state replay matches P2_RESULTS.json')
 else:p.write_text(json.dumps(result,indent=2)+'\n')
 log('PASS neighbor P2 J='+str(complex(float(jr),float(ji)))+' algebraic corrected budget='+str(float(coralg)))
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('folder');ap.add_argument('--generate',action='store_true');args=ap.parse_args();main(args.folder,args.generate)
