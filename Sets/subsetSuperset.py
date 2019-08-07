#Write a Python program to issubset and issuperset.


set1 = {1,2,3,4}
set2 = {3,4}

print(set1 >= set2)   #superset
print(set2 <= set1)   #subset

print(set2.issubset(set1))
print(set1.issuperset(set2))
