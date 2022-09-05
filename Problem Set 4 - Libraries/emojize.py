"""translates emoji codes to emoji symbol
    Args:
        usr_input (str): Eg :thumbs_up:
    Returns:
        s (str): 👍
see list here: [emoji list](https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias)
"""
__author__ = "Wilro - https://github.com/SciWilro"

import os

# Install package if unable to import
try:
    import emoji
except ImportError:
    os.system(f"pip install emoji")
    import emoji


def main():
    print(emoji.emojize(input("Emoji code?")))


if __name__ == "__main__":
    main()
