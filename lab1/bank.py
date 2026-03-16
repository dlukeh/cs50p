def main():
    # Prompt the user for a greeting and normalize it
    # strip() removes surrounding spaces; lower() ensures case-insensitive comparison
    greeting = input("Greeting: ").strip().lower()

    # If the greeting starts with "hello", reward is $0
    if greeting.startswith("hello"):
        print("$0")

    # If it starts with 'h' (e.g., "hi", "hey"), reward is $20
    elif greeting.startswith("h"):
        print("$20")

    # Otherwise (no 'hello' or 'h' prefix), reward is $100
    else:
        print("$100")


# Run main() only when the file is executed directly
if __name__ == "__main__":
    main()
