import numpy as np
from scipy.optimize import minimize

data_points = [(-2, 231), (-1, 19), (0, 5), (1, 9), (2, 19), (3, -169),
               (-1.5, 100), (-0.5, 20), (0.5, 12), (2.5, 0), (3.5, -25)]

lambda_reg = 0.1

def polynomial(params, x):
    a0, a1, a2, a3, a4, a5 = params
    return a0 + a1 * x + a2 * x**2 + a3 * x**3 + a4 * x**4 + a5 * x**5

def objective(params):
    error = 0
    for x, y in data_points:
        error += (y - polynomial(params, x))**2
    regularization_term = lambda_reg * np.sum(np.array(params)**2)
    return error + regularization_term

initial_guess = [1, 1, 1, 1, 1, 1]

result = minimize(objective, initial_guess)

optimal_coefficients = result.x

print("Optimal Coefficients (a0, a1, a2, a3, a4, a5):", optimal_coefficients)



# Given data points
data_points = [
    (-2, 12/11), (-1, 3/2), (0, 2), (1, 0), (2, 0),
    (-1.5, 10/3), (-0.5, 20/15), (0.5, -12/5), (2.5, -11/3), (3.5, -25/7)
]

# Regularization coefficient
lambda_reg = 0.1

# Define the function to fit (f(x) = (a0 + a1x + a2x^2) / (1 + b1x + b2x^2))
def function(params, x):
    a0, a1, a2, b1, b2 = params
    return (a0 + a1 * x + a2 * x**2) / (1 + b1 * x + b2 * x**2)

# Define the objective function to minimize (including the regularization term)
def objective(params):
    error = 0
    for x, y in data_points:
        error += (y - function(params, x))**2
    regularization_term = lambda_reg * np.sum(np.array(params)**2)
    return error + regularization_term

# Initial guess for the coefficients
initial_guess = [0.1, 0.1, 0.1, 0.1, 0.1]  # Adjust initial guess

# Minimize the objective function to find the coefficients
result = minimize(objective, initial_guess)

# Extract the optimal coefficients
optimal_coefficients = result.x

print("Optimal Coefficients (a0, a1, a2, b1, b2):", optimal_coefficients)
