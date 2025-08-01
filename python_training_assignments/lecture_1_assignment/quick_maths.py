"""
Assignment 2: Quick Maths
Write a program that asks the user for two numbers
and then performs basic arithmetic operations on them.
"""
def get_user_input(a, b):
    #Get user input
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    return a, b

def arithmetic_operations(a, b):
    #Perform arithmetic operations
    print(f"Sum: {a + b}")
    print(f"Difference: {a - b}")
    print(f"Product: {a * b}")
    try:
        quotient = round(a / b, 10) #Roung to 10 decimal places
        print(f"Quotient: {quotient}")
    except ZeroDivisionError:
        print("Quotient: Cannot divide by zero.")
    finally:
        print("Arithmetic operations completed.")
        
if __name__ == "__main__":
    a, b = get_user_input(0, 0)  #Placeholders for a and b
    arithmetic_operations(a, b)  #Execute arithmetic operations
