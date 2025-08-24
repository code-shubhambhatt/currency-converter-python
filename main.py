from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://api.freecurrencyapi.com/"
API_KEY = "fca_live_dvxhZ9Q3nE0x0gFbjMyor3GEDUyaI6eYTEBxcH3T"

printer = PrettyPrinter()


def get_currencies():
    endpoint = f"v1/currencies?apikey={API_KEY}"
    url = BASE_URL + endpoint
    response = get(url).json()

    data = response["data"]   # new API returns "data"
    data = list(data.items())
    data.sort()

    return data


def print_currencies(currencies):
    for code, currency in currencies:
        name = currency['name']
        symbol = currency.get("symbol", "")
        print(f"{code} - {name} - {symbol}")


def exchange_rate(currency1, currency2):
    endpoint = f"v1/latest?apikey={API_KEY}&base_currency={currency1}"
    url = BASE_URL + endpoint
    response = get(url).json()

    data = response.get("data", {})

    if currency2 not in data:
        print("Invalid currencies.")
        return None

    rate = data[currency2]
    print(f"{currency1} -> {currency2} = {rate}")

    return rate


def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return

    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount.")
        return

    converted_amount = rate * amount
    print(f"{amount} {currency1} is equal to {converted_amount} {currency2}")
    return converted_amount


def main():
    currencies = get_currencies()

    print("Welcome to the currency converter!")
    print("List - lists the different currencies")
    print("Convert - convert from one currency to another")
    print("Rate - get the exchange rate of two currencies")
    print()

    while True:
        command = input("Enter a command (q to quit): ").lower()

        if command == "q":
            break
        elif command == "list":
            print_currencies(currencies)
        elif command == "convert":
            currency1 = input("Enter a base currency: ").upper()
            amount = input(f"Enter an amount in {currency1}: ")
            currency2 = input("Enter a currency to convert to: ").upper()
            convert(currency1, currency2, amount)
        elif command == "rate":
            currency1 = input("Enter a base currency: ").upper()
            currency2 = input("Enter a currency to convert to: ").upper()
            exchange_rate(currency1, currency2)
        else:
            print("Unrecognized command!")


if __name__ == "__main__":
    main()
