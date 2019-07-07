#Write a Python program to convert temperatures to and from celsius, fahrenheit.


def cel_to_fer(c):
    f = (c * 9 / 5) + 32
    print('Farenheit:', format(f, '.2f'))


def fer_to_cel(f):
    c = (f - 32) * 5 / 9
    print('Celcius:', format(c, '.2f'))


def main():
    temp1 = 60
    temp2 = 45
    cel_to_fer(temp1)
    fer_to_cel(temp2)


main()