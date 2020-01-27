#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 16:00:55 2019

@author: administrator
"""
# Isabella Samuelsson
# samuelsson_hw6_p2.py
# 2/20/19

import numpy as np
import pylab as p

                                                        
def decay_deriv(N,t):                                                          
     return -(1./tau) * N                                                      
    
    
    
def RK2_solver(N_initial, tmin, tmax, nts, deriv):
    N = np.zeros(nts+1)
    t = np.linspace(tmin, tmax, nts+1)
    
                                                                    
    dt = t[1] - t[0]
    N[0] = N_initial
    
    for it in range(0,nts):
        N_h     = N[it] + dt/2.0 * deriv(N[it], t[it])
        N[it+1] = N[it] + dt*(-1./tau * N_h)
    return t, N





tau = 0.7        # mean lifetime
N0 = 100.0       # initial number of nuclei
tmin = 0.0       # start time
tmax = 4.0       # end time
nts=20           # number of points

t,N_euler = RK2_solver(N0, tmin, tmax, nts, decay_deriv)


print ("Shapes:",np.shape(t), np.shape(N_euler))

p.plot(t,N_euler,'o-')

p.show()
