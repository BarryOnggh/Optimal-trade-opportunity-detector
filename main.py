import pandas as pd
from kline_obtainer import get_binance_klines
from datetime import datetime, timezone

#data for running program
symbol = 'AAVEUSDT'
interval = '1h'
start_time = datetime(2024, 6, 1, tzinfo=timezone.utc)
end_time = datetime(2024, 6, 2, tzinfo=timezone.utc) 

data = get_binance_klines(symbol, interval, start_time, end_time)
print(data)
#print(data.head())


#pandas stuff
high = data["high"]
low = data["low"]
close = data["close"]

# Find the rolling maximum and minimum for the high and low prices
rolling_max = high.rolling(24).max().mean()
rolling_min = low.rolling(24).min().mean()

# Identify the support levels as the rolling minimum
support = rolling_min

# Identify the resistance levels as the rolling maximum
resistance = rolling_max

# Print the support and resistance levels
print("Support levels:", support)
print("Resistance levels:", resistance)