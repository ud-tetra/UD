"""Affine divergencefree curls of quadratic edge/face potentials; exact posterior audit."""
import sys
sys.dont_write_bytecode=True
from curl_interface import *

def projected(c,vs):
 sx=[sum(v[j] for v in vs) for j in range(3)];beta=[dot(c[12:],v) for v in vs];sb=sum(beta);xb=[sum(v[i]*b for v,b in zip(vs,beta)) for i in range(3)];m=[]
 for a in range(4):
  m.append([c[4*i]/4+sum(c[4*i+1+j]*(sx[j]+vs[a][j])/20 for j in range(3))+(sx[i]*sb+xb[i]+vs[a][i]*sb+beta[a]*sx[i]+2*vs[a][i]*beta[a])/120 for i in range(3)])
 sm=[sum(row[i] for row in m) for i in range(3)];p=[[20*m[a][i]-4*sm[i] for i in range(3)] for a in range(4)]
 assert [sum(row[i] for row in p)/4 for i in range(3)]==avgflux(c,vs)
 return p

def affine_coeff(values,vs):
 D=inv([[F(1),*v] for v in vs]);return [x for axis in range(3) for x in mv(D,[v[axis] for v in values])]
def pair(u,v):
 return (sum(metric(a,b) for a,b in zip(u,v))+metric([sum(a[i] for a in u) for i in range(3)],[sum(a[i] for a in v) for i in range(3)]))/20

def apply_linear(out,q,ts,flux,states,propose):
 faces={}
 for cell,t in enumerate(ts):
  for f in combinations(sorted(t),3):faces.setdefault(f,[]).append(cell)
 boundary={e for f,cs in faces.items() if len(cs)==1 for e in combinations(f,2)};edges=sorted({e for t in ts for e in combinations(sorted(t),2)}-boundary);internal=sorted(f for f,cs in faces.items() if len(cs)==2);ei={e:i for i,e in enumerate(edges)};fi={f:i for i,f in enumerate(internal)};n=2*(len(edges)+len(internal));nr=len(flux);assert n==5560 and nr==8
 local=[];projections=[];basis_divchecks=0
 for cell,t in enumerate(ts):
  gs=grads(q,t);idx={v:i for i,v in enumerate(t)};loc=[]
  for e in combinations(sorted(t),2):
   if e not in ei:continue
   i,j=map(idx.get,e);v=cross(gs[i],gs[j])
   for k,node in enumerate([i,j]):
    vals=[[F(0)]*3 for _ in range(4)];vals[node]=[3*x for x in v];loc.append((2*ei[e]+k,vals))
  for f in combinations(sorted(t),3):
   if f not in fi:continue
   ids=list(map(idx.get,f))
   for k,(a,b,c) in enumerate([ids,[ids[1],ids[2],ids[0]]]):
    vals=[[F(0)]*3 for _ in range(4)];vals[b]=list(cross(gs[a],gs[c]));vals[c]=[-x for x in cross(gs[a],gs[b])];vals[a]=[2*x for x in cross(gs[b],gs[c])];loc.append((2*len(edges)+2*fi[f]+k,vals))
  for index,vals in loc:assert sum(dot(gs[i],vals[i]) for i in range(4))==0;basis_divchecks+=1
  local.append(loc);projections.append([projected(flux[r][cell],[q[i] for i in t]) for r in range(nr)])
 log('affine curl basis prepared:5560 coefficients;'+str(basis_divchecks)+' exact local divergence identities')
 if propose:
  assert not (out/'LINEAR_WITNESS.json').exists(),'generation needs an unpublished directory'
  import scipy
  from scipy.sparse import coo_matrix
  from scipy.sparse.linalg import lsmr
  L=np.linalg.cholesky((np.eye(4)+np.ones((4,4)))/20).T;weights=[1.,1.,2.**-.5];rows=[];cols=[];data=[];Y=np.zeros((12*len(ts),nr))
  for cell,loc in enumerate(local):
   for index,vals in loc:
    for axis in range(3):
     w=L@np.array([float(v[axis]) for v in vals])*weights[axis]
     for a,z in enumerate(w):
      if z:rows.append(12*cell+4*axis+a);cols.append(index);data.append(z)
   for r in range(nr):
    for axis in range(3):Y[12*cell+4*axis:12*cell+4*axis+4,r]=-weights[axis]*(L@np.array([float(v[axis]) for v in projections[cell][r]]))
  B=coo_matrix((data,(rows,cols)),shape=(12*len(ts),n)).tocsr();words=[];diagnostics=[]
  for r in range(nr):
   x=lsmr(B,Y[:,r],atol=1e-11,btol=1e-11,conlim=1e12,maxiter=2500);words.append(encode(x[0]));diagnostics.append({'component':r,'stop_code':int(x[1]),'iterations':int(x[2]),'residual_norm':float(x[3]),'normal_residual_norm':float(x[4])});log('linear curl proposal '+str(r+1)+'/8;iterations'+str(x[2]))
  wit={'backend':{'numpy':np.__version__,'scipy':scipy.__version__,'solver':'scipy.sparse.linalg.lsmr','dtype':'float64','scope':'Sparse least-squares proposal in edge/face potential space; exact posterior validity/decrease, not exact optimality/rank or all-input IEEE theorem.','diagnostics':diagnostics},'edges':[list(e) for e in edges],'faces':[list(f) for f in internal],'real_components_hex':words};(out/'LINEAR_WITNESS.json').write_text(json.dumps(wit,indent=2)+'\n')
 else:wit=json.loads((out/'LINEAR_WITNESS.json').read_text())
 assert wit['edges']==[list(e) for e in edges] and wit['faces']==[list(f) for f in internal];coeff=decode_curl(wit,n,nr);new=[[[*flux[r][cell]] for cell in range(len(ts))] for r in range(nr)];corr=[];delta=[F(0)]*nr;orth=[F(0)]*nr;actualdiv=0
 for cell,(t,loc) in enumerate(zip(ts,local)):
  values=[[[sum(coeff[r][i]*v[a][axis] for i,v in loc) for axis in range(3)] for a in range(4)] for r in range(nr)];corr.append(values);gs=grads(q,t)
  for r in range(nr):
   cc=affine_coeff(values[r],[q[i] for i in t]);assert cc[1]+cc[6]+cc[11]==0;actualdiv+=1
   for i,v in enumerate(cc):new[r][cell][i]+=v
   delta[r]+=F(1,512)*(2*pair(projections[cell][r],values[r])+pair(values[r],values[r]));gv=[sum(states[r][vi]*gs[j][axis] for j,vi in enumerate(t)) for axis in range(3)];orth[r]+=F(1,2048)*dot(gv,[sum(v[axis] for v in values[r]) for axis in range(3)])
  if cell%128==127:log('exact affine curl reconstruction '+str(cell+1)+'/1024')
 assert all(x<=0 for x in delta),'exact flux norm increased';assert not any(orth),'global gradient orthogonality failed'
 tracechecks=0;nonconstant=0
 for cell,t in enumerate(ts):
  for r in range(nr):nonconstant+=int(any(v!=corr[cell][r][0] for v in corr[cell][r][1:]))
 for f,cells in faces.items():
  normal=cross(subvec(q[f[1]],q[f[0]]),subvec(q[f[2]],q[f[0]]))
  for vi in f:
   aidx=ts[cells[0]].index(vi)
   for r in range(nr):
    a=dot(normal,corr[cells[0]][r][aidx]);b=dot(normal,corr[cells[1]][r][ts[cells[1]].index(vi)]) if len(cells)==2 else F(0);assert a==b,'affine curl trace discontinuity';tracechecks+=1
 controls=[]
 for name,mutate in [('nonfinite potential coefficient',lambda w:w['real_components_hex'][0].__setitem__(0,'nan')),('truncated potential coefficients',lambda w:w['real_components_hex'][0].pop())]:
  bad=json.loads(json.dumps(wit));mutate(bad)
  try:decode_curl(bad,n,nr)
  except (AssertionError,ValueError,OverflowError):controls.append(name)
  else:raise AssertionError(name+' accepted')
 assert nonconstant>0
 result={'status':'PASS','source_linear_witness_sha256':hashlib.sha256((out/'LINEAR_WITNESS.json').read_bytes()).hexdigest(),'mesh':{'nodes':len(q),'tetrahedra':len(ts),'interior_edges':len(edges),'interior_faces':len(internal),'potential_coefficients_per_component':n},'checks':{'local_basis_divergence_identities':basis_divchecks,'actual_affine_divergence_checks':actualdiv,'correction_face_vertex_component_checks':tracechecks,'gradient_orthogonality':nr,'exact_flux_norm_nonincrease':nr,'nonconstant_cell_components':nonconstant},'exact_flux_norm_changes':[str(x) for x in delta],'controls':controls,'backend':wit['backend'],'independent_review':False,'physical_promotion':0}
 target=out/'LINEAR_CORRECTION_RESULTS.json'
 if target.exists():assert json.loads(target.read_text())==result;log('read-only replay matches LINEAR_CORRECTION_RESULTS.json')
 else:target.write_text(json.dumps(result,indent=2)+'\n')
 return new,result
