from pathlib import Path
import numpy as np,json
from common import load,positions
p=Path(__file__).resolve().parent;f=json.loads((p/'FREEZE.json').read_text());rows=[]
for c in f['cases']:
 a,B,nei,b=load(c);x=a['positions_A'];plan=np.load(p/c/'PLAN.npz');radii=plan['radii_A'];norm=np.linalg.norm(b,axis=2);u=b/norm[:,:,None];pairs=[(0,1),(0,2),(1,2)];theta=np.stack([np.sum(u[:,i]*u[:,j],axis=1) for i,j in pairs],axis=1);knots=np.array([-.6666666667,-.5,-.3333333333]);branch0=theta[:,:,None]>=knots;minmargin=np.inf;maximum_error=0.
 for j,w in enumerate(plan['vectors']):
  disp=np.einsum('nam,m->na',B,w);errors=[]
  for h in radii:
   xp=positions(x,disp,h);xm=positions(x,disp,-h);eff=np.asarray((xp.astype(np.longdouble)-xm.astype(np.longdouble))/(2*np.longdouble(h)),dtype=float);errors.append(np.linalg.norm(eff-disp))
  for h in f['steps_A']:
   xp=positions(x,disp,h).astype(np.longdouble);x2p=positions(x,disp,2*h).astype(np.longdouble);xm=positions(x,disp,-h).astype(np.longdouble);x2m=positions(x,disp,-2*h).astype(np.longdouble);xx0=x.astype(np.longdouble)
   for eff in [(-3*xx0+4*xp-x2p)/(2*np.longdouble(h)),(3*xx0-4*xm+x2m)/(2*np.longdouble(h))]:errors.append(float(np.linalg.norm(np.asarray(eff,dtype=float)-disp)))
  assert np.array_equal(errors,plan['input_errors'][j]);maximum_error=max(maximum_error,max(errors));ok=True;cross=np.zeros(theta.shape,bool)
  for t in np.linspace(-1,1,17):
   xx=positions(x,disp,t*radii[0]);bb=b+(xx-x)[nei]-(xx-x)[:,None,:];lens=np.linalg.norm(bb,axis=2);assert lens.max()<1.7;uu=bb/lens[:,:,None];th=np.stack([np.sum(uu[:,i]*uu[:,j],axis=1) for i,j in pairs],axis=1);changed=(th[:,:,None]>=knots)!=branch0;ok=bool(ok and not np.any(changed[:,:,[0,2]]));cross|=changed[:,:,1]
  assert ok==plan['branch_safe'][j];assert int(cross.sum())==plan['crossed_triples_count'][j]
  # Conservative analytic displacement inequality, evaluated in floating point,
  # independently checks separation from the two other angular knots.
  db=(disp[nei]-disp[:,None,:])*radii[0];dn=np.linalg.norm(db,axis=2)
  for k,(i,l) in enumerate(pairs):
   bound=2*dn[:,i]/(norm[:,i]-dn[:,i])+2*dn[:,l]/(norm[:,l]-dn[:,l]);margin=np.min(abs(theta[:,k,None]-knots[[0,2]])-bound[:,None]);minmargin=min(minmargin,float(margin))
 assert maximum_error<=1e-6 and minmargin>0
 rows.append(dict(case=c,plans_recomputed=True,max_input_error=maximum_error,other_knot_margin_after_displacement_bound=minmargin))
(p/'GEOMETRY_VERIFICATION.json').write_text(json.dumps(dict(status='PASS_CONSTRUCTOR',cases=rows,scope='All rounded samples and input errors reproduced; supplementary analytic cosine displacement inequality evaluated in floating point, not directed-rounding interval certification.'),indent=2)+'\n');print(rows)
