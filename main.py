"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Lubomír Smola
email: L.smola@seznam.cz
"""
import random

#Functions for the game
def get_number_for_guessing():
    """
    Function to generate a 4-digit number for guessing.
    """
    number = ""
    while len(number) < 4:
        digit = str(random.randint(0, 9))
        if digit not in number:
            number += digit
    return number

def begins_with_zero(number):
    """
    Function to control if number begins with zero.
    """
    if number[0] == "0":
        return True

def get_user_guess():
    """
    Function to get a guess from the user.
    """
    while True:
        user_input = input(">>> ")#("Enter a 4-digit number: ")
        print(("-" * 79))
#        if user_input.isdigit() and len(user_input) == 4:
        return user_input
#        else:
#            print("Wrong input. Please enter a 4-digit number.")

def compare_numbers(number_for_guessing, user_guess):
    """
    Function to compare numbers and return bulls and cows.
    """
    bulls = 0
    cows = 0
    for i in range(4):
        if user_guess[i] == number_for_guessing[i]:
            bulls += 1
        elif user_guess[i] in number_for_guessing:
            cows += 1
    return bulls, cows

def is_number_len_four(number):
    """
    Function to check if the number is 4 digits long.
    """
    if len(number) == 4:
        return True
    else:
        return False
    
def check_duplicates(number):
    """
    Function to check if the number contains duplicates.
    """
    if len(set(number)) != 4:
        return True
    return False

def check_numeric(number):
    """
    Function to check if the input is numeric.
    """
    if number.isdigit():
        return True
    else:
        return False

#Run the game
section = ("-" * 79)
print("Hi there!")
print(section)
print("""I've generated a random 4 digit number for you.
Let's play a bulls and cows game.""")
print(section)
print("Enter a number:")
print(section)
number_for_guessing = get_number_for_guessing()

while True:
    user_guess = get_user_guess()
    if begins_with_zero(user_guess):
        print("Your number begins with zero. Please try again.")
        continue
    elif not is_number_len_four(user_guess):
        print("Your number is not 4 digits long. Please try again.")
        continue
    elif check_duplicates(user_guess):
        print("Your number contains duplicates. Please try again.")
        continue
    elif not check_numeric(user_guess):
        print("Your input is not numeric. Please try again.")
        continue
    bulls, cows = compare_numbers(number_for_guessing, user_guess)
    print(f"Bulls: {bulls}, Cows: {cows}")
    if bulls == 4:
        print("Congratulations! You've guessed the right number!")
        break
    else:
        print("Try again!")
        print(section)
#        print("Enter a number:")