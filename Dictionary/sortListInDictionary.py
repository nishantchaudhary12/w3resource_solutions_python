#Write a Python program to sort a list alphabetically in a dictionary.


user_ip = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}

user_ip = {key: sorted(value) for key, value in user_ip.items()}

print(user_ip)