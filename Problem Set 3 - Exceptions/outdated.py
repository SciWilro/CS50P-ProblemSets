# outdated.py
# https://cs50.harvard.edu/python/2022/psets/3/outdated/
__author__ = "Wilro - https://github.com/SciWilro"

# prompt for date
# Input format: 9/8/1636 OR September 8, 1636
# Output format: year-month-day (YYYY-MM-DD) each with leading zeroes as needed


months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main():
    while True:
        usr_date = input("Date: ").strip()
        # usr_date = "September 8, 1636"
        # usr_date = "9/8/1636"
        # usr_date = "9/8/1636"

        if is_valid_date(usr_date):
            y, m, d = convert_date(usr_date)
            y = int(y)
            m = int(m)
            d = int(d)
            print(f"{y}-{m:02}-{d:02}")
            break


def is_valid_date(usr_date):
    try:
        if usr_date.split(" ")[0].title() in months and 32 > int(
            usr_date.split(" ")[1][:-1]
        ):
            return True
        elif int(usr_date.split("/")[0]) < 13 and int(usr_date.split("/")[1]) < 32:
            return True
        else:
            return False

    except ValueError:
        return False
    except IndexError:
        return False


def convert_date(usr_date: str) -> int:
    if "/" in usr_date:
        m, d, y = usr_date.split("/")
        return y, m, d
    elif "," in usr_date:
        y = int(usr_date.split(", ")[1])
        m = int(months.index(usr_date.split(" ")[0].title()) + 1)
        d = int(usr_date.replace(",", "").split(" ")[1])
        return y, m, d


main()
