"""
Assignment 1: Create a temperature converter
"""

def convert_temp(value, to_scale):
    if to_scale.upper() == 'C':
        return (value - 32) * 5.0 / 9.0
    elif to_scale.upper() == 'F':
        return (value * 9.0 / 5.0) + 32
    else:
        raise ValueError("Invalid scale. Use 'C' for Celsius or 'F' for Fahrenheit.")

def get_user_input():
    while True:
        try:
            temp_value = float(input("Enter the temperature value: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for temperature.")
    while True:
        temp_scale = input("Convert to (C/F): ").strip()
        if temp_scale.upper() in ('C', 'F'):
            break
        else:
            print("Invalid scale. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    return temp_value, temp_scale

if __name__ == "__main__":
    default_temp = 100.0  # Default temperature value
    default_scale = 'C'  # Default scale to convert to
    temp_value, temp_scale = get_user_input()
    converted_temp = convert_temp(temp_value, temp_scale)
    print(f"Fixed temperature value: {default_temp}°{default_scale.upper()}")
    print(f"Converted temperature: {converted_temp:.2f}°{temp_scale.upper()}")
