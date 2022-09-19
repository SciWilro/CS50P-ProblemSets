""" Little Professor Maths Game
[Info](https://en.wikipedia.org/wiki/Little_Professor)
Prompts user for level (int) 1, 2, OR 3
3 Tries per problem -> Displays answer
10 problems total -> Display score

Addition Only
"""

__author__ = "Wilro - https://github.com/SciWilro"

import random


def main():
    t = 10  # How many questions / stages
    score = 0
    level = get_level()
    plist = gen_problems(level, t)

    for x in range(0, t):
        counter = 0
        while counter < 3:
            question = plist[x][0]
            answer = int(input(question))
            if answer != plist[x][1]:
                print("EEE")
                counter += 1
                if counter == 3:
                    print((plist[x][0]).strip(), plist[x][1])
            else:
                score = score + 1
                break
    print("Score: ", score)


def get_level():
    """Reprompts user for level
    Returns:
        level (int): level 1, 2, or 3"""
    while True:
        level = input("Level?: ")
        if level in ["1", "2", "3"]:
            return int(level)


def generate_integer(level):
    if level not in [1, 2, 3]:
        raise ValueError("Level must be either 1, 2, OR 3")
    else:
        match level:
            case 1:
                return random.randrange(0, 10)
            case 2:
                return random.randrange(10, 100)
            case 3:
                return random.randrange(100, 1000)


def gen_problems(level: int, t=10):
    #   returns list with question string and int answer
    # length of list based on level (int)
    plist = [None for x in range(t)]
    for z in range(0, t):
        a = generate_integer(level)
        b = generate_integer(level)
        plist[z] = [f"{a} + {b} = ", (a + b)]
    return plist


if __name__ == "__main__":
    main()
