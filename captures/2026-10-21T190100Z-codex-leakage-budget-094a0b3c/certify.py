from pathlib import Path
from fractions import Fraction as F
import hashlib,json
P=Path(__file__).resolve().parent;root=P.parents[1];c=json.loads((P/'CONTRACT.json').read_text());basepath=root/c['base_certificate'];base=json.loads(basepath.read_text())
assert base['status']=='PASS_EXACT_RATIONAL_CONDITIONAL_BUDGET' and base['physical_promotion']==0
kernel=root/'captures/2026-10-21T173313Z-codex-local-quadrature-8ba1d409/KERNEL.csv'
assert hashlib.sha256(kernel.read_bytes()).hexdigest()==base['kernel_sha256']
def upper(key):
 q=F(base[key]['fraction']);d=10**12
 return F(-((-q.numerator*d)//q.denominator),d)
R=upper('continuous_band_error_upper');H=upper('H0_l1_upper');C0=upper('baseline_leak_upper');fp=F(1,1<<30);fixed=R+3*C0+fp
T=F(1,1000);eps=F(1,4000);cap=F(99,10000);delay=F(1024,1953125)
def bound(t,e):return fixed+(H+1)*t+H*e
D=bound(T,eps);ratio=2*D;phase=F(100,99)*ratio
assert D<cap and ratio<F(1,10) and phase<F(1,50) and delay<F(3,5000)
shares={'noise_and_quantization_V':F(1,10000),'gain_V':F(1,20000),'timing_V':F(1,20000),'baseline_variation_V':F(1,20000)}
assert sum(shares.values())==eps
assert F(1,100000)*5==shares['gain_V'];assert F(1,5000000000)*250000==shares['timing_V']
fc=F(257*1953125,16184);slope_upper=F(44,7)*((fc+50)+200000*T);assert slope_upper<250000
assert 1+T+3+eps<5
Tmax=(cap-fixed-H*eps)/(H+1);epsmax=(cap-fixed-(H+1)*T)/H
assert T<Tmax and eps<epsmax
assert bound(F(1,500),eps)>cap and bound(T,F(1,1000))>cap
# Distinguish full-state and in-band-only targets: the missing reference tail costs exactly T in this sufficient bound.
inband=fixed+H*T+H*eps;assert D-inband==T
# Exact frontier controls; no floating threshold decisions.
assert bound(Tmax,eps)==cap and bound(Tmax+F(1,10**12),eps)>cap
assert bound(T,epsmax)==cap and bound(T,epsmax+F(1,10**12))>cap
def datum(x):return {'fraction':str(x),'approximation':float(x)}
out={'status':'PASS_EXACT_CONDITIONAL_LEAKAGE_BUDGET','physical_promotion':0,'contract_sha256':hashlib.sha256((P/'CONTRACT.json').read_bytes()).hexdigest(),'base_certificate_sha256':hashlib.sha256(basepath.read_bytes()).hexdigest(),'kernel_sha256':base['kernel_sha256'],'inherited_rounded_upper':{'R':datum(R),'H0':datum(H),'constant_baseline_leak':datum(C0)},'fixed_error_V':datum(fixed),'tail_contribution_V':datum((H+1)*T),'instrument_contribution_V':datum(H*eps),'full_error_upper_V':datum(D),'phase_upper_rad':datum(phase),'joint_error_cap_V':datum(cap),'unallocated_output_margin_V':datum(cap-D),'max_tail_at_frozen_input_V':datum(Tmax),'max_input_at_frozen_tail_V':datum(epsmax),'allocation':{k:datum(v) for k,v in shares.items()},'timing_source_derivative_upper_V_per_s':datum(slope_upper),'availability_delay_s':datum(delay),'negative_controls':{'tail_1over500_sufficient_bound':datum(bound(F(1,500),eps)),'input_1over1000_sufficient_bound':datum(bound(T,F(1,1000))),'target_missing_tail_difference_V':datum(D-inband),'frontier_equality_and_beyond':'PASS_EXACT'},'limits':'All source/instrument numbers are proposed requirements, not measurements; generic tail theorem permits aliasing.200kHz physical cutoff is used only for illustrative timing slope. Prior empirical gates unchanged.'}
(P/'CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k in ['status','full_error_upper_V','phase_upper_rad','unallocated_output_margin_V','max_tail_at_frozen_input_V','max_input_at_frozen_tail_V','timing_source_derivative_upper_V_per_s']},indent=2))
