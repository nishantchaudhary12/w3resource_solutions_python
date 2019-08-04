#Write a Python program to find the median of three values.


def median(x, y, z):
    if x > y:
        if x > z:
            if y > z:
                return y
            else:
                return z
        else:
            return x
    else:
        if y > z:
            if x > z:
                return x
            else:
                return z
        else:
            return y


print(median(25, 18, 22))