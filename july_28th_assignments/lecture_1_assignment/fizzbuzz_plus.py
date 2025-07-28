"""
Assignment 4: FizzBuzz Plus
Read an integer from the user (1 <= N <= 1000)
Loop from 1 to N and print:
- "Fizz" if the number is divisible by 3
- "Buzz" if the number is divisible by 5
- "FizzBuzz" if the number is divisible by both 3 and 5 (aka 15)
Otherwise, print the number itself.
Count the number of times "Fizz", "Buzz", "FizzBuzz", and the numbers themselves are printed.
"""

def get_user_input():
    #Get user input
    while True:
        try:
            n = int(input("Enter an integer (1 <= N <= 1000): "))
            if 1 <= n <= 1000:
                return n
            else:
                print("Please enter a number between 1 and 1000.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.") #exception handling for non-integer inputs
        finally:
            print("Input completed.") 

def fizzbuzz_plus(n):
    fizz_count = 0
    buzz_count = 0
    fizzbuzz_count = 0
    number_count = 0

    for i in range(1, n + 1):
        if i % 3 == 0:
            print("Fizz")
            fizz_count += 1
        elif i % 5 == 0:
            print("Buzz")
            buzz_count += 1
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
            fizzbuzz_count += 1
        else:
            print(i)
            number_count += 1

    print(f"Fizz count: {fizz_count}")
    print(f"Buzz count: {buzz_count}")
    print(f"FizzBuzz count: {fizzbuzz_count}")
    print(f"Number count: {number_count}")

fizzbuzz_plus(get_user_input())  #Get user input and execute FizzBuzz Plus logic