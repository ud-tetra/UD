#!/usr/bin/env python3
"""Create a geometric visualization of the exact four-quadrant partition.
Visualization only; all proofs are in UD_TETRAHEDRAL_QUADRANTS_VERIFY_v0.8.py.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib import colors as mcolors
from pathlib import Path

V=np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]],dtype=float)
O=np.array([0.,0.,0.])
colors=plt.rcParams['axes.prop_cycle'].by_key()['color'][:4]

fig=plt.figure(figsize=(13,6),dpi=180,layout='constrained')
ax1=fig.add_subplot(121,projection='3d')
for i in range(4):
    face=V[[j for j in range(4) if j!=i]]
    tris=[face, np.array([O,face[0],face[1]]),np.array([O,face[1],face[2]]),np.array([O,face[2],face[0]])]
    poly=Poly3DCollection(tris,facecolors=[colors[i]]*4,alpha=.17,edgecolors=colors[i],linewidths=.7)
    ax1.add_collection3d(poly)
    center=face.mean(axis=0)
    p=center*1.13
    ax1.text(*p, f'Q{i}', fontsize=11, weight='bold')
for vertex in V:
    ax1.plot(*np.array([O,vertex]).T,linewidth=1.7)
ax1.scatter([0],[0],[0],s=45,zorder=10)
ax1.text(0,0,-.27,'O')
ax1.set_title('One tetrahedron = four bounded quadrants\nEach has 1/4 of the volume')
ax1.set(xlim=(-1.7,1.7),ylim=(-1.7,1.7),zlim=(-1.7,1.7))
ax1.set_box_aspect((1,1,1)); ax1.set_axis_off()
ax1.view_init(elev=22,azim=-65)

ax2=fig.add_subplot(122,projection='3d')
# Partition the unit sphere by which tetrahedral vertex has the smallest dot product.
# Color each spherical direction with its quadrant index.
u=np.linspace(0,np.pi,95)
phi=np.linspace(0,2*np.pi,191)
TH,PH=np.meshgrid(u,phi,indexing='ij')
X=np.sin(TH)*np.cos(PH);Y=np.sin(TH)*np.sin(PH);Z=np.cos(TH)
pts=np.stack([X,Y,Z],axis=-1)
index=np.argmin(np.einsum('...i,ji->...j',pts,V),axis=-1)
F=np.zeros((*index.shape,4))
for i in range(4):F[index==i]=mcolors.to_rgba(colors[i],alpha=.7)
ax2.plot_surface(X,Y,Z,facecolors=F,linewidth=0,antialiased=False,shade=False,rstride=1,cstride=1)
# Overlay the exact great-circle edges of the four spherical triangles.
for j in range(4):
    for k in range(j+1,4):
        a=V[j]/np.linalg.norm(V[j]); b=V[k]/np.linalg.norm(V[k]);
        theta=np.arccos(np.clip(np.dot(a,b),-1,1)); t=np.linspace(0,1,80)
        arc=np.sin((1-t)*theta)[:,None]/np.sin(theta)*a + np.sin(t*theta)[:,None]/np.sin(theta)*b
        ax2.plot(*(arc*1.003).T,linewidth=1.5)
for i in range(4):
    p=-V[i]/np.linalg.norm(V[i])*1.19
    ax2.text(*p,f'Q{i}',fontsize=11,weight='bold')
ax2.set(xlim=(-1.4,1.4),ylim=(-1.4,1.4),zlim=(-1.4,1.4)); ax2.set_box_aspect((1,1,1))
ax2.set_axis_off();ax2.view_init(elev=22,azim=-65)
ax2.set_title('All directions in 3D = four angular quadrants\nSolid angle per quadrant: π steradians')
fig.suptitle('Tetrahedral quadrant coordinates — exact geometry, not physical cosmology',fontsize=14)
out=Path('/mnt/data/UD_TETRAHEDRAL_QUADRANTS_VISUAL_v0.8.png')
fig.savefig(out,dpi=180,bbox_inches='tight')
print(out,out.stat().st_size)
