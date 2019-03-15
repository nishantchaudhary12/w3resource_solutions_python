#Write a Python program to get a list, sorted in increasing order by the last element in each tuple
#  from a given list of non-empty tuples.


def sort_list(list_inp):
    for index_element in range(len(list_inp)-1):
        current_min = list_inp[index_element][-1]
        min = current_min
        temp1 = list_inp[index_element]
        for num in range(index_element+1, len(list_inp)):
            cmp = list_inp[num][-1]
            if cmp < current_min:
                current_min = cmp
                index_min = num
        temp2 = list_inp[index_min]
        if current_min != min:
            list_inp[index_element] = temp2
            list_inp[index_min] = temp1
    return list_inp



def main():
    list_inp = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    print(sort_list(list_inp))


main()

'''

#using sorted function

def last(element):
    return element[-1]


def sort_list(list_inp):
    return sorted(list_inp, key=last)


def main():
    list_inp = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    print(sort_list(list_inp))


main()

'''

