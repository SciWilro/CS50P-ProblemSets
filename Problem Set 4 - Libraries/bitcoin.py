import sys

import requests


def main():
    if len(sys.argv) != 2:
        sys.exit("Expects 1 arguement")
    if args_check() is False:
        sys.exit("Command-line arguement is not a number")

    amount = float(sys.argv[1])
    # amount = float("1")
    token = "bpi"
    # try:
    price = get_price(token)
    total = amount * price
    print(f"${total:,.4f}")


def get_price(token: str):
    url = "https://api.coindesk.com/v1/" + token + "/currentprice.json"
    r = requests.get(url)
    # except requests.RequestException:
    # Or hard exit for now:
    if r.status_code is not requests.codes.ok:
        sys.exit("Error with API")
    return r.json()[token]["USD"]["rate_float"]


def args_check(args=sys.argv):
    try:
        float(sys.argv[1])
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    main()
