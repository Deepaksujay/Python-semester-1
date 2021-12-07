""" From "A SURVEY OF COMPUTATIONAL PHYSICS", Python eBook Version
   by RH Landau, MJ Paez, and CC Bordeianu
   Copyright Princeton University Press, Princeton, 2012; Book  Copyright R Landau, 
   Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2012.
   Support by National Science Foundation , Oregon State Univ, Microsoft Corp"""

# OOPPlanet.py: Planet orbiting Sun, or moon orbiting planet

from pylab import *
from time import sleep
import numpy
import matplotlib.pyplot as plt

#ion()

class OOPPlanet:
    def __init__(self, Rad, pomg):             # Planet class constructor
        self.Radius = Rad                                 # Planet Radius
        self.wplanet = pomg                     # Planet angular velocity
        self.color = 'r'
        self.dt = 0.04
        
    def getXp(self, time):
       return self.Radius*cos(self.wplanet*time)
    
    def getYp(self, time):
       return self.Radius*sin(self.wplanet*time)

    def getX(self, time):
       return self.getXp(time)
    
    def getY(self, time):
       return self.getYp(time)
    
    def position(self):                                 # for plane orbit
        xo = self.getX(0.)
        yo = self.getY(0.)
        for time in arange(0.,  + 3.3, self.dt):            # min, max, step
            xp = self.getX(time)
            yp = self.getY(time)
            hh, = plot([xo,xp], [yo,yp],self.color)                     # plots moon position
#            sleep(0.001)
            xo = xp
            yo = yp
            hh.set_xdata(numpy.append(hh.get_xdata(),[xo,xp]))
            hh.set_ydata(numpy.append(hh.get_ydata(),[yo,yp]))
            draw()
           

class OOPMoon(OOPPlanet):             # OOPMoon is  subclass of OOPPlanet
    
    def __init__(self, Rad, pomg, rad, momg):   # constructor planet&Moon
                                         
        OOPPlanet.__init__(self, Rad, pomg)
        self.radius = rad                                   # Moon radius
        self.wmoon = momg                         # Moon angular velocity
        self.color = 'b'
        self.dt = 0.02
        
    def getXm(self, time):
        xp = self.getXp(time)
        return (xp +  self.radius*cos(self.wmoon*time))

    def getYm(self, time):
        yp = self.getYp(time)
        return (yp +  self.radius*sin(self.wmoon*time))

    def getX(self, time):
       return self.getXm(time)
    
    def getY(self, time):
       return self.getYm(time)

planet = OOPPlanet(4.0, 2.0)                         # initializes planet
planet.position()

moon = OOPMoon(4.0, 2.0, 1.0, 14.0)                  # init planet & moon
moon.position()                              # overrrides moon position

plt.plot()

                

