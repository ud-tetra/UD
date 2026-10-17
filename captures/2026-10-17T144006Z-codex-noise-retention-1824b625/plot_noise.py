"""Static scientific plot. Floating conversions are display-only."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent
d=json.loads((ROOT/'NOISE_RETENTION_CERTIFICATE.json').read_text())
fig,axs=plt.subplots(1,2,figsize=(11,4.5),sharey=True)
for ax,name,title in zip(axs,['output_only','restricted_pass_contract'],['Output error only','Including restricted-pass model budget']):
 for p,color in zip(d['protocols'],['#3b6aa0','#b76428','#267b63']):
  rows=p['models'][name]['samples']
  ax.step([r['delta_exponent'] for r in rows],[r['guaranteed_retained_count'] for r in rows],where='pre',label=f"M = {p['M']:,}",color=color,linewidth=2)
 ax.set_title(title);ax.set_xlim(-26,-8);ax.set_ylim(0,2000)
 ax.set_xticks([-26,-23,-20,-17,-14,-11,-8]);ax.set_xticklabels([r'$2^{%d}$'%n for n in [-26,-23,-20,-17,-14,-11,-8]])
 ax.set_xlabel('Per 62-vector additive error bound δ');ax.grid(alpha=.22);ax.legend(frameon=False)
axs[0].set_ylabel('Guaranteed distinguishable signal count (lower bound)')
fig.suptitle('Original 600-cell vertex-link readout • 37 preparations',fontsize=13)
fig.text(.5,.02,'Conservative frequency-block bounds; conditional certificate, no measured data. Discrete dyadic grid; jumps are not exact loss thresholds.',ha='center',fontsize=8)
fig.tight_layout(rect=(0,.05,1,.94))
fig.savefig(ROOT/'NOISE_RETENTION_CURVE.png',dpi=180)
fig.savefig(ROOT/'NOISE_RETENTION_CURVE.pdf')
