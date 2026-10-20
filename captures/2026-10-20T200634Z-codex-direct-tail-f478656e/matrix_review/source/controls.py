"""Pure synthetic all-entry tail-CRT corruption and scalar-enclosure controls."""
import argparse,json,tempfile
from pathlib import Path
from fractions import Fraction as F
import numpy as np
import audit as a

def toy():
 N=np.array([[1,-2],[3,4],[-1,5]],dtype=np.int64);V=np.array([[.5,.125],[-.25,.5]],dtype=np.float64);Vi,bV=a.encoded(V);E=np.array([[-44,-4],[-4,-47]],dtype=object);H=np.array([[276,-246],[-246,771]],dtype=object);return N,Vi,E,H,bV

def checked(v):
 p=a.plan(*v);c=a.residues(*v[:4],p);return p,c

def run():
 rows=[]
 def check(name,value):a.need(value,'control '+name);rows.append({'id':name,'pass':True})
 def rejects(name,fn):
  try:fn();got=False
  except Exception:got=True
  check(name,got)
 v=toy();p,c=checked(v);a.verify_crt(p,c);check('signed_tail_toy_both_full_matrices_match',all(x[k]['matching_entries']==4 for x in c for k in['E','H']))
 E=v[2].copy();E[0,1]+=1;q,cc=checked((v[0],v[1],E,v[3],v[4]));rejects('one_E_entry_corruption',lambda:a.verify_crt(q,cc))
 H=v[3].copy();H[0,0]+=1;q,cc=checked((v[0],v[1],v[2],H,v[4]));rejects('one_H_entry_corruption',lambda:a.verify_crt(q,cc));check('all_primes_and_both_matrices_checked_after_corruption',len(cc)==len(q['primes'])and all(set(['E','H'])<=set(x)for x in cc))
 H=v[3].copy();H[0,0]+=p['product'];q,cc=checked((v[0],v[1],v[2],H,v[4]));rejects('primorial_H_corruption',lambda:a.verify_crt(q,cc));check('primorial_corruption_forces_longer_prefix',len(q['primes'])>len(p['primes']))
 q,cc=checked((v[0],v[1],v[2],v[3],v[4]+1));rejects('wrong_V_scale_identity_refused',lambda:a.verify_crt(q,cc))
 bad=p|{'product':2*p['bound']};rejects('insufficient_or_inconsistent_product',lambda:a.verify_crt(bad,c));check('common_B_dominates_E_and_H',p['bound']==max(p['BE'],p['BH']))
 check('distinct_trial_proved_small_primes',len(set(p['primes']))==len(p['primes'])and all(a.is_prime(z)and z<(1<<24)for z in p['primes']));check('composite_refused',not a.is_prime(15));rejects('overflow_refused',lambda:a.safe_dot_bound(1<<30,(1<<24)-3));rejects('outside_prime_range_refused',lambda:a.safe_dot_bound(8191,1<<24))
 # Orthonormal V=I gives E=0 and H=N^TN for a valid positive-rank scalar toy.
 E=np.zeros((2,2),dtype=object);H=np.array([[11,5],[5,45]],dtype=object);w={'exact_V_gram_defect_F_squared':['0','1'],'exact_tail_output_gram_F_squared':a.pair(F(2196,1<<220)),'etaV_upper':['0','1'],'tail_output_norm_upper':['1','1'],'tail_sigma210_upper':['1','1']};a.scalar_bounds(E,H,0,w);check('scalar_exact_denominators_and_enclosures',True)
 rejects('false_E_norm_upper',lambda:a.scalar_bounds(v[2],v[3],v[4],{'exact_V_gram_defect_F_squared':a.pair(a.norm_squared(v[2],2*v[4])),'exact_tail_output_gram_F_squared':a.pair(a.norm_squared(v[3],2*(55+v[4]))),'etaV_upper':['0','1'],'tail_output_norm_upper':['1','1'],'tail_sigma210_upper':['1','1']}))
 rejects('false_fourthroot_upper',lambda:a.scalar_bounds(E,H,0,w|{'tail_output_norm_upper':['0','1']}));rejects('rank_boundary_eta_one',lambda:a.scalar_bounds(E,H,0,w|{'etaV_upper':['1','1']}));rejects('insufficient_sigma_quotient',lambda:a.scalar_bounds(E,H,0,w|{'tail_sigma210_upper':['0','1']}));rejects('false_exact_H_squared',lambda:a.scalar_bounds(E,H,0,w|{'exact_tail_output_gram_F_squared':['0','1']}))
 for name,path in [('self',a.P),('descendant',a.P/'bad'),('ancestor',a.P.parent)]:rejects('guard_'+name,lambda path=path:a.guard(path))
 with tempfile.TemporaryDirectory(prefix='ud-c19-guard-')as td:
  alias=Path(td)/'alias';alias.symlink_to(a.P,target_is_directory=True);rejects('guard_resolved_symlink',lambda:a.guard(alias/'bad'))
 return {'status':'PASS_SYNTHETIC_TAIL_CRT_CORRUPTION_AND_SCALAR_CONTROLS','rows':rows,'production_matrices_checked':0,'new_estimator_calls':0,'physical_promotion':0}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--out',required=True);arg=p.parse_args();out=a.guard(arg.out);out.mkdir(parents=True,exist_ok=False)
 with(out/'CONTROLS.json').open('x')as f:json.dump(run(),f,indent=2);f.write('\n')
