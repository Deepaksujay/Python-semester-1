from numpy import*
from matplotlib import*
from pylab import*
from scipy.integrate import odeint

N=1000#number of iterations
L=9.8
g=9.8
y=zeros([2])
#initial values
y[0]=30*pi/float(180)
y[1]=0.0

t = linspace(0,45,N)
#plt.style.use('dark_background')
def pendulum(y,t,L,g):
    dydt0=y[1]
    dydt1=(-g/float(L))*sin(y[0])
    f=array([dydt0,dydt1])
    return f
def pendulum_approx(y,t,L,g):
    dydt0=y[1]
    dydt1=(-g/float(L))*(y[0])
    f=array([dydt0,dydt1])
    return f
dynamics=odeint(pendulum,y,t,args=(L,g))
dynamics_approx=odeint(pendulum_approx,y,t,args=(L,g))

theta=dynamics[:,0]
omega=dynamics[:,1]
theta_approx=dynamics_approx[:,0]
omega_approx=dynamics_approx[:,1]
plot(t,theta,'-r',lw=2)
plot(t,theta_approx,'-g',lw=2)
show()