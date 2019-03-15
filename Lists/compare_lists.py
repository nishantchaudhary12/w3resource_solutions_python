# Write a Python function that takes two lists and returns True if they have at least one common member.


def compare(list1, list2):
    for elem1 in list1:
        for elem2 in list2:
            if elem1 == elem2:
                return True
            else:
                continue
    print('No matches found')

def main():
    list1 = [1,3,5,6,3,8]
    list2 = [3,5,1,7,2]
    print(compare(list1, list2))


main()