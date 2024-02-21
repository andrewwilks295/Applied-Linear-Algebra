# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 13:29:23 2023

@author: wilks
"""
import numpy as np

#US military budget from 1960-2021 (in billion current U.S. dollars)
budget = np.array([
    47.35, 49.88, 54.65, 54.56, 53.43, 54.56, 66.44, 78.40, 84.33, 84.99,
    83.41, 78.24, 80.71, 81.47, 89.28, 92.08, 94.72, 104.67, 113.38, 126.88, 143.69,
    176.56, 221.67, 223.43, 245.15, 272.16, 295.55, 304.09, 309.66, 321.87, 325.13,
    299.37, 325.03, 316.72, 308.08, 295.85, 287.96, 293.17, 291.00, 298.09, 320.09,
    331.81, 378.46, 440.53, 493.00, 533.20, 558.34, 589.59, 656.76, 705.92, 738.01,
    752.29, 725.21, 679.23, 647.79, 633.83, 639.86, 646.75, 682.49, 734.34, 778.40,
    800.67
])

n = len(budget)
A = np.array([[1,k] for k in range(n)])

x = np.linalg.lstsq(A,budget, rcond=None)[0]

import matplotlib.pyplot as plt
plt.scatter(np.arange(1959,2021) + 1, budget)
plt.plot(np.arange(1959,2021) + 1, A @ x, 'r')
plt.show()

#This is worthy as a contribution becuase firstly, I had to go out
#and find data and create the data. Secondly, I think this could
#replace the text book example of petrolium or be added becuase
#this is more relevent to our lives since this is our military
#budget. I am submitting this as a data set and I got the
#information from the link below. 

#https://www.macrotrends.net/countries/USA/united-states/military-spending-defense-budget



