#Write a Python program to sort a tuple by its float element.


def sortTuple(tup):
    new_tup = list(sorted(tup, key=lambda x: x[1], reverse=True))
    print(new_tup)


def main():
    tup = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
    sortTuple(tup)
    

main()