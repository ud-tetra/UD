"""Two-word conforming P2 wave state, exact algebraic and paired residual audit."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
REPO=Path(__file__).resolve().parents[2]
RROOT=REPO/'captures/2026-10-19T214921Z-codex-j1-p2-riesz-44ebda6e'
sys.path.insert(0,str(RROOT))
from riesz_lower import *
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
 oldw1=[F(0)]*nv
 for t,mu in zip(ts,vols):
  for node in t:oldw1[node]+=mu/4
 oldwitraw=(SOURCE/'CENTER_WITNESS.json').read_bytes();oldwit=json.loads(oldwitraw);ow=decode_state(oldwit,nv);oldnodal=[project([x+y for x,y in zip(ow[r],ow[r+2])],oldw1) for r in range(2)];oldstates=[v+[(v[i]+v[j])/2 for i,j in edges] for v in oldnodal];assert dot(w,oldstates[0])==dot(w,oldstates[1])==0
 om,ga=F(9,2),F(1,10);a,b=om*om,2*ga*om;beta2=F(4,2029);kappa=sqrtup(1/beta2)
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
 oldrr,oldri=residual(K,M,g,*oldstates,om,ga);oldlowerraw=(RROOT/'RIESZ_RESULTS.json').read_bytes();oldlower=json.loads(oldlowerraw);twit=json.loads((RROOT/'RIESZ_WITNESS.json').read_text());testpayload=(RROOT/'RIESZ_TESTS.bin.gz').read_bytes();assert hashlib.sha256(testpayload).hexdigest()==twit['test_payload_sha256'];tests=decode_payload(testpayload,n);G=[[energy_pair(K,x,y) for y in tests] for x in tests];assert [[str(x) for x in row] for row in G]==oldlower['test_energy_Gram'];Cold=[[dot(r,x) for x in tests] for r in [oldrr,oldri]];assert [[str(x) for x in row] for row in Cold]==oldlower['residual_test_pairings'];Lo,_=lower_from_gram(G,Cold);assert Lo==F(oldlower['dual_norm_squared_lower']);Cnew=[[dot(r,x) for x in tests] for r in [rr,ri]];Lsame,_=lower_from_gram(G,Cnew)
 log('same P2 Riesz tests: prior exact lower reproduced; new squared lower '+str(float(Lsame)))
 # Reuse the old exactly equilibrated flux for a valid upper on the new state.
 upperraw=(COUPLED/'COUPLED_RESULTS.json').read_bytes();up=json.loads(upperraw);assert up['source_state_sha256']==hashlib.sha256(oldwitraw).hexdigest();delta=[[x-y for x,y in zip(v,u)] for v,u in zip(states,oldstates)];Ed=sum(energy_pair(K,d,d) for d in delta);Md=sum(energy_pair(M,d,d) for d in delta);cross=sum(dot(r,d) for r,d in zip([oldrr,oldri],delta));T2=F(up['eta_squared'])+Ed-2*cross;R2=(a*a+b*b)*Md;assert T2>=0 and R2>=0;eta=sqrtup(T2)+sqrtup(R2)/2;U=eta*eta;newradius=kappa*U+cev
 oldsource=json.loads((SOURCE/'CENTER_SOLVE_RESULTS.json').read_text());difference=sqrtup((jr-F(oldsource['corrected_output_real']))**2+(ji-F(oldsource['corrected_output_imag']))**2);oldcenter=decode(up['phase_circle_reported_center_hex']);inherited=F(up['phase_circle_reported_radius'])+sqrtup((oldcenter[0]-cf[0])**2+(oldcenter[1]-cf[1])**2)
 # Independent cell-supported quartic bubbles, beyond the P2 trial space.
 bubble=[F(0),F(0)];projected_residual2=F(0);projected_weighted2=F(0)
 for cell,(ids,gs,Kl,mu) in enumerate(cells):
  EB=sum(gm(x,x) for x in gs)/15120;assert EB>0;lap=[4*gm(gs[i],gs[i]) for i in range(4)]+[8*gm(gs[i],gs[j]) for i,j in EDGES];fb=sum(f[i] for i in ids[:4])/3360
  for index,vs in enumerate([oldstates,states]):
   vals=[[v[i] for i in ids] for v in vs];vb=[-sum(x[:4])/10080+sum(x[4:])/3780 for x in vals];laps=[dot(lap,x) for x in vals]
   if index==0:assert laps==[0,0]
   br=fb+a*vb[0]+b*vb[1]+laps[0]/840;bi=a*vb[1]-b*vb[0]+laps[1]/840;bubble[index]+=mu*(br*br+bi*bi)/EB
  # Exact L2 projection of the P2 state onto broken affine cell values.
  localR=F(0)
  for v in states:
   x=[v[i] for i in ids];bb=mv(tr(Q),x);pc=[20*(y-sum(bb)/5) for y in bb];assert all((pc[i]+sum(pc))/20==bb[i] for i in range(4));localM=quad(Mr,x);projM=(sum(y*y for y in pc)+sum(pc)**2)/20;defect=localM-projM;assert defect>=0;localR+=mu*(a*a+b*b)*defect
  h2=max(distance(q,i,j) for i,j in combinations(ids[:4],2));projected_residual2+=localR;projected_weighted2+=h2*localR/9
  if cell%2048==2047:log('paired quartic bubbles and projected-source budget '+str(cell+1)+'/12288')
 olddiag=json.loads((SOURCE/'CENTER_DIAGNOSTIC_RESULTS.json').read_text());assert bubble[0]==F(olddiag['center_state_local_bubble_squared_lower']);L=max(Lsame,bubble[1]);assert L<=U;delta2=F(2029,16);blocked=delta2*L*L>F(1,100);controls=[];raw=gzip.decompress(payload)
 for name,bad in [('truncated P2 state',gzip.compress(raw[:-8],mtime=0)),('nonfinite P2 state',gzip.compress(struct.pack('<d',float('nan'))+raw[8:],mtime=0))]:
  try:decode_state2(bad,n)
  except (AssertionError,ValueError,OverflowError):controls.append(name)
  else:raise AssertionError(name+' accepted')
 # Signed P2 basis means cannot be used as a positive lumped residual norm.
 assert any(x<0 for x in MEANS);controls.append('signed P2 means rejected as positive lumped norm')
 result={'status':'PASS','classification':'CONDITIONAL_CONFORMING_P2_WAVE_STATE_AND_PAIRED_RESIDUAL_AUDIT','omega':str(om),'gamma':str(ga),'source_old_state_sha256':hashlib.sha256(oldwitraw).hexdigest(),'source_old_dual_results_sha256':hashlib.sha256(oldlowerraw).hexdigest(),'source_upper_results_sha256':hashlib.sha256(upperraw).hexdigest(),'source_witness_sha256':hashlib.sha256((out/'P2_WITNESS.json').read_bytes()).hexdigest(),'mesh':{'nodes_P1':nv,'edges_total':len(edges),'nodes_P2':n,'tetrahedra':len(ts),'stiffness_nonzeros':sum(map(len,K)),'mass_nonzeros':sum(map(len,M)),'all_boundary_nodes_included':True},'mass_lower_alpha':str(alpha),'mass_lower_LDL_pivots':[str(x) for x in pivots],'raw_output':[str(lr),str(li)],'corrected_output':[str(jr),str(ji)],'algebraic_dual_residual_squared_upper':str(eps2),'raw_evaluation_bound':str(rev),'corrected_evaluation_bound':str(cev),'raw_total_algebraic_output_bound':str(rawalg),'corrected_total_algebraic_output_bound':str(coralg),'algebraic_precision_target':'1/10000000000','raw_algebraic_precision_passed':rawalg<=F(1,10**10),'corrected_algebraic_precision_passed':coralg<=F(1,10**10),'prior_same_Riesz_squared_lower':str(Lo),'new_same_Riesz_squared_lower':str(Lsame),'same_Riesz_lower_ratio':str(Lsame/Lo),'prior_local_quartic_bubble_squared_lower':str(bubble[0]),'new_local_quartic_bubble_squared_lower':str(bubble[1]),'new_combined_tested_squared_lower':str(L),'combined_lower_rule':'max of overlapping families, not sum','tested_circle_one_tenth_obstruction':blocked,'state_change_energy_squared':str(Ed),'state_change_mass_squared':str(Md),'state_change_old_residual_real_pairing':str(cross),'transported_old_flux_defect_squared':str(T2),'transported_volume_residual_squared':str(R2),'transported_residual_dual_squared_upper':str(U),'own_transported_corrected_output_radius':str(newradius),'inherited_corrected_output_radius':str(inherited),'selected_reported_corrected_output_radius':str(min(newradius,inherited)),'selected_reported_corrected_output_method':'transported_old_flux' if newradius<=inherited else 'inherited_disk_recentered','continuum_precision_target':'1/10','own_transported_continuum_precision_passed':newradius<=F(1,10),'corrected_output_difference_upper':str(difference),'difference_scope':'Refinement diagnostic, not continuum error','projected_source_volume_residual_squared':str(projected_residual2),'projected_source_cell_Poincare_budget_squared':str(projected_weighted2),'projected_source_scope':'Budget for a future RT1 flux with div tau=z Pi1(v_P2)-F; no such new flux constructed here. Pi1 is exact cell L2 affine projection. diam/pi < diam/3 and meanzero residual permit this local budget.','checks':{'P2_mass_P1_nesting':True,'positive_reference_mass_lower_LDL':True,'exact_source_L2_squared':20,'exact_source_state_residual_meanfree':True,'old_Riesz_Gram_and_pairings_reproduced':True,'old_local_bubble_lower_reproduced':True,'transported_norm_identity_exact':True,'lower_le_transport_upper':True},'controls':controls,'backend':wit['backend'],'scope':'New P2 state. Same-test lower reduction and absence of tested obstruction are not an accuracy upper certificate. Transported flux has nonzero volume residual, bounded with global Poincare1/2; no new equilibrated P2 flux or shifted circle proxy claimed. Externally declared benchmark, not native UD action.','independent_review':False,'physical_promotion':0}
 target=out/'P2_RESULTS.json'
 if target.exists():assert json.loads(target.read_text())==result;log('read-only replay matches P2_RESULTS.json')
 else:target.write_text(json.dumps(result,indent=2)+'\n')
 log('PASS P2 J='+str(complex(float(jr),float(ji)))+' raw algebraic='+str(float(rawalg))+' corrected algebraic='+str(float(coralg))+' same Riesz L='+str(float(Lsame))+' bubble L='+str(float(bubble[1]))+' transport U='+str(float(U))+' output radius='+str(float(newradius))+' tested blocked='+str(blocked)+' projected R budget='+str(float(projected_weighted2)))
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('folder');ap.add_argument('--generate',action='store_true');args=ap.parse_args();main(args.folder,args.generate)
