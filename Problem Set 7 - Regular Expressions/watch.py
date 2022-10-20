__author__ = 'Wilro - https://github.com/SciWilro'
'''_summary_
Takes HTML sourcecode as input and tries to extract youtube url within an `iframe`'s `src` attribute
and returns shortened url
'''

import re
import sys


def main():
    print(parse(input("HTML: ")))
    
    
    

def parse(s):
    '''
    Args:
        s (string): string of HTML sourcecode to parse
    
    Returns:
        string: Shortened URL in the form of "https://youtu.be/XXXXXXXXXX"
        None:   If no valid url is found
    '''
    pattern = r'(?:<iframe).*(?:src=")(?:https?://(?:www\.)?(?:youtube\.com/embed/))(.*?)(?:".*)'
    #  (.*?) makes group non-greedy - as few characters as possible will be matched
    if matches := re.search(pattern, s):
        return f"https://youtu.be/{matches.group(1)}"
    else:
        return None





if __name__ == "__main__":
    main()