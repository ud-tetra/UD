"""One auxiliary inverse proposal, not a state estimator or exact arithmetic claim."""
import argparse,json,platform
import numpy as np
from common import P,freeze,sha,check_evidence
def main():
 p=argparse.ArgumentParser();p.add_argument('--evidence',required=True);args=p.parse_args();freeze();check_evidence(args.evidence)
 with np.load(args.evidence+'/C.npz',allow_pickle=False) as z:C=z['coefficient']
 M=np.linalg.solve(C@C.T,np.eye(209));assert np.isfinite(M).all()
 dest=P/'INVERSE_PROPOSAL.npz';assert not dest.exists();np.savez_compressed(dest,inverse=M)
 (P/'PROPOSAL_FREEZE.json').write_text(json.dumps({'sha256':sha(dest),'proposal':'one untrusted binary64 LU solve for inverse of C C^T; K subsequently formed exactly','python':platform.python_version(),'numpy':np.__version__,'outcome_tuning':False,'physical_promotion':0},indent=2))
 print(json.dumps({'status':'AUXILIARY_PROPOSAL_FROZEN','sha256':sha(dest)}),flush=True)
if __name__=='__main__':main()
