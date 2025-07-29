"""
Assignment 3: Factorial Sum
Write a program that get a user input from 1 to 12
Calculates the factorial of input number using for loop
Calculates the sum of all numbers from 1 to input number
"""

def get_user_input():
    #Get user input
    while True:
        try:
            number = int(input("Enter a number (1 - 12): "))
            if 1 <= number <= 12:
                return number
            else:
                print("Please enter a number between 1 and 12.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def factorial_sum(number):
    #Calculate factorial and sum from 1 to number
    factorial = 1
    total_sum = 0
    
    for i in range(1, number + 1): #Loop from start (1) to stop (number + 1, include number)
        factorial *= i
        total_sum += i
    
    print(f"Factorial of {number} is: {factorial}")
    print(f"Sum of all numbers from 1 to {number} is: {total_sum}")
if __name__ == "__main__":
    factorial_sum(get_user_input())