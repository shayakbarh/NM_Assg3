# Root finding using Newton-Raphson method

from scipy.optimize import newton
import numpy as np
import matplotlib.pyplot as plt


# Define the function and its derivative
def f(x):
    return np.sin(np.cos(np.exp(x)))

def df(x):
    # Replace this with the derivative you obtained from Wolfram Alpha
    return -np.exp(x)* np.cos(np.cos(np.exp(x))) * np.sin(np.exp(x))


# Use the Newton-Raphson method to find the roots with initial guess -1
root_1 = newton(f, -1, fprime = df)
print("Solution of the equation with initial guess -1: ", root_1)

# Use the Newton-Raphson method to find the roots with initial guess -0.1
root_2 = newton(f, -0.1, fprime = df)
print("Solution of the equation with initial guess -0.1: ", root_2)

# Plot the function
xx = np.linspace(-2,10,10000)
yy = f(xx)

plt.plot(xx,yy, label = "sin(cos(exp(x)))")
plt.scatter(-1, 0, label = "initial guess of root -1", color = 'purple')
plt.scatter(root_1,0, label = "final root with initial guess -1", color = 'red')
plt.scatter(-0.1, 0, label = "initial guess of root -0.1", color = 'orange')
plt.scatter(root_2,0, label = "final root with initial guess -0.1", color = 'green')
plt.legend(loc = "upper left")
plt.title("Newton-Raphson Method for root finding")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.show()