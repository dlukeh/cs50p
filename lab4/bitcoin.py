import sys
import requests


def main():
    # 1. Validate command-line argument count
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    # 2. Validate that argument is a float
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # 3. Query CoinCap API (public endpoint, no API key)
    url = "https://api.coincap.io/v3/assets/bitcoin"

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        sys.exit("Request error")

    # 4. Parse JSON
    data = response.json()
    price = float(data["data"]["priceUsd"])

    # 5. Compute cost
    cost = n * price

    # 6. Print formatted result
    print(f"${cost:,.4f}")


if __name__ == "__main__":
    main()
