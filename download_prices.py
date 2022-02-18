import pandas as pd
from pandas_datareader import data as pdr
from helpers.get_str_date import get_str_date

def download_prices(ticker, path, today, period):

    # tenyearsago, fiveyearsago, oneyearago, threemonthsago = get_str_date(today, period)

    period_ago = str(today.year - period) + '-' + str(today.month) + '-' + str(today.day)

    # if period == 10:
    #     df = pdr.DataReader(ticker, 'yahoo', tenyearsago, today)
    # elif period == 5:
    #     df = pdr.DataReader(ticker, 'yahoo', fiveyearsago, today)
    # else:
    #     df = pdr.DataReader(ticker, 'yahoo', oneyearago, today)

    df = pdr.DataReader(ticker, 'yahoo', period_ago, today)
    df.drop(['Volume', 'Open', 'Adj Close'], axis=1, inplace=True)
    df.rename(columns = {'High':'high', 'Low': 'low', 'Close':'close'}, inplace = True)
    df.index.rename('date', inplace=True)
    df['daily_return'] = (df['close'] / df['close'].shift(1)) - 1

    # if period >= 10:
    #     df.loc[pd.to_datetime(df.index) > tenyearsago, 'tenyeardaily'] = df['daily_return']
    #     df['cum10year'] = (1 + df['tenyeardaily']).cumprod()
    #     df.drop(['tenyeardaily'], axis=1, inplace=True)

    # if period >= 5:
    #     df.loc[pd.to_datetime(df.index) > fiveyearsago, 'fiveyeardaily'] = df['daily_return']
    #     df['cum5year'] = (1 + df['fiveyeardaily']).cumprod()
    #     df.drop(['fiveyeardaily'], axis=1, inplace=True)

    # # periods always included
    # df.loc[pd.to_datetime(df.index) > oneyearago, 'oneyeardaily'] = df['daily_return']
    # df.loc[pd.to_datetime(df.index) > threemonthsago, 'threemonthdaily'] = df['daily_return']
    # df['cum1year'] = (1 + df['oneyeardaily']).cumprod()
    # df['cum3month'] = (1 + df['threemonthdaily']).cumprod()
    # df.drop(['oneyeardaily', 'threemonthdaily'], axis=1, inplace=True)
  
    df.to_csv(path + ticker + '//' + 'prices.csv')
    print(ticker)

    return df

