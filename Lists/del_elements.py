# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.


def del_elements(list_inp):
    del list_inp[0]
    del list_inp[3]      #after deletion of element at 0 the index will be reduced by 1 so i.e. 3 instead of 4
    del list_inp[3]      #after deletion of element at 0 and 4 the index will be reduced by 2 so i.e. 3 instead of 5
    return list_inp


def main():
    list_inp = [1,3,5,6,3,8,10]
    print(del_elements(list_inp))


main()

'''
#using list comprehension

def main():
    list_inp = [1,3,5,6,3,8,10]
    res = [list_inp[i] for i in range(len(list_inp)) if i not in [0,4,5]]
    print(res)
    

main()

'''