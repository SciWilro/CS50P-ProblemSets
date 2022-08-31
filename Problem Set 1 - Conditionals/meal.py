# Meal Time
# https://cs50.harvard.edu/python/2022/psets/1/meal/
__author__ = "Wilro - https://github.com/SciWilro"


def main():
    usr_input = input("Time?: ")
    time_value = convert(usr_input)
    convert(usr_input)  # Test

    if 7 <= time_value <= 8:
        print("breakfast time")
    if 12 <= time_value <= 13:
        print("lunch time")
    if 18 <= time_value <= 19:
        print("dinner time")


def convert(time: str) -> float:
    hours, mins = time.split(":")
    return float(hours) + (float(mins)) / 60


main()
