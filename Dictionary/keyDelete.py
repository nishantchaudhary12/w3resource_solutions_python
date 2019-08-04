#Write a Python program to remove a key from a dictionary.


def delete_key(user_ip, key):
    if key in user_ip:
        del user_ip[key]
    else:
        print('Key does not exist')
    return user_ip


def main():
    user_ip = {1: 20, 2: 30, 3: 90}
    key = 3
    print(delete_key(user_ip, key))

main()