# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 19:27:44 2023

@author: wilks
"""

import numpy as np

# Define the given points as (x, y) pairs
points = [(-2, 231), (-1, 19), (0, 5), (1, 9), (2, 19), (3, -169),
          (-1.5, 100), (-0.5, 20), (0.5, 12), (2.5, 0), (3.5, -25)]

# Extract x and y values
x_values = [point[0] for point in points]
y_values = [point[1] for point in points]

# Create the matrix A for the system of equations
A = np.zeros((11, 6))
for i, x in enumerate(x_values):
    A[i] = [1, x, x**2, x**3, x**4, x**5]

# Solve the system of equations to find the coefficients a0, a1, a2, a3, a4, a5
coefficients = np.linalg.lstsq(A, y_values, rcond=None)[0]

# Coefficients contains the values of a0, a1, a2, a3, a4, a5
a0, a1, a2, a3, a4, a5 = coefficients

# Print the coefficients
print(f'a0: {a0}')
print(f'a1: {a1}')
print(f'a2: {a2}')
print(f'a3: {a3}')
print(f'a4: {a4}')
print(f'a5: {a5}')

# Define the given points as (x, y) pairs
points = [(-2, 12/11), (-1, 3/2), (0, 2), (1, 0), (2, 0),
          (-1.5, 10/3), (-0.5, 20/15), (0.5, -12/5), (2.5, -11/3), (3.5, -25/7)]

# Extract x and y values
x_values = [point[0] for point in points]
y_values = [point[1] for point in points]

# Create the matrix A for the system of equations
A = np.zeros((10, 5))
for i, x in enumerate(x_values):
    A[i] = [1, x, x**2, (x / (1 + 1 * x + 1 * x**2)), (x**2 / (1 + 1 * x + 1 * x**2))]

# Solve the system of equations to find the coefficients a0, a1, a2, b1, b2
coefficients = np.linalg.lstsq(A, y_values, rcond=None)[0]

# Coefficients contains the values of a0, a1, a2, b1, b2
a0, a1, a2, b1, b2 = coefficients

# Print the coefficients
print("---------------------")
print(f'a0: {a0}')
print(f'a1: {a1}')
print(f'a2: {a2}')
print(f'b1: {b1}')
print(f'b2: {b2}')

