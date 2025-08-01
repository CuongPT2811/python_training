"""
Assignment 1: Hello, You!
Write a program that asks the user for their name
and then greets them with Hello, <NAME>! Nice to meet you!
"""
def greet_user():
    #Ask the user for inputting their name
    name = input("What is your name?: ")
    
    #Greet the user
    print(f"Hello, {name.upper()}! Nice to meet you!") #.upper() converts the name to uppercase, can be removed

if __name__ == '__main__':
    greet_user() #Execute above function