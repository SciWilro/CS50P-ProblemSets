''' Little Professor Maths Game  
[Info](https://en.wikipedia.org/wiki/Little_Professor)
Prompts user for level (int) 1, 2, OR 3
3 Tries per problem -> Displays answer
10 problems total -> Display score

Addition Only
'''

__author__ = 'Wilro - https://github.com/SciWilro'

import random


def main()
    # Get level (reprompt)
    level = get_level()
    
    # Generate 10 problems
    #   return dictionary/ list with question string and int answer
    # length of list based on arg n (int)
    

def get_level():
    ''' Reprompts user for level  
Returns:
    level (int): level 1, 2, or 3
'''
    while True:
        level = input("Level?: ")
        if level in ['1','2','3']:
            print("Level string matches")
            return int(level)


def generate_integer(level):
    ...

if __name__ == '__main__':
    main()





