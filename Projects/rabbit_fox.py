# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 16:48:10 2023

@author: wilks
"""

import numpy as np

T = 20 # number of years 
A = np.array([[1.9, -8],    #transition matrix for predator-prey model
              [0.1,0.1]])

X = np.zeros((2,T+1,2))     #Initialization of 2 dynamical systems: X[0] and X[1]
                            #X[0] is simulation without new hunting tags
                            #X[1] is simulation with new hunting tags
X[0,0] = np.array([100,12]) #initial state: rabbits, foxes by thousands
X[1,0] = X[0,0]

#construct the dynamical systems X[0] without tags and X[1] with tags here
#my work-------------------------------

#without tags
for i in range(0,T):
    X[0, i + 1] = A @ X[0,i]
    # print(X)

#with tags
for i in range(0,T):
    # X[1, i, 1] = X[1, i, 1] - 1
    X[1, i + 1] = A @ X[1,i]
    X[1, i + 1, 1] = X[1, i + 1, 1] - 1
#--------------------------------------
   
### GRAPHING ############################
import matplotlib.pyplot as plt
labels = ['Without New Tags', 'With New Tags']
for i in range(2):
    plt.plot(np.arange(len(X[i])), X[i,:,0], "-")
    plt.plot(np.arange(len(X[i])), X[i,:,1], "--")
    plt.xlabel(labels[i])
    plt.xlim(0,T)
    plt.ylim(0,300)
    plt.legend(['Rabbit', 'Foxes'])
    plt.show()
    print(f"Population of Rabbits and Foxes over {T} years {labels[i]}:")
    print(X[i,:,0])
    print(X[i,:,1],"\n")
    
### FINAL ANSWER #########################
print("Based off the 20 year model, without new tags is better. New tags, after 20") # Who is right based upon these models? Defend your answer.
print("years, has a rabbit population of 208,391 which surpasses the limt of 200,000.")
print("Without new tags, the rabbit population is 144,276 which is significantly lower.")
print("In conclusion, the ecologist's prediction is correct.")