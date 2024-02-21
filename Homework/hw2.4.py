# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 14:48:54 2023

@author: wilks
"""

import numpy as np

points = np.array([[-2, 12/11],
                  [-1, 3/2],
                  [0,2],
                  [1, 0],
                  [2, 0],
                  [3, 1/8]])
x = points[:,0]
y= points[:,1]

print("x = ",x)
print("y = ", y, "\n")

answer = 

V = np.vander(x, increasing=True)
print("V = ", V, "\n")

c = np.linalg.solve(V,y)
print("c = ", c)


reverse = lambda x: np.array([a for a in reversed(x)])

f = np.poly1d(reverse(c))
print(f)


import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8-whitegrid")

plt.ion()
domain = np.linspace(-3, 3, 100)
plt.xlim(-3,3)
plt.ylim(-1,25)
plt.scatter(x, y)
plt.plot(domain,f(domain))
plt.show()