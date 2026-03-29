import re


def main():
    print(parse(input("HTML: ")))


def parse(s: str) -> str | None:
    """
    Extract a YouTube video ID from an iframe embed HTML string
    and return the corresponding shortened youtu.be URL.
    """
    match = re.search(
        r'src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"', s
    )
    if match:
        return f"https://youtu.be/{match.group(1)}"
    return None


if __name__ == "__main__":
    main()
