import re


def validate(ip: str) -> bool:
    """
    Validate an IPv4 address.
    Returns True if ip is in the form X.X.X.X where each X is 0–255.
    """
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)\.(\d+)", ip)
    if not match:
        return False

    for octet in match.groups():
        if not 0 <= int(octet) <= 255:
            return False

    return True


def main():
    print(validate(input("IPv4 Address: ")))


if __name__ == "__main__":
    main()
