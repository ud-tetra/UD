"""Cross-check manuscript geometry and cited exact capture statuses; no empirical fit."""
from fractions import Fraction as Q
from math import acos,degrees,isclose
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[2]
CAPTURES={
 'coarse':'2026-10-22T184127Z-codex-octa-coarse-3ddfe996-c702-4694-9e18-0b84add389f1',
 'correlated':'2026-10-22T192310Z-codex-octa-correlated-metric-a65b3c9f-0abf-4038-b9d3-59d6a0aa8c23',
 'locality':'2026-10-22T192713Z-codex-octa-zero-locality-463c4c55-8dec-46ce-87ef-6a2d9b4ec52a',
 'spring':'2026-10-22T193247Z-codex-octa-spring-response-74f9cf83-d28e-43b5-a1ad-85739f1c6112'
}

def main():
 m,n=2,1
 cosine=Q(m*m+4*m*n+n*n,2*(m*m+m*n+n*n))
 assert cosine==Q(13,14)
 smaller=degrees(acos(float(cosine)));larger=60-smaller
 assert isclose(smaller,21.8,abs_tol=0.05)
 assert isclose(larger,38.2,abs_tol=0.05)
 assert round(smaller,1)+round(larger,1)==60
 entries={key:json.loads((ROOT/'captures'/capture/'RESULTS.json').read_text())
          for key,capture in CAPTURES.items()}
 assert entries['coarse']['coarse_f']==[4,6,4,1]
 assert entries['coarse']['fine_f']==[11,30,32,12]
 assert entries['coarse']['subdivision_gram_by_grade']==[1,2,4,12]
 assert entries['coarse']['leakage_fraction_of_squared_action']=='11/31'
 assert entries['correlated']['exact_seed_generator_intertwining']
 assert entries['locality']['sharp_min_BtH0S0u_squared_for_unit_coarse_metric']==4
 assert entries['spring']['static_centroid_old']=='-3ab/(2a+b+mu) < 0 for a,b>0,mu>=0'
 result={'status':'PASS_CONSTRUCTOR_ONLY','angle_cosine':'13/14',
         'angle_degrees':[smaller,larger],
         'sum_degrees':smaller+larger,
         'parent_capture_checks':list(CAPTURES),
         'empirical_peak_height':None,'empirical_peak_load_slope':None,
         'UD_residual_prediction':None,
         'physical_promotion':0}
 (Path(__file__).parent/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result))

if __name__=='__main__':main()
