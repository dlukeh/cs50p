import re


def main():
    print(parse(input("HTML: ")))


def parse(s: str) -> str | None:
    """
    Extract a YouTube video ID from an iframe's src attribute
    and return the corresponding youtu.be short link.
    """
    match = re.search(
        r'<iframe[^>]*src="https?://(?:www\.)?youtube\.com/embed/([\w-]+)"',
        s,
        re.IGNORECASE,
    )
    if match:
        return f"https://youtu.be/{match.group(1)}"
    return None


if __name__ == "__main__":
    main()
