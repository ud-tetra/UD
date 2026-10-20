"""Independent read-only shared-raw audit, no raw generation or estimator call."""
import argparse,hashlib,json
from pathlib import Path
import numpy as np
P=Path(__file__).resolve().parent
CASE='null_top1_alternating_negated';BASE_SHA='25a0888972c8fb961774ef69430070e07e1cf6bd02ca05fd1bb0a5552c6e9f59'
SHAPE=(37,8191,62);COUNT=18790154

def sha(path):
 h=hashlib.sha256()
 with Path(path).open('rb')as f:
  for block in iter(lambda:f.read(1048576),b''):h.update(block)
 return h.hexdigest()
def read(path):return json.loads(Path(path).read_text())
def negated_weights(v,channels=62,preps=37):
 w=np.zeros((channels,preps),dtype=np.int64)
 for prep in range(preps):
  c=max(range(channels),key=lambda c:(abs(int(v[c*preps+prep])),-c));w[c,prep]=-1 if int(v[c*preps+prep])>=0 else 1
 return w

def controls():
 rows=[]
 def ck(name,value):assert value,name;rows.append({'id':name,'pass':True})
 v=np.array([5,-7,-5,7],dtype=np.int64);w=negated_weights(v,2,2)
 ck('tie_breaks_lowest_channel_and_negates_sign',w.tolist()==[[-1,1],[0,0]])
 u=np.array([1,-1,1],dtype=np.int64);delta=u[:,None]*np.array([-1,0],dtype=np.int64)[None,:]
 ck('negative_recipe_alternates_sign',delta.tolist()==[[-1,0],[1,0],[-1,0]])
 ck('exact_unit_squared_vector_norm',np.all(np.sum(delta*delta,axis=1)==1))
 ck('nominal_zero_delta_not_candidate',not np.array_equal(np.zeros_like(delta),delta))
 ck('positive_recipe_not_candidate',not np.array_equal(-delta,delta))
 Y=np.arange(12,dtype=np.int64).reshape(2,3,2);X=Y.transpose(1,2,0).reshape(3,4)
 ck('layout_channel_times_preparation',all(X[t,c*2+a]==Y[a,t,c]for a in range(2)for t in range(3)for c in range(2)))
 ck('unsafe_subtraction_bound_refused',not (2**63-1)+1<2**63)
 ck('one_quantum_inside_frozen_radius_squared',4*1<=9)
 ck('two_quanta_same_scalar_outside_source_ball',not 4*4<=9)
 ck('binary64_exact_range_strict',2**53-1<2**53 and not 2**53<2**53)
 return rows

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--repo',required=True);ap.add_argument('--producer',required=True);ap.add_argument('--baseline',required=True);ap.add_argument('--raw',required=True);ap.add_argument('--raw-release',required=True);args=ap.parse_args();repo=Path(args.repo);producer=Path(args.producer);baseline=Path(args.baseline);raw=Path(args.raw);freeze=read(P/'DATA_DRIVER_FREEZE.json');assert sha(__file__)==freeze['driver_sha256'];assert sha(producer/freeze['producer_freeze_file'])==freeze['producer_freeze_sha256'];assert read(args.raw_release)['raw_generation_released']is True
 for name,h in read(P/'REVIEW_PLAN.json')['source_hashes'].items():assert sha(repo/name)==h,name
 datum=read(producer/'DATA_FREEZE.json')['record'];assert datum['case']==CASE;assert sha(baseline)==BASE_SHA and baseline.stat().st_size==150321232;assert raw.stat().st_size==150321232;assert raw.stat().st_mode&0o222==0,'shared raw must be read-only';before=sha(raw);assert datum['record_sha256']==before and before!=BASE_SHA
 assert not(producer/'RUN_EXECUTIONS.json').exists(),'data review must precede fit';assert not(producer/'results'/CASE/'RUN.json').exists(),'no fit before data audit'
 source=read(repo/'captures/2026-10-19T222108Z-codex-uniform-phase-evidence-4a6f6bda/phase/inputs/NULL_VECTOR.json');v=np.zeros(2294,dtype=np.int64);v[:len(source['vector'])]=source['vector'];w=negated_weights(v);u=np.ones(8191,dtype=np.int64);u[1::2]=-1;Y0=np.memmap(baseline,dtype='<i8',mode='r',shape=SHAPE);Y=np.memmap(raw,dtype='<i8',mode='r',shape=SHAPE);changed=0;vectors=0;scalars=0;actual_max=0;base_max=0
 for prep in range(37):
  a=np.asarray(Y[prep],dtype=np.int64);b=np.asarray(Y0[prep],dtype=np.int64);ma=max(abs(int(a.min())),abs(int(a.max())));mb=max(abs(int(b.min())),abs(int(b.max())));assert ma+mb<2**63,'subtraction overflow bound';difference=a-b;expected=u[:,None]*w[:,prep][None,:];assert np.array_equal(difference,expected),'candidate recipe sign/layout mismatch';norms=np.sum(difference*difference,axis=1);assert np.all(norms==1);changed+=int(np.count_nonzero(difference));vectors+=len(norms);scalars+=difference.size;actual_max=max(actual_max,ma);base_max=max(base_max,mb)
 assert vectors==303067 and scalars==COUNT and changed==303067
 # Independent association: project the nominal once and add the proved rank-one negative update.
 old=np.random.default_rng(172026).choice([-1.,1.],(2294,160)).astype(np.int64);new=np.random.default_rng(184052).choice([-1.,1.],(2294,160)).astype(np.int64);assert int(v@v)==16228 and np.all(v@old==0);A=np.column_stack((2*old,v,2*new));col_bound=max(int(x)for x in np.abs(A).sum(axis=0));assert base_max*col_bound<2**63 and actual_max*col_bound<2**63
 X0=np.asarray(Y0.transpose(1,2,0).reshape(8191,2294),dtype=np.int64);N0=X0@A;del X0;correction=w.reshape(-1)@A;assert max(abs(int(x))for x in correction)<2**63;N=N0+u[:,None]*correction[None,:];maximum=max(abs(int(N.min())),abs(int(N.max())));assert maximum<2**53
 integer_hash=hashlib.sha256(N.astype('<i8').tobytes()).hexdigest();dyadic_hash=hashlib.sha256((N.astype(float)/2.**55).astype('<f8').tobytes()).hexdigest();assert datum['projection']['integer_bytes_sha256']==integer_hash and datum['projection']['projection_bytes_sha256']==dyadic_hash;assert datum['projection']['numerator_max']==maximum;assert sha(raw)==before and sha(baseline)==BASE_SHA
 result={'status':'PASS_INDEPENDENT_SHARED_RAW_RECIPE_NORM_AND_RANK_ONE_PROJECTION','case':CASE,'record_sha256':before,'baseline_sha256':BASE_SHA,'raw_bytes':150321232,'scalar_differences_checked':scalars,'vectors_checked':vectors,'integer_vector_squared_norm':1,'changed_scalars':changed,'negative_w_int64le_sha256':hashlib.sha256(w.reshape(-1).astype('<i8').tobytes()).hexdigest(),'integer_projection_sha256':integer_hash,'dyadic_projection_sha256':dyadic_hash,'projection_entries':int(N.size),'numerator_max':maximum,'actual_integer_partial_sum_bound':actual_max*col_bound,'frozen_source_radius':[3,1<<49],'data_freeze_sha256':sha(producer/'DATA_FREEZE.json'),'driver_freeze_sha256':sha(P/'DATA_DRIVER_FREEZE.json'),'new_estimator_calls':0,'duplicate_raw_generation_or_copy':False,'new_case_full_reconstruction':'NOT_EVALUATED','scope':'All actual bytes checked read-only before fit; nominal/targets exposed, no global/blind/physical freshness claim','external_review':'PENDING','physical_promotion':0};out=P/'DATA_REVIEW_RECEIPT.json';assert not out.exists()
 with out.open('x')as f:json.dump(result,f,indent=2);f.write('\n')
 print(json.dumps({'status':result['status'],'record_sha256':before,'integer_projection_sha256':integer_hash}))
if __name__=='__main__':main()
