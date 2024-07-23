import requests
import json
#Binance API
base_url = 'https://api.binance.com'
endpoint = '/api/v3/klines'

# Define parameters
params = {
    'symbol': 'BTCUSDT',   # Trading pair symbol
    'interval': '1h',      # Interval (e.g., '1m', '5m', '1h', '1d')
    'limit': 10          # Number of data points (optional, default 500, max 1000)
}

# Make the request
response = requests.get(base_url + endpoint, params=params)

# Check the status code and print data if successful
if response.status_code == 200:
    klines_data = response.json()
    print(json.dumps(klines_data, indent=2))
else:
    print(f"Error: {response.status_code} - {response.text}")
