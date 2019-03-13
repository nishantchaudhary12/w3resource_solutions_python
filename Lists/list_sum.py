#Write a Python program to sum all the items in a list.


def sum_list(inp_list):
    sum = 0
    for item in inp_list:
        sum += item
    return sum


def main():
    inp_list = [1,2,3,4,5,6,7,8,9,10]
    print('The sum of all the elements of the list is:',sum_list(inp_list))


main()
