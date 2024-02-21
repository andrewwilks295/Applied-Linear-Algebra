# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 18:06:51 2023

@author: wilks
"""

import numpy as np

### TASK 1 ###
def linear_code(A):
    idMat = np.eye(len(A))
    h = np.zeros([len(A), len(A)+len(A[0])])

    for i in range(len(A)):
        temp = np.append(A[i], idMat[i])
        h[i] = temp
    idMat = np.eye(len(A[0]))
    g = np.zeros([len(idMat)+len(A), len(idMat)])
    for i in range (len(idMat)):
        g[i] = idMat[i]
    for i in range(len(idMat), len(A)+len(idMat)):
        g[i] = A[i-len(idMat)]
    return h, g

    #Write code here
    #will output canonical parity check matrix
    #and generator matrix associated to A

A = np.array([[0,1,1],[1,1,0],[1,0,1]])
H,G = linear_code(A)
print(H,"\n",G,"\n")

### TASK 2 ###
def linear_encode(G,message):
    #write code here
    #will output the encoded message for
    #the linear code associated to generator matrix G
    if len(G.shape) == 1:
        G = G.reshape(1, -1)

    # Perform linear encoding
    codeword = np.dot(G, message)
    for i in range(len(codeword)):
        codeword[i] = codeword[i] % 2
    return codeword

A = np.array([[1,1],[1,0],[1,1]])
H,G = linear_code(A)
for w in [[0,0],[0,1],[1,0],[1,1]]:
    print(linear_encode(G,w))
print("\n")
    
# ### TASK 3 ###
def linear_decode(H,message):
    #H is transposed for ease of comparison later on
    trans = np.transpose(H)
    print("Original message: ", message)
    # print(H)
    #this np.dot calculation finds the Hx, Hy, etc 
    temp = np.dot(H, message)
    #then each value is modded by 2
    for x in range(len(temp)):
        temp[x] = temp[x] % 2
    if(sum(temp) == 0):
        print("There are no errors")
    else:
        check = False
        #checks for a matching column within the H
        for i in range(len(trans)):
            if (trans[i] == temp).all():
                # print(trans[i])
                # print(temp)
                
                #this error column start at 1 technically
                #does not count from zero like a python loop
                print("There is an error in column: ", i+1)
                message[i] = (message[i]+1)%2
                print("decoded: ", message)
                check = True
        if(not check):
            print("There are multiple errors. Please re-trasmit")
    return temp
        

A = np.array([[1,1,1,0,0],
              [1,0,1,1,1],
              [1,1,0,1,0],
              [0,0,1,1,1],
              [0,1,0,0,1]])
H,G = linear_code(A)
words = [[1,0,0,1,0,1,1,1,0,0],
          [0,1,1,0,1,0,0,1,0,0],
          [1,1,0,0,0,0,0,0,1,1],
          [1,1,0,0,1,0,1,0,1,0],
          [1,1,1,0,1,1,1,0,0,0]]


for w in words:
    print(linear_decode(H,w))
project18.py
Displaying project18.py.