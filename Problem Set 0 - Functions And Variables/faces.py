__author__ = "Wilro - https://github.com/SciWilro"


def main():
    user_string = input("Input string: ")
    print(convert(user_string))


def convert(input: str) -> str:
    # Probably best to use translate() - after creating dictionary
    return input.replace(":)", "🙂").replace(":(", "🙁")


main()
