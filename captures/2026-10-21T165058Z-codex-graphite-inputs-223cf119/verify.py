from fractions import Fraction as F
import math,json
from pathlib import Path
# Source Eq24; carbon-12 mass used as a declared numerical evaluation convention.
phi=F(27,10); omega=F(120000000000000); mass=12*F('1.66053906660e-27')
rate=3*math.pi/2*float(phi*phi/(mass*mass*omega**3))
assert 0.049 < rate*1e-12 < 0.051
assert F('0.1')/F('0.05')==2
# weak-damping oscillator q''+r q'+w0^2 q=0:
# amplitude e^(-r t/2), energy envelope e^(-r t).
# numerical values are not independently measured lifetimes.
out={'status':'PASS_SCOPED_NUMERICAL_REPLAY','source':'arXiv:2306.00205v2 Eq24','phi_N_per_m':str(phi),'omega_rad_per_s':str(omega),'mass_kg':str(mass),'rate_per_ps':rate*1e-12,'per_atom_Gamma_kg_per_s':float(mass)*rate,'approx_energy_envelope_time_ps':1/(rate*1e-12),'approx_amplitude_envelope_time_ps':2/(rate*1e-12),'scope':'Re-evaluation of published approximate substrate bath model; not angle-specific measured damping, friction or prediction.','physical_promotion':0}
Path(__file__).with_name('RESULTS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
