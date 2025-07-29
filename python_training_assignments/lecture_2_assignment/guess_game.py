"""Assignment 4: Guess Game
Write a program that pick a random int from 1 to 100
Repeatedlt ask user to guess the number until correct
After each guess, print "Too high!" or "Too low!" or "Correct!"
At the end, print the number of attempts it took to guess correctly.
"""
import random #Module to generate random numbers
def guess_game():
    
    secret_number = random.randint(1, 100) #Function to get a random integer, from 1 to 100
    attempts = 0 #Count for attempts

    while True:
        try:
            guess_number = int(input("Guess a integer in 1-100: "))
            attempts += 1
            if guess_number < 1 or guess_number > 100:
                print("Please enter a number between 1 and 100.")
                continue
            if guess_number < secret_number:
                print("Too low!")
            elif guess_number > secret_number:
                print("Too high!")
            else:
                print(f"Correct! The secret number was {secret_number}.")
                print(f"It took you {attempts} attempts to guess the correct number.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
if __name__ == "__main__":
    guess_game()
