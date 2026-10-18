import unittest,json,tempfile
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from flint import ctx
from bindings import P,checked,sha
from frame_math import span_residual,assemble_span
from numeric_math import encode
ctx.prec=512
class SpanTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.c=json.loads((P/'inputs/PHASE_STABILITY_CERTIFICATE.json').read_text())['constants']
  cls.m={k:[0,1] for k in ['basis_orthogonality_upper','frame_span_residual_upper','shift_residual_upper','inverse_residual_upper','eigenpair_residual_upper','argument_output_error_upper']};cls.m['inverse_norm_upper']=[1,1]
 def test_real_complex_frame_change_scale(self):
  t=np.array([[1,0,0],[0,.5,-.5j],[0,.5,.5j]])
  self.assertTrue(np.array_equal(np.linalg.eigvalsh(t.conj().T@t),[.5,.5,1.]))
 def test_exact_span_and_corrupted_reduction(self):
  u=np.eye(3,dtype=float);pp=(np.eye(3,dtype=np.int64)*(1<<60));d=u.copy()
  good,_=span_residual(pp,u,d);self.assertTrue(good<1e-16)
  d[0,0]=2.;bad,_=span_residual(pp,u,d);self.assertTrue(bad>=1)
 def test_amplitude_changes_do_not_change_column_span(self):
  from proof_math import fm
  f=np.array([[1,0],[1,1],[1,2]],dtype=object);c=np.array([[2,1],[0,3]],dtype=object);scaled=c.copy();scaled[0,:]+=np.array([7,-4],dtype=object)
  self.assertEqual(fm(f).rank(),fm(f@c).rank());self.assertEqual(fm(f@c).rank(),fm(np.c_[f@c,f@scaled]).rank())
 def test_zero_residual_baseline_certifies(self):self.assertTrue(assemble_span(self.m,self.c)['unique_reference_phase_matching'])
 def test_wrong_span_refuses(self):
  m=self.m.copy();m['frame_span_residual_upper']=[100,1]
  with self.assertRaises(AssertionError):assemble_span(m,self.c)
 def test_singular_basis_refuses(self):
  m=self.m.copy();m['basis_orthogonality_upper']=[1,1]
  with self.assertRaises(AssertionError):assemble_span(m,self.c)
 def test_shift_or_inverse_or_argument_refuses(self):
  for k,v in [('shift_residual_upper',[1,10]),('inverse_residual_upper',[1,1]),('argument_output_error_upper',[1,100])]:
   m=self.m.copy();m[k]=v
   with self.assertRaises(AssertionError):assemble_span(m,self.c)
 def test_bit_exact_subnormal_and_tampered_source_refusal(self):
  a=np.array([.1,float.fromhex('0x0.0000000000001p-1022')]);n,b=encode(a)
  for x,y in zip(a,n):self.assertEqual(F(int(y),1<<b),F(*float(x).as_integer_ratio()))
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'witness';p.write_bytes(b'original');h=sha(p);checked(p,h);p.write_bytes(b'corrupted')
   with self.assertRaises(AssertionError):checked(p,h)
if __name__=='__main__':unittest.main()
