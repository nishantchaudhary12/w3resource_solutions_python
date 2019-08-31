#Write a Python program to create an array of 5 integers and display the array items.
# Access individual element through indexes.


import numpy as np
from array import *

#using numpy
arr = np.array([1, 2, 3, 4, 5])
print('NumPy')
for i in range(len(arr)):
    print(arr[i])

#using array
arr1 = array('i', [1, 2, 3, 4, 5])
print('Array')
for i in range(len(arr1)):
    print(arr[i])



