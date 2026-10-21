from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import json
P=Path(__file__).resolve().parent
s=Q(61,27648);h=s*(Q(1,384)-Q(1,8192));tau=Q(5,2)**41/factorial(41)/(1-Q(5,84));ad=4096*(4096*tau+Q(6240,2**104))+Q(52,2**96);EY=Q(3,2**127)+Q(504,2**96);delta=45*(ad+EY);eta=45*EY;alpha=delta/h+delta/(h-delta);beta=454*h/(h-delta)
impl=(2*eta+Q(1,2**64))/(h-delta)+Q(52,2**96);reference=impl+908*alpha;truth=alpha+455*Q(1,2**50)+impl
p=160;den=192+p;lift_den=96+p
checks={'positive_frame_floor':h>delta,'full_projection_defect_lt2^-55':alpha<Q(1,2**55),'gain_lt455':beta<455,'fixed_implementation_lt2^-46':impl<Q(1,2**46),'exact_B0_record_comparison_lt2^-44':reference<Q(1,2**44),'conditional_truth_profile_lt2^-40':truth<Q(1,2**40),'residual_norm_den352':den==352,'residual_squared_den704':2*den==704,'residual_integer_threshold576':2*den-128==576,'lift_den256':lift_den==256,'lift_squared_den512':2*lift_den==512,'lift_integer_threshold424':2*lift_den-88==424,'lift52grid_lt2^-90':Q(52,2**96)<Q(1,2**90),'residual_gate_strict_boundary_pass':Q(2**576-1,2**704)<Q(1,2**128),'residual_gate_strict_boundary_reject':not Q(2**576,2**704)<Q(1,2**128),'lift_intrinsic_floor_bound':Q(2640*2**320,2**512)<Q(1,2**88)}
assert all(checks.values()),checks
rat=lambda x:[x.numerator,x.denominator]
(P/'BOUND_CHECKS.json').write_text(json.dumps({'status':'PASS','checks':checks,'exact':{k:rat(v)for k,v in {'h':h,'delta':delta,'eta':eta,'alpha':alpha,'beta':beta,'fixed_record_implementation':impl,'exact_B0_record_comparison':reference,'conditional_truth_profile':truth}.items()},'scope':'source-bound deterministic arithmetic envelopes; physical truth/input premises remain unsupplied','physical_promotion':0},indent=2,sort_keys=True)+'\n');print('PASS16exactfixedboundsandstrictscalecontrols')
