import sys
from random import randint


# generate random number


def run_guess(r,guess):
    if 0 < guess < 11:
        if guess == r:
            print('you got it right')
            return True
    else:
        print('number should be between 1-10')
        # continue

if __name__ == '__main__':
    r = randint(1, 11)
    while True:
        try:
            guess = int(input("guess a number 1-11  "))
            if run_guess(r, guess):
                break

        except ValueError:
            print('enter numbers only')
            continue

    # ask for input from user btwn 1-10
    # compare number and randm number
