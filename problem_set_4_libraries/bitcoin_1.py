import sys
import requests
import json

# get values from the command line
# check for cl arg
if len(sys.argv) == 2:
    try:
        value = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
else:
    print("Missing command-line argument")
    # exit with error exit code
    sys.exit(1)

try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    # print(r) # <Response [200]> - Need to convert to dict
    response = r.json()  # converts to json
    # print(response) # get a dictionary back
    # print(response["bpi"])
    # print(response["bpi"]["USD"])
    # print(response["bpi"]["USD"]["rate_float"]) # 1 bitcoin = 20153.7522 dollars
    bitcoin = response["bpi"]["USD"]["rate_float"]
    total = bitcoin * value
    print(f"${total:,.4f}")
except requests.RequestException:
    print("Request Exception")
