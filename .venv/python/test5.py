"""1) to find common elements in a list!.
--> write a function which takes 2 lists as arguments and find out the common elements between them
--->do not use builtin functions
---> function should be re-usable
---> return a new list which contains both elements
---> if possible use list comprehension"""

def find_common_elements(list1, list2):
    common = [item for item in list1 if item in list2]
    return common

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = find_common_elements(list1, list2)
print("Common elements:", common_elements)

"""2. Print the max value element from the below list.
list_a= [12,13,5,2,6,7,8]

output should be max value printed
list_a = [12, 13, 5, 2, 6, 7, 8]"""

def find_max(lst):
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val

print("Max value:", find_max(list_a))

"""3. Consider the nested list given below,
k = [
[123, 234, 345, 234, 321, 444],
[456, 123, 434, 567, 678, 678, 123],
[456, 345, 333, 888, 777, 456, 999, 222],
]
remove duplicate entries in the each list and return the list
----> should use list comprehension"""
k = [
    [123, 234, 345, 234, 321, 444],
    [456, 123, 434, 567, 678, 678, 123],
    [456, 345, 333, 888, 777, 456, 999, 222],
]

def remove_duplicates(nested_list):
    return [[item for i, item in enumerate(sublist) if item not in sublist[:i]] for sublist in nested_list]

print("List after removing duplicates:", remove_duplicates(k))

"""4. Write a function, which takes tuple as argument, and return the 2 lists [ str list and integer list] for each type
---> eg: (123, 'abc', 'def', 345, 'sss', 999)
---> required output:
intlist: [123, 345, 999]
strlist: ['abc', 'def', 'sss']
---> validate the type and insert the record into each list"""
def separate_tuple_elements(input_tuple):
    int_list = [item for item in input_tuple if isinstance(item, int)]
    str_list = [item for item in input_tuple if isinstance(item, str)]
    return int_list, str_list

result = separate_tuple_elements((123, 'abc', 'def', 345, 'sss', 999))
print("Integer list:", result[0])
print("String list:", result[1])

"""5. take out all the ones in the list at start and keep the other element sequence intact.
l=[0,1,3,0,1,2,0,1,2,3,4,1,6,3]
output should be= [1,1,1,1,0,3,0,2,0,2,3,4,6,3]
l = [0, 1, 3, 0, 1, 2, 0, 1, 2, 3, 4, 1, 6, 3]"""

def move_ones(lst):
    ones = [x for x in lst if x == 1]
    others = [x for x in lst if x != 1]
    return ones + others

print("Output list:", move_ones(l))

"""6. Reverse the number?
(Note- do not convert the number to string and take output.)
write a function which takes number as arguments and returns the reversed number
--->do not use builtin functions
---> function should be re-usable
Eg: number= 123495867
Expected Output: 768594321"""
def reverse_number(num):
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10
    return reversed_num

print("Reversed number:", reverse_number(123495867))