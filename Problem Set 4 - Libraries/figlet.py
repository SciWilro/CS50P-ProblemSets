"""cmdline program implementing the pyfiglet package  
Commandline Args:
    Optional:
    1] "-f" or "--font"
    2] fontname see [list](http://www.figlet.org/examples.html)
"""
__author__ = "Wilro - https://github.com/SciWilro"

import os
import random
import sys

# Install pyfiglet package if unable to import Figlet()
try:
    from pyfiglet import Figlet
except ImportError:
    os.system(f"pip install pyfiglet")
    from pyfiglet import Figlet

figlet = Figlet()


def main():

    # 0 args asks for text and prints random font
    if len(sys.argv) == 1:  # First argv element is filename
        usr_input = input("Input1:")
        figlet.setFont(font=random.choice(figlet.getFonts()))
        print("Output:\n", figlet.renderText(usr_input))

    # Two arguements: 1) '-f' or '--font'   2) Font name
    elif len(sys.argv) == 3:
        if check_args() == True:
            usr_input = input("Input2:")
            figlet.setFont(font=sys.argv[2])
            print("Output:\n", figlet.renderText(usr_input))
        else:
            sys.exit("Check Arguements")
    else:
        sys.exit("Program expects 0 or 2 args.")


def check_args(args=sys.argv):
    if args[1] == "-f" or args[1] == "--font":
        if args[2] in figlet.getFonts():
            return True
    # return [args[1] == "-f" or args[1] == "--font"] and [args[2] in figlet.getFonts()]


if __name__ == "__main__":
    main()
