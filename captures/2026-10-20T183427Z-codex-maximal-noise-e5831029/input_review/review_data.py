"""Independent two-boundary-pattern audit. Never generates raw or calls an estimator."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import argparse,hashlib,json,itertools,math
from pathlib import Path
from fractions import Fraction as F
import numpy as np
P=Path(__file__).resolve().parent
CASES=('boundary_pair_block','boundary_pair_rotating')
BASE_SHA='25a0888972c8fb961774ef69430070e07e1cf6bd02ca05fd1bb0a5552c6e9f59'
EST_SHA='5fa15ca0f3830f168fe9e1483db7f21cb6e462780209b4d8b4e8ad43d64cfe86'
WORD=(1,1,-1,1,-1,-1,-1);RESIDUES=frozenset((0,1,3,4,9,10,12));SHAPE=(37,8191,62)
def need(x,m):
 if not x:raise ValueError(m)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb')as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def read(p):return json.loads(Path(p).read_text())
def at(case,p,t):
 need(case in CASES,'unknown frozen case');need(0<=p<37 and 0<=t<8191,'index range')
 if case==CASES[0]:return ((17,1 if(p+t//257)%2==0 else-1),(48,1 if(t//31)%2==0 else-1))
 c=(7*p+11*t+5)%62
 return ((c,1 if(t+3*p)%13 in RESIDUES else-1),((c+31)%62,WORD[(t+2*p)%7]))
def expected(case,p):
 out=np.zeros((8191,62),np.int64)
 for t in range(8191):
  pairs=at(case,p,t);need(pairs[0][0]!=pairs[1][0],'two distinct channels')
  for c,s in pairs:out[t,c]=s
 return out
def lattice():
 # Complete canonical sparse enumeration, justified by the integer sum-of-squares proof.
 objects=[()]
 for c in range(62):
  for s in(-1,1):objects.append(((c,s),))
 for a,b in itertools.combinations(range(62),2):
  for s,u in itertools.product((-1,1),repeat=2):objects.append(((a,s),(b,u)))
 need(len(objects)==len(set(objects))==7689,'complete sparse cardinality')
 counts={k:sum(sum(s*s for _,s in obj)==k for obj in objects)for k in range(3)}
 need(counts=={0:1,1:124,2:7564},'exact norm allocation')
 need(all(F(sum(s*s for _,s in obj))<=F(9,4)for obj in objects),'inside fixed rational ball')
 # Exhaustive small-dimensional cross-check; analytic sum-of-squares argument supplies dimension62.
 for v in itertools.product(range(-2,3),repeat=4):
  sq=sum(c*c for c in v);classification=all(c in(-1,0,1)for c in v)and sum(c!=0 for c in v)<=2
  need((F(sq)<=F(9,4))==classification,'classification small exhaustive control')
 return {'status':'PASS_EXACT_QUANTIZED_ALPHABET_CLASSIFICATION','dimension':62,'quantum':[1,1<<48],'radius_over_quantum':[3,2],'squared_radius_over_quantum':[9,4],'integer_squared_norm_allowed':[0,1,2],'counts_by_squared_norm':counts,'total_per_vector_alphabet':7689,'maximum_integer_squared_norm':2,'maximum_norm_symbolic':'sqrt(2)*2^-48','maximum_squared_radius_ratio':[8,9],'global_trajectory_configurations_symbolic':'7689^303067','whole_trajectory_estimator_guarantee':False,'proof':'Sum of integer squares is an integer <=9/4 iff <=2. A coordinate of magnitude>=2 contributes>=4 and is excluded. The remaining unit coordinates contribute exactly their count, so at most two are nonzero. Conversely each listed sparse vector satisfies the inequality. Count=1+2*62+4*binomial(62,2).','crosscheck_dimension':4,'crosscheck_integer_coordinates':[-2,2],'crosscheck_vectors':625,'physical_promotion':0}
def controls():
 rows=[]
 def ck(k,x):need(bool(x),'control '+k);rows.append({'id':k,'pass':True})
 ck('block_origin',at(CASES[0],0,0)==((17,1),(48,1)))
 ck('block_before31',at(CASES[0],0,30)==((17,1),(48,1)))
 ck('block_at31',at(CASES[0],0,31)==((17,1),(48,-1)))
 ck('block_before257',at(CASES[0],0,256)==((17,1),(48,1)))
 ck('block_at257',at(CASES[0],0,257)==((17,-1),(48,1)))
 ck('block_prep_parity',at(CASES[0],1,257)==((17,1),(48,1)))
 ck('block_last',at(CASES[0],36,8190)==((17,-1),(48,1)))
 ck('rotating_origin',at(CASES[1],0,0)==((5,1),(36,1)))
 ck('rotating_nonresidue',at(CASES[1],0,2)==((27,-1),(58,-1)))
 ck('rotating_t12',at(CASES[1],0,12)==((13,1),(44,-1)))
 ck('rotating_t13',at(CASES[1],0,13)==((24,1),(55,-1)))
 ck('rotating_prep1_origin',at(CASES[1],1,0)==((12,1),(43,-1)))
 ck('rotating_last',at(CASES[1],36,8190)==((13,1),(44,-1)))
 for case in CASES:
  for p in(0,1,36):
   arr=expected(case,p);ck(case+'_unit_pairs_'+str(p),np.all(np.sum(arr*arr,axis=1)==2)and np.all(np.count_nonzero(arr,axis=1)==2))
  arr=expected(case,0);bad=arr.copy();bad[257,17]+=1;ck(case+'_altered_scalar_rejected',not np.array_equal(arr,bad))
 ck('cases_distinct',not np.array_equal(expected(CASES[0],0),expected(CASES[1],0)))
 ck('squared_ratio_exact',F(2,1<<96)/F(3,1<<49)**2==F(8,9))
 ck('two_quantum_same_coordinate_excluded',F(4)>F(9,4))
 ck('three_distinct_unit_coordinates_excluded',F(3)>F(9,4))
 ck('two_unit_coordinates_eligible',F(2)<F(9,4))
 toy=np.arange(12,dtype=np.int64).reshape(2,3,2);layout=toy.transpose(1,2,0).reshape(3,4)
 ck('channel_major_preparation_minor',all(layout[t,2*c+p]==toy[p,t,c]for p in range(2)for t in range(3)for c in range(2)))
 ck('wrong_layout_rejected',not np.array_equal(layout,toy.transpose(1,0,2).reshape(3,4)))
 ck('int64_strict_guard',2**63-1<2**63 and not 2**63<2**63)
 ck('binary64_strict_guard',2**53-1<2**53 and not 2**53<2**53)
 for case,p,t in[('replacement',0,0),(CASES[0],0,8191),(CASES[1],37,0)]:
  try:at(case,p,t);refused=False
  except ValueError:refused=True
  ck('index_or_replacement_'+str(len(rows)),refused)
 lattice();return rows
def validate(producer,repo,case):
 own=read(P/'DATA_DRIVER_FREEZE.json');need(sha(__file__)==own['driver_sha256'],'reviewer changed');need(set(own['cases'])==set(CASES),'two fixed case freezes');need(sha(producer/'FREEZE.json')==own['cases'][case],'producer freeze changed');f=read(producer/'FREEZE.json')
 for name,h in f['files'].items():need(sha(producer/name)==h,'source changed '+name)
 for name,h in f['repository_sources'].items():need(sha(repo/name)==h,'repository source changed '+name)
 need(sha(producer/'estimator.py')==EST_SHA,'estimator changed')
 for sibling in CASES:
  p=producer.parent/sibling;need(not(p/'FIT_INTENT.json').exists()and not(p/'RUN_EXECUTIONS.json').exists()and not(p/'results').exists(),'all data audits before first fit')
 return own
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--repo');ap.add_argument('--producer');ap.add_argument('--case',choices=CASES);ap.add_argument('--baseline');ap.add_argument('--raw');ap.add_argument('--raw-release');ap.add_argument('--out',required=True);ap.add_argument('--controls-only',action='store_true');ap.add_argument('--lattice-only',action='store_true');args=ap.parse_args();out=Path(args.out);need(not out.exists(),'exclusive review output')
 if args.lattice_only:result=lattice()
 elif args.controls_only:result={'status':'PASS_INDEPENDENT_BOUNDARY_PATTERN_CONTROLS','rows':controls(),'new_raw_records':0,'new_estimator_calls':0,'physical_promotion':0}
 else:
  need(all((args.repo,args.producer,args.case,args.baseline,args.raw,args.raw_release)),'all arguments required');repo=Path(args.repo);producer=Path(args.producer);baseline=Path(args.baseline);raw=Path(args.raw);case=args.case;validate(producer,repo,case);dfile=producer/'DATA_FREEZE.json';data=read(dfile);datum=data['record'];release=read(args.raw_release);need(release['raw_generation_released']is True and release['protocol_sha256']==sha(producer/'FREEZE.json'),'raw-only sourcebound release');need(data['protocol_sha256']==sha(producer/'FREEZE.json')and datum['case']==case,'data binding');need(sha(baseline)==BASE_SHA and baseline.stat().st_size==150321232 and baseline.stat().st_mode&0o222==0,'baseline identity and readonly');need(raw.stat().st_size==150321232 and raw.stat().st_mode&0o222==0,'actual raw size and readonly');before=sha(raw);need(before==datum['record_sha256']and before!=BASE_SHA,'actual new raw digest');y0=np.memmap(baseline,dtype='<i8',mode='r',shape=SHAPE);y=np.memmap(raw,dtype='<i8',mode='r',shape=SHAPE);full=np.empty(SHAPE,dtype=np.int64);scalars=vectors=changed=actualmax=basemax=0
  for p in range(37):
   actual=np.asarray(y[p],np.int64);base=np.asarray(y0[p],np.int64);am=max(abs(int(actual.min())),abs(int(actual.max())));bm=max(abs(int(base.min())),abs(int(base.max())));need(am+bm<2**63,'safe subtraction');difference=actual-base;target=expected(case,p);need(np.array_equal(difference,target),'all scalar differences');need(np.all(np.sum(difference*difference,axis=1)==2),'exact every vector norm');need(np.all(np.count_nonzero(difference,axis=1)==2),'two changed scalars pervector');full[p]=difference;scalars+=difference.size;vectors+=len(difference);changed+=int(np.count_nonzero(difference));actualmax=max(actualmax,am);basemax=max(basemax,bm)
  need(scalars==18790154 and vectors==303067 and changed==606134,'complete counts');small=read(producer/'inputs/NULL_VECTOR.json')['vector'];v=np.zeros(2294,np.int64);v[:len(small)]=small;old=np.random.default_rng(172026).choice([-1.,1.],(2294,160)).astype(np.int64);new=np.random.default_rng(184052).choice([-1.,1.],(2294,160)).astype(np.int64);need(int(v@v)==16228 and np.all(v@old==0),'independent sketch identities');A=np.column_stack((2*old,v,2*new));columnsum=int(np.abs(A).sum(axis=0).max());need(basemax*columnsum<2**63 and actualmax*columnsum<2**63,'projection int64 safety');X0=np.asarray(y0.transpose(1,2,0).reshape(8191,2294),np.int64);nominal=X0@A;del X0;correction=full.transpose(1,2,0).reshape(8191,2294)@A;need(max(abs(int(nominal.min())),abs(int(nominal.max())))+max(abs(int(correction.min())),abs(int(correction.max())))<2**63,'separated sum safety');N=nominal+correction;maximum=max(abs(int(N.min())),abs(int(N.max())));need(maximum<2**53,'exact binary64 conversion');ih=hashlib.sha256(N.astype('<i8').tobytes()).hexdigest();zh=hashlib.sha256((N.astype(float)/2.**55).astype('<f8').tobytes()).hexdigest();need(datum['projection']['integer_bytes_sha256']==ih and datum['projection']['projection_bytes_sha256']==zh,'independent separated projection digests');need(datum['projection']['numerator_max']==maximum and datum['projection']['partial_sum_bound']==actualmax*columnsum,'projection range identities');need(sha(raw)==before and sha(baseline)==BASE_SHA,'both inputs unchanged');validate(producer,repo,case)
  result={'status':'PASS_INDEPENDENT_BOUNDARY_RAW_AND_SEPARATED_PROJECTION','case':case,'record_sha256':before,'baseline_sha256':BASE_SHA,'raw_bytes':150321232,'scalar_differences_checked':scalars,'vectors_checked':vectors,'integer_vector_squared_norm':2,'changed_scalars':changed,'integer_projection_sha256':ih,'dyadic_projection_sha256':zh,'projection_entries':int(N.size),'numerator_max':maximum,'actual_integer_partial_sum_bound':actualmax*columnsum,'source_radius':[3,1<<49],'noise_quantum':[1,1<<48],'radius_squared_ratio':[8,9],'data_freeze_sha256':sha(dfile),'driver_freeze_sha256':sha(P/'DATA_DRIVER_FREEZE.json'),'source_freeze_sha256':sha(producer/'FREEZE.json'),'raw_release_sha256':sha(args.raw_release),'new_estimator_calls':0,'new_raw_records':0,'input_read_only_and_unchanged':True,'newcase_full_reconstruction_sigma210_lower':'NOT_EVALUATED','scope':'Complete actual raw audit and separate nominal+delta projection; maximal encoded amplitude only, no whole trajectory or physical guarantee','external_review':'PENDING','physical_promotion':0}
 out.parent.mkdir(parents=True,exist_ok=True)
 with out.open('x')as f:json.dump(result,f,indent=2);f.write('\n')
 print(json.dumps({'status':result['status'],'case':result.get('case'),'control_count':len(result.get('rows',[]))}),flush=True)
if __name__=='__main__':main()
