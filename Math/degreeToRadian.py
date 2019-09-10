#Write a Python program to convert degree to radian.


def convert(degree):
    radian = degree*(22/(7*180))
    return radian

print(convert(15))