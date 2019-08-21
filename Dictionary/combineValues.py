# Write a Python program to combine values in python list of dictionaries.

from collections import Counter


def combineValues(user_ip):
    result = dict()
    for each in user_ip:
        if each['item'] not in result:
            result[each['item']] = each['amount']
        else:
            result[each['item']] += each['amount']
    return result


def combine(user_ip):     #using counter
    result = Counter()
    for each in user_ip:
        result[each['item']] += each['amount']
    return result


user_ip =  [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
print(combineValues(user_ip))
print(combine(user_ip))