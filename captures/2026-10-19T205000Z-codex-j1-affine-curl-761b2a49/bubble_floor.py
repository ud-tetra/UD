"""Exact continuum residual-dual lower bound from disjoint cell bubbles."""
import sys
sys.dont_write_bytecode=True
from curl_interface import *
from red_mesh import edgewise
from level2_check import lift,sparse,spmv
from linear_circle import params

def main(folder):
 p=Path(folder);state=json.loads((p/'STATE_WITNESS.json').read_text());a,t,_=refine(points,tets);a,t,_=edgewise(a,t);q,ts,_=edgewise(a,t);n=len(q);K,M=assemble(q,ts,[F(1,512)]*len(ts));w=spmv(sparse(M),[F(1)]*n);pivot=state['pivot'];idx=[i for i in range(n) if i!=pivot];rat=[w[i]/w[pivot] for i in idx];records=[];energy_checks=0
 moment=lambda e:F(6*__import__('math').prod(factorial(x) for x in e),factorial(sum(e)+3))
 assert moment([1,1,1,1])==F(1,840)
 assert all(moment([1+int(i==j) for i in range(4)])==F(1,3360) for j in range(4))
 for fixture in state['fixtures']:
  om,ga=F(fixture['omega']),F(fixture['gamma']);words=[decode(fixture[k]) for k in ['hi_real_hex','hi_imag_hex','low_real_hex','low_imag_hex']];v=[lift([x+y for x,y in zip(words[i],words[i+2])],idx,pivot,rat,n) for i in range(2)];assert dot(w,v[0])==dot(w,v[1])==0;lower=F(0)
  for tet in ts:
   gs=grads(q,tet);C=sum(g[0]**2+g[1]**2+2*g[2]**2 for g in gs);energy=F(1,512*15120)*C;assert energy>0
   if not records:
    direct=F(0)
    for i in range(4):
     for j in range(4):
      direct+=moment([int(k!=i)+int(k!=j) for k in range(4)])*(gs[i][0]*gs[j][0]+gs[i][1]*gs[j][1]+2*gs[i][2]*gs[j][2])/512
    assert direct==energy;energy_checks+=1
   rr=F(1,512*3360)*sum(10*sum(q[i][:2])+om*om*v[0][i]+2*ga*om*v[1][i] for i in tet);ri=F(1,512*3360)*sum(om*om*v[1][i]-2*ga*om*v[0][i] for i in tet);lower+=(rr*rr+ri*ri)/energy
  _,delta2=params(om,ga);current=json.loads((p/'LINEAR_COVARIANCE_RESULTS.json').read_text())['records'][len(records)];assert F(current['eta_squared'])>=lower>=0;records.append({'omega':str(om),'gamma':str(ga),'dual_residual_squared_lower':str(lower),'phase_circle_flux_only_obstruction':delta2*lower*lower>F(1,100)})
 result={'status':'PASS','source_state_sha256':hashlib.sha256((p/'STATE_WITNESS.json').read_bytes()).hexdigest(),'bubble':'product of four barycentric coordinates; each test mean-subtracted globally','cells':len(ts),'direct_bubble_energy_checks':energy_checks,'barycentric_moment_identities':5,'records':records,'scope':'Lower bound on continuum residual V-dual norm squared for the fixed frozen P1 state, using energy-orthogonal disjoint cell bubbles. It lower-bounds every admissible flux estimator eta², not actual output error. Circle obstruction excludes flux-only1/10 certification at listed points, not other certificates or a changed state.','independent_review':False,'physical_promotion':0}
 target=p/'BUBBLE_FLOOR_RESULTS.json'
 if target.exists():assert json.loads(target.read_text())==result;print('read-only replay matches BUBBLE_FLOOR_RESULTS.json')
 else:target.write_text(json.dumps(result,indent=2)+'\n')
 for r in records:print('omega',r['omega'],'dual squared lower',float(F(r['dual_residual_squared_lower'])),'flux-only circle obstruction',r['phase_circle_flux_only_obstruction'])
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('folder');main(a.parse_args().folder)
