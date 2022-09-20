"""
Module takes str as input and removes all vowels (case insensitive)
    Args:
        word (str):
    Returns:
        str: str with all vowels removed
TODO Don't remove certain single letter words like 'A' or 'I'
     Also.. regex method might be better - for future reference
"""

__author__ = "Wilro - https://github.com/SciWilro"

banned_letters = list("AaEeOoUuIi")


def main():
    word = input("Input string:")
    print(shorten(word))


def shorten(word: str) -> str:
    output = ""
    try:
        for s in word.strip():
            if s not in banned_letters:
                output += s
    except AttributeError:
        raise TypeError("shorten function expects string variable as arguement")
    return output.strip()


if __name__ == "__main__":
    main()
