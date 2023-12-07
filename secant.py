from scipy.optimize import newton
import numpy as np

# Define the function
def func(x):
    return np.sin(np.cos(np.exp(x)))

# Set the initial guess
initial_guess = -0.1

# Use the Secant method (no need to specify fprime)
root_secant = newton(func, initial_guess)

# Print the result
print(f"Root with initial guess -0.1 using Secant method: {root_secant}")
