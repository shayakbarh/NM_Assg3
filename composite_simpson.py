# composite simpson's rule to find integration
import numpy as np

# Define the composite simpson's rule
def composite_simpson(func, a, b, n):
    h = (b - a)/n
    result = func(a) + func(b)
    for i in range(1, n, 2):
        result += 4 * func(a + h*i)
    
    for i in range(2, n, 2):
        result += 2 * func(a + h*i)

    result *= h/3

    return result

# function 1: x*ln(x)
def func_1(x):
    return x*np.log(x)

# function 2: 2/(x**2 + 4)
def func_2(x):
    return 2/(x**2 + 4)

# function 3: tan(x)
def func_3(x):
    return np.tan(x)

# integral 1: from 1 to 2 with n = 4
result_1 = composite_simpson(func_1, 1, 2, 4)

# integral 2: from 0 to 2 with n = 6
result_2 = composite_simpson(func_2, 0, 2, 6)

# integral 3: from 0 to (3*pi)/8 with n = 8
result_3 = composite_simpson(func_3, 0, 3*np.pi/8, 8)

#print the results
print("Using Composite Simpson's Rule")
print("Result for integral of x*lnx : ", result_1)
print("Result for integral of 2/(x**2 + 4) : ", result_2)
print("Result for integral of tan(x) : ", result_3)