__author__ = 'Wilro - https://github.com/SciWilro'
'''_summary_
Program takes input (str) from user and counts the number of times 'um' is
found as a word on it's own.
    Input:
        string (str): input sentence
    Output:
        count (str): Number of times word was found
'''

import re

def main():
    print(count(input("Text: ")))

def count(s: str) -> int:
    return len(re.findall(r"\b\W*um\W*\b", s, re.IGNORECASE))

if __name__ == "__main__":
    main()