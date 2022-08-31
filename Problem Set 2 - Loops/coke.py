__author__ = "Wilro - https://github.com/SciWilro"

# Prompt user for coin (5, 10, 25)
# After prompt display amount still owed
# After reaching 50c - Display change due

valid_coins = ["5", "10", "25"]


def main():
    usr_total = 0
    while True:
        usr_input = input("Insert Coin: ")

        if isValidCoin(usr_input):
            usr_total += int(usr_input)
            # print("Total:", usr_total)

        if usr_total >= 50:
            print("Change Owed: ", (usr_total - 50))
            break
        else:
            print("Amount Due: ", (50 - usr_total))


def isValidCoin(coin):
    return coin in valid_coins


main()
