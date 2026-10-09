#!/usr/bin/env python3
"""Independent integration/rank/interval/calibration/topology witnesses; synthetic only."""
from pathlib import Path
import json,math,itertools
import numpy as np
import sympy as sp
from scipy.integrate import quad
ROOT=Path(__file__).resolve().parents[1]
C=299792.458;U=C/70

def curved(k,x):
 if k>0:return math.sin(math.sqrt(k)*x)/math.sqrt(k)
 if k<0:return math.sinh(math.sqrt(-k)*x)/math.sqrt(-k)
 return x

def main():
 z,u,v,k,c=sp.symbols('z u v k c',positive=True)
 D=u*z+v*z**2;dp=sp.diff(D,z);H=c*sp.sqrt(1-k*D**2)/dp
 estimator=(1-(H*dp/c)**2)/D**2
 assert sp.simplify(estimator-k)==0
 cbl=1+H**2/c**2*(D*sp.diff(D,z,2)-dp**2)+H*sp.diff(H,z)/c**2*D*dp
 assert sp.simplify(cbl)==0
 derivative=sp.diff(H,k)
 assert sp.simplify(derivative+c*D**2/(2*dp*sp.sqrt(1-k*D**2)))==0
 z1,z2=sp.symbols('z1 z2',positive=True)
 det=sp.Matrix([[z1,z1**2],[z2,z2**2]]).det();assert sp.factor(det-z1*z2*(z2-z1))==0
 reports={'symbolic':{'status':'PASS','identities':4}}
 count=0;maximum=0.;inv=0;rank=0;scale=0;interval=0;screen=0;clipped=0
 families=list(itertools.product([1.,3.,U],[-.2,0.,.2],[-.4,-.2,0.,.1,.2]))
 for uu,aa,qq in families:
  vv=uu*aa;kk=qq/uu**2
  dist=lambda zz:uu*(zz+aa*zz**2)
  slope=lambda zz:uu*(1+2*aa*zz)
  rate=lambda zz:C*math.sqrt(1-kk*dist(zz)**2)/slope(zz)
  cap=1/dist(1.5)**2;assert kk<cap and slope(1.5)>0
  for zz in [0.,.001,.05,.2,.5,.9,1.2,1.5]:
   chi=quad(lambda zz:C/rate(zz),0,zz,epsabs=1e-10,epsrel=1e-12)[0]
   expected=dist(zz);error=abs(curved(kk,chi)-expected)/max(1.,abs(expected));maximum=max(maximum,error);assert error<2e-12;count+=1
   if kk>0:assert chi<math.pi/(2*math.sqrt(kk))
  zz1,zz2=.4,1.1;yy1,yy2=dist(zz1),dist(zz2)
  vv2=(yy2/zz2-yy1/zz1)/(zz2-zz1);uu2=(zz2*yy1/zz1-zz1*yy2/zz2)/(zz2-zz1)
  assert abs(vv-vv2)<1e-9 and abs(uu-uu2)<1e-9;inv+=1
  zs=.75;kk2=(1-(rate(zs)*slope(zs)/C)**2)/dist(zs)**2;assert abs(kk-kk2)*uu**2<1e-12;inv+=1
  # Numeric rank in well-scaled finite parameters (u,v,q), using central differences.
  par=np.array([2.,2.*aa,qq]);step=1e-5
  def responses(p):
   us,vs,qs=p;d=us*zs+vs*zs**2;return np.array([us*zz1+vs*zz1**2,us*zz2+vs*zz2**2,math.sqrt(1-qs*d*d/us**2)/(us+2*vs*zs)])
  matrix=np.column_stack([(responses(par+step*np.eye(3)[j])-responses(par-step*np.eye(3)[j]))/(2*step) for j in range(3)])
  assert np.linalg.matrix_rank(matrix,tol=1e-9)==3
  ds=par[0]*zs+par[1]*zs**2;dps=par[0]+2*par[1]*zs
  analytic=zz1*zz2*(zz2-zz1)*(-ds**2/(2*par[0]**2*dps*math.sqrt(1-qq*ds**2/par[0]**2)))
  assert abs(np.linalg.det(matrix)-analytic)<1e-9;rank+=1
  for frac in [.005,.02,.10]:
   hp=rate(1.);low=hp*(1-frac);high=hp*(1+frac)
   km=(1-(high*slope(1)/C)**2)/dist(1)**2;kp=(1-(low*slope(1)/C)**2)/dist(1)**2
   assert km<=kk<=kp
   # The rate interval is local; the global branch is a separate open constraint.
   # A raw upper endpoint beyond cap is clipped, never admitted as a completion.
   if kp>=cap:clipped+=1
   assert abs(C*math.sqrt(1-km*dist(1)**2)/slope(1)-high)<1e-7
   assert abs(C*math.sqrt(1-kp*dist(1)**2)/slope(1)-low)<1e-7
   interval+=1
   for candidate in np.linspace(min(km,kk)-.1/uu**2,max(kp,kk)+.1/uu**2,201):
    if candidate>=cap:continue
    hr=C*math.sqrt(1-candidate*dist(1)**2)/slope(1)
    assert (km<=candidate<=kp)==(low-1e-8<=hr<=high+1e-8);screen+=1
  for lam in [.2,.8,1.5,3.]:
   for zz in [.2,.7,1.3]:
    dd=dist(zz);hh=rate(zz);rd=147.;mag=-19.3
    lhs=np.array([dd/rd,C/(hh*rd),mag+5*math.log10((1+zz)*dd)])
    rhs=np.array([lam*dd/(lam*rd),C/((hh/lam)*(lam*rd)),mag-5*math.log10(lam)+5*math.log10((1+zz)*lam*dd)])
    assert np.max(abs(lhs-rhs))<1e-10;scale+=1
 reports['curved_distance_integration']={'status':'PASS','cases':count,'max_relative_error':maximum}
 reports['finite_parameter_inversion']={'status':'PASS','cases':inv}
 reports['central_difference_rank']={'status':'PASS','cases':rank,'parameters':'u,v,q; c=1 for rank scaling'}
 reports['interval_endpoints']={'status':'PASS','cases':interval,'candidate_equivalence_checks':screen,'global_branch_clipped_intervals':clipped,'open_global_upper_bound_preserved':True}
 reports['calibration_scaling']={'status':'PASS','cases':scale}
 # Explicit incompatible positive rates in the declared synthetic family.
 f=lambda zz:zz-.15*zz**2;g=lambda zz:1-.3*zz
 qflat=(1-(100*g(1)/70)**2)/f(1)**2
 qconflict=(1-(100*g(.5)/70)**2)/f(.5)**2
 assert abs(qflat)<1e-14 and abs(qconflict-qflat)>.1
 reports['incompatible_rates']={'status':'PASS','z1':1.,'H1':100,'q1':qflat,'z2':.5,'H2':100,'q2':qconflict}
 rng=np.random.default_rng(8649);R=1.1625;points=rng.normal(size=(600,3));points/=np.linalg.norm(points,axis=1)[:,None];points*=rng.uniform(0,R,(600,1))
 checks=0
 for side in [2.1*R,3*R,5*R]:
  for n in itertools.product([-1,0,1],repeat=3):
   if not any(n):continue
   shifted=points+side*np.array(n);assert np.all(np.linalg.norm(shifted,axis=1)>R);checks+=len(points)
 reports['torus_patch_aliases']={'status':'PASS','checks':checks,'scope':'finite lattice witnesses; full injectivity follows from norm proof'}
 ts=np.linspace(-.3,1.1,1501);b=np.zeros_like(ts);bp=np.zeros_like(ts);mask=(ts>.3)&(ts<.8);tm=ts[mask];prod=(tm-.3)*(.8-tm)
 b[mask]=np.exp(16-1/prod);bp[mask]=b[mask]*(1.1-2*tm)/prod**2
 assert np.max(abs(bp))<=128
 for lam in [-1/256,-1/512,1/512,1/256]:
  h=1+lam*bp;a=np.exp(ts+lam*b);assert np.all(h>.49);assert np.array_equal(a[ts<=0],np.exp(ts[ts<=0]));assert np.max(abs(a-np.exp(ts)))>0
 reports['future_matching']={'status':'PASS','histories':4,'time_points':len(ts),'analytic_derivative_upper_bound':128,'scope':'synthetic time unit; b=e^(16-1/((t-.3)(.8-t))) on (.3,.8)'}
 qlo=(1-1.02**2)/.85**2;qhi=(1-.98**2)/.85**2
 reports['unit_passport']={'synthetic':True,'c_km_per_s':C,'H0_km_per_s_per_Mpc':70,'u_Mpc':U,'v_Mpc':-.15*U,'Z':1.5,'q_open_upper_bound':1/f(1.5)**2,'q_interval':[qlo,qhi],'rate_interval_km_per_s_per_Mpc':[98,102]}
 reports['status']='PASS';reports['scope']='Finite synthetic witnesses accompany self-contained proofs; no catalogue fit, confidence calibration, matter admissibility or exhaustive novelty certificate.'
 (ROOT/'verification.json').write_text(json.dumps(reports,indent=2)+'\n');print(json.dumps(reports,indent=2))
if __name__=='__main__':main()
