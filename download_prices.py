import pandas as pd
from pandas_datareader import data as pdr
from datetime import datetime
import numpy as np

def download_prices(ticker, path, start, end):
    df = pdr.DataReader(ticker, 'yahoo', start, end)
    df.drop(['Volume', 'Open', 'Adj Close'], axis=1, inplace=True)
    df.rename(columns = {'High':'high', 'Low': 'low', 'Close':'close'}, inplace = True)
    df.index.rename('date', inplace=True)
    df['daily_return'] = (df['close'] / df['close'].shift(1)) - 1

    cum5year = str(end.year - 5) + '-' + str(end.month) + '-' + str(end.day)
    cum1year = str(end.year - 1) + '-' + str(end.month) + '-' + str(end.day)


    if end.month <= 3:
        cum3month = str(end.year - 1) + '-' + str(13 - end.month) + '-' + str(end.day)
    else:
        cum3month = str(end.year) + '-' + str(end.month - 3) + '-' + str(end.day)
  

    df.loc[pd.to_datetime(df.index) > cum5year, 'fiveyeardaily'] = df['daily_return']
    df.loc[pd.to_datetime(df.index) > cum1year, 'oneyeardaily'] = df['daily_return']
    df.loc[pd.to_datetime(df.index) > cum3month, 'threemonthdaily'] = df['daily_return']

    df['cum5year'] = (1 + df['fiveyeardaily']).cumprod()
    df['cum1year'] = (1 + df['oneyeardaily']).cumprod()
    df['cum3month'] = (1 + df['threemonthdaily']).cumprod()

    df.drop(['fiveyeardaily', 'oneyeardaily', 'threemonthdaily'], axis=1, inplace=True)
  
    df.to_csv(path + ticker + '//' + 'prices.csv')

    return df

