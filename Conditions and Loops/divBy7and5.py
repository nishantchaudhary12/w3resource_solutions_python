#Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).


def main():
    for each in range(1500, 2701):
        if each % 7 == 0:
            if each % 5 == 0:
                print(each)


main()