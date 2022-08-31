__author__ = "Wilro - https://github.com/SciWilro"

# prompts for variable name in camel case
# outputs name in snake case
# Assume that the user’s input will indeed be in camel case.
# str methods doc: https://docs.python.org/3/library/stdtypes.html#string-methods
# Eg
# camelCase: preferredFirstName
# snake_case: preferred_first_name


def main():
    usr_input = input("camelCase: ")
    snake_case = convertCamelToSnake(usr_input)
    print("snake_case: " + snake_case)


def convertCamelToSnake(camel):
    """Uses list methods - Regex would probably be better though"""
    snake = [""]
    for s in camel:
        if s.isupper():
            snake.append("_")
            snake.append(s.lower())
        else:
            snake.append(s)
    return "".join(snake)


def convertCamelToSnakeShort(camel):
    """Still using list methods - But as one liner"""
    return "".join(["_" + camel.lower() if camel.isupper() else s for s in camel])


main()
