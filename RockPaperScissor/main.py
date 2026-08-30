# Loop
    # Ask the user to make a choice
    # If choice is invalid
    #   Print an error
    # Let the computer to make a choice
    # Print choices (Emojis)
    # Determine the winner
    # Ask the user if they want to continue
    # If not terminates
    
import random

ROCK = 'r'
PAPER = 'p'
SCISSOR = 's'

choices = {ROCK: '🪨', PAPER: '📄', SCISSOR: '✂️'}
choices_keys = tuple(choices.keys())

def get_user_choice():
    while True:
        user_choice = input("Rock, paper, scissor? (r/p/s): ").lower()

        if user_choice in choices_keys:
            return user_choice
        else:
            print('Invalid input!')

def display_choices(user_choice, computer_choice):
    print(f"You chose {choices[user_choice]}")
    print(f"Computer chose {choices[computer_choice]}")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('Tie!')
    elif (
        (user_choice == ROCK and computer_choice == SCISSOR) or
        (user_choice == SCISSOR and computer_choice == PAPER) or
        (user_choice == PAPER and computer_choice == ROCK)):
            print('You won')
    else:
        print('You lose')

def play_game():
    while True:
        user_choice = get_user_choice()
        
        computer_choice = random.choice(choices_keys)
        
        display_choices(user_choice, computer_choice)
        
        determine_winner(user_choice, computer_choice)
        
        play_more = input('Do you want to play more? (y/n)').lower()
        if play_more == 'n':
            print('Thank for playing!')
            break
    
play_game()