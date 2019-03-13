#Write a Python program to get the largest number from a list.


def largest(inp_list):
    large = inp_list[0]
    for item in inp_list:
        if large < item:
            large = item
    return large


def main():
    inp_list = [10,12,43,44,87,60,17,8,19,10]
    print('The largest number of all the elements of the list is:',largest(inp_list))


main()
