import csv
import sys


def main():
    """Entry point: validate arguments and convert the CSV."""
    input_file, output_file = check_args(sys.argv)
    convert(input_file, output_file)


def check_args(argv):
    """Validate command-line arguments and return input/output filenames."""
    # Must have exactly 2 arguments after the script name
    if len(argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = argv[1]
    output_file = argv[2]

    return input_file, output_file


def convert(input_file, output_file):
    """Read the input CSV, split names, and write cleaned output."""
    try:
        with open(input_file, newline="") as file_input:
            reader = csv.DictReader(file_input)

            with open(output_file, "w", newline="") as file_output:
                writer = csv.DictWriter(
                    file_output, fieldnames=["first", "last", "house"]
                )
                writer.writeheader()

                for row in reader:
                    last, first = row["name"].split(", ")
                    writer.writerow(
                        {"first": first, "last": last, "house": row["house"]}
                    )

    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")


if __name__ == "__main__":
    main()
