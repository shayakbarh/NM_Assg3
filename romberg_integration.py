# Romberg integration to compute R3,3

import numpy as np 
from scipy.integrate import quad

# Function-1: x^2 * ln(x)
def func_1(x):
    return x**2 * np.log(x)

# Function-2: x^2 * e^(-x)
def func_2(x):
    return x**2 * np.exp(-x)

# Function-3: (cos(x))^2
def func_3(x):
    return np.cos(x)**2

# romberg integration function 
def romberg_integration(func, a, b, k, m):
    R = np.zeros((k,k), dtype = float)
    
    for i in range(k):
        R[i,0],_ = quad(func, a, b, limit = 2**(i + 1))
    
    for j in range(1,k):
        for i in range(j,k):
            R[i,j] = (4*j*R[i,j-1] - R[i-1,j-1])/(4*j - 1)

    return R[k-1,k-1]

# integrate Function-1 from 1 to 1.5 
result_1 = romberg_integration(func_1, 1, 1.5, 3, 3)

# integrate Function-2 from 0 to 1
result_2 = romberg_integration(func_2, 0, 1, 3, 3)

# integrate Function-3 from 0 to π/4
result_3 = romberg_integration(func_3, 0, np.pi/4, 3, 3)

#Print the results
print("\nUsing Romberg integration")
print("\nResult for integral of x^2 * lnx : ", result_1)
print("\nResult for integral of x^2 * exp(-x) : ", result_2)
print("\nResult for integral of (cos(x))^2 : ", result_3)
print(" ")