#Write a Python program to reverse a string.


def reverse_string(user_ip):
    result = ''.join(list((reversed(user_ip))))
    print(result)

    result_str = ''
    for num in range(len(user_ip)-1, -1, -1):
        result_str += user_ip[num]
    print(result_str)

    r_str = ''
    indx = len(user_ip)
    while indx > 0:
        r_str += user_ip[indx - 1]
        indx -= 1
    print(r_str)




def main():
    user_ip = 'w3resourse'
    reverse_string(user_ip)


main()