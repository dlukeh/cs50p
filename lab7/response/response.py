from validator_collection import checkers

"""
Uses validator-collection. Prompts the user for an email address via input 
and then prints Valid or Invalid, respectively,
"""


def main():
    email = input("What's your email address? ")
    print("Valid" if checkers.is_email(email) else "Invalid")


if __name__ == "__main__":
    main()
