# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 14:37:34 2023

@author: wilks
"""
import numpy as np
import sympy as sp


def row_replacement(a, b, scalar, i, j):
    scaled_coeff_matrix = np.copy(a)
    scaled_aug_matrix = np.copy(b)
    
    scaled_coeff_matrix[j] = scaled_coeff_matrix[j] * scalar
    scaled_aug_matrix[j] = scaled_aug_matrix[j] * scalar
    
    a[i] += scaled_coeff_matrix[j]
    b[i] += scaled_aug_matrix[j]
    
    return a, b

def row_interchange(a, b, i, j):
    interchange_coeff_matrix = np.copy(a)
    interchange_aug_matrix = np.copy(b)
    
    interchange_coeff_matrix[i] = a[j]
    interchange_coeff_matrix[j] = a[i]
    interchange_aug_matrix[i] = b[j]
    interchange_aug_matrix[j] = b[i]
    
    return interchange_coeff_matrix, interchange_aug_matrix

def row_scaling(a, b, s, row):
    scaled_coeff_matrix = np.copy(a)
    scaled_aug_matrix = np.copy(b)
    
    scaled_coeff_matrix[row] = scaled_coeff_matrix[row] * s
    scaled_aug_matrix[row] = scaled_aug_matrix[row] * s
    return scaled_coeff_matrix, scaled_aug_matrix

def find_scalar(pivot, s):
    # Define the symbolic variable
    x = sp.symbols('x')

    # Define the equation
    equation = pivot * x + s

    # Solve for x
    solutions = sp.solve(equation, x)

    return solutions[0]

def zero_below(coefficient_matrix, augmented_matrix, i, j):
    pivot = coefficient_matrix[i][j]
    if pivot == 0: #check to see if the pivot is zero
        for k in range(len(coefficient_matrix[:,j])): #iterates through rows to find the first non zero
            if coefficient_matrix[k][j] != 0:
                coefficient_matrix, augmented_matrix = row_interchange(coefficient_matrix, augmented_matrix, i, k)
                break
    for k in range(i, len(coefficient_matrix[:,j])):#i keeps us from changing the values above the pivot point
        if k != i and coefficient_matrix[k][j] != 0: #avoids changing the pivot position and if zero is already there
            # print(coefficient_matrix[k][i])
            scalar = find_scalar(pivot, coefficient_matrix[k][i])
            coefficient_matrix, augmented_matrix = row_replacement(coefficient_matrix, augmented_matrix, scalar, k, i)
    # print(coefficient_matrix, augmented_matrix)
    return coefficient_matrix, augmented_matrix

def zero_above(coefficient_matrix, augmented_matrix, i, j):
    pivot = coefficient_matrix[i][j]
    if pivot != 1:
        piv_scale = 1 / pivot
        coefficient_matrix, augmented_matrix = row_scaling(coefficient_matrix, augmented_matrix, piv_scale, j)
        pivot = coefficient_matrix[i][j] #sets pivot to 1
    for k in range(i, -1, -1):#-1 as the final value lets us access the zeroith spot and the last -1 is a decrementor
        if k != i and coefficient_matrix[k][j] != 0:
            scalar = find_scalar(pivot, coefficient_matrix[k][i])
            coefficient_matrix, augmented_matrix = row_replacement(coefficient_matrix, augmented_matrix, scalar, k, i)
    return coefficient_matrix, augmented_matrix
    
    
    
m = np.array([[1, 2, 3],
     [5, 6, 7],
     [9, 10, 11]])
am = np.array([4, 8, 12])
print("\n\n\n\n\nPROJECT 9\n-----------------------------")
print("This is the origional coefficent and augmented matrix\n")
print(m, am)
print("-----------------------------")

print("\n-----------------------------")
print("TASK 1")
print("-----------------------------")
m, am = zero_below(m, am, 0, 0)
print("\nHere below, we use the zero_below function to check if the pivot at (1,1) is zero. If it is, we loop through the rows in one column to find the first non-zero value then we use the interchange function to switch them. Next, We use the find_scalar function to find the scalar to use the row_replacement function to get the zeros below the pivot.\n")
print(m, am)

print("-----------------------------\n")
m, am = zero_below(m, am, 1, 1)
print("Here below, we switch the pivot point to spot (2,2) in the matrix inorder to repeat everything in the pervious step. Fortunately, the last row becomes all zeros so we did not have to call the next pivot because there isn't one. \n")
print(m, am)
print("-----------------------------")

print("\n-----------------------------")
print("TASK 2")
print("-----------------------------\n")
m, am = zero_above(m, am, 1, 1)
print("Here below, our pivot point is still (2,2), but now we are using the zero_above function. The first step was to make sure that the pivot point was 1 and if not, the find_scalar function would make the pivot point to 1 and change the row values. Next, we look at the values above the pivot point and make them zero. It was tricky at first with the for loop because I forgot they iterate by +1 every time, so I had to switch it to -1.\n")
print(m, am)
print("-----------------------------")





