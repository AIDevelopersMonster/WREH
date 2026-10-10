#!/usr/bin/env python3
"""Independent matrix witnesses; computations supplement, never replace proofs."""
from pathlib import Path
import json, math
import numpy as np
import sympy as sp
from scipy.linalg import expm
from scipy.stats import binom
ROOT=Path(__file__).resolve().parents[1]
S=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.diag([1,-1]).astype(complex)]
def response(n,phi):
    u=expm(-1j*phi*sum(a*s for a,s in zip(n,S)))@np.array([1,0],complex)
    return float(abs(u[1])**2),np.array([np.vdot(u,s@u).real for s in S]),np.outer(u,u.conj())
def main():
    checks=[]; rng=np.random.default_rng(20261009)
    # Symbolic exponentials on transverse axes, including density ambiguity.
    sx=sp.Matrix([[0,1],[1,0]]); sy=sp.Matrix([[0,-sp.I],[sp.I,0]])
    initial=sp.Matrix([1,0]); target=sp.Matrix([[0,0],[0,1]])
    for angle in [sp.pi/6,sp.pi/4,sp.pi/3,sp.pi/2]:
        for axis in [sx,sy]:
            u=(sp.eye(2)*sp.cos(angle)-sp.I*axis*sp.sin(angle))*initial
            assert sp.simplify(abs(u[1])**2-sp.sin(angle)**2)==0
    for axis in [sx,sy]:
        u=-sp.I*axis*initial
        assert sp.simplify(u*u.conjugate().T-target)==sp.zeros(2)
    checks.append({'check':'symbolic Pauli witnesses and complete-transfer density','cases':10,'status':'PASS'})
    worst=0.; count=0
    for p in [.01,.25,.5,.99,1.]:
        theta=math.asin(math.sqrt(p))
        for cap in [theta-.001,theta,theta+.3,theta+math.pi,theta+2.4*math.pi]:
            windows=[(m*math.pi+theta,min((m+1)*math.pi-theta,cap)) for m in range(5) if m*math.pi+theta<=cap+1e-13]
            expected=0 if cap<theta-1e-13 else 1+math.floor((cap-theta)/math.pi+1e-13)
            assert len(windows)==expected
            for lo,hi in windows:
                for phi in np.linspace(lo,hi,7):
                    radial=math.sqrt(p)/abs(math.sin(phi)); z=math.sqrt(max(0,1-radial**2))
                    for sign in [-1,1]:
                        for beta in [0,.713,2.431]:
                            n=[radial*math.cos(beta),radial*math.sin(beta),sign*z]
                            value,_,_=response(n,phi)
                            worst=max(worst,abs(value-p)); assert abs(value-p)<3e-13
                            assert abs(np.linalg.norm(n)-1)<2e-13 and phi<=cap+1e-13
                            count+=1
    checks.append({'check':'phase-window count, endpoints and matrix-exponential responses','cases':count,'max_error':worst,'status':'PASS'})
    for p in [.01,.25,.5,.9,.99,1.]:
        theta=math.asin(math.sqrt(p))
        for beta in np.linspace(0,2*math.pi,17):
            n=[math.cos(beta),math.sin(beta),0]
            _,r,rho=response(n,theta)
            expected=[math.sin(beta)*math.sin(2*theta),-math.cos(beta)*math.sin(2*theta),math.cos(2*theta)]
            assert np.max(abs(r-expected))<2e-14
            if p<1:
                inferred=math.atan2(r[0],-r[1]); assert abs(np.exp(1j*inferred)-np.exp(1j*beta))<1e-13
            else:
                assert np.max(abs(rho-np.diag([0,1])))<1e-14
                _,half,_=response(n,theta/2)
                assert np.max(abs(half[:2]-[math.sin(beta),-math.cos(beta)]))<2e-14
            shifted=expm(-1j*(theta*sum(a*s for a,s in zip(n,S))+1.713*np.eye(2)))@np.array([1,0],complex)
            assert np.max(abs(np.outer(shifted,shifted.conj())-rho))<2e-14
    checks.append({'check':'final versus intermediate probes and scalar phase gauge','cases':102,'status':'PASS'})
    # Independent 4-dimensional controls with Q of rank 2 and noncommuting steps.
    max_excess=-1.; cases=320
    for _ in range(cases):
        state=np.array([1,0,0,0],complex); action=0.
        for step in range(4):
            raw=rng.normal(size=(4,4))+1j*rng.normal(size=(4,4)); h=(raw+raw.conj().T)/2
            h*=rng.uniform(.01,.45); duration=rng.uniform(.02,.5)
            eig=np.linalg.eigvalsh(h); diameter=eig[-1]-eig[0]
            action+=diameter*duration/2 # natural-unit computation hbar=1
            state=expm(-1j*h*duration)@state
        p=float(np.sum(abs(state[2:])**2)); ceiling=math.sin(min(action,math.pi/2))**2
        excess=p-ceiling; max_excess=max(max_excess,excess)
        assert excess<1e-13
    checks.append({'check':'noncommuting higher-dimensional action certificate','cases':cases,'max_probability_excess':max_excess,'status':'PASS'})
    min_coverage=1.; cases=0
    for n in [32,64,128,512]:
        for mu in [.01,.1,.25,.5,.9,.99]:
            for alpha in [.05,.01]:
                radius=math.sqrt(math.log(2/alpha)/(2*n)); outcomes=np.arange(n+1)/n
                coverage=float(binom.pmf(np.arange(n+1),n,mu)[abs(outcomes-mu)<=radius+1e-15].sum())
                assert coverage>=1-alpha-1e-13; min_coverage=min(min_coverage,coverage); cases+=1
    checks.append({'check':'exact binomial coverage for fixed independent repetitions','cases':cases,'minimum_coverage':min_coverage,'status':'PASS'})
    h=6.62607015e-34; nu=1e7; radius=math.sqrt(math.log(40)/1024); lower=.25-radius-.01
    numeric={'energy_J':h*nu,'p_quarter_min_ns':1e9/(6*nu),'p_one_min_ns':1e9/(2*nu),'N':512,'successes':128,'alpha':.05,'delta':.01,'radius':radius,'lower_probability':lower,'certified_time_ns':1e9*math.asin(math.sqrt(lower))/(math.pi*nu)}
    assert abs(numeric['energy_J']-6.62607015e-27)<1e-41
    report={'status':'PASS','seed':20261009,'checks':checks,'benchmark':numeric,'scope':'Synthetic finite witnesses. General statements are proved in the manuscript; no apparatus data or novelty certification.'}
    (ROOT/'verification.json').write_text(json.dumps(report,indent=2)+'\n'); print(json.dumps(report,indent=2))
if __name__=='__main__': main()
