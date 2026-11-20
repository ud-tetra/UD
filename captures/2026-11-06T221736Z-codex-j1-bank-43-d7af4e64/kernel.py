"""Frozen-bank scalar evaluator and exact outward rectangle bounds."""
import sys
sys.dont_write_bytecode=True
import json
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
HERE=Path(__file__).resolve().parent
BANK=json.loads((HERE/'BANK.json').read_text())['states']
EXACT={sid:{k:F(x) for k,x in s['exact_constants'].items()} for sid,s in BANK.items()}
CONSTANTS={sid:{k:float.fromhex(x) for k,x in s['constant_hex'].items()} for sid,s in BANK.items()}
U=F(1,2**53);TINY=F(1,2**1075);GRID=2**120
OPS=[('dw','sub','omega','OMEGA0'),('sw','add','omega','OMEGA0'),('s','mul','dw','sw'),('dg','sub','gamma','GAMMA0'),('p','mul','gamma','dw'),('q','mul','OMEGA0','dg'),('v','add','p','q'),('t','mul','TWO','v'),('pr','mul','s','M_R'),('qr','mul','t','M_I'),('cr','add','pr','qr'),('real','add','J_R','cr'),('pi','mul','s','M_I'),('qi','mul','t','M_R'),('ci','sub','pi','qi'),('imag','add','J_I','ci')]

def roots(x):
 x=F(x);assert x>=0;s=10**30;n=isqrt(x.numerator*s*s//x.denominator);lo=F(n,s);hi=lo if lo*lo==x else F(n+1,s)
 assert lo*lo<=x<=hi*hi
 return lo,hi

def ceilgrid(x):return F(-((-x.numerator*GRID)//x.denominator),GRID)
def op(a,b,kind):return a+b if kind=='add' else a-b if kind=='sub' else a*b

def interval(a,b,kind):
 l,h,ea=a;ll,hh,eb=b;ma=max(abs(l),abs(h));mb=max(abs(ll),abs(hh))
 if kind=='mul':
  pp=[l*ll,l*hh,h*ll,h*hh];lo,hi=min(pp),max(pp);prop=ma*eb+mb*ea+ea*eb
 else:lo,hi=(l+ll,h+hh) if kind=='add' else (l-hh,h-ll);prop=ea+eb
 mag=max(abs(lo),abs(hi));assert mag+prop<16
 e=ceilgrid(prop+U*(mag+prop)+TINY);assert e>=prop+U*(mag+prop)+TINY
 return lo,hi,e

def floating_bound(sid,box):
 wl,wu,gl,gu=box;exact=EXACT[sid]
 nodes={k:(x,x,abs(F.from_float(CONSTANTS[sid][k])-x)) for k,x in exact.items()}
 nodes['omega']=(wl,wu,F(0));nodes['gamma']=(gl,gu,F(0))
 errors=[]
 for name,kind,a,b in OPS:nodes[name]=interval(nodes[a],nodes[b],kind);errors.append(nodes[name][2])
 return roots(nodes['real'][2]**2+nodes['imag'][2]**2)[1],errors

def certificate(sid,box):
 wl,wu,gl,gu=box;assert 0<wl<=wu and 0<gl<=gu
 st=BANK[sid];e=EXACT[sid];wc,gc=e['OMEGA0'],e['GAMMA0']
 dr=max(abs(wl*wl-wc*wc),abs(wu*wu-wc*wc));di=2*max(abs(gl*wl-gc*wc),abs(gu*wu-gc*wc));dz2=dr*dr+di*di
 mass=F(st['full_state_L2_squared']);d2=F(st['defect_squared']);nu2=F(st['local_lift_squared']);assert mass>0 and d2>=0 and nu2>=0
 res=roots(d2)[1]+roots(nu2)[1];kap=roots(1+(wu/(2*gl))**2)[1];shifted=res+roots(dz2)[1]*roots(mass)[1]/2;model=kap*shifted**2
 ee,errors=floating_bound(sid,box)
 return {'state':sid,'delta_z_components_upper':[str(dr),str(di)],'delta_z_squared_upper':str(dz2),'kappa_upper':str(kap),'center_residual_upper':str(res),'shifted_residual_upper':str(shifted),'model_radius':str(model),'floating_radius':str(ee),'node_error_bounds':[str(x) for x in errors],'total_radius':str(model+ee)}

def point_formula_bounds(sid,w,g):
 st=BANK[sid];e=EXACT[sid];wc,gc=e['OMEGA0'],e['GAMMA0'];dz2=(w*w-wc*wc)**2+4*(g*w-gc*wc)**2
 dd=roots(F(st['defect_squared']));nn=roots(F(st['local_lift_squared']));mm=roots(F(st['full_state_L2_squared']));zz=roots(dz2);kk=roots(1+(w/(2*g))**2)
 lo=kk[0]*(dd[0]+nn[0]+zz[0]*mm[0]/2)**2;hi=kk[1]*(dd[1]+nn[1]+zz[1]*mm[1]/2)**2
 assert lo<=hi
 return lo,hi

def trace(sid,omega,gamma):
 J_R,J_I,M_R,M_I,OMEGA0,GAMMA0,TWO=[CONSTANTS[sid][k] for k in ['J_R','J_I','M_R','M_I','OMEGA0','GAMMA0','TWO']]
 dw=omega-OMEGA0
 sw=omega+OMEGA0
 s=dw*sw
 dg=gamma-GAMMA0
 p=gamma*dw
 q=OMEGA0*dg
 v=p+q
 t=TWO*v
 pr=s*M_R
 qr=t*M_I
 cr=pr+qr
 real=J_R+cr
 pi=s*M_I
 qi=t*M_R
 ci=pi-qi
 imag=J_I+ci
 return [dw,sw,s,dg,p,q,v,t,pr,qr,cr,real,pi,qi,ci,imag]
