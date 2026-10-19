"""Three-state audit on unchanged coarse bubbles after adding interior-center P1 nodes."""
import sys
sys.dont_write_bytecode=True
from center_solve import *
from fine_diagnostics import moment,multiply,integr,old_state

def reference_moments(ref):
 ans=[]
 for weights,ratio in ref:
  polys=[{tuple(int(j==a) for j in range(4)):weights[a][i] for a in range(4) if weights[a][i]} for i in range(4)];b={(0,0,0,0):F(1)}
  for f in polys:b=multiply(b,f)
  L=[integr(multiply(b,{tuple(int(j==a) for j in range(4)):F(1)})) for a in range(4)];G=[]
  for i in range(4):
   d={(0,0,0,0):F(1)}
   for j,f in enumerate(polys):
    if i!=j:d=multiply(d,f)
   G.append(integr(d))
  ans.append((weights,ratio,L,G))
 assert sum(ratio*sum(L) for weights,ratio,L,G in ans)==F(1,840)
 for i in range(4):
  assert sum(ratio*sum(weights[a][i]*L[a] for a in range(4)) for weights,ratio,L,G in ans)==F(1,3360)
  assert sum(ratio*G[i] for weights,ratio,L,G in ans)==F(1,120)
 assert any(__import__('math').prod(v)>0 for weights,ratio,L,G in ans for v in weights)
 return ans

def main(folder):
 out=Path(folder);coarse,t,parent,parentts,coarseP,q,ts,P,vols,ref,K,M,w,vr,vi=__import__('center_solve').main(folder,False);n0=len(parent);wp=[F(0)]*n0
 for wi,row in zip(w,P):
  for j,c in row:wp[j]+=wi*c
 fw=json.loads((out/'FINE_WITNESS.json').read_text());assert fw['nodes']==n0 and fw['omega']=='9/2' and fw['gamma']=='1/10';words=[decode(fw[k]) for k in ['hi_real_hex','hi_imag_hex','low_real_hex','low_imag_hex']];assert all(len(x)==n0 for x in words);uniform=[project([a+b for a,b in zip(words[i],words[i+2])],wp) for i in range(2)]
 original=old_state(out,coarse,t);original_parent=[[sum(c*v[j] for j,c in row) for row in coarseP] for v in original]
 def prolong(values):return [[sum(c*v[j] for j,c in row) for row in P] for v in values]
 states=[prolong(original_parent),prolong(uniform),[vr,vi]];assert all(dot(w,v)==0 for values in states for v in values);reference=reference_moments(ref);bounds=[]
 for values in states:
  lower=F(0)
  for cell,tet in enumerate(t):
   gp=grads(coarse,tet);energy=F(1,512*15120)*sum(g[0]**2+g[1]**2+2*g[2]**2 for g in gp);r=[F(0),F(0)]
   for k,(child,(weights,ratio,L,G)) in enumerate(zip(ts[12*cell:12*cell+12],reference)):
    mu=vols[12*cell+k];assert mu==ratio/512;gc=grads(q,child);bgrad=[sum(gp[i][axis]*G[i] for i in range(4)) for axis in range(3)];vg=[[sum(v[j]*gc[a][axis] for a,j in enumerate(child)) for axis in range(3)] for v in values]
    rr=[10*sum(q[j][:2])+F(81,4)*values[0][j]+F(9,10)*values[1][j] for j in child];ri=[F(81,4)*values[1][j]-F(9,10)*values[0][j] for j in child]
    for c,R in enumerate([rr,ri]):r[c]+=mu*(dot(R,L)-(vg[c][0]*bgrad[0]+vg[c][1]*bgrad[1]+2*vg[c][2]*bgrad[2]))
   lower+=(r[0]*r[0]+r[1]*r[1])/energy
  bounds.append(lower);log('coarse bubble audit state'+str(len(bounds))+'/3 lower '+str(float(lower)))
 previous=json.loads((out/'FINE_DIAGNOSTIC_RESULTS.json').read_text());assert bounds[0]==F(previous['old_state_same_coarse_bubble_squared_lower']);assert bounds[1]==F(previous['new_state_same_coarse_bubble_squared_lower']);local=F(0)
 for tet,mu in zip(ts,vols):
  gs=grads(q,tet);energy=mu/F(15120)*sum(g[0]**2+g[1]**2+2*g[2]**2 for g in gs);rr=mu/F(3360)*sum(10*sum(q[j][:2])+F(81,4)*vr[j]+F(9,10)*vi[j] for j in tet);ri=mu/F(3360)*sum(F(81,4)*vi[j]-F(9,10)*vr[j] for j in tet);local+=(rr*rr+ri*ri)/energy
 g=spmv(M,[10*sum(v[:2]) for v in q]);added=[]
 for values in [states[1],states[2]]:
  rr,ri=residual(K,M,g,*values,F(9,2),F(1,10));assert sum(rr)==sum(ri)==0;added.append(sum((rr[i]**2+ri[i]**2)/K[i][i] for i in range(n0,len(q))))
 d2=F(2029,16);combined=max(bounds[2],local,added[1]);result={'status':'PASS','source_center_witness_sha256':hashlib.sha256((out/'CENTER_WITNESS.json').read_bytes()).hexdigest(),'source_uniform_witness_sha256':hashlib.sha256((out/'FINE_WITNESS.json').read_bytes()).hexdigest(),'omega':'9/2','gamma':'1/10','reference_partition_moment_checks':9,'old1024_and_uniform8192_source_bounds_reproduced':True,'coarse_bubble_cells':len(t),'new_local_bubble_cells':len(ts),'interior_centers_added':len(q)-n0,'coarse_bubble_interpolant_now_nonzero':True,'original_state_same_coarse_squared_lower':str(bounds[0]),'uniform_state_same_coarse_squared_lower':str(bounds[1]),'center_state_same_coarse_squared_lower':str(bounds[2]),'center_to_uniform_same_test_ratio':str(bounds[2]/bounds[1]),'center_state_local_bubble_squared_lower':str(local),'uniform_state_added_center_test_squared_lower':str(added[0]),'center_state_added_center_test_squared_lower':str(added[1]),'strongest_available_center_squared_lower':str(combined),'phase_circle_factor_squared':str(d2),'uniform_same_test_circle_obstruction':d2*bounds[1]**2>F(1,100),'center_same_test_circle_obstruction':d2*bounds[2]**2>F(1,100),'center_local_test_circle_obstruction':d2*local**2>F(1,100),'center_strongest_test_circle_obstruction':d2*combined**2>F(1,100),'scope':'All three states use the SAME1024 coarse bubbles. Lower-bound reductions do not prove full residual/error reduction. Absence of this obstruction is not an upper certificate or precision pass. Overlapping test-family bounds combined by max only. No own center-mesh continuum flux/dual upper certificate.','independent_review':False,'physical_promotion':0};target=out/'CENTER_DIAGNOSTIC_RESULTS.json'
 if target.exists():assert json.loads(target.read_text())==result;log('read-only replay matches CENTER_DIAGNOSTIC_RESULTS.json')
 else:target.write_text(json.dumps(result,indent=2)+'\n')
 log('local bubble lower '+str(float(local))+';center coarse obstruction '+str(result['center_same_test_circle_obstruction'])+';strongest obstruction '+str(result['center_strongest_test_circle_obstruction']))
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('folder');main(a.parse_args().folder)
