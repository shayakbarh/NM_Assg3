# Root finding using bisection method

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import bisect

# define give function
def func(x):
    return np.sin(np.cos(np.exp(x)))

# Set the bracket for bisection
a, b = -1, 1

# Use the bisection method to find the root
root = bisect(func, a, b)

#Report the result
print(f"Root of the equation: {root}")

# Evaluate the function at the root
value_at_root = func(root)

# Report the value of the function at root
print(f"Value of sin(cos(exp(x))) at the root: {value_at_root}")

# Check it is zero or not
if value_at_root == 0:
    print("The value is exactly zero")
else:
    print("The value is not exactly zero")

if np.isclose(value_at_root, 0):
    print("The value is approximately zero.")
else:
    print("The value is not zero")

# Plot the function
xx = np.linspace(-2,10,10000)
yy = func(xx)

plt.plot(xx,yy, label='sin(cos(exp(x)))', color = "green")
plt.scatter(root,value_at_root, label='Root', color = 'red')
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.show()