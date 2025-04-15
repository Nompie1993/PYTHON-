import requests

# Fetch data from a public API
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json')

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    # Print a key piece of information
    print(f"Current Bitcoin price in USD: {data['bpi']['USD']['rate']}")
else:
    print("Failed to fetch data from the API.")