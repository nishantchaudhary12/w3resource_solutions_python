#Write a Python program to calculate a dog's age in dog's years.
#Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.


def dogAge(age):
    dAge = 0
    if age <= 2:
        dAge *= 10.5
    else:
        age -= 2
        dAge = (10.5 * 2) + (age * 4)
    print(dAge)


dogAge(15)