import os
from datetime import datetime
from download_financials import download_financials

path = 'Q://STONKS//downloads//'

startyear = 2017 # full pull
# startyear = 2022 # update recent

endyear = 2023

tickers = ['MMM','ABT','ABBV','ADM','AMCR','AMD','AAPL','ADSK','BLL','CAT','CSCO','C','CTVA','COST','DUK','DRE','EMR','EQIX','HON','INTC','MA','MCD','MU','MSFT','NUE','NVDA','ORCL','PYPL','PG','RTX','ROK','CRM','STX','SYY','TGT','TXN','UDR','V','WDC']

for t in tickers:
    if not os.path.exists(path + t):
        os.mkdir(path + t)

download_financials(tickers, path, startyear, endyear)
