#Write a Python program to reverse the order of the items in the array.


import numpy as np
from array import *

#using numpy
arr = np.array([1, 2, 3, 4, 5])
print('NumPy')
new_arr = np.array([])
for i in range(len(arr)-1, -1, -1):
    new_arr = np.append(new_arr, arr[i])
print(new_arr)

#using array
arr1 = array('i', [1, 2, 3, 4, 5])
print('Array')
new_arr1 = array('i', [])
for i in range(len(arr1)-1, -1, -1):
    new_arr1.append(arr1[i])
print(new_arr1)

'''#or we can use reversesd function
print(list(reversed(arr)))
'''






