def is_valid(s):
    # Rule 1: Length must be between 2 and 6
    if not (2 <= len(s) <= 6):
        return False

    # Rule 2: Must start with at least two letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Rule 3: Must be alphanumeric
    if not s.isalnum():
        return False

    # Rule 4: Numbers must come at the end
    number_started = False
    for char in s:
        if char.isdigit():
            if not number_started:
                # First number cannot be zero
                if char == "0":
                    return False
                number_started = True
        else:
            if number_started:
                return False

    return True


plate = input("Plate: ")

if is_valid(plate):
    print("Valid")
else:
    print("Invalid")

