# Integration using diffrent methods

import numpy as np
from scipy.integrate import trapezoid, simpson, romberg

# Define the function to be integrated
def f(x):
    return np.exp(x)

# Define the integration interval [a, b]
a = 0
b = 1

# Number of points for numerical integration
num_points = 100

# Generate equally spaced x values
x_values = np.linspace(a, b, num_points)

# Trapezoidal rule
trapezoidal_result = trapezoid(f(x_values), x=x_values)

# Simpson's rule
simpson_result = simpson(f(x_values), x=x_values)

# Romberg method
romberg_result = romberg(f, a, b)

# Print the results
print(f'Trapezoidal rule result: {trapezoidal_result}')
print(f"Simpson's rule result: {simpson_result}")
print(f'Romberg method result: {romberg_result}')
