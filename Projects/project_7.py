# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 15:34:17 2023

@author: wilks
"""
import numpy as np

def row_scaling(a, b, s, row):
    scaled_coeff_matrix = np.copy(a)
    scaled_aug_matrix = np.copy(b)
    
    scaled_coeff_matrix[row] *= s
    scaled_aug_matrix[row] *= s
    return scaled_coeff_matrix, scaled_aug_matrix

def row_replacement(a, b, scalar, i, j):
    scaled_coeff_matrix = np.copy(a)
    scaled_aug_matrix = np.copy(b)
    
    scaled_coeff_matrix[j] *= scalar
    scaled_aug_matrix[j] *= scalar
    
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

m = np.array([[1, 2, 3],
     [5, 6, 7],
     [9, 10, 11]])
am = np.array([4, 8, 12])
scale_num = 2
row_num = 0
row_num2 = 1
row_num3 = 2
print("------------------------------------------------")
print("ORIGIONAL\n", m, am)
print("------------------------------------------------")


print("\n\n------------------------------------------------")
print("ROW SCALING\n")
a, b = row_scaling(m, am, scale_num, row_num)
print("scaled row", row_num + 1, "by", scale_num, "\n", a, b)
print("------------------------------------------------")

print("\n\n------------------------------------------------")
print("ROW REPLACEMENT\n")

a, b = row_replacement(m, am, scale_num,row_num, row_num2)
print("replaced row", row_num+1, "with row", row_num+1, "+ row", scale_num, "*", row_num2 + 1, "\n",a, b)
print("------------------------------------------------")

m = np.array([[1, 2, 3],
     [5, 6, 7],
     [9, 10, 11]])
am = np.array([4, 8, 12])
row_swap1 = 0
row_swap2 = 1
row_swap3 = 2
print("\n\n------------------------------------------------")
print("ROW INTERCHANGE\n")
a, b = row_interchange(m, am, row_swap1, row_swap3)
print("Interchanged row", row_swap1 + 1, "with row", row_swap3 + 1, "\n",a, b)
print("------------------------------------------------")
