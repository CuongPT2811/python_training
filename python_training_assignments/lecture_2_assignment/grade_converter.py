"""
Assignment 2: Grade Converter
Write a program that take user score (0 <= s <= 100)
Convert score to grade
"""

def get_user_score():
    #Get user score 
    while True:
        try:
            score = float(input("Enter a score (0 <= N <= 100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid score input. Please enter a valid score.") #exception handling for non-integer inputs

def grade_converter(score):
    #Convert score to grade
    match score:
        case score if 90 <= score <= 100: 
            return "A"
        case score if 80 <= score <= 89: 
            return "B"
        case score if 70 <= score <= 79: 
            return "C"
        case score if 60 <= score <= 69:
            return "D"
        case score if score < 60:
            return "F"
        
if __name__ == "__main__":
    #Run the grade converter 
    print(grade_converter(get_user_score()))
