# Name: Roshan Yadav
# Roll No: 2311144
# Assignment: Finding Roots for Multivariable function

from Func_for_Assgn_8 import *

# System of equations:
# x1^2 + x2 = 37
# x1 - x2^2 = 5  
# x1 + x2 + x3 = 3

G = [6, 1, -4]   # Initial Guess

# Fixed point functions g(x)| x = g(x)
def g(X, t):
    if t == 0:  # x1 = (37 - x2)^0.5
        return (37 - X[1])**0.5
    if t == 1:  # x2 = (x1 - 5)^0.5
        return (X[0] - 5)**0.5
    if t == 2:  # x3 = 3 - x1 - x2
        return 3 - (X[0] + X[1])

# Function definitions f(x) = 0
def f(X, t):
    if t == 0:  # f1 := x1^2 + x2 - 37 = 0
        return X[0]**2 + X[1] - 37
    if t == 1:  # f2 := x1 - x2^2 - 5 = 0
        return X[0] - X[1]**2 - 5
    if t == 2:  # f3 := x1 + x2 + x3 - 3 = 0
        return X[0] + X[1] + X[2] - 3

# Jacobian matrix for Newton-Raphson
# J[i][j] = ∂fi/∂xj
def jacobian(X):
    J = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    J[0][0] = 2 * X[0]
    J[0][1] = 1
    J[0][2] = 0
    J[1][0] = 1
    J[1][1] = -2 * X[1]
    J[1][2] = 0
    J[2][0] = 1
    J[2][1] = 1
    J[2][2] = 1
    
    return J


# Fixed Point Method
R, i = fixed_point(G, g)
print(f"Results by Fixed point method in {i} iterations: {R}") #Output:Results by Fixed point method in 1 iterations: [6.0, 1.0, -4]


# Newton-Raphson Method
J = jacobian(G)
R2, i2 = Newton_Raphson(G, jacobian, f)
print(f"\nResults by Newton Raphson method in {i2} iterations: {R2}") #Output: Results by Fixed point method in 1 iterations: [6.0, 1.0, -4]

