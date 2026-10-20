"""Synthetic corruption and CRT proof controls, never production input execution."""
import argparse,json,tempfile
from pathlib import Path
from fractions import Fraction as F
import numpy as np
import audit as a

def toy():
 N=np.array([[1,-2],[3,4]],dtype=np.int64);U=np.array([[.5,.25],[.125,-.5]],dtype=np.float64);V=np.array([[.25,0.],[.5,.5]],dtype=np.float64);s=np.array([2.,.5],dtype=np.float64)
 Ui,bU=a.encoded(U);Vi,bV=a.encoded(V);si,bS=a.encoded(s);bits=max(55+bU,bV+bS);D=np.zeros((2,2),dtype=object)
 for i in range(2):
  for j in range(2):
   exact=sum(F(int(N[k,i]),1<<55)*F(*float(U[k,j]).as_integer_ratio())for k in range(2))-F(*float(V[i,j]).as_integer_ratio())*F(*float(s[j]).as_integer_ratio());value=exact*(1<<bits);a.need(value.denominator==1,'toy exactly scaled');D[i,j]=value.numerator
 return N,Ui,Vi,si,D,bU,bV,bS,bits

def checked(values):
 N,U,V,s,D,bU,bV,bS,bD=values;p=a.plan(N,U,V,s,D,bU,bV,bS,bD);p.update(bU=bU,bV=bV,bS=bS);checks=a.residues(N,U,V,s,D,p);return p,checks

def run():
 rows=[]
 def check(name,condition):a.need(condition,'control '+name);rows.append({'id':name,'pass':True})
 def rejects(name,fn):
  try:fn();got=False
  except Exception:got=True
  check(name,got)
 v=toy();p,c=checked(v);a.verify_crt(p,c);check('all_entry_signed_toy_equality',all(x['matching_entries']==4 for x in c))
 broken=v[4].copy();broken[0,0]+=1;q,cc=checked(v[:4]+(broken,)+v[5:]);rejects('single_entry_corruption',lambda:a.verify_crt(q,cc));check('all_declared_primes_ran_after_mismatch',len(cc)==len(q['primes']))
 broken=v[4].copy();broken[0,0]+=p['product'];q,cc=checked(v[:4]+(broken,)+v[5:]);rejects('primorial_sized_corruption',lambda:a.verify_crt(q,cc));check('large_corruption_expands_bound_and_prime_prefix',len(q['primes'])>len(p['primes']))
 bad=p.copy();bad['product']=2*bad['bound'];rejects('insufficient_or_inconsistent_CRT_product',lambda:a.verify_crt(bad,c))
 check('distinct_proved_small_prime_prefix',len(p['primes'])==len(set(p['primes']))and all(a.is_prime(z)and z<(1<<24)for z in p['primes']))
 check('composite_refused',not a.is_prime(15));rejects('overflow_inner_length_refused',lambda:a.safe_dot_bound(1<<30,(1<<24)-3));rejects('outside_prime_range_refused',lambda:a.safe_dot_bound(8191,1<<24))
 rejects('wrong_denominator_refused',lambda:a.plan(*v[:5],*v[5:8],v[8]+1))
 D=v[4];sq=F(sum(int(x)**2 for x in D.flat),1<<(2*v[8]));root={'exact_Frobenius_squared':a.pair(sq),'norm_upper':['10','1']};a.exact_norm(D,v[8],root);check('exact_norm_positive_bound',True);rejects('false_zero_norm_upper',lambda:a.exact_norm(D,v[8],root|{'norm_upper':['0','1']}));rejects('false_exact_norm_squared',lambda:a.exact_norm(D,v[8],root|{'exact_Frobenius_squared':['0','1']}))
 values=np.array([-.5,0.,np.nextafter(0.,1.)],dtype=np.float64);encoded,bits=a.encoded(values);check('independent_ratios_include_subnormal',all(F(int(n),1<<bits)==F(*float(x).as_integer_ratio())for n,x in zip(encoded,values)))
 for name,path in [('self',a.P),('descendant',a.P/'bad'),('ancestor',a.P.parent)]:rejects('guard_'+name,lambda path=path:a.guard(path))
 with tempfile.TemporaryDirectory(prefix='ud-c18-guard-')as td:
  alias=Path(td)/'alias';alias.symlink_to(a.P,target_is_directory=True);rejects('guard_resolved_symlink',lambda:a.guard(alias/'bad'))
 return {'status':'PASS_SYNTHETIC_DETERMINISTIC_CRT_AND_CORRUPTION_CONTROLS','rows':rows,'production_matrices_checked':0,'new_estimator_calls':0,'physical_promotion':0}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--out',required=True);arg=p.parse_args();out=a.guard(arg.out);out.mkdir(parents=True,exist_ok=False)
 with(out/'CONTROLS.json').open('x')as f:json.dump(run(),f,indent=2);f.write('\n')
