#Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as its input and
# print the numbers that are divisible by 5 in a comma separated sequence.


def divisibleByFive(sample_data):
    result = list()
    for each in sample_data:
        num = int(each[0]) * (2 ** 3) + int(each[1]) * (2 ** 2) + int(each[2]) * (2 ** 1)  + int(each[3]) * (2 ** 0)
        # print(num)
        if num % 5 == 0:
            result.append(each)
    print(result)


def divisible(sample_data):
    result = list()
    for each in sample_data:
        num = int(each, 2)
        # print(num)
        if num % 5 == 0:
            result.append(each)
    print(result)

sample_data = ['0100', '0011', '1010', '1001', '1100', '1001']
divisibleByFive(sample_data)
divisible(sample_data)
