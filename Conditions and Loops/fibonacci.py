# Write a Python program to get the Fibonacci series between 0 to 50.


def fibonacci(num):
    a = 0
    b = 1
    while b < num:
        print(b)
        a, b = b, a + b


def main():
    num = 50
    fibonacci(num)


main()