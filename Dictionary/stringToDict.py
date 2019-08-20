#Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.


from collections import Counter


sampleString = 'w3resource'

result = Counter(sampleString)

print(result)