'''
This is going to be a random number guessing game where the player has to guess a number between 1 and 100.
The player will have a limited number of guesses to get the secret number and will receive feedback to guide them and a final score if they guess
right number. 
'''

import random
import time

def number_to_guess():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a random number between 1 and 100.")
    return random.randint(1, 100)

user_guesses = 0
secret_number = number_to_guess()
guess_limit = 10  # Set a limit for the number of guesses

# This is the main game loop where the player will be prompted to enter their guess and receive feedback.
while user_guesses < guess_limit:
    try:
        guess = int(input("Enter your guess (between 1 and 100): "))
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue
        
        user_guesses += 1 
         
        if guess == secret_number:
            score = (guess_limit - user_guesses + 1) * 10
            print(f"Congratulations! You've guessed the number {secret_number} in {user_guesses} guesses.")
            print(f"Final score: {score}")
            break
        elif guess < secret_number:
            if user_guesses >= guess_limit:
                break
            print("Your guess is too low. You have", guess_limit - user_guesses, "guesses left. Try again.")
        else:
            if user_guesses >= guess_limit:
                break
            print("Your guess is too high. You have", guess_limit - user_guesses, "guesses left. Try again.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

# The game will end if the player runs out of guesses or guesses the correct number.
if __name__ == "__main__":
    if user_guesses >= guess_limit:
        print(f"Sorry, you've used all your guesses. The number was {secret_number}.")
    time.sleep(2)  # Pause for 2 seconds before exiting
