#Write a Python program to append a new item to the end of the array.


import numpy as np
from array import *

#using numpy
arr = np.array([1, 2, 3, 4, 5])
print('NumPy')
arr = np.append(arr, [6])
for i in range(len(arr)):
    print(arr[i])

#using array
arr1 = array('i', [1, 2, 3, 4, 5])
arr1.append(6)
print('Array')
for i in range(len(arr1)):
    print(arr[i])





