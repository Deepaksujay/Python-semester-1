import matplotlib.animation as animation 
from matplotlib import *
from numpy import*
from pylab import*
from scipy.integrate import odeint 

def derive2pen(main,t,m1,m2,l1,l2,g):
    f0=main[1]
    f2=main[3]
    f1=((m2*g*cos(main[0]-main[2])*sin(main[2]))-(m2*l2*(main[3]**2)*sin(main[0]-main[2]))-(g*sin(main[0])*(m1+m2))-(m2*l1*(main[1]**2)*cos(main[0]-main[2])*sin(main[0]-main[2])))/(((m1+m2)*l1)-(l1*m2*cos(main[0]-main[2])*cos(main[0]-main[2])))
                                                                     # (((m1+m2)*l1)-(l1*m2*cos(main[0]-main[2])*cos(main[0]-main[2])))
    f3=((2*(m1+m2)*l1*(main[1]**2)*sin(main[0]-main[2]))-(2*(m1+m2)*g*sin(main[2]))+(2*(m1+m2)*g*sin(main[0])*cos(main[0]-main[2]))+(l2*m2*(main[3]**2)*sin(2*(main[0]-main[2]))))/((2*l2*(m1+m2))-(2*l2*m2*((cos(main[0]-main[2])**2))))
                                                                  #  ((2*l2*(m1+m2))-(2*l2*m2*((cos(main[0]-main[2])**2))))
    return array([f0,f1,f2,f3])
def rk4(y,t,dt,derive2pen):# defining the 2nd order Runge Kutta method function that could find the new state with inputs 
    k1=dt*derive2pen(y,t,m1,m2,l1,l2,g)#Using the slope at initial point
    k2=dt*derive2pen(y+(k1/2),t+(dt/2),m1,m2,l1,l2,g)#Using the slope b/w initial and new point
    k3=dt*derive2pen(y+(k2/2),t+(dt/2),m1,m2,l1,l2,g)#Using the slope b/w initial and new point
    k4=dt*derive2pen(y+k3,t+dt,m1,m2,l1,l2,g)#Using the slope at new point
    y_next=y + (k1+2*k2+2*k3+k4)/6 # #Using the average of above four slopes to find new point
    return y_next # new state is retuned to rk4 function

fig = figure() 
axis = axes(xlim =(0,20),ylim =(0,19)) 
#line, = axis.plot([], [], lw = 2) 
line, = axis.plot([],[],'ro-')
line2, = axis.plot([],[],'yo-')
# what will our line dataset contain? 
def init(): 
	line.set_data([],[]) 
	line2.set_data([],[])
	return line,line2,  
# initializing empty values for x and y co-ordinates 
xdata, ydata, x2data, y2data = [], [], [], [] 
# animation function 
def animate(i): 
    # x, y values to be plotted 
	x1=10+(l1*sin(ymain[i,0]))
	y1=10-(l1*cos(ymain[i,0]))
	x2=10+(l1*sin(ymain[i,0]))+(l2*sin(ymain[i,2]))
	y2=10-(l1*cos(ymain[i,0]))-(l2*cos(ymain[i,2]))
	x2data=([x1,x2]) 
	y2data=([y1,y2])
	xdata=([10,x1]) 
	ydata=([10,y1])
	line.set_data(xdata,ydata)
	line2.set_data(x2data,y2data) 
	# plot([10,x1],[10,y1],'go-')
	# plot([x1,x2],[y1,y2],'co-') 
	return line,line2,
m1=10
m2=7
l1=5
l2=4
g=9.8
theta10=pi/3
theta20=pi/3
main=[theta10,0,theta20,0]
no_of_frames=10000

time=linspace(0,500,no_of_frames)
#print(time)
ymain=odeint(derive2pen,main,time,args=(m1,m2,l1,l2,g,))
theta1=ymain[:,0]
theta2=ymain[:,2]
xx1=10+(l1*sin(theta1))
yy1=10-(l1*cos(theta1))
xx2=10+(l1*sin(theta1))+(l2*sin(theta2))
yy2=10-(l1*cos(theta1))-(l2*cos(theta2))
#plot(xx1, yy1,'b*')
#plot(xx2, yy2,'r*')

anim = animation.FuncAnimation(fig, animate, init_func = init, 
							frames = no_of_frames, interval =30, blit = False,repeat=False) 							
draw()
show()
# saves the animation in our desktop 
#anim.save('growingCoil.mp4', writer = 'ffmpeg', fps = 30) 
