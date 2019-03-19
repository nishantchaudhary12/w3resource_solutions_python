# Write a Python program to count the number of elements in a list within a specified range.


def frequency(list_inp, range_low, range_high):
    freq_dict = {}
    list_inp = [i for i in list_inp if i >= range_low and i <= range_high]
    for each in list_inp:
        if each in freq_dict.keys():
            freq_dict[each] += 1
        else:
            freq_dict[each] = 1
    print('Values\tCount')
    for num in freq_dict:
        print(num, '\t\t', freq_dict[num])
    print('Total elements within this range', sum(freq_dict.values()))


def main():
    list_inp = [1, 4, 6, 4, 4, 2, 8, 9, 3, 8, 2, 5, 2]
    range_low = 2
    range_high = 9
    frequency(list_inp, range_low, range_high)


main()
