#Write a Python program to add a key to a dictionary.


if __name__ == '__main__':
    usr_inp = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    usr_inp.update({5:10})
    print(usr_inp)