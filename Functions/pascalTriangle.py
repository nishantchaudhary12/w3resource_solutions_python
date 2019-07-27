# Write a Python function that prints out the first n rows of Pascal's triangle.


def pascal_triangle(num):
    if num == 1:
        my_list = [[1]]
    elif num == 2:
        my_list = [[1], [1, 1]]
    else:
        my_list = [[1], [1, 1]]
    for each in range(2, num):
        my_list.append([1])
        for num in range(1, each):
            my_list[each].append(my_list[each - 1][num - 1] + my_list[each - 1][num])
        my_list[each].append(1)
        # print(my_list)
    print(my_list)


def main():
    num = 6
    pascal_triangle(num)
    pascal_tri(6)

main()