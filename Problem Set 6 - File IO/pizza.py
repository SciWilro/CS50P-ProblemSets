__author__ = "Wilro - https://github.com/SciWilro"
"""pizza.py
Takes on command-line arg of the path to Pinocchio’s format and outputs table formated as ASCII art using tabulate PyPI format:
    sys.argv[1] (str): path to csv file
Output:
    Prints: Table formatted with tabulate package
"""
import sys
from tabulate import tabulate
def main():
    if len(sys.argv) != 2:
        sys.exit("Expects 1 command-line arguement")
    if sys.argv[1][-4::] != ".csv":
        sys.exit("Not a csv File")
    try:
        table = get_csv_table(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File not found")

    print(tabulate(table, headers = "firstrow"))

def get_csv_table(filename):
    '''
    Import csv file, split 3 columns and return list of lists of columns
    '''
    table = []
    with open(filename) as file:
        for line in file:
            a, b, c = line.rstrip().split(",")
            table.append([a,b,c])
    return table


if __name__ == "__main__":
    main()