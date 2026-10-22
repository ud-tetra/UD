from pathlib import Path
import numpy as np,json,hashlib,itertools
root=Path(__file__).resolve().parent;base=root.parent
cases=['21_dir_0','21_dir_10024','31_dir_10084','31_dir_10134']
def dump(p,o):p.write_text(json.dumps(o,indent=2)+'\n')
def read(name,c):
 p=base/'graphite-hessian'/name if c==16 else base/'graphite-cutoff'/name/f'cutoff_{c}'
 a=np.load(p/'MATRICES.npz');return a,p

def shell(a,name,c):
 x=a['equilibrium_positions_A'];t=a['atom_types'];lo=np.where(t==1)[0];up=np.where(t==2)[0]
 pat,di=name.split('_',1);lines=(base/'graphite-target-replay'/'selected'/pat/di/'struct.inp.data').read_text().splitlines()
 lx=float(next(l for l in lines if 'xlo xhi' in l).split()[1]);ly=float(next(l for l in lines if 'ylo yhi' in l).split()[1]);xy=float(next(l for l in lines if 'xy xz yz' in l).split()[0]);L=np.array([[lx,xy],[0,ly]]);inv=np.linalg.inv(L)
 frac=x[:,:2]@inv.T;extent=np.ptp(frac,axis=0);bound=np.ceil(extent+(c+.005)*np.linalg.norm(inv,axis=1)).astype(int)
 ids=[];vec=[];ims=[]
 for b1,b2 in itertools.product(range(-bound[0],bound[0]+1),range(-bound[1],bound[1]+1)):
  r=x[up][None,:,:]-x[lo][:,None,:];r[:,:,:2]+=L@np.array([b1,b2]);rad=np.linalg.norm(r,axis=2);ii,jj=np.where(abs(rad-c)<.005)
  if len(ii):ids.append(np.stack([lo[ii],up[jj]],1));vec.append(r[ii,jj]);ims.append(np.tile([b1,b2],(len(ii),1)))
 return np.concatenate(ids),np.concatenate(vec),np.concatenate(ims),bound.tolist()

def pair(r,c):
 rs=(r*r).sum(1);rr=np.sqrt(rs);rho=(r[:,:2]**2).sum(1)/.578**2;e=np.exp(-3.629*(rr-3.34));f=np.exp(-rho)*(.01571+.01229*rho+.004933*rho*rho);C=.003030+2*f
 v=-.010238*(3.34/rr)**6+e*C+.010238*(3.34/c)**6
 # force on upper, displacement upper minus lower
 fu=r[:,2]*(-6*.010238*3.34**6/rr**8+3.629*e/rr*C)
 inside=rs<c*c
 return v*inside,fu*inside,inside

def group_force(ids,fu,group,counts,d):
 return np.bincount(group[ids[:,1]],weights=fu/np.sqrt(counts[group[ids[:,1]]]),minlength=d)-np.bincount(group[ids[:,0]],weights=fu/np.sqrt(counts[group[ids[:,0]]]),minlength=d)
rows=[];pairdata={}
for name,c in [('21_dir_10024',20),('21_dir_0',24),('21_dir_10024',24)]:
 a,p=read(name,c);ids,r,im,bounds=shell(a,name,c);group=a['group_index'];d=len(a['g_fine']);counts=np.bincount(group)
 pred=np.zeros((d,2));axisrows=[]
 for ax in [0,1]:
  states=[]
  for h,sgn in [(1e-4,1),(1e-4,-1),(5e-5,1),(5e-5,-1)]:
   rr=r.copy();rr[:,ax]+=sgn*h;states.append(pair(rr,c))
  member=np.stack([s[2] for s in states]);cross=member.any(0)&~member.all(0)
  Fs=[group_force(ids[cross],s[1][cross],group,counts,d) for s in states]
  gc=-(Fs[0]-Fs[1])/(2e-4);gf=-(Fs[2]-Fs[3])/1e-4;pred[:,ax]=gf-gc
  axisrows.append({'axis':ax,'crossing_pairs':int(cross.sum())})
  key=f'{name}_{c}_axis{ax}';pairdata[key+'_ids']=ids[cross]+1;pairdata[key+'_images']=im[cross];pairdata[key+'_r']=r[cross];pairdata[key+'_membership']=member[:,cross]
 observed=a['g_fine']-a['g_coarse'];res=observed-pred;j,ax=np.unravel_index(abs(observed).argmax(),observed.shape)
 rows.append({'kind':'local_g','case':name,'cutoff_A':c,'image_bounds':bounds,'shell_pairs':len(ids),'axes':axisrows,'max_observed_step_difference':float(abs(observed).max()),'largest_entry':[int(j),int(ax)],'observed_at_largest':float(observed[j,ax]),'crossing_at_largest':float(pred[j,ax]),'max_residual_after_attribution':float(abs(res).max()),'attribution_pass':bool(abs(res).max()<=1e-7)})
 pairdata[f'{name}_{c}_observed']=observed;pairdata[f'{name}_{c}_predicted']=pred;pairdata[f'{name}_{c}_residual']=res
 print(rows[-1],flush=True)
for name,ax in [('21_dir_10024',0),('31_dir_10084',1),('31_dir_10134',1)]:
 c=16;a,p=read(name,c);ids,r,im,bounds=shell(a,name,c);group=a['group_index'];d=len(a['g_fine']);counts=np.bincount(group);w=np.where(np.arange(d)<d//2,-1.,1.)/np.sqrt(d);D=w[group]/np.sqrt(counts[group]);deltaD=D[ids[:,1]]-D[ids[:,0]]
 states=[];h=.001
 for sz,sx in [(1,1),(1,-1),(-1,1),(-1,-1)]:
  rr=r.copy();rr[:,2]+=sz*h*deltaD;rr[:,ax]+=sx*h;states.append(pair(rr,c))
 for sx in [1,-1]:
  rr=r.copy();rr[:,ax]+=sx*5e-5;states.append(pair(rr,c))
 member=np.stack([s[2] for s in states]);cross=member.any(0)&~member.all(0)
 ge=(states[0][0]-states[1][0]-states[2][0]+states[3][0])/(4*h*h)
 gf=-(states[4][1]-states[5][1])*deltaD/1e-4
 predicted=float((ge[cross]-gf[cross]).sum())
 er=json.loads((base/'graphite-cutoff'/name/'ENERGY_CHECK.json').read_text());erow=next(z for z in er['checks'] if z['direction']=='breathing' and z['h_A']==.001)['mixed'][ax]
 observed=erow['energy_mixed']-erow['force_mixed'];res=observed-predicted
 rows.append({'kind':'energy_mixed','case':name,'cutoff_A':c,'axis':ax,'h_A':h,'image_bounds':bounds,'shell_pairs':len(ids),'crossing_pairs':int(cross.sum()),'observed_signed_error':observed,'crossing_energy_mixed':float(ge[cross].sum()),'crossing_force_mixed':float(gf[cross].sum()),'predicted_signed_error':predicted,'residual_after_attribution':res,'attribution_pass':bool(abs(res)<=5e-6)})
 key=f'{name}_{c}_energyaxis{ax}';pairdata[key+'_ids']=ids[cross]+1;pairdata[key+'_images']=im[cross];pairdata[key+'_r']=r[cross];pairdata[key+'_membership']=member[:,cross];pairdata[key+'_energy_g']=ge[cross];pairdata[key+'_force_g']=gf[cross]
 print(rows[-1],flush=True)
np.savez_compressed(root/'PAIRS.npz',**pairdata)
inputs={}
for name in cases:
 for c in [16,20,24]:
  a,p=read(name,c);fp=p/'MATRICES.npz';inputs[str(fp.relative_to(base))]=hashlib.sha256(fp.read_bytes()).hexdigest()
res={'status':'CUTOFF_CROSSINGS_ACCOUNT_FOR_FAILED_STENCILS' if all(r['attribution_pass'] for r in rows) else 'ATTRIBUTION_INCOMPLETE','rows':rows,'input_sha256':inputs,'pairs_sha256':hashlib.sha256((root/'PAIRS.npz').read_bytes()).hexdigest(),'scope':'Post-failure computational attribution only; original scientific gates unchanged; hard cutoff has force discontinuity','bath_inference':'HOLD','physical_promotion':0}
dump(root/'RESULTS.json',res)
