import matplotlib.pyplot as plt 
import numpy as np 
import random
from scipy.integrate import odeint
seed=9874
np.random.seed(seed)
def derive(y,x):
    return ((x*x)-(2*x)-3)
Max_total=10000
x=np.random.uniform(0,np.pi/2,Max_total)
y=np.random.uniform(0,1,Max_total)
inside=0
for i in range(Max_total):
    if ((y[i])<=np.sin(x[i])):
        plt.plot(x[i],y[i],'g*')
        inside+=1
    else:
        plt.plot(x[i],y[i],'c*')
x1=np.linspace(-1,3,Max_total+1)
y0=0
y1=odeint(derive,y0,x1)
Odeint_area=2
Odeint_area=abs(Odeint_area)
plt.plot(x1,((x1*x1)-(2*x1)-3),'r-')
Montecarlo_area=np.pi*(inside/Max_total)
Error=Odeint_area-Montecarlo_area
Error=abs(Error)
print(f"Odeint Area:{Odeint_area}")
print("Monte Carlo Area:",Montecarlo_area)
print("Error:",Error)



