__author__ = "Wilro - https://github.com/SciWilro"

"""
get_calories(fruit):
Takes fruit name (case-insensitive) as input and gives amount of calories in 1 portion.
Data from FDA poster: [link](https://www.fda.gov/food/food-labeling-nutrition/raw-fruits-poster-text-version-accessible-version)
    Args:
        fruit (str): Name of fruit
    Returns:
        int: Amount of calories in one portion
"""

fruit_data = {
    "Apple": 130,
    "Avocado": 50,
    "Banana": 110,
    "Cantaloupe": 50,
    "Grapefruit": 60,
    "Grapes": 90,
    "Honeydew Melon": 50,
    "Kiwifruit": 90,
    "Lemon": 15,
    "Lime": 20,
    "Nectarine": 60,
    "Orange": 80,
    "Peach": 60,
    "Pear": 100,
    "Pineapple": 50,
    "Plums": 70,
    "Strawberries": 50,
    "Sweet Cherries": 100,
    "Tangerine": 50,
    "Watermelon": 80,
}


def main():
    usr_input = input("Item: ").strip().title()
    if usr_input in fruit_data:
        print("Calories: ", get_calories(usr_input))


def get_calories(fruit):
    return fruit_data[fruit]


if __name__ == "__main__":
    main()
