"""Exact finite replay of the live site's idle-mask and Hodge margin claims."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

def response_states(T,L):
    omega=T*L
    return [q for q in (0,1) if q<=T and omega<=q]

checks={}
def check(name,value):
    checks[name]=bool(value)
    assert value,name

rows=[]
for T,L in product((0,1),repeat=2):
    omega=T*L; I=T*(1-L)
    qs=response_states(T,L)
    rows.append({'T':T,'L':L,'omega':omega,'I':I,'admissible_q':qs})
    check(f'local_decomposition_T{T}L{L}',
          qs==[omega+h for h in (0,1) if h<=I])
check('four_source_strata',[(r['T'],r['L'],r['admissible_q']) for r in rows]==
      [(0,0,[0]),(0,1,[0]),(1,0,[0,1]),(1,1,[1])])
check('only_intact_null_is_nonunique',
      [(r['T'],r['L']) for r in rows if len(r['admissible_q'])>1]==[(1,0)])
check('three_pair_response_count_2_to_m',all(
      (len(response_states(*s[0]))*len(response_states(*s[1]))*len(response_states(*s[2])))
      ==2**sum(T*(1-L) for T,L in s)
      for s in product(tuple(product((0,1),repeat=2)),repeat=3)))

# The identification C_cl^hard := q and T_int^hard := T is a declared
# diagnostic bridge only.  Neither source asserts it across these types.
conditional=[(q,T,L,q*T) for T,L in product((0,1),repeat=2)
             for q in response_states(T,L)]
closed={(q,T) for q,T,L,h in conditional if h==0}
check('conditional_bridge_forbids_C1_T0', (1,0) not in {(q,T) for q,T,_,_ in conditional})
check('conditional_bridge_still_has_two_closed_factor_states',closed=={(0,0),(0,1)})
check('intact_null_allows_two_different_hard_masks',
      {(q*T) for q,T,L,_ in conditional if (T,L)==(1,0)}=={0,1})

def active_margin(x,y):
    x,y=F(x),F(y)
    return F(0) if x*x+y*y==0 else 2*abs(x*y)/(x*x+y*y)
check('hodge_transport_exact_fixtures',
      [active_margin(1,y) for y in (1,F(1,2),F(1,3),0)]==
      [F(1),F(4,5),F(3,5),F(0)])
check('scale_and_orientation_invariance',all(
      active_margin(k*x,k*y)==active_margin(x,y)==active_margin(-x,y)
      for x,y in ((1,1),(2,3),(0,4)) for k in (F(1,2),F(3),F(-2))))
check('soft_margin_not_hard_switch',
      {active_margin(1,1),active_margin(1,F(1,2))}=={F(1),F(4,5)})
# Both source fixture rows declare hard h=1.  This checks the differing soft
# scores; the hard labels are provenance premises, not inferred from x,y.

out={'claim_class':'EXACT replay of live-site idle-mask theorem and Hodge margins; cross-type bridge OPEN',
     'source_edition':'Papers I–III 1.1.1 / IV 0.1; live site inspected 2026-10-10 UTC',
     'local_response_rows':rows,
     'conditional_bridge':'C_cl^hard := q, T_int^hard := T solely for diagnostic comparison; not sourced',
     'conditional_bridge_closed_factor_patterns':sorted([list(x) for x in closed]),
     'hodge_margin_fixtures':['1','4/5','3/5','0'],
     'checks':checks,'passed':sum(checks.values()),
     'physical_promotion':0,'independent_review':'PENDING'}
Path(__file__).with_name('results.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps({'passed':out['passed'],'conditional_closed_patterns':out['conditional_bridge_closed_factor_patterns']}))
