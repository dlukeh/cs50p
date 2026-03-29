import re


def main():
    print(convert(input("Hours: ")))


def convert(s: str) -> str:
    """
    Convert a 12-hour time range like '9 AM to 5 PM'
    into a 24-hour format like '09:00 to 17:00'.
    Raises ValueError for invalid formats or values.
    """
    time = re.search(
        r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$",
        s,
    )
    if time:
        start_hour = int(time.group(1))
        start_minute = int(time.group(2) or 0)
        start_period = time.group(3)

        end_hour = int(time.group(4))
        end_minute = int(time.group(5) or 0)
        end_period = time.group(6)

        # Validate minutes
        if start_minute > 59 or end_minute > 59:
            raise ValueError

        # Validate hours
        if not (1 <= start_hour <= 12 and 1 <= end_hour <= 12):
            raise ValueError

        # Convert start time
        if start_period == "PM" and start_hour != 12:
            start_hour += 12
        elif start_period == "AM" and start_hour == 12:
            start_hour = 0

        # Convert end time
        if end_period == "PM" and end_hour != 12:
            end_hour += 12
        elif end_period == "AM" and end_hour == 12:
            end_hour = 0

        return f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}"

    raise ValueError


if __name__ == "__main__":
    main()
