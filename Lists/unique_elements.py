# Write a Python program to get unique values from a list.


def unique(list_inp):
    unique_list = list()
    for each in list_inp:
        if each not in unique_list:
            unique_list.append(each)
    return unique_list



def main():
    list_inp = [3, 6, 4, 7, 12, 15, 10, 3, 10, 4]
    print('List of all the unique elements in the list:', unique(list_inp))


main()


'''
#using sets

list_inp = [3, 6, 4, 7, 12, 15, 10, 3, 10, 4]
print(set(list_inp))

'''

