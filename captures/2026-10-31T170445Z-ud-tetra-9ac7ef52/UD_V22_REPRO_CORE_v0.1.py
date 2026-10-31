#!/usr/bin/env python3
from fractions import Fraction as F
S0=F(43,7); H=F(101,6); S=2*S0
vals={'mu/e':(S*H,F('206.77'),F(4343,21)),
      'tau/mu':(H,F('16.82'),F(101,6)),
      'tau/e':(S*H**2,F('3477.15'),F(438643,126))}
for label,(val,obs,expected) in vals.items():
    assert val==expected
    z=obs/val-1
    print(label, 'bare=',val, 'z=',z)
assert vals['mu/e'][0]!=F('207.21')
assert vals['tau/e'][0]!=F('3490.37')
for n in (10,100,1000):
    v=F(1,n)
    assert abs(v)/(v*v/2)==2*n
print('PASS - exact arithmetic only; physical promotion 0')
