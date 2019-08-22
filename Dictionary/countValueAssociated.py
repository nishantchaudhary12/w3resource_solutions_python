#Write a Python program to count the values associated with key in a dictionary.


sampleData = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'},
              {'id': 3, 'success': True, 'name': 'Alex'}]

count = 0
for each in sampleData:
    if each['success'] == True:
        count += 1

print(count)

#using sum

print(sum(each['success'] for each in sampleData))