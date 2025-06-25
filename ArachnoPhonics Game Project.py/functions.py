import random
import os
import time

# Prompts user for letter guess. Checks through the secret word to see if it contains the letter guessed by the user. Returns the number of wrong guesses
#Takes in the correct letter list, incorrect letter list, secret word and the number of tries as parameters.

def check_word(guess, word, correct, incorrect, tries):

  if not is_guess_valid(guess):
    print("Please input only one letter \n")
    return correct, incorrect, tries
  
  if already_guessed(guess, incorrect, correct):
    print("You already guessed that.")
    return correct, incorrect, tries

  if is_guess_correct(guess, word):
    correct.append(guess)
    print(f"{guess} is in the hidden word!")
    time.sleep(2)
    os.system('clear')
  else:
    incorrect.append(guess)
    tries += 1
    print(f"{guess} is not in the word!")
    time.sleep(2)
    os.system('clear')

  return correct, incorrect, tries

  
'''
def check_word():
  guess = input("Enter a valid guess: ")

  if guess.isaplha() and len(guess) == 1:
    return guess
  else:
    check_word()
'''
    
def is_guess_correct(guess, word):
  return guess.lower() in word

def is_guess_valid(guess):
  return (guess.isalpha() and len(guess) == 1)


# Returns the word to the console containing "_" for any letter not guessed by the user.
#Takes in the correct word and the list of correct guesses as parameters
def print_word(correctWord, correctGuesses):
  word = " "

  for i, letter in enumerate(correctWord):
    if letter not in correctGuesses:
      word += "_"
    else: 
      word += letter
  
  return word



# Prints spider from the spider drawing functions in the spiderDraw.py file. Takes the number of wrong guesses and the list of spider drawing functions as parameters.

def print_spider(tries,spiderList):
  spiderList[tries]()


#Opens the word list text file, stores the contents into a list, chooses a random word from the list, finds the length of that word and prints a string of blanks for each letter in the word. Returns the word.
def generate_word():
  wordList = open('/workspaces/SDE2-python-env-starter-GSP/ArachnoPhonics Game Project.py/words.txt').read().split()
  word = random.choice(wordList)
  #print('Word = ' + '_'*len(word))
  return word

# Returns True if user's guess is already in incorrect or correct list
def already_guessed(guess, incorrectGuesses, correctGuesses):
  return guess in incorrectGuesses or guess in correctGuesses

# Prints wrong guesses
def print_wrong_guesses(incorrectGuesses):
  print(f'Incorrect Guesses = {incorrectGuesses}')

#Put the introduction code/input player name into here 
def introduction():
  print("")
  print("")
  print("Welcome to ArachnoPhonics! \n")
  userName = input("What is your name? \n")
  print(f'{userName}, your goal is to guess the word, letter by letter. \n')
  print("Do not let the spider get you! \n")
  

def won_game(word, correctGuesses):
  for letter in word:
    if letter not in correctGuesses:
      return False

  return True


def lost_game(tries):
  return tries == 6

def victory_drawing():
  print(f"################################################################")
  print(f"#       ____       ______      ______                ___       #")
  print(f"#      /    |     /      \    /      \              /  /       #")
  print(f"#     /__   |    |   __   |  |   __   |    ___     /  /        #")
  print(f"#       |   |    |  |  |  |  |  |  |  |   |   |   /  /         #")
  print(f"#       |   |    |  |  |  |  |  |  |  |   |___|  /  /  ___     #")
  print(f"#       |   |    |  |__|  |  |  |__|  |         /  /  |   |    #")
  print(f"#     __|   |__  |        |  |        |        /  /   |___|    #")
  print(f"#    |_________|  \______/    \______/        /__/             #")
  print(f"#                                                              #")
  print(f"################################################################")





  