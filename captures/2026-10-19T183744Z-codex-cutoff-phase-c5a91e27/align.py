"""Untrusted auxiliary coordinates; never alter U, T, order, or the fixed budget."""
import argparse,json
from pathlib import Path
import numpy as np
from scipy.linalg import solve
from common import P,freeze,check_source,sha

def propose(source):
 freeze();check_source(source);runs=json.loads((P/'RUN_EXECUTIONS.json').read_text());out=P/'alignments';out.mkdir(exist_ok=False);U0=np.vstack([np.load(source/('U0_'+k+'.npz'),allow_pickle=False)['basis'] for k in ['A','B']]);G=U0.T@U0
 for run in runs['rows']:
  if run['learned_order']!=209 or run['execution_status']!='COMPLETED':continue
  case=P/'results'/run['case']
  for n,h in run['numeric_witnesses'].items():assert sha(case/n)==h
  U=np.vstack([np.load(case/f'U_{k}.npz',allow_pickle=False)['basis'] for k in range(3)]);X=solve(G,U0.T@U,assume_a='gen',check_finite=False);np.savez_compressed(out/(run['case']+'.npz'),alignment=X)
 receipt=dict(status='UNTRUSTED_AUXILIARY_COORDINATES_FROZEN_BEFORE_EXACT_MEASUREMENT',files={str(x.relative_to(P)):sha(x) for x in sorted(out.glob('*.npz'))},run_executions_sha256=sha(P/'RUN_EXECUTIONS.json'),data_freeze_sha256=sha(P/'DATA_FREEZE.json'),physical_promotion=0);assert not(P/'ALIGNMENT_FREEZE.json').exists();(P/'ALIGNMENT_FREEZE.json').write_text(json.dumps(receipt,indent=2))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--source',type=Path,required=True);propose(p.parse_args().source)
