"""Independent canonical bytes via exact Fraction denominators and integer gcd."""
from fractions import Fraction as F
from functools import reduce
import hashlib,math,struct
DOMAIN=b'UD_DYADIC_MATRIX_V1\0'

def canonical_fraction(rows,b):
 m=len(rows);n=len(rows[0]);assert m>0 and n>0 and all(len(row)==n for row in rows)and 0<=b<=256
 values=[F(int(v),2**b)for row in rows for v in row]
 denominator=1
 for v in values:denominator=math.lcm(denominator,v.denominator)
 assert denominator>0 and denominator&(denominator-1)==0
 bbar=denominator.bit_length()-1;numerators=[v.numerator*(denominator//v.denominator)for v in values]
 assert all(-2**63<=v<2**63 for v in numerators)
 blob=DOMAIN+struct.pack('<IIH',m,n,bbar)+b''.join(struct.pack('<q',v)for v in numerators)
 return {'m':m,'n':n,'bbar':bbar,'numerators':numerators,'bytes':blob,'fingerprint':hashlib.sha256(blob).hexdigest()}

def canonical_gcd(rows,b):
 m=len(rows);n=len(rows[0]);values=[int(v)for row in rows for v in row];g=reduce(math.gcd,(abs(v)for v in values),0);cancel=math.gcd(g,2**b);bbar=(2**b//cancel).bit_length()-1
 numerators=[v//cancel for v in values];blob=DOMAIN+struct.pack('<IIH',m,n,bbar)+b''.join(struct.pack('<q',v)for v in numerators)
 return blob

def controls():
 rows=[]
 def ck(n,x):
  assert x,n
  rows.append({'id':n,'pass':True})
 for value in range(-8,9):
  for b in range(9):ck('scalar_fraction_gcd_'+str(value)+'_'+str(b),canonical_fraction([[value]],b)['bytes']==canonical_gcd([[value]],b))
 examples=[([[2,-4],[0,6]],1),([[0,0,0]],256),([[-2**63]],63),([[-2**63]],256),([[-2**63,1]],64),([[-8,-4]],4),([[8,4]],4),([[2,-4],[0,6]],0)]
 for i,(a,b)in enumerate(examples):ck('matrix_fraction_gcd_'+str(i),canonical_fraction(a,b)['bytes']==canonical_gcd(a,b))
 a=canonical_fraction([[2,-4],[0,6]],1)
 ck('scaled_alias_bytes',a['bytes']==canonical_fraction([[4,-8],[0,12]],2)['bytes'])
 ck('reduced_alias_bytes',a['bytes']==canonical_fraction([[1,-2],[0,3]],0)['bytes'])
 ck('unpaired_exponent_change_bytes',a['bytes']!=canonical_fraction([[2,-4],[0,6]],2)['bytes'])
 ck('shape_is_typed',a['bytes']!=canonical_fraction([[2,-4,0,6]],1)['bytes'])
 ck('allzero_exponent_invariance',canonical_fraction([[0,0,0]],0)['bytes']==canonical_fraction([[0,0,0]],256)['bytes'])
 ck('integer_saturation_even',canonical_fraction([[2,-4],[0,6]],0)['bbar']==0 and canonical_fraction([[2,-4],[0,6]],0)['numerators']==[2,-4,0,6])
 ck('int64_min_cancel63',canonical_fraction([[-2**63]],63)['bbar']==0 and canonical_fraction([[-2**63]],63)['numerators']==[-1])
 ck('int64_min_cancel_limited63',canonical_fraction([[-2**63]],256)['bbar']==193)
 ck('int64_min_odd_blocks_cancel',canonical_fraction([[-2**63,1]],64)['bbar']==64)
 return rows
