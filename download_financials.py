import requests
import pandas as pd
from time import sleep

def get_req(url):
    try:
        a = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0'})
    except:
        sleep(3)
        a = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0'})
    return a

def download_financials(tickers, path, startyear, endyear):

    stocklist = pd.read_excel('Q://STONKS//stocks.xlsx', sheet_name='stock', converters={'CIK': str})
    ciks = []
    ticker_lookup = {}

    for t in tickers:
        cik = str(stocklist.loc[stocklist['Ticker'] == t]['CIK'].item())
        ciks.append(cik)
        ticker_lookup[cik] = t

    filings = []

    for year in range(startyear, endyear):
        for qtr in range(1,5):
            earl = f'https://www.sec.gov/Archives/edgar/full-index/{year}/QTR{qtr}/master.idx'
            download = str(get_req(earl).content)
            download = download.split('\\n')
            for item in download:
                if '10-Q' in item or '10-K' in item: 
                    for cik in ciks:
                        if item.split('|')[0] == cik:
                            filings.append(item)

    for f in filings:
        print(f) # f = '50863|INTEL CORP|10-Q|2019-04-26|edgar/data/50863/0000050863-19-000013.txt'

        s = f.split('|')

        cik = s[0]
        ticker = ticker_lookup[cik]
        company_name = s[1]
        filing_type = s[2].replace('/', '')
        filing_date = s[3]
        doc_num = s[4].split('/')[3].replace('.txt', '').replace('-', '')

        base = 'https://www.sec.gov/Archives/edgar/data/'
        url = base + cik + '/' + doc_num + '/Financial_Report.xlsx'
        a = get_req(url)

        filename = path + ticker + '/' + filing_date + '_' + filing_type + '.xlsx'
        with open(filename,'wb') as f:
            f.write(a.content)
