# Write a Python program to get the maximum and minimum value in a dictionary.


def min_and_max(user_ip):
    max_val = max(user_ip.items(), key=lambda x: x[1])
    min_val = min(user_ip.items(), key=lambda x: x[1])
    return max_val, min_val


def main():
    user_ip = {1: 10, 2: 20, 4: 30, 5: 5, 7: 20, 6: 25}
    max_val, min_val = min_and_max(user_ip)
    print('Max value:', max_val, 'Min value:', min_val)


main()