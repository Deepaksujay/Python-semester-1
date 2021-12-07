import random
import numpy as np
from matplotlib import*
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
from pylab import*
from scipy.integrate import odeint

def derive(z,x,y):
  return ((1)-(x**2)-(y**2))**0.5

#fig = plt.figure()
ax = plt.axes(projection='3d')
Total=10000
seed=6317
np.random.seed(seed)
radius=1
inside=0
x1=0;y1=0;z1=0;xmax=1;ymax=1;zmax=1
x=np.random.uniform(x1,xmax,Total)
y=np.random.uniform(y1,ymax,Total)
z=np.random.uniform(z1,zmax,Total)
for j in np.arange(0,Total,1):
  #ax.plot3D(x[j],y[j],z[j],'gray')
  r=np.sqrt((x[j]*x[j]*x[j])+(y[j]**2)+(z[j]**2))
  if (r<=radius):
    inside=inside+1
    ax.plot3D(x[j],y[j],z[j],'red')
actual_volume=(4/3)*pi*(radius**3)
volume=8*(inside/10000)
x0=linspace(0,xmax,Total+1)
y0=linspace(0,ymax,Total+1)
z00=0
z0=odeint(derive,z00,x0,y0)
Odient_area=(z0[Total]-z[0])*8
print("Odeint area:",Odient_area)
correction=actual_volume-(volume)
print("volume:",volume)
print("actual volume:",actual_volume)
print("correction:",correction)
#plt.show()