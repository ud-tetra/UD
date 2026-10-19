"""Exact audited fixed-port solve and hierarchical RT1 on h-reducing edgewise mesh."""
import sys
sys.dont_write_bytecode=True
from patch_flux import *
from red_mesh import edgewise,family_certificate
def main(out,generate):
 out=Path(out);out.mkdir(parents=True,exist_ok=True)
 parent,pts,P0=refine(points,tets);q,ts,P=edgewise(parent,pts)
 n=len(q)
 for tet in ts:
  d=[subvec(q[i],q[tet[0]]) for i in tet[1:]]
  assert abs(dot(d[0],cross(d[1],d[2])))==F(1,64),'child volume'
 cert=family_certificate()
 K,M=assemble(q,ts,[F(1,64)]*len(ts));Kp,Mp=assemble(parent,pts,[F(1,8)]*len(pts))
 assert mm(tr(P),mm(K,P))==Kp and mm(tr(P),mm(M,P))==Mp
 g=mv(M,[10*sum(x[:2]) for x in q]);gp=mv(Mp,[10*sum(x[:2]) for x in parent]);assert mv(tr(P),g)==gp
 w=mv(M,[F(1)]*n);Z=[[F(i==j)-F(i==0)*w[j]/w[0] for j in range(1,n)] for i in range(n)]
 Kr=mm(tr(Z),mm(K,Z));Mr=mm(tr(Z),mm(M,Z));gr=mv(tr(Z),g);Kri=inv(Kr)
 specs=[(F(0),F(1,10)),(F(4),F(1,10)),(F(9,2),F(1,10)),(F(5),F(1,10))]
 if generate:
  assert np is not None
  witness={'backend':{'python':platform.python_version(),'numpy':np.__version__,'dtype':'complex128','solver':'numpy.linalg.solve','target_arithmetic':'Fraction; exact rational gamma=1/10','representation':'Exact hex decoding of state, parent free flux and patch free flux proposals; exact reconstruction imposes constraints.'},'fixtures':[]}
  for om,ga in specs:
   ar=farray(add(Kr,Mr,-om*om))+1j*float(2*ga*om)*farray(Mr);xf=np.linalg.solve(ar,np.array(list(map(float,gr)),dtype=np.complex128))
   qfloat=farray(Z)@xf;gf=np.array(list(map(float,g)));fullA=farray(add(K,M,-om*om))+1j*float(2*ga*om)*farray(M);hout=gf@qfloat;jout=2*hout-qfloat@(fullA@qfloat)
   witness['fixtures'].append({'omega':str(om),'gamma':str(ga),'x_real_hex':encode(xf.real),'x_imag_hex':encode(xf.imag),'reported_raw_hex':encode([hout.real,hout.imag]),'reported_corrected_hex':encode([jout.real,jout.imag]),'patch_free':[]})
 else:witness=json.loads((out/'WITNESS.json').read_text())
 states=[];projections=[]
 assert len(witness['fixtures'])==len(specs)
 for f,(om,ga) in zip(witness['fixtures'],specs):
  assert f['omega']==str(om) and f['gamma']==str(ga)
  xr,xi=decode(f['x_real_hex']),decode(f['x_imag_hex']);assert len(xr)==len(xi)==n-1
  vr,vi=mv(Z,xr),mv(Z,xi);states.append((vr,vi,xr,xi))
 # Exact cellwise L2 projection of each fine P1 field onto parent P1.
 for vr,vi,xr,xi in states:
  projected=[]
  for v in (vr,vi):
   cells=[]
   for k,t in enumerate(pts):
    moments=[F(0)]*4
    for child in ts[8*k:8*k+8]:
     for i,parentvi in enumerate(t):
      for j,a in enumerate(child):
       for l,b in enumerate(child):moments[i]+=F(1+int(j==l),1280)*P[a][parentvi]*v[b]
    coeff=[160*(m-sum(moments)/5) for m in moments]
    # M_parent=V/20*(I+11^T), inverse=20/V*(I-11^T/5).
    assert all(F(1,160)*(coeff[i]+sum(coeff))==moments[i] for i in range(4))
    cells.append(coeff)
   projected.append(cells)
  projections.append(projected)
 log('55-node/128-cell exact matrices, source and cellwise L2 projections checked')
 vals=[]
 for k,t in enumerate(pts):
  cell=[]
  for vi in t:
   row=[]
   for f,((om,ga),(vr,vi_,xr,xi)) in enumerate(zip(specs,states)):
    local=t.index(vi);pr,pi=projections[f][0][k][local],projections[f][1][k][local]
    row.extend([-om*om*pr-2*ga*om*pi-10*sum(parent[vi][:2]),-om*om*pi+2*ga*om*pr])
   cell.append(row)
  vals.append(cell)
 A,rhs=constraints(parent,pts,vals);parts,N,free=rref_many(A,rhs);G=blockmatrix(gramblocks(parent,pts,[F(1,8)]*len(pts)))
 if generate:
  proposals=minimize(N,G,parts)
  for k,f in enumerate(witness['fixtures']):f['free_real_hex']=encode(proposals[:,2*k]);f['free_imag_hex']=encode(proposals[:,2*k+1])
 parentflux=[]
 for k,f in enumerate(witness['fixtures']):parentflux.append([reconstruct(parts[2*k+j],N,f['free_real_hex' if j==0 else 'free_imag_hex']) for j in range(2)])
 blocks=gramblocks(q,ts,[F(1,64)]*len(ts));flux=[[[F(0)]*(15*len(ts)) for _ in range(2)] for f in specs];patchdata=[]
 for k,t in enumerate(pts):
  child=ts[8*k:8*k+8];vv=[]
  for tet in child:
   cell=[]
   for vi in tet:
    row=[]
    for f,((om,ga),(vr,vi_,xr,xi)) in enumerate(zip(specs,states)):
     dr=vr[vi]-sum(P[vi][pv]*projections[f][0][k][l] for l,pv in enumerate(t));di=vi_[vi]-sum(P[vi][pv]*projections[f][1][k][l] for l,pv in enumerate(t))
     row.extend([-om*om*dr-2*ga*om*di,-om*om*di+2*ga*om*dr])
    cell.append(row)
   vv.append(cell)
  Ap,bp=constraints(q,child,vv);ps,Np,fp=rref_many(Ap,bp);Gp=blockmatrix(blocks[8*k:8*k+8]);patchdata.append((Ap,bp,Np,fp))
  pp=[]
  for f in range(len(specs)):
   for j in range(2):pp.append([a+b for a,b in zip(parentflux[f][j][15*k:15*k+15]*8,ps[2*f+j])])
  if generate:
   proposals=minimize(Np,Gp,pp)
   for f in range(len(specs)):witness['fixtures'][f]['patch_free'].append({'real_hex':encode(proposals[:,2*f]),'imag_hex':encode(proposals[:,2*f+1])})
  for f,wit in enumerate(witness['fixtures']):
   for j in range(2):flux[f][j][120*k:120*k+120]=reconstruct(pp[2*f+j],Np,wit['patch_free'][k]['real_hex' if j==0 else 'imag_hex'])
  log('local eight-child patch '+str(k+1)+'/16 rank '+str(120-len(fp)))
 if generate:(out/'WITNESS.json').write_text(json.dumps(witness,indent=2)+'\n')
 # Audit final assembled flux directly, independently of the hierarchical constraint construction.
 vals=[]
 for t in ts:
  cell=[]
  for vi in t:
   row=[]
   for (om,ga),(vr,vi_,xr,xi) in zip(specs,states):row.extend([-om*om*vr[vi]-2*ga*om*vi_[vi]-10*sum(q[vi][:2]),-om*om*vi_[vi]+2*ga*om*vr[vi]])
   cell.append(row)
  vals.append(cell)
 Af,bf=constraints(q,ts,vals);checks=[];records=[]
 def check(name,cond):
  assert cond,name
  checks.append(name)
 check('55 vertices and128 tetrahedra',n==55 and len(ts)==128)
 check('exact nested stiffness mass and source',mm(tr(P),mm(K,P))==Kp and mm(tr(P),mm(M,P))==Mp and mv(tr(P),g)==gp)
 check('source zero mean',sum(g)==0)
 check('exact child determinant volumes and local affine L2 projection',True)
 for k,(f,(om,ga),(vr,vi,xr,xi)) in enumerate(zip(witness['fixtures'],specs,states)):
  jr,ji=flux[k]
  for r,(row,b) in enumerate(zip(Af,bf)):
   sparse=[(j,v) for j,v in enumerate(row) if v]
   check('assembled real flux constraint '+str((k,r)),sum(v*jr[j] for j,v in sparse)==b[2*k])
   check('assembled imag flux constraint '+str((k,r)),sum(v*ji[j] for j,v in sparse)==b[2*k+1])
  check('exact meanfree '+str(k),dot(w,vr)==dot(w,vi)==0)
  def fluxquad(x):return sum(quad(b,x[15*i:15*i+15]) for i,b in enumerate(blocks))
  mass=quad(M,vr)+quad(M,vi);stiff=quad(K,vr)+quad(K,vi);lr,li=dot(g,vr),dot(g,vi)
  eta2=fluxquad(jr)+fluxquad(ji)-2*lr-2*om*om*mass+stiff
  check('nonnegative flux norm '+str(k),eta2>=0)
  a=add(Kr,Mr,-om*om);b=[[2*ga*om*x for x in row] for row in Mr]
  rhoR=[x-y+z for x,y,z in zip(gr,mv(a,xr),mv(b,xi))];rhoI=[-x-y for x,y in zip(mv(a,xi),mv(b,xr))]
  eps2=quad(Kri,rhoR)+quad(Kri,rhoI);beta2=max(4*ga*ga/(om*om+4*ga*ga),max(F(0),1-om*om/4)**2);B=1+(om*om+2*ga*om)/4
  algout2=5*eps2/beta2;budget=F(1,10**10)
  check('raw algebraic budget '+str(k),algout2<=budget*budget)
  kR=quad(K,vr)-quad(K,vi);kI=2*dot(vr,mv(K,vi));mR=quad(M,vr)-quad(M,vi);mI=2*dot(vr,mv(M,vi))
  azR=kR-om*om*mR-2*ga*om*mI;azI=kI-om*om*mI+2*ga*om*mR
  corrR,corrI=2*lr-azR,2*li-azI;rbR,rbI=lr-azR,li-azI
  def sqrtup(x,digits=18):
   from math import isqrt
   scale=10**digits;v=isqrt(x.numerator*scale*scale//x.denominator)
   if F(v*v,scale*scale)<x:v+=1
   return F(v,scale)
  residual_correction=sqrtup(rbR*rbR+rbI*rbI)
  kap2=(om*om+4*ga*ga)/(4*ga*ga) if om*om+4*ga*ga>=4 else 16/((4-om*om)**2+4*ga*ga*om*om)
  kap=sqrtup(kap2);check('outward spectral factor '+str(k),kap*kap>=kap2)
  cont=kap*eta2;oldcont=B*eta2/beta2
  check('spectral factor no worse than prior bound '+str(k),kap<=B/beta2)
  raw_report=decode(f['reported_raw_hex']);corr_report=decode(f['reported_corrected_hex']);raw_eval=sqrtup((raw_report[0]-lr)**2+(raw_report[1]-li)**2);corr_eval=sqrtup((corr_report[0]-corrR)**2+(corr_report[1]-corrI)**2)
  total_alg=sqrtup(algout2)+raw_eval;check('end to end raw algebraic budget '+str(k),total_alg<=budget)
  static_bracket=None
  if om==0:
   scale=10**6;lo=F((corrR*scale).numerator//(corrR*scale).denominator,scale);bound=corrR+cont;hi=F(-((-bound*scale).numerator//(-bound*scale).denominator),scale)
   check('static outward bracket',lo<=corrR and hi>=bound and corrI==0);static_bracket={'lower':str(lo),'upper':str(hi)}
  records.append({'omega':str(om),'gamma':str(ga),'static_continuum_bracket':static_bracket,'raw_output_real':str(lr),'raw_output_imag':str(li),'corrected_output_real':str(corrR),'corrected_output_imag':str(corrI),'flux_estimator_squared':str(eta2),'spectral_factor_squared':str(kap2),'spectral_factor_upper':str(kap),'corrected_continuum_error_bound':str(cont),'prior_factor_same_flux_bound':str(oldcont),'reported_corrected_continuum_error_bound':str(cont+corr_eval),'raw_continuum_error_bound':str(cont+residual_correction+raw_eval),'raw_algebraic_dual_residual_squared':str(eps2),'reported_raw_total_algebraic_error_bound':str(total_alg),'reported_raw_evaluation_error_bound':str(raw_eval),'reported_corrected_evaluation_error_bound':str(corr_eval),'raw_algebraic_budget':str(budget)})
  log('omega='+str(om)+' eta2~'+str(float(eta2))+' corrected continuum bound~'+str(float(cont)))
 result={'status':'PASS','classification':'CONDITIONAL_H_REDUCING_EDGEWISE_MESH_AND_LOCAL_RT1','check_count':len(checks),'checks':[c for c in checks if not c.startswith('assembled ')],'mesh':{'vertices':n,'tetrahedra':len(ts),'parent_max_diameter_squared':str(max(distance(parent,i,j) for tet in pts for i,j in combinations(tet,2))),'child_max_diameter_squared':str(max(distance(q,i,j) for tet in ts for i,j in combinations(tet,2))),'parent_constraint_equations':len(A),'parent_constraint_rank':240-len(free),'parent_free':len(free),'patches':len(pts),'patch_constraint_equations':len(patchdata[0][0]),'patch_constraint_rank':120-len(patchdata[0][3]),'patch_free':len(patchdata[0][3]),'assembled_constraint_equations':len(Af),'scalar_flux_checks':len(Af)*2*len(specs)},'family_certificate':cert,'records':records,'backend':witness['backend'],'independent_review':False,'physical_promotion':0}
 if not generate and (out/'RESULTS.json').exists():assert json.loads((out/'RESULTS.json').read_text())==result;log('read-only exact replay matches RESULTS.json')
 else:(out/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
 log('PASS '+str(len(checks))+' checks')
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('output');a.add_argument('--generate',action='store_true');args=a.parse_args();main(args.output,args.generate)
