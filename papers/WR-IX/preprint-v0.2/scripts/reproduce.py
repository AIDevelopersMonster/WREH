#!/usr/bin/env python3
"""Finite checks of WR-IX formulas; infinite-tail claims use manuscript proofs."""
from pathlib import Path
import json, math
import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]

def switch(u):
    if u<=0:return 0.
    if u>=1:return 1.
    a,b=math.exp(-1/u),math.exp(-1/(1-u))
    return a/(a+b)

def rate(t,H=1.,T=1.,delta=.5):
    if t<=T:return H
    s=switch((t-T)/delta)
    return H*(1-s)+H*s/(1+H*(t-T))

def tail_constants(H=1.,T=1.,delta=.5):
    end=T+delta
    aend=math.exp(H*T+quad(lambda t:rate(t,H,T,delta),T,end,epsabs=1e-12)[0])
    A=aend/(1+H*delta)
    def a(t):
        if t<=T:return math.exp(H*t)
        if t>=end:return A*(1+H*(t-T))
        return math.exp(H*T+quad(lambda v:rate(v,H,T,delta),T,t,epsabs=1e-12)[0])
    s_end=quad(lambda t:1/a(t),0,end,points=[T],epsabs=1e-11)[0]
    def reach(t):
        if t<=T:return -math.expm1(-H*t)/H
        if t<=end:return quad(lambda v:1/a(v),0,t,points=[T],epsabs=1e-11)[0]
        return s_end+math.log((1+H*(t-T))/(1+H*delta))/(A*H)
    return a,reach,A,s_end

def main():
    H,c,L,Ed=sp.symbols('H c L Ed',positive=True)
    x=H*L/c; TL=-sp.log(1-x)/H
    assert sp.simplify(c/H*(1-sp.exp(-H*TL))-L)==0
    assert sp.simplify(sp.exp(H*TL)-1/(1-x))==0
    assert sp.simplify(sp.diff(c/H*(1-sp.exp(-H*sp.Symbol('t'))),sp.Symbol('t'))-c*sp.exp(-H*sp.Symbol('t')))==0
    rng=np.random.default_rng(20261009);count=0;max_error=0.
    # Numerical integration and root-finding independent of the closed inverse.
    for _ in range(160):
        h=10**rng.uniform(-4,2);cv=10**rng.uniform(-2,6);xx=rng.uniform(.001,.98)
        lv=cv/h*xx;t=-math.log1p(-xx)/h
        root=brentq(lambda u:quad(lambda v:math.exp(-v),0,u,epsabs=1e-12)[0]-xx,0,10)/h
        err=abs(root-t)/max(1,t);max_error=max(max_error,err);assert err<1e-10
        sv=quad(lambda v:cv*math.exp(-h*v),0,t,epsabs=1e-9)[0];assert math.isclose(sv,lv,rel_tol=2e-11)
        for _ in range(40):
            ht=rng.uniform(0,8);ee=rng.uniform(.1,100)
            direct=t<=ht/h and ee>=1/(1-xx)
            frontier=ee>=1 and xx<=min(-math.expm1(-ht),1-1/ee)
            assert direct==frontier;count+=1
    a,S,A,se=tail_constants()
    # Independent ODE evolves log(a) and accumulated reach before/after join.
    ode=solve_ivp(lambda t,y:[rate(t),math.exp(-y[0])],(0,50),[0.,0.],rtol=2e-11,atol=2e-12,dense_output=True,max_step=.02)
    assert ode.success
    tail_error=0.
    for t in np.linspace(0,50,251):
        v=ode.sol(t);err=max(abs(v[0]-math.log(a(t))),abs(v[1]-S(t)));tail_error=max(tail_error,err);assert err<2e-8
    # L=1.2 is inaccessible under exponential tail, accessible under smooth linear tail.
    target=1.2;tt=brentq(lambda t:S(t)-target,1.5,100)
    assert tt>1 and math.isclose(S(tt),target,rel_tol=1e-10) and math.isfinite(a(tt))
    # Quantifier example has every finite return but diverging resource requirements.
    for n in [2,3,10,100,1000,100000]:
        h=1-1/n;t=math.log(n)/h
        assert math.isclose((1-math.exp(-h*t))/h,1,rel_tol=1e-11)
        assert math.isclose(math.exp(h*t),n,rel_tol=1e-11)
    report={'status':'PASS','symbolic_identities':3,'frontier_cases':count,'inverse_quad_root_cases':160,'max_relative_root_error':max_error,'tail_ode_points':251,'max_tail_ode_error':tail_error,'tail_constants':{'A':A,'S_at_join':se},'smooth_tail_return_L_1.2':{'time':tt,'energy_in_Ed':a(tt)},'proof_limit':'Finite computations do not establish infinite-tail convergence or scientific priority.'}
    (ROOT/'verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
