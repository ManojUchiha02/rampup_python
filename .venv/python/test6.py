"""1. Write a function which takes dictionary as an argument, if the value of particular key is empty, delete the key and value
and return the dictionary
---> use the dictionary comprehension if possible
---> eg dict = {'k': ['abc', 'cab', 'dog'], 'k2': [], 'k3':['sss', 'www', 'rrr'], 'k4':['qqq','aaa', 'eee'], 'k5':[]}
---> expected Output: {'k': ['abc', 'cab', 'dog'], 'k3':['sss', 'www', 'rrr'], 'k4':['qqq','aaa', 'eee'] }
---> return the dictionary"""
def clean_dict(d):
    return {k: v for k, v in d.items() if v}

dict_input = {'k': ['abc', 'cab', 'dog'], 'k2': [], 'k3': ['sss', 'www', 'rrr'], 'k4': ['qqq', 'aaa', 'eee'], 'k5': []}
print("Cleaned dictionary:", clean_dict(dict_input))

"""2. dict_1= {'A1':1, 'B1':2,'C1':3, D1:4}, dict_2= {'M':6,'N':7,'o':8,'p':9}

Note: Should use dictionary comprehension for Q1 and list comprehension for Q2 & Q3

Q1 add dict_1 & dict_2 and store them in a new dictionary.

Q2 take out values from both the dictionary above and store them in a list.

Q3 take out keys from both the dictionary above and store them in a list.
dict_1 = {'A1': 1, 'B1': 2, 'C1': 3, 'D1': 4}
dict_2 = {'M': 6, 'N': 7, 'O': 8, 'P': 9}"""

combined_dict = {**dict_1, **dict_2}
print("Combined dictionary:", combined_dict)

values_list = [v for d in (dict_1, dict_2) for v in d.values()]
print("Values list:", values_list)

keys_list = [k for d in (dict_1, dict_2) for k in d.keys()]
print("Keys list:", keys_list)

"""Reverse the string below?
Write a function that takes string as an argument and returns reversed string
—> Do Not use builtin functions
—> functions should be reusable

Eg: string= "Juniper Automation"""""
def reverse_string(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s

print("Reversed string:", reverse_string("Juniper Automation"))

"""Write a function, which takes tuple as argument, and return the 2 lists [ str list and integer list] for each type
---> eg: (123, 'abc', 'def', 345, 'sss', 999)
---> required output:
intlist: [123, 345, 999]
strlist: ['abc', 'def', 'sss']
---> validate the type and insert the record into each list"""
def separate_elements(input_tuple):
    int_list = []
    str_list = []
    for item in input_tuple:
        if isinstance(item, int):
            int_list.append(item)
        elif isinstance(item, str):
            str_list.append(item)
    return int_list, str_list

input_tuple = (123, 'abc', 'def', 345, 'sss', 999)
intlist, strlist = separate_elements(input_tuple)
print("Integer list:", intlist)
print("String list:", strlist)

"""Write an example of Exception method. where you are divding the a number with zero and error is poppingup.
Use (Try and except method)"""
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Error:", e)

#Using datetime module of python, write a code which gives the weeknumber of the input date
from datetime import datetime

def get_week_number(date_str):
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    return date_obj.isocalendar()[1]

print("Week number:", get_week_number("2025-01-06"))
