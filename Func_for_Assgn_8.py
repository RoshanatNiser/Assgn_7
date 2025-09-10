# Name: Roshan Yadav
# Roll No: 2311144
# Assignment: Finding Roots for Multivariable function

import math, copy

class matrix():
    def __init__(self, data=None):
        self.m = len(data)
        self.n = len(data[0])
        self.data = data
    
    def display(self):
        for row in self.data:
            print([f"{x:.6f}" for x in row])
        return None
    
    def row_swap(self, u=None, p=None):
        self.data[u], self.data[p] = self.data[p], self.data[u]
    
    def con_mul(self, c=0, p=0):
        '''This function does the 
        constant 'c' multiplication 
        to a row no 'p'.'''
        for i in range(len(self.data[p])):
            self.data[p][i] = float(c) * float(self.data[p][i])
    
    def row_ops(self, f=None, r=None, c=None):
        '''This function does the following row operation:
        Row[f] ->Row[f] + c*Row[r]'''
        for i in range(len(self.data[f])):
            self.data[f][i] = float(self.data[f][i]) + float(c) * float(self.data[r][i])
    
    def aug(self, b=None):
        A = copy.deepcopy(self.data)
        # Handle both 1D and 2D b vectors
        for i in range(len(A)):
            if isinstance(b[0], list):
                A[i].append(b[i][0])  # b is 2D, take first element
            else:
                A[i].append(b[i])     # b is 1D
        return A
    
    def gauss_jorden(self, b=None):
        if b is None:
            # Create identity matrix for finding inverse
            b = [[0.0] * self.m for _ in range(self.m)]
            for i in range(self.m):
                b[i][i] = 1.0
        
        # Create augmented matrix
        A_data = []
        for i in range(self.m):
            row = self.data[i][:] + b[i][:]  # Copy original row and append b row
            A_data.append(row)
        
        A = matrix(A_data)
        m = self.m
        n = self.n
        
        # Forward elimination with partial pivoting
        for i in range(min(m, n)):
            # Find pivot (largest element in column i from row i onwards)
            max_row = i
            for k in range(i + 1, m):
                if abs(A.data[k][i]) > abs(A.data[max_row][i]):
                    max_row = k
            
            # Swap rows if needed
            if max_row != i:
                A.row_swap(i, max_row)
            
            # Check if pivot is zero
            if abs(A.data[i][i]) < 1e-10:
                print(f"Matrix is singular at column {i}")
                return None, None
            
            # Make diagonal element 1
            pivot = A.data[i][i]
            A.con_mul(c=1.0/pivot, p=i)
            
            # Make elements below pivot zero
            for j in range(i + 1, m):
                if abs(A.data[j][i]) > 1e-10:
                    multiplier = -A.data[j][i]
                    A.row_ops(j, i, multiplier)
        
        # Back substitution (Jordan part)
        for i in range(min(m, n)-1, -1, -1):
            for j in range(i):
                if abs(A.data[j][i]) > 1e-10:
                    multiplier = -A.data[j][i]
                    A.row_ops(j, i, multiplier)
        
        # Extract inverse matrix 
        I = []
        for i in range(m):
            row = []
            for j in range(n, n + m):
                row.append(A.data[i][j])
            I.append(row)
        
        return I  


def fixed_point(X, g, e=10**-6, max_iter=100):
    """This function finds the roots of multivariable function 
    using Fixed point method"""
    
    for i in range(max_iter):
        Y = [0.0 for _ in range(len(X))]
        
        for j in range(len(X)):
            Y[j] = g(X, j)  # Iteration Step
        
        # Calculating relative error
        norm_diff = ((Y[0] - X[0])**2 + (Y[1] - X[1])**2 + (Y[2] - X[2])**2)**0.5
        norm_Y = (Y[0]**2 + Y[1]**2 + Y[2]**2)**0.5
        
        
        if norm_diff / norm_Y < e:
            return Y, i + 1
        
        X = Y[:]  # Copy Y to X for next iteration
    
    return X, max_iter


def Newton_Raphson(X, J_func, f, e=10**-6, max_iter=100):
    """This function finds the roots of multivariable function 
    using Newton-Raphson method"""
    
    for i in range(max_iter):
        # Jacobian Matrix
        J_matrix = J_func(X)
        
        # Inverse of Jacobian
        J = matrix(J_matrix)
        J_inv = J.gauss_jorden()
        
        # Calculate function values
        F = [f(X, k) for k in range(len(X))]
        
        # Newton-Raphson update: X_new = X - J^(-1) * F(X)
        Y = [0.0 for _ in range(len(X))]
        for j in range(len(X)):
            Total = 0
            for k in range(len(X)):
                Total = Total + J_inv[j][k] * F[k]
            Y[j] = X[j] - Total
        
        # Calculate relative error
        norm_diff = sum((Y[j] - X[j])**2 for j in range(len(X)))**0.5
        norm_Y = sum(Y[j]**2 for j in range(len(X)))**0.5
        
        
        if norm_diff / norm_Y < e:
            return Y, i + 1
        
        X = Y[:]  
    return X, max_iter