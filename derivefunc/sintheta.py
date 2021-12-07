from scipy.integrate import odeint
from numpy import*
from pylab import*

def der(y,t):
    f=2*t
    return f

y1=0
t=linspace(0,100,100)
z=t**2
m=odeint(der,y1,t,)
plot(t,m,'r.-')
plot(t,z,'y-')
show()
