#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 09:50:00 2021
@author: iiitdwd
"""

import matplotlib.animation as animation 
import matplotlib.pyplot as plt 
import numpy as np 

# creating a blank window for the animation 
fig = plt.figure() 
axis = plt.axes(xlim =(-50, 50),ylim =(-50, 50)) 
#line, = axis.plot([], [], lw = 2) 
line, = axis.plot([], [], 'ro-')
# what will our line dataset contain? 
def init(): 
	line.set_data([], []) 
	return line, 
# initializing empty values for x and y co-ordinates 
xdata, ydata = [], [] 
# animation function 
def animate(i): 
	# t is a parameter which varies with the frame number 
	t = 0.1 * i 
	
	# x, y values to be plotted 
	x = t * np.sin(t) 
	y = t * np.cos(t) 
	
	# appending values to the previously empty x and y data holders 
	xdata.append(x) 
	ydata.append(y) 
	line.set_data(xdata, ydata) 
#	print (i)
	return line, 
"""
Calling the animation function	 animate(i), which takes an argument i, 
where i is called the frame number and using this we create the sine wave(or any other figure) 
which will continuously vary depending upon the value of i. 
 we use the FuncAnimation function to create an animation which will display 200 frames per second 
and in an interval of 20 micro secs.
"""
t = np.linspace(1,2*np.pi,501) 
# x, y values to be plotted 
xx = t * np.sin(t) 
yy = -t * np.cos(t)
#plt.plot(xx, yy,'*-')

anim = animation.FuncAnimation(fig, animate, init_func = init, 
							frames = 501, interval = 20, blit = True,repeat=False) 
plt.draw()
plt.show()
# saves the animation in our desktop 
#anim.save('growingCoil.mp4', writer = 'ffmpeg', fps = 30) 
