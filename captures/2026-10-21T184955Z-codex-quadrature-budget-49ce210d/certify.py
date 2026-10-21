"""Exact integer/rational certificate for the unchanged saved dyadic kernel.
No external numerical library, downloaded code execution, or empirical inputs.
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import csv,hashlib,json
P=Path(__file__).resolve().parent;root=P.parents[1];contract=json.loads((P/'CONTRACT.json').read_text());source=root/contract['kernel_source'];S=1<<160

def I(x):
 x=F(x);num=x.numerator*S;den=x.denominator
 return (num//den,-((-num)//den))
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def neg(a):return (-a[1],-a[0])
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 q=[a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1]]
 return (min(q)//S,-((-max(q))//S))
def scale(a,q):return mul(a,I(q))
def ub(a):return F(max(abs(a[0]),abs(a[1])),S)
def cmul(a,b):return (sub(mul(a[0],b[0]),mul(a[1],b[1])),add(mul(a[0],b[1]),mul(a[1],b[0])))
def cadd(a,b):return (add(a[0],b[0]),add(a[1],b[1]))
def cscale(a,q):return (scale(a[0],q),scale(a[1],q))
def norm1(a):return ub(a[0])+ub(a[1])
def atan_bounds(q,N):
 x=F(1,q);v=sum(((-1)**r*x**(2*r+1)/F(2*r+1) for r in range(N)),F(0));next_term=(-1)**N*x**(2*N+1)/F(2*N+1)
 return min(v,v+next_term),max(v,v+next_term)
a=atan_bounds(5,80);b=atan_bounds(239,20);pi=(16*a[0]-4*b[1],16*a[1]-4*b[0]);piI=(I(pi[0])[0],I(pi[1])[1]);assert pi[0]>3 and pi[1]<F(22,7)
def sincos(x):
 assert ub(x)<=1
 # Taylor through degree60. Lagrange remainder <=1/61! for either function.
 power=I(1);co=I(0);si=I(0)
 for j in range(61):
  if j%2==0:co=add(co,scale(power,F((-1)**(j//2),factorial(j))))
  else:si=add(si,scale(power,F((-1)**((j-1)//2),factorial(j))))
  power=mul(power,x)
 rem=I(F(1,factorial(61)))[1];return ((co[0]-rem,co[1]+rem),(si[0]-rem,si[1]+rem))
def phase_table(f,m):
 step=scale(piI,2*f/F(1953125));z=sincos(step);powers=[z]
 for j in range(m.bit_length()-1):powers.append(cmul(powers[-1],powers[-1]))
 table={0:(I(1),I(0))}
 for k in range(1,m+1):
  v=(I(1),I(0))
  for j in range(k.bit_length()):
   if (k>>j)&1:v=cmul(v,powers[j])
  table[k]=v;table[-k]=(v[0],neg(v[1]))
 return table
rows=[]
with source.open() as f:
 for r in csv.DictReader(f):rows.append((int(r['sample_offset']),F(float(r['real_h'])),F(float(r['imag_h']))))
assert len(rows)==2049 and [r[0] for r in rows]==list(range(-1024,1025))
fc=F(257*1953125,16184);table=phase_table(fc,1024)
def response(table,derivative=False):
 A=(I(0),I(0));B=(I(0),I(0))
 for k,re,im in rows:
  h=(I(re),I(im));e=table[k];ec=(e[0],neg(e[1]));va=cmul(h,e);vb=cmul(h,ec)
  if derivative:
   # d/df (half exp(+-2pi i f s)) = +-i pi s exp(+-2pi i f s).
   t=scale(piI,F(k,1953125));va=(neg(mul(va[1],t)),mul(va[0],t));vb=(mul(vb[1],t),neg(mul(vb[0],t)))
  else:va=cscale(va,F(1,2));vb=cscale(vb,F(1,2))
  A=cadd(A,va);B=cadd(B,vb)
 return A,B
A,B=response(table);Ap,Bp=response(table,True);D0=norm1((sub(A[0],I(1)),A[1]))+norm1(B);D1=norm1(Ap)+norm1(Bp)
H0=sum((abs(re)+abs(im) for _,re,im in rows),F(0));H2=sum(((abs(re)+abs(im))*F(k,1953125)**2 for k,re,im in rows),F(0));dc=abs(sum(r[1] for r in rows))+abs(sum(r[2] for r in rows))
width=F(50);band=D0+width*D1+2*pi[1]**2*H2*width**2
u=F(1,1<<53);ops=4098;gamma=ops*u/(1-ops*u);fp_bound=gamma*5*H0+F(2*ops,1<<1074)/(1-ops*u);fp_allow=F(1,1<<30);assert fp_bound<fp_allow
error=band+3*dc+H0/F(2000)+fp_allow;ratio=error/F(1,2);assert ratio<F(1,10)
phase=F(100,99)*ratio;delay=F(1024,1953125);passed=error<=F(1,100) and phase<=F(1,50) and delay<=F(3,5000);assert passed
A600,B600=response(phase_table(fc+600,1024));# reverse triangle: every phase suffers at least |A-1|-|B|.
negative_lower=1-F(A600[0][1],S)-norm1(B600);assert negative_lower>F(1,100)
noise_fail=band+3*dc+H0/F(100)+fp_allow;assert noise_fail>F(1,100);assert delay>F(1,2000)
def datum(q):return {'fraction':str(q),'approximation':float(q)}
out={'status':'PASS_EXACT_RATIONAL_CONDITIONAL_BUDGET','physical_promotion':0,'contract_sha256':hashlib.sha256((P/'CONTRACT.json').read_bytes()).hexdigest(),'kernel_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'precision_bits':160,'coefficient_interpretation':'IEEE754 binary64 values decoded exactly; no refit','D0_upper':datum(D0),'D1_upper_per_Hz':datum(D1),'H0_l1_upper':datum(H0),'H2_upper_s2':datum(H2),'baseline_leak_upper':datum(dc),'continuous_band_error_upper':datum(band),'input_error_output_upper_V':datum(H0/F(2000)),'floating_error_bound_V':datum(fp_bound),'floating_allowance_V':datum(fp_allow),'total_error_upper_V':datum(error),'phase_upper_rad':datum(phase),'availability_delay_s':datum(delay),'negative_controls':{'600Hz_actual_unit_tone_error_lower':datum(negative_lower),'epsilon_1over100_sufficient_budget':datum(noise_fail),'delay_cap_1over2000_fails':True},'source_requirements':'50Hz compact envelope spectrum, TV<=1V, phase center magnitude>=1/2V, input error<=1/2000V, baseline constant<=3V. Not empirically established.','limits':'Source class only; conditional serial floating bound, not all-platform runtime certification; no empirical rerun, promotion or action estimate.'}
(P/'CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['negative_controls']},indent=2))
