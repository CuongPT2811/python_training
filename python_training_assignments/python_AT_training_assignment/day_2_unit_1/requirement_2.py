"""Function to reverse a string"""

import time


def reverse_string(string):
    #Using slicing to reverse string
    return string[::-1]

def get_user_input():
    #Get user input string
    string = input("Enter your string: ")
    return string

if __name__ == '__main__':
    original_string = get_user_input()
    reversed_str = reverse_string(original_string)
    print(f"Original string: '{original_string}'")
    print(f"Reversed string: '{reversed_str}'")