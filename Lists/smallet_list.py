#Write a Python program to get the smallest number from a list.


def smallest(inp_list):
    small = inp_list[0]
    for item in inp_list:
        if small > item:
            small = item
    return small


def main():
    inp_list = [10,12,43,44,87,60,17,8,19,10]
    print('The smallest number of all the elements of the list is:',smallest(inp_list))


main()
