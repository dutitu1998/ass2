import sympy as sp

# Define the normal vectors
n1 = sp.Matrix([3, -6, -2])
n2 = sp.Matrix([2, 1, -2])

# Compute the cross product
direction_vector = n1.cross(n2)

print("Vector parallel to the line of intersection:")
print(direction_vector)