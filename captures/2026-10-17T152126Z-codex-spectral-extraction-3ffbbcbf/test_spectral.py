"""Adversarial exact checks; dense matrices only for tiny independent controls."""
from pathlib import Path
from fractions import Fraction as F
import tempfile,unittest
import numpy as np
from flint import fmpz_mat
from hankel_exact import HankelRecord,disk_cores
from spectral_certificate import certify
from propose_basis import FloatActions,propose

def dense_num(Y):
 p,n,c=Y.shape;M=(n+1)//2
 return np.array([[int(Y[aa,i+j,cc]) for j in range(M) for aa in range(p)] for i in range(M) for cc in range(c)],dtype=object)
def to_dense_gram(G,r):
 if not isinstance(G,dict):return G
 return fmpz_mat([[G.get((min(i,j),max(i,j)),0) for j in range(r)] for i in range(r)])

class SpectralTests(unittest.TestCase):
 def setUp(self):
  self.Y=np.arange(3*9*2,dtype=np.int64).reshape(3,9,2)-20
  self.H=HankelRecord(self.Y,17);self.D=dense_num(self.Y)
 def test_exact_polynomial_action_matches_independent_dense(self):
  x=np.arange(self.H.cols,dtype=np.int64)-7
  nums,den=self.H.action(x)
  self.assertEqual(den,5*17);self.assertEqual([int(v) for v in nums],list(self.D@x))
 def test_exact_adjoint_and_duality(self):
  x=np.arange(self.H.cols,dtype=np.int64)-8;y=np.arange(self.H.rows,dtype=np.int64)-5
  hx,d=self.H.action(x);hty,dd=self.H.action(y,True)
  self.assertEqual([int(v) for v in hty],list(self.D.T@y))
  self.assertEqual(sum(int(xx)*int(yy) for xx,yy in zip(hx,y)),sum(int(xx)*int(yy) for xx,yy in zip(x,hty)))
  self.assertEqual(d,dd)
 def test_energy_counts_hankel_duplication_exactly(self):
  expected=F(sum(int(v)**2 for v in self.D.flat),self.H.den**2)
  self.assertEqual(self.H.energy(),expected)
 def test_sparse_selector_cores_match_dense(self):
  chosen=[0,4,11];gv,vd,gc,cd=self.H.selector_cores(chosen)
  C=fmpz_mat(self.D[:,chosen].tolist());self.assertEqual(to_dense_gram(gc,3),C.transpose()*C)
  self.assertEqual(to_dense_gram(gv,3),fmpz_mat([[1,0,0],[0,1,0],[0,0,1]]));self.assertEqual(cd,self.H.den**2)
 def test_streamed_dense_candidate_cores_match_independent_products(self):
  V=np.arange(self.H.cols*3,dtype=np.int64).reshape(self.H.cols,3)-15
  with tempfile.TemporaryDirectory() as tmp:
   path=Path(tmp)/'C.i128';gv,vd,gc,cd=disk_cores(self.H,V,path,31,block_rows=3)
   VV=fmpz_mat(V.tolist());CC=fmpz_mat((self.D@V).tolist())
   self.assertEqual(gv,VV.transpose()*VV);self.assertEqual(gc,CC.transpose()*CC)
   self.assertEqual(vd,31**2);self.assertEqual(cd,(self.H.den*31)**2)
   self.assertEqual(path.stat().st_size,self.H.rows*3*16)
   with self.assertRaises(FileExistsError):disk_cores(self.H,V,path,31)
 def test_missing_signal_candidate_cannot_certify_completeness(self):
  Y=np.zeros((1,9,1),dtype=np.int64);Y[0,2,0]=100
  H=HankelRecord(Y,100);cores=H.selector_cores([0,1])
  c=certify(H.energy(),*cores,2,F(1,100))
  self.assertEqual(c['status'],'HOLD');self.assertGreaterEqual(F(*c['sigma_r_plus1_upper_squared']),F(1,25))
 def test_duplicate_candidate_and_noninteger_inputs_reject(self):
  with self.assertRaises(ValueError):self.H.selector_cores([1,1])
  with self.assertRaises(ValueError):self.H.action(np.ones(self.H.cols,dtype=float))
 def test_bad_candidate_gram_holds_and_inconsistent_energy_rejects(self):
  bad=certify(F(1),{(0,0):4},1,{(0,0):1},1,1,F(1,10))
  self.assertEqual(bad['status'],'HOLD')
  with self.assertRaises(ValueError):certify(F(0),{(0,0):1},1,{(0,0):1},1,1,F(1,10))
 def test_inexact_orthogonality_residual_bound_covers_true_tail(self):
  # V is a rescaled coordinate basis; no assumption of exact orthogonality.
  Y=np.zeros((1,9,1),dtype=np.int64);Y[0,1,0]=100
  H=HankelRecord(Y,100);V=np.zeros((5,2),dtype=np.int64);V[0,0]=999;V[1,1]=999
  with tempfile.TemporaryDirectory() as tmp:
   cores=disk_cores(H,V,Path(tmp)/'C',1000)
  c=certify(H.energy(),*cores,2,F(1,100))
  self.assertGreater(F(*c['candidate_Gram_defect_squared']),0)
  self.assertGreaterEqual(F(*c['projection_tail_frobenius_squared_upper']),0)
 def test_individual_bands_cover_independent_small_svd(self):
  Y=np.zeros((1,15,2),dtype=np.int64);Y[0,2,0]=1000;Y[0,:,1]=1
  H=HankelRecord(Y,1000);cores=H.selector_cores([0,1,2]);c=certify(H.energy(),*cores,3,F(1,100))
  exact_numeric=np.linalg.svd(np.asarray(dense_num(Y),dtype=float)/H.den,compute_uv=False)
  self.assertEqual(c['status'],'CERTIFIED_NUMERIC_RECORD_SIGNATURE')
  for s,interval in zip(exact_numeric,c['individual_retained_singular_intervals']):
   lo,hi=map(lambda x:float(F(*x)),interval)
   self.assertGreaterEqual(s+1e-14,lo);self.assertLessEqual(s-1e-14,hi)
  self.assertLessEqual(exact_numeric[3]**2,float(F(*c['sigma_r_plus1_upper_squared']))+1e-14)
 def test_fft_proposals_match_dense_actions_but_are_not_proofs(self):
  A=FloatActions(self.H);x=np.arange(self.H.cols,dtype=np.float64)-7;y=np.arange(self.H.rows,dtype=np.float64)-2
  np.testing.assert_allclose(A.action(x),np.asarray(self.D@x,dtype=float)/self.H.den,rtol=1e-12,atol=1e-12)
  np.testing.assert_allclose(A.action(y,True),np.asarray(self.D.T@y,dtype=float)/self.H.den,rtol=1e-12,atol=1e-12)
 def test_end_to_end_proposal_then_exact_certificate(self):
  Y=np.zeros((1,15,2),dtype=np.int64);Y[0,2,0]=2**40
  H=HankelRecord(Y,2**40)
  with tempfile.TemporaryDirectory() as tmp:
   p=Path(tmp);propose(H,3,p/'V.npy',block_size=1,power_steps=2)
   V=np.load(p/'V.npy',mmap_mode='r',allow_pickle=False)
   cores=disk_cores(H,V,p/'C',2**60);c=certify(H.energy(),*cores,3,F(1,100))
   self.assertEqual(c['status'],'CERTIFIED_NUMERIC_RECORD_SIGNATURE')
   self.assertEqual(c['count_above_threshold_certified'],3)
 def test_nondiagonal_core_requires_verified_eigen_proposal(self):
  Y=np.array([[[1],[3],[10]]],dtype=np.int64);H=HankelRecord(Y,1)
  cores=H.selector_cores([0,1]);c=certify(H.energy(),*cores,2,F(1,1000))
  self.assertEqual(c['status'],'CERTIFIED_NUMERIC_RECORD_SIGNATURE')
  self.assertIn('polar correction',c['verified_core_spectral_bounds']['method'])
  self.assertGreater(F(*c['sigma_r_lower_squared']),0)

if __name__=='__main__':unittest.main()
