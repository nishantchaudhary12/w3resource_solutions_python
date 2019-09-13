#Write a Python program to calculate the area of a trapezoid.


def areaTrapezoid(height, base_1, base_2):
    area = (base_1 + base_2)/2 * height
    print(area)


height = 5
base_1 = 5
base_2 = 6
areaTrapezoid(height, base_1, base_2)