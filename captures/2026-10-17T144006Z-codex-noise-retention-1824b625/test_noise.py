"""Small adversarial checks of the mathematical contracts, not apparatus tests."""
import unittest
import numpy as np
from fractions import Fraction as F
from certify_noise import modal_bounds,model_budgets,load,beta_squared,counts,frac,a
from flint import arb

class NoiseContracts(unittest.TestCase):
 def test_duplicate_hankel_noise_can_be_coherent(self):
  # No independent-error averaging: all time errors identical and aligned.
  for M in [3,7]:
   delta=.125;p=37;c=2
   z=np.zeros((c,p));z[0,:]=delta
   E=np.tile(z,(M,M))/M
   self.assertAlmostEqual(np.linalg.norm(E,2),np.sqrt(p)*delta,places=13)

 def test_weighted_time_moments(self):
  # Directly enumerate Hankel antidiagonal multiplicities.
  for M in [2,3,17]:
   ts=[F(i+j,2) for i in range(M) for j in range(M)]
   self.assertEqual(sum(ts)/M**2,F(M-1,2))
   self.assertEqual(sum(t*t for t in ts)/M**2,F(7*M*M-12*M+5,24))

 def test_singular_bounds_survive_complex_transpose(self):
  # Right factor is transpose, not adjoint. Singular-value bounds still hold.
  rng=np.random.default_rng(3947);M=13;n=5
  phases=np.array([-.9,-.4,0,.4,.9])
  V=np.exp(1j*np.outer(np.arange(M),phases))/np.sqrt(M)
  D=np.diag([.03,.2,.7,1.1,2.])
  H=V@D@V.T
  gram=np.linalg.eigvalsh(V.conj().T@V)
  s=np.linalg.svd(H,compute_uv=False)[:n]
  nominal=np.sort(np.diag(D))[::-1]
  self.assertTrue(np.all(s>=gram[0]*nominal-1e-13))
  self.assertTrue(np.all(s<=gram[-1]*nominal+1e-13))

 def test_threshold_is_not_exact_partial_rank(self):
  # A weak real signal may also exceed2beta. Do not label the guaranteed count exact.
  beta=.1;D=np.diag([.4,.25,0.]);E=np.diag([-.1,0.,.1])
  s=np.linalg.svd(D+E,compute_uv=False)
  self.assertEqual(sum(s>2*beta),2)
  self.assertEqual(sum(np.diag(D)>=4*beta),1)
  self.assertLessEqual(s[-1],beta)

 def test_parent_error_contract_reproduces(self):
  budgets=model_budgets(load('PARENT_FITTED_CERTIFICATE.json'),load('PARENT_TRADEOFF_CERTIFICATE.json'))
  for p in load('PARENT_FITTED_CERTIFICATE.json')['protocols']:
   got=a(beta_squared(p['axis_samples'],F(1,2**26),budgets['parent_model'])).sqrt()
   expected=arb(p['Hankel_residual_error']['arb_enclosure'])
   self.assertTrue(abs(got-expected)<a(F(1,10**40)))

 def test_curve_monotonicity_and_block_accounting(self):
  blocks=modal_bounds(load('PARENT_PREPARATION_CERTIFICATE.json'))
  self.assertEqual(sum(b['rank_total'] for b in blocks),1893)
  self.assertEqual(sum(b['signed_frequency_multiplicity'] for b in blocks),105)
  b=model_budgets(load('PARENT_FITTED_CERTIFICATE.json'),load('PARENT_TRADEOFF_CERTIFICATE.json'))['restricted_pass_contract']
  C=F(1828864,1021)
  for M in [2048,4096,8192]:
   last=1893
   for n in range(30,7,-1):
    lower,upper4,upper2,_=counts(blocks,1-C/M,1+C/M,beta_squared(M,F(1,2**n),b))
    self.assertLessEqual(lower,last);self.assertLessEqual(lower,upper4)
    self.assertLessEqual(upper4,upper2);self.assertLessEqual(upper2,1893);last=lower

if __name__=='__main__':unittest.main()
