#!/usr/bin/env python3
"""Exact finite witnesses for WR-VI; standard library, not proof replacement."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

def matrix(a,b,c):
    return ((1-a-b,a,b),(a,1-a-c,c),(b,c,1-b-c))

def feasible(p):
    return all(v >= 0 for row in p for v in row) and all(sum(r)==1 for r in p)

def response(p,f=(F(0),F(1,2),F(1))):
    return tuple(sum(v*w for v,w in zip(row,f)) for row in p)

def activity(p):
    return sum(p[i][j] for i in range(3) for j in range(3) if i!=j)/3

def irreducible(p):
    for source in range(3):
        reached={source}
        while True:
            more={j for i in reached for j in range(3) if p[i][j]>0}
            new=reached|more
            if new==reached: break
            reached=new
        if len(reached)!=3: return False
    return True

def main():
    target=(F(1,4),F(1,2),F(3,4))
    total=fibre=0
    points=[]
    for ia,ib,ic in product(range(25),repeat=3):
        a,b,c=(F(v,24) for v in (ia,ib,ic))
        p=matrix(a,b,c)
        if not feasible(p): continue
        total+=1
        assert all(p[i][j]==p[j][i] for i in range(3) for j in range(3))
        assert all(sum(p[i][j] for i in range(3))==1 for j in range(3))
        if response(p)!=target: continue
        fibre+=1; points.append(p)
        t=(a-F(1,6))/2
        assert F(-1,12)<=t<=F(1,6)
        assert (a,b,c)==(F(1,6)+2*t,F(1,6)-t,F(1,6)+2*t)
        assert activity(p)==F(1,3)+2*t==F(1,6)+a
        assert irreducible(p)==(t>F(-1,12))
    # Independently generate the continuous formula at 301 rational positions.
    curve=0
    for i in range(301):
        t=F(-1,12)+F(i,1200)
        p=matrix(F(1,6)+2*t,F(1,6)-t,F(1,6)+2*t)
        assert feasible(p) and response(p)==target
        assert irreducible(p)==(i>0)
        curve+=1
    threshold=F(1,6)
    star=matrix(F(0),F(1,4),F(0))
    assert activity(star)==threshold and not irreducible(star)
    cap_checks=0
    for units in range(601):
        cap=F(units,600)
        if cap<threshold:
            assert all(activity(p)>cap for p in points)
        elif cap==threshold:
            assert [p for p in points if activity(p)<=cap]==[star]
        else:
            # Two distinct continuous feasible witnesses, even below lattice spacing.
            dt=min(F(1,8),(cap-threshold)/4)
            p1=matrix(2*dt,F(1,4)-dt,2*dt)
            p2=matrix(dt,F(1,4)-dt/2,dt)
            assert p1!=p2 and all(feasible(p) and response(p)==target and
                activity(p)<=cap and irreducible(p) for p in [p1,p2])
        cap_checks+=1
    # Actual sufficient Farkas witness, not just a solver's verdict.
    A=((F(1,2),F(1),F(0)),(F(-1,2),F(0),F(1,2)))
    d=(F(1,4),F(0)); H=(F(2,3),)*3
    lam=(F(-2,3),F(-4,3)); mu=F(1)
    assert tuple(sum(A[i][j]*lam[i] for i in range(2))+mu*H[j]
                 for j in range(3))==(F(1),F(0),F(0))
    cert_gap=sum(v*w for v,w in zip(d,lam))+F(3,20)
    assert cert_gap==F(-1,60)
    tolerance_checks=0
    for eps in [F(1,1000),F(1,100),F(1,10)]:
        for weight in [F(0),F(1,4),F(1,2),F(3,4),F(1)]:
            b=F(1,4)-eps*weight
            p=matrix(F(0),b,F(0))
            assert feasible(p) and activity(p)<=threshold
            assert max(abs(v-w) for v,w in zip(response(p),target))<=eps
            tolerance_checks+=1
    quantifier_checks=0
    for mid in [F(3,20),threshold,F(1,5),F(1,4),F(2,3)]:
        for delta in [F(0),F(1,600),F(1,60),F(1,20)]:
            lower=max(F(0),mid-delta);upper=mid+delta
            for p in points:
                test=[activity(p)<=v for v in [lower,mid,upper]]
                assert all(test)==(activity(p)<=lower)
                assert any(test)==(activity(p)<=upper)
                quantifier_checks+=1
    uniform=((F(1,3),)*3,)*3;energy=(F(0),F(1),F(2))
    mean=sum(uniform[i][j]*(energy[j]-energy[i])/3 for i in range(3) for j in range(3))
    squared=sum(uniform[i][j]*(energy[j]-energy[i])**2/3 for i in range(3) for j in range(3))
    assert mean==0 and squared==F(4,3)
    report={'status':'PASS','arithmetic':'exact fractions; no random sampling',
        'feasible_lattice_matrices':total,'exact_response_lattice_matrices':fibre,
        'continuous_fibre_checks':curve,'activity_cap_checks':cap_checks,
        'tolerance_witness_checks':tolerance_checks,'quantifier_checks':quantifier_checks,
        'threshold':'1/6','threshold_matrix_irreducible':False,
        'dual_certificate_at_cap_3_20':{'coefficient_vector':['1','0','0'],'gap':str(cert_gap)},
        'energy_counterexample':{'mean':str(mean),'mean_square':str(squared)},
        'scope':'finite witnesses; general propositions rely on manuscript proofs'}
    (ROOT/'verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__': main()
