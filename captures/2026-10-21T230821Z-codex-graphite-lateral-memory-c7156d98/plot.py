from pathlib import Path
import numpy as np,json,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
p=Path(__file__).resolve().parent;r=json.loads((p/'RESULTS_v02.json').read_text());fig,axes=plt.subplots(2,2,figsize=(11.2,7.6),layout='constrained');colors=['#2864a7','#e1812c','#43925b','#8b5ba7']
for ax,case in zip(axes[0],['21_dir_0','31_dir_10084']):
 a=np.load(p/'run_v02'/case/'MODEL.npz');raw=np.load(p/'run_v02'/case/'hidden_displacement.npz');D=a['D'];m=len(D);n=(m+2)//3;L=m-n;tt=raw['tau'];lam,W=np.linalg.eigh(D);q=(np.cos(tt[:,None]*np.sqrt(lam))*(W.T@raw['q0'])+np.sin(tt[:,None]*np.sqrt(lam))/np.sqrt(lam)*(W.T@raw['v0']))@W.T;z=raw['memory_state'][:,:n];ax.plot(tt,np.linalg.norm(q[:,L:],axis=1),color='#222',lw=2.0,label='Full harmonic model');ax.plot(tt,np.linalg.norm(z,axis=1),color='#e1812c',ls='--',lw=1.3,label='Memory equation');ax.plot(tt,np.linalg.norm(raw['omitted_source_vertical'],axis=1),color='#2864a7',ls=':',lw=2,label='Initial source omitted');ax.set(title=case+' — hidden displacement',xlabel='Normalized time τ',ylabel='Vertical displacement norm');ax.grid(alpha=.18);ax.legend(fontsize=8)
ax=axes[1,0]
for c,color in zip(r['cases'],colors):
 a=np.load(p/'run_v02'/c['case']/'MODEL.npz');tt=np.linspace(0,80,801);coef=np.cos(tt[:,None]*np.sqrt(a['A_eigenvalues']))/a['A_eigenvalues'];B=(a['G']@a['G'].T)**2;norm=np.sqrt(np.maximum(np.einsum('ti,ij,tj->t',coef,B,coef),0))/np.linalg.norm(a['K0']);ax.plot(tt,norm,color=color,lw=1,label=c['case'])
ax.set(title='Finite oscillatory memory',xlabel='Normalized time τ',ylabel='Kernel Frobenius norm / initial norm');ax.grid(alpha=.18);ax.legend(fontsize=7)
ax=axes[1,1];xx=np.arange(4);good=[max(z['z_error_max'] for z in c['preparations']) for c in r['cases']];bad=[min(z['omitting_initial_source_error'] for z in c['preparations'] if z['preparation']!='conditional_lateral_equilibrium') for c in r['cases']];ax.bar(xx-.19,good,width=.38,color='#e1812c',label='Largest memory error');ax.bar(xx+.19,bad,width=.38,color='#2864a7',label='Smallest nonzero-source omission error');ax.set(yscale='log',title='Error compared with full harmonic model',ylabel='Maximum component error');ax.set_xticks(xx,[c['case'] for c in r['cases']],rotation=18,fontsize=8);ax.legend(fontsize=7);ax.grid(axis='y',alpha=.18)
fig.suptitle('Conservative lateral-memory verification — normalized linear models',fontsize=14);fig.savefig(p/'MEMORY_CHECK.png',dpi=170)
