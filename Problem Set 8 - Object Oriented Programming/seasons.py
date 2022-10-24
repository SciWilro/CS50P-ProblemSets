__author__ = 'Wilro - https://github.com/SciWilro'
'''
Prompts user for birth date and prints the total amount of minutes since they were born
    Input:
        date in format `YYYY-MM-DD`
    
    Output:
        Minutes since born printed in words
'''

import inflect
import re
import sys
from datetime import date

p = inflect.engine()

def get_birthday(birthday):
    
    if re.fullmatch(pattern = r"\d{4}-\d{2}-\d{2}", string = birthday) == None:
        sys.exit("Program takes date in format YYYY-MM-DD")
    else:
        birthlist = birthday.split('-')
        return date(int(birthlist[0]), int(birthlist[1]), int(birthlist[2]))

def get_mins(birthday):
    return (date.today() - birthday).days * 24 * 60

def to_words(birthday):
    mins = get_mins(birthday)
    return p.number_to_words(mins, andword='').capitalize() + ' minutes'


def main():
    birthday = get_birthday(input("Birth date: ").strip())
    print(to_words(birthday))
    


if __name__ == "__main__":
    main()