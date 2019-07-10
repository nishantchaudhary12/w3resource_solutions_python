#Write a Python function to check whether a number is in a given range


def rangeCheck(low, high, num):
    result = False
    if num in range(low, high+1):
        result = True
    return result


def main():
    range_low = 1
    range_high = 10
    num = 5
    print(rangeCheck(range_low, range_high, num))


main()