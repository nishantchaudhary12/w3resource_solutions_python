# Write a Python program to generate and print a list of first
# and last 5 elements where the values are square of numbers between 1 and 30 (both included).


def square():
    square_list = list()
    for num in range(1,31):
        num = num ** 2
        square_list.append(num)
    print(square_list[:5])
    print(square_list[-5:])

def main():
    square()


main()