import functions as md
import os

def main():
    tries = 0
    guessedWords = []
    coloredGuesses = []
    word = md.generate_word()

    continue_game = True

    md.introduction()

    while continue_game:
        guess = md.take_input(guessedWords)
        guessedWords.append(guess)
        tries += 1


        coloredGuesses.append(md.compare(guess, word))
        md.display_guesses(coloredGuesses)

        if guess == word:
            continue_game = False
            print("\nCongrats! You won the game.")
        elif tries == 6:
            continue_game = False
            print("\nSorry you are out of tries.")
        else:
            continue_game = True

    play_again = input("Would you like to play again (y/n)? ")

    if play_again.lower() == "y":
        os.system('clear')
        main()
    else:
        print("Thanks for playing! Goodbye!")


main()






