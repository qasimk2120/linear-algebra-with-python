import numpy as np

# Create a 1D NumPy array
arr = np.array([1, 2, 3])

print("Array:", arr)  # prints the array contents
print(type(arr))      # shows the object type -> <class 'numpy.ndarray'>
print(arr.shape)      # shape of 1D array -> (3,)

# Create a 2D NumPy array (matrix). NumPy arrays enforce a single dtype.
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Array:\n", arr)  # prints matrix in 2 rows

print(arr[0, 1])  # element at row 0, column 1 -> 2

print(arr.shape)  # shape of 2D array -> (2, 3)
print(arr.size)   # total number of elements -> 6
print(arr.ndim)   # number of dimensions -> 2

# Re-create the same 2D array again
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print(arr.ndim)   # still 2 dimensions

print(arr.data)   # low-level buffer object (memory view of the array)

# Append 99 to the first row ONLY and return a new array (does NOT modify original 'arr')
print(np.append(arr[0], 99))

# Here you overwrite 'arr' with the appended version of arr[0]
# IMPORTANT: arr is no longer 2D after this; it becomes 1D -> [1 2 3 99]
arr = np.append(arr[0], 99)
print(arr)

# Delete element at index 1 (the value 2) and return a new array
print(np.delete(arr, 1))

# Overwrite arr with the deleted version
arr = np.delete(arr, 1)  # arr becomes [1 3 99]
print(arr)
