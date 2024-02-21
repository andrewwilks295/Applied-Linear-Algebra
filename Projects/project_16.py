# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 17:28:06 2023

@author: wilks
"""

import numpy as np

### TASK 1 ###
def gram_schmidt(vectors):
    num_vectors = len(vectors)
    ortho_basis = []

    for i in range(num_vectors):
        ortho_vec = vectors[i]
        for j in range(i):
            ortho_vec -= np.dot(vectors[i], ortho_basis[j]) / np.dot(ortho_basis[j], ortho_basis[j]) * ortho_basis[j]

        norm = np.linalg.norm(ortho_vec)
        if norm > 0:
            ortho_vec /= norm

        ortho_basis.append(ortho_vec)

    return ortho_basis

A = np.array([[1.0,1.0,1.0,1.0],[0.0,1.0,1.0,1.0],[0.0,0.0,1.0,1.0]]) 
gs = gram_schmidt(A)

print("\n\n-------------------\nTASK 1\n-------------------\n")

for i, vector in enumerate(gs):
    print(f"Orthonormal Vector {i + 1}: {vector}")
    print("-------------------------------------------")
  

### TASK 2 ###
def IsIndependent_gs(vectors, tol = 0):
    num_vectors = len(vectors)
    ortho_basis = []

    for i in range(num_vectors):
        ortho_vec = vectors[i]
        for j in range(i):
            ortho_vec -= np.dot(vectors[i], ortho_basis[j]) / np.dot(ortho_basis[j], ortho_basis[j]) * ortho_basis[j]

        if np.linalg.norm(ortho_vec) < tol:
            return False

        norm = np.linalg.norm(ortho_vec)
        if norm > 0:
            ortho_vec /= norm

        ortho_basis.append(ortho_vec)

    return True
    
A = np.array([[ 1.0, 2, 3, 4, 5, 6, 7, 8, 9, 10],
              [ 3, 2, 1, 6, 0, 0, 0, 3, 2, 1],
              [ 0, 0, 4, 2, -1, 2, 0, 0, 8, -9],
              [ 0, 0, 0, 0, 0, 1, 2, 3, 4, 5],
              [ 6, 1, -5, 6, -5, -5, 1, 8, -6, 9],
              [ 2, 3, 3, 3, 3, 2, 1, 0, 0, 0],
              [ 0, -2, -2, 4, -1, 3, 7, 14, 15, 16],
              [ 7, 7, 6, 6, 5, 5, 4, 4, 3, 3],
              [ 7, -2, -1, 2, 10, 8, -3, -2, 1, 19],
              [ 3, -2, 0, 0, 2, 2, -5, -5, 0, 0],
              [ 3, -4, -3, 2, 1, 1, 0, 3, 3, 2],
              [ 1, 1, -1, -1, 2, 0, 2, 2, 1, 1]])
print("\n\n-------------------\nTASK 2\n-------------------\n")
print("linearly independent:", IsIndependent_gs(A))