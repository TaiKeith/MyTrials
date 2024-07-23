import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

hangman_stages = [
    '''
       +---+
           |
           |
           |
          ===''',
    '''
       +---+
       O   |
           |
           |
          ===''',
    '''
       +---+
       O   |
       |   |
           |
          ===''',
    '''
       +---+
       O   |
      /|   |
           |
          ===''',
    '''
       +---+
       O   |
      /|\\  |
           |
          ===''',
    '''
       +---+
       O   |
      /|\\  |
      /    |
          ===''',
    '''
       +---+
       O   |
      /|\\  |
      / \\  |
          ==='''
]

incorrect_guesses = 0

#Create a list of words for the game:
word_list = ["apple", "banana", "cherry", "date", "berry", "fig", "grapes"]

#Select a random word from the list:
word = random.choice(word_list)

#Create a variable to keep track of a player's guesses:
guesses = set()

#Set the number of turns the player has:
turns = 6

#Create a while loop to keep running until the player runs out of turns
while turns > 0:
    #Display the hangman stage:
    """clear_screen()
    print(hangman_stages[incorrect_guesses])"""

    #Display the current state of the word with underscores for unguessed letters:
    display_word = ""
    for letter in word:
        if letter in guesses:
            display_word += letter
        else:
            display_word += "_ "
    print (display_word)

    #Get the player's guess
    guess = input("Guess a letter: ").lower()

    #Check if guessed letter has already been made
    if guess in guesses:
        print("You already made that guess before")
        continue

    #Add the guess to the player's list of guesses
    guesses.add(guess)

    #Check if the guess is correct:
    if guess not in word:
        turns -= 1
        if turns < 1:
            print(f"Wrong guess! You have {turns} turns left.")
        elif turns == 1:
            print(f"Wrong guess! You have {turns} turn left.")
        else:
            print(f"Wrong guess! You have {turns} turns left.")
        incorrect_guesses += 1
    #Check if the player has won:
    if "_" not in display_word:
        print("Congratulations! You guessed the word correctly.")
        break

#Check if the player has run out of turns:
if turns == 0:
    print(f"Sorry, you ran out of turns. The word was {word}")
