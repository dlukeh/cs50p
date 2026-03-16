def main():
    word = input("Input: ")
    print(shorten(word))


def shorten(word):
    result = ""
    for ch in word:
        if ch.lower() not in "aeiou":
            result += ch
    return result


if __name__ == "__main__":
    main()
