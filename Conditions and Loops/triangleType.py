#Write a Python program to check a triangle is equilateral, isosceles or scalene.


def traingleType(x, y, z):
    if x == y == z:
        return 'Equilateral'
    elif x == y or y == z or x == z:
        return 'Isoseles'
    else:
        return 'Scalene'


print(traingleType(6, 8, 12))