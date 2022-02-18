import pandas as pd
from datetime import datetime
import numpy as np
today = datetime.now().date()

path = 'Q://STONKS//price_downloads//'

tickers = ['VOO','VOX','VCR','VDC','VDE','VFH','VHT','VIS','VGT','VAW','VNQ','VPU','BND','BNDX','BSV','BIV','BLV','VEA','VXUS'] 
periods = [10, 5, 3, 1]
period = periods[0]
period_ago = str(today.year - period) + '-' + str(today.month) + '-' + str(today.day)

rf = 0
returns = pd.DataFrame()

for t in tickers:
    df = pd.read_csv(path + t + '/prices.csv', index_col = 0)
    returns[t] = df.loc[pd.to_datetime(df.index) > period_ago]['daily_return']

rets = []
stdev = [] 
sharpe = []
weights = [] 

for x in range(1000):
    if x % 1000 == 0:
        print(x)
    rand = np.random.random(len(tickers))
    norm = rand / np.sum(rand)

    ret = np.sum(norm * returns.mean()) * 250
    rets.append(ret)
    weights.append(norm)

    std = np.sqrt(np.dot(norm.T, np.dot(returns.cov() * 250, norm)))
    stdev.append(std)
    sharpe.append((ret - rf) / std)
 
ret = np.array(ret)
stdev = np.array(stdev)
sharpe = np.array(sharpe)
weights = np.array(weights)

bigshark = np.argmax(sharpe)
for w in weights[bigshark]:
    print(w)

print()
print(rets[bigshark])

