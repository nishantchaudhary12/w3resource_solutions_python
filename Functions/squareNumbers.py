# Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included).


def square_numbers():
    my_list = list()
    for each in range(1, 31):
        my_list.append(each * each)
    print(my_list)


def main():
    square_numbers()


main()