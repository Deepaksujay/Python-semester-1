from pylab import*
from numpy import*
from scipy.integrate import*

def euler(y,t,dt,derdecay):# defining the euler function that could find the new state with inputs 
    y_next=y + derdecay(y,t,L)*dt # Euler's rule for inputs y, derivs, dt by call to derivs function
    return y_next # new state is retuned to euler function
def derdecay(N,t,L):
    dNdt=-L*N
    return dNdt
N1=1000
L=0.23
t=linspace(0,20,101)
y= odeint(derdecay,N1,t,args=(L,))
y2=zeros([101,2])
y2[0][0]=1000
for j in range(99):
    y2[j+1,:]=euler(y2[j,:],t[j],0.2,derdecay)
plot(t,y2,'b-')
plot(t,y,'r-')
y1=N1*exp(-L*t)
plot(t,y1,'m.-')
show()

