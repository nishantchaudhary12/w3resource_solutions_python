#Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number.
# The numbers obtained should be printed in a comma-separated sequence.


result = list()
for num in range(100,401):
    flag = True
    curr = num
    while num > 0:
        rem = num % 10
        if rem % 2:
            flag = False
            break
        num = num // 10
    if flag:
        result.append(curr)

print(result)