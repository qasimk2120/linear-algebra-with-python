import numpy as np

# Create two 2D arrays (matrices) of the same shape
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])

# Element-wise addition using the + operator
print(x + y)  # adds corresponding elements

# Element-wise addition using NumPy function
z = np.add(x, y)
print(z)

# Element-wise subtraction using - operator
d = x - y
print(d)

# Element-wise subtraction using NumPy function
e = np.subtract(x, y)
print(e)

# Element-wise multiplication using * operator (NOT matrix multiplication)
f = x * y
print(f)

# Element-wise multiplication using NumPy function
g = np.multiply(x, y)
print(g)

# Element-wise division using / operator
h = x / y
print(h)

# Element-wise division using NumPy function
i = np.divide(x, y)
print(i)

# Square root of each element in x
j = np.sqrt(x)
print(j)

# Create two 1D arrays for dot product
v = np.array([9, 10])
w = np.array([11, 13])

# Dot product of 1D arrays (vector dot product)
print(v.dot(w))      # method form
print(np.dot(v, w))  # function form

# Dot product (matrix multiplication) of two 2D arrays
# Result is a 2x2 matrix: x @ y
print(np.dot(x, y))

# Transpose of matrix x (swap rows and columns)
print(x.T)

# Sum of all elements in x
print(np.sum(x))

# Sum along axis=0 (column-wise sum) -> returns 1D array of column totals
print(np.sum(x, axis=0))

# Sum along axis=1 (row-wise sum) -> returns 1D array of row totals
print(np.sum(x, axis=1))
