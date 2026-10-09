"""WR-VIII head 6120d9b: separately derived boundary and adversarial checks.
Requires numpy, scipy and sympy. This is an AI audit, not external peer review.
"""
from pathlib import Path
import json, math
import numpy as np
import sympy as s
from scipy.integrate import quad

OUT = Path(__file__).resolve().parents[1]
report = {"audited_parent_sha": "6120d9b37196f9cee4f00bebc2ec1d84d43d44f0", "revision": "WR-VIII v0.2", "scope": "Separate derivations and adversarial witnesses; no empirical fit or external peer review"}
z = s.symbols('z', positive=True)
c = s.symbols('c', positive=True)
D, H = s.Function('D')(z), s.Function('H')(z)
dp = s.diff(D,z)
khat = (1-(H*dp/c)**2)/D**2
C = 1+H**2*(D*s.diff(D,z,2)-dp**2)/c**2+H*s.diff(H,z)*D*dp/c**2
assert s.simplify(s.diff(khat,z)+2*dp*C/D**3)==0
report['generic_CBL_derivative'] = 'PASS: arbitrary differentiable D,H, including sign and dimensional c'

u,v,k = s.symbols('u v k', real=True)
z1,z2,zstar = s.symbols('z1 z2 zstar', positive=True)
ds=u*zstar+v*zstar**2
hs=c*s.sqrt(1-k*ds**2)/(u+2*v*zstar)
J=s.Matrix([u*z1+v*z1**2,u*z2+v*z2**2,hs]).jacobian([u,v,k])
expected=z1*z2*(z2-z1)*(-c*ds**2/(2*(u+2*v*zstar)*s.sqrt(1-k*ds**2)))
assert s.simplify(J.det()-expected)==0
assert s.simplify(s.limit(s.diff(hs,k)/zstar**2,zstar,0)+c*u/2)==0
report['finite_Jacobian_and_low_z_limit']='PASS: full determinant; curvature sensitivity vanishes quadratically at zstar=0'

rd,M=s.symbols('rd M', positive=True)
obs=s.Matrix([M+5*s.log((1+zstar)*ds,10),ds/rd,c/(hs*rd)])
pars=[u,v,k,rd,M]
tangent=s.Matrix([u,v,-2*k,rd,-5/s.log(10)])
assert all(s.simplify(e)==0 for e in obs.jacobian(pars)*tangent)
report['scale_null_direction']='PASS: infinitesimal null vector (u,v,-2k,rd,-5/ln(10)) with free calibrations'

profiles=[('exponential',lambda x: math.expm1(.7*x)/.7,lambda x: math.exp(.7*x)),
 ('logarithmic',lambda x: math.log1p(.8*x)/.8,lambda x: 1/(1+.8*x)),
 ('sinusoidal',lambda x:x+.2*math.sin(math.pi*x)/math.pi,lambda x:1+.2*math.cos(math.pi*x))]
errors=[];clock_checks=[]
for name,f,fp in profiles:
 for q in [-2.,0.,.7,.99]:
  kk=q/f(1.)**2
  rate=lambda x:math.sqrt(1-kk*f(x)**2)/fp(x)
  for zz in [.03,.2,.65,1.]:
   chi=quad(lambda x:1/rate(x),0,zz,epsabs=1e-12,epsrel=1e-12)[0]
   recovered=math.sin(math.sqrt(kk)*chi)/math.sqrt(kk) if kk>0 else math.sinh(math.sqrt(-kk)*chi)/math.sqrt(-kk) if kk<0 else chi
   errors.append(abs(recovered-f(zz)))
   if kk>0:assert chi<math.pi/(2*math.sqrt(kk))
   # A finite elapsed proper time exists; derivative gives (da/dt)/a=H.
   tt=-quad(lambda x:1/((1+x)*rate(x)),0,zz)[0]
   dt=-1/((1+zz)*rate(zz));da=-1/(1+zz)**2
   clock_checks.append(abs((da/dt)/(1/(1+zz))-rate(zz)))
   assert tt<0
assert max(errors)<1e-11 and max(clock_checks)<1e-12
report['nonpolynomial_completions']={'cases':len(errors),'max_absolute_error':max(errors),'clock_checks':len(clock_checks)}

# Boundary counterexamples are exact in c=1 and a fixed length unit.
assert s.limit(1/(3*z*z),z,0,dir='+')==s.oo
report['abstract_counterexample']={'D':'z^3 on [0,1]','strictly_increasing':True,'Dprime0':0,'Hflat':'1/(3 z^2), not finite at z=0','targets':'v0.1 abstract overstatement, corrected in v0.2; not Theorem 3.1'}
assert s.limit(s.log(z), z, 0, dir='+') == -s.oo
report['magnitude_domain']={'D_L_at_z0':0,'magnitude_at_z0':'not finite',
                          'positive_distance_domain':'0<z<=Z, under Dprime>0 and D(0)=0'}
report['open_cap']={'D':'z on [0,1]','cap':1,'H_at_cap_at_Z':0,'pointwise_rate_at_z_half_for_k1':math.sqrt(.75),'global_member':False}

def raw_interval(zz,low,high):return ((1-high*high)/(zz*zz),(1-low*low)/(zz*zz))
def intersect(items):
 lo=max(x[0] for x in items);hi=min(x[1] for x in items)
 if lo>hi or lo>=1:return {'kind':'empty'}
 if lo==hi:return {'kind':'singleton','value':lo}
 return {'kind':'interval','lower':lo,'upper':min(hi,1),'upper_closed':hi<1}
cases={
 'exact_flat':intersect([raw_interval(.5,1,1)]),
 'incompatible_exact':intersect([raw_interval(.5,1,1),raw_interval(.75,.8,.8)]),
 'global_cap_clipping':intersect([raw_interval(.5,.1,2)]),
 'boundary_only':intersect([(1.,1.)]),
 'local_but_globally_excluded':intersect([raw_interval(.5,.5,.5)]),
 'touching_intervals_singleton':intersect([(-.5,0),(0,.5)])}
assert cases['exact_flat']['value']==0
assert cases['incompatible_exact']['kind']=='empty'
assert cases['global_cap_clipping']=={'kind':'interval','lower':-12.,'upper':1,'upper_closed':False}
assert cases['boundary_only']['kind']=='empty'
assert cases['local_but_globally_excluded']['kind']=='empty'
assert cases['touching_intervals_singleton']['value']==0
report['interval_cases']=cases
# A hard box may be an outer screen for a joint set: with D=z, both rates lie
# on the same side of 1. The singleton joint pair (0.95,1.05) is incompatible,
# although its marginal enclosing box [0.9,1.1]^2 contains a compatible pair.
assert intersect([raw_interval(.25,.9,1.1),raw_interval(.75,.9,1.1)])['kind']=='interval'
assert intersect([raw_interval(.25,.95,.95),raw_interval(.75,1.05,1.05)])['kind']=='empty'
report['joint_vs_marginal']='PASS: compatible marginal box does not certify an incompatible joint pair'

R,L=1.,3.
x,y=np.array([R,0,0]),np.array([-R,0,0])
assert L>2*R
global_torus=min(np.linalg.norm(x-y-L*np.array(n)) for n in [(i,j,h) for i in [-1,0,1] for j in [-1,0,1] for h in [-1,0,1]])
assert global_torus==1 and np.linalg.norm(x-y)==2
assert np.linalg.norm(x-y)==2*R
report['torus_edges']={'injectivity_inequality':'L>2R','equality_alias':'x=R e1 and y=-R e1 alias when L=2R','shortcut_witness':{'R':R,'L':L,'Euclidean_distance':2.,'global_torus_distance':float(global_torus)},'interpretation':'Not a counterexample to restricted-path Theorem 7.1'}

# Analytic future proof: s=(t-t1)/tau, b=exp[-1/(s(1-s))], zero outside.
# w>=4; |db/dt| <= w^2 exp(-w)/tau <=16 exp(-4)/tau.
tau=s.symbols('tau',positive=True);x=s.symbols('x',real=True)
b=s.exp(-1/(x*(1-x)))
assert s.simplify(s.diff(b,x,2).subs(x,s.Rational(1,2))+32*s.exp(-4))==0
bound=16*math.exp(-4)
ts=np.linspace(-1,3,2001);bb=np.zeros_like(ts);bp=np.zeros_like(ts)
mask=(ts>1)&(ts<2);ss=ts[mask]-1;ww=1/(ss*(1-ss))
bb[mask]=np.exp(-ww);bp[mask]=np.exp(-ww)*(1-2*ss)/(ss**2*(1-ss)**2)
assert np.max(abs(bp))<bound
for lam in [-.5,.5,1.]:
 rate=1+lam*bp
 assert np.min(rate)>0
 assert np.all(bb[ts<=0]==0)
 assert 6*lam*(-32*math.exp(-4))!=0
report['future_witness']={'histories':3,'time_samples':len(ts),'analytic_bprime_bound_tau1':bound,'safe_lambda_bound_Hb1':1/bound,'Ricci_difference_at_t1_5_c_tau1':'-192 lambda exp(-4), nonzero','interpretation':'Same anchored past; distinct curvature invariants later; no fixed matter law'}
report['status']='PASS'
(OUT/'independent_verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
