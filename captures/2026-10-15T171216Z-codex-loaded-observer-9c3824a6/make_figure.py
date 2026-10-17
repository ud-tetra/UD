from pathlib import Path
from fractions import Fraction as F
import json,numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.linalg import expm
root=Path(__file__).resolve().parent;d=json.loads((root/'LOADED_OBSERVER_DATA.json').read_text())
arr=lambda a:np.array([[float(F(x)) for x in r] for r in a])
A=arr(d['A6']);G=arr(d['G6']);C=arr(d['C6']);w=d['write'];polys=[np.array([float(F(x)) for x in r]) for r in w['state_polynomials_ascending']]
tw=np.linspace(0,1,501);tr=np.linspace(0,2,801)[1:];xw=np.array([[np.polynomial.polynomial.polyval(t,a) for a in polys] for t in tw]);xr=np.array([expm(A*t)@np.array(w['target6']) for t in tr]);xx=np.vstack([xw,xr]);tt=np.r_[tw,1+tr]
energy=np.einsum('ij,jk,ik->i',xx,G,xx)/2;ys=xx@C.T;Is=(xx[:,2]+xx[:,4])/2;I2=(xx[:,2]-xx[:,4])/2
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
fig,ax=plt.subplots(2,2,figsize=(12,7.7),sharex=True,layout='constrained')
for a in ax.flat:
 a.axvspan(0,1,color='#e4edf6',alpha=.7);a.axvline(1,color='#586d80',lw=1,ls='--');a.grid(alpha=.2);a.set_xlim(0,3)
ax[0,0].plot(tt,Is,label='I₁',color='#12679e',lw=2);ax[0,0].plot(tt,I2,label='I₂',color='#b75338',lw=2);ax[0,0].set(title='Loop currents',ylabel='Current / I₀');ax[0,0].legend(loc='lower right')
ax[0,1].plot(tt,ys[:,0],color='#12679e',lw=2);ax[0,1].set(title='Shared-face voltage',ylabel='V_F / (I₀ Z₀)')
ax[1,0].plot(tt,ys[:,1],color='#8060a8',lw=2);ax[1,0].set(title='Loaded pickup voltage',ylabel='V_R / (I₀ Z₀)',xlabel='Time / t₀')
for t in [1,2,3]:
 state=expm(A*(t-1))@np.array(w['target6']);v=C@state
 ax[0,1].plot(t,v[0],'o',color='#172d42',ms=5);ax[1,0].plot(t,v[1],'o',color='#172d42',ms=5)
ax[1,1].plot(tt,energy,label='Stored electrical energy',color='#38744e',lw=2);ax[1,1].axhline(.5,color='#8d9b8f',ls=':',lw=1);ax[1,1].set(title='Energy during write and free read',ylabel='E / E_ref',xlabel='Time / t₀');ax[1,1].legend(loc='lower right')
fig.suptitle('Finite one-loop write, followed by a loaded two-channel read',fontsize=17,fontweight='bold')
fig.text(.5,-.025,'Shading: finite write pulse. Markers: three samples per channel. Dimensionless constructor benchmark; no measurements.',ha='center',fontsize=10)
fig.savefig(root/'Loaded_Write_Read_Trajectory.png',dpi=160,bbox_inches='tight');fig.savefig(root/'Loaded_Write_Read_Trajectory.svg',bbox_inches='tight')
