from datetime import date
import re
import sys
import inflect

p = inflect.engine()


def main():
    birth_date = input("Enter your birth date (YYYY-MM-DD): ")
    try:
        year, month, day = check_birthday(birth_date)
    except:
        sys.exit("Invalid Date")

    date_of_birth = date(int(year), int(month), int(day))
    today = date.today()
    total_days = (today - date_of_birth).days
    total_minutes = total_days * 24 * 60
    final_output = p.number_to_words(total_minutes, andword="")
    print(final_output.capitalize() + " minutes")


def check_birthday(birth_date):
    if re.search(r"^\d{4}-\d{2}-\d{2}$", birth_date):
        year, month, day = birth_date.split("-")
        return year, month, day


if __name__ == "__main__":
    main()
