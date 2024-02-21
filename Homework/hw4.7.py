import numpy as np

# Define the weighted matrices A and B
A = np.array([[2, 3], [4, 9], [0.5, 13]])
B = np.array([0, 16, 13])

# Define the weight matrix W
W = np.array([1, 0.5])

# Compute the weighted matrices AW and BW
AW = A * W[:, np.newaxis]
BW = B * W

# Compute the weighted normal equations ATA and ATB
ATA = np.dot(AW.T, AW)
ATB = np.dot(AW.T, BW)

# Solve the weighted normal equations to find the least squares solution
solution = np.linalg.lstsq(ATA, ATB, rcond=None)[0]

print("Least Squares Solution:", solution)
