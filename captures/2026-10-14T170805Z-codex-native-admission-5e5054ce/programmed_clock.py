"""Supplied finite-word clock; engineered weighted path, not native tetrahedral selection."""
from fractions import Fraction as Q
from math import comb,sin,cos,pi,sqrt
from dataclasses import asdict
from joint_carrier import Carrier,witness

def path_metrics(n):
    if type(n) is not int or n<2 or n%2:raise ValueError('Even positive word length required for full ordinary path Hodge representation.')
    v=[Q(1)];e=[]
    for r in range(n//2):
        e.append(v[r]/((2*r+1)*(n-2*r)))
        v.append(e[-1]*(2*r+2)*(n-2*r-1))
    return v,e

def characteristic_clock(n):
    # Ascending integer coefficients of the tridiagonal determinant; no square-root rounding.
    prev=[1];cur=[0,1]
    for j in range(n):
        out=[0]+cur
        for k,a in enumerate(prev):out[k]-=(j+1)*(n-j)*a
        prev,cur=cur,out
    return cur

def clock_snapshot(n,xi):
    # xi=kappa*t/pi is an internal normalized phase, not seconds.
    a=sin(pi*xi);b=cos(pi*xi)
    probs=[comb(n,j)*a**(2*j)*b**(2*(n-j)) for j in range(n+1)]
    terminal=max(0.,min(1.,probs[-1]))
    return {'xi':xi,'clock_probabilities':probs,'terminal_probability':terminal,
      'full_joint_terminal_trace_distance':sqrt(max(0.,1-terminal)),
      'scope':'Floating diagnostics of the exact binomial clock formulas; ideal arbitrary payload/spectator state, no continuous monitoring.'}

def compiled_word(branch='C',ticks=4,resets=1,pad=True):
    old=witness(branch,ticks,resets);spec=old['specification'];c=Carrier(spec['successor'],spec['receipt'],spec['record_dimension'],ticks,resets)
    x=c.prepared();prefix=[{'address':0,'operation':'PREPARATION','active':asdict(x.active),'donors':list(map(asdict,x.donors))}]
    for k in range(c.L-1):
        a=c.action(x.clock);x=c.step(x);prefix.append({'address':k+1,'operation':a['kind'],'active':asdict(x.active),'donors':list(map(asdict,x.donors))})
    K=c.L-1;n=K+(int(bool(pad)) if K%2 else 0)
    if n>K:prefix.append({**prefix[-1],'address':n,'operation':'IDENTITY_PADDING'})
    v,e=path_metrics(n) if n%2==0 else ([],[])
    data=c.resources()['payload_dimension']**(resets+1)
    return {'branch':branch,'version':'0.1','original_word_length':K,'word_length':n,'padding_gates':n-K,
      'clock_addresses':n+1,'data_bank_dimension':data,'complete_joint_dimension':(n+1)*data,
      'per_component_vertices':n//2+1 if n%2==0 else None,'per_component_edges':n//2 if n%2==0 else None,
      'weighted_path_components':data if n%2==0 else None,'kernel_dimension':data if n%2==0 else 0,
      'unit_rate_vertex_metrics':list(map(str,v)),'unit_rate_edge_metrics':list(map(str,e)),
      'clock_spectrum_over_kappa':[n-2*j for j in range(n+1)],'characteristic_clock_coefficients':characteristic_clock(n),
      'norm_over_kappa':n,'initial_variance_over_kappa_squared':n,'interaction_norm_upper_bound_over_kappa':2*n,
      'terminal_kappa_t':'pi/2','return_kappa_t':'pi','return_global_phase':(-1)**n,
      'payload_reset_count':resets,'history_cells':(resets+1)*ticks,'receipt_cells':(resets+1)*ticks,
      'prefixes':prefix,'specification':spec,
      'phase_samples':[clock_snapshot(n,x) for x in [0,.125,.25,.375,.5,.625,.75,.875,1]],
      'status':'EXACT CONDITIONAL SUPPLIED WORD / CANDIDATE ENGINEERED GEOMETRY',
      'physical_promotion':0,'independent_human_review':'PENDING'}

if __name__=='__main__':
    import json
    from pathlib import Path
    p=Path(__file__).parent/'dist/sources/programmed-clock-v0.1';p.mkdir(parents=True,exist_ok=True)
    (p/'PROGRAMMED_CLOCK_WITNESS_v0.1.json').write_text(json.dumps({'version':'0.1','branches':{b:compiled_word(b) for b in ['C','H']}},indent=2)+'\n')
