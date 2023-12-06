import numpy as np
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt

# Given data
x_data = np.array([0, 1, 2, 3, 4, 5])
y_data = np.array([1.0, 2.0, 1.0, 0.5, 4.0, 8.0])

# Use Lagrange's method to find the fifth-order polynomial
poly_coefficients = lagrange(x_data, y_data)

# Generate x values for the polynomial
x_poly = np.linspace(0, 5, 1000)

# Evaluate the polynomial at the generated x values
y_poly = np.polyval(poly_coefficients, x_poly)

# Plot the original data and the Lagrange polynomial
plt.scatter(x_data, y_data, label='Original Data')
plt.plot(x_poly, y_poly, label='Fifth-order Polynomial', color='purple')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Lagrange Polynomial Interpolation')
plt.show()
