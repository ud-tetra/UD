"""Conforming P2 Riesz test proposals and exact continuum residual lower certificate."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
REPO=Path(__file__).resolve().parents[2]
SOURCE=REPO/'captures/2026-10-19T213000Z-codex-j1-center-state-2786e1d9'
UPPER=REPO/'captures/2026-10-19T213658Z-codex-j1-coupled-curl-86434624'
sys.path.insert(0,str(SOURCE))
from center_solve import *
from center_mesh import mesh
import struct,gzip,math
from math import isqrt

EDGES=list(combinations(range(4),2))
P=eye(4)+[[F(k in e,2) for k in range(4)] for e in EDGES]
# Normalized integrals of lambda_k times each quadratic Lagrange basis.
Q=[[F(int(i==k)-1,60) for k in range(4)] for i in range(4)]+[[F(1+int(k in e),30) for k in range(4)] for e in EDGES]
MEANS=[F(-1,20)]*4+[F(1,5)]*6

def gm(a,b):return a[0]*b[0]+a[1]*b[1]+2*a[2]*b[2]
@lru_cache(None)
def local(frame):
 gs=tr(inv(frame));gs=[tuple(-sum(g[i] for g in gs) for i in range(3))]+[tuple(g) for g in gs]
 vals=[[[F(4*int(a==i)-1)*v for v in gs[i]] for a in range(4)] for i in range(4)]
 for i,j in EDGES:vals.append([[4*(int(a==i)*gs[j][k]+int(a==j)*gs[i][k]) for k in range(3)] for a in range(4)])
 assert all(sum(vals[i][a][k] for i in range(10))==0 for a in range(4) for k in range(3))
 means=[[sum(v[k] for v in row)/4 for k in range(3)] for row in vals]
 K=zeros(10,10)
 for i in range(10):
  for j in range(i,10):
   value=(sum(gm(a,b) for a,b in zip(vals[i],vals[j]))+16*gm(means[i],means[j]))/20;K[i][j]=K[j][i]=value
 assert not any(sum(row) for row in K)
 assert mm(tr(P),mm(K,P))==[[gm(a,b) for b in gs] for a in gs],'P1/P2 energy nesting'
 assert [sum(row) for row in Q]==MEANS and sum(MEANS)==1
 assert mm(tr(P),Q)==[[F(1+int(i==j),20) for j in range(4)] for i in range(4)],'P1/P2 affine load nesting'
 return gs,K,means

def decode_payload(blob,n):
 raw=gzip.decompress(blob);assert len(raw)==16*n,'dual test payload length'
 words=struct.unpack('<'+str(2*n)+'d',raw);assert all(math.isfinite(x) for x in words),'nonfinite dual coefficient'
 return [[F.from_float(x) for x in words[r*n:(r+1)*n]] for r in range(2)]

def sqrt_down(x,digits=24):
 assert x>=0;s=10**digits;y=F(isqrt(x.numerator*s*s//x.denominator),s);assert y*y<=x<(y+F(1,s))**2;return y

def lower_from_gram(G,C):
 aa,bb,cc=G[0][0],G[0][1],G[1][1];det=aa*cc-bb*bb;assert aa>0 and cc>0 and det>0,'test Gram is not positive definite'
 parts=[(cc*x*x-2*bb*x*y+aa*y*y)/det for x,y in C];assert min(parts)>=0
 return sum(parts),parts

def main(folder,generate):
 out=Path(folder);_,_,_,_,_,q,ts,_,vols,_=mesh();nv=len(q);edges=sorted({e for t in ts for e in combinations(sorted(t),2)});ei={e:nv+i for i,e in enumerate(edges)};n=nv+len(edges);assert n==18673
 topology=hashlib.sha256(json.dumps({'edges':edges,'cells':ts},separators=(',',':')).encode()).hexdigest();state_raw=(SOURCE/'CENTER_WITNESS.json').read_bytes();witstate=json.loads(state_raw);K1,M1=assemble_sparse(q,ts,vols);w1=spmv(M1,[F(1)]*nv);words=decode_state(witstate,nv);states=[project([a+b for a,b in zip(words[r],words[r+2])],w1) for r in range(2)];vr,vi=states;assert dot(w1,vr)==dot(w1,vi)==0
 om,ga=F(9,2),F(1,10);a,b=om*om,2*ga*om;rhs=[[F(0)]*n for _ in range(2)];w=[F(0)]*n;cells=[];rows=[];cols=[];data=[]
 for cell,t in enumerate(ts):
  frame=tuple(tuple(q[t[i]][axis]-q[t[0]][axis] for axis in range(3)) for i in range(1,4));gs,Kl,means=local(frame);ids=list(t)+[ei[tuple(sorted((t[i],t[j])))] for i,j in EDGES];mu=vols[cell];cells.append((ids,Kl,mu))
  sources=[[10*sum(q[k][:2])+a*vr[k]+b*vi[k] for k in t],[a*vi[k]-b*vr[k] for k in t]];gv=[[sum(states[r][node]*gs[j][axis] for j,node in enumerate(t)) for axis in range(3)] for r in range(2)]
  for i,node in enumerate(ids):
   w[node]+=mu*MEANS[i]
   for r in range(2):rhs[r][node]+=mu*(dot(Q[i],sources[r])-gm(gv[r],means[i]))
  if generate:
   for i,node in enumerate(ids):
    for j,other in enumerate(ids):
     if Kl[i][j]:rows.append(node);cols.append(other);data.append(float(mu*Kl[i][j]))
  if cell%2048==2047:log('exact P2 geometry/source assembly '+str(cell+1)+'/12288')
 assert sum(w)==2 and sum(rhs[0])==sum(rhs[1])==0
 g1=spmv(M1,[10*sum(x[:2]) for x in q]);r1=residual(K1,M1,g1,vr,vi,om,ga);pulled=[r[:nv] for r in rhs]
 for edge,node in ei.items():
  for r in range(2):
   for endpoint in edge:pulled[r][endpoint]+=rhs[r][node]/2
 assert pulled==list(r1),'P2 residual does not restrict to the frozen P1 residual'
 log('P2 constant annihilation, local nesting and exact P1 residual restriction PASS')
 if generate:
  assert not (out/'RIESZ_WITNESS.json').exists(),'generation requires unpublished directory'
  import scipy
  from scipy.sparse import coo_matrix
  from scipy.sparse.linalg import cg,LinearOperator
  K=coo_matrix((data,(rows,cols)),shape=(n,n)).tocsr();diagonal=K.diagonal()+1/n;assert np.all(diagonal>0)
  A=LinearOperator((n,n),matvec=lambda x:K@x+np.full(n,float(np.mean(x))),dtype=np.float64);M=LinearOperator((n,n),matvec=lambda x:x/diagonal,dtype=np.float64);tests=[];diagnostics=[]
  for r in range(2):
   rf=np.array(list(map(float,rhs[r])));rf-=rf.mean();count=[0]
   def callback(x):count[0]+=1
   x,info=cg(A,rf,M=M,rtol=1e-11,atol=0.,maxiter=3000,callback=callback);tests.append(x);diagnostics.append({'component':r,'stop_code':int(info),'iterations':count[0],'floating_residual_norm':float(np.linalg.norm(A@x-rf))});log('P2 Riesz proposal '+str(r+1)+'/2 iterations '+str(count[0])+' stop '+str(info))
  raw=np.array(tests,dtype='<f8').tobytes(order='C');payload=gzip.compress(raw,mtime=0);out.joinpath('RIESZ_TESTS.bin.gz').write_bytes(payload)
  wit={'omega':str(om),'gamma':str(ga),'source_state_sha256':hashlib.sha256(state_raw).hexdigest(),'topology_sha256':topology,'nodes_P1':nv,'edges_total':len(edges),'nodes_P2':n,'coefficient_format':'gzip of 2*n little-endian binary64 words, first real-residual test then imaginary-residual test; P1 vertices first, then all sorted mesh edges','test_payload_sha256':hashlib.sha256(payload).hexdigest(),'backend':{'numpy':np.__version__,'scipy':scipy.__version__,'solver':'cg with diagonal preconditioner on K_P2 + 11^T/n; proposal RHS subtracts floating Euclidean mean','scope':'Numerical Riesz test proposals only; exact lower certificate needs neither a solver tolerance guarantee nor exact Galerkin optimality.','diagnostics':diagnostics}};out.joinpath('RIESZ_WITNESS.json').write_text(json.dumps(wit,indent=2)+'\n')
 else:wit=json.loads((out/'RIESZ_WITNESS.json').read_text());payload=(out/'RIESZ_TESTS.bin.gz').read_bytes()
 assert wit['omega']==str(om) and wit['gamma']==str(ga) and wit['source_state_sha256']==hashlib.sha256(state_raw).hexdigest() and wit['topology_sha256']==topology and wit['nodes_P2']==n and wit['test_payload_sha256']==hashlib.sha256(payload).hexdigest()
 tests=decode_payload(payload,n);means=[dot(w,x)/2 for x in tests];assert all(dot(w,[x-m for x in row])==0 for row,m in zip(tests,means));C=[[dot(r,x) for x in tests] for r in rhs];G=zeros(2,2)
 for cell,(ids,Kl,mu) in enumerate(cells):
  ds=[[test[node]-test[ids[0]] for node in ids] for test in tests]
  for i in range(10):
   for j in range(i,10):
    k=mu*Kl[i][j]
    if not k:continue
    if i==j:
     G[0][0]+=k*ds[0][i]**2;G[1][1]+=k*ds[1][i]**2;G[0][1]+=k*ds[0][i]*ds[1][i]
    else:
     G[0][0]+=2*k*ds[0][i]*ds[0][j];G[1][1]+=2*k*ds[1][i]*ds[1][j];G[0][1]+=k*(ds[0][i]*ds[1][j]+ds[0][j]*ds[1][i])
  if cell%2048==2047:log('exact P2 test energy Gram '+str(cell+1)+'/12288')
 G[1][0]=G[0][1];lower,parts=lower_from_gram(G,C);single=C[0][0]**2/G[0][0]+C[1][1]**2/G[1][1];variational=2*(C[0][0]+C[1][1])-G[0][0]-G[1][1];assert lower>=single>=variational
 upperraw=(UPPER/'COUPLED_RESULTS.json').read_bytes();upper=json.loads(upperraw);assert upper['source_state_sha256']==wit['source_state_sha256'] and upper['omega']==str(om) and upper['gamma']==str(ga);U=F(upper['eta_squared']);assert 0<lower<=U
 delta2=F(upper['phase_circle_delta_squared']);assert delta2==F(2029,16);floor2=delta2*lower*lower;floor=sqrt_down(floor2);blocked=floor2>F(1,100);controls=[]
 raw=gzip.decompress(payload)
 for name,bad in [('truncated dual payload',gzip.compress(raw[:-8],mtime=0)),('nonfinite dual payload',gzip.compress(struct.pack('<d',float('inf'))+raw[8:],mtime=0))]:
  try:decode_payload(bad,n)
  except (AssertionError,ValueError,OverflowError):controls.append(name)
  else:raise AssertionError(name+' accepted')
 for name,gg in [('zero test energy',[[F(0),F(0)],[F(0),F(1)]]),('indefinite test Gram',[[F(1),F(2)],[F(2),F(1)]])]:
  try:lower_from_gram(gg,C)
  except AssertionError:controls.append(name)
  else:raise AssertionError(name+' accepted')
 result={'status':'PASS','classification':'DERIVED_CONDITIONAL_CONFORMING_P2_RESIDUAL_DUAL_LOWER','omega':str(om),'gamma':str(ga),'source_state_sha256':wit['source_state_sha256'],'source_witness_sha256':hashlib.sha256((out/'RIESZ_WITNESS.json').read_bytes()).hexdigest(),'source_upper_results_sha256':hashlib.sha256(upperraw).hexdigest(),'mesh':{'nodes_P1':nv,'edges_total':len(edges),'nodes_P2':n,'tetrahedra':len(ts),'distinct_local_geometry_cache':local.cache_info().currsize,'all_boundary_P2_nodes_included':True,'unequal_volumes':['1/4096','1/8192']},'checks':{'exact_constant_annihilation':2,'exact_source_meanfree':True,'exact_test_meanfree_projection':2,'P1_residual_restriction_coefficients':2*nv,'local_partition_gradient_mass_energy_nesting':True,'exact_Gram_positive_definite':True,'two_test_lower_dominates_separate_Rayleigh_and_variational':True,'lower_le_verified_flux_upper':True},'test_raw_means':[str(x) for x in means],'test_energy_Gram':[[str(x) for x in row] for row in G],'residual_test_pairings':[[str(x) for x in row] for row in C],'dual_component_squared_lowers':[str(x) for x in parts],'dual_norm_squared_lower':str(lower),'separate_test_Rayleigh_lower':str(single),'variational_lower':str(variational),'verified_dual_norm_squared_upper':str(U),'squared_effectivity_upper':str(U/lower),'residual_lower_fraction_of_upper':str(lower/U),'circle_delta_squared':str(delta2),'any_equilibrated_flux_circle_radius_squared_lower':str(floor2),'any_equilibrated_flux_circle_radius_lower_outward':str(floor),'circle_one_tenth_obstruction_proved':blocked,'obstruction_scope':'Only the delta*eta_squared phase-circle enclosure family for this frozen enriched state at this point, for every admissible exactly equilibrated flux. Not an actual transfer-error lower bound, not a no-go for adjoint/spectral/other certificates or a different state.','controls':controls,'backend':wit['backend'],'independent_review':False,'physical_promotion':0}
 target=out/'RIESZ_RESULTS.json'
 if target.exists():assert json.loads(target.read_text())==result;log('read-only replay matches RIESZ_RESULTS.json')
 else:target.write_text(json.dumps(result,indent=2)+'\n')
 log('PASS lower='+str(float(lower))+' upper='+str(float(U))+' ratio='+str(float(U/lower))+' circle radius floor='+str(float(floor))+' blocked='+str(blocked))
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('folder');ap.add_argument('--generate',action='store_true');args=ap.parse_args();main(args.folder,args.generate)
