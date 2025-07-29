import day_2
import yaml
import sys
#This allows us to use the odd_even function in other files 
# without running the main code

"""
def odd_even():
    
   #Function to check if a number is even
    num = int(input("Enter a number: "))
    return num % 2 == 0

#which function will be used?
print(odd_even()) #example.py odd_even has priority over day_2 odd_even
"""

#File functions
def load_scores():
    with open("score.yaml", "r") as file:
        return yaml.safe_load(file)  # Load the YAML file contents

if __name__ == "__main__":
    # If this file is run directly, execute the code below
    data = load_scores()  # Load the YAML data

    if len(sys.argv) >= 3:
        name = sys.argv[1]
        subject = sys.argv[2]
        print(data['scores'][subject][name])  # Get the name from command line arguments
    else:
        print("Usage: python example.py <name> <subject>")
        sys.exit(1)
"""
print(data)  # Print the contents of the file
print(data['mentors'][1])
print(data['scores']['linux'])  # Accessing a specific key in the YAML data"
"""