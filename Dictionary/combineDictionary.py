#Write a Python program to combine two dictionary adding values for common keys.


d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}


for each in d2:           #can also be solved by using Counter from Collections
    if each in d1:
        d1[each] += d2[each]
    else:
        d1[each] = d2[each]


print(d1)