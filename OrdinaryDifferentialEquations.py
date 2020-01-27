#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 13:43:57 2019

@author: administrator
"""
# Isabella Samuelsson
# samuelsson_hw5_p1.py
# lesson 8
# 2/19/19

import numpy as np
import pylab as py
 
def euler(Iy,Iv,a,numSlots,b):
    
    t_list = np.linspace(0.0,8.0,numSlots)
    dt=t_list[1]-t_list[0]
    y_list = np.zeros_like(t_list)
    v_list = np.zeros_like(t_list)
    y_list[0] = Iy
    v_list[0] = Iv
   
    
    
    for x in range(1,len(t_list)):
        
        v_list[x] = v_list[x-1] + (a-b*v_list[x-1])*(dt)
        y_list[x] = y_list[x-1] + v_list[x-1]*(dt)
        
    return (y_list,t_list,v_list)

        
yI = 12.0
vI = 35.0
g = -9.8  
nts_list = [8,16,32,64,128,256,512,1024,2048,4096,8192]



for ix, x in enumerate(nts_list):
    py.figure(1)
    py.plot(euler(yI,vI,g,x,0)[1],euler(yI,vI,g,x,0)[0],"-",label = "nts = {}".format(x))
    py.xlabel("Time")
    py.ylabel("Height")
    py.legend(fontsize = "x-small")
    py.grid(True)
    py.show()
    

    
    height_list = euler(yI,vI,g,x,0)[0]
    error = np.abs((height_list[-1]+21.6))/np.abs(-21.6)
    
    py.figure(2)
    py.plot(x,error,"-o")
    py.xlabel("dt")
    py.ylabel("Error")
    py.grid(True)
    py.show()
    

b_list = np.arange(0,1,0.1)
 
for ix, x in enumerate(b_list): 
    py.figure(3)
    py.plot(euler(yI,vI,g,8192,x)[1],euler(yI,vI,g,8192,x)[0], label = "b = .{}".format(x))
    py.xlabel("Time in Seconds")
    py.ylabel("Height with Drag")
    py.legend(fontsize = 'x-small')

    py.figure(4)
    py.plot(euler(yI,vI,g,8192,x)[1],euler(yI,vI,g,8192,x)[2], label = "b = .{}".format(x))
    py.xlabel("Time in Seconds")
    py.ylabel("Velocity with Drag")
    py.legend(fontsize = 'x-small')
    
    
