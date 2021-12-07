import matplotlib.animation as animation 
from matplotlib import *
from numpy import*
from pylab import*
from scipy.integrate import odeint 

m1=10
m2=7
l1=5
l2=4
g=9.8
theta10=pi/3
theta20=pi/3
main=[theta10,0,theta20,0]
n=200  #n=total time
t=linspace(0,n,n+1)

def derive2pen(main,t,m1,m2,l1,l2,g):
    f0=main[1]
    f2=main[3]
    f1=((m2*g*cos(main[0]-main[2])*sin(main[2]))-(m2*l2*(main[3]**2)*sin(main[0]-main[2]))-(g*sin(main[0])*(m1+m2))-(m2*l1*(main[1]**2)*cos(main[0]-main[2])*sin(main[0]-main[2])))/(((m1+m2)*l1)-(l1*m2*cos(main[0]-main[2])*cos(main[0]-main[2])))
                                                                     # (((m1+m2)*l1)-(l1*m2*cos(main[0]-main[2])*cos(main[0]-main[2])))
    f3=((2*(m1+m2)*l1*(main[1]**2)*sin(main[0]-main[2]))-(2*(m1+m2)*g*sin(main[2]))+(2*(m1+m2)*g*sin(main[0])*cos(main[0]-main[2]))+(l2*m2*(main[3]**2)*sin(2*(main[0]-main[2]))))/((2*l2*(m1+m2))-(2*l2*m2*((cos(main[0]-main[2])**2))))
                                                                  #  ((2*l2*(m1+m2))-(2*l2*m2*((cos(main[0]-main[2])**2))))
    return array([f0,f1,f2,f3])

differ=odeint(derive2pen,main,t,args=(m1,m2,l1,l2,g,))

"""x1=10+(l1*sin(differ[:,0]))
y1=10-(l1*cos(differ[:,0]))
x2=10+(l1*sin(differ[:,0]))+(l2*sin(differ[:,2]))
y2=10-(l1*cos(differ[:,0]))-(l2*cos(differ[:,2]))
plot([x1,x2],[y1,y2],'ro-')
plot(10,10,'ro')"""

for i in range (n+1):
    x1=10+(l1*sin(differ[i,0]))
    y1=10-(l1*cos(differ[i,0]))
    x2=10+(l1*sin(differ[i,0]))+(l2*sin(differ[i,2]))
    y2=10-(l1*cos(differ[i,0]))-(l2*cos(differ[i,2]))
    plot([10,x1],[10,y1],'co-')
    plot([x1,x2],[y1,y2],'ro-')

show()