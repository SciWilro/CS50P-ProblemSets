# https://cs50.harvard.edu/python/2022/psets/1/bank/
__author__ = "Wilro - https://github.com/SciWilro"


def main():
    answer = format_answer(input("Greeting?: "))

    if answer.startswith("hello"):
        print("$0")
    elif answer.startswith("h"):
        print("$20")
    else:
        print("$100")


def format_answer(input: str) -> str:
    return input.strip().lower()


main()

# bank.py prompts user for a greeting.
# If string starts with “hello”, output $0.
# If string starts with an “h” (but not “hello”), output $20.
# Else, output $100.
# ignore whitespace and treat case-insensitively.
