#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 06:43:14 2021

@author: iiitdwd
"""

import numpy
from pylab import *
from tools import derivspring
from tools import euler
N=5000 # Number of iterations
y=numpy.zeros([N,2])# initialization of memory to save results
#deriv=zeros([N,2])
y[0,0]=0 # initial position of the object
y[0,1]=0 # initial velocity of the object
tau=20 # total iterative/computation time
dt=tau/float(N-1)# time step for each iteration
#state=y[0,:]
#k=3.5
#m=0.2
time=numpy.linspace(0,tau,N)# creation of time grid for plotting

figure()#starting plot figure
for j in range(N-1):#starting a for loop of iterations
#    d=derivspring(y[j,:],time[j])
#    print (d)
    y[j+1,:]=euler(y[j,:],time[j],dt,derivspring) # calling euler function for initial state y[j,:], note colon is ignored

xdata=[y[j,0] for j in range(N)] # collecting xdata from y vector with addressing to first column
vdata=[y[j,1] for j in range(N)] # collecting vdata from y vector with addressing to second column
plot(time,xdata,'-r') # plotting position with red line
plot(time,vdata,'-b')# plotting position with blue line
legend(['position','velocity'])
#xlim(0,0.02)
show()
#draw()
#print (xdata)