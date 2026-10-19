"""Read-only sourceweighted exact coefficient audit and graph arithmetic diagnostic."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
from fractions import Fraction as F
import numpy as np
from flint import fmpz_mat,arb,fmpq,ctx
import mpmath as mp
ctx.prec=512;mp.mp.dps=160
P=Path(__file__).resolve().parent;W=P.parent/'source-weighted-work';I=P.parent/'source-weighted-inputs';repo=P.parent/'ud-repo'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
freeze=load(P/'FINAL_AUDIT_FREEZE.json');assert sha(__file__)==freeze['review_code_sha256']
f=load(W/'FREEZE.json');assert sha(W/'FREEZE.json')==freeze['source_freeze_sha256'];checked={}
for n,h in f['files'].items():assert sha(W/n)==h;checked[str(W/n)]=h
for row in load(W/'INPUT_INDEX.json')['members']:
 assert sha(I/row['destination'])==row['sha256'];checked[str(I/row['destination'])]=row['sha256']
 assert sha(repo/'captures'/row['capture']/'MANIFEST.json')==row['manifest_sha256'] and sha(repo/row['archive'])==row['archive_sha256']
pf=load(W/'PROPOSAL_FREEZE.json');assert sha(W/'INVERSE_PROPOSAL.npz')==pf['sha256'];checked[str(W/'INVERSE_PROPOSAL.npz')]=pf['sha256']
w=load(W/'WEIGHTS_CERTIFICATE.json');graph=load(W/'GRAPH_CERTIFICATE.json');u=load(W/'inputs/PARENT_UNIFORM.json');o=load(W/'inputs/PARENT_ORDER.json');g=load(W/'inputs/PR210_FREEZE.json')['gates'];allow=load(W/'inputs/PUBLISHED_ALLOWANCE.json')
def encode(x):
 assert x.dtype==np.float64 and np.all(np.isfinite(x))
 pair=[float(v).as_integer_ratio() for v in x.flat];b=max(d.bit_length()-1 for n,d in pair)
 return np.array([n<<(b-d.bit_length()+1) for n,d in pair],object).reshape(x.shape),b
with np.load(I/'C.npz',allow_pickle=False) as z:cn,bc=encode(z['coefficient'])
with np.load(W/'INVERSE_PROPOSAL.npz',allow_pickle=False) as z:mn,bm=encode(z['inverse'])
Cf=fmpz_mat(cn.tolist());Mf=fmpz_mat(mn.tolist());K=Cf.transpose()*Mf;bk=bc+bm
defect=np.array((Cf*K).tolist(),object)-np.eye(209,dtype=object)*(1<<(bc+bk));rho2=F(sum(int(v)**2 for v in defect.flat),1<<(2*(bc+bk)))
assert rho2<1 and rho2<=F(*w['right_inverse_residual_F_upper'])**2
old=np.random.default_rng(172026).choice([-1.,1.],size=(2294,160)).astype(np.int64);v=np.pad(np.array(load(I/'NULL_VECTOR.json')['vector'],np.int64),(0,1974));new=np.random.default_rng(184052).choice([-1.,1.],size=(2294,160)).astype(np.int64);A=np.column_stack((2*old,v,2*new))
AK=fmpz_mat(A.tolist())*K;row_squared=np.array([sum(int(v)**2 for v in row) for row in AK.tolist()],dtype=object).reshape(62,37);maxima=np.max(row_squared,axis=0)
assert list(map(str,maxima))==w['row_square_maxima_decimal'] and w['row_square_scale_bits']==2*(bk+7)
noisec=arb(8191).sqrt()*sum(arb(int(v)).sqrt() for v in maxima)/(1<<(bk+7));published=arb(fmpq(*w['weighted_noise_multiplier_upper']));assert noisec<=published
rk2=F(*w['baseline_weighted_squared']);assert rk2>=0 and rk2<=F(*w['baseline_weighted_F_upper'])**2
assert F(*w['baseline_unweighted_squared_control'])==F(*u['baseline_exact_low_rank_residual_squared'])
# Independently check the cyclic correction at frozen sign/channel boundary times.
times=np.array(freeze['baseline_sample_times'],np.int64);cyclic=[]
for k in range(3):
 with np.load(I/f'ANCHOR_{k}.npz',allow_pickle=False) as z:cyclic.append(z['numerator'])
Nc=np.vstack(cyclic);selected=Nc[times].copy()
for prep in range(37):selected-=(1-2*((prep+times//62)%2))[:,None]*A[37*((prep+times)%62)+prep,:]
raw=Path(freeze['baseline_raw_path']);assert sha(raw)==freeze['baseline_raw_sha256'];Y=np.memmap(raw,dtype='<i8',mode='r',shape=(37,8191,62));X=Y[:,times,:].transpose(1,2,0).reshape(len(times),2294).copy();assert max(abs(int(X.min())),abs(int(X.max())))*int(np.abs(A).sum(axis=0).max())<2**63
assert np.array_equal(X@A,selected)
q=lambda p:mp.mpf(p[0])/p[1]
r=q(u['baseline_low_rank_residual_upper']);alpha=q(o['qth_sigma_lower'])-r;rho=q(w['right_inverse_residual_F_upper']);eta0=q(w['source_Gram_defect_F_upper']);M=mp.sqrt(1+eta0)*q(w['source_coefficient_F_upper']);diagnostics=[]
for row in graph['rows']:
 mode=row['mode'];delta=q(row['encoded_radius']);eps=mp.mpf(0) if mode=='ideal' else q(g['full_SVD_error']);eta=mp.mpf(0) if mode=='ideal' else q(g['full_left_orthogonality']);ep=eps*(mp.sqrt(209) if mode=='returned_operator_only' else 1)
 e=r+q(u['per_vector_noise_multiplier_upper'])*delta+eps;ef=r+q(u['per_vector_noise_multiplier_upper'])*delta+ep;weighted=(q(w['baseline_weighted_F_upper'])+q(w['weighted_noise_multiplier_upper'])*delta)/((1-rho)*mp.sqrt(1-eta0))+ep/alpha
 z=weighted+e*ef/(alpha*alpha);ac=(2*M*e+2*e*e)/(alpha*alpha);bcg=e*(M+e)/(alpha*alpha);disc=(1-ac)**2-4*bcg*z
 root=((1-ac)-mp.sqrt(disc))/(2*bcg);x=q(row['graph_tangent_F_upper']);assert x>=root and z+ac*x+bcg*x*x<x and ac+2*bcg*x<1 and alpha>2*e
 lead=((alpha-e)**2-2*e*(M+e)*x)/(1+x*x);assert lead>e*e
 dist=x+2*eta/(1+mp.sqrt(1-eta));J=mp.sqrt(1+eta)*(q(u['comparison_shift_residual_upper'])+dist*(1+q(u['comparison_shift_norm_upper'])));amin=mp.sqrt(1-eta)*(q(u['deleted_two_rows_beta_lower'])-dist);ret=mp.sqrt(J*J+(q(row['normal_residual_ceiling'])/amin)**2)
 assert J<=q(row['exact_LS_shift_upper']) and ret<=q(row['returned_shift_upper']) and amin>=q(row['deleted_sigma_lower'])
 sufficient=ret<q(allow['raw_shift_strict_upper_allowance_lower']);assert sufficient==row['published_shift_allowance_sufficient'] and all(row['graph_gates'].values())
 diagnostics.append({'mode':mode,'radius':row['encoded_radius'],'normal_ceiling':row['normal_residual_ceiling'],'independent_J':mp.nstr(J,100),'shift_only_sufficient':bool(sufficient)})
assert all(sha(Path(p))==h for p,h in checked.items())
result={'status':'PASS_SAME_TEAM_SOURCE_WEIGHTED_CODE_AND_GRAPH_REVIEW','reviewed_at_utc':datetime.now(timezone.utc).isoformat(),'review_code_sha256':sha(__file__),'source_freeze_sha256':sha(W/'FREEZE.json'),'source_hashes_before_after':checked,'weights_certificate_sha256':sha(W/'WEIGHTS_CERTIFICATE.json'),'graph_certificate_sha256':sha(W/'GRAPH_CERTIFICATE.json'),'exact_auxiliary_checks':['K=CtransposeM constructed exact, rightinverse residualsquared<1 and withinreportedupper.','All37rowmax squarednorms and128/2^bk scales exactlyrecomputed.','Weightednoise constant independently recomputed with512bitArb.','Five correctedbaselineN rows independentlyequal exact rawdot atsign/channelboundaries.','Unweightedresidual exactfraction matchespinnedbaseline; weightedbaselinefraction enclosure direction checks.'],'baseline_sample_times':freeze['baseline_sample_times'],'sampled_integer_projection_entries':len(times)*321,'weighted_baseline_matrix_reexecution_by_reviewer':False,'graph_arithmetic_diagnostic':diagnostics,'diagnostic_precision_decimal_digits':mp.mp.dps,'findings':['Riccati fixedpoint selfmap/contraction andleadingRayleighgate are valid and prevent selectingwronginvariantsubspace.','ExactMoorePenrose/rightsourceC/polarwhitening andcyclicbaselinecorrection are consistent.','ProjectedF vsoperator lanes, fullretainedpolar2p correction andnormalresidualpremise remain explicit.','Ideal fullradius shift-only sufficiency passes; returnedF/abstractoperator qualityceilings remainHOLD.','No uniform solver, otherseven gates, completephaseadmission or physicalsuccess follows.'],'material_issues':[],'dependencies':['Fullweighted baseline directmatrix calculation andcompletecleanproofreplay are separate pinned proofdependencies, not repeated by this audit.','Inputmember/archive manifests andexistingbaseline/sourcecertificates remainexplicit.'],'new_estimator_runs':0,'new_SVD_runs':0,'new_raw_generation':False,'external_independent_review':'PENDING','physical_promotion':0,'lane':'development — no registry entry'}
(P/'FINAL_AUDIT.json').write_text(json.dumps(result,indent=2));print(json.dumps({k:result[k] for k in ['status','sampled_integer_projection_entries','material_issues']}))
