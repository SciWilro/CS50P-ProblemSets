# https://cs50.harvard.edu/python/2022/psets/1/bank/
# Rewritten based on Problem Set 5 - Unit Tests
__author__ = "Wilro - https://github.com/SciWilro"


def main():
    print_value = value(input("Greeting?: "))
    print(f"${print_value}")


def value(greeting: str) -> int:
    greeting = greeting.strip().lower()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


main()

# bank.py prompts user for a greeting.
# If string starts with “hello”, output $0.
# If string starts with an “h” (but not “hello”), output $20.
# Else, output $100.
# ignore whitespace and treat case-insensitively.
