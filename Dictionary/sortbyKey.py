# Write a Python program to sort a dictionary by key


def sort_dict(user_ip):
    my_dict = dict(sorted(user_ip.items(), key=lambda x: x[0]))
    return my_dict


def main():
    user_ip = {1: 10, 2: 20, 4: 30, 5: 10, 7: 20, 6: 25}
    print(sort_dict(user_ip))


main()