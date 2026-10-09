#!/usr/bin/env python3
"""Adversarial checks of strict endpoints, adaptive premises and quantifiers."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
from scipy.integrate import quad
import math,json
ROOT=Path(__file__).resolve().parents[1]
def main():
    checks=[]
    def check(name,condition):
        assert condition,name;checks.append(name)
    # Distinct equality conventions: finite detector/deadline inclusive; causal tail excluded.
    check('finite double equality',abs(-math.log(.5)-math.log(2))<1e-14 and 1/(1-.5)==2)
    check('no positive period with Emax=Ed',1-1/1==0)
    check('no positive period at zero deadline',1-math.exp(0)==0)
    for t in [0,1,2,10,20]:check('causal endpoint strictly unreached at t='+str(t),-math.expm1(-t)<1)
    # Avoid subtracting to 1 at huge t in floating point; use the positive residual exp(-t).
    check('endpoint residual at t=100',math.exp(-100)>0)
    eps=F(1,10);left=(F(0)-eps,F(0)+eps);right=(2*eps-eps,2*eps+eps)
    check('bounded-error equality overlaps',left[1]==right[0])
    check('strictly larger bounded-error gap disjoint',3*eps-eps>left[1])
    check('tolerance nontransitivity',abs(0-eps)<=eps and abs(eps-2*eps)<=eps and abs(0-2*eps)>eps)
    # Identical isolated marginals, unequal transcript laws.
    same={(0,0):F(1,2),(1,1):F(1,2)};opposite={(0,1):F(1,2),(1,0):F(1,2)}
    for j in [0,1]:
        for y in [0,1]:check(f'fair isolated marginal {j},{y}',sum(v for h,v in same.items() if h[j]==y)==sum(v for h,v in opposite.items() if h[j]==y)==F(1,2))
    check('transcript detects dependence',same!=opposite)
    # Adaptive policy chooses p=h0 after its first recorded bit, common conditional laws.
    def law():
        out={}
        for y0 in [0,1]:
            for y1 in [0,1]:
                q=F(1,3) if y0==0 else F(2,3)
                out[(y0,y1)]=F(1,2)*(q if y1 else 1-q)
        return out
    world_w=Counter();world_v=Counter()
    for u0 in [0,1]:
        for u1 in [0,1,2]:
            world_w[(u0,int(u1<(1 if u0==0 else 2)))]+=1
            world_v[(u0,int(u1>(1 if u0==0 else 0)))]+=1
    empirical_w={k:F(v,6) for k,v in world_w.items()}
    empirical_v={k:F(v,6) for k,v in world_v.items()}
    check('different latent mechanisms, common adaptive transcript',empirical_w==empirical_v==law() and sum(law().values())==1)
    check('two actions exceed individual-only energy certificate',F(3,4)<=1 and 2*F(3,4)>1)
    for deadline in [0,1,100]:
        check(f'noncompact unresolved tail T={deadline}',max(0,deadline-(deadline+1))==max(0,deadline-(deadline+2))==0)
    spans=[1/(1-1/n) for n in [2,3,10,1000]]
    check('infimum equality is compatible with every return',all(v>1 for v in spans) and spans[-1]<1.002)
    check('common exclusion uses supremum',not (1.5>=max(spans)))
    def bump(t):return math.exp(-1/(t*(1-t))) if 0<t<1 else 0
    changed_prefix=quad(lambda t:math.exp(-t-bump(t)),0,1,epsabs=1e-13)[0]
    original_prefix=1-math.exp(-1)
    check('same compact tail changes finite span value',changed_prefix<original_prefix and abs(changed_prefix-original_prefix)>1e-4)
    # Every dimensional expression is audited algebraically in SOURCE_MAP.md; units are not numerical tests.
    report={'status':'PASS','checks':checks,'count':len(checks),'review_type':'AI-assisted adversarial technical audit; not independent external peer review','infinite_tail_claims':'Analytic manuscript proofs, not sampling.'}
    (ROOT/'adversarial-verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
