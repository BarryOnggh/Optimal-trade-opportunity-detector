import pandas as pd
import numpy as np
import requests
import json
from datetime import datetime, timezone

#convert yy/mm/dd to epoch time
def to_milliseconds(dt):
    epoch = datetime(1970, 1, 1, tzinfo=timezone.utc)
    return int((dt - epoch).total_seconds() * 1000.0)

#pull data from api
def get_binance_klines(symbol, interval, start_time, end_time):
    start_time_ms = to_milliseconds(start_time)
    end_time_ms = to_milliseconds(end_time)
    url = f"https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&startTime={start_time_ms}&endTime={end_time_ms}"
    response = requests.get(url)
    data = json.loads(response.text)
    df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 
                                     'close_time', 'quote_asset_volume', 'number_of_trades', 
                                     'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    df = df[['open', 'high', 'low', 'close', 'volume']].astype(float)
    return df

#prevent top level code from being executed
if __name__ == "__main__":
    # Example usage
    symbol = 'CAKEUSDT'
    interval = '1h'
    start_time = datetime(2024, 6, 1, tzinfo=timezone.utc)
    end_time = datetime(2024, 6, 2, tzinfo=timezone.utc)  


    data = get_binance_klines(symbol, interval, start_time, end_time)
    print(data.head())
