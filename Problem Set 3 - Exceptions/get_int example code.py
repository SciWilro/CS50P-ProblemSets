# Example of a function that returns an int using try except blocks
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt)
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()
