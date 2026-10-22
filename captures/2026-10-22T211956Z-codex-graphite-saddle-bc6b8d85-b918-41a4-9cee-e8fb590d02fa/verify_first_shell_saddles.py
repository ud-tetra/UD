#!/usr/bin/env python3
"""Exact critical values, Hessian signs, barriers and equilibrium load slopes."""
from fractions import Fraction as Q
import json

# Exact cosines at all stationary points; sin conditions can be
# checked from {0, pi, +/-2pi/3}, with sin(2pi/3)=sqrt(3)/2.
points={
 'maximum':((0,0), (Q(1),Q(1),Q(1))),
 'minimum_plus':(('2pi/3','2pi/3'),(Q(-1,2),Q(-1,2),Q(-1,2))),
 'minimum_minus':(('-2pi/3','-2pi/3'),(Q(-1,2),Q(-1,2),Q(-1,2))),
 'saddle_a':(('pi',0),(Q(-1),Q(1),Q(-1))),
 'saddle_b':((0,'pi'),(Q(1),Q(-1),Q(-1))),
 'saddle_ab':(('pi','pi'),(Q(-1),Q(-1),Q(1)))
}
for label,(_,c) in points.items():
    ca,cb,cab=c
    S=sum(c)
    H=((-ca-cab,-cab),(-cab,-cb-cab))
    det=H[0][0]*H[1][1]-H[0][1]*H[1][0]
    if label=='maximum':assert S==3 and det>0 and H[0][0]<0
    elif label.startswith('minimum'):assert S==Q(-3,2) and det>0 and H[0][0]>0
    else:assert S==-1 and det<0
# Stationary solution completeness: sin(a)=sin(b) implies a=b or a=pi-b.
# In the first branch sin(a)*(1+2*cos(a))=0; in the second sin(a)=0.
# The resulting six points above exhaust the 2pi-periodic phase torus.
# The separating level S=-1 follows identically from
# S+1=4 cos(a/2)cos(b/2)cos((a+b)/2).
range_multiplier=2*(Q(3)-Q(-3,2))
positive_barrier=2*(Q(-1)-Q(-3,2))
negative_barrier=2*(Q(3)-Q(-1))
assert (range_multiplier,positive_barrier,negative_barrier)==(9,1,8)

# Exactly solvable vertical energy: E= k(z-zref)^2/2 + f(a+bz),
# f=2S. With compressive load L, eliminate z exactly.
k=Q(20);zref=Q(2);L=Q(1)
def z(f,derivative,load):return zref-(load+f*derivative)/k
def H(f,amplitude,derivative,load):
    return f*(amplitude+derivative*zref)+load*zref-(load+f*derivative)**2/(2*k)
for amplitude,derivative,fmin,fsaddle,c in [
    (Q(10),Q(1),Q(-3),Q(-2),Q(1)),
    (Q(-10),Q(-1),Q(6),Q(-2),Q(8))
]:
    barrier=lambda load:H(fsaddle,amplitude,derivative,load)-H(fmin,amplitude,derivative,load)
    delta_z=z(fsaddle,derivative,L)-z(fmin,derivative,L)
    assert barrier(L)>0
    assert (barrier(L+Q(1,7))-barrier(L))/Q(1,7)==delta_z
    assert delta_z==-(fsaddle-fmin)*derivative/k
    assert abs(fsaddle-fmin)==c
# The old 9 multiplier tests the range, never the path barrier.
assert positive_barrier!=range_multiplier and negative_barrier!=range_multiplier
print(json.dumps({'status':'PASS_EXACT_CONDITIONAL',
 'global_range_multiplier':9,'minimum_path_barrier_V_positive':1,
 'minimum_path_barrier_V_negative':8,
 'stationary_point_counts':{'max':1,'min':2,'saddle':3},
 'minimum_saddle_load_identity_exact_examples':True},indent=2))
