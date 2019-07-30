#Write a Python program to find the repeated items of a tuple.

from collections import Counter


def main():
    x = ('w', '3', 'r', 'e', 's', 'o', 'u', 'r', 'c', 'e')
    x_counter = Counter(x)
    for each in x_counter:
        if x_counter[each] > 1:
            print(each)
            

main()