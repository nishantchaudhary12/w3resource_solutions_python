# Write a Python function that takes a list and returns a new list with unique elements of the first list.


def uniqueList(sample_list):
    new_list = list()
    for each in sample_list:
        if each not in new_list:
            new_list.append(each)
    print(new_list)
    
    return list(set(sample_list))


def main():
    sample_list = [1,2,3,3,3,3,4,5]
    print(uniqueList(sample_list))


main()