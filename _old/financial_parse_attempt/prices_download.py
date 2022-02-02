import pandas as pd
from pandas_datareader import data as pdr
import datetime
from time import sleep

start = datetime.datetime(2016, 1, 1)
end = datetime.datetime(2021, 12, 31)

failed_stocks = []

def get_yahoo(ticker, start, end):
    df = pdr.DataReader(ticker, 'yahoo', start, end)
    try:
        if df.shape[0] > 69:
            return df, 'ok'
        else:
            return 'fail', 'fail'
    except:
        return 'fail', 'fail'

stocklist = pd.read_excel('Q://STONKS//stocklist.xlsx', sheet_name='lista')
tickers = list(stocklist['Ticker'])

tickers = ['RTX']

for ticker in tickers:
    print(ticker)
    df, status = get_yahoo(ticker, start, end)    

    if status == 'ok':
        df.to_csv('Q://STONKS//downloads//' + ticker + '//' + 'prices.csv')
    elif status == 'fail':
        failed_stocks.append(ticker)

print('failed stocks: ', failed_stocks)