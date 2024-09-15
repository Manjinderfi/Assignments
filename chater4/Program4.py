import random

def guessing_game():
    secret_number = random.randint(1, 10)

    while True:
        guess = input("Guess a number between 1 and 10: ")

        try:
            guess = int(guess)

            if guess > secret_number:
                print("Too high!")
            elif guess < secret_number:
                print("Too low!")
            else:
                print("Correct! You guessed the right number!")
                break  # End the game if the guess is correct
        except ValueError:
            print("Please enter a valid number.")

guessing_game()
