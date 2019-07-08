#Write a Python program to count the elements in a list until an element is a tuple.


def countElements(tup):
    count = 0
    for each in tup:
        if isinstance(each, tuple):
            break
        count += 1
    print(count)


def main():
    tup =  [1, 2, 3,(1, 2, 3),4]
    countElements(tup)


main()