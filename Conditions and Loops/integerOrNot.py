#Write a Python program to check a string represent an integer or not


def intOrNot(data):
    # if data.isdigit():
    #     print("Integer")
    # else:
    #     print("Not an integer")
    if all(data[i] in "0123456789" for i in range(len(data))):
        print("Integer")
    elif data[0] in "+-" and all(data[i] in "0123456789" for i in range(1, len(data))):
        print("Integer")
    else:
        print("Not an integer")


intOrNot('Python')