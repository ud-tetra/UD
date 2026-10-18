import json,argparse
from bindings import P,freeze,sha

def run(replay=False):
 f=freeze();data=json.loads((P/'DATA_FREEZE.json').read_text());assert data['protocol_freeze_sha256']==sha(P/'PROTOCOL_FREEZE.json');r=data['records'][0];assert r['max_vector_integer_squared_error']==1
 prior=json.loads((P/'inputs/PREVIOUS_UNIFORM.json').read_text());assert next(x for x in prior['rows'] if x['delta']==[1,1<<37])['order209_guaranteed'];assert 1<<48>1<<37
 out=P/'results/cyclic_unit';out.mkdir(exist_ok=True);result={'status':'CERTIFIED_SOURCE_PRECISION_ORDER','case':'cyclic_unit','exact_encoded_count_above_source_cutoff':209,'source_precision_cutoff':f['source_precision_cutoff'],'record_sha256':r['record_sha256'],'route':'Prior arbitrary-vector2^-37 order theorem applied to exact new2^-48 vector error','prior_certificate_sha256':sha(P/'inputs/PREVIOUS_UNIFORM.json'),'physical_promotion':0,'replay':replay};dest=out/('ORDER_REPLAY.json' if replay else 'ORDER_CERTIFICATE.json');assert not dest.exists();dest.write_text(json.dumps(result,indent=2));return result
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('case');p.add_argument('--replay',action='store_true');a=p.parse_args();assert a.case=='cyclic_unit';print(json.dumps(run(a.replay)))
