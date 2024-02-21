# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 18:58:58 2023

@author: wilks
"""

import numpy as np
import matplotlib.pyplot as plt
import math
plt.style.use('seaborn-whitegrid')

plt.ion()
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
#create and solve your linear system here. You will need a coefficient matrix A and an augmented column b
#Recall that np.sin(x) gives the sine function in Python, where the angle is measured in radians.
x_vector = np.arange(.1,2*np.pi,2*np.pi/25)
y_vector = np.array([round(np.sin(i)+.5) for i in x_vector])
y_vector = [i-.5 for i in y_vector]
print(y_vector)



# matrix_25 = [[0] * 25]* 25
matrix_25 = np.zeros((25,25))
print(len(matrix_25))
print(len(matrix_25[0]))
for i in range(25):
    # print(i, "-------------------")
    for j in range(25):
        # print(i,j)
        # print(((j + 1) *math.sin(x_vector[i]) * (2 * j - 1)))
        matrix_25[i][j] = (np.sin(x_vector[i] * (2 * j + 1)))

# for i in range(25):
c = np.linalg.solve(matrix_25, y_vector) #uncomment this line when you have set up the linear system and are ready to solve it
print(c)
plt.plot(x,1/2+sum([c[j]*np.sin((2*j+1)*x) for j in range(25)])) #uncomment this line when you are ready to graph g

plt.show()