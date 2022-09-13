import requests
import sys
import json

# https://api.coindesk.com/v1/bpi/currentprice.json

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
else:
    req = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    # print(json.dumps(req.json(), indent=2))
    try:
        float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    data = req.json()
    # # print(data)
    price = data["bpi"]["USD"]["rate"]
    # print(price)
    price = price.replace(",", "")
    print(f"${float(price) * float(sys.argv[1]):,.4f}")