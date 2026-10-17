"""Adversarial contract/receipt checks. Tiny fixtures are not physical or600-cell data."""
from pathlib import Path
from fractions import Fraction as F
import copy,csv,json,tempfile,unittest,uuid
import numpy as np
from audit_run import audit_run,audit_history,sha,exact,evaluate_declared_intervals
from exact_encoding import quantize,history_bytes,diagnostic_record
ROOT=Path(__file__).resolve().parent
def pair(x):x=F(x);return [x.numerator,x.denominator]

class ProtocolTests(unittest.TestCase):
 def setUp(self):
  self.c=json.loads((ROOT/'FROZEN_CONTRACT.json').read_text())
  self.r=json.loads((ROOT/'RUN_RECEIPT_TEMPLATE.json').read_text())
 def small(self,p):
  c=copy.deepcopy(self.c);fmt=c['data_format'];fmt['shape']=[2,3,2];fmt['bytes']=12*8
  fmt['index_ledger']['rows']=6
  cp=p/'contract.json';cp.write_text(json.dumps(c))
  data=p/fmt['filename'];np.arange(12,dtype='<i8').tofile(data)
  ledger=p/'sample_index.csv'
  with ledger.open('w',newline='') as stream:
   w=csv.writer(stream);w.writerow(fmt['index_ledger']['columns'])
   for k in range(6):w.writerow([k//3,k%3,'fixture-'+str(k)])
  return cp,c,data,ledger
 def complete(self,p):
  cp,c,data,ledger=self.small(p);r=copy.deepcopy(self.r)
  r.update(protocol_sha256=sha(cp),run_id=str(uuid.UUID(int=1)),acquisition_executed=True,
   started_utc='2026-10-17T12:00:00+00:00',completed_utc='2026-10-17T13:00:00+00:00')
  for k in ['raw_source_sha256','processing_implementation_sha256','review_receipt','family_and_stability_receipt',
   'diagnostic_pass_receipt','shape_gate_pass_receipt','six_ratio_gate_receipt','spectral_proof_receipt']:r[k]='0'*64
  r['normalized_data_sha256']=sha(data);r['sample_index_sha256']=sha(ledger)
  for k,v in c['budgets'].items():
   # Values are synthetic declarations, deliberately not real evidence.
   r['error_evidence'][k]={'unit':v['unit'],'reported_upper':[0,1],'evidence_sha256':'0'*64,'method':'SYNTHETIC FIXTURE, not evidence'}
  s=c['spectral_rule'];r['signature_evaluation']={
   'sigma1':[[0,1],s['computed_sigma_1_upper']],
   'sigma1893':[s['computed_sigma_1893_lower'],s['computed_sigma_1_upper']],
   'sigma1894':[[0,1],s['computed_sigma_1894_upper']],
   'numerical_operator_error_upper':s['numerical_operator_error_ceiling']}
  return cp,c,r,data,ledger

 def test_empty_template_does_not_pass(self):
  out=audit_run(self.r,ROOT/'FROZEN_CONTRACT.json',ROOT)
  self.assertEqual(out['research_status'],'NOT_EXECUTED');self.assertFalse(out['empirical_certification'])

 def test_wrong_contract_hash_and_changed_rank_reject(self):
  for k,v in [('protocol_sha256','0'*64),('selected_target_count',1519)]:
   r=copy.deepcopy(self.r);r[k]=v
   self.assertEqual(audit_run(r,ROOT/'FROZEN_CONTRACT.json',ROOT)['structural_status'],'REJECTED')

 def test_scalar_and_vector_errors_cannot_be_substituted(self):
  self.r['error_evidence']['history_instrument']['reported_upper']=[1,2**20]
  out=audit_run(self.r,ROOT/'FROZEN_CONTRACT.json',ROOT)
  self.assertIn('error ceiling exceeded: history_instrument',out['problems'])
  self.r['error_evidence']['history_instrument']['reported_upper']=[0,1]
  self.r['error_evidence']['history_instrument']['unit']='normalized_state_l2'
  self.assertEqual(audit_run(self.r,ROOT/'FROZEN_CONTRACT.json',ROOT)['structural_status'],'REJECTED')

 def test_strict_ratio_boundary_rejects_equality(self):
  self.r['error_evidence']['six_ratio_error']['reported_upper']=[1,2**39]
  self.assertIn('error ceiling exceeded: six_ratio_error',audit_run(self.r,ROOT/'FROZEN_CONTRACT.json',ROOT)['problems'])

 def test_reused_raw_record_and_missing_index_reject(self):
  with tempfile.TemporaryDirectory() as tmp:
   p=Path(tmp);cp,c,data,ledger=self.small(p)
   with ledger.open(newline='') as stream:rows=list(csv.reader(stream))
   rows[-1][2]=rows[1][2]
   with ledger.open('w',newline='') as out:csv.writer(out).writerows(rows)
   o=audit_history(p,c['data_format'],sha(data),sha(ledger));self.assertTrue(o['problems'])
   with ledger.open('w',newline='') as out:csv.writer(out).writerows(rows[:-1])
   o=audit_history(p,c['data_format'],sha(data),sha(ledger));self.assertIn('indexed record count mismatch',o['problems'])

 def test_tampered_data_and_truncation_reject(self):
  with tempfile.TemporaryDirectory() as tmp:
   p=Path(tmp);cp,c,data,ledger=self.small(p);h=sha(data)
   data.write_bytes(bytes(96));self.assertIn('normalized dataset hash mismatch',audit_history(p,c['data_format'],h,sha(ledger))['problems'])
   data.write_bytes(bytes(88));self.assertIn('normalized dataset byte count mismatch',audit_history(p,c['data_format'],sha(data),sha(ledger))['problems'])

 def test_int64_min_does_not_bypass_range_gate(self):
  with tempfile.TemporaryDirectory() as tmp:
   p=Path(tmp);cp,c,data,ledger=self.small(p);z=np.arange(12,dtype='<i8');z[0]=-(2**63);z.tofile(data)
   out=audit_history(p,c['data_format'],sha(data),sha(ledger))
   self.assertIn('normalized amplitude exceeds conservative absolute bound2',out['problems'])

 def test_forged_complete_receipts_never_become_empirical_pass(self):
  with tempfile.TemporaryDirectory() as tmp:
   p=Path(tmp);cp,c,r,data,ledger=self.complete(p);out=audit_run(r,cp,p)
   self.assertEqual(out['structural_status'],'COMPLETE')
   self.assertEqual(out['declared_interval_result'],'CONDITIONAL_SIGNATURE_CONSISTENT')
   self.assertEqual(out['research_status'],'HOLD_PENDING_EVIDENCE_AND_PROOF_REVIEW')
   self.assertFalse(out['empirical_certification'])

 def test_spectral_threshold_tie_remains_inconclusive(self):
  with tempfile.TemporaryDirectory() as tmp:
   p=Path(tmp);cp,c,r,_,_=self.complete(p);s=r['signature_evaluation']
   s['sigma1893'][0]=c['spectral_rule']['selection_threshold']
   self.assertEqual(evaluate_declared_intervals(s,c['spectral_rule']),'INCONCLUSIVE')

 def test_certified_tail_contradiction_is_detected(self):
  with tempfile.TemporaryDirectory() as tmp:
   p=Path(tmp);cp,c,r,_,_=self.complete(p);s=r['signature_evaluation']
   tail=exact(c['spectral_rule']['computed_sigma_1894_upper'])
   s['sigma1894']=[pair(2*tail),pair(2*tail)]
   self.assertEqual(evaluate_declared_intervals(s,c['spectral_rule']),'CONTRACT_CONTRADICTION_IF_ENCLOSURES_VALID')

 def test_float_and_boolean_bounds_reject(self):
  for v in [[.5,1],[True,1],[1,0],[1,-2]]:
   with self.assertRaises(ValueError):exact(v)
  with self.assertRaises(ValueError):history_bytes([2**64,1])

 def test_exact_rounding_ties_and_diagnostic_integer_width(self):
  for n in range(-100,101):
   for bits in [0,3,48,64]:
    x=F(n,7*2**bits);q=quantize(pair(x),bits)
    self.assertLessEqual(abs(F(q,2**bits)-x),F(1,2**(bits+1)))
  self.assertEqual([quantize([n,2],0) for n in [-5,-3,-1,1,3,5]],[-2,-2,0,0,2,2])
  z=diagnostic_record([1,1]);self.assertEqual(int(z['numerator_decimal']),2**64)
  self.assertGreater(int(z['numerator_decimal']),2**63-1)

 def test_frozen_computation_gap_and_all_error_components(self):
  s=self.c['spectral_rule'];T=exact(s['selection_threshold'])
  self.assertGreater(exact(s['computed_sigma_1893_lower']),T)
  self.assertLess(exact(s['computed_sigma_1894_upper']),T)
  self.assertLess(exact(s['computed_sigma_1_upper'])/exact(s['computed_sigma_1893_lower']),2029)
  components=['history_instrument','history_blank_correction','history_processing','history_quantization']
  u=sum(exact(self.c['budgets'][k]['upper_ceiling']) for k in components)
  self.assertLess(62*u*u,F(1,2**40))

if __name__=='__main__':unittest.main()
