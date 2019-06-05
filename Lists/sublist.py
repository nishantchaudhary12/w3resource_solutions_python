#Write a Python program to check whether a list contains a sublist.


def contains_sublist(super_list, sub_list):
    current = 0
    flag = False
    if sub_list == []:
        flag = True
    else:
        for each in range(len(super_list)):
            if super_list[each] == sub_list[0]:
                current = 1
                while (current + each) < len(super_list) and current < len(sub_list):
                    if super_list[each + current] == sub_list[current]:
                        current += 1
                    else:
                        break
                if len(sub_list) == current:
                    flag = True
                    break

    return flag


def main():
    super_list = [1, 4, 6, 7]
    sub_list = [1, 4, 7]
    print(contains_sublist(super_list, sub_list))


main()