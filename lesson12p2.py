#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 14:33:30 2019

@author: administrator
"""
# Isabella Samuelsson
# samuelsson_hw8_p2.py
# 3/5/19

import numpy as np
import pylab as py
from scipy.optimize import curve_fit

a = np.genfromtxt("damped_oscillation.txt")

t     = a[:,0]
angle = a[:,1]

def func(t,a,omega,phi,tau,B):
    return a*np.cos(omega*t+phi)*np.exp(-t/tau)+B

par, con = curve_fit(func, t, angle)

a = par[0]
omega = par[1]
phi = par[2]
tau = par[3]
B = par[4]


R2 = np.sqrt(sum((func(t,a,omega,phi,tau,B)-angle)**2))



fig, ax = py.subplots(1,1)
ax.plot(t,angle,label = "Data Points")
ax.plot(t,func(t,a,omega,phi,tau,B),label = "Best Fit Curve")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Angle (radians)")
py.figtext(0.3,0.85, "a           ={}".format(round(a, 2)))
py.figtext(0.3,0.82, "omega  ={}".format(round(omega, 2)))
py.figtext(0.3,0.79, "phi        ={}".format(round(phi, 2)))
py.figtext(0.3,0.76, "tau        ={}".format(round(tau, 2)))
py.figtext(0.3,0.73, "B           ={}".format(round(B, 2)))
py.figtext(0.3,0.70, "R2         ={}".format(round(R2, 2)))
ax.legend()

