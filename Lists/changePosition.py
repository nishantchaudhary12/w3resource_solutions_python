# Write a Python program to change the position of every n-th value with the (n+1)th in a list.


def change_position(sample_list):
    for each in range(0, len(sample_list) - 1, 2):
        temp = sample_list[each]
        sample_list[each] = sample_list[each + 1]
        sample_list[each + 1] = temp
    return sample_list


def main():
    sample_list = [0, 1, 2, 3, 4, 5]
    print(change_position(sample_list))


main()