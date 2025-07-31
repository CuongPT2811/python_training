"""Seperate positive and negative number"""

def input_numbers():
    """
   Allow user enter a list of integer, seperate by space
    """
    while True:
        input_str = input("Enter float number, seperate by space: ")
        try:
            number_list = [float(num) for num in input_str.strip().split()]
            return number_list
        except ValueError:
            print("Please enter float number, seperate by space only")

def separate_numbers(number_list):
    """
    Separates positive and negative numbers from a list.
    0 is considered a positive number.
    """
    positive_numbers = []
    negative_numbers = []
    for number in number_list:
        if number >= 0:
            positive_numbers.append(number)
        else:
            negative_numbers.append(number)
    return positive_numbers, negative_numbers

if __name__ == '__main__':
    numbers = input_numbers()
    positive_nums, negative_nums = separate_numbers(numbers)
    print(f"Original list: {numbers}")
    print(f"Positive numbers and zero: {positive_nums}")
    print(f"Negative numbers: {negative_nums}")