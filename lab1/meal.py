def convert(time):
    # Split HH:MM into hours and minutes
    hours, minutes = time.split(":")

    # Convert to float hours (e.g., "7:30" → 7.5)
    return int(hours) + int(minutes) / 60


def main():
    # Prompt user for the current time
    time = input("What time is it? ")

    # Convert input to a float representing hours
    t = convert(time)

    # Check meal ranges
    if 7 <= t <= 8:
        # Between 7:00 and 8:00
        print("breakfast time")
    elif 12 <= t <= 13:
        # Between 12:00 and 13:00
        print("lunch time")
    elif 18 <= t <= 19:
        # Between 18:00 and 19:00
        print("dinner time")


if __name__ == "__main__":
    main()
