from pylab import *
from time import sleep
from numpy import*
from matplotlib import*

class Main:
    def __init__(self,velocity,theta,length):
        self.velocity=velocity
        self.theta=theta
        self.length=length
        self.color='r'
    def GetX(self,time):
        return self.velocity*cos(self.theta*22/1260)*time
    def GetY(self,time):
        return (self.velocity*sin(self.theta*22/1260)*time)-0.5*9.8*(time**2)
    def getx(self,time):
        return self.GetX(time)
    def gety(self,time):
        return self.GetY(time)
    def position(self):
        x=self.getx(0.0)
        y=self.gety(0.0)
        l=2*self.velocity*sin(self.theta*22/1260)/9.8
        for time in arange(0.0,+l,0.002):
          xo=self.getx(time)
          yo=self.gety(time)
          plot([x,xo],[y,yo],self.color)
          x=xo
          y=yo
          draw()


class Ball1(Main):
    def __init__(self,velocity,theta,length):
        self.velocity=velocity
        self.theta=theta
        self.length=length
        self.color='y'
    def gety(self,time):
        return (self.velocity*sin(self.theta*22/1260)*time)-0.5*9.8*(time**2)+(self.length*sin(2*self.velocity*time/self.length))
    def getx(self,time):
        return self.velocity*cos(self.theta*22/1260)*time+(self.length*cos(2*self.velocity*time/self.length))


class Ball2(Main):
    def __init__(self,velocity,theta,length):
        self.velocity=velocity
        self.theta=theta
        self.length=length
        self.color='b'
    def getx(self,time):
        return self.velocity*cos(self.theta*22/1260)*time-(self.length*cos(2*self.velocity*time/self.length))
    def gety(self,time):
        return (self.velocity*sin(self.theta*22/1260)*time)-0.5*9.8*(time**2)-(self.length*sin(2*self.velocity*time/self.length))


a=float(input("Enter velocity here: "))
b=float(input("Enter theta here: "))
c=float(input("Enter length of  the rod here: "))

baton= Main(a,b,c/2)
baton.position()
bato= Ball1(a,b,c/2) 
bato.position()
bat= Ball2(a,b,c/2)
bat.position()
show()


     