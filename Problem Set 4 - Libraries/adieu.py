"""Program gives greeting string
    Eg Adieu, adieu, to Liesl and Friedrich
Uses inflect pkg to construct list and adding oxform comma if needed
"""
__author__ = "Wilro - https://github.com/SciWilro"

import os

try:
    import inflect
except ImportError:
    os.system(f"pip install inflect")
    import inflect


def main():
    p = inflect.engine()  # https://pypi.org/project/inflect/
    mylist = []

    while True:
        try:
            usr_input = str(input("Name: "))
            mylist.append(usr_input)
        except (EOFError, KeyError, KeyboardInterrupt):
            print(f"Adieu, adieu, to {p.join(mylist)}", end="\n")
            break


if __name__ == "__main__":
    main()
