"""
Assignment 1: Odd or Even
Write a program that take user input (accepts integer values, can be negative) 
and determines if the number is odd or even.
"""
def get_user_input():
    #Get user input, accept integer values, can be negative
    while True:
        try:
            n = int(input("Enter an integer: "))
            return n
        except ValueError:
            print("Invalid input. Please enter a valid integer.")



def is_odd_or_even(n):
    return "even" if n % 2 == 0 else "odd" #Return "even" if n is divisible by 2, else return "odd" - Tenary operator 

print(is_odd_or_even(get_user_input())) #Print out the result 
