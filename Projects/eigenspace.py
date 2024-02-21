# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 17:32:54 2023

@author: wilks
"""

import numpy as np
import sympy as sp

def rowScaling(coefficient_matrix, augmented_matrix, scalar, i):
    #your code from Project: Elementary Row Operations
    scaled_coeff_matrix = np.copy(coefficient_matrix)
    scaled_aug_matrix = np.copy(augmented_matrix)
    scaled_coeff_matrix[i] *= scalar
    scaled_aug_matrix[i] *= scalar
    return scaled_coeff_matrix, scaled_aug_matrix

def rowReplacement(a, b, scalar, i, j):
    scaled_coeff_matrix = np.copy(a)
    scaled_aug_matrix = np.copy(b)
    
    scaled_coeff_matrix[j] = scaled_coeff_matrix[j] * scalar
    scaled_aug_matrix[j] = scaled_aug_matrix[j] * scalar
    
    a[i] += scaled_coeff_matrix[j]
    b[i] += scaled_aug_matrix[j]
    
    return a, b

def rowInterchange(a, b, i, j):
    interchange_coeff_matrix = np.copy(a)
    interchange_aug_matrix = np.copy(b)
    
    interchange_coeff_matrix[i] = a[j]
    interchange_coeff_matrix[j] = a[i]
    interchange_aug_matrix[i] = b[j]
    interchange_aug_matrix[j] = b[i]
    
    return interchange_coeff_matrix, interchange_aug_matrix

def zeroBelow(coefficient_matrix, augmented_matrix, i, j): #need to replace pivot with i and j?
    #your code from Project: Row Reduction
    pivot = coefficient_matrix[i][j]

    if pivot == 0:
        for k in range(len(coefficient_matrix)):
            if coefficient_matrix[k][j] != 0:
                coefficient_matrix, augmented_matrix = rowInterchange(coefficient_matrix, augmented_matrix, i, k)
                break

    for k in range(i, len(coefficient_matrix)):
        if k != i and coefficient_matrix[k][j] != 0:
            scalar = findScalar(pivot, coefficient_matrix[k][i])
            coefficient_matrix, augmented_matrix = rowReplacement(coefficient_matrix, augmented_matrix, scalar, k, i)

    return coefficient_matrix, augmented_matrix

def zeroAbove(coefficient_matrix, augmented_matrix, i, j): # change pivot to i and j?
    #your code from Project: Row Reduction
    pivot = coefficient_matrix[i][j]

    if pivot != 1:
        pivot_scale = 1 / pivot
        coefficient_matrix, augmented_matrix = rowScaling(coefficient_matrix, augmented_matrix, pivot_scale, j)
        pivot = 1 # ADDED 10/26/2023 NEED TO SHOW ANDREW SMITH
    
    for k in range(i, -1, -1):
        if k != i and coefficient_matrix[k][j] != 0:
            scalar = findScalar(pivot, coefficient_matrix[k][i])
            coefficient_matrix, augmented_matrix = rowReplacement(coefficient_matrix, augmented_matrix, scalar, k, i)

    return coefficient_matrix, augmented_matrix

def findScalar(pivot, s):
    # Define the symbolic variable
    x = sp.symbols('x')

    # Define the equation
    equation = pivot * x + s

    # Solve for x
    solutions = sp.solve(equation, x)

    return solutions[0]

def forwardPhase(coefficient_matrix, constant_matrix):
    #your code from Project: RREF
    reducedCoefficientMatrix = coefficient_matrix
    reducedConstantMatrix = constant_matrix
    pivots = []

    for i in range(len(coefficient_matrix)):
        reducedCoefficientMatrix, reducedConstantMatrix = zeroBelow(reducedCoefficientMatrix, reducedConstantMatrix, i, i)
        pivots.append([i,i])


    return reducedCoefficientMatrix, reducedConstantMatrix, pivots

def Reverse(lst):
   new_lst = lst[::-1]
   return new_lst

def backwardPhase(coefficient_matrix, constant_matrix, pivots): #this is broken apparently.
    #your code from Project: RREF
    reducedCoefficientMatrix = coefficient_matrix
    reducedConstantMatrix = constant_matrix

    # show this to Andrew Smith vvv
    # pivots = np.array([[2,2],[1,1],[0,0]])
    # this line ^^^ changes the solution in spot (0,0) from 2 to 0, but the correct solution is 0.5
    pivots = Reverse(pivots) #CHANGED THIS SHOW ANDREW SMITH !!!!!!!!!!!!!!!!!!!

    for i, j in pivots:
        reducedCoefficientMatrix, reducedConstantMatrix = zeroAbove(reducedCoefficientMatrix, reducedConstantMatrix, i, j)

    return reducedCoefficientMatrix, reducedConstantMatrix

def rref(coefficient_matrix, constant_matrix):
    c = forwardPhase(coefficient_matrix, constant_matrix)
    c = backwardPhase(c[0], c[1], c[2])
    return c[0], c[1]

def Null(matrix):
    M = matrix.copy()
    a = sp.Matrix(M).rref()
    A = np.array(a[0])
    pivots = np.array(a[1])
    freevar = np.setdiff1d(np.arange(len(A[0])),pivots)
    # print(pivots)
    # print(freevar)
    id_matrix = np.eye(len(A[0]))
    # print(id_matrix)
    # print(pivots)
    # print(A)
    _, n = A.shape
    
    temp = np.zeros((len(freevar),len(A[0])))
    for i in range(len(freevar)):
        temp[i, freevar[i]] = 1
        for j in range(len(pivots)):
            temp[i,pivots[j]] += -A[j,freevar[i]]
            
        
    # nul = np.zeros((len(A[0]) - len(pivots), len(A)))
    
    # x = 0
    # for i in range(len(A[0])):
    #     if np.sum(A[:, i]) != 0:
    #         nul[x] = A[:, i]
    #         x += 1
    return temp

def Eigenspace(matrix,eigenvalue):
    #write your code here
    #returns eigenspace, that is, 
    #returns a basis for the eigenspace of matrix with respect to eigenvalue
    A = matrix.copy()
    A = A - (eigenvalue * np.identity(len(A)))
    return Null(A)
   
### VERIFY ############################
print("Task 1")
A = np.array([[6,5,4,3,2,1],
              [5,4,3,2,1,6],
              [2,4,6,8,2,4],
              [0,1,0,1,2,6]])
print(np.round(Null(A),12))
print(Null(np.zeros((4,5))),"\n")

print("Task 2")
B = np.array([[17,5,5],
              [-41,-12,-14],
              [-19,-6,-4]])
print(np.round(np.linalg.eigvals(B),6))
print(Eigenspace(B,-3))
print(Eigenspace(B,2),"\n")

C = np.array([[6,10,0,-4],
              [3,5,0,-2],
              [12,24,-1,-8],
              [15,30,0,-11]])
print(np.round(np.linalg.eigvals(C),6))
print(Eigenspace(C,-1))
print(Eigenspace(C,0))
print(Eigenspace(C,1))