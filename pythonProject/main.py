from pylab import *
from time import sleep
from numpy import*
from matplotlib import*

"""m= int(input("enter Maths marks here: "))
p= int(input("enter Physics marks here: "))
c= int(input("enter Chemistry marks here: "))
average=float
average=(m+p+c)/3
print(f"average marks of student={average}")"""

"""number= int(input("please enter your number here: "))
base=2
while number>base:
    if number%base==0:
        print(f"{number} is not a prime number")
        break
    else:
        base+=1
else:
    print(f"{number} is a prime number")"""




"""h=int(input("Enter heads here: "))
l=int(input("Enter legs here: "))
x=int((l/2)-h)
y=int(h-x)
print(f"No of cows: {x}")
print(f"No of hens: {y}")"""



# Python program to print all
# prime number in an interval
# number should be greater than 1
"""start = 1
end = 25

for i in range(start, end):
    if i > 1:
        for j in range(2, i):
            if (i % j == 0):
                break
        else:
            print(i)"""


"""import math
x= float(input("here "))
def y(x):
  x=math.sin(22*x/7)+2*x;
  return x
print (y(x))"""


# from time import sleep
# from numpy import*
# from matplotlib import*
# R=4.0
# r=1.0
# wp=2.0
# wm=14.0
# t=(0.,3.2,0.02)
# xo=R*cos(wp*t)
# yo=R*sin(wp*t)
# x=R*cos(wp*t)+r*cos(wm*t)
# y=R*sin(wp*t)+r*sin(wm*t)
# plot(x,y,xo,yo)
# show()


class Projection:
    def __init__(self,theta,velocity):
        self.theta = theta
        self.velocity = velocity
        self.color= 'r'
    def GetX(self,time):
        return (self.velocity*cos(self.theta*22/1260)*time)
    def GetY(self,time):
        return((self.velocity*sin(self.theta*22/1260)*time)-0.5*9.8*(time**2))
    # def getx(self,time):
    #     return self.GetX(time)
    # def gety(self,time):
    #     return self.GetY(time)
    def position(self):
        x = self.GetX(0.0)
        y = self.GetY(0.0)
        l=2*self.velocity*sin(self.theta*22/1260)/9.8
        for time in arange (0.,l,0.04):
            xo =self.GetX(time)
            yo =self.GetY(time)
            hh,= plot ([x,xo],[y,yo],self.color)
            # hh.set_xdata(numpy.append(hh.get_xdata(),[x,xo]))
            # hh.set_ydata(numpy.append(hh.get_ydata(),[y,yo]))
            x= xo
            y= yo
            draw()

class project (Projection):
    def __init__(self,theta,velocity):
        self.theta = theta
        self.velocity = velocity
        self.color= 'y'
    def GetX(self,time):
        return (self.velocity*cos(self.theta*22/1260)*time)
    def GetY(self,time):
        return((self.velocity*sin(self.theta*22/1260)*time)-0.5*9.8*(time**2))
    
        
# m= float(input("Enter angle here: "))
# n= float(input("Enter Projection velocity here: "))
        
ball = Projection(76,10)
ball.position()

hall = project(28,10)
hall.position()

show()









































