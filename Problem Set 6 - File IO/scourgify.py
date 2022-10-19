__author__ = 'Wilro - https://github.com/SciWilro'
'''_summary_
Commandline program that reads 2 column `csv` file and exports it to 3 column csv, after splitting and switching first column
    Args:
        argv[1]: name of existing csv file
        argv[2]: name of new csv file to write to
'''

import sys
import csv

def open_csv(filename: str, students: list):
    with open(filename, "r", newline="") as file:
        for row in csv.DictReader(file):
            students.append({"name": row["name"], "house": row["house"]})

def write_csv(filename: str, students: list):
    with open(filename, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"], lineterminator="\n")
        # Specify lineterminator for windows otherwise you get double newlines (empty rows between data rows)
        writer.writeheader()
        for _ in students:
            writer.writerow({"first": _["name"].split(',')[1].strip(), "last": _["name"].split(',')[0].strip(), "house": _["house"]})


def main():
    
    students = []
    if len(sys.argv) != 3:
        sys.exit("Program expects 2 cmdline arguments")
    try:
        open_csv(sys.argv[1], students)
    except FileNotFoundError:
        sys.exit("File Not Found")
    
    write_csv(sys.argv[2], students)
    
if __name__ == '__main__':
    main()
