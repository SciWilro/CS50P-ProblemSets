# grocery.py
# https://cs50.harvard.edu/python/2022/psets/3/grocery/
__author__ = "Wilro - https://github.com/SciWilro"

# prompts user for items, one per line, until user inputs control-d (EOFError)
# output grocery list
#     all uppercase
#     sorted alphabetically by item,
#     prefixing each line with the number of times user inputted that item

GroceryList = {}


def main():
    while True:
        try:
            item = input()
            # if item == "q":
            #     break
            add_item(item)
        except EOFError:
            break
    display_items(sort_items(GroceryList))  # List of sorted keys


def add_item(item):
    item = item.strip().upper()
    try:  # worse alternative? if item in GroceryList:
        GroceryList[item] += 1
    except KeyError:
        GroceryList[item] = 1


def display_items(sorted_item_list):
    for _ in sorted_item_list:
        print(f"{GroceryList[_]} {_}")


def sort_items(GroceryList):
    return sorted(GroceryList.keys())


main()
