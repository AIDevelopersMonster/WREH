#!/usr/bin/env python3
"""Exact synthetic FLRW distance curves with EN/RU labels; no survey data."""
from pathlib import Path
from io import BytesIO
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle
ROOT=Path(__file__).resolve().parents[1]
(ROOT/'figures').mkdir(exist_ok=True)
def save_pdf(fig,path,metadata):
 buffer=BytesIO();fig.savefig(buffer,format='pdf',metadata=metadata)
 payload=buffer.getvalue()
 assert payload.startswith(b'%PDF-') and len(payload)>1000
 path.write_bytes(payload)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'pdf.fonttype':42})
c=299792.458;h0=70;u=c/h0;z=np.linspace(0,1.5,500);f=z-.15*z*z;g=1-.3*z
colors=['#b86813','#166a8c','#773f8c']
fig,(ax,bx)=plt.subplots(1,2,figsize=(10,3.4),layout='constrained')
for q,col,style in zip([-.2,0,.2],colors,['--','-',':']):
 ax.plot(z,u*f,color=col,ls=style,lw=2,label=f'$q={q:g}$')
 bx.plot(z,h0*np.sqrt(1-q*f*f)/g,color=col,ls=style,lw=2,label=f'$q={q:g}$')
for x in [ax,bx]:x.grid(alpha=.15);x.legend(frameon=False);x.set_xlabel('Redshift $z$');x.set_xlim(0,1.5)
ax.set_ylabel('$D(z)$ (Mpc)');bx.set_ylabel('$H(z)$ (km/s/Mpc)')
save_pdf(fig,ROOT/'figures/distance-fibre.pdf',metadata={'Title':'WR-VIII v0.2 synthetic distance completion (EN)','Author':'A. A. Malachevsky','CreationDate':None});fig.savefig(ROOT/'figures/distance-fibre.png',dpi=180)
for x in [ax,bx]: x.set_xlabel('Красное смещение $z$')
ax.set_ylabel('$D(z)$ (Мпк)');bx.set_ylabel('$H(z)$ (км/с/Мпк)')
save_pdf(fig,ROOT/'figures/distance-fibre-ru.pdf',metadata={'Title':'WR-VIII v0.2 synthetic distance completion (RU)','Author':'A. A. Malachevsky','CreationDate':None});fig.savefig(ROOT/'figures/distance-fibre-ru.png',dpi=180);plt.close(fig)
fig,(ax,bx)=plt.subplots(1,2,figsize=(10,3.3),layout='constrained')
lo=(1-1.02**2)/.85**2;hi=(1-.98**2)/.85**2
ax.plot([-.4,.4],[2,2],lw=8,color='#c8d5df',solid_capstyle='butt');ax.plot([lo,hi],[1,1],lw=8,color='#166a8c',solid_capstyle='butt');ax.scatter([0],[0],s=65,color='#b86813',zorder=3)
ax.set(xlabel='$q=\\kappa u^2$',yticks=[0,1,2],yticklabels=['Exact flat rate','Rate interval','Declared prior'],xlim=(-.45,.45),ylim=(-.5,2.5));ax.grid(axis='x',alpha=.15)
r=1.1625;side=3.5
bx.add_patch(Rectangle((-side/2,-side/2),side,side,facecolor='#f3f7fa',edgecolor='#166a8c',lw=1.7));bx.add_patch(Circle((0,0),r,facecolor='#b86813',edgecolor='#b86813',alpha=.18));bx.plot([0,r],[0,0],color='#b86813');bx.scatter([0],[0],s=18,color='#263f50');bx.text(r/2,.12,'$R/u$',ha='center');bx.text(0,side/2+.18,'$L/u=3.5>2R/u$',ha='center');bx.set(xlim=(-2.1,2.1),ylim=(-2.1,2.1),aspect='equal',xlabel='$x/u$',ylabel='$y/u$');bx.grid(alpha=.12)
save_pdf(fig,ROOT/'figures/refinement-lifts.pdf',metadata={'Title':'WR-VIII v0.2 synthetic refinement and local topology witness (EN)','Author':'A. A. Malachevsky','CreationDate':None});fig.savefig(ROOT/'figures/refinement-lifts.png',dpi=180)
ax.set_yticklabels(['Точная плоская скорость','Интервал скорости','Заданное ограничение'])
save_pdf(fig,ROOT/'figures/refinement-lifts-ru.pdf',metadata={'Title':'WR-VIII v0.2 synthetic refinement and local topology witness (RU)','Author':'A. A. Malachevsky','CreationDate':None});fig.savefig(ROOT/'figures/refinement-lifts-ru.png',dpi=180);plt.close(fig)
print('Two analytic figures, each with EN/RU labels, written in PDF and PNG.')
