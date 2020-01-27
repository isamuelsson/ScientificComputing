#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 20:29:46 2019

@author: administrator
"""
# Isabella Samuelsson
# samuelsson_hw5_p2.py
# Lesson 9
# 2/20/19

import numpy as np
import pylab as py

tau = 0.7                          
N0 = 100.0                         
    
nts_list = np.arange(100,251,10) 
tmin = 0.0
tmax = 4.0


lastPoint_list = np.zeros_like(nts_list,dtype=float)


    
for ix, x in enumerate(nts_list):    
    t_array = np.linspace(tmin, tmax, x, endpoint=True)  
    dt = t_array[1] - t_array[0] 
    
   
    N_array = np.zeros( len(t_array) )
    N_array[0] = N0
    for it in range(0, len(t_array)-1 ):
        t  = t_array[it]         
        th = t_array[it] + dt/2  
    
        N_h           = N_array[it] + dt/2.0*(-1./tau * N_array[it])
        N_array[it+1] = N_array[it] + dt*(-1./tau *N_h)     
        
    lastPoint_list[ix] = N_array[-1]


rel_error = np.zeros_like(nts_list,dtype=float)


for ix, x in enumerate(lastPoint_list):
    rel_error[ix] = np.abs((x-(N0*np.exp(-4.0/tau))))/np.abs((N0*np.exp(-4.0/tau)))





py.figure(2)    
py.plot(np.log10(nts_list),np.log10(rel_error), '-o', label="log10 plot with nts = ")
py.xlabel("log10 of nts")
py.ylabel("log10 of the relative error at t=4.0 seconds")


RK2 = rel_error[0]
print(RK2)



t_array = np.linspace(tmin, tmax, 5000, endpoint=True)  
dt = t_array[1] - t_array[0] 
    
                                                             
N_euler = np.zeros( len(t_array) )
N_euler[0] = N0
    
for it in range(0, len(t_array)-1 ):
    N_euler[it+1] = N_euler[it] + dt * (-1./tau * N_euler[it])
    
lastPoint = N_euler[-1]


print(np.abs((lastPoint-(N0*np.exp(-4.0/tau))))/np.abs(N0*np.exp(-4.0/tau)))
    
    












