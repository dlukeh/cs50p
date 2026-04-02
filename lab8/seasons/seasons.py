from datetime import date
import sys
import inflect

p = inflect.engine()


def main():
    # 1. Get validated date object from our helper
    dob = get_date(input("Enter your birth date (YYYY-MM-DD): "))

    # 2. Use the subtraction operator (-)
    # This creates a 'timedelta' object automatically
    today = date.today()
    delta = today - dob

    # 3. Access the .days attribute of the delta object
    minutes = delta.days * 24 * 60

    # 4. Pass to our word converter
    print(format_words(minutes))


def get_date(s):
    try:
        return date.fromisoformat(s)
    except ValueError:
        sys.exit("Invalid date")


def format_words(n):
    words = p.number_to_words(n, andword="")
    # Clean up 'and', capitalize, and append 'minutes'
    return f"{words.capitalize()} minutes"


if __name__ == "__main__":
    main()
