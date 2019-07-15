#Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output
# (all characters in lower case).


def printLinesLowerCase(line_list):
    for each in line_list:
        print(each.lower())
        

def main():
    line = input('Enter a line ( blank to terminate): ')
    line_list = list()
    while line:
        line_list.append(line)
        line = input('Enter a line ( blank to terminate): ')
    printLinesLowerCase(line_list)



main()