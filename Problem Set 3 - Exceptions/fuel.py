# Fuel.py
# https://cs50.harvard.edu/python/2022/psets/3/fuel/
__author__ = "Wilro - https://github.com/SciWilro"

# prompts user for fraction, formt = X/Y
# x & y are ints
# If not ints, x > y, or y = 0 -> prompt again
# catch any exceptions like ValueError or ZeroDivisionError
# outputs:
# percentage rounded integer
# If, <= 1% output E
# If >= 99%, output F


def main():
    # Get valid input
    valid_input = get_valid_input()
    # Get and Display Fuel Value
    temp = get_fuel_ratio(valid_input)
    print(display_fuel_value(temp))


def get_valid_input() -> str:
    while True:
        usr_input = input("Fraction?: ")
        if is_valid(usr_input):
            return usr_input


def get_fuel_ratio(fuel_value: str):
    x, y = fuel_value.strip().split("/")
    return round((float(x) / float(y)) * 100, 0)


def display_fuel_value(fuel_value):
    fuel_value = int(fuel_value)
    if 0 <= fuel_value <= 1:
        return "E"
    if 1 < fuel_value < 99:
        return str(round(fuel_value, 0)) + "%"
    if 99 <= fuel_value <= 100:
        return "F"
    return fuel_value


def is_valid(usr_input: str):
    try:
        x, y = usr_input.strip().split("/")
        if int(x) <= int(y):
            return True
        else:
            return False
    except (ValueError, ZeroDivisionError):
        return False


main()
