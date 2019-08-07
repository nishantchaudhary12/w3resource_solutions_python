#Write a Python program to create a symmetric difference.


set1 = {1,2,3,4}
set2 = {3,4,5,6}

set3 = set1 ^ set2
set4 = set1.symmetric_difference(set2)

print(set3)
print(set4)