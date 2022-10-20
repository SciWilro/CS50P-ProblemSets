__author__ = 'Wilro - https://github.com/SciWilro'
'''_summary_
    Asks user to input ip4 address and prints out whether it is valid or not
'''

import re
import sys

def validate(ip: str) -> bool:
    pattern = r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    return bool(re.search(pattern, ip))

def main():
    # print(validate(input("IPv4 Address: ")))
    print(validate(str(input("IPv4 Address: "))))


if __name__ == "__main__":
    main()
