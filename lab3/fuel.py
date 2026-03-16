def main():
    fraction = get_fraction()
    percentage = round(fraction * 100)

    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")


def get_fraction():
    while True:
        num = input("Fraction: ")
        try:
            x, y = num.split("/")
            x = int(x)
            y = int(y)

            if y == 0:
                continue
            if x > y:
                continue
            if x < 0 or y < 0:
                continue
            return x / y

        except (ValueError, ZeroDivisionError):
            continue


if __name__ == "__main__":
    main()
