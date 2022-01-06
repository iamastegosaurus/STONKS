import requests
import pandas as pd
import bs4
import json
from time import sleep

def get_req(url):
    try:
        a = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0'})
    except: # code for actual error
        # HTTPSConnectionPool(host='www.sec.gov', port=443): Max retries exceeded with url: /Archives/edgar/data/50863/0000050863-17-000029.txt (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x00000251E220DE08>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))
        sleep(5)
        a = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0'})
    return a


filings = []

ticker = 'AMD'

companies = {
    'INTC': '50083',
    'AMD': '2488'
}

cik = companies[ticker]

for year in range(2018, 2019):
    for qtr in range(1,2):#5):
        earl = f'https://www.sec.gov/Archives/edgar/full-index/{year}/QTR{qtr}/master.idx'
        download = str(get_req(earl).content)
        download = download.split('\\n')
        for item in download:
            if '10-Q' in item or '10-K' in item: 
                if cik in item: # go through list of ciks later
                    filings.append(item)

base = 'https://www.sec.gov/Archives/'

for f in filings:
    print(f)
    cik = f.split('|')[0]
    company = f.split('|')[1]
    filing_type = f.split('|')[2]
    filing_date = f.split('|')[3]
    url = f.split('|')[4]

    req_url = base + url # https://www.sec.gov/Archives/edgar/data/50863/0000050863-20-000026.txt
    data = get_req(req_url).content
    data = data.decode("utf-8") 
    data = data.split('FILENAME>')
    data = data[1].split('\n')[0]
    url_to_use = 'https://www.sec.gov/Archives/'+ url.replace('.txt', '') + '/' + data # https://www.sec.gov/Archives/edgar/data/50863/0000050863-16-000105/a10kdocument12262015q4.htm
    url_to_use = url_to_use.replace('-', '')

    resp = get_req(req_url)
    soup = bs4.BeautifulSoup(resp.text, 'lxml')

    replace_chars = ',$—() '

    key_text = ['Net revenue', 'Current assets:', 'Net cash provided by operating activities']
    names = ['IncomeStatement', 'BalanceSheet', 'CashFlows']
    starting_indexes = [4, 3, 4]

    for s in range(3):
        data = {}
        table = soup.find(text=key_text[s]).find_parent("table")
        for row in table.findAll('tr')[starting_indexes[s]:]:

            try:

                item = row.find("ix:nonfraction").attrs['name']
                item = item.replace('us-gaap:','')
                value = row.find("ix:nonfraction").text
                try:
                    sign = row.find("ix:nonfraction")["sign"]
                except:
                    sign = ''
                for c in replace_chars:
                    value = value.replace(c, '')
                value = sign + value
            except:
                try:
                    val_changed = False
                    negative = False
                    for i, td in enumerate(row.findAll('td')):
                        if i < 5:
                            q = td.text
                            if i == 0:
                                item = q
                            
                            if '(' in q and ')' in q:
                                negative = True
                            for c in replace_chars:
                                q = q.replace(c, '')
                            
                            if q.replace('.', '').isdigit():
                                if negative == True:
                                    value = '-' + q
                                else:
                                    value = q
                                val_changed = True
                                break
                    if val_changed == False:
                        value = ''
                except:
                    continue

            data[item] = value

        df = pd.DataFrame(data, index=['Value']).T

        fil = 'Q://STONKS//' + ticker + '//' + filing_date + '_' + filing_type + '_'
        df.to_excel(fil + names[s] + '.xlsx')

