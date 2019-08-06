#Write a Python program to access a function inside a function.


def func(var):
    def add(var1):
        nonlocal var
        return var + var1
    return add

result = func(5)
print(result(5))