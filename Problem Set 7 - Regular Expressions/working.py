__author__ = 'Wilro - https://github.com/SciWilro'
'''_summary_
Takes user working times in [12 hour clock](https://en.wikipedia.org/wiki/12-hour_clock) format
Returns the [24 hour clock](https://en.wikipedia.org/wiki/24-hour_clock) format.
E.g.
    Input: 09:00 AM to 5:00 PM
    Input: 9 AM to 5 PM

    Output: 09:00 to 17:00
'''

import re

def main():
    print(convert(input("Hours: ")))

# --------------------------------------------------------------------------- #

def convert(input: str) -> str:
    pattern = r"^(0?[1-9]|1[0-2]):?([0-5][0-9])? (AM|PM) to (0?[1-9]|1[0-2]):?([0-5][0-9])? (AM|PM)"
    matches = re.search(pattern, string = input)

    # Initial regex tests - Valid Time
    if matches == None:
        raise ValueError

    # Get meridian format - AM|PM
    frmt1 = matches.group(3)
    frmt2 = matches.group(6)

    # Convert hours
    hours1 = convert_hour(hour = matches.group(1), format = frmt1)
    hours2 = convert_hour(hour = matches.group(4), format = frmt2)

    # Set minutes to zero if not found
    mins1 = matches.group(2) if matches.group(2) else "00"
    mins2 = matches.group(5) if matches.group(5) else "00"

    return f"{hours1}:{mins1} to {hours2}:{mins2}"

# --------------------------------------------------------------------------- #

def convert_hour(hour: str, format: str) -> str:
    if hour == "12" and format == "AM":
        return "00"
    elif int(hour) < 12 and format == "PM":
        return str(int(hour) + 12)
    elif int(hour) < 10 and format == "AM":
        return f"0{hour}"
    else:
        return hour

# --------------------------------------------------------------------------- #

if __name__ == '__main__':
    main()




# --------------------------------------------------------------------------- #
# Pseudocode
# --------------------------------------------------------------------------- #

# Raise a ValueError instead if the input to convert is not in either of those formats
# or if either time is invalid (e.g., 12:60 AM, 13:00 PM
# Could just catch None from function and set up good regex instead of if statements

# Regex - extract `hours`, `mins`, `AM`/`PM` and `hours`, `mins`, `AM`/`PM` - (9 AM and 09:00 AM)

# If no mins found in matches min = 00

# Depending on AM or PM convert (special case for 12 AM and 12 PM)
# AM will get leading zero if < 10 & 12AM -> 00
# PM will add 12 to int & 12 PM -> 12

# Print output by concatenating vars