__author__ = 'Wilro - https://github.com/SciWilro'
'''_summary_
Program uses validator_collection library to print validity of an email address to the terminal
Input:
    email (str): asks user email
Output:
    prints (str): 'Invalid' or 'Valid'
'''

from validator_collection import validators

# email = "malan@harvard.edu"
# email = "malan@@@harvard.edu"
# email = "malan@harvard..edu"
def check_email(email: str) -> str:
    try:
        if validators.email(email):
            return "Valid"
    except:
        return "Invalid"


def main():
    print(check_email(input("Email: ")))
    # check_email(email)

    
if __name__ == '__main__':
    main()

