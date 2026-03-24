import sys


# Entry point: validate arguments, then count lines of code
def main():
    filename = check_args(sys.argv)
    count_lines(filename)


# Validate command-line usage and ensure a .py file was provided
def check_args(argv):
    if len(argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = argv[1]

    # Enforce Python file extension
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    return filename


# Count non-blank, non-comment lines in the given file
def count_lines(filename):
    count = 0

    try:
        with open(filename) as file:
            for line in file:
                stripped_left = line.lstrip()

                # Skip full-line comments
                if stripped_left.startswith("#"):
                    continue

                # Skip blank or whitespace-only lines
                if stripped_left.strip() == "":
                    continue

                count += 1

        print(count)

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
