# prompts the user for the answer to the Great Question of Life, the Universe and Everything,
# outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two.
# Otherwise output No.


__author__ = "Wilro - https://github.com/SciWilro"


def main():
    answer = input("Answer to the Great Question of Life, the Universe and Everything?")
    isAnswer(answer)


def isAnswer(input):
    match format_answer(input):
        case "42" | "forty two" | "forty-two":
            print("Yes")
        case _:
            print("No")


def format_answer(input: str) -> str:
    return input.strip().lower()


main()
