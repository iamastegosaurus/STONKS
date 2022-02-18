import os
from datetime import datetime
from download_prices import download_prices

path = 'Q://STONKS//price_downloads//'

period = 10
today = datetime.now().date()

tickers = ['VOO','VOX','VCR','VDC','VDE','VFH','VHT','VIS','VGT','VAW','VNQ','VPU','BND','BNDX','BSV','BIV','BLV','VEA','VXUS'] 

for t in tickers:
    if not os.path.exists(path + t):
        os.mkdir(path + t)
    download_prices(t, path, today, period)

