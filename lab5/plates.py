def main():
    plates = input("Plate: ")
    if is_valid(plates):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Rule 1: Length of 2 to 6 characters
    if not (2 <= len(s) <= 6):
        return False
    # Rule 2: First two characters must be letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    # Rule 3: Must be alphanumeric
    if not s.isalnum():
        return False
    # Rule 4: Numbers must come at the end
    numbers_started = False
    for char in s:
        if char.isdigit():
            if not numbers_started:
                # First number cannot be '0'
                if char == "0":
                    return False
                numbers_started = True
        else:
            if numbers_started:
                return False
    return True


if __name__ == "__main__":
    main()
