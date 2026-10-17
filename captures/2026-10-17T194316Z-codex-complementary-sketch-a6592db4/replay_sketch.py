"""Portable exact residual replay of the supplied small-Gram certificates."""
from pathlib import Path
import json
import numpy as np
from flint import ctx,arb,fmpq
from proof_math import fm,arr,norm_exact,up,down
ctx.prec=512
P=Path(__file__).resolve().parent

def replay_arrays(gg,qn,dn,certificate,rule):
 assert gg.shape==(161,161) and qn.shape==(161,161) and dn.shape==(161,)
 assert np.array_equal(gg,gg.T)
 assert np.all(dn[:-1]>=dn[1:])
 G=fm(gg);q=fm(qn)
 eta=norm_exact(arr(q.transpose()*q)-np.eye(161,dtype=object)*(1<<120),120)
 assert eta<1,'Orthogonality unresolved'
 R=arr(G*q)-qn.astype(object)*dn.astype(object)[None,:]*(1<<70)
 res=norm_exact(R,170);gnorm=norm_exact(gg,110);s=(1+eta).sqrt();dist=eta/(1+(1-eta).sqrt())
 radius=gnorm*eta+res*s+arb(max(abs(int(x)) for x in dn))/(1<<40)*dist*(s+1)
 assert up(eta)==certificate['eigenvector_orthogonality_defect_upper']
 assert up(res)==certificate['eigenpair_residual_upper']
 assert up(radius)==certificate['gram_eigenvalue_radius_upper']
 cut=arb(fmpq(*rule['cutoff']));above=[];below=[]
 for i,x in enumerate(dn):
  center=arb(int(x))/(1<<40)
  if center-radius>cut*cut:above.append(i)
  elif center+radius<cut*cut:below.append(i)
  else:raise AssertionError('Cutoff classification unresolved')
 count=len(above);assert above==list(range(count)) and count==certificate['above_cutoff_count']
 assert len(above)+len(below)==161
 lo=(arb(int(dn[count-1]))/(1<<40)-radius).sqrt();hi=(arb(int(dn[0]))/(1<<40)+radius).sqrt()
 tail=(arb(int(dn[count]))/(1<<40)+radius).sqrt() if count<161 else arb(0)
 assert down(lo)==certificate['retained_sigma_lower']
 assert up(hi)==certificate['largest_sigma_upper']
 assert up(tail)==certificate['discarded_sigma_upper']
 assert up(hi/lo)==certificate['retained_condition_upper']
 noise=arb(fmpq(*rule['noise_squared_ceiling'])).sqrt()
 assert bool(count==105 and lo-noise>cut and tail+noise<cut)==certificate['uniform_105_separation_in_error_ball']
 return count

def load_case(directory):
 d=Path(directory)
 with np.load(d/'EXACT_SKETCH_GRAM.npz',allow_pickle=False) as z:gg=z['integers_decimal'].astype(object)
 gg=np.array([[int(x) for x in row] for row in gg],dtype=object)
 with np.load(d/'EIGEN_PROPOSAL.npz',allow_pickle=False) as z:qn=z['Q'];dn=z['eigenvalues']
 c=json.loads((d/'SKETCH_CERTIFICATE.json').read_text());rule=json.loads((P/'inputs/SKETCH_RULE.json').read_text())
 return gg,qn,dn,c,rule

def run():
 results={}
 for d in sorted((P/'results').glob('sketch-*')):
  if not (d/'SKETCH_CERTIFICATE.json').exists():continue
  results[d.name]=replay_arrays(*load_case(d))
 assert len(results)==5
 return {'status':'PASS','exact_small_Gram_replays':results,'raw_record_Gram_recomputation_claimed':False,'scope':'Stored exact Gram and dyadic eigensystem proof replay; source-record-to-Gram hash binding comes from frozen execution receipts','physical_promotion':0,'independent_review':'pending; same constructor replay only'}
if __name__=='__main__':
 r=run();(P/'SKETCH_REPLAY_RESULTS.json').write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2))
