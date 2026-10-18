"""Noisy-record order: charge exact added noise; DC stays in stationary span."""
import argparse,json
import numpy as np
from flint import arb,fmpq,ctx
from bindings import P,freeze,case,sha
from noise_math import noise_upper
from proof_math import up,down
ctx.prec=512

def run(n,replay=False):
 f=freeze();e=case(n);data=json.loads((P/'DATA_FREEZE.json').read_text());r=next(x for x in data['records'] if x['case']==n);assert data['noise_freeze_sha256']==sha(P/'NOISE_FREEZE.json');base=json.loads((P/'inputs/BASE_ORDER_CERTIFICATE.json').read_text());o=P/'results'/n;o.mkdir(exist_ok=True);gp=P/f"NOISE_GRAM_{e['mode']}.npz";assert sha(gp)==r['unit_noise_Gram_sha256']
 with np.load(gp,allow_pickle=False) as z:G=np.array([[int(x) for x in row] for row in z['integers_decimal']],object)
 assert G.shape==(321,321) and np.array_equal(G,G.T);b=noise_upper(G,e['integer_amplitude']);s0=arb(fmpq(*base['qth_sigma_lower']));eps0=arb(fmpq(*base['qplus1_sigma_upper']));cut=arb(fmpq(*f['source_precision_cutoff']));lower=s0-b
 tail=eps0 if e['mode']=='coherent_dc' else eps0+b
 passed=bool(lower>cut and tail<cut)
 result={'status':'CERTIFIED_SOURCE_PRECISION_ORDER' if passed else 'HOLD_NOISY_ORDER_BOUND','case':n,'source_comparison_rank_upper':209,'exact_encoded_count_above_source_cutoff':209 if passed else None,'qth_sigma_lower':down(lower),'qplus1_sigma_upper':up(tail),'added_noise_sketch_norm_upper':up(b),'source_precision_cutoff':f['source_precision_cutoff'],'noise_Gram_sha256':sha(gp),'record_sha256':r['record_sha256'],'stationary_noise_absorbed_in_model':e['mode']=='coherent_dc','source_tail_includes_actual_added_noise':True,'readable':{'qth_sigma_lower':float(lower.lower()),'qplus1_sigma_upper':float(tail.upper()),'added_noise_sketch_norm_upper':float(b.upper())},'physical_promotion':0,'replay':replay}
 dest=o/('ORDER_REPLAY.json' if replay else 'ORDER_CERTIFICATE.json');assert not dest.exists();dest.write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2));return result
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('case');p.add_argument('--replay',action='store_true');a=p.parse_args();run(a.case,a.replay)
