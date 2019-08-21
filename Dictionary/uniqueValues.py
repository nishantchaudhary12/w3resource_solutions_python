#Write a Python program to print all unique values in a dictionary.


data = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

result = set(value for each in data for value in each.values())

print(result)