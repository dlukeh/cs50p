import re


def main():
    print(validate(input("IPv4 Address: ")))


import re


def validate(ip):
    if match := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        for octet in match.groups():
            if not 0 <= int(octet) <= 255:
                return False
        return True
    return False


if __name__ == "__main__":
    main()
