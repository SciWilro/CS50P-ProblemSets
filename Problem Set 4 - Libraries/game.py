"""Guessing Game    
Args:
    n (int): level ( answer 1 <= n)
Output:
    Prints: Too small!, Too large!, or Just right!
"""
__author__ = "Wilro - https://github.com/SciWilro"

import random


def main():
    while True:
        try:
            n = int(input("Level: "))
            if n > 0:
                break
        except ValueError:
            continue  # Not really needed

    answer = gen_answer(n)

    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                guess_answer(guess, answer)
        except ValueError:
            continue  # Not really needed


def gen_answer(n: int) -> int:
    return random.randint(1, n)


def guess_answer(guess, answer):
    if guess == answer:
        print("Just right!")
        exit()
    elif guess > answer:
        print("Too large!")
    elif guess < answer:
        print("Too small!")


if __name__ == "__main__":
    main()
