def main():
    answer = input("What is the answer to the Great Question of Life, the Universe, and Everything? ")

    # Normalize
    normalized = answer.strip().lower().replace("-", " ")

    # Collapse multiple spaces into one
    normalized = " ".join(normalized.split())

    if normalized in ["42", "forty two"]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
