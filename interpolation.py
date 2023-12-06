import numpy as np
from scipy.interpolate import UnivariateSpline
import matplotlib.pyplot as plt

# Given data
x_data = np.array([0, 1, 2, 3, 4, 5])
y_data = np.array([1.0, 2.0, 1.0, 0.5, 4.0, 8.0])

# Fit a linear spline
linear_spline = UnivariateSpline(x_data, y_data, k=1, s=0)

# Fit a quadratic spline
quadratic_spline = UnivariateSpline(x_data, y_data, k=2, s=0)

# Fit a cubic spline
cubic_spline = UnivariateSpline(x_data, y_data, k=3, s=0)

# Generate x values for the spline
x_spline = np.linspace(0, 5, 1000)

# Evaluate the linear spline at the generated x values
y_linear = linear_spline(x_spline)

# Evaluate the quadratic spline at the generated x values
y_quad = quadratic_spline(x_spline)

# Evaluate the cubic spline at the generated x values
y_cubic = cubic_spline(x_spline)

# Plot the original data and the linear, quadratic and cubic spline
plt.scatter(x_data, y_data, label='Original Data')
plt.plot(x_spline, y_linear, label='Linear Spline', color='green')
plt.plot(x_spline, y_quad, label='Quadratic Spline', color='red')
plt.plot(x_spline, y_cubic, label='Cubic Spline', color='blue')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolation')
plt.show()
