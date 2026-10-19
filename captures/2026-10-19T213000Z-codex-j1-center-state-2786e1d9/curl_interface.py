"""Global interior-edge curl proposals; exact divergence/trace and energy-decrease audit."""
import sys
sys.dont_write_bytecode=True
from patch_flux import *
from red_mesh import metric

def grads(q,t):
 R=[subvec(q[i],q[t[0]]) for i in t[1:]];T=inv(R);g=tr(T);return [tuple(-sum(x[i] for x in g) for i in range(3))]+[tuple(x) for x in g]
def avgflux(c,vs):
 m=[sum(v[j] for v in vs)/4 for j in range(3)];Q=[[F(sum(v[i] for v in vs)*sum(v[j] for v in vs)+sum(v[i]*v[j] for v in vs),20) for j in range(3)] for i in range(3)]
 return [c[4*i]+sum(c[4*i+1+j]*m[j]+c[12+j]*Q[i][j] for j in range(3)) for i in range(3)]
def decode_curl(w,n,nrhs):
 assert len(w['real_components_hex'])==nrhs,'component count'
 out=[]
 for row in w['real_components_hex']:
  assert len(row)==n,'edge coefficient count'
  out.append(decode(row))
 return out

def apply_curl(out,q,ts,flux,states,propose):
 faces={}
 for k,t in enumerate(ts):
  for f in combinations(sorted(t),3):faces.setdefault(f,[]).append(k)
 boundary={e for f,c in faces.items() if len(c)==1 for e in combinations(f,2)};edges=sorted({e for t in ts for e in combinations(sorted(t),2)}-boundary);index={e:i for i,e in enumerate(edges)};n=len(edges);nr=len(flux);assert n==924 and nr==8
 curls=[];gradients=[];means=[]
 for k,t in enumerate(ts):
  gs=grads(q,t);gradients.append(gs);loc=[]
  for i,j in combinations(range(4),2):
   edge=tuple(sorted((t[i],t[j])))
   if edge in index:
    a,b=(i,j) if t[i]<t[j] else (j,i);loc.append((index[edge],tuple(2*x for x in cross(gs[a],gs[b]))))
  curls.append(loc);means.append([avgflux(flux[r][k],[q[i] for i in t]) for r in range(nr)])
 log('global curl space:924 interior edges;'+str(len(boundary))+' boundary edges excluded')
 if propose:
  assert not (out/'CURL_WITNESS.json').exists(),'proposal generation requires a new unpublished output directory'
  assert np is not None
  B=np.zeros((3*len(ts),n));Y=np.zeros((3*len(ts),nr));weights=[1.,1.,2.**-.5]
  for k,loc in enumerate(curls):
   for i,c in loc:
    for j in range(3):B[3*k+j,i]=float(c[j])*weights[j]
   for r in range(nr):
    for j in range(3):Y[3*k+j,r]=-float(means[k][r][j])*weights[j]
  coeff,residual,rank,svals=np.linalg.lstsq(B,Y,rcond=None)
  wit={'backend':{'numpy':np.__version__,'solver':'numpy.linalg.lstsq','dtype':'float64','numerical_rank':int(rank),'proposal_scope':'Minimum flux norm in the924-coefficient interior-edge curl space; exact checks establish validity and decrease, not exact optimality or an all-input IEEE guarantee.'},'interior_edges':[list(e) for e in edges],'real_components_hex':[encode(coeff[:,r]) for r in range(nr)]}
  (out/'CURL_WITNESS.json').write_text(json.dumps(wit,indent=2)+'\n');log('global curl proposals stored; numerical rank'+str(rank))
 else:wit=json.loads((out/'CURL_WITNESS.json').read_text())
 assert wit['interior_edges']==[list(e) for e in edges];coeff=decode_curl(wit,n,nr)
 correction=[[[F(0)]*3 for _ in ts] for r in range(nr)];delta=[F(0)]*nr;orth=[F(0)]*nr
 for k,(t,loc) in enumerate(zip(ts,curls)):
  for r in range(nr):
   a=tuple(sum(coeff[r][i]*c[j] for i,c in loc) for j in range(3));correction[r][k]=a;delta[r]+=F(1,512)*(2*metric(means[k][r],a)+metric(a,a));gv=[sum(states[r][vi]*gradients[k][j][axis] for j,vi in enumerate(t)) for axis in range(3)];orth[r]+=F(1,512)*dot(gv,a)
 assert all(x<=0 for x in delta),'curl proposal increases exact flux norm'
 assert not any(orth),'curl gradient orthogonality failed'
 traces=0;macro=0;changed=0
 for f,cells in faces.items():
  normal=cross(subvec(q[f[1]],q[f[0]]),subvec(q[f[2]],q[f[0]]));ismacro=len(cells)==2 and cells[0]//64!=cells[1]//64
  macro+=int(ismacro)
  for r in range(nr):
   a=dot(normal,correction[r][cells[0]]);b=dot(normal,correction[r][cells[1]]) if len(cells)==2 else F(0);assert a==b,'curl normal trace discontinuity';traces+=1
   changed+=int(ismacro and a!=0)
 new=[[[*flux[r][k]] for k in range(len(ts))] for r in range(nr)]
 for r in range(nr):
  for k in range(len(ts)):
   for axis in range(3):new[r][k][4*axis]+=correction[r][k][axis]
 assert changed>0,'no coarse interface correction'
 controls=[]
 for name,mutate in [('nonfinite coefficient',lambda w:w['real_components_hex'][0].__setitem__(0,'nan')),('truncated edge coefficients',lambda w:w['real_components_hex'][0].pop())]:
  bad=json.loads(json.dumps(wit));mutate(bad)
  try:decode_curl(bad,n,nr)
  except (AssertionError,ValueError,OverflowError):controls.append(name)
  else:raise AssertionError(name+' accepted')
 # A local constant perturbation on an exterior cell must fail the boundary normal test.
 f,cells=next((f,c) for f,c in faces.items() if len(c)==1);normal=cross(subvec(q[f[1]],q[f[0]]),subvec(q[f[2]],q[f[0]]));axis=next(i for i,v in enumerate(normal) if v);bad=list(correction[0][cells[0]]);bad[axis]+=1;assert dot(normal,bad)!=0;controls.append('corrupted exterior curl trace')
 result={'status':'PASS','source_curl_witness_sha256':hashlib.sha256((out/'CURL_WITNESS.json').read_bytes()).hexdigest(),'mesh':{'nodes':len(q),'tetrahedra':len(ts),'interior_edges':n,'boundary_edges_excluded':len(boundary),'original_macro_interface_faces':macro},'checks':{'constant_curl_divergence_identities':len(ts)*nr,'correction_face_component_trace_checks':traces,'global_gradient_orthogonality':nr,'exact_flux_norm_nonincrease':nr,'nonzero_original_macro_trace_components':changed},'exact_flux_norm_changes':[str(x) for x in delta],'controls':controls,'backend':wit['backend'],'independent_review':False,'physical_promotion':0}
 target=out/'CURL_CORRECTION_RESULTS.json'
 if target.exists():assert json.loads(target.read_text())==result;log('read-only replay matches CURL_CORRECTION_RESULTS.json')
 else:target.write_text(json.dumps(result,indent=2)+'\n')
 old=json.loads((out/'FLUX_RESULTS.json').read_text());floors=[]
 for k,rec in enumerate(old['records']):
  meansq=sum(F(1,512)*(metric(row[2*k],row[2*k])+metric(row[2*k+1],row[2*k+1])) for row in means)
  floor=F(rec['flux_norm_squared'])-meansq;assert floor>=0
  floors.append({'omega':rec['omega'],'gamma':rec['gamma'],'cell_mean_flux_norm_squared':str(meansq),'constant_correction_eta_squared_floor':str(floor)})
 floor_result={'status':'PASS','source_flux_witness_sha256':hashlib.sha256((out/'FLUX_WITNESS.json').read_bytes()).hexdigest(),'source_flux_results_sha256':hashlib.sha256((out/'FLUX_RESULTS.json').read_bytes()).hexdigest(),'records':floors,'scope':'Exact within-cell flux variance. It is invariant under every piecewise constant correction, even without continuity/divergence restrictions. This lower-bounds eta squared, not actual transfer error.','independent_review':False,'physical_promotion':0}
 target=out/'CONSTANT_FLOOR_RESULTS.json'
 if target.exists():assert json.loads(target.read_text())==floor_result;log('read-only replay matches CONSTANT_FLOOR_RESULTS.json')
 else:target.write_text(json.dumps(floor_result,indent=2)+'\n')
 log('exact curl corrections pass; changed macro traces '+str(changed));return new,result
