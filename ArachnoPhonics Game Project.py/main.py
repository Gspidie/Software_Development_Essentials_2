#access libraries and py files 
import time
import os
import spiderDraw as sd
import functions as md

#Make a list of the spider drawings
spiderList = [sd.spider_0, sd.spider_1, sd.spider_2, sd.spider_3, sd.spider_4, sd.spider_5, sd.spider_6]

streak = 0

def play_game():
  #generate a random word from word list
  word = md.generate_word()  

  #Initialize variables and setup 
  #Need to keep track of correct letters, incorrect letters and tries
  correct = []  #List of correct letters guessed
  incorrect = []  #List of incorrect letters guessed
  tries = 0   #Number of incorrect guesses
  game = True 
  global streak

  #Print intro statements (welcome to game, etc)
  md.introduction()
  
  #Game Loop
  while not md.won_game(word, correct) and not md.lost_game(tries): 
    #time.sleep(1)
    if len(correct) > 0 or len(incorrect) > 0:
      print(f"Word = {md.print_word(word, correct)}")
    md.print_spider(tries,spiderList)

    md.print_wrong_guesses(incorrect)
    guess = input('Guess a letter: ')
    correct, incorrect, tries = md.check_word(guess, word, correct, incorrect, tries)

  if md.lost_game(tries):
    streak = 0
    print("You lost! Streak reset!")

  if md.won_game(word, correct):
    streak += 1
    print(f"You won! Your streak is {streak}")
    time.sleep(3)
    md.victory_drawing()

  anwser = input("Do you wanna play again (y/n)? ")

  play_again = anwser == "y"
  
  if play_again: 
    print("Nice to have you back! \n")
  else:
    print("Have a good day. Thank you for playing!")

  return play_again

playing_game = True
while playing_game:
  playing_game = play_game()