#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 18:22:19 2019

@author: administrator
"""
# Isabella Samuelsson
# samuelsson_hw6_p3.py
# 2/20/19

import numpy as np
import pylab as py
from scipy.integrate import odeint


def decay_deriv(N,t):
                                                            
     return -(1./tau) * N 


def diffeq_solver_from_scipy(N_initial, tmin, tmax, nts, deriv):
    t = np.linspace(tmin, tmax, nts)
  
    N = odeint(deriv, N_initial, t,rtol=10,atol=10)

    return t,N

  
def RK2_solver(N_initial, tmin, tmax, nts, deriv):
    N = np.zeros(nts+1)
    t = np.linspace(tmin, tmax, nts+1)
                                                                    
    dt = t[1] - t[0]
    N[0] = N_initial
    
    for it in range(0,nts):
        N_h     = N[it] + dt/2.0 * deriv(N[it], t[it])
        N[it+1] = N[it] + dt*(-1./tau * N_h)
    return t, N

  
def Euler_solver(N_initial, tmin, tmax, nts, deriv):
    N = np.zeros(nts+1)
    t = np.linspace(tmin, tmax, nts+1)
      
    dt = t[1] - t[0]
    N[0] = N_initial
    
    for it in range(0, len(t)-1 ):
        N[it+1] = N[it] + dt * deriv(N[it], t[it])
        print(N[it])  
    
    return t, N



tau = 0.7                          
N0  = 100.0                         
    
nts  = 5
tmin = 0.0
tmax = 4.0

t,N_solverSci = diffeq_solver_from_scipy(N0, tmin, tmax, nts, decay_deriv)

t2,N_Euler = Euler_solver(N0, tmin, tmax, nts, decay_deriv)

t3,N_RK2 = RK2_solver(N0, tmin, tmax, nts, decay_deriv)

py.plot(t,N_solverSci,'o-', label = "Scipy Odient")
py.plot(t,N0*np.exp(-t/tau),'-', label = "Analytic")
py.plot(t2,N_Euler, '-', label = "Euler")
py.plot(t3,N_RK2,'-', label ="RK2")

py.xlabel("time (nts=5)")
py.ylabel("Number of Nuclei")
py.legend()
py.show()
