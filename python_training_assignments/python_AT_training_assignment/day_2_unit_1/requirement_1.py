"""Function to display factorial of a number"""

def calculate_factorial(n):
    """
    This function helps calculating factorial of positive numbers
    """
    #Check if the input number is negative
    if n < 0:
        return "Factorial is not defined for negative numbers"
    #The case for input = 0: 0! = 1
    elif n == 0:
        return 1
    else:
        factorial = 1
        # Use a for loop to calculate the product from 1 to n
        for i in range(1, n + 1):
            factorial *= i
        return factorial

def get_user_input():
    #Get user input
    while True:
        try:
            n = int(input("Enter an integer: "))
            return n
        except ValueError:
            print("Invalid input. Please enter a valid integer.") #exception handling for non-integer inputs

if __name__ == '__main__':
    number = get_user_input()
    print(f"The factorial of {number} is: {calculate_factorial(number)}")