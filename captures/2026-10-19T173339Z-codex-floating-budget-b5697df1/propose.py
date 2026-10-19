"""Three untrusted auxiliary frame-coordinate proposals; no estimator refit."""
import argparse,json,platform
import numpy as np
from pathlib import Path
from common import P,freeze,check_evidence,sha
def main():
 p=argparse.ArgumentParser();p.add_argument('--evidence',type=Path,required=True);a=p.parse_args();f=freeze();check_evidence(a.evidence)
 U0=np.vstack([np.load(a.evidence/('U0_'+k+'.npz'),allow_pickle=False)['basis'] for k in ['A','B']]);G=U0.T@U0
 out=P/'witnesses';out.mkdir(exist_ok=False);files={}
 for n in f['cases']:
  U1=np.vstack([np.load(a.evidence/f'{n}_F{k}.npz',allow_pickle=False)['left'] for k in range(3)])[:,:209]
  X=np.linalg.solve(G,U0.T@U1);assert np.isfinite(X).all();q=out/(n+'.npz');np.savez_compressed(q,alignment=X);files[str(q.relative_to(P))]=sha(q)
 r={'status':'AUXILIARY_FRAMES_FROZEN_BEFORE_EXACT_RESIDUAL_EVALUATION','files':files,'python':platform.python_version(),'numpy':np.__version__,'known_prior_outputs':True,'source_budget_ceiling_already_known':True,'numerical_exactness_assumed':False,'new_state_estimator_runs':0,'auxiliary_LU_proposals':3,'physical_promotion':0};(P/'PROPOSAL_FREEZE.json').write_text(json.dumps(r,indent=2));print(json.dumps(r),flush=True)
if __name__=='__main__':main()
