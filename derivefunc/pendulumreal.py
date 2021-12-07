import numpy as np
from pylab import *
import matplotlib.pyplot as plt
from scipy.integrate import odeint

N=100000#number of iterations
L=9.8
g=9.8
A=1.5
b=0.5
w=0.724
y=np.zeros([2])
#initial values
y[0]=30*np.pi/float(180)
y[1]=0.7240
t = np.linspace(0,500,N)
#plt.style.use('dark_background')
def pendulum_real(y,t,L,g,A,b,w):
    dydt0=y[1]
    dydt1=((-g/float(L))*np.sin(y[0]))-b*y[1]+(A*np.cos(w*t))
    f=np.array([dydt0,dydt1])
    return f

dynamics=odeint(pendulum_real,y,t,args=(L,g,0,0,0))
dynamics_damped=odeint(pendulum_real,y,t,args=(L,g,0,b,0))
dynamics_damped_driven=odeint(pendulum_real,y,t,args=(L,g,A,b,w))
theta=dynamics[:,0]
omega=dynamics[:,1]
theta_damped=dynamics_damped[:,0]
omega_damped=dynamics_damped[:,1]
theta_damped_driven=dynamics_damped_driven[:,0]
omega_damped_driven=dynamics_damped_driven[:,1]
plt.figure()
#plt.plot(t,theta,'-r',lw=2)
#plt.plot(t,theta_damped,'-g',lw=2)
plt.plot(t,theta_damped_driven,'-c',lw=3)
#plt.plot(theta_damped_driven,omega_damped_driven,'-c',lw=3)
#plt.plot(theta_damped_driven[N-500:N-1],omega_damped_driven[N-500:N-1],'-c',lw=3)
plt.show()