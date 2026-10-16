"""Exact symbolic/rational checks for the sixth-order parity proof.
The generic tensor estimates are analytic in the manuscript; these identities
check their constants, absorption and uniform comparison polynomials.
"""
from pathlib import Path
from fractions import Fraction as F
import sympy as s,json,hashlib
from parity_budget import budget

def main():
 checks=[]
 def ck(name,condition):
  assert bool(condition),name;checks.append({'name':name,'pass':True})
 M=s.Matrix([[1,2,0],[1,0,2]])
 ck('sphere_speed_squared_operator_norm',max((M*M.T).eigenvals())==6)
 ck('order_six_bound',864+F(1728,25)<940)
 ck('sixth_remainder',F(940,720)<2)
 ck('fifth_polarization',380*F(5**5,120)<10000)
 ck('cubic_W_squared',F(1,2)+F(1,3)+F(1,2)==F(4,3))
 ck('cubic_young_coefficient',2*F(3,2)**2==F(9,2))
 ck('quartic_multi_z',F(6+4+1,24)<=F(1,2))
 ck('quartic_W_squared',F(34,2)==17)
 ck('quartic_x_six',F(10,2)==5)
 ck('quintic_base_parity',F(5+10+1,120)==F(2,15))
 ck('quintic_linear_W',F(5,120)*2**4==F(2,3))
 ck('quintic_young_coefficient',2*F(2,3)**2==F(8,9))
 ck('quintic_multi_W',F(10+10+5+1,120)*2**3<2)
 ck('sixth_x_six',2*(4+4*32)==264)
 ck('sixth_W_squared',2*4*32*2**4==4096)
 ck('coarse_remainder_coefficient',F(4,3)*279+17*1600+2*10000+4096==51668)
 ck('fast_absorption_all_parameters',F(3,8)+F(51668,500000)<F(1,2))
 ck('critical_shift_all_parameters',F(279,2000000)<F(1,2))
 ck('quartic_distance_conversion',F(3,1600)<=F(1,400))
 # Put lambda=alpha/N=1/[100(1+u)], u>=0. Coefficient positivity
 # proves each rational function positive throughout the full parameter range.
 u=s.symbols('u',nonnegative=True);lam=1/(100*(1+u));D=279/(4*lam)
 E=2177*D**2+s.Rational(800,3)*D+s.Rational(19,6)+s.Rational(1280000,9)/lam
 S=s.Rational(9,2)*279**2*D**2/lam+279*D**3/6+1600**2/(18*lam)+5*1600*D**2+s.Rational(2,15)*10000*D+s.Rational(8,9)*10000**2/lam+264
 polynomials={}
 for name,expr in [('old_radius_uses_quartic_cap',400*lam*E-10000),('linear_radius_gain_50000',400*lam*E-500000*50000),('root_radius_gain_50000',400*E**2-50000**2*S)]:
  n,d=s.fraction(s.cancel(expr));pn,pd=s.Poly(n,u),s.Poly(d,u)
  ck(name,all(c>0 for c in pn.all_coeffs()) and all(c>0 for c in pd.all_coeffs()))
  polynomials[name]={'variable':'u=N/(100alpha)-1 >=0','numerator_coefficients_descending':[str(c) for c in pn.all_coeffs()],'denominator_coefficients_descending':[str(c) for c in pd.all_coeffs()]}
 fixtures=[budget(),budget(F(1,100000),F(1)),budget(F(100),F(3)),budget(F(1),F(1),F(1,10**12))]
 inherited=Path('FROZEN_ENDPOINT_QUARTIC_CERTIFICATE_v0.1.json');dep=json.loads(inherited.read_text());assert dep['status']=='PASS'
 out={'status':'PASS','claim_bin':'DERIVED_CONDITIONAL','independent_review':'PENDING','physical_promotion':0,'checks':checks,'check_count':len(checks),'uniform_radius_gain':'R_parity >= 50000 R_EQT for all a,N>0 at each finite rank','comparison_certificates':polynomials,'budget_examples':fixtures,'inherited_status_validated_separately':True,'inherited_certificate_sha256':hashlib.sha256(inherited.read_bytes()).hexdigest(),'scope':'Analytic isometric involution, parity and sixth-order proof in manuscript; exact constant identities, positive-coefficient full-parameter comparison and rational examples checked here. Frozen EQT input is dependency, not newly re-proved or independently reviewed.'}
 Path('PARITY_ENDPOINT_CERTIFICATE_v0.1.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':'PASS','exact_checks':len(checks),'unit_budget':fixtures[0]},indent=2))
if __name__=='__main__':main()
