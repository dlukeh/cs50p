def convert(fraction):
    try:

        if "-" in fraction:
            raise ValueError

        x, y = fraction.split("/")
        x = int(x)
        y = int(y)

        if x < 0 or y < 0:
            raise ValueError

        if y == 0:
            raise ZeroDivisionError

        if x > y:
            raise ValueError

        return round((x / y) * 100)

    except ValueError:
        raise ValueError
