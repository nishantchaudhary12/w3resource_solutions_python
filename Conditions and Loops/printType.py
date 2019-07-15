#Write a Python program that prints each item and its corresponding type from the following list.


def printType(sample_list):
    for each in sample_list:
        print(each, type(each))


def main():
    dataList = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
    printType(dataList)


main()