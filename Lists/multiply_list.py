#Write a Python program to multiplies all the items in a list.


def mul_list(inp_list):
    mul_result = 1
    for item in inp_list:
        mul_result *= item
    return mul_result


def main():
    inp_list = [1,2,3,4,5,6,7,8,9,10]
    print('The result of the multiplication of all the elements of the list is:',mul_list(inp_list))


main()
