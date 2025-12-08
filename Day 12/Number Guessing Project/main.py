import random
import art

NUMBER_TO_GUESS = random.randint(1, 100)
print(NUMBER_TO_GUESS)

print(art.logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == 'easy':
    number_attempts = 10
else:
    number_attempts = 5

guess = int(input(f"You have {number_attempts} attempts remaining to guess the number.\nMake a guess: "))

def compare(guess_attempt, NUMBER_TO_GUESS):
    if guess_attempt == NUMBER_TO_GUESS:
        return 0
    elif guess_attempt < NUMBER_TO_GUESS:
        return 1
    elif guess_attempt > NUMBER_TO_GUESS:
        return 2
    else:
        return 3
result = (compare(guess, NUMBER_TO_GUESS))

while number_attempts > 0 and result != 0:
    if result != 0:
        number_attempts -= 1
        if number_attempts == 0:
            print(f"You lose! You don't have more attempts and the number was {NUMBER_TO_GUESS}.")
        elif result == 1:
            print(f"Too low.\nYou have {number_attempts} attempts remaining to guess the number.")
            guess = int(input("Guess again: "))
        elif result == 2:
            print(f"Too high.\nYou have {number_attempts} attempts remaining to guess the number.")
            guess = int(input("Guess again: "))
        else:
            print(f"You have {number_attempts} attempts remaining to guess the number.")
            guess = int(input("Guess again: "))
        result = compare(guess, NUMBER_TO_GUESS)
    else:
        print(f"You got it! The answer was {NUMBER_TO_GUESS}.")

print(f"You got it! The answer was {NUMBER_TO_GUESS}.")
