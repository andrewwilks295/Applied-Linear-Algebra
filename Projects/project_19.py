# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 11:02:36 2023

@author: wilks
"""

import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-whitegrid')

plt.axis([-10,10,-3,3])
x = np.linspace(-10, 10, 1000)

f = np.piecewise(x, [((-4*np.pi <= x) & (x < -3*np.pi)),  
                     ((-3*np.pi <= x) & (x < -2*np.pi)),
                     ((-2*np.pi <= x) & (x < -1*np.pi)), 
                     ((-1*np.pi <= x) & (x < 0)), 
                     ((0 <= x) & (x < np.pi)),
                     ((np.pi <= x) & (x < 2*np.pi)),
                     ((2*np.pi <= x) & (x < 3*np.pi))], 
                 [1,0,1,0,1,0,1])
plt.plot(x,f)

x_vector = np.arange(.1,2*np.pi,2*np.pi/101)
y_vector = np.array([round(np.sin(i)+.5) for i in x_vector])
y_vector = [i-.5 for i in y_vector]

matrix_100 = np.zeros((100,25))
for i in range(100):
    # print(i, "-------------------")
    for j in range(25):
        # print(i,j)
        # print(((j + 1) *math.sin(x_vector[i]) * (2 * j - 1)))
        matrix_100[i][j] = (np.sin(x_vector[i] * (2 * j + 1)))

A = matrix_100
b = y_vector
#create and solve your linear system here. You will need a coefficient matrix A and an augmented column b
#Recall that np.sin(x) gives the sine function in Python, where the angle is measured in radians.

c = np.linalg.lstsq(A,b,rcond=None)[0]
plt.plot(x,1/2+sum([c[j]*np.sin((2*j+1)*x) for j in range(25)]))

plt.show()