# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 13:32:30 2023

@author: wilks
"""

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-whitegrid')#replace with 'seaborn-whitegrid' if error occurs

dilate = lambda a, b: np.array([[a, 0], [0, b]])

rotate = lambda theta: np.array([[np.cos(theta), -np.sin(theta)],[np.sin(theta), np.cos(theta)]])

reflect = lambda theta: np.array([[np.cos(2*theta), np.sin(2*theta)],[np.sin(2*theta), -np.cos(2*theta)]])

project = lambda theta: 1/2*np.array([[1+np.cos(2*theta), np.sin(2*theta)],[np.sin(2*theta), 1-np.cos(2*theta)]])

#create a scatter plot for "J"
points = np.concatenate([[[1+(0.1+0.01*i),1] for i in range(81)], 
                       [[1+0.5, 1-0.01*j] for j in range(76)],
                       [[1+0.25+0.25*np.cos(np.pi*(1+0.01*k)), 0.25+0.25*np.sin(np.pi*(1+0.01*k))] for k in range(101)]]) #np.concatenate([[[i*0.01,j*0.01] for i in range(101)] for j in range(101)])

plt.figure(figsize=(8, 8), dpi=80)
plt.ion()
plt.axis([-9,3,-7,7])

#Transform the set of points   
# print(dilate(10,10))
# print("\nrotate", rotate(10))
# print("\nreflect", reflect(10))
# print("\nproject", project(10))
pi = 3.14159265359
points_orange = np.dot(points, rotate(90))
points_orange = np.dot(points_orange, reflect(pi/3))


#points_green = np.dot(points, rotate(149.7)) - 2
points_green = np.dot(points, rotate(pi/1.4))
# points_green = np.dot(points_green, project(np.sin(pi)))
points_green = np.dot(points_green, rotate(70.5))
points_green = np.dot(points_green, rotate(3.141592/2)) + [-2.5, 1.5]

points_red = np.dot(points, rotate(90))
points_red = np.dot(points_red, reflect(pi/3)) + [-5.1,2.9]






# points_green = np.dot(points_green, reflect(20))
#Show the sets of points
#prints J
plt.scatter([c[0] for c in points], [c[1] for c in points])
plt.scatter([c[0] for c in points_orange], [c[1] for c in points_orange])
plt.scatter([c[0] for c in points_green], [c[1] for c in points_green])
plt.scatter([c[0] for c in points_red], [c[1] for c in points_red])




#prints line
t = np.linspace(-10, 10, 100)
plt.plot(t,t*np.tan(5*np.pi/6), "-.r")
plt.show()