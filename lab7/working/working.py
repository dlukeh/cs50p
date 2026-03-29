import re
import sys


def main():
    """Run the converter interactively and handle invalid input gracefully."""
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        print("Invalid input")
        sys.exit(1)


def convert(s: str) -> str:
    """
    Convert a 12-hour time range (e.g., '9 AM to 5 PM')
    into 24-hour format (e.g., '09:00 to 17:00').

    Raises:
        ValueError: If the input format or time values are invalid.
    """
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.match(pattern, s)
    if not match:
        raise ValueError

    h1, m1, p1, h2, m2, p2 = match.groups()

    # Default missing minutes to "00"
    m1 = m1 or "00"
    m2 = m2 or "00"

    # Validate minute ranges
    if not (0 <= int(m1) < 60 and 0 <= int(m2) < 60):
        raise ValueError

    # Convert hours to 24-hour format
    h1 = convert_hour(int(h1), p1)
    h2 = convert_hour(int(h2), p2)

    return f"{h1}:{m1} to {h2}:{m2}"


def convert_hour(hour: int, period: str) -> str:
    """Convert a single 12-hour clock hour into 24-hour format."""
    if not 1 <= hour <= 12:
        raise ValueError

    if period == "AM":
        hour = 0 if hour == 12 else hour
    else:
        hour = 12 if hour == 12 else hour + 12

    return f"{hour:02}"


if __name__ == "__main__":
    main()
