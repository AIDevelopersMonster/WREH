#!/usr/bin/env python3
from pathlib import Path
from io import BytesIO
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from reproduce import tail_constants
ROOT=Path(__file__).resolve().parents[1]
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'figure.dpi':150})
def save(fig,stem):
    for ext in ['pdf','png']:
        b=BytesIO();fig.savefig(b,format=ext,bbox_inches='tight');data=b.getvalue();assert len(data)>1000
        (ROOT/'figures'/f'{stem}.{ext}').write_bytes(data)
    plt.close(fig)
def main():
    a,S,A,se=tail_constants()
    for ru in [False,True]:
        suffix='-ru' if ru else ''
        x=np.linspace(.001,.985,500);fig,axs=plt.subplots(1,2,figsize=(9,3.1))
        axs[0].plot(x,-np.log1p(-x),color='#164769',lw=2);axs[1].plot(x,1/(1-x),color='#ac542d',lw=2)
        for ax in axs:
            ax.set_xlabel('x = HL/c');ax.axvline(1,color='grey',ls=':',lw=1);ax.set_xlim(0,1.02);ax.grid(alpha=.2)
        axs[0].set_ylabel('HT_L');axs[1].set_ylabel('E_req / E_d');axs[1].set_yscale('log')
        axs[0].set_title('Время возвращения' if ru else 'Return time');axs[1].set_title('Порог энергии' if ru else 'Energy threshold')
        fig.tight_layout();save(fig,'frontier'+suffix)
        fig,axs=plt.subplots(1,2,figsize=(9,3.1));t=np.linspace(0,6,160)
        axs[0].plot(t,t,color='#164769',label='Экспонента' if ru else 'Exponential');axs[0].plot(t,[np.log(a(v)) for v in t],color='#ac542d',label='Гладкий линейный хвост' if ru else 'Smooth linear tail')
        t=np.r_[np.linspace(0,1.5,90),np.geomspace(1.51,10000,150)]
        axs[1].plot(t,-np.expm1(-t),color='#164769');axs[1].plot(t,[S(v) for v in t],color='#ac542d');axs[1].axhline(1,color='grey',ls=':',lw=1);axs[1].set_xscale('symlog',linthresh=1)
        axs[0].legend(fontsize=8);axs[0].set_ylabel('log a(t)');axs[1].set_ylabel('S(t)  (H=c=1)')
        for ax in axs:
            ax.set_xlabel('t  (H=1)');ax.axvspan(0,1,color='#164769',alpha=.07);ax.grid(alpha=.2)
        axs[0].set_title('Общее прошлое и начало будущего' if ru else 'Shared past and initial future');axs[1].set_title('Различная доступность хвостов' if ru else 'Different remaining reach')
        fig.tight_layout();save(fig,'tails'+suffix)
if __name__=='__main__':main()
