def main():
    # Menu of items and prices
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }

    total = 0
    # Continuously prompt until EOF is reached
    while True:
        item = get_item()
        if item is None:
            print()
            break
        # add price to total if item is in menu
        if item in menu:
            total += menu[item]
            print(f"Total: ${total:.2f}")


def get_item():
    try:
        return input("Item: ").title()
    except EOFError:
        return None


if __name__ == "__main__":
    main()
