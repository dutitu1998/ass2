import numpy as np
import sympy as sp
t = sp.symbols('t') 

# First curve
print('For the first curve, the parametric equation:')
t1 = 2
x1, y1, z1 = np.log(t1), np.exp(-t1), t1**3
dx1 = sp.diff(x1, t) 
dy1 = sp.diff(y1, t) 
dz1 = sp.diff(z1, t) 
dx1_ = dx1.subs(t, t1) 
dy1_ = dy1.subs(t, t1) 
dz1_ = dz1.subs(t, t1) 

print(f'x = {x1} + {dx1_} * t')
print(f'y = {y1} + {dy1_} * t')
print(f'z = {z1} + {dz1_} * t')