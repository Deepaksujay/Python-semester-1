import matplotlib.animation as animation 
from matplotlib import *
from numpy import*
from pylab import*

length=2.5
velocity=5
g=9.8
theta=pi/4
Total=1000
Max_time=(2*(velocity/g)*np.sin(theta))
time=np.linspace(0,Max_time,Total)
X_maximum=(((velocity**2)*(sin(2*theta))/g)+length)
Y_maximum=(((velocity**2)*(sin(theta)**2)/(2*g))+length)
fig = figure() 
axis = axes(xlim =(-length, X_maximum),ylim =(-length, Y_maximum)) 
#line, = axis.plot([], [], lw = 2) 
line, = axis.plot([], [], 'ro-')
# what will our line dataset contain? 
def init(): 
	line.set_data([], []) 
	return line, 
# initializing empty values for x and y co-ordinates 
xdata, ydata = [], []

x1=velocity*cos(theta)*time-(length*cos(2*velocity*time/length))
y1=(velocity*sin(theta)*time)-0.5*g*(time**2)-(length*sin(2*velocity*time/length))
x2=velocity*cos(theta)*time+(length*cos(2*velocity*time/length))
y2=(velocity*sin(theta)*time)-0.5*g*(time**2)+(length*sin(2*velocity*time/length))
xm=velocity*cos(theta)*time
ym=(velocity*sin(theta)*time)-(0.5*g*(time**2))
plot(xm,ym,'y-')
plot(x1,y1,'m-')
plot(x2,y2,'c-')
def animate(i):
    x1data=([x1[i],x2[i]])
    y1data=([y1[i],y2[i]])
    # plot((x1[i],x2[i]),(y1[i],y2[i]),'ro-')
    line.set_data(x1data,y1data)
    # xdata.append(x1data)
    # ydata.append(y1data)
    # line.set_data(xdata,ydata)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func = init, 
							frames = Total, interval =5, blit = False,repeat=True)
print(x)
plt.show()
    

 



