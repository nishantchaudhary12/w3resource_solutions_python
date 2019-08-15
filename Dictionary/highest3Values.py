#Write a Python program to find the highest 3 values in a dictionary.

#getting values
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
values = set(my_dict.values())
count = 3      #number of highest values
curr = 0
result = set()
while curr < count:
    max_elem = max(values)
    result.add(max_elem)
    values.remove(max_elem)
    curr += 1

print(result)


#getting keys (non-repetitive)
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
count = 3
curr = 0
result = dict()
while curr < count:
    max_elem = max(my_dict.items(), key=lambda x:x[1])
    if max_elem[1] not in result.values():
        result[max_elem[0]] = max_elem[1]
        curr += 1
    del my_dict[max_elem[0]]

print(result.keys())


#getting keys (repetitive)
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
count = 3
curr = 0
result = dict()
while curr < count:
    max_elem = max(my_dict.items(), key=lambda x:x[1])
    result[max_elem[0]] = max_elem[1]
    curr += 1
    del my_dict[max_elem[0]]

print(result.keys())

