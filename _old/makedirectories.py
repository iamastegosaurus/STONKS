import os
import pandas as pd


stocklist = pd.read_excel('Q://STONKS//stocklist.xlsx', sheet_name='lista')
basepath = 'Q://STONKS//downloads//'

for q in range(stocklist.shape[0]):
    tick = stocklist.loc[q, 'Ticker']

    try:
        os.mkdir(basepath + tick)
    except:
        pass
