__author__ = 'Wilro - https://github.com/SciWilro'
'''_summary_
Takes user working times in [12 hour clock](https://en.wikipedia.org/wiki/12-hour_clock) format
Returns the [24 hour clock](https://en.wikipedia.org/wiki/24-hour_clock) format.
E.g.
    Input: 09:00 AM to 5:00 PM
    Input: 9 AM to 5 PM
    
    Output: 09:00 to 17:00 
'''

# Regex - extract `from`, `AM`/`PM` and `to`, `AM`/`PM` - (9 AM and 09:00 AM)

# Raise a ValueError instead if the input to convert is not in either of those formats
# or if either time is invalid (e.g., 12:60 AM, 13:00 PM
# Could just catch None from function and set up good regex instead of if statements


# Break into hrs and min (if ':' is present) otherwise min = 00

# Depending on AM or PM convert (special case for 12 AM and 12 PM)
# AM will mostly stay the same (adding 0 if < 10) + 12AM -> 00
# PM will add 12 to int + 12 PM -> 12

# Print output