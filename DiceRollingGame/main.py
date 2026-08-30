# Loop
    # Ask: rool the dice?
    # If user enters y
    #   Generate two random numbers
    #   Print them
    # If user enters n
    #   Print thanks for playing
    #   Terminate program
    # Else
    #   Print invalid choice
    
import random

rolled_count = 0
max_count = int(input("How many times do you want to roll the dice? "))
while rolled_count < max_count:
    choice = input("Roll the dice? (y/n) ").lower()
    if choice == 'y':
        rolled_count += 1
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f'({die1},{die2})')
    elif choice == 'n':
        print(f'You rolled {rolled_count} times')
        print('Thanks for playing!')
        break
    else:
        print('Invalid choice')
        
print(f'You rolled {rolled_count} times')
print('Thanks for playing!')