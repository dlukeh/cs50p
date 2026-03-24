import sys
import csv
from tabulate import tabulate


# Entry point: validate arguments, then render the CSV as a table
def main():
    filename = check_args(sys.argv)
    print_table(filename)


# Validate command-line usage and ensure a .csv file was provided
def check_args(argv):
    if len(argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = argv[1]

    # Enforce CSV file extension
    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    return filename


# Read the CSV and display it as an ASCII table using tabulate
def print_table(filename):
    try:
        with open(filename) as file:
            reader = csv.DictReader(file)
            table = tabulate(reader, headers="keys", tablefmt="grid")
            print(table)
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
