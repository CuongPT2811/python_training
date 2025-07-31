"""Function to remove duplicate"""


def remove_duplicates(string):
    """
    Removes duplicates in string
    preserving the order of the first string
    """
    result = ""
    seen_characters = set() #Using a set for faster lookup
    for char in string:
        if char not in seen_characters:
            result += char
            seen_characters.add(char)
    return result

def remove_duplicate_words(string):
    """
    Removes duplicate words in a string,
    preserving the order of the first appearance.
    """
    words = string.split()  #Split string into words
    result = []
    seen_words = set()
    for word in words:
        if word not in seen_words:
            result.append(word)
            seen_words.add(word)
    return ' '.join(result)

def get_user_input():
    #Get user input string
    string = input("Enter your string: ")
    return string

if __name__ == '__main__':
    input_string = get_user_input()
    unique_string = remove_duplicates(input_string)
    unique_word_string = remove_duplicate_words(input_string)
    print(f"Original string: '{input_string}'")
    print(f"String after removing duplicate characters: '{unique_string}'")
    print(f"String after removing duplicate words: '{unique_word_string}'")