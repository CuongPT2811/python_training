print("Hello, World!\nThis is CuongPT24 speaking!")

#Indentation example
if True:
    print("This is indented code block.")
else:
    print("This is not executed.")  

#Variable assignment
name = "CuongPT24"
age = 24
print("Name:", name)
print("Age:", age)

#Variable reassignment
age = 25.0
print("Updated Age:", age)

#Type checking
x = 5
y = "CuongPT24"
print(type(x))
print(type(y))

#Variable rules
# 1. Cannot start with a number, example "1st_variable" is invalid
#    but "variable1" , "_1st_variable" are valid
# 2. Cannot contain spaces, example "my variable" is invalid
#    but "my_variable" is valid
# 3. Cannot use special characters except underscore (_), 
#    example "my-variable" is invalid
#    but "my_variable" is valid
# 4. Case-sensitive, example "myVariable" and "myvariable" are different variables
# 5. Cannot use Python reserved keywords, example "def", "class", "if", etc. are invalid

#Data types
"""Dictionary, List, Tuple, Set"""

# Dictionary example
dict_ex = {
    "name": "CuongPT",
    "age": 30,
    "is_student": False,
    "courses": ["Python", "JavaScript", "C++"]} #dict with key-value pairs, can not have duplicate keys

print(dict_ex["name"])
print(dict_ex.get("age"))  # Using get method to avoid KeyError if key doesn't exist
dict_ex["age"] = 31  # Changing the value of an existing key
print(dict_ex)

#List example
list_ex = [1, 2, 3, 4, 5]
print(list_ex[-1])
list_ex.append(6)  # Adding an element to the list
print(list_ex)
list_ex[2] = 10  # Changing the value at index 2
print(list_ex)# can add or remove elements, but cannot access by index like dict

#Tuple example
tuple_ex = (1, 2, 3, 4, 5) #tuple is immutable, cannot change values after creation
print(tuple_ex[0])

#Set example
set_ex = {1, 2, 3, 4, 5} #diff from list, no duplicate values, same as dict keys

#Muteable vs Immutable
# Mutable: List, Dictionary, Set
# Immutable: Tuple, String, Integer, Float  

#Example of mutability
mutable_list = [1, 2, 3]
mutable_list_2 = mutable_list 
mutable_list_2.append(4)
print(mutable_list)  # Both mutable_list and mutable_list_2 will show the same content
mutable_list[0] = 10  # This is allowed, list is mutable
print(mutable_list) 
# Example of immutability Integer 
immutable_int = 5
immutable_int = 10  # This is allowed, but it creates a new integer object, not changing the original one, or like in C, point to a new memory address
# immutable_int[0] = 10  # This will raise an error, integers are immutable
# Example of immutability String
immutable_string = "Hello"
# immutable_string[0] = "h"  # This will raise an error, strings are immutable

ex_project = ['Python Basics', 'Data Types', 'Variables', 'Mutability']
 # Joining list elements into a string with 'and' as separator
print(' and '.join(ex_project) )

#Formatting strings
name = "CuongPT24"
age = 24
# Using f-string for formatting
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)