"""
Module takes str as input and removes all vowels (case insensitive)
    Args:
        usr_input (str):
    Returns:
        str: str with all vowels removed
TODO Don't remove certain single letter words like 'A' or 'I'
     Also.. regex method might be better - for future reference
"""

__author__ = "Wilro - https://github.com/SciWilro"

banned_letters = list("AaEeOoUuIi")


def main():
    usr_input = input("Input string:")
    print(devowel(usr_input))


def devowel(usr_input):
    return "".join([s for s in usr_input if s not in banned_letters]).strip()


if __name__ == "__main__":
    main()
