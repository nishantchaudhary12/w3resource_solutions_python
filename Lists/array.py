#Write a Python program to generate a 3*4*6 3D array whose each element is *.


def main():
    arr = [[['*' for col in range(6)] for col in range(4)]for row in range(3)]
    print(arr)


main()