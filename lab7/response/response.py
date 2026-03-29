from validator_collection import checkers


def main():
    email = input("What's your email address? ")
    print("Valid" if checkers.is_email(email) else "Invalid")


if __name__ == "__main__":
    main()
