import pandas as pd
import datetime

tickers = ['AMD']

ticker = tickers[0]
# for ticker in tickers:

path = 'Q://STONKS//downloads//' + ticker
p = pd.read_csv(path + '//' + 'prices.csv')
f = pd.read_csv(path + '//' + 'financials.csv')

firstfilingdate = (list(f['DATE'])[-1])
p = p.loc[p['Date'] >= firstfilingdate].iloc[::-1]
p = p.reset_index(drop=True)

findex = 0
for i in range(0, p.shape[0]):
    fdate = f.loc[findex, 'DATE']

    if p.loc[i, 'Date'] < fdate:
        findex += 1

    p.loc[i, 'eps'] = f.loc[findex, 'EPS']
    p.loc[i, 'bvps'] = f.loc[findex, 'BVPS']
    p.loc[i, 'net income'] = f.loc[findex, 'NETINCOME']
    p.loc[i, 'book value'] = f.loc[findex, 'BV']
    p.loc[i, 'share count'] = f.loc[findex, 'SHARECT']
    p.loc[i, 'lastfilingdate'] = f.loc[findex, 'DATE']

    try:
        earnings = f.loc[findex, 'EPS'] + f.loc[findex+1, 'EPS'] + f.loc[findex+2, 'EPS'] + f.loc[findex+3, 'EPS']
        p.loc[i, 'trailing 4 qtr earnings per share'] = earnings
        p.loc[i, 'P/E'] = p.loc[i, 'Close'] / earnings
    except:
        pass

    p.loc[i, 'P/B'] = p.loc[i, 'Adj Close'] / f.loc[findex, 'BVPS']

p['dailyreturn'] = (p['Close'] / p['Close'].shift(1)) - 1

p.to_excel('Q://STONKS//downloads//' + ticker + '//' + 'combined.xlsx', index=False)


