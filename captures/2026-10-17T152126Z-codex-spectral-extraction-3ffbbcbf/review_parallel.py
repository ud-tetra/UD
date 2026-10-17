"""Source-bound claim audit of the user-supplied auxiliary-monitoring appendix."""
from pathlib import Path
import json
from fractions import Fraction as F
import numpy as np
from scipy.sparse import csr_matrix
ROOT=Path(__file__).resolve().parent
def build():
 config=json.loads((ROOT/'sources'/'FROZEN_CONTRACT.json').read_text())
 p=np.load(ROOT/'sources'/'OPERATORS.npz',allow_pickle=False)
 A=csr_matrix((p['A_data'],p['A_indices'],p['A_indptr']),shape=(2640,2640))
 coordinate=int(p['obs'][0]);row=A.getrow(coordinate)
 assert coordinate==33 and int(A[33,120])==-1 and row.nnz==12
 claims=[
  {'claim':'M4096,8191 timestamps,37 preparations,18790154 readings,delta2^-20,scalar2^-23,target1893,condition<2029',
   'status':'RETAIN_WITH_CONDITIONS','reason':'Matches the primary constructor-frozen contract; bound depends on all model,error and numerical proof requirements, not on active monitoring.'},
  {'claim':'62 auxiliary diagnostic channels','status':'CORRECT_IDENTIFICATION','reason':'62 are the original history observer; diagnostics use189 outputs and six-ratio calibration needs four extra ports. No physical current or nonperturbative readout bridge is supplied.'},
  {'claim':'Port0 stationary and one-to-one port/frequency-block registry','status':'EXACT_COUNTEREXAMPLE','reason':'Port0 reads coordinate33; A[33,120]=-1. From statee120 its output derivative atzero is-1, so it is not a stationary-only port. Spectral blocks are temporal decomposition components, not individual channels.'},
  {'claim':'Per-port model residual<2^-49 follows from the contract','status':'NOT_DERIVED_AND_NOT_IMPLIED','reason':'A single scalar instrument error2^-24 is allowed by the frozen history allocation but exceeds2^-49 by2^25. Systematic preparation/model/timing terms also contribute.'},
  {'claim':'Norm(deltaGamma_Borel)<=2^-38','status':'UNDEFINED_NEW_PROPOSAL','reason':'2^-38 is the source-defined shape-statistic gate. No Borel-to-metric map, norm or propagation inequality authorizes reassigning it toGamma.'},
  {'claim':'1146-dimensional active Hankel invariant plane','status':'UNSUPPORTED_IN_THIS_CHAIN','reason':'The frozen target is1893 thresholded real history signals; no source certificate here identifies an1146-dimensional invariant plane.'},
  {'claim':'No leakage across F13^12 field boundaries','status':'NO_TRANSFER_SUPPLIED','reason':'This spectrum,absolute errors andEuclidean norms are real-valued. Finite-field splitting arithmetic supplies none of the claimed norm or measurement identifications.'},
  {'claim':'Monitoring identifies phase leakage from747 permanently hidden dimensions','status':'NO_GO_FOR_NOMINAL_HIDDEN_SECTOR','reason':'ForN=intersection ker(RA^k),A preservesN andNperp. Any skewJ supported entirely onN leaves Rexp(t(A+J))x unchanged for allx,t.747 is conditional on the nominalA,R, not permanent under arbitrary modified coupling.'},
  {'claim':'104th-order history derivative used in acquisition','status':'DISTINGUISH_IDENTIFIABILITY_FROM_SAMPLING','reason':'Degree105 minimal-polynomial/derivative-history facts do not mean the frozen8191 sampled vectors are directly measured104th derivatives.'},
  {'claim':'ACTIVE_MONITOR status and failure isolates the cause','status':'OVERSTATED','reason':'No acquisition or active hardware monitor exists in the supplied evidence. A failed gate rejects its declared contract or candidate certificate; it does not identify the physical cause.'},
  {'claim':'Physical promotion0 and tolerances are O03 controls','status':'RETAIN','reason':'Correct status boundary; it does not by itself validate the appendix equations.'}]
 out={'status':'AUDITED_CONSTRUCTOR_REVIEW_NOT_INDEPENDENT','physical_promotion':0,
  'source':'User-supplied LaTeX appendix in the2026-10-17 request; reviewed as proposal data',
  'claims':claims,'port0_counterexample':{'readout_coordinate':33,'initial_state_coordinate':120,
   'initial_output':0,'initial_derivative':-1,'row_nonzero_count':12},
  'residual_gate_counterexample':{'allowed_instrument_scalar_error':[1,2**24],'proposed_gate':[1,2**49],'violation_factor':2**25},
  'hidden_generator_blind_skew_parameters':747*746//2,
  'latex_only_notes':['geometry command requires geometry package','F macro is undefined as supplied','Transport backslashes andHTML space entities require cleanup before compilation'],
  'disposition':'Retain the conditional acquisition arithmetic; replace the leakage-sieve and port-registry interpretation with the corrected real projection-tail certificate.'}
 (ROOT/'PARALLEL_APPENDIX_REVIEW.json').write_text(json.dumps(out,indent=2)+'\n')
 return out
if __name__=='__main__':print(json.dumps({k:v for k,v in build().items() if k!='claims'}))
