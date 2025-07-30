"""
Assignment 2: Create a text statistics toolkit
The toolkit provides functions to analyze text, including counting words, characters,
and calculating the average word length. 
It also includes a main function to run the analysis
"""

def word_count(text):
    """Count the number of words in the text.
    Split the text into words and count them, by default ignore spaces
    """
    return len(text.split()) 

def char_count(text):
    """Count the number of characters in the text.
    Replace spaces with nothing and count the characters."""
    return len(text.replace(" ", "")) 

def average_word_length(text):
    """Calculate the average word length in the text.
    Returns 0 if there are no words to avoid division by zero."""
    return round((char_count(text) / word_count(text)), 2) if word_count(text) > 0 else 0 

def analyze_text(text):
    """Analyze the text and return a tuple of 
    word count, character count, and average word length."""
    words = word_count(text)
    characters = char_count(text)
    avg_len = average_word_length(text)
    return (words, characters, avg_len)

def get_text_input():
    """Get text input from the user."""
    return input("Please enter the text to analyze: ")


def main():
    """Main function to run the text statistics toolkit."""
    text = get_text_input()
    analysis = analyze_text(text)
    print(f"Tuple of text statistics: {analysis}")

if __name__ == "__main__":
    main()