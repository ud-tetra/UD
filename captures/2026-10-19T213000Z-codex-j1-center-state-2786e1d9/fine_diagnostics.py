"""Paired coarse-cell bubble tests for old/new states plus new-mesh residual lower bound."""
import sys
sys.dont_write_bytecode=True
from fine_solve import *

def moment(ex):return F(6*__import__('math').prod(factorial(x) for x in ex),factorial(sum(ex)+3))
def multiply(p,q):
 out={}
 for a,x in p.items():
  for b,y in q.items():
   e=tuple(i+j for i,j in zip(a,b));out[e]=out.get(e,F(0))+x*y
 return {e:x for e,x in out.items() if x}
def integr(p):return sum(x*moment(e) for e,x in p.items())
def reference_moments():
 ans=[]
 for weights,perm in pattern():
  polys=[]
  for i in range(4):polys.append({tuple(int(j==a) for j in range(4)):weights[a][i] for a in range(4) if weights[a][i]})
  b={(0,0,0,0):F(1)}
  for f in polys:b=multiply(b,f)
  L=[integr(multiply(b,{tuple(int(j==a) for j in range(4)):F(1)})) for a in range(4)];G=[]
  for i in range(4):
   d={(0,0,0,0):F(1)}
   for j,f in enumerate(polys):
    if i!=j:d=multiply(d,f)
   G.append(integr(d))
  ans.append((weights,L,G))
 assert sum(sum(L)/8 for weights,L,G in ans)==F(1,840)
 for i in range(4):assert sum(sum(weights[a][i]*L[a] for a in range(4))/8 for weights,L,G in ans)==F(1,3360)
 for i in range(4):assert sum(G[i]/8 for weights,L,G in ans)==F(1,120)
 return ans

def old_state(folder,p,t):
 wit=json.loads((folder/'STATE_WITNESS.json').read_text());f=wit['fixtures'][2];assert f['omega']=='9/2' and f['gamma']=='1/10';_,M=assemble_sparse(p,t,F(1,512));w=spmv(M,[F(1)]*len(p));pivot=wit['pivot'];idx=[i for i in range(len(p)) if i!=pivot];rat=[w[i]/w[pivot] for i in idx];words=[decode(f[k]) for k in ['hi_real_hex','hi_imag_hex','low_real_hex','low_imag_hex']];return [lift([a+b for a,b in zip(words[i],words[i+2])],idx,pivot,rat,len(p)) for i in range(2)]

def main(folder):
 out=Path(folder);p,t,q,ts,P,K,M,w,vr,vi=__import__('fine_solve').main(folder,False);old=old_state(out,p,t);oldfine=[[sum(c*v[j] for j,c in row) for row in P] for v in old];reference=reference_moments();assert all(dot(w,x)==0 for x in oldfine);bounds=[];oldlocal=[]
 for values in [oldfine,[vr,vi]]:
  lower=F(0);localres=[]
  for cell,parent in enumerate(t):
   gp=grads(p,parent);energy=F(1,512*15120)*sum(g[0]**2+g[1]**2+2*g[2]**2 for g in gp);r=[F(0),F(0)]
   for child,(weights,L,G) in zip(ts[8*cell:8*cell+8],reference):
    gc=grads(q,child);bgrad=[sum(gp[i][axis]*G[i] for i in range(4)) for axis in range(3)];vg=[[sum(v[j]*gc[a][axis] for a,j in enumerate(child)) for axis in range(3)] for v in values]
    rr=[10*sum(q[j][:2])+F(81,4)*values[0][j]+F(9,10)*values[1][j] for j in child];ri=[F(81,4)*values[1][j]-F(9,10)*values[0][j] for j in child]
    for c,R in enumerate([rr,ri]):r[c]+=F(1,4096)*(dot(R,L)-(vg[c][0]*bgrad[0]+vg[c][1]*bgrad[1]+2*vg[c][2]*bgrad[2]))
   lower+=(r[0]*r[0]+r[1]*r[1])/energy;localres.append(r)
  bounds.append(lower)
  if len(bounds)==1:oldlocal=localres
 oldresult=json.loads((out/'BUBBLE_FLOOR_RESULTS.json').read_text())['records'][2];assert bounds[0]==F(oldresult['dual_residual_squared_lower']),'old coarse-bubble quadrature replay mismatch'
 lowerfine=F(0)
 for tet in ts:
  gs=grads(q,tet);energy=F(1,4096*15120)*sum(g[0]**2+g[1]**2+2*g[2]**2 for g in gs);rr=F(1,4096*3360)*sum(10*sum(q[j][:2])+F(81,4)*vr[j]+F(9,10)*vi[j] for j in tet);ri=F(1,4096*3360)*sum(F(81,4)*vi[j]-F(9,10)*vr[j] for j in tet);lowerfine+=(rr*rr+ri*ri)/energy
 delta2=F(2029,16);assert delta2==F(1,4)*(1+F(81,4)/F(1,25));combined=max(bounds[1],lowerfine)
 result={'status':'PASS','source_fine_witness_sha256':hashlib.sha256((out/'FINE_WITNESS.json').read_bytes()).hexdigest(),'source_old_witness_sha256':hashlib.sha256((out/'STATE_WITNESS.json').read_bytes()).hexdigest(),'omega':'9/2','gamma':'1/10','reference_partition_moment_checks':9,'coarse_bubble_cells':len(t),'fine_bubble_cells':len(ts),'old_state_same_coarse_bubble_squared_lower':str(bounds[0]),'new_state_same_coarse_bubble_squared_lower':str(bounds[1]),'paired_squared_lower_ratio':str(bounds[1]/bounds[0]),'old_source_bubble_value_reproduced':True,'new_state_fine_bubble_squared_lower':str(lowerfine),'strongest_available_squared_lower':str(combined),'phase_circle_factor_squared':str(delta2),'old_same_test_circle_obstruction':delta2*bounds[0]**2>F(1,100),'new_same_test_circle_obstruction':delta2*bounds[1]**2>F(1,100),'new_fine_test_circle_obstruction':delta2*lowerfine**2>F(1,100),'scope':'Paired lower bounds use the SAME1024 coarse bubbles. A decreased lower bound is a diagnostic, not an upper error certificate or a proof that the full residual norm decreased. Fine-bubble bound uses8192 cells separately; do not add the overlapping-family bounds. No own fine flux/dual upper certificate.','independent_review':False,'physical_promotion':0};target=out/'FINE_DIAGNOSTIC_RESULTS.json'
 if target.exists():assert json.loads(target.read_text())==result;log('read-only replay matches FINE_DIAGNOSTIC_RESULTS.json')
 else:target.write_text(json.dumps(result,indent=2)+'\n')
 log('same coarse test:old '+str(float(bounds[0]))+';new '+str(float(bounds[1]))+';fine test '+str(float(lowerfine))+';new obstruction '+str(result['new_same_test_circle_obstruction']))
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('folder');main(a.parse_args().folder)
