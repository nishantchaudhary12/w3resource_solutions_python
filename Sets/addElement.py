#Write a Python program to add member(s) in a set.


def main():
    x = set([1, 2, 3, 4, 5])
    x.add(6)
    x.update([7, 8])
    print(x)


main()