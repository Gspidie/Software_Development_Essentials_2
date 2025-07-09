# UCASE
    # Understand the problem
        # A Wordle clone that chooses a hidden word, takes user guesses, and displays an alphabet with colored letters based on their guess.
        # Inputs:
            # words 
        # Outputs
            # alphabet, introduction, input message
        # Edge Cases
            # Non-existing word 
            # Numbers and special characters
            # Not 5 letters
            # Repeats guess
    # Clue Detection
        # 'Guess the 5 letter word'
            # Take Input and perform Input validation
                # Use len()
                # Use .isalpha()
            # "Correct Letter in Correct Spot"
                # For loop, compare each letter in guess to hidden word
                # Keep track of index, enumerate()
                # List of correct and incorrect guesses
    # Assemble the Outline
        # Display Introduction
        # Take user Input
        # Compare user guess to hidden word
        # Display alphabet with correct, out-of-place, and incorrect letters.
        # Display win (correct word) or loss (out of tries)
