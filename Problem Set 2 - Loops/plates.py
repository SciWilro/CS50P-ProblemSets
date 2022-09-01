__author__ = "Wilro - https://github.com/SciWilro"

# 1) must start with at least two letters.
# 2) Maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
# 3) Numbers must come at the end. Eg, AAA222 acceptable; AAA22A NOT.
#     The first number used cannot be a ‘0’.
# 4) No periods, spaces, or punctuation marks are allowed.

from curses.ascii import isdigit


def main():
    plate = input("Plate: ")
    # plate = "Test20"
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return all([valid_a(s), valid_b(s), valid_c(s), valid_numbers(s)])


# First 3 sub-functions can written inside is_valid return line - Harder to read though
def valid_a(s):
    return s[0:2].isalpha()


def valid_b(s):
    return 2 <= len(s) <= 6


def valid_c(s):
    return s.isalnum()


def valid_numbers(s):
    first_num = False
    for c in s:
        if first_num == False:
            if c.isdigit() and c != "0":
                first_num = True
            elif c.isalpha():
                pass
            else:
                return False
        else:  # If first_num == True
            if c.isalpha():
                return False
    return True


if __name__ == "__main__":
    main()
