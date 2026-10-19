"""Interior-center enriched P1 state at omega9/2; sparse proposal and exact audit."""
import sys
sys.dont_write_bytecode=True
from curl_interface import *
from red_mesh import edgewise,determinant,frame,pattern
from level2_check import sqrtup,lift
import platform

def assemble_sparse(q,ts,vol):
 K=[{} for _ in q];M=[{} for _ in q]
 for cell,t in enumerate(ts):
  cellvol=vol[cell] if isinstance(vol,list) else vol;gs=grads(q,t)
  for i,a in enumerate(t):
   for j,b in enumerate(t):
    v=cellvol*(gs[i][0]*gs[j][0]+gs[i][1]*gs[j][1]+2*gs[i][2]*gs[j][2]);K[a][b]=K[a].get(b,F(0))+v;M[a][b]=M[a].get(b,F(0))+cellvol*F(1+int(i==j),20)
 return [{j:v for j,v in row.items() if v} for row in K],M

def spmv(A,x):return [sum(v*x[j] for j,v in row.items()) for row in A]
def pull(A,P,n):
 out=[{} for _ in range(n)]
 for i,row in enumerate(A):
  for j,v in row.items():
   for a,aa in P[i]:
    for b,bb in P[j]:out[a][b]=out[a].get(b,F(0))+v*aa*bb
 return [{j:v for j,v in row.items() if v} for row in out]
def project(v,w):
 mean=dot(w,v)/2;return [x-mean for x in v]
def decode_state(wit,n=2809):
 assert wit['omega']=='9/2' and wit['gamma']=='1/10' and wit['nodes']==n,'state target mismatch'
 words=[decode(wit[k]) for k in ['hi_real_hex','hi_imag_hex','low_real_hex','low_imag_hex']]
 assert all(len(x)==n for x in words),'state coefficient count'
 return words
def residual(K,M,g,vr,vi,om,ga):
 kr,ki,mr,mi=spmv(K,vr),spmv(K,vi),spmv(M,vr),spmv(M,vi)
 return [a-b+om*om*c+2*ga*om*d for a,b,c,d in zip(g,kr,mr,mi)],[-a+om*om*b-2*ga*om*c for a,b,c in zip(ki,mi,mr)]
def main(folder,generate):
 out=Path(folder);out.mkdir(parents=True,exist_ok=True)
 from center_mesh import mesh
 coarse,coarsets,parent,parentts,coarseP,q,ts,Ps,vols,ref=mesh();n=len(q);h2=max(distance(q,i,j) for tet in ts for i,j in combinations(tet,2));assert h2==F(5,256)
 K,M=assemble_sparse(q,ts,vols);Kp,Mp=assemble_sparse(parent,parentts,F(1,4096));assert pull(K,Ps,len(parent))==Kp and pull(M,Ps,len(parent))==Mp
 g=spmv(M,[10*sum(v[:2]) for v in q]);w=spmv(M,[F(1)]*n);assert sum(g)==0 and sum(w)==2 and not any(sum(row.values()) for row in K);om,ga=F(9,2),F(1,10)
 log('center-enriched geometry, boundary and exact nested sparse forms checked')
 if generate:
  assert not (out/'CENTER_WITNESS.json').exists(),'generation requires unpublished directory'
  import scipy
  from scipy.sparse import coo_matrix
  from scipy.sparse.linalg import splu
  rows=[];cols=[];values=[]
  for i in range(n):
   for j in K[i].keys()|M[i].keys():rows.append(i);cols.append(j);values.append(complex(float(K[i].get(j,F(0))-om*om*M[i].get(j,F(0))),float(2*ga*om*M[i].get(j,F(0)))))
  A=coo_matrix((values,(rows,cols)),shape=(n,n)).tocsc();lu=splu(A);gf=np.array(list(map(float,g)));wf=np.array(list(map(float,w)));hi=lu.solve(gf.astype(np.complex128));hr,hi_=decode(encode(hi.real)),decode(encode(hi.imag));vr,vi=project(hr,w),project(hi_,w);rr,ri=residual(K,M,g,vr,vi,om,ga);assert sum(rr)==sum(ri)==0
  low=lu.solve(np.array([complex(float(a),float(b)) for a,b in zip(rr,ri)]));qf=hi+low;qf-=wf@qf/2;H=gf@qf;J=2*H-qf@(A@qf)
  wit={'omega':str(om),'gamma':str(ga),'nodes':n,'meanfree_projection':'Subtract exact integral divided by2 after decoding the sums of two binary64 words per component.','backend':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'solver':'scipy.sparse.linalg.splu','dtype':'complex128','scope':'Sparse full Neumann matrix at nonzero z; exact residual correction solved once. Actual witness posterior audit, not all-input IEEE guarantee.'},'hi_real_hex':encode(hi.real),'hi_imag_hex':encode(hi.imag),'low_real_hex':encode(low.real),'low_imag_hex':encode(low.imag),'reported_raw_hex':encode([H.real,H.imag]),'reported_corrected_hex':encode([J.real,J.imag])};(out/'CENTER_WITNESS.json').write_text(json.dumps(wit,indent=2)+'\n');log('sparse two-word state proposed')
 else:wit=json.loads((out/'CENTER_WITNESS.json').read_text())
 assert wit['omega']==str(om) and wit['gamma']==str(ga) and wit['nodes']==n;words=decode_state(wit,n);vr,vi=[project([a+b for a,b in zip(words[i],words[i+2])],w) for i in range(2)];assert dot(w,vr)==dot(w,vi)==0
 rr,ri=residual(K,M,g,vr,vi,om,ga);assert sum(rr)==sum(ri)==0;eps2=F(5,4)*sum((a*a+b*b)/wi for a,b,wi in zip(rr,ri,w));beta2=4*ga*ga/(om*om+4*ga*ga);kap=sqrtup(1/beta2)
 lr,li=dot(g,vr),dot(g,vi);kr,ki,mr,mi=spmv(K,vr),spmv(K,vi),spmv(M,vr),spmv(M,vi);ar=dot(vr,kr)-dot(vi,ki)-om*om*(dot(vr,mr)-dot(vi,mi))-4*ga*om*dot(vr,mi);ai=2*dot(vr,ki)-2*om*om*dot(vr,mi)+2*ga*om*(dot(vr,mr)-dot(vi,mi));jr,ji=2*lr-ar,2*li-ai;raw,cor=decode(wit['reported_raw_hex']),decode(wit['reported_corrected_hex']);re=sqrtup((raw[0]-lr)**2+(raw[1]-li)**2);ce=sqrtup((cor[0]-jr)**2+(cor[1]-ji)**2);rawalg=sqrtup(5*eps2/beta2)+re;assert rawalg<=F(1,10**10)
 old=json.loads((out/'FINE_SOLVE_RESULTS.json').read_text());difference=sqrtup((jr-F(old['corrected_output_real']))**2+(ji-F(old['corrected_output_imag']))**2);prior=json.loads((out/'LINEAR_PHASE_RESULTS.json').read_text())['records'][2];pc=decode(prior['selected_reported_center_hex']);inherited=F(prior['selected_reported_radius'])+sqrtup((pc[0]-jr)**2+(pc[1]-ji)**2)+ce
 result={'status':'PASS','classification':'CONDITIONAL_CENTER_ENRICHED_P1_SPARSE_TWO_WORD_STATE','source_witness_sha256':hashlib.sha256((out/'CENTER_WITNESS.json').read_bytes()).hexdigest(),'source_previous_state_sha256':hashlib.sha256((out/'FINE_WITNESS.json').read_bytes()).hexdigest(),'mesh':{'nodes':n,'tetrahedra':len(ts),'max_diameter_squared':str(h2),'stiffness_nonzeros':sum(map(len,K)),'mass_nonzeros':sum(map(len,M)),'exact_nested_stiffness_mass':True,'new_interior_nodes':1024,'exterior_boundary_faces_unchanged':True,'normalized_cell_volumes':['1/4096','1/8192']},'omega':str(om),'gamma':str(ga),'raw_output_real':str(lr),'raw_output_imag':str(li),'corrected_output_real':str(jr),'corrected_output_imag':str(ji),'algebraic_dual_residual_squared_upper':str(eps2),'raw_total_algebraic_output_bound':str(rawalg),'corrected_algebraic_output_bound':str(kap*eps2+ce),'raw_evaluation_bound':str(re),'corrected_evaluation_bound':str(ce),'coarse_fine_corrected_output_difference_upper':str(difference),'difference_scope':'Numerical refinement diagnostic, not a continuum accuracy bound.','inherited_reported_corrected_continuum_radius':str(inherited),'continuum_radius_scope':'Prior valid continuum disk recentered to the new reported corrected output; no own fine flux/dual upper certificate.','precision_target':'1/10','continuum_precision_passed':inherited<=F(1,10),'backend':wit['backend'],'independent_review':False,'physical_promotion':0};target=out/'CENTER_SOLVE_RESULTS.json'
 if target.exists():assert json.loads(target.read_text())==result;log('read-only replay matches CENTER_SOLVE_RESULTS.json')
 else:target.write_text(json.dumps(result,indent=2)+'\n')
 log('raw algebraic bound '+str(float(rawalg))+';corrected output '+str(complex(float(jr),float(ji)))+';coarse-fine difference '+str(float(difference)))
 return coarse,coarsets,parent,parentts,coarseP,q,ts,Ps,vols,ref,K,M,w,vr,vi
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('folder');a.add_argument('--generate',action='store_true');args=a.parse_args();main(args.folder,args.generate)
