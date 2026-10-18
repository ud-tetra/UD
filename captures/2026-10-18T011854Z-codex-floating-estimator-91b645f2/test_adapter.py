import unittest,json
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from flint import ctx
from proof_math import fm,up
from numeric_math import encode,encode_complex,diffnorm,complex_residual,cmul,assemble
ctx.prec=512
P=Path(__file__).resolve().parent
class AdapterTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.cert=json.loads((P/'results/clean/FLOAT_CERTIFICATE.json').read_text());cls.c=json.loads((P/'inputs/PHASE_STABILITY_CERTIFICATE.json').read_text())['constants'];cls.c['discovery_cutoff']=json.loads((P/'inputs/SKETCH_RULE.json').read_text())['cutoff']
  with np.load(P/'results/clean/FLOAT_WITNESS.npz',allow_pickle=False) as z:cls.w={k:z[k] for k in z.files}
 def test_exact_float_encoding_including_subnormal(self):
  a=np.array([[0.1,-0.25],[0.,float.fromhex('0x0.0000000000001p-1022')]],dtype=float);n,b=encode(a)
  for x,y in zip(a.flat,n.flat):self.assertEqual(F(int(y),1<<b),F(*float(x).as_integer_ratio()))
 def test_singular_basis_gate_refuses(self):
  m=self.cert['metrics'].copy();m['basis_orthogonality_upper']=[1,1]
  with self.assertRaises(AssertionError):assemble(m,self.c)
 def test_perturbed_actual_shift_refuses(self):
  u,bu=encode(self.w['basis']);t,bt=encode(self.w['shift']);t=t.copy();t[0,0]+=1<<(bt-7)
  r,_=diffnorm(fm(u[1:]),bu,fm(u[:-1])*fm(t),bu+bt);m=self.cert['metrics'].copy();m['shift_residual_upper']=up(r)
  with self.assertRaises(AssertionError):assemble(m,self.c)
 def test_perturbed_actual_eigenvalue_refuses(self):
  v,vi,bv=encode_complex(self.w['eigenvectors']);l,li,bl=encode_complex(self.w['eigenvalues']);t,bt=encode(self.w['shift']);l=l.copy();l[0]+=1<<(bl-4)
  r,_=complex_residual((fm(t)*fm(v),fm(t)*fm(vi)),bt+bv,(fm(v*l[None,:]-vi*li[None,:]),fm(v*li[None,:]+vi*l[None,:])),bv+bl)
  m=self.cert['metrics'].copy();m['eigenpair_residual_upper']=up(r)
  with self.assertRaises(AssertionError):assemble(m,self.c)
 def test_bad_inverse_refuses(self):
  m=self.cert['metrics'].copy();m['inverse_residual_upper']=[1,1]
  with self.assertRaises(AssertionError):assemble(m,self.c)
 def test_bad_argument_output_refuses(self):
  m=self.cert['metrics'].copy();m['argument_output_error_upper']=[1,100]
  with self.assertRaises(AssertionError):assemble(m,self.c)
if __name__=='__main__':unittest.main()
