# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 19:59:17 2023

@author: wilks
"""

import numpy as np

def linear_encode(info_bits, generator_matrix):
    """
    Linearly encode information bits into codewords using a generator matrix.

    Args:
    info_bits (numpy array): An array of information bits (a row vector).
    generator_matrix (numpy array): The generator matrix of the linear code.

    Returns:
    codeword (numpy array): The encoded codeword.
    """
    # Ensure info_bits is a row vector
    if len(info_bits.shape) == 1:
        info_bits = info_bits.reshape(1, -1)

    # Perform linear encoding
    codeword = np.dot(info_bits, generator_matrix)

    return codeword

# Example usage:
if __name__ == "__main__":
    # Define the generator matrix (A) for your linear code
    generator_matrix = np.array([[1, 0, 1, 1],
                                 [0, 1, 1, 0]])

    # Define the information bits (a row vector)
    info_bits = np.array([[1, 0]])

    # Encode the information bits
    encoded_codeword = linear_encode(info_bits, generator_matrix)

    print("Encoded Codeword:", encoded_codeword)
