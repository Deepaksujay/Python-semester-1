import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
seed=8675
def deriving(y,x):
  return x**3
x=np.linspace(0,2,1001)
y=0
y1=odeint(deriving,y,x)
actual_area=(y1[1000]-y1[0])
random.seed(seed)
Max_steps=1000
x=np.random.uniform(0,2,Max_steps)
y=np.random.uniform(0,8,Max_steps)
count_inside=0
for i in np.arange(1,Max_steps,1):
  if (x[i]**3>=y[i]):
    count_inside+=1
    plt.plot(x[i],y[i],'c*')
  else:
    plt.plot(x[i],y[i],'y*')
x1=np.linspace(0,2,Max_steps)
plt.plot(x1,x1**3,'r-')
area=16*(count_inside/Max_steps)
print("area found:",area)
print("actual area:",actual_area)
print("error:",actual_area-area)
plt.show()