import requests
import pandas as pd
from time import sleep

def df_handler(filepath, sheet_name):
    df = pd.read_excel(filepath, engine = 'openpyxl', sheet_name = s)
    unnamed = []
    rename = {}
    for i, col in enumerate(df.columns):
        c = col.lower()
        if i == 0:
            rename[col] = 'words'
        elif 'unnamed' in c:
            unnamed.append(col)
        elif '3' in c and 'month' in c:
            rename[col] = '3-month'
        elif '6' in c and 'month' in c:
            rename[col] = '6-month'
        elif '9' in c and 'month' in c:
            rename[col] = '9-month'
        elif '12' in c and 'month' in c:
            rename[col] = '12-month'
    df.rename(columns = rename, inplace = True)
    df.drop(unnamed, axis=1, inplace=True)
    return df

def get_req(url):
    try:
        a = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0'})
    except: # code for actual error
        # HTTPSConnectionPool(host='www.sec.gov', port=443): Max retries exceeded with url: /Archives/edgar/data/50863/0000050863-17-000029.txt (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x00000251E220DE08>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))
        sleep(5)
        a = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0'})
    return a

stocklist = pd.read_excel('Q://STONKS//stocklist.xlsx', sheet_name='lista', converters={'CIK': str})

cik_list = []
ticker_lookup = {}
tickers = list(stocklist['Ticker'])

tickers = ['RTX']

for t in tickers:
    cik = str(stocklist.loc[stocklist['Ticker'] == t]['CIK'].item())
    cik_list.append(cik)
    ticker_lookup[cik] = t


filings = []
# year = 2015
# qtr = 3
for year in range(2016, 2022):
    for qtr in range(1,5):
        earl = f'https://www.sec.gov/Archives/edgar/full-index/{year}/QTR{qtr}/master.idx'
        download = str(get_req(earl).content)
        download = download.split('\\n')
        for item in download:
            if '10-Q' in item or '10-K' in item: 
                for cik in cik_list:
                    if item.split('|')[0] == cik:
                        filings.append(item)

for f in filings:
    print(f) # f = '50863|INTEL CORP|10-Q|2019-04-26|edgar/data/50863/0000050863-19-000013.txt'
    if '/A' in f:
        continue

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

    filename = 'Q://STONKS//downloads//' + ticker + '/' + filing_date + '_' + filing_type + '.xlsx'
    meta = [[company_name, ticker, cik, filing_date, filing_type, url]]
    meta = pd.DataFrame(meta, columns=['NAME', 'TICKER', 'CIK', 'DATE', 'TYPE', 'URL'])
    with open(filename,'wb') as f:
        f.write(a.content)

    # try:
        sheet_names = pd.ExcelFile(filename, engine = 'openpyxl').sheet_names

        for s in sheet_names[1:10]:
            tmpdf = pd.read_excel(filename, engine = 'openpyxl', sheet_name=s)
            n = tmpdf.columns[0].lower()

            if 'comprehensive' in n or 'parenthetical' in n:
                pass
            else:
                if 'statement' in n and ('income' in n or 'operation' in n or 'earning' in n):
                    # income_statement = pd.read_excel(filename, engine = 'openpyxl', sheet_name=s)
                    income_statement = df_handler(filename, s)
                elif 'balance' in n and 'sheet' in n:
                    # balance_sheet = pd.read_excel(filename, engine = 'openpyxl', sheet_name=s)
                    balance_sheet = df_handler(filename, s)
                elif 'cash' in n and 'flow' in n:
                    # cash_flows = pd.read_excel(filename, engine = 'openpyxl', sheet_name=s)
                    cash_flows = df_handler(filename, s)
                    break

        writer = pd.ExcelWriter(filename)
        income_statement.to_excel(writer, 'IncomeStatement', index=False)
        balance_sheet.to_excel(writer, 'BalanceSheet', index=False)
        cash_flows.to_excel(writer, 'CashFlows', index=False)
        meta.to_excel(writer, 'META', index=False)
        writer.save()

    # except: 
    #     print('amendment or similar - invalid xlsx?')

# interactive data
# https://www.sec.gov/cgi-bin/viewer?action=view&cik=50863&accession_number=0000050863-19-000013&xbrl_type=v
