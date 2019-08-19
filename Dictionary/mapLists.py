# Write a Python program to map two lists into a dictionary.


def map_lists(user_ip_1, user_ip_2):
    my_dict = dict(zip(user_ip_1, user_ip_2))
    return my_dict


def main():
    user_ip_1 = [1, 2, 3]
    user_ip_2 = [10, 20, 30]
    print(map_lists(user_ip_1, user_ip_2))

main()