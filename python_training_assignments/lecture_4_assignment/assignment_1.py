"""Assignment 1: Mark List Manager
"""

def parse_input_to_marks(input_str: str) -> list[int]:
    """
    Split string of mark by (,) to list of integer
    """
    marks_str_list = input_str.split(',')
    return [int(mark.strip()) for mark in marks_str_list]

def calculate_statistics(marks: list[int]) -> dict:
    """
    Calculate value from mark list
    """
    if not marks:
        return {}
        
    highest = max(marks)
    lowest = min(marks) 
    average = sum(marks) / len(marks) 
    
    return {
        "highest": highest,
        "lowest": lowest,
        "average": average
    }

def create_bonus_list(marks: list[int]) -> list[int]:
    """
    Create a bonus list which not change the default list
    """
    return [mark + 5 for mark in marks]

def main():
    """
    Handle input, process and print
    """
    input_str = input("Enter list of marks, seperate by (,): ")
    
    try:
        original_marks = parse_input_to_marks(input_str)
        
        if original_marks:
            stats = calculate_statistics(original_marks)
            bonus_marks = create_bonus_list(original_marks)
            
            print(f"Highest mark: {stats['highest']}")
            print(f"Lowest mark: {stats['lowest']}")
            print(f"Average mark: {stats['average']:.2f}") 
            print(f"Bonus mark list (+5): {bonus_marks}")
            print(f"Original mark list (unchanged): {original_marks}")
        else:
            print("Empty mark list")

    except ValueError:
        print("Error: Please enter mark and (,) only")


if __name__ == "__main__":
    main()
