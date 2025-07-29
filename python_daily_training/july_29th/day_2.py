"""
Function is a python block of code that performs a specific task

"""
import sys
#print() has a default end character of newline, seperate by space
#print(value, sep=',', end='\t') output will be separated by comma and end with a tab

def odd_even(): #Can pass parameters to function, but not required, 

    """
    Function to check if a number is odd or even
    """
    num = int(input("Enter a number: "))
    return "is Even" if num % 2 == 0 else "is Odd"


if __name__ == "__main__":
    #if this file is run directly, then execute the code below
    #if this file is imported, then do not execute the code below
    #print(odd_even(5)) #Call the function with a parameter
    print(odd_even())

#Python can import this file as a module
#and use the odd_even function without executing the code below
#If we do not use the if __name__ == "__main__": block,
#then the code below will be executed when this file is imported
#This is a good practice to avoid executing code when importing modules