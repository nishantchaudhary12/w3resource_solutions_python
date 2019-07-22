#Write a Python function to calculate the factorial of a number (a non-negative integer).
# The function accepts the number as an argument.


def factorial(user_ip):
    if user_ip <= 1:
        return 1
    else:
        return user_ip * factorial(user_ip - 1)


def main():
    user_ip = 5
    result = factorial(user_ip)
    print(result)


main()