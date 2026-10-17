"""Exact decoder checks, including the new row-local static receipt."""
import unittest,json
from fractions import Fraction as F
from optimized_gate import ROOT,spec,assess_epoch

class GateTests(unittest.TestCase):
 def fixture(self,profile='recommended'):
  d=json.loads((ROOT/'sources/PROBE_DESIGN.json').read_text());m,*_=spec(profile)
  Y=[[[0]*189 for _ in range(260)] for _ in range(m+1)]
  for ri,r in enumerate(d['observed_coordinates']):
   cc=d['colors'][r];Y[0][cc][ri]=F(1,d['preparation_denominators'][cc])
  return d,Y
 def test_local_readout_rejected(self):
  d,Y=self.fixture();r=4;j=0;cc=d['colors'][j];ri=d['observed_coordinates'].index(r)
  Y[0][cc][ri]+=F(1,2**40)/d['preparation_denominators'][cc]
  self.assertEqual(assess_epoch(Y)['decision'],'REJECT_JOINT_CONTRACT')
 def test_pair_filter_exact_derivative(self):
  d,Y=self.fixture();m,h,eps,*_=spec();r=4;t=0;ri=d['observed_coordinates'].index(r)
  data=json.loads((ROOT/'MATCHED_FILTER_DESIGN.json').read_text())
  rec=next(x for x in data['records'] if x['row']==r and x['partner']==t)
  amplitude=F(1,2**42)
  for j,sign in zip(rec['exclusive_columns'],rec['exclusive_signs']):
   cc=d['colors'][j];q=d['preparation_denominators'][cc]
   for k in range(1,m+1):Y[k][cc][ri]+=sign*amplitude*k*h/q
  out=assess_epoch(Y)
  score=next(x for x in out['scores'] if x['row']==r and x['partner']==t)
  self.assertEqual(F(*score['score']),amplitude)
  self.assertIn([r,t],out['filters_rejected'])
 def test_row_gate_has_independent_work(self):
  d,Y=self.fixture();data=json.loads((ROOT/'MATCHED_FILTER_DESIGN.json').read_text());eps=spec()[2]
  r=min(d['observed_coordinates'],key=lambda r:F(*data['row_gate_factors'][str(r)]))
  ri=d['observed_coordinates'].index(r);j=d['readout_stencils'][str(r)][0];cc=d['colors'][j]
  amplitude=F(20)*eps
  self.assertLess(F(*data['row_gate_factors'][str(r)])*eps,amplitude)
  Y[0][cc][ri]+=amplitude/d['preparation_denominators'][cc]
  out=assess_epoch(Y)
  self.assertLess(F(*out['static_squared']),(46*eps)**2)
  self.assertIn(r,out['static_rows_rejected'])
 def test_strict_profile(self):
  d,Y=self.fixture('strict');r=4;j=0;cc=d['colors'][j];ri=d['observed_coordinates'].index(r)
  Y[0][cc][ri]+=F(1,2**40)/d['preparation_denominators'][cc]
  self.assertEqual(assess_epoch(Y,'strict')['decision'],'REJECT_JOINT_CONTRACT')
 def test_float_rejected(self):
  d,Y=self.fixture();Y[0][0][0]=0.1
  with self.assertRaises(ValueError):assess_epoch(Y)
 def test_shape_rejected(self):
  with self.assertRaises(ValueError):assess_epoch([])

if __name__=='__main__':unittest.main()
