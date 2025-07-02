"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Lubomír Smola
email: L.smola@seznam.cz
"""
# Library imports
import random

# Constants
number_length = 4 # Length of the number to guess. Max is 10.
section_separator = "-" * 79 # Section separator for better readability.

# Functions for the game
def get_number_for_guessing(number_length):
    """
    Function to generate a number_length-digit number for guessing
    without duplicates. Max number_length is 10.
    """
    number = str(random.randint(1, 9))
    while len(number) < number_length:
        digit = str(random.randint(0, 9))
        if digit not in number:
            number += digit
    return number

def check_empty(number):
    """
    Function to check if the input is empty.
    """
    if number == "":
        return True
    else:
        return False

def begins_with_zero(number):
    """
    Function to control if number begins with zero.
    """
    if number[0] == "0":
        return True
    else:
        return False

def compare_numbers(number_for_guessing, user_guess, number_length):
    """
    Function to compare numbers and return bulls and cows.
    """
    bulls = 0
    cows = 0
    for i in range(number_length):
        if user_guess[i] == number_for_guessing[i]:
            bulls += 1
        elif user_guess[i] in number_for_guessing:
            cows += 1
    return bulls, cows

def is_number_len_valid(number, number_length):
    """
    Function to check if the number is number_length digits long.
    """
    if len(number) == number_length:
        return True
    else:
        return False
    
def check_duplicates(number):
    """
    Function to check if the number contains duplicates.
    """
    if len(set(number)) != len(number):
        return True
    else:
        return False

def is_numeric(number):
    """
    Function to check if the input is numeric.
    """
    return number.isdigit()

# Main program starts here
print(section_separator)
print(f"Hi there!\n{section_separator}")
print(f"I've generated a random {number_length} digit number for you.")
print("Let's play a bulls and cows game.")
print(section_separator)
print("Enter a number:")
print(section_separator)

# Main game loop
number_for_guessing = get_number_for_guessing(number_length)
# Uncomment the following line to enable debug mode:
# print(f"Debug: The number to guess is {number_for_guessing}.\n{section}")
attempts = 0
while True:
    user_guess = input(">>> ")
    attempts += 1
    first_attempt_win = "Wow!!! " if attempts == 1 else ""
    attempts_word = "attempt" if attempts == 1 else "attempts"
    
    if check_empty(user_guess):
        print("You didn't enter anything. Please try again.")
        continue
    elif not is_numeric(user_guess):
        print("Your input is not numeric. Please try again.")
        continue    
    elif begins_with_zero(user_guess):
        print("Your number begins with zero. Please try again.")
        continue
    elif not is_number_len_valid(user_guess, number_length):
        print(f"Your number is not {number_length} digits long. Please try again.")
        continue
    elif check_duplicates(user_guess):
        print("Your number contains duplicates. Please try again.")
        continue

    bulls, cows = compare_numbers(number_for_guessing, user_guess, number_length)
    bull_word = "bull" if bulls == 1 else "bulls"
    cow_word = "cow" if cows == 1 else "cows"
    print(f"{bulls} {bull_word}, {cows} {cow_word}")
    if bulls == number_length:
        print(
            f"{first_attempt_win}Congratulations! You've guessed the right number "
            f"in {attempts} {attempts_word}!\n"
            "Thanks for playing. See you next time!"
        )
        break
    else:
        print("Try again!")
        print(section_separator)