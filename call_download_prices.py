import os
from datetime import datetime
from download_prices import download_prices

path = 'Q://STONKS//downloads//'

period = 6 # years

end = datetime.now().date()
start = datetime(end.year - 5, end.month, end.day).date()

tickers = ['CTVA'] 

for t in tickers:
    if not os.path.exists(path + t):
        os.mkdir(path + t)
    download_prices(t, path, start, end)
