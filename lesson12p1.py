#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 13:37:45 2019

@author: administrator
"""
# Isabella Samuelsson
# samuelsson_hw8_p1.py
# 3/5/19

import numpy as np
import pylab as py

a = np.genfromtxt("freefall.data")

t      = a[:,0]
speed  = a[:,1]

sumX   = 0
sumX2  = 0
sumXY  = 0
sumY   = 0

N = len(t)

sumX += sum(t)
sumY += sum(speed)


for x in range(0,N):
    sumX2 += t[x]**2
    sumXY += t[x]*speed[x]

A = np.matrix([[sumX2,sumX],[sumX,N]])
r = np.matrix([[sumXY],[sumY]])

soln = np.linalg.solve(A,r)

a = soln[0,0]
b = soln[1,0]

print(a)




fig, ax = py.subplots(1,1)
ax.plot(t,speed, label = "Data Points")
ax.plot(t,t*a, label = "Line of Best Fit")
ax.set_xlabel("time s", fontsize=15)
ax.set_ylabel("speed m/s", fontsize=15)
ax.legend()

py.show()