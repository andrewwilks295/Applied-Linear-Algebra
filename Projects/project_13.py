# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 15:24:42 2023

@author: wilks
"""
import numpy as np

### TASK 1 #########
def Hamming_dist(x,y):
    count = 0
    for a in range(0, len(x)):
        if(x[a] != y[a]):
            count+=1
    return count;
    
def Hamming_norm(x):
    count = 0;
    for a in x:
        if(a == 1):
            count += 1
    return count
    
Words = np.array([[1,0,1,0,1],[1,1,0,1,0],[0,0,0,1,1]])

#Compute Hamming Distances
for i in range(len(Words)):
    for j in range(i+1,len(Words)):
        print(f"Hamming distance between {Words[i]} and {Words[j]} is {Hamming_dist(Words[i], Words[j])}.")
        
#Compute Hamming Norms
for w in Words:
    print(f"Hamming norm of {w} is {Hamming_norm(w)}.")
print("\n")

### TASK 2 #########
C = np.array([[0,0,0,0,0],[1,1,1,1,0],[1,0,1,0,1],[0,1,0,1,1]])

def decode_C(w):
    l = len(w)
    distances = np.zeros(l)
    for i in range(l):
        distances[i] = np.linalg.norm(w[i])
    return np.argmin(distances)


Words = np.array([[0,1,0,1,1],[1,1,1,0,0],[1,0,0,0,1]])
for w in Words:
    print(f"{w} decodes as {decode_C(w)}.")
print("\n")

### TASK 3 #########
A = np.array([[0,0,0,1,1,1],[0,1,1,0,1,1],[1,0,1,0,0,1]])

def detect_A(w):
    temp = np.multiply(w, A)
    for x in temp:
        if(Hamming_norm(x) % 2 != 0):
            return True
    return False

Words = np.array([[1,1,1,0,0,0],[1,1,0,1,1,0],[1,1,1,1,0,1]])
for w in Words:
    print(f"{w} has error? {detect_A(w)}.")
print("\n")