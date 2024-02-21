import numpy as np

# Assuming A is a one-dimensional vector
A = np.array([1, 2, 2, 4])
o1 = 5

A = [1,1],[1,1]

A = [3,4],[0,3],[-4,0]

# Reshape the vector into a matrix with one row
# A_matrix = A.reshape(1, -1)

# Perform Singular Value Decomposition (SVD)
U, S, Vt = np.linalg.svd(A)

print("U matrix:")
print(U)
print("\nSigma matrix:")
print(np.diag(S))
print("\nV transpose matrix:")
print(Vt)
