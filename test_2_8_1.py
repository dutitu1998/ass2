import sympy as sp

# Define the variables
x, y, r, theta = sp.symbols('x y r theta')

# Define P and Q
P = sp.exp(x) - y**3
Q = sp.cos(y) + x**3

# Compute partial derivatives
dQ_dx = sp.diff(Q, x)
dP_dy = sp.diff(P, y)

# Compute the integrand (dQ/dx - dP/dy)
integrand = dQ_dx - dP_dy

# Convert to polar coordinates (x = r*cos(theta), y = r*sin(theta))
integrand_polar = integrand.subs({x: r*sp.cos(theta), y: r*sp.sin(theta)})

# Multiply by 'r' since dA in polar coordinates is r dr dtheta
integrand_polar *= r

# Integrate over the unit disk (r from 0 to 1, theta from 0 to 2*pi)
result = sp.integrate(sp.integrate(integrand_polar, (r, 0, 1)), (theta, 0, 2*sp.pi))

# Print the result
print("The work done by the force field is:", result)
