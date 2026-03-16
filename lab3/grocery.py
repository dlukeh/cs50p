def main():
    grocery = {}
    # Continuously prompt until EOF is reached
    while True:
        item = get_item()
        if item is None:
            print()
            break

        if item in grocery:
            grocery[item] += 1
        else:
            grocery[item] = 1
    # Print items and their counts in sorted order
    for item in sorted(grocery.keys()):
        print(grocery[item], item)


def get_item():
    try:
        return input().upper()
    except EOFError:
        return None


if __name__ == "__main__":
    main()
