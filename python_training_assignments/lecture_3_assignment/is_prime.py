"""Assignment 4: Check prime number"""

def is_prime(number, divisor=2):
    """
    Check if a number is prime or not using recursion.
    """

    #Base cases
    if number < 2:
        return False
    if number == 2:
        return True
    if number % divisor == 0:
        return False
    if divisor * divisor > number:
        return True
    
    #Recursive step
    return is_prime(number, divisor + 1)

def prime_list(limit):
    """
    Generate a list of prime numbers less than or equal to the given limit.
    """

    primes = []
    for number in range(2, limit + 1):
        if is_prime(number):
            primes.append(number)
    return primes

def get_limit_input():
    """
    ASK user to enter a positive integer limit (<= 10000)
    Returns the validated integer.
    """
    while True:
        try:
            limit = int(input("Enter the limit (a positive integer <= 10000): "))
            if 0 < limit <= 10000:
                return limit
            else:
                print("Error: Please enter a number between 1 and 10000.")
        except ValueError:
            print("Error: Invalid integer. Please try again.")

def main():
    """Main function to run the program, get limit input, and print results."""
    
    #Get validated input from user
    limit = get_limit_input()

    #Generate the list and print results
    primes = prime_list(limit)
    print(f"\nPrime numbers less than or equal to {limit}:")
    print(primes)
    print(f"Total primes found: {len(primes)}")

if __name__ == "__main__":
    main()