import pandas as pd
from pandas_datareader import data as pdr
from datetime import datetime

def download_prices(ticker, path, start, end):
    df = pdr.DataReader(ticker, 'yahoo', start, end)
    df.drop(['Volume', 'Open', 'Adj Close'], axis=1, inplace=True)
    df.rename(columns = {'High':'high', 'Low': 'low', 'Close':'close'}, inplace = True)
    df.index.rename('date', inplace=True)

    df['daily_return'] = (df['close'] / df['close'].shift(1)) - 1

    # cumulative 5 year
    # cumulative 1 year
    # cumulative 3 month

    df.to_csv('Q://STONKS//downloads//' + ticker + '//' + 'prices.csv')

    return df

