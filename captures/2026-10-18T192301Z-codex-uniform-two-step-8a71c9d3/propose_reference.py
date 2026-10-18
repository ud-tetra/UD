"""Untrusted verifier-only source-frame reduction, separate from record-only adapter."""
import argparse,numpy as np
from bindings import P,witness
from reference import model_frame
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('case');a=p.parse_args();e,o=witness(a.case)
 with np.load(o/'BASIS_A.npz',allow_pickle=False) as z:ua=z['basis']
 with np.load(o/'BASIS_B.npz',allow_pickle=False) as z:ub=z['basis']
 pp,J,targets,points,sep=model_frame(e);U=np.r_[ua,ub];D=U.T@(pp.astype(float)/2.**60);K=np.linalg.inv(D);dest=o/'SOURCE_WITNESS.npz';assert not dest.exists();np.savez_compressed(dest,reduction=D,inverse=K)
