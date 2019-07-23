# Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.


def makeArray(i, j):
    arr = [[0 for each in range(j)]for each in range(i)]
    for r in range(i):
        for c in range(j):
            arr[r][c] = r * c
    print(arr)


def main():
    i = 3
    j = 3
    makeArray(i, j)


main()