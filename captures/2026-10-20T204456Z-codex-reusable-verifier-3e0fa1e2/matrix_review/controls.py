"""Synthetic generic all-statistic identity, dependency, codec, root and guard controls."""
import argparse,json,tempfile
from pathlib import Path
from fractions import Fraction as F
import numpy as np
import audit as a

def toy():
 data={'N':np.array([[2,0],[0,0],[0,0]],dtype=np.int64),'Ui':np.array([[1],[0],[0]],dtype=object),'Vi':np.array([[1],[0]],dtype=object),'Di':np.array([[0],[1]],dtype=object),'si':np.array([2],dtype=object),'s':[F(2),F(0)],'m':3,'n':2,'q':1,'bN':0,'bU':0,'bV':0,'bD':0,'bS':0}
 mat={'M':np.array([[4,0],[0,0]],dtype=object),'K':np.array([[2],[0]],dtype=object),'A':np.array([[1]],dtype=object),'B':np.array([[1]],dtype=object),'E':np.array([[0]],dtype=object),'H':np.array([[0]],dtype=object)};return data,mat

def run():
 rows=[]
 def check(name,value):a.need(value,'control '+name);rows.append({'id':name,'pass':True})
 def rejects(name,fn):
  try:fn();got=False
  except Exception:got=True
  check(name,got)
 d,m=toy();out=a.matrices(d,m);check('all_six_generic_small_matrices',all(v['status']=='PASS_EXACT_ALL_ENTRY_CRT'for v in out.values()))
 for k in a.STAT:
  bad={n:x.copy()for n,x in m.items()};bad[k][0,0]+=1;result=a.matrices(d,bad);check('mutation_'+k,result[k]['status']!='PASS_EXACT_ALL_ENTRY_CRT')
  if k=='M':check('H_blocked_until_M_proved',result['H']['status']=='HOLD_UNVERIFIED_M_DEPENDENCY')
 bad={n:x.copy()for n,x in m.items()};bad['K'][0,0]+=int(out['K']['CRT_product']);result=a.matrices(d,bad);check('primorial_sized_corruption_rejected_by_full_bound_or_CRT',result['K']['status']!='PASS_EXACT_ALL_ENTRY_CRT')
 p=out['M'].copy();p['CRT_product']=str(2*int(p['difference_bound']));rejects('insufficient_CRT_product',lambda:a.finalize_plan(p));p=out['M'].copy();p['checks']=[];rejects('missing_prime_check',lambda:a.finalize_plan(p));rejects('unsafe_dot_overflow',lambda:a.dot_bound(1<<30,(1<<24)-3));rejects('out_of_range_prime',lambda:a.dot_bound(321,1<<24))
 decoded=a.decode_matrix({'shape':[2,2],'storage':'upper','values':['4','0','0']},(2,2),True);check('upper_row_major_unpack',np.array_equal(decoded,m['M']));rejects('wrong_packed_count',lambda:a.decode_matrix({'shape':[2,2],'storage':'upper','values':['4']},(2,2),True));rejects('wrong_storage',lambda:a.decode_matrix({'shape':[2,2],'storage':'full','values':['4','0','0','0']},(2,2),True));rejects('boolean_shape',lambda:a.decode_matrix({'shape':[True,True],'storage':'upper','values':['1']},(1,1),True));rejects('duplicate_JSON_key',lambda:a.parse_json('{"x":1,"x":2}'))
 exact,terms=a.scalar_statistics(d,m);check('trace_quadratic_norms_cancel_exactly',all(v==0 for v in exact.values()));check('different_trace_contraction',terms=={'cross':4,'trace':4,'udiag':4,'vdiag':4,'ksquare':4})
 a.verify_ceil(F(3,2),F(2),2,1);check('minimal_root_grid_proved_by_power',True);rejects('too_low_root_bound',lambda:a.verify_ceil(F(1),F(2),2,1));rejects('nonminimal_root_bound',lambda:a.verify_ceil(F(2),F(2),2,1));rejects('off_grid_root_bound',lambda:a.verify_ceil(F(7,5),F(1),2,1));a.verify_ceil(F(3,2),F(4),4,1);check('fourth_root_grid_proof',True)
 contract=json.loads((a.P/'PROFILE.json').read_text());g,b=a.derive({k:F(0)for k in['a','b','eta','r','f','g']},d['s'],1,contract);check('generic_q1_all_scalar_gates',all(g.values())and b['full_abs_error_upper']==0 and b['ambient_leading_condition_upper']==1)
 g,b=a.derive({'a':F(1),'b':F(0),'eta':F(0),'r':F(0),'f':F(0),'g':F(0)},d['s'],1,contract);check('rank_boundary_HOLD',not all(g.values())and b=={})
 for name,path in [('self',a.P),('descendant',a.P/'bad'),('ancestor',a.P.parent)]:rejects('guard_'+name,lambda path=path:a.guard(path))
 with tempfile.TemporaryDirectory(prefix='ud-c20-review-control-')as temp:
  alias=Path(temp)/'alias';alias.symlink_to(a.P,target_is_directory=True);rejects('guard_symlink',lambda:a.guard(alias/'bad'))
 return {'status':'PASS_GENERIC_ALL_STATISTIC_CRT_SCALAR_CORRUPTION_CONTROLS','rows':rows,'actual_supplied_bundles_audited':0,'new_estimator_calls':0,'physical_promotion':0}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--out',required=True);x=p.parse_args();out=a.guard(x.out);out.mkdir(parents=True,exist_ok=False)
 with(out/'CONTROLS.json').open('x')as f:json.dump(run(),f,indent=2);f.write('\n')
