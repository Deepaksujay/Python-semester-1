#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 07:16:11 2021

@author: iiitdwd
"""

""" From "A SURVEY OF COMPUTATIONAL PHYSICS", Python eBook Version
   by RH Landau, MJ Paez, and CC Bordeianu
   Copyright Princeton University Press, Princeton, 2012; Book  Copyright R Landau,
   Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2012.
   Support by National Science Foundation , Oregon State Univ, Microsoft Corp"""

# Dumbbell.py: Combines classes to form a Baton with Mass and Radius

#from visual import *
#from visual.graph import *                    # graphics and math classes
from matplotlib import*
from pylab import *
class Ball:
    def __init__(self, mass, radius):                  # Ball constructor
        self.m = mass                                   # initialize mass
        self.r = radius                               # initialize radius

    def getM1(self):                                      # get Ball mass
        return self.m

    def getR(self):                                     # get Ball radius
        return self.r

    def getI1(self):
        return (2.0/5.0)*self.m*(self.r)**2

class Path:                                       # parabolic path of COM
    def __init__(self, v0, theta):                     # Path constructor
        self.g = 9.8                                            # gravity
        self.v0 = v0                                      # initial speed
        self.theta = theta                                # initial angle
        self.v0x = self.v0*cos(self.theta*pi/180.0)          # initial Vx
        self.v0y = self.v0*sin(self.theta*pi/180.0)          # initial Vy

    def getX(self, t):                                         # get Xcom
        self.t = t
        return self.v0x*self.t

    def getY(self, t):                                         # get Ycom
        self.t = t
        return self.v0y*self.t  -  0.5*self.g*t**2

class Baton(Ball, Path):         # Baton inherints Ball & Path properties
    def __init__(self, mass, radius, v0, theta, L1, w1):
        Ball.__init__(self, mass, radius)                # contructs Ball
        Path.__init__(self, v0, theta)             # constructs classPath
        self.L = L1                                    # Lenght of  Baton
        self.w = w1                                  # ang velocity Baton

    def getM(self):
        return 2.0*self.getM1()

    def getI(self):
        return (2*self.getI1() + 0.5*self.getM()*self.L**2)

    def getXa(self, t):
        xa = self.getX(t) +  0.5*self.L*cos(self.w*t)
        return xa

    def getYa(self, t):
        return self.getY(t) +  0.5*self.L*sin(self.w*t)

    def getXb(self, t):
        return self.getX(t) -  0.5*self.L*cos(self.w*t)

    def getYb(self, t):
        return self.getY(t) -  0.5*self.L*sin(self.w*t)

#    def scenario(self, mytitle, myxtitle, myytitle, xma, xmi, yma, ymi):
#        graph = gdisplay(x = 0, y = 0, width = 500, height = 500,  
#               title=mytitle, xtitle=myxtitle, ytitle=myytitle, xmax=xma,
#               xmin=xmi, ymax=yma, ymin=ymi, foreground=color.black,
#               background=color.white)

    def position(self):
#        batonmassa = gcurve(color = color.blue)       # blue a trajectory
#        batonmassb = gcurve(color = color.red)         # red b trajectory
#        batoncm = gcurve(color = color.magenta)
        t = 0.0                                     # start motion at t=0
        count = 4
        yy = self.getYa(t)                                   # initial Ya
        while (self.getYa(t)>= 0.0):                      # do till Yb <0
            xa = self.getXa(t)                                       # Xa
            ya = self.getYa(t)                                       # Yb
#            batonmassa.plot(pos = (xa, ya) )                     # plot a
            plot(xa, ya)
            xb = self.getXb(t)
            yb = self.getYb(t)
#            batonmassb.plot(pos = (xb, yb) )                     # plot b
            plot(xb, yb)
            # if count%4 == 0:
                                 #  uncommented 2 two lines to plot baton
                # gcurve(pos = [(xa, ya), (xb, yb)], color = color.cyan)
            xcm = self.getX(t)                                     # Xcom
            ycm = self.getY(t)                                     # Ycom
#            batoncm.plot(pos = (xcm, ycm) )                    # plot COM
            plot(xcm, ycm)
            rate(10,0,0,0)
            t  += 0.02                          # increments time in 0.02
            count   += 1
        show()

mybaton = Baton(0.5, 0.4, 15.0, 34.0, 2.5, 15.0)  # m radius v0 theta L w
#mybaton.scenario('Positions of mass a(blue), b(red) and COM (magenta)',
#                 'x', 'y', 20, 0, 5,  - 1)           # xmx = 20, xmin = 0
mybaton.position()                                 #ymax = 10, ymin =  - 1
