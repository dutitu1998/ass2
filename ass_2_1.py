import sympy as sp 
import math 
 
# Define the parameter t 
t = sp.symbols('t') 
 
# Define the parametric equations for each part of the problem 
x1 = sp.ln(t) 
y1 = sp.exp(-t) 
z1 = t**3 
x2 = 2 * sp.cos(math.pi * t) 
y2 = 2 * sp.sin(math.pi * t) 
z2 = 3 * t 
 
# Define the points of tangency 
t0_1 = 2 
t0_2 = 1/3 
 
# Find the derivatives 
dx1_dt = sp.diff(x1, t) 
dy1_dt = sp.diff(y1, t) 
dz1_dt = sp.diff(z1, t) 
 
dx2_dt = sp.diff(x2, t) 
dy2_dt = sp.diff(y2, t) 
dz2_dt = sp.diff(z2, t) 
 
# Evaluate the derivatives at the points of tangency 
dx1_dt_val = dx1_dt.subs(t, t0_1) 
dy1_dt_val = dy1_dt.subs(t, t0_1) 
dz1_dt_val = dz1_dt.subs(t, t0_1) 
 
dx2_dt_val = dx2_dt.subs(t, t0_2) 
dy2_dt_val = dy2_dt.subs(t, t0_2) 
dz2_dt_val = dz2_dt.subs(t, t0_2) 
 
# Evaluate the parametric equations at the points of tangency 
x1_0 = x1.subs(t, t0_1) 
y1_0 = y1.subs(t, t0_1) 
z1_0 = z1.subs(t, t0_1) 
 
x2_0 = x2.subs(t, t0_2) 
y2_0 = y2.subs(t, t0_2) 
z2_0 = z2.subs(t, t0_2) 
 
# Define the parameter s for the tangent line 
s = sp.symbols('s') 
 
# Parametric equations of the tangent line for each part 
x_tangent1 = x1_0 + s * dx1_dt_val 
y_tangent1 = y1_0 + s * dy1_dt_val 
z_tangent1 = z1_0 + s * dz1_dt_val 
 
x_tangent2 = x2_0 + s * dx2_dt_val 
y_tangent2 = y2_0 + s * dy2_dt_val 
z_tangent2 = z2_0 + s * dz2_dt_val 
 
# Display the parametric equations of the tangent lines 
print(f"Parametric equations of the tangent line at t0 = {t0_1}:") 
print(f"x(s) = {x_tangent1}") 
print(f"y(s) = {y_tangent1}") 
print(f"z(s) = {z_tangent1}") 
 
print(f"Parametric equations of the tangent line at t0 = {t0_2}:") 
print(f"x(s) = {x_tangent2}") 
print(f"y(s) = {y_tangent2}") 
print(f"z(s) = {z_tangent2}") 
 
 
import numpy as np 
 
# Define the normal vectors of the planes 
normal_vector1 = np.array([3, -6, -2]) 
normal_vector2 = np.array([2, 1, -2]) 
 
# Find the cross product of the normal vectors 
parallel_vector = np.cross(normal_vector1, normal_vector2) 
 
print(f"Vector parallel to the line of intersection: {parallel_vector}") 
 
import sympy as sp 
 
# Define the parameter t 
t = sp.symbols('t') 
 
# Define the parametric equations for r(t) 
r_t = sp.Matrix([3*t, sp.sin(t), t**2]) 
 
# Find the velocity as the first derivative of r(t) 
velocity = sp.diff(r_t, t) 
 
# Find the acceleration as the second derivative of r(t) 
acceleration = sp.diff(velocity, t) 
 
print(f"Velocity vector: {velocity}") 
print(f"Acceleration vector: {acceleration}") 
 
# Plot the graph of theta(t) versus t (assuming theta(t) is the angle in the xy-plane) 
import matplotlib.pyplot as plt 
import numpy as np 
 
theta = sp.atan2(velocity[1], velocity[0]) 
theta_func = sp.lambdify(t, theta, 'numpy') 
t_vals = np.linspace(0, 10, 400) 
theta_vals = theta_func(t_vals) 
 
plt.plot(t_vals, theta_vals) 
plt.xlabel('t') 
plt.ylabel('θ(t)') 
plt.title('θ(t) vs t') 
plt.grid(True) 
plt.show()