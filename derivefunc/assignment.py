from numpy import*
from matplotlib import*
from pylab import*
from scipy.integrate import odeint

def derivation(main,time):        #main[0]=x     main[1]=v
    v=main[1]                               #main'[0]=v    main'[1]=a
    a=-0.5*v-(main[0]**2)-(main[0]**4)+0.3*sin(1.1*time)
    return array([v,a])
# g=0.3
# w=1  #1.1       for chaos=>w=1,d=0.2
# d=0.2   #0.5
# b=-1
# a=1
#y=zeros([2])
y=[0,0]
time=linspace(0,100,10000)
z=odeint(derivation,y,time)
l=z[:,0]
v=z[:,1]
plot(l,v,'r-')
show()