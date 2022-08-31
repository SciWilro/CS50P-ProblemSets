# taqueria.py
# https://cs50.harvard.edu/python/2022/psets/3/taqueria/
__author__ = "Wilro - https://github.com/SciWilro"

Menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}


def main():
    cart_total = 0
    while True:
        try:
            item = input("Item: ").strip().title()
        except EOFError:
            break
        if item in Menu:
            try:
                cart_total += Menu[item]
                print(f"${cart_total:.2f}")
            except KeyError:
                continue


main()
