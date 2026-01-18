import numpy as np

# Create a 2x3 array filled with zeros (integers)
x = np.zeros((2, 3), dtype=int)
# print(x)  # uncomment to display

# Create a 4x5 array filled with ones (floats)
y = np.ones((4, 5), dtype=float)
# print(y)  # uncomment to display

# Create a 3D array of shape (4, 5, 3) filled with ones (integers)
# Means: 4 blocks, each block is 5 rows x 3 columns
z = np.ones((4, 5, 3), dtype=int)
print(z)

# Create a 1D array from 0 up to 9
a = np.arange(10)
print(a)

# Create a 1D array from 5 up to 14
b = np.arange(5, 15)
print(b)

# Create a 1D array from 2 up to <20, stepping by 3
c = np.arange(2, 20, 3)
print(c)

# Create a float array from 2 up to <3 with step of 0.1
# Note: floating-point precision may create slight rounding artifacts
d = np.arange(2, 3, 0.1)
print(d)

# Create 6 evenly spaced numbers between 1.0 and 4.0 (inclusive)
e = np.linspace(1.0, 4.0, 6)
print(e)

# Create a 2x2 array filled with the value 8
f = np.full((2, 2), 8)
print(f)

# Create a 5x5 identity matrix (1s on diagonal, 0s elsewhere)
g = np.eye(5)
print(g)

# Create a 4x5 array with random floats in range [0.0, 1.0)
h = np.random.random((4, 5))
print(h)

random_arr =  np.random.rand(5) #Uniform distribution between 0 and 1 
print(random_arr)


random_Int = np.random.randint(1, 10, size=(5)) #Random integers between 1 and 10  (low, high), size]
print(random_Int)