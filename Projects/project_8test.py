# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 13:33:11 2023

@author: wilks
"""

import sympy as sp

def create_linear_system(normal_vectors, particular_solution):
    """
    Create a linear system in the form of an augmented matrix.

    Args:
    normal_vectors (list of lists): List of normal vectors, where each sublist represents a normal vector.
    particular_solution (list or sp.Matrix): The particular solution as a column vector.

    Returns:
    sp.Matrix: Augmented matrix representing the linear system.
    """

    # Convert the list of normal vectors to a SymPy Matrix
    normal_matrix = sp.Matrix(normal_vectors)

    # Convert the particular solution to a SymPy Matrix if needed
    if not isinstance(particular_solution, sp.Matrix):
        particular_solution = sp.Matrix(particular_solution)

    # Stack the normal matrix and particular solution column vector horizontally to form the augmented matrix
    augmented_matrix = sp.Matrix.hstack(normal_matrix, particular_solution)

    return augmented_matrix

# Example usage:
normal_vectors = [[2, -1, 3], [1, 4, -2], [-3, 2, 1]]
particular_solution = [5, 3, -7]

augmented_matrix = create_linear_system(normal_vectors, particular_solution)
sp.pprint(augmented_matrix)

