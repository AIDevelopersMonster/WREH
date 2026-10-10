#!/usr/bin/env python3
"""Analytic figures: actual units, no measured data."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'pdf.fonttype':42})
fig,(ax,bx)=plt.subplots(1,2,figsize=(10,3.6),gridspec_kw={'width_ratios':[1.1,1]},layout='constrained')
nu=np.linspace(2,20,400)
for p,color in [(.25,'#166a8c'),(.5,'#b86813'),(1,'#773f8c')]:
    theta=np.arcsin(np.sqrt(p)); ax.plot(nu,1000*theta/(np.pi*nu),label=f'$p={p:g}$',color=color,lw=2)
ax.set(xlabel='$E/h$ (MHz)',ylabel='$\\tau_{\\min}$ (ns)',xlim=(2,20),ylim=(0,260));ax.grid(alpha=.15);ax.legend(frameon=False)
ax.scatter([10,10],[50/3,50],color=['#166a8c','#773f8c'],s=22,zorder=3)
phi=np.linspace(0,2*np.pi,900);bx.plot(phi/np.pi,np.sin(phi)**2,color='#3d5568',lw=1.8,label='$\\sin^2\\phi$');bx.axhline(.25,color='#166a8c',ls='--',lw=1)
cap=5*np.pi/4;theta=np.pi/6
for m in [0,1]:
    lo=m*np.pi+theta;hi=min((m+1)*np.pi-theta,cap)
    bx.axvspan(lo/np.pi,hi/np.pi,color='#166a8c',alpha=.18)
bx.axvline(cap/np.pi,color='#b86813',lw=1.5);bx.text(cap/np.pi+.025,.77,'$C=5\\pi/4$',color='#b86813')
bx.set(xlabel='$\\phi/\\pi$',ylabel='$p$',xlim=(0,2),ylim=(0,1.03));bx.grid(alpha=.15)
bx.set_xticks([0,1/6,5/6,1,7/6,1.25,2],['0','$1/6$','$5/6$','1','$7/6$','$5/4$','2']);bx.tick_params(axis='x',labelsize=8)
fig.savefig(ROOT/'figures/frontiers.pdf',metadata={'Title':'WR-VII analytic energy-time frontiers','Author':'A. A. Malachevsky','CreationDate':None})
fig.savefig(ROOT/'figures/frontiers.png',dpi=180)
print('figures/frontiers.pdf and figures/frontiers.png')
