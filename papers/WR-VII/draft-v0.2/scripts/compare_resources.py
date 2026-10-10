#!/usr/bin/env python3
"""Static, synthetic QSL positioning witnesses; hbar=1, not apparatus data."""
from pathlib import Path
import numpy as np,json,math
from scipy.linalg import expm
ROOT=Path(__file__).resolve().parents[1]
def main():
    cases=[]
    for name,levels,amplitudes in [
        ('transverse frontier equivalent energy statistics',[-.5,.5],[1/math.sqrt(2),1/math.sqrt(2)]),
        ('unused high level makes diameter certificate loose',[0,.1,1],[1/math.sqrt(2),1/math.sqrt(2),0]),
        ('mean energy does not uniformly improve diameter',[0,1,2],[0,1/math.sqrt(2),1/math.sqrt(2)])]:
        h=np.diag(levels);psi=np.array(amplitudes,complex);weights=abs(psi)**2
        mean=float(weights@np.array(levels));variance=float(weights@np.array(levels)**2-mean**2)
        spread=math.sqrt(variance);diameter=max(levels)-min(levels);above=mean-min(levels)
        bounds={'diameter':math.pi/diameter,'Mandelstam_Tamm':math.pi/(2*spread),'Margolus_Levitin':math.pi/(2*above)}
        indices=np.flatnonzero(weights);actual=math.pi/(levels[indices[1]]-levels[indices[0]])
        assert abs(np.vdot(psi,expm(-1j*h*actual)@psi))<1e-13
        assert spread<=diameter/2+1e-13 and max(bounds.values())<=actual+1e-12
        cases.append({'case':name,'levels':levels,'hbar':1,'diameter':diameter,'spread':spread,'mean_above_ground':above,'lower_times':bounds,'orthogonalization_time':actual})
    assert abs(cases[0]['lower_times']['diameter']-cases[0]['lower_times']['Mandelstam_Tamm'])<1e-13
    assert cases[1]['lower_times']['Mandelstam_Tamm']>cases[1]['lower_times']['diameter']
    assert cases[2]['lower_times']['Margolus_Levitin']<cases[2]['lower_times']['diameter']
    report={'status':'PASS','scope':'Three synthetic state-dependent positioning witnesses in natural units; no new theorem or apparatus data. Static formulas only.','cases':cases}
    (ROOT/'qsl-positioning-verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print('Three static resource comparison witnesses PASS')
if __name__=='__main__':main()
