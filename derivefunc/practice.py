from numpy import*
from matplotlib import*
from pylab import*
from scipy.integrate import odeint

def deriv(y,t,k):
    dydt=-k*y
    return dydt
y0=5
t= linspace(0,20)
k=0.1
y1=odeint(deriv,y0,t,args=(k,))
k=0.2
y2=odeint(deriv,y0,t,args=(k,))
k=0.5
y3=odeint(deriv,y0,t,args=(k,))
plot(t,y1,'r-')
plot(t,y2,'y--')
plot(t,y3,'m.-')
show()




