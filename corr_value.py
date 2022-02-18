import pandas as pd
from datetime import datetime
import numpy as np
today = datetime.now().date()

path = 'Q://STONKS//price_downloads//'

tickers = ['VOO','VOX','VCR','VDC','VDE','VFH','VHT','VIS','VGT','VAW','VNQ','VPU','BND','BNDX','BSV','BIV','BLV','VEA','VXUS'] 
periods = [10, 5, 3, 1]

res = pd.DataFrame()

for period in periods:
    period_ago = str(today.year - period) + '-' + str(today.month) + '-' + str(today.day)

    rf = 0
    returns = pd.DataFrame()

    for t in tickers:
        df = pd.read_csv(path + t + '/prices.csv', index_col = 0)
        returns[t] = df.loc[pd.to_datetime(df.index) > period_ago]['daily_return']

    sharpes = []

    for t in tickers:
        ret = returns[t].mean() * 250
        std = returns[t].std()

        sharpe = (ret - rf) / std
        sharpes.append(sharpe)

    sharpes = np.array(sharpes)

    corr = returns.corr()
    weighted_corr = 1 - corr*1.2

    corr_sharpe_factor = pd.DataFrame()
    for t in tickers:
        corr_sharpe_factor[t] = weighted_corr[t] * sharpes

    value = corr_sharpe_factor.sum(axis=1)
    res[period] = value

res['mean'] = res.mean(axis=1)
res.to_excel('Q://STONKS//value_result.xlsx')
