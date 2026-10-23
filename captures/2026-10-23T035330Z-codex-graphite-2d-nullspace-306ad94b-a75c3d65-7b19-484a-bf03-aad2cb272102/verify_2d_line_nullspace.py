#!/usr/bin/env python3
"""Check a D6-periodic Fourier-shell perturbation invisible on the archived line.

Dimensionless phase coordinates u=kx*x, v=ky*y, kx=sqrt(3)*ky.
Base first-shell PES is U1*[2*cos(v)*cos(u)+cos(2*v)].
This is a counterexample about inverse identifiability, NOT a graphite force law.
"""
import heapq
import json
import math
from pathlib import Path

import numpy as np

U1_MICROEV = 0.07933966537954996  # source-profile fit from prior capture


def base(u,v):
    return 2*np.cos(v)*np.cos(u)+np.cos(2*v)


def invisible(u,v):
    return (1-np.cos(u-3*v))*(1-np.cos(u+3*v))*(1-np.cos(2*u))


def minimax(n,epsilon_ratio):
    assert n%12==0
    phases=-math.pi+2*math.pi*np.arange(n)/n
    u,v=np.meshgrid(phases,phases,indexing='ij')
    landscape=base(u,v)+epsilon_ratio*invisible(u,v)
    # AB minima in the first-harmonic model: u=0,v=2pi/3 and u=pi,v=pi/3.
    start=(n//2,5*n//6)
    goal=(0,2*n//3)  # u=-pi and u=pi represent the same periodic phase.
    assert abs(landscape[start]+1.5)<1e-12 and abs(landscape[goal]+1.5)<1e-12
    distance=np.full((n,n),np.inf)
    distance[start]=-1.5
    queue=[(-1.5,*start)]
    neighbors=((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1))
    while queue:
        cost,i,j=heapq.heappop(queue)
        if cost>distance[i,j]+1e-13:
            continue
        if (i,j)==goal:
            return {'grid_n':n,'epsilon_over_U1':epsilon_ratio,
                    'barrier_over_U1':float(cost+1.5),
                    'sampled_global_min_over_U1':float(np.min(landscape))}
        for di,dj in neighbors:
            ii=(i+di)%n;jj=(j+dj)%n
            new=max(cost,landscape[ii,jj])
            if new<distance[ii,jj]-1e-13:
                distance[ii,jj]=new
                heapq.heappush(queue,(new,ii,jj))
    raise RuntimeError('goal not reached')


def main():
    # First factor vanishes on the entire archived line, including all 37 samples.
    t=np.linspace(0,math.pi,37)
    u=3*t;v=2*math.pi/3+t
    line_error=float(max(abs(invisible(u,v))))
    assert line_error<1e-25
    # q vectors rotate under 120 degrees as an unordered set; cosine gives inversion.
    ky=1.;kx=math.sqrt(3)
    q=np.array([[kx,-3*ky],[kx,3*ky],[-2*kx,0.]])
    angle=2*math.pi/3
    R=np.array([[math.cos(angle),-math.sin(angle)],[math.sin(angle),math.cos(angle)]])
    assert max(min(np.linalg.norm(R@vec-other) for other in q) for vec in q)<1e-12
    test=np.array([[0.12,0.7],[1.23,-.4],[-.91,.18],[.65,1.4]])
    periodic_error=0.
    symmetry_error=0.
    for p in test:
        uu,vv=kx*p[0],ky*p[1]
        val=float(invisible(uu,vv))
        for du,dv in ((2*math.pi,0),(math.pi,math.pi)):
            periodic_error=max(periodic_error,abs(val-float(invisible(uu+du,vv+dv))))
        rp=R@p
        symmetry_error=max(symmetry_error,abs(val-float(invisible(kx*rp[0],ky*rp[1]))),
                           abs(val-float(invisible(-uu,-vv))))
    assert periodic_error<1e-12 and symmetry_error<1e-12
    # At the symmetry saddle i=30, tangent curvature is negative; transverse
    # curvature of V/U1 in physical coordinates is (6+48*eps/U1)*ky^2.
    saddle_u=30*math.pi/12;saddle_v=2*math.pi/3+30*math.pi/36
    assert abs(float(base(saddle_u,saddle_v))+1)<1e-12
    assert abs(float(invisible(saddle_u,saddle_v)))<1e-25
    nvec=np.array([0.5,-math.sqrt(3)/2])
    h=1e-3
    du=kx*nvec[0]*h;dv=ky*nvec[1]*h
    h_base=float((base(saddle_u+du,saddle_v+dv)-2*base(saddle_u,saddle_v)+base(saddle_u-du,saddle_v-dv))/h**2)
    h_F=float((invisible(saddle_u+du,saddle_v+dv)-2*invisible(saddle_u,saddle_v)+invisible(saddle_u-du,saddle_v-dv))/h**2)
    assert abs(h_base-6)<1e-4 and abs(h_F-48)<1e-3
    threshold=-1/8
    runs=[minimax(n,e) for n in (120,240,480,960) for e in (0.,-.2)]
    exact=next(x for x in runs if x['grid_n']==960 and x['epsilon_over_U1']==0.)
    pert=next(x for x in runs if x['grid_n']==960 and x['epsilon_over_U1']==-.2)
    output={'classification':'EXACT symmetry and line nullspace; NUMERICAL grid minimax counterexample; NO-GO 1D profile alone identifies 2D MEP; not a material law',
            'first_shell':'f(u,v)=2 cos(v) cos(u)+cos(2v)',
            'perturbation':'F(u,v)=[1-cos(u-3v)][1-cos(u+3v)][1-cos(2u)] = [cos(u)-cos(3v)]^2[1-cos(2u)]',
            'archived_line':'u=3t, v=2pi/3+t for 0<=t<=pi; F=0 for every t',
            'max_abs_F_on_37_samples':line_error,
            'periodicity_error_sample':periodic_error,
            'D6_symmetry_error_sample':symmetry_error,
            'AB_minimum_hessian_change':'zero: F vanishes to sixth order at AB',
            'saddle_transverse_curvature_over_U1_ky2':'6+48*(epsilon/U1)',
            'finite_difference_saddle_hessian_check':[h_base,h_F],
            'saddle_transverse_stability_threshold_epsilon_over_U1':threshold,
            'eps_minus_0p2_saddle_transverse_curvature_over_U1_ky2':6+48*(-.2),
            'minimax_grids':runs,
            'grid_960_barrier_change_fraction':(pert['barrier_over_U1']/exact['barrier_over_U1'])-1,
            'grid_960_barriers_microeV_per_upper':[U1_MICROEV*exact['barrier_over_U1'],U1_MICROEV*pert['barrier_over_U1']],
            'caveats':'8-neighbor periodic minimax grid, not continuum proof or physical graphite PES; AB remains local minimum exactly, and sampled global minimum is -1.5 U1 on each grid; 1D path cannot certify transverse stability or 2D barrier without first-harmonic/source assumption.'}
    path=Path(__file__).with_name('LINE_NULLSPACE_RESULTS.json')
    path.write_text(json.dumps(output,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'line_error':line_error,'threshold':threshold,'grid_960':[exact,pert]},indent=2))

if __name__=='__main__':main()
