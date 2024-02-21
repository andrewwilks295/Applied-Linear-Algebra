# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 16:48:59 2023

@author: wilks
"""

import numpy as np

### Task 1 ################
print("~Task 1~")
#Let A denote the adjacency matrix for this graph Γ
A =  np.array([[0,1,0,0,1,1],
               [1,0,1,1,0,1],
               [0,1,0,1,1,0],
               [0,1,1,0,1,0],
               [1,0,1,1,0,1],
               [1,1,0,0,1,0]])
print(f"Adjacency Matrix\n {A}\n")

### Task 2 ###############################
print("~Task 2~")
k=100

row_sums = A.sum(axis=1, keepdims=True)
T = A / row_sums#The transition matrix T will be time-invariant and can be considered a modification of the adjacency matrix A for Γ
T = T.T
print(f"Transition Matrix\n {T}\n")
print("What is the relationship between these two matrices?")
print("    T is equal to each value in A divided by the sum of it's column.") #What is the relationship between these two matrices?

print("\nStarting at vertex A")
X = np.zeros((k+1,6))
X[0] = np.array([1,0,0,0,0,0]) #A
# X[0] = np.array([0,1,0,0,0,0]) #B
# X[0] = np.array([0,0,1,0,0,0]) #C
# X[0] = np.array([0,0,0,1,0,0]) #D
# X[0] = np.array([0,0,0,0,1,0]) #E
# X[0] = np.array([1,0,0,0,0,1]) #F


#Create a linear dynamical system X such that X[t] is the 6-vector of probabilities that a person following a random walk will be at vertex A after t steps.

for i in range(0,k):
    X[i + 1] = T @ X[i]


print(f"x_3 = {X[3]}\nx_10 = {X[10]}\nx_100 = {X[100]}")

print("\nWhat pattern do you see emerging?")
print("    A, C, D, and F have the same probabilites and B and E have the same probabilites.") #What pattern do you see emerging? 
print("Also, they all come to a point where the vector is (0.15, 0.2, 0.15, 0.2, 0.15)\n")

### Task 3 ###############################
print("\n~Task 3~")
print("Starting at vertex B")
X = np.zeros((k+1,6))
X[0] = np.array([0,1,0,0,0,0]) #B

#Create a linear dynamical system X such that X[t] is the 6-vector of probabilities that a person following a random walk will be at vertex B after t steps.

for i in range(0,k):
    X[i + 1] = T @ X[i]

print(f"x_3 = {X[3]}\nx_10 = {X[10]}\nx_100 = {X[100]}")

print("\nWhat pattern do you see emerging?")
print("    The exact same thing from task two. The higher Xn is, the closer we get to") #What pattern do you see emerging? 
print("(0.15, 0.2, 0.15, 0.2, 0.15), also this adds up to 1.0 or 100%\n")
#What happens if another vertex is the starting location? 
#Make a conjecture about X[t] as t -> infinity. 
#How could this information had been gleaned from the original graph in retrospect?
print("What happens if another vertex is the starting location?")
print("    If another vertex is the starting location, it will mimic either A or B.\n")
print("Make a conjecture about X[t] as t -> infinity")
print("    As t approaches infinity, the values will add up to 100% and give the probability of going to that vertice\n")
print("How could this information had been gleaned from the original graph in retrospect?")
print("    You could of done the math using the number of verticies and the chance your verticie is an option. The math is")
print("using A as an example: 3/10 = 0.3 then you would divide by two because there is a 50% chance that vertice could")
print("be an option, therefore the math is 3 / 10 / 2 = 0.15, or for B: 4 / 10 / 2 = 0.2")