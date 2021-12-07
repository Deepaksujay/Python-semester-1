#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 06:35:36 2021

@author: iiitdwd
"""

#import numpy
from numpy import *
def derivs(state,time): # defining a derivs function with input as state and time, where state =[x,v] 
    go=state[1]# derivative of x is v, so second entry of state with index 1 is labelled as go
    g1=-9.8 #derivative of v is acceleration which is g=-9.8, so it is labelled as g1
    g=array([go,g1])#derivatives of state=[x,v] is put in the array form, labelled as g
    return g # derivative of state is returned as derivs function

def euler(y,t,dt,derivs):# defining the euler function that could find the new state with inputs 
    y_next=y + derivs(y,t,)*dt # Euler's rule for inputs y, derivs, dt by call to derivs function
    return y_next # new state is retuned to euler function

def derivspring(state,time): # defining a derivs function with input as state and time, where state =[x,v] 
    k=-3.5
    m=0.2
    g=9.8
    go=state[1]# derivative of x is v, so second entry of state with index 1 is labelled as go
    g1=state[0]*(k/m)-g #derivative of v is acceleration which is k/m x-g, so it is labelled as g1
    g=array([go,g1])#derivatives of state=[x,v] is put in the array form, labelled as g
    return g # derivative of state is returned as derivs function
def rk2(y,t,dt,derivs):# defining the 2nd order Runge Kutta method function that could find the new state with inputs 
    k0=dt*derivs(y,t)#Using the slope at initial point
    k1=dt*derivs(y+k0,t+dt)#Using the slope at new point
    y_next=y + 0.5*(k0+k1) # #Using the average of above two slopes to find new point
    return y_next # new state is retuned to rk2 function

def rk4(y,t,dt,derivs):# defining the 2nd order Runge Kutta method function that could find the new state with inputs 
    k1=dt*derivs(y,t)#Using the slope at initial point
    k2=dt*derivs(y+(k1/2),t+(dt/2))#Using the slope b/w initial and new point
    k3=dt*derivs(y+(k2/2),t+(dt/2))#Using the slope b/w initial and new point
    k4=dt*derivs(y+k3,t+dt)#Using the slope at new point
    y_next=y + (k1+2*k2+2*k3+k4)/6 # #Using the average of above four slopes to find new point
    return y_next # new state is retuned to rk4 function

def derivsfric(y,t,k,m,c): # defining a derivs function with input as state and time, where state =[x,v] 
#    k=3.5
#    m=0.2
#    c=2
    go=y[1]# derivative of x is v, so second entry of state with index 1 is labelled as go
    g1=y[0]*(-k/m)-c*y[1] #derivative of v is acceleration which is k/m x-g, so it is labelled as g1
    g=array([go,g1])#derivatives of state=[x,v] is put in the array form, labelled as g
    return g # derivative of state is returned as derivs function
def derivs_fric(state,time): # defining a derivs function with input as state and time, where state =[x,v] 
    k=3.5
    m=0.2
    c=2
    go=state[1]# derivative of x is v, so second entry of state with index 1 is labelled as go
    g1=state[0]*(-k/m)-c*state[1] #derivative of v is acceleration which is k/m x-g, so it is labelled as g1
    g=array([go,g1])#derivatives of state=[x,v] is put in the array form, labelled as g
    return g # derivative of state is returned as derivs function
def derive(y,t):
    f=exp(t)
    return f
def derivp(y,t):
    f=2*(t)
    return f
def derivf(y,t):
    f=t*2
    return f
def derivcos(y,t):
    f=cos(t)
    return f
def derivcost(y,t):
    f=3*t**2+4*t+1
    return f
def derivsine(y,t):
    f=exp(t)*sin(t)+exp(t)*cos(t)
    return f
def deriv2(y,t):
    y0=y[1]
    y1=2*(((y[0])**2)-t)
    dydt=array([y0,y1])
    return dydt
