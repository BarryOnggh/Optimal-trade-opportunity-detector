from kline_obtainer import get_binance_klines
from datetime import datetime, timezone
import pandas as pd
import numpy as np
from scipy.signal import argrelextrema

#data for running program
symbol = 'AAVEUSDT'
interval = '1h'
start_time = datetime(2024, 6, 1, tzinfo=timezone.utc)
end_time = datetime(2024, 6, 2, tzinfo=timezone.utc) 

data = get_binance_klines(symbol, interval, start_time, end_time)

#find maxima and minima(maximum and minimum point)

data['Min'] = data['low'][argrelextrema(data['low'].values, np.less_equal, order=5)[0]]
data['Max'] = data['high'][argrelextrema(data['high'].values, np.greater_equal, order=5)[0]]

#removing null values
support = data['Min'].dropna().values
resistance = data['Max'].dropna().values

# Group into zones 
buffer_percentage = 0.02
support_zones = [(level * (1 - buffer_percentage), level * (1 + buffer_percentage)) for level in support]
resistance_zones = [(level * (1 - buffer_percentage), level * (1 + buffer_percentage)) for level in resistance]

print(support_zones)