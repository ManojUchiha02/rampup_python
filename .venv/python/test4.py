#nested dictionary
"""nested_dict = {
    "student1": {"name": "Alice", "age": 20},
    "student2": {"name": "Bob", "age": 22}
}
print(nested_dict["student1"]["name"])"""

#list comprehension
"""squares = [x**2 for x in range(1, 6)]
print(squares)"""

#dictionary comprehension
"""cubes = {x: x**3 for x in range(1, 6)}
print(cubes)"""

#email validation regex
"""import re
email = "example@example.com"
pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"
if re.match(pattern, email):
    print("Valid email")
else:
    print("Invalid email")"""

#exception handling
"""try:
    num = int(input("Enter a number: "))
    assert num > 0, "Number must be positive"
    result = 10 / num
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Division successful:", result)
finally:
    print("Execution completed.")"""

#writing to a file
"""with open("example.txt", "w") as file:
    file.write("Hello, file handling in Python!")
with open("example.txt", "r") as file:
    content = file.read()
    print(content)"""

#lambda function for squaring a number
"""square = lambda x: x ** 2
print(square(2))"""

#using map to square all numbers in a list
"""numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x ** 2, numbers)
print(list(squared_numbers))"""

#using enumerate to loop with index
"""fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")"""

#swap first and last element in given list
l=[1,2,3,4,5]
l[0],l[-1]=l[-1],l[0]
print(l)