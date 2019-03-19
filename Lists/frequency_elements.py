# Write a Python program to get the frequency of the elements in a list.

#using dictionary

def frequency(list_inp):
    freq_dict = {}
    for each in list_inp:
        if each in freq_dict.keys():
            freq_dict[each] += 1
        else:
            freq_dict[each] = 1
    print('Values\tCount')
    for num in freq_dict:
        print(num, '\t\t', freq_dict[num])


def main():
    list_inp = [1, 4, 6, 4, 4, 2, 8, 9, 3, 8, 2, 5, 2]
    frequency(list_inp)


main()
'''

#using collections

import collections


list_inp = [1, 4, 6, 4, 4, 2, 8, 9, 3, 8, 2, 5, 2]
count = collections.Counter(list_inp)
print('Frequency: \n',count)

'''