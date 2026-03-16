def main():
    month_names = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    while True:
        date = input("Date: ")

        # Try numeric format M/D/YYYY
        if "/" in date:
            try:
                month, day, year = date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)

                if 1 <= month <= 12 and 1 <= day <= 31:
                    break
            except ValueError:
                continue

        # Try written format Month Day, Year
        elif "," in date:
            try:
                date = date.replace(",", "")
                parts = date.split()  # <-- FIXED
                month_str, day, year = parts  # <-- SAFE NOW

                if month_str in month_names:
                    month = month_names.index(month_str) + 1
                    day = int(day)
                    year = int(year)

                    if 1 <= month <= 12 and 1 <= day <= 31:
                        break
            except ValueError:
                continue

    print(f"{year}-{month:02}-{day:02}")


if __name__ == "__main__":
    main()
