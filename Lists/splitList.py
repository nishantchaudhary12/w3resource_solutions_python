# Write a Python program to split a list based on first character of word.


def splitList(usr_inp):
    split_dict = dict()
    for each in usr_inp:
        if each[0] in split_dict:
            split_dict[each[0]].append(each)
        else:
            split_dict[each[0]] = [each]
    print(sorted(split_dict.items()))


def main():
    usr_inp = ['be', 'have', 'do', 'say', 'get', 'make', 'go', 'know', 'take', 'see', 'come', 'think',
     'look', 'want', 'give', 'use', 'find', 'tell', 'ask', 'work', 'seem', 'feel', 'leave', 'call']
    splitList(usr_inp)


main()