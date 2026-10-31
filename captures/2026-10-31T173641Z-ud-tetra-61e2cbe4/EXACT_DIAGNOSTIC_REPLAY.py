#!/usr/bin/env python3
from fractions import Fraction as F
from decimal import Decimal as D,getcontext
getcontext().prec=60
s0=F(43,7);h=F(101,6);s=2*s0
src={'alpha':F(7,960),'mu/e':s*h,'tau/mu':h,'tau/e':s*h*h,'ns':F(185,192)}
m={'e':D('0.51099895069'),'mu':D('105.6583755'),'tau':D('1776.93')}
obs={'alpha':1/D('137.035999177'),'mu/e':m['mu']/m['e'],'tau/mu':m['tau']/m['mu'],'tau/e':m['tau']/m['e'],'ns':D('0.9649')}
Dq=lambda q:D(q.numerator)/D(q.denominator)
assert src['tau/e']==src['tau/mu']*src['mu/e']
assert obs['tau/e']==obs['tau/mu']*obs['mu/e']
L={k:(obs[k]/Dq(src[k])).ln() for k in src}
assert abs(L['tau/e']-L['tau/mu']-L['mu/e'])<D('1e-50')
for k in src: print(k, src[k], (obs[k]/Dq(src[k])-1)*100)
assert obs['alpha']/Dq(src['alpha'])>1 and obs['mu/e']/Dq(src['mu/e'])<1
print('PASS: internal fractions and relative diagnostics; no physical promotion')
