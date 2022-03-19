#1) Create a 1D array of numbers from 0 to 9 called arr.. Desired output: #> array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr)

#2)From arr, extract all odd numbers
oddnum = arr[arr % 2 == 1]
print(oddnum)

# 3.) Replace all even numbers in arr with -1.
evennum = arr[arr % 2 == 0]
arr[evennum] = -1
print(arr)

#4.) Convert the following 1D array to a 2D array with 2 rows. Input: np.arange(10)
#> array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# Desired Output:
# array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
reshaped_arr = np.reshape(arr,(2,5))
print(reshaped_arr)

# 5.) Create a single dimension array, array_1d, of size n containing integers 0 to n-1. Reshape the array. The reshaped array, array_reshaped, should be n/3 columns and 3 rows.
n = 9
array_1d = np.arange(n)
print(array_1d)
array_reshaped = np.reshape(array_1d, (3, int(n/3)))
print (array_reshaped)

# 6.) Create a numpy identity matrix of size n.
identity_matrix = np.identity(10)
print(identity_matrix)

# 7.) Create an array filled with zeroes of size n x n (n rows, n columns).
n = 10 
zero_matrix = np.zeros((n,n))
print(zero_matrix)
