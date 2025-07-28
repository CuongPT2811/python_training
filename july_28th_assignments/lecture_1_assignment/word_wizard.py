"""
Assignment 3: Word Wizard
Write a program that asks the user for a short sentence
Perform printing operations on the sentence.
"""

def get_user_sentence():
    #Get user sentence
    sentence = input("Please enter a short sentence: ")
    return sentence

def print_sentence_operations(sentence):
    print(f"Number of words: {len(sentence.split())}") #Count words by splitting the sentence
    print(f"The first word of the sentence: {sentence.split()[0]}") #Get the first word by splitting and return first element
    print(f"The last word of the sentence: {sentence.split()[-1]}") #Get the last word by splitting and return last element
    print(f"After reversing the sentence: {' '.join(sentence.split()[::-1])}") #Reverse the sentence by splitting and joining

print_sentence_operations(get_user_sentence())  #Get the user sentence and perform operations on it
