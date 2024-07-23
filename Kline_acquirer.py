import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging
from datetime import datetime, timezone

config_logging(logging, logging.DEBUG)

spot_client = Client(base_url="https://data-api.binance.vision")

def to_milliseconds(dt):
    epoch = datetime(1970, 1, 1, tzinfo=timezone.utc)
    return int((dt - epoch).total_seconds() * 1000.0)

start_time = datetime(2023, 6, 1, tzinfo=timezone.utc)
end_time = datetime(2023, 6, 30, 23, 59, 59, tzinfo=timezone.utc)

start_time_ms = to_milliseconds(start_time)
end_time_ms = to_milliseconds(end_time)

all_klines = []
current_start_time = start_time_ms

while current_start_time < end_time_ms:
    klines = spot_client.klines("BTCUSDT", "1h", startTime=current_start_time, endTime=end_time_ms, limit=1000)
    if not klines:
        break
    all_klines.extend(klines)
    current_start_time = klines[-1][6] + 1  # Use the close time of the last K-line as the new start time


logging.info(all_klines)
#returns klines between time duration as a list