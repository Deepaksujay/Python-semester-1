""" From "A SURVEY OF COMPUTATIONAL PHYSICS", Python eBook Version
   by RH Landau, MJ Paez, and CC Bordeianu
   Copyright Princeton University Press, Princeton, 2012; Book  Copyright R Landau, 
   Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2012.
   Support by National Science Foundation , Oregon State Univ, Microsoft Corp"""

#    Moon.py: moon orbiting a planet via OOP
from pylab import *
#from time import sleep
#import numpy

Radius = 4.0                                        # Planet Orbit radius
wplanet = 2.0                                   # planet angular velocity
radius = 1.0                            # moon Orbit radius around planet
wmoon = 14.0                               # moon ang. vel. around planet

time=arange(0.,3.2,0.02)                  # time min, max, step
xo = Radius*cos(wplanet*time) #planet x
yo = Radius*sin(wplanet*time) #planet y
#ion()

#for time in arange(0., 3.2, 0.02):                  # time min, max, step
x = Radius*cos(wplanet*time) + radius*cos(wmoon*time)        # moon x
y = Radius*sin(wplanet*time) + radius*sin(wmoon*time)        # moon y
#  hh, = plot([xo,x], [yo,y],'b')                     # plots moon position
#  sleep(0.001)
#  xo = x
#  yo = y
#  hh.set_xdata(numpy.append(hh.get_xdata(),[xo,x]))
#  hh.set_ydata(numpy.append(hh.get_ydata(),[yo,y]))
#  draw()
plot(x,y,xo,yo)
show()
