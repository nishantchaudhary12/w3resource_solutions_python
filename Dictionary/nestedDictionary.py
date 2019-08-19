#Write a Python program to convert a list into a nested dictionary of keys.


sampleData = [1, 2, 3, 4, 5]

result = dict()
curr = result
for i in sampleData:
    curr[i] = {}
    curr = curr[i]

print(result)

