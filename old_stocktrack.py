from pymongo import MongoClient
import yfinance as yf
import pandas as pd
import json
import matplotlib.pyplot as plt

client = MongoClient('mongodb://localhost:27017/')
db = client.UnhealthyPotato

stok = db.stok

ticker_list = ['AMD', 'INTC', 'NVDA']

def push_mongo(ticker_list):

    for ticker in ticker_list:

        for month in range(6, 11):

            data = yf.Ticker(ticker)
            df = data.history(start='2020-{}-1'.format(month), end='2020-{}-1'.format(month+1), interval='1d')

            close_price = list(df['Close'])
            open_price = list(df['Open'])
            daily_diff = []

            for i in range(len(close_price)):
                daily_diff.append( (close_price[i] - open_price[i]) / open_price[i])

            stok.insert_one({
                "ticker": ticker,
                "month": month,
                "close": close_price,
                "daily_change": daily_diff
            })


def get_month_data(ticker, month_id):
    q = stok.find({
        "ticker": "AMD",
        "month": month_id
    })

    data = q[0]['close']
    print(data)
    return data

period = []

for month in range(7, 10):
    data = get_month_data('AMD', month)

    for day in data:
        period.append(day)

print(len(period))
plt.plot(period)