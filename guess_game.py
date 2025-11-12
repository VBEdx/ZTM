from unittest import result
from sys import argv
import random


def play_guess_game(upper_bound:int, expected_value:int):
    print('Welcome to the Guess Game!')
    print(f'I am thinking of a number between 1 and {upper_bound}. Try to guess it.')
    while True:
        try:
            guess = int(input('Enter a guess: '))
            if guess < 1 or guess > upper_bound:
                print('Sorry, your guess is outside requested range.')
            elif guess == expected_value:
                print(f'You guessed it in {guess}!')
                return
            else:
                print(f'Unfortunately {guess} is incorrect, please try again!')
        except ValueError:
            print(f'You did not enter a number. Try again!')

if __name__ == '__main__':
    upper_bound = int(argv[1])
    random_value = random.randint(0, upper_bound)
    play_guess_game(upper_bound, random_value)
