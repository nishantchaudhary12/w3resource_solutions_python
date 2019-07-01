# Write a Python program to multiply all the items in a dictionary.


def multiply_dict(user_ip):
    mult = 1
    for each in user_ip:
        mult *= user_ip[each]
    return mult


def main():
    user_ip = {1: 20, 2: 30, 3: 90}
    print(multiply_dict(user_ip))

main()