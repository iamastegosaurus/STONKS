import os
import pandas as pd
from datetime import datetime
from download_prices import download_prices
from download_financials import download_financials
from create_template import create_template

path = 'Q://STONKS//downloads//'

period = 6 # years

end = datetime.now().date()
start = datetime(end.year - 5, end.month, end.day).date()

tickers = ['AMD']

for t in tickers:
    if not os.path.exists(path + t):
        os.mkdir(path + t)
    # download_prices(t, path, start, end)


download_financials(tickers, path, start, end)

for t in tickers:
    create_template(path, t)
