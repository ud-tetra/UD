import json
from pathlib import Path
import numpy as np
from scipy.linalg import svdvals
P=Path(__file__).resolve().parent;rows=[]
for case in ['clean','coherent_dc']:
 with np.load(P/'results'/('old-'+case)/'PROPOSAL.npz') as z:C=z['coeff'];theta=z['theta']
 ranks=[]
 for j in range(len(theta)+1):
  B=C[0].reshape(62,37)/2.**60 if j==0 else(C[2*j-1].reshape(62,37)-1j*C[2*j].reshape(62,37))/2.**61
  s=svdvals(B,check_finite=False);ranks.append(int(np.count_nonzero(s>s[0]*2.**-30)))
 rows.append({'case':case,'stationary_rank_at_old_relative_cutoff':ranks[0],'total_real_rank_at_old_relative_cutoff':ranks[0]+2*sum(ranks[1:])})
(P/'OLD_SPATIAL_RANK_DIAGNOSTIC.json').write_text(json.dumps(rows,indent=2));print(rows)
