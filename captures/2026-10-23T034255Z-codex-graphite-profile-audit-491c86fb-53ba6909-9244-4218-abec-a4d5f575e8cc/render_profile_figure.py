#!/usr/bin/env python3
"""Render the two public DFT lateral scans and first-harmonic residuals to SVG."""
import argparse
import csv
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--capture-dir',type=Path,required=True)
p.add_argument('--preview-png',type=Path)
a=p.parse_args()
root=a.capture_dir
r=json.loads((root/'FULL_PROFILE_RESULTS.json').read_text())
rows=list(csv.DictReader((root/'FULL_PROFILE_SCAN.csv').open()))
x=np.asarray([int(v['index']) for v in rows])*(1.6144023331994939/36)
shape=np.asarray([float(v['first_harmonic_shape']) for v in rows])
styles=[('3.4022','d3p4022_relative_microeV_per_upper','#1673b1'),('3.34','d3p34_relative_microeV_per_upper','#c75628')]
plt.rcParams.update({'font.size':10,'svg.fonttype':'none','svg.hashsalt':'ud-graphite-v6','axes.spines.top':False,'axes.spines.right':False})
fig,(ax,bx)=plt.subplots(2,1,figsize=(7.2,5.3),sharex=True,gridspec_kw={'height_ratios':[2.6,1]},layout='constrained')
for d,col,color in styles:
 y=np.asarray([float(v[col]) for v in rows]);u=r['profiles'][d]['U1_fit_microeV_per_upper']
 ax.plot(x,y,'o',color=color,ms=3.7,label=f'{d} Å DFT')
 ax.plot(x,u*shape,'-',color=color,lw=1.8,label=f'{d} Å first shell')
 bx.plot(x,y-u*shape,'o-',color=color,ms=2.5,lw=.8,label=f'{d} Å')
ax.set_ylabel('Energy above index 0 (μeV / upper atom)')
ax.set_title('Rigid (2,1) interface: archived lateral scans and first-shell fits',fontsize=11)
ax.legend(ncol=2,fontsize=8,frameon=False,loc='upper right')
ax.grid(alpha=.15)
bx.axhline(0,color='#555555',lw=.8)
bx.set_ylabel('Fit residual\n(μeV / atom)')
bx.set_xlabel('Displacement along archived high-symmetry line (Å)')
bx.grid(alpha=.15)
fig.savefig(root/'FULL_PROFILE_FIGURE.svg',format='svg',metadata={'Date':'2026-10-23','Creator':'UD graphite numerical replay'})
if a.preview_png:
    fig.savefig(a.preview_png,dpi=140)
