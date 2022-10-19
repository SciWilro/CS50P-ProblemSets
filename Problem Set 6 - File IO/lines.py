__author__ = "Wilro - https://github.com/SciWilro"
"""Lines of Code
Program expects one arguement of a python file and counts number of lines of code, excluding comments and blank lines
Cmdline Arg:
    sys.argv[1] (str): Python filename
Output:
    Prints: number of lines of code excluding comments and whitespace (int)
"""
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Expects 1 command-line arguments")
    if sys.argv[1][-3::] != ".py":
        sys.exit("Not a Python File")
    try:
        print(count_lines(sys.argv[1]))
    except FileNotFoundError:
        sys.exit("File not found")

def count_lines(filename):
    counter = 0
    with open(filename, "r") as file:
        file_lines = file.readlines()
        for line in file_lines:
            if line.strip().startswith("#") is True or line.rstrip() == "":
                # Using strip() to remove indentation before comment
                pass 
            else:
                counter += 1
    return counter


if __name__ == "__main__":
    main()