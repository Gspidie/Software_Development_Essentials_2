import random
import os
import time

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[33m'
RESET = '\033[0m'

def introduction():
    print("\nWelcome to Woordle!")
    print("Guess the mystery 5 letter word.")
    #print("You will be presented an alphabet.")
    print(f"If the letter is {GREEN}green{RESET}, it is the correct letter in the correct spot.")
    print(f"If the letter is {YELLOW}yellow{RESET}, it is the correct letter in the wrong spot.")
    print(f"If the letter is {RED}red{RESET}, that letter is NOT in the word.")
    print("You have six attempts, good luck!")
    print("")

def take_input(guesses):
    user_has_guess = False
    user_word = ""

    while not user_has_guess:
        user_word = input("What is your guess? ").lower()
        user_has_guess = valid(user_word, guesses)

    time.sleep(2)
    os.system('clear')   
    
    return user_word

def valid(guess, guesses):
    word_list = open('/workspaces/SDE2-python-env-starter-GSP/Lesson12/words.text').read().split()

    if not guess.isalpha(): 
        print("Please include only letters in your guess. \n")
        return False
    elif not len(guess) == 5:
        print("Your guess must be five characters. \n")
        return False
    elif guess in guesses:
        print("You have already guessed that. \n")
        return False
    elif not guess in word_list:
        print("Oops. Guess provided is not saved as a real word! \n")
        return False
    else:
        return True
    
def compare(guess, word):
    correct = []
    incorrect = []
    misplaced = []
    coloredGuess = ""

    for index, letter in enumerate(guess):
        if letter == word[index]:
            correct.append(letter)
            coloredGuess += f"{GREEN}{letter}{RESET} "
        elif letter in word:
            misplaced.append(letter)
            coloredGuess += f"{YELLOW}{letter}{RESET} "
        else:
            incorrect.append(letter)
            coloredGuess += f"{RED}{letter}{RESET} "

    return coloredGuess

def display_guesses(guesses):
    for guess in guesses:
        print(f"[ {guess}] \n") 

def generate_word():
    word_list = open('/workspaces/SDE2-python-env-starter-GSP/Lesson12/words.text').read().split()
    word = random.choice(word_list)
    return word

