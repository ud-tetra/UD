"""Supplemental validated source-target discrepancy, never replacing the main gate."""
import argparse,json
import numpy as np
from scipy.optimize import linear_sum_assignment
from flint import arb,fmpq
from bindings import P,witness
from reference import model_frame
from proof_math import up

def run(n):
 e,o=witness(n);pp,J,targets,points,sep=model_frame(e)
 with np.load(o/'PHASE_PROPOSAL.npz',allow_pickle=False) as z:angles=z['two_step_phase']
 q=len(points);assert angles.shape==(q,);pa=np.array([float(z.arg().mid()) for z in points]);ea=angles.astype(float)/2.**60;cost=abs(np.angle(np.exp(1j*(pa[:,None]-ea[None,:]))));rows,cols=linear_sum_assignment(cost);assert np.array_equal(rows,np.arange(q));bounds=[]
 for i,k in zip(rows,cols):
  d=points[i].arg()-arb(int(angles[k]))/(1<<60);bounds.append(min(up(arb(abs(d).upper()))[0],up(arb(abs(d+2*arb.pi()).upper()))[0],up(arb(abs(d-2*arb.pi()).upper()))[0]))
 b=arb(max(bounds))/(1<<100);result={'status':'VALIDATED_ASSIGNED_SOURCE_TARGET_ERROR','case':n,'circular_two_step_error_upper':[max(bounds),1<<100],'unique_disjoint_phase_matching':bool(2*b<sep),'readable_error_upper':float(b.upper()),'does_not_replace_frozen_similarity_certificate':True,'physical_promotion':0};dest=o/'DIRECT_ERROR.json';assert not dest.exists();dest.write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2));return result
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('case');a=p.parse_args();run(a.case)
