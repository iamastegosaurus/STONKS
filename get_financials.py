import pandas as pd
import os 

from testdate import get_date

def get_sheet_names(filepath):
    sheet_names = pd.ExcelFile(path + '/' + file, engine = 'openpyxl').sheet_names

    for s in sheet_names[0:7]:
        sheet = pd.read_excel(path + '/' + file, sheet_name = s)
        header = sheet.columns[0].lower().replace(' ', '')

        if ('income' in header) and ('comprehensive' not in header): # add or as necessary
            income_sheet_name = s
        elif ('balance' in header) and ('parenthetical' not in header):
            balance_sheet_name = s
        else:
            pass
    
    return income_sheet_name, balance_sheet_name


longtext = {
    'NR': 'Net revenue',
    'COGS': 'Cost of goods sold',
    'SGA': 'Selling, general, and administrative',
    'RND': 'Research and development',
    'OI': 'Operating income',
    'NI': 'Net income',
    'SHARES': 'Diluted common shares outstanding',

    'CCE': 'Cash and cash equivalents',
    'AR': 'Accounts receivable',
    'IN': 'Inventories',
    'TCA': 'Total current assets',
    'TA': 'Total assets'
}


def get_lookups(row):

    lookups = {
        'netrevenue': 'NR',
        'revenues': 'NR',
        'totalrevenue': 'NR',
        'netsales': 'NR',

        'costofsales': 'COGS',
        'merchandisecosts': 'COGS',
        'costofgoodssold': 'COGS',

        'marketinggeneralandadministrative': 'SGA',
        'sellinginformationalandadministrativeexpenses': 'SGA',
        'sellinggeneralandadministrative': 'SGA',
        'sellinggeneralandadministrativeexpenses': 'SGA',

        'researchanddevelopment': 'RND',
        'researchanddevelopmentexpenses': 'RND',
        'researchanddevelopmentexpense': 'RND',
        'researchanddevelopmentcosts': 'RND',

        'operatingincome': 'OI',

        'netincome': 'NI',
        'netincomeattributabletocompany': 'NI',
        'netearnings': 'NI',

        'dilutedshares': 'SHARES',
        'weightedaveragesharesdiluted': 'SHARES',
        'dilutedshares': 'SHARES',
        'diluted': 'SHARES',

        'cashandcashequivalents': 'CCE',

        'accountsreceivable': 'AR',
        'receivablesnet': 'AR',
        'accountsandnotesreceivablenet': 'AR',

        'inventories': 'IN',
        'merchandiseinventories': 'IN',

        'totalcurrentassets': 'TCA',
        'totalassets': 'TA',
    }

    fuzzylookups = {
        'cashandcashequivalents': 'cashandcashequivalents',
        'accountsreceivable': 'accountsreceivable',
        'netincomeattributableto': 'netincomeattributabletocompany',
    }

    avoid = { # values from fuzzylookups
        'netincomeattributabletocompany': ['less', 'share', 'stock', 'noncontrolling']
    }
    r = str(row).lower()
    replace_chars = [',', '(', ')', '.', '-', '–', ' ']
    for c in replace_chars:
        r = r.replace(c, '')
    if r in lookups.keys():
        return lookups[r]
    else:
        for fzy in fuzzylookups.keys():
            if fzy in r:
                if fuzzylookups[fzy] in avoid.keys():
                    for a in avoid[fuzzylookups[fzy]]:
                        if a in r:
                            return -1
                    return lookups[fuzzylookups[fzy]]

        return -1


path = 'Q:/STONKS/downloads/'

ticker = 'COST'

path = path + ticker
filings = [f for f in os.listdir(path) if '_10-' in f]

data = []
labels = ['filing_date', 'filing_type', 'period_type', 'period_ended']
for l in longtext.keys():
    labels.append(l)

for file in filings[2:3]:
    # file = filings[0]
    f = file.split('.')[0]

    filepath = path + '/' + file
    filing_date = f.split('_')[0]
    filing_type = f.split('_')[1]

    # ALL INCOME STATEMENT ONLY
    income_sheet_name, balance_sheet_name = get_sheet_names(filepath)

    df = pd.read_excel(filepath, sheet_name = income_sheet_name)

    newest_year = 2000
    newest_month = 1
    newest_date = ''

    for col in list(df.columns)[1:]:
        c = col.lower()
        if '3' in c and 'month' in c:
            period_type = '3-month'
        elif '12' in c and 'month' in c:
            period_type = '12-month'
        elif 'unnamed' in c:
            pass
        else:
            period_type = 'unknown'

        if str(df.loc[0, col]) != 'nan':
            period_date = get_date(df.loc[0, col])

            period_year = int(period_date.split('-')[0])
            period_month = int(period_date.split('-')[1])

            if period_year > newest_year:
                col_name = col
                newest_month = period_month
                newest_year = period_year
                newest_date = period_date

            elif period_month >= newest_month and period_year == newest_year:
                col_name = col
                newest_month = period_month
                newest_date = period_date
    period_date = newest_date

    rowheaders = list(df[df.columns[0]])
    fieldmap = {}
    datamap = {}

    for row in rowheaders:
        field = get_lookups(row)
        if field != -1:
            fieldmap[field] = row

            if field == 'SHARES':
                break

    income_sheet_name, balance_sheet_name = get_sheet_names(filepath)

    df = pd.read_excel(filepath, sheet_name = balance_sheet_name)

    for field in list(longtext.keys()):
        if field in fieldmap.keys():
            datamap[field] = df.loc[df[df.columns[0]] == fieldmap[field]][col_name].values[0]
        else:
            datamap[field] = ''

    line = [filing_date, filing_type, period_type, period_date]

    for d in datamap.keys():
        line.append(datamap[d])

    data.append(line)


res = pd.DataFrame(data, columns = labels)
res.to_excel(path + '/auto.xlsx', index=False)
