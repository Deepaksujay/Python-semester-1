#Beats: plots sin(30x)+sin(33x), #0<=x<=5.0
#from  vpython import* # Graphic and Math classes
#from pylab import*
from numpy import*
from matplotlib.pyplot import*
# Plotsetup( initx, width, height,title,axes ames,font,color)
#graph = gdisplay(x=0,y=0,width=500,height=300,title='Beats:f(x)=sin(30*x)+sin(33*x)',xtitle= 'x',ytitle='f(x)',xmax=5.0,xmin=0.0,ymax =2,ymin=-2,foregroung=color.black,bachground.color=color.white) #setup plot
#function=gcurve(color=color.red)
#for x in arange(0.0,5.0,0.01): # min,max,step
#rate(40)
#    print x
x=arange(0.0,5.0,0.01)
y=sin(30*x)+sin(33*x) # function to plot
#function.plot(x,y) # plot function
plot(x,y)
show()
