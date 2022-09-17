"""Guessing Game    
Args:
    n (int): level ( answer 1 <= n)
Returns:
    s (str): Too small!, Too large!, or Just right!
"""
__author__ = "Wilro - https://github.com/SciWilro"

import random


def main():
    while True:
        n = int(input("Level: "))
        if n > 0:
            break

    answer = gen_answer(n)

    while True:
        guess = int(input("Guess: "))
        if n > 0:
            guess_answer(guess, answer)


def gen_answer(n: int) -> int:
    return random.randint(1, n)


def guess_answer(guess, answer):
    if guess == answer:
        print("Just right!")
        exit()
    elif guess > answer:
        print("Too large!")
    elif guess < answer:
        print("Too samll!")


if __name__ == "__main__":
    main()
