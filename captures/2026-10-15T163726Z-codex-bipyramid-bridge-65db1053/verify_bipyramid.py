"""Exact finite exploration of the pictured hub and filled bipyramid models."""
from pathlib import Path
from itertools import combinations,permutations
from fractions import Fraction as Q
import json,numpy as np
ROOT=Path(__file__).resolve().parent
checks=[]
def check(name,ok,kind='EXACT'):
 assert bool(ok),name
 checks.append({'name':name,'kind':kind,'status':'PASS'})
def oriented(t):
 if len(set(t))!=len(t):return None,0
 return tuple(sorted(t)),(-1)**sum(t[i]>t[j] for i in range(len(t)) for j in range(i+1,len(t)))
def complex_of(tets=None,edges=None):
 tops=tets if tets is not None else edges
 C=[sorted({s for t in tops for s in combinations(t,d+1)}) for d in range(4)]
 ids=[{s:i for i,s in enumerate(c)} for c in C];off=np.cumsum([0]+list(map(len,C)));n=int(off[-1]);boundary=np.zeros((n,n),dtype=object);B=[]
 for d in [1,2,3]:
  b=np.zeros((len(C[d-1]),len(C[d])),dtype=object)
  for j,s in enumerate(C[d]):
   for k in range(d+1):b[ids[d-1][s[:k]+s[k+1:]],j]=(-1)**k
  B.append(b);boundary[off[d-1]:off[d],off[d]:off[d+1]]=b
 return dict(C=C,ids=ids,off=off,n=n,B=B,boundary=boundary,A=boundary.T-boundary)
def rank(a):
 a=[[Q(int(x)) if not isinstance(x,Q) else x for x in row] for row in a];r=0
 if not a:return 0
 for j in range(len(a[0])):
  p=next((i for i in range(r,len(a)) if a[i][j]),None)
  if p is None:continue
  a[r],a[p]=a[p],a[r];v=a[r][j];a[r]=[x/v for x in a[r]]
  for i in range(r+1,len(a)):
   v=a[i][j]
   if v:a[i]=[x-v*y for x,y in zip(a[i],a[r])]
  r+=1
  if r==len(a):break
 return r
def inverse(a):
 n=len(a);z=[[Q(x) for x in row]+[Q(int(i==j)) for j in range(n)] for i,row in enumerate(a)]
 for k in range(n):
  p=next(i for i in range(k,n) if z[i][k]);z[k],z[p]=z[p],z[k];v=z[k][k];z[k]=[x/v for x in z[k]]
  for i in range(n):
   if i!=k:
    v=z[i][k]
    if v:z[i]=[x-v*y for x,y in zip(z[i],z[k])]
 return np.array([r[n:] for r in z],dtype=object)
def spectrum(model,candidates):
 A=model['A'];L=-A@A;n=model['n'];spec={}
 for lam in candidates:
  mult=n-rank(L-lam*np.eye(n,dtype=object))
  if mult:spec[str(lam)]=mult
 check('complete_squared_spectrum_'+str(n),sum(spec.values())==n)
 return spec
old=complex_of(tets=[(0,1,2,3),(0,1,2,4)])
fine=complex_of(tets=[tuple(sorted((5,i,j,a))) for i,j in [(0,1),(1,2),(0,2)] for a in [3,4]])
star=complex_of(edges=[(i,5) for i in range(5)])
for name,m in [('old',old),('fine',fine),('star',star)]:
 check('boundary_squared_'+name,np.array_equal(m['boundary']@m['boundary'],np.zeros((m['n'],m['n']),dtype=object)))
 check('skew_'+name,np.array_equal(m['A'].T,-m['A']))
specold=spectrum(old,[0,3,5]);specfine=spectrum(fine,[0,1,3,4,6]);specstar=spectrum(star,[0,1,6])
check('old_spectrum_matches_ledger',specold=={'0':1,'3':8,'5':14})
check('filled_bipyramid_fvector',list(map(len,old['C']))==[5,9,7,2])
check('hub_refinement_fvector',list(map(len,fine['C']))==[6,14,15,6])
check('outer_boundary_still_six_faces',sum(sum(int(x!=0) for x in row)==1 for row in fine['B'][2])==6)

# Symbolic two-coefficient star polynomial: use a tiny polynomial ring over Q.
def add(p,q):
 r=p.copy()
 for k,v in q.items():r[k]=r.get(k,Q(0))+v
 return {k:v for k,v in r.items() if v}
def mul(p,q):
 r={}
 for (i,j),a in p.items():
  for (k,l),b in q.items():r[(i+k,j+l)]=r.get((i+k,j+l),Q(0))+a*b
 return {k:v for k,v in r.items() if v}
trace={(2,0):Q(4),(0,2):Q(3)};disc=add(mul({(2,0):Q(4),(0,2):Q(-3)},{(2,0):Q(4),(0,2):Q(-3)}),{(2,2):Q(24)})
check('weighted_star_discriminant',disc=={(4,0):Q(16),(0,4):Q(9)})
check('weighted_star_collective_determinant',12-6==6)
check('regular_tetrahedron_pair_radial_ratio_squared',Q(2,3)/Q(1,3)==2)
check('adding_hub_does_not_mean_adding_four_simplex',fine['n']==41 and len(fine['C'][3])==6)
# A Berry-type endpoint reassignment can couple an old dark direction to the hub.
Dstar=star['B'][0];weights=np.array([1 if next(v for v in edge if v!=5)<3 else 2 for edge in star['C'][1]],dtype=object)
W=np.diag(weights);Aw=np.block([[np.zeros((6,6),dtype=object),-Dstar@W],[W@Dstar.T,np.zeros((5,5),dtype=object)]])
old_dark=np.zeros(11,dtype=object);old_dark[0]=1;old_dark[2]=-1
swapped=np.zeros(11,dtype=object);swapped[3]=1;swapped[2]=-1
check('equatorial_difference_hub_second_derivative_zero',(Aw@Aw@old_dark)[5]==0)
check('axial_equatorial_reassignment_mixes_hub_visible_mode',(Aw@Aw@swapped)[5]==3)

# The radial graph is not an invariant chain subspace of the filled model.
J=np.zeros((fine['n'],star['n']),dtype=object)
for d in [0,1]:
 for j,s in enumerate(star['C'][d]):J[fine['off'][d]+fine['ids'][d][s],star['off'][d]+j]=1
leak=(np.eye(fine['n'],dtype=object)-J@J.T)@fine['A']@J
leak_rank=rank(leak);check('spoke_subspace_leaks_under_completion',leak_rank>0)

# Hub response and a peripheral discriminator.
def port(m,simplex,degree=0):
 v=np.zeros(m['n'],dtype=object);v[m['off'][degree]+m['ids'][degree][simplex]]=1;return v
hubmoments={};obs={}
for name,m in [('star',star),('fine',fine)]:
 h=port(m,(5,));v=h.copy();mom=[];columns=[]
 for k in range(m['n']):
  columns.append(v.copy())
  if k<10:mom.append(int(h@v))
  v=m['A']@v
 hubmoments[name]=mom;obs[name]=rank(np.array(columns,dtype=object).T)
 check('hub_bright_dimension_three_'+name,obs[name]==3)
 axial=port(m,(3,))-port(m,(4,));lam=1 if name=='star' else 4
 check('axial_difference_squared_frequency_'+name,np.array_equal(-m['A']@m['A']@axial,lam*axial))
 h0=h[:6];L0=m['B'][0]@m['B'][0].T
 check('hub_Laplacian_identity_'+name,np.array_equal(L0@h0,6*h0-np.ones(6,dtype=object)))
check('hub_moments_identical',hubmoments['star']==hubmoments['fine'])
face=port(old,(0,1,2),2);check('shared_face_only_squared_frequency_5',np.array_equal(-old['A']@old['A']@face,5*face))
cellsum=port(old,(0,1,2,3),3)+port(old,(0,1,2,4),3)
celldiff=port(old,(0,1,2,3),3)-port(old,(0,1,2,4),3)
check('cell_sum_squared_frequency_5',np.array_equal(-old['A']@old['A']@cellsum,5*cellsum))
check('cell_difference_squared_frequency_3',np.array_equal(-old['A']@old['A']@celldiff,3*celldiff))
check('shared_face_blind_to_difference',face@old['A']@celldiff==0)
Cmap=np.column_stack([port(old,(0,1,2,3),3),port(old,(0,1,2,4),3)])
M3=old['B'][2].T@old['B'][2];M3i=inverse(M3)
J4=np.column_stack([Cmap,-old['A']@Cmap@M3i]);A4=np.block([[np.zeros((2,2),dtype=object),np.eye(2,dtype=object)],[-M3,np.zeros((2,2),dtype=object)]])
check('minimal_cell_exchange_module_dimension_four',rank(J4)==4)
check('minimal_cell_exchange_module_invariant',np.array_equal(old['A']@J4,J4@A4))
H4=J4.T@J4
check('minimal_cell_exchange_storage_metric',np.array_equal(H4,np.block([[np.eye(2,dtype=object),np.zeros((2,2),dtype=object)],[np.zeros((2,2),dtype=object),M3i]])) and np.array_equal(H4@A4+A4.T@H4,np.zeros((4,4),dtype=object)))

# Exact subdivision chain map and three simplicial collapse retractions.
S=np.zeros((fine['n'],old['n']),dtype=object)
for d,cs in enumerate(old['C']):
 for j,s in enumerate(cs):
  pieces=[(s,1)]
  if s[:3]==(0,1,2):
   tail=s[3:];pieces=[((5,1,2)+tail,1),((5,0,2)+tail,-1),((5,0,1)+tail,1)]
  for t,coef in pieces:
   t,sgn=oriented(t);S[fine['off'][d]+fine['ids'][d][t],old['off'][d]+j]+=coef*sgn
Rs=[]
for a in range(3):
 R=np.zeros((old['n'],fine['n']),dtype=object)
 for d,cs in enumerate(fine['C']):
  for j,s in enumerate(cs):
   t,sgn=oriented(tuple(a if v==5 else v for v in s))
   if sgn:R[old['off'][d]+old['ids'][d][t],fine['off'][d]+j]=sgn
 check('collapse_chain_map_'+str(a),np.array_equal(R@fine['boundary'],old['boundary']@R))
 check('collapse_left_inverse_'+str(a),np.array_equal(R@S,np.eye(old['n'],dtype=object)))
 Rs.append(R)
R=sum(Rs)/Q(3);check('subdivision_chain_map',np.array_equal(fine['boundary']@S,S@old['boundary']))
Pi=np.eye(fine['n'],dtype=object)-S@R;H=R.T@R+Pi.T@Pi;Hi=inverse(H)
AH=Hi@fine['boundary'].T@H-fine['boundary']
check('metric_coarse_isometry',np.array_equal(S.T@H@S,np.eye(old['n'],dtype=object)))
check('metric_positive_factor_inverse',np.array_equal(Hi@H,np.eye(fine['n'],dtype=object)))
check('weighted_skew_identity',np.array_equal(H@AH+AH.T@H,np.zeros_like(H)))
check('coarse_clock_intertwiner',np.array_equal(AH@S,S@old['A']))
check('coarse_readout_intertwiner',np.array_equal(R@AH,old['A']@R))
check('Euclidean_metric_does_not_intertwine',not np.array_equal(fine['A']@S,S@old['A']))

# Equatorial permutations and axial exchange form 12 signed geometric symmetries.
for n,p in enumerate(permutations(range(3))):
 for swap in [False,True]:
  vp=list(p)+([4,3] if swap else [3,4])+[5]
  def action(m):
   T=np.zeros((m['n'],m['n']),dtype=object)
   for d,cs in enumerate(m['C']):
    for j,s in enumerate(cs):
     t,sgn=oriented(tuple(vp[v] for v in s));T[m['off'][d]+m['ids'][d][t],m['off'][d]+j]=sgn
   return T
  Tf=action(fine);To=action(old)
  check('refinement_symmetry_'+str(n)+'_'+str(swap),np.array_equal(Tf@S,S@To) and np.array_equal(R@Tf,To@R))
  check('metric_symmetry_'+str(n)+'_'+str(swap),np.array_equal(Tf.T@H@Tf,H))

# Numerical corroboration of exact identities and one generic weighted-star port rank.
for e,a in [(1.,2.),(1.,1.)]:
 D=np.array(star['B'][0],dtype=float);weights=np.array([e if next(v for v in edge if v!=5)<3 else a for edge in star['C'][1]])
 Aw=np.block([[np.zeros((6,6)),-D@np.diag(weights)],[np.diag(weights)@D.T,np.zeros((5,5))]])
 h=np.array(port(star,(5,)),dtype=float);O=np.array([h@np.linalg.matrix_power(Aw,k) for k in range(11)])
 expected=5 if e!=a else 3
 check('weighted_hub_bright_rank_'+str(e)+'_'+str(a),np.linalg.matrix_rank(O,tol=1e-6)==expected,'NUMERICAL')
for t in [.1,.7,2.]:
 from scipy.linalg import expm
 c=np.zeros(old['n']);c[old['off'][3]]=1
 y=expm(np.array(AH,dtype=float)*t)@np.array(S,dtype=float)@c
 target=np.array(S,dtype=float)@expm(np.array(old['A'],dtype=float)*t)@c
 check('weighted_trajectory_matches_coarse_'+str(t),np.linalg.norm(y-target)<1e-10,'NUMERICAL')

encode=lambda a:[[str(x) for x in row] for row in a]
data={'f_vectors':{k:list(map(len,m['C'])) for k,m in [('spoke_graph',star),('two_tetrahedra',old),('hub_refinement',fine)]},'squared_generator_spectra':{'spoke_graph':specstar,'two_tetrahedra':specold,'hub_refinement':specfine},'spoke_inclusion_leak_rank':leak_rank,'hub_bright_dimensions':obs,'hub_transfer_function':'(s^2+1)/(s*(s^2+6))','weighted_star_characteristic':'lambda*(lambda^2+e^2)^2*(lambda^2+a^2)*(lambda^4+(4*e^2+3*a^2)*lambda^2+6*e^2*a^2)','weighted_star_squared_collective_frequencies':'(4*e^2+3*a^2 +/- sqrt(16*e^4+9*a^4))/2','metric_construction':'H=R^T R+(I-SR)^T(I-SR), R=mean of the three equatorial simplicial collapses','minimal_module':{'embedding':encode(J4),'generator':encode(A4),'metric':encode(H4)},'simplices':{'old':old['C'],'fine':fine['C'],'star':star['C']},'S':encode(S),'R':encode(R),'H':encode(H),'A_weighted':encode(AH),'physical_promotion':0}
(ROOT/'BIPYRAMID_DATA.json').write_text(json.dumps(data,indent=2)+'\n')
result={'status':'PASS','exact_checks':sum(c['kind']=='EXACT' for c in checks),'numerical_checks':sum(c['kind']=='NUMERICAL' for c in checks),'checks':checks,'independent_review':False,'physical_promotion':0}
(ROOT/'BIPYRAMID_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='checks'}));print(json.dumps({k:data[k] for k in ['f_vectors','squared_generator_spectra','spoke_inclusion_leak_rank','hub_bright_dimensions']}))
