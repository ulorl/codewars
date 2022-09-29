import numpy as np

def matrix_mult(a, b):
    return np.array(a).dot(np.array(b)).tolist()

a = [ [1, 2], [3, 2] ]
b = [ [3, 2], [1, 1] ]
print(matrix_mult(a, b))