"""In-build Methods
reverse a string using inbuild method.
Convert a string to num using inbuild methods
Convert a string to float using inbuild method
Write a program to create a text file(.txt), and write and read the file."""
string = "Juniper Automation"
reversed_string = string[::-1]
print("Reversed string:", reversed_string)

num_str = "123"
num = int(num_str)
print("Converted to integer:", num)

float_str = "123.45"
num_float = float(float_str)
print("Converted to float:", num_float)

file_name = "example.txt"
with open(file_name, "w") as file:
    file.write("Hello, this is a sample text file.\n")
    file.write("This file is created, written, and read using Python.")

with open(file_name, "r") as file:
    content = file.read()
    print("File content:")
    print(content)

#Write a generator function and take out the output using a looping function.
def simple_generator():
    for i in range(5):
        yield i

for val in simple_generator():
    print(val)

"""Write a factorial fucntion for recursion for any number as input and try to understand its functioning."""
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial:", factorial(5))
