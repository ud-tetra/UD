"""Coupled quadratic edge/face potential proposal and exact affine-curl audit."""
import sys
sys.dont_write_bytecode=True
from curl_interface import *
import gzip,struct,math
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


def decode_payload(blob,n,nr):
 raw=gzip.decompress(blob);assert len(raw)==8*n*nr,'potential payload length'
 words=struct.unpack('<'+str(n*nr)+'d',raw)
 assert all(math.isfinite(x) for x in words),'nonfinite potential coefficient'
 return [[F.from_float(x) for x in words[r*n:(r+1)*n]] for r in range(nr)]

def apply_coupled(out,q,ts,vols,flux,states,propose):
 faces={}
 for cell,t in enumerate(ts):
  for f in combinations(sorted(t),3):faces.setdefault(f,[]).append(cell)
 boundary={e for f,cs in faces.items() if len(cs)==1 for e in combinations(f,2)};edges=sorted({e for t in ts for e in combinations(sorted(t),2)}-boundary);internal=sorted(f for f,cs in faces.items() if len(cs)==2);ei={e:i for i,e in enumerate(edges)};fi={f:i for i,f in enumerate(internal)};n=2*(len(edges)+len(internal));nr=len(flux);assert len(q)==2809 and len(ts)==12288 and nr==2
 topologyhash=hashlib.sha256(json.dumps({'edges':edges,'faces':internal},separators=(',',':')).encode()).hexdigest()
 local=[];projections=[];basischecks=0;proj_norm=[F(0)]*nr
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
  for index,vals in loc:assert sum(dot(gs[i],vals[i]) for i in range(4))==0;basischecks+=1
  local.append(loc);pr=[projected(flux[r][cell],[q[i] for i in t]) for r in range(nr)];projections.append(pr)
  for r in range(nr):proj_norm[r]+=vols[cell]*pair(pr[r],pr[r])
  if cell%2048==2047:log('coupled basis and exact affine projections '+str(cell+1)+'/12288')
 log('global coupled curl space: '+str(n)+' coefficients per real component; interior edges '+str(len(edges))+' faces '+str(len(internal)))
 if propose:
  assert not (out/'CURL_WITNESS.json').exists(),'proposal requires unpublished directory'
  import scipy
  from scipy.sparse import coo_matrix,diags
  from scipy.sparse.linalg import lsmr
  L=np.linalg.cholesky((np.eye(4)+np.ones((4,4)))/20).T;metricweights=[1.,1.,2.**-.5];rows=[];cols=[];data=[];Y=np.zeros((12*len(ts),nr))
  for cell,loc in enumerate(local):
   scale=math.sqrt(float(vols[cell]))
   for index,vals in loc:
    for axis in range(3):
     ww=(L@np.array([float(v[axis]) for v in vals]))*metricweights[axis]*scale
     for j,z in enumerate(ww):
      if z:rows.append(12*cell+4*axis+j);cols.append(index);data.append(z)
   for r in range(nr):
    for axis in range(3):Y[12*cell+4*axis:12*cell+4*axis+4,r]=-metricweights[axis]*scale*(L@np.array([float(v[axis]) for v in projections[cell][r]]))
  B=coo_matrix((data,(rows,cols)),shape=(12*len(ts),n)).tocsr();scales=np.sqrt(np.asarray(B.multiply(B).sum(axis=0)).ravel());assert np.all(scales>0);D=1/scales;Bs=B@diags(D);diagnostics=[];xs=[]
  for r in range(nr):
   ans=lsmr(Bs,Y[:,r],atol=1e-11,btol=1e-11,conlim=1e12,maxiter=3000);xs.append(ans[0]*D);diagnostics.append({'component':r,'stop_code':int(ans[1]),'iterations':int(ans[2]),'residual_norm':float(ans[3]),'normal_residual_norm':float(ans[4])});log('coupled sparse proposal '+str(r+1)+'/2 iterations '+str(ans[2])+' stop '+str(ans[1]))
  raw=np.array(xs,dtype='<f8').tobytes(order='C');payload=gzip.compress(raw,mtime=0);out.joinpath('CURL_COEFFICIENTS.bin.gz').write_bytes(payload)
  wit={'topology_sha256':topologyhash,'nodes':len(q),'tetrahedra':len(ts),'interior_edges':len(edges),'interior_faces':len(internal),'coefficients_per_component':n,'components':nr,'coefficient_format':'gzip of 2*n little-endian IEEE754 binary64 words; real component then imaginary; sorted interior edges (two modes each), then sorted interior faces (two modes each)','coefficient_payload_sha256':hashlib.sha256(payload).hexdigest(),'backend':{'numpy':np.__version__,'scipy':scipy.__version__,'solver':'scipy.sparse.linalg.lsmr, positive diagonal column normalization','scope':'Weighted least-squares proposal only; exact posterior validity and decrease, no global optimality/rank or all-input IEEE claim','unequal_cell_measures_included':True,'diagnostics':diagnostics}};out.joinpath('CURL_WITNESS.json').write_text(json.dumps(wit,indent=2)+'\n')
 else:wit=json.loads(out.joinpath('CURL_WITNESS.json').read_text());payload=out.joinpath('CURL_COEFFICIENTS.bin.gz').read_bytes()
 assert wit['topology_sha256']==topologyhash and wit['coefficients_per_component']==n and wit['components']==nr and wit['coefficient_payload_sha256']==hashlib.sha256(payload).hexdigest()
 coeff=decode_payload(payload,n,nr);new=[[[*c] for c in component] for component in flux];corr=[];delta=[F(0)]*nr;orth=[F(0)]*nr;actualdiv=0
 for cell,(t,loc) in enumerate(zip(ts,local)):
  values=[[[sum(coeff[r][i]*v[j][axis] for i,v in loc) for axis in range(3)] for j in range(4)] for r in range(nr)];corr.append(values);gs=grads(q,t)
  for r in range(nr):
   cc=affine_coeff(values[r],[q[i] for i in t]);assert cc[1]+cc[6]+cc[11]==0;actualdiv+=1
   for i,v in enumerate(cc):new[r][cell][i]+=v
   delta[r]+=vols[cell]*(2*pair(projections[cell][r],values[r])+pair(values[r],values[r]));gv=[sum(states[r][node]*gs[j][axis] for j,node in enumerate(t)) for axis in range(3)];orth[r]+=vols[cell]*dot(gv,[sum(v[axis] for v in values[r]) for axis in range(3)])/4
  if cell%2048==2047:log('exact coupled affine correction '+str(cell+1)+'/12288')
 assert all(x<=0 for x in delta),'exact flux norm increased';assert not any(orth),'global gradient orthogonality failed'
 tracechecks=0;crosspatch=0;changed=0
 for f,cells in faces.items():
  normal=cross(subvec(q[f[1]],q[f[0]]),subvec(q[f[2]],q[f[0]]));macro=len(cells)==2 and cells[0]//12!=cells[1]//12;crosspatch+=int(macro)
  for vertex in f:
   for r in range(nr):
    a=dot(normal,corr[cells[0]][r][ts[cells[0]].index(vertex)]);b=dot(normal,corr[cells[1]][r][ts[cells[1]].index(vertex)]) if len(cells)==2 else F(0);assert a==b,'affine curl normal trace failed';tracechecks+=1;changed+=int(macro and a!=0)
 assert changed>0,'correction did not cross old patches'
 controls=[];raw=gzip.decompress(payload)
 for name,bad in [('truncated coefficient payload',gzip.compress(raw[:-8],mtime=0)),('nonfinite coefficient payload',gzip.compress(struct.pack('<d',float('nan'))+raw[8:],mtime=0))]:
  try:decode_payload(bad,n,nr)
  except (AssertionError,ValueError,OverflowError):controls.append(name)
  else:raise AssertionError(name+' accepted')
 f,cells=next((f,c) for f,c in faces.items() if len(c)==1);normal=cross(subvec(q[f[1]],q[f[0]]),subvec(q[f[2]],q[f[0]]));axis=next(i for i,x in enumerate(normal) if x);bad=corr[cells[0]][0][ts[cells[0]].index(f[0])][:];bad[axis]+=1;assert dot(normal,bad)!=0;controls.append('corrupted exterior affine trace')
 result={'status':'PASS','source_curl_witness_sha256':hashlib.sha256((out/'CURL_WITNESS.json').read_bytes()).hexdigest(),'source_coefficient_payload_sha256':hashlib.sha256(payload).hexdigest(),'mesh':{'nodes':len(q),'tetrahedra':len(ts),'interior_edges':len(edges),'interior_faces':len(internal),'potential_coefficients_per_component':n,'unequal_volumes':['1/4096','1/8192']},'checks':{'local_basis_divergence_identities':basischecks,'actual_affine_divergence_checks':actualdiv,'correction_face_vertex_component_checks':tracechecks,'gradient_orthogonality':nr,'exact_flux_norm_nonincrease':nr,'old_parent_interface_faces':crosspatch,'nonzero_old_parent_face_vertex_components':changed},'prior_affine_projection_norm_squared':[str(x) for x in proj_norm],'exact_flux_norm_changes':[str(x) for x in delta],'controls':controls,'backend':wit['backend'],'independent_review':False,'physical_promotion':0}
 target=out/'CURL_CORRECTION_RESULTS.json'
 if target.exists():assert json.loads(target.read_text())==result;log('read-only replay matches CURL_CORRECTION_RESULTS.json')
 else:target.write_text(json.dumps(result,indent=2)+'\n')
 log('exact coupled changes '+str([float(x) for x in delta]));return new,result
