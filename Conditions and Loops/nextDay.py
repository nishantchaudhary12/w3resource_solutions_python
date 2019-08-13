#Write a Python program to get next day of a given date.


def leapYear(year):
    if year % 400 == 0:
        leap_year = True
    elif year % 100 == 0:
        leap_year = False
    elif year % 4 == 0:
        leap_year = True
    else:
        leap_year = False
    return leap_year


def nextDate(year, month, day):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day != 31:
            day += 1
        else:
            day = 1
            if month != 12:
                month += 1
            else:
                month = 1
                year += 1
    elif month in [4, 6, 9, 11]:
        if day != 30:
            day += 1
        else:
            day = 1
            if month != 12:
                month += 1
            else:
                month = 1
                year += 1
    else:
        if leapYear(year):
            if day != 29:
                day += 1
            else:
                day = 1
                month = 3

    nextDay = str(year) + '-' + str(month) + '-' + str(day)
    return nextDay


print(nextDate(2016, 8, 23))