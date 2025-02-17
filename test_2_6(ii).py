import scipy.integrate as spi
import numpy as np

# Define the function to integrate
def f(x,y):  # scipy expects inner variable first
    return (x * y) / np.sqrt(x**2 + y**2 + 1)

# Integration limits
x_lower, x_upper = 0, 1
y_lower, y_upper = 0, 1

# Compute the integral
result, error = spi.dblquad(f, x_lower, x_upper, lambda x: y_lower, lambda x: y_upper)

print("Double Integral Result:", result)
