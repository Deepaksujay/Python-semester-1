from pylab import *
from time import sleep
from numpy import*
from matplotlib import*
#from scipy.integrand import*

class  Rotation:
    def __init__(self,velocity,radius):    #radius= radius of the sphere 
        self.velocity= velocity            #velocity= velocity it is travelling with
        self.radius= radius
    def GetX1(self,time):
        return self.radius+self.velocity*time+self.radius*sin(self.velocity*180*time/(self.radius*pi))
    def GetY1(self,time):
        return self.radius+self.radius*cos(self.velocity*180*time/(self.radius*pi))
    def plotting(self):
        x=self.GetX1(0.0)
        y=self.GetY1(0.0)
        for time in (0.0,+2.0,0.005):
            xo=self.GetX1(time)
            yo=self.GetY1(time)
            plot([xo,x],[yo,y],'g')
            x=xo
            y=yo
            draw()

hall= Rotation(10,2)
hall.plotting()
show()            


      
        