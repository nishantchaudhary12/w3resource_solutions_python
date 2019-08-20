#Write a Python program to remove duplicates from Dictionary.


student_data = {'id1':
   {'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id2':
  {'name': ['David'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id3':
    {'name': ['Sara'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
 'id4':
   {'name': ['Surya'],
    'class': ['V'],
    'subject_integration': ['english, math, science']
   },
}


result_dict = dict()


for each in student_data:
    if student_data[each] not in result_dict.values():
        result_dict[each] = student_data[each]

print(result_dict)